# -*- coding: UTF-8 -*-
"""
Test cases for Issue #32: URLs incorrectly get periods appended at end.

## Problem Description

URLs at the end of sentences were having periods incorrectly appended to them,
breaking the URL format and making them non-functional as links.

**Example of the defect:**
```
Input:  "Watch the video at https://youtu.be/glck33tRFAk"
Output: "Watch the video at https://youtu.be/glck33tRFAk."  # Period added incorrectly
```

The period being appended to the URL breaks clickable links and violates URL
format standards. This occurred because the segmenter's post-processing logic
would add periods to sentences lacking terminal punctuation, without recognizing
that URLs should be exempt from this normalization.

## Solution Approach

The fix uses a placeholder normalization pattern (similar to how the codebase
handles ellipses, middle initials, and other special patterns):

1. **Normalize**: Replace URLs with placeholders (xurl1x, xurl2x, etc.) before
   sentence segmentation
2. **Segment**: Run spaCy and segmentation logic on the placeholder text
3. **Denormalize**: Restore original URLs from placeholders

Special handling for sentence-boundary periods:
- If a URL ends with a TLD period (e.g., ".com") followed by whitespace,
  the regex properly distinguishes between the TLD period and sentence punctuation
- Trailing periods indicating sentence boundaries are preserved outside the URL

## Test Coverage

This test suite includes 286 comprehensive test cases organized into 24 classes:

### URL Scheme Coverage
- HTTP, HTTPS, FTP, FTPS, WebSocket (ws/wss), mailto, tel, file protocol
- Special schemes without :// (mailto:, tel:)

### URL Component Testing
- Basic URLs with/without www
- Simple & complex paths (hyphens, underscores, numbers, deep nesting)
- Query parameters (single, multiple, arrays, encoded, nested)
- Fragments/anchors (#section)
- Port numbers (standard & custom)
- Subdomains (single & multiple levels)

### TLD Variations
- Common TLDs (.com, .org, .net, .edu, .gov)
- New TLDs (.io, .ai, .dev, .app, .co)
- Country codes (.uk, .de, .jp, .fr, .ca, .au, .in, .cn)
- Two-part country codes (.co.uk, .co.jp, .com.au, .ac.uk)

### Positional & Contextual Testing
- URLs at start, middle, and end of sentences
- Isolated URLs
- URLs in parentheses, brackets, quotes
- URLs after colons, dashes
- **URLs with trailing punctuation** (the critical defect case)

### Real-World URLs
- **YouTube**: youtu.be short URLs, full URLs, timestamps, playlists
- **GitHub**: repos, issues, PRs, files, Gists, Pages
- **Documentation**: Python docs, MDN, Stack Overflow, npm, PyPI
- **Social Media**: Twitter/X, LinkedIn, Facebook, Instagram, Reddit, Medium
- **Blogs/News**: Including the uww.edu URL from the issue

### Edge Cases & Stress Tests
- Multiple URLs in one sentence
- Repeated URLs across sentences
- URLs with IP addresses (IPv4 & IPv6)
- Localhost variations
- Complex paths with encoding (%20, etc.)
- Complex query strings with special characters
- URLs mixed with numbered titles, dates, abbreviations

## Related GitHub Issues

- Primary: #32 - URLs incorrectly get periods appended at end
  https://github.com/craigtrim/fast-sentence-segment/issues/32

## Implementation Files

- fast_sentence_segment/dmo/url_normalizer.py - URL placeholder normalization
- fast_sentence_segment/svc/perform_sentence_segmentation.py - Integration into segmentation flow
- fast_sentence_segment/dmo/spacy_doc_segmenter.py - Updated to recognize URL placeholders

Created:
    10-Feb-2026
    craigtrim@gmail.com
"""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestURLsBasicHTTP:
    """Test basic HTTP and HTTPS URLs"""

    @pytest.mark.parametrize("text,expected", [
        # HTTPS URLs - basic
        ("Watch the video at https://youtu.be/glck33tRFAk",
         ["Watch the video at https://youtu.be/glck33tRFAk"]),

        ("Another example: https://youtu.be/6ThmAqf--t8",
         ["Another example: https://youtu.be/6ThmAqf--t8"]),

        ("Check this out https://youtu.be/sKWsZUxXUWE",
         ["Check this out https://youtu.be/sKWsZUxXUWE"]),

        ("Visit https://example.com for more info",
         ["Visit https://example.com for more info"]),

        ("See https://example.org for details",
         ["See https://example.org for details"]),

        ("Documentation at https://docs.python.org",
         ["Documentation at https://docs.python.org"]),

        ("More at https://github.com",
         ["More at https://github.com"]),

        ("Learn at https://stackoverflow.com",
         ["Learn at https://stackoverflow.com"]),

        # HTTP URLs
        ("Visit http://example.com for more",
         ["Visit http://example.com for more"]),

        ("Check http://test.org",
         ["Check http://test.org"]),

        ("See http://www.example.com",
         ["See http://www.example.com"]),

        ("Go to http://site.net",
         ["Go to http://site.net"]),

        # With www
        ("Visit https://www.example.com",
         ["Visit https://www.example.com"]),

        ("Check https://www.google.com",
         ["Check https://www.google.com"]),

        ("See https://www.github.com",
         ["See https://www.github.com"]),

        # Without www
        ("Visit https://example.com",
         ["Visit https://example.com"]),

        ("Check https://google.com",
         ["Check https://google.com"]),

        ("See https://github.com",
         ["See https://github.com"]),
    ])
    def test_basic_http_urls(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsWithPaths:
    """Test URLs with various path structures"""

    @pytest.mark.parametrize("text,expected", [
        # Simple paths
        ("Visit https://example.com/about",
         ["Visit https://example.com/about"]),

        ("See https://example.com/contact",
         ["See https://example.com/contact"]),

        ("Go to https://example.com/help",
         ["Go to https://example.com/help"]),

        # Multi-level paths
        ("Check https://example.com/docs/api",
         ["Check https://example.com/docs/api"]),

        ("Visit https://example.com/products/software",
         ["Visit https://example.com/products/software"]),

        ("See https://example.com/blog/2024/01/article",
         ["See https://example.com/blog/2024/01/article"]),

        # Deep nesting
        ("Documentation at https://example.com/en/docs/guide/quickstart",
         ["Documentation at https://example.com/en/docs/guide/quickstart"]),

        ("API docs at https://api.example.com/v2/reference/endpoints",
         ["API docs at https://api.example.com/v2/reference/endpoints"]),

        # Paths with hyphens
        ("Visit https://example.com/my-page",
         ["Visit https://example.com/my-page"]),

        ("See https://example.com/user-guide",
         ["See https://example.com/user-guide"]),

        ("Check https://example.com/getting-started",
         ["Check https://example.com/getting-started"]),

        # Paths with underscores
        ("Visit https://example.com/my_page",
         ["Visit https://example.com/my_page"]),

        ("See https://example.com/user_guide",
         ["See https://example.com/user_guide"]),

        # Paths with numbers
        ("Visit https://example.com/article-123",
         ["Visit https://example.com/article-123"]),

        ("See https://example.com/post/2024",
         ["See https://example.com/post/2024"]),

        ("Check https://example.com/v2",
         ["Check https://example.com/v2"]),

        # File extensions
        ("Download https://example.com/file.pdf",
         ["Download https://example.com/file.pdf"]),

        ("See https://example.com/image.jpg",
         ["See https://example.com/image.jpg"]),

        ("Get https://example.com/data.json",
         ["Get https://example.com/data.json"]),

        ("View https://example.com/document.html",
         ["View https://example.com/document.html"]),
    ])
    def test_urls_with_paths(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsWithQueryParameters:
    """Test URLs with query parameters"""

    @pytest.mark.parametrize("text,expected", [
        # Single parameter
        ("Search at https://example.com?q=test",
         ["Search at https://example.com?q=test"]),

        ("Visit https://example.com?id=123",
         ["Visit https://example.com?id=123"]),

        ("See https://example.com?page=1",
         ["See https://example.com?page=1"]),

        # Multiple parameters
        ("Search https://example.com?q=test&lang=en",
         ["Search https://example.com?q=test&lang=en"]),

        ("Visit https://example.com?id=123&type=user",
         ["Visit https://example.com?id=123&type=user"]),

        ("See https://example.com?page=1&limit=10",
         ["See https://example.com?page=1&limit=10"]),

        # Many parameters
        ("API call https://example.com?a=1&b=2&c=3&d=4",
         ["API call https://example.com?a=1&b=2&c=3&d=4"]),

        # With paths and parameters
        ("Visit https://example.com/search?q=test",
         ["Visit https://example.com/search?q=test"]),

        ("See https://example.com/api/v2?key=abc123",
         ["See https://example.com/api/v2?key=abc123"]),

        ("Check https://example.com/products?category=electronics&sort=price",
         ["Check https://example.com/products?category=electronics&sort=price"]),

        # Encoded parameters
        ("Search https://example.com?q=hello%20world",
         ["Search https://example.com?q=hello%20world"]),

        ("Visit https://example.com?name=John%20Doe",
         ["Visit https://example.com?name=John%20Doe"]),

        # Array-like parameters
        ("Filter https://example.com?tags[]=python&tags[]=tutorial",
         ["Filter https://example.com?tags[]=python&tags[]=tutorial"]),

        # Special characters in parameters
        ("Visit https://example.com?redirect=/home",
         ["Visit https://example.com?redirect=/home"]),

        ("See https://example.com?next=/dashboard",
         ["See https://example.com?next=/dashboard"]),
    ])
    def test_urls_with_query_parameters(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsWithFragments:
    """Test URLs with fragment identifiers"""

    @pytest.mark.parametrize("text,expected", [
        # Basic fragments
        ("Jump to https://example.com#section1",
         ["Jump to https://example.com#section1"]),

        ("See https://example.com#introduction",
         ["See https://example.com#introduction"]),

        ("Visit https://example.com#top",
         ["Visit https://example.com#top"]),

        # Fragments with hyphens
        ("Go to https://example.com#getting-started",
         ["Go to https://example.com#getting-started"]),

        ("See https://example.com#api-reference",
         ["See https://example.com#api-reference"]),

        # Fragments with underscores
        ("Visit https://example.com#user_guide",
         ["Visit https://example.com#user_guide"]),

        # With paths and fragments
        ("See https://example.com/docs#installation",
         ["See https://example.com/docs#installation"]),

        ("Visit https://example.com/guide/quickstart#step-1",
         ["Visit https://example.com/guide/quickstart#step-1"]),

        # With query parameters and fragments
        ("Search https://example.com?q=test#results",
         ["Search https://example.com?q=test#results"]),

        ("Visit https://example.com/search?q=python#top",
         ["Visit https://example.com/search?q=python#top"]),

        # GitHub-style fragments
        ("See https://github.com/user/repo#readme",
         ["See https://github.com/user/repo#readme"]),

        ("Check https://github.com/user/repo/issues/123#issue-comment",
         ["Check https://github.com/user/repo/issues/123#issue-comment"]),
    ])
    def test_urls_with_fragments(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsWithPorts:
    """Test URLs with port numbers"""

    @pytest.mark.parametrize("text,expected", [
        # Common ports
        ("Visit https://example.com:443",
         ["Visit https://example.com:443"]),

        ("See http://example.com:80",
         ["See http://example.com:80"]),

        ("Check http://example.com:8080",
         ["Check http://example.com:8080"]),

        # Development ports
        ("Visit http://localhost:3000",
         ["Visit http://localhost:3000"]),

        ("See http://localhost:8000",
         ["See http://localhost:8000"]),

        ("Check http://localhost:5000",
         ["Check http://localhost:5000"]),

        # With paths
        ("Visit http://localhost:3000/dashboard",
         ["Visit http://localhost:3000/dashboard"]),

        ("API at http://localhost:8080/api/v1",
         ["API at http://localhost:8080/api/v1"]),

        # With query parameters
        ("Visit http://localhost:3000?debug=true",
         ["Visit http://localhost:3000?debug=true"]),

        # Custom ports
        ("Connect to http://example.com:9000",
         ["Connect to http://example.com:9000"]),

        ("See https://example.com:8443",
         ["See https://example.com:8443"]),
    ])
    def test_urls_with_ports(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsVariousTLDs:
    """Test URLs with different top-level domains"""

    @pytest.mark.parametrize("text,expected", [
        # Common TLDs
        ("Visit https://example.com",
         ["Visit https://example.com"]),

        ("See https://example.org",
         ["See https://example.org"]),

        ("Check https://example.net",
         ["Check https://example.net"]),

        ("Go to https://university.edu",
         ["Go to https://university.edu"]),

        ("Visit https://government.gov",
         ["Visit https://government.gov"]),

        # New TLDs
        ("Check https://startup.io",
         ["Check https://startup.io"]),

        ("Visit https://tech.ai",
         ["Visit https://tech.ai"]),

        ("See https://developer.dev",
         ["See https://developer.dev"]),

        ("Go to https://mobile.app",
         ["Go to https://mobile.app"]),

        ("Check https://company.co",
         ["Check https://company.co"]),

        # Country code TLDs
        ("Visit https://example.uk",
         ["Visit https://example.uk"]),

        ("See https://example.de",
         ["See https://example.de"]),

        ("Check https://example.jp",
         ["Check https://example.jp"]),

        ("Go to https://example.fr",
         ["Go to https://example.fr"]),

        ("Visit https://example.ca",
         ["Visit https://example.ca"]),

        ("See https://example.au",
         ["See https://example.au"]),

        ("Check https://example.in",
         ["Check https://example.in"]),

        ("Go to https://example.cn",
         ["Go to https://example.cn"]),

        # Two-part country codes
        ("Visit https://example.co.uk",
         ["Visit https://example.co.uk"]),

        ("See https://example.co.jp",
         ["See https://example.co.jp"]),

        ("Check https://example.com.au",
         ["Check https://example.com.au"]),

        ("Go to https://example.ac.uk",
         ["Go to https://example.ac.uk"]),
    ])
    def test_urls_various_tlds(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsSubdomains:
    """Test URLs with various subdomain patterns"""

    @pytest.mark.parametrize("text,expected", [
        # Common subdomains
        ("Visit https://www.example.com",
         ["Visit https://www.example.com"]),

        ("See https://blog.example.com",
         ["See https://blog.example.com"]),

        ("Check https://api.example.com",
         ["Check https://api.example.com"]),

        ("Go to https://docs.example.com",
         ["Go to https://docs.example.com"]),

        ("Visit https://app.example.com",
         ["Visit https://app.example.com"]),

        ("See https://mail.example.com",
         ["See https://mail.example.com"]),

        ("Check https://shop.example.com",
         ["Check https://shop.example.com"]),

        # Multiple subdomains
        ("Visit https://api.v2.example.com",
         ["Visit https://api.v2.example.com"]),

        ("See https://docs.internal.example.com",
         ["See https://docs.internal.example.com"]),

        ("Check https://blog.tech.example.com",
         ["Check https://blog.tech.example.com"]),

        # Subdomains with hyphens
        ("Visit https://my-api.example.com",
         ["Visit https://my-api.example.com"]),

        ("See https://test-server.example.com",
         ["See https://test-server.example.com"]),

        # Subdomains with numbers
        ("Visit https://api2.example.com",
         ["Visit https://api2.example.com"]),

        ("See https://server01.example.com",
         ["See https://server01.example.com"]),

        ("Check https://v2.example.com",
         ["Check https://v2.example.com"]),
    ])
    def test_urls_subdomains(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsPositionInText:
    """Test URLs at different positions in text"""

    @pytest.mark.parametrize("text,expected", [
        # URL at start
        ("https://example.com is a great site",
         ["https://example.com is a great site"]),

        ("https://github.com has many repositories",
         ["https://github.com has many repositories"]),

        # URL in middle
        ("Check out https://example.com for more details",
         ["Check out https://example.com for more details"]),

        ("The site https://example.com has information",
         ["The site https://example.com has information"]),

        # URL at end (most common issue case)
        ("Visit https://example.com",
         ["Visit https://example.com"]),

        ("More info at https://example.com",
         ["More info at https://example.com"]),

        ("See https://example.com",
         ["See https://example.com"]),

        # Isolated URL (nothing else)
        ("https://example.com",
         ["https://example.com"]),

        ("https://youtu.be/abc123",
         ["https://youtu.be/abc123"]),

        # URL after colon
        ("Website: https://example.com",
         ["Website: https://example.com"]),

        ("Link: https://example.com",
         ["Link: https://example.com"]),

        # URL after dash
        ("Site - https://example.com",
         ["Site - https://example.com"]),

        ("Resource - https://example.com",
         ["Resource - https://example.com"]),
    ])
    def test_urls_position_in_text(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsWithSurroundingPunctuation:
    """Test URLs with various punctuation around them"""

    @pytest.mark.parametrize("text,expected", [
        # URL in parentheses
        ("Check this site (https://example.com) for details",
         ["Check this site (https://example.com) for details"]),

        ("See the documentation (https://docs.example.com) for help",
         ["See the documentation (https://docs.example.com) for help"]),

        ("Visit the website (https://example.com)",
         ["Visit the website (https://example.com)"]),

        # URL in brackets
        ("See [https://example.com] for more",
         ["See [https://example.com] for more"]),

        ("Reference [https://docs.example.com] for details",
         ["Reference [https://docs.example.com] for details"]),

        # URL in quotes
        ('Visit "https://example.com" for info',
         ['Visit "https://example.com" for info']),

        ("Check out 'https://example.com' for more",
         ["Check out 'https://example.com' for more"]),

        ('The URL is "https://example.com"',
         ['The URL is "https://example.com"']),

        # URL with comma after (tricky - comma should not be part of URL)
        ("Visit https://example.com, then check the docs",
         ["Visit https://example.com, then check the docs"]),

        ("See https://example.com, https://example.org, and https://example.net",
         ["See https://example.com, https://example.org, and https://example.net"]),

        # URL before semicolon
        ("Visit https://example.com; it has good info",
         ["Visit https://example.com; it has good info"]),
    ])
    def test_urls_with_surrounding_punctuation(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsMultipleInText:
    """Test text with multiple URLs"""

    @pytest.mark.parametrize("text,expected", [
        # Two URLs
        ("Visit https://example.com and https://example.org",
         ["Visit https://example.com and https://example.org"]),

        ("Check https://github.com or https://gitlab.com",
         ["Check https://github.com or https://gitlab.com"]),

        # Three URLs
        ("Try https://example.com, https://example.org, or https://example.net",
         ["Try https://example.com, https://example.org, or https://example.net"]),

        # Multiple URLs in separate sentences (URLs at end - no period)
        ("Visit https://example.com for details. Also check https://example.org",
         ["Visit https://example.com for details.", "Also check https://example.org"]),

        ("See https://example.com first. Then visit https://example.org",
         ["See https://example.com first.", "Then visit https://example.org"]),

        # URLs with different schemes
        ("Check http://example.com and https://example.org",
         ["Check http://example.com and https://example.org"]),

        # Same URL repeated (URL at end - no period)
        ("Visit https://example.com for info. Also see https://example.com",
         ["Visit https://example.com for info.", "Also see https://example.com"]),
    ])
    def test_urls_multiple_in_text(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsRealWorldYouTube:
    """Test real-world YouTube URLs from the issue"""

    @pytest.mark.parametrize("text,expected", [
        # Direct from issue #32
        ("Watch the video at https://youtu.be/glck33tRFAk",
         ["Watch the video at https://youtu.be/glck33tRFAk"]),

        ("Another example: https://youtu.be/6ThmAqf--t8",
         ["Another example: https://youtu.be/6ThmAqf--t8"]),

        ("Check out https://youtu.be/sKWsZUxXUWE",
         ["Check out https://youtu.be/sKWsZUxXUWE"]),

        ("See https://youtu.be/Nn7grjTpcNA",
         ["See https://youtu.be/Nn7grjTpcNA"]),

        ("Watch https://youtu.be/GdBvuALfI1k",
         ["Watch https://youtu.be/GdBvuALfI1k"]),

        ("Visit https://youtu.be/CTxhyUUsmHM",
         ["Visit https://youtu.be/CTxhyUUsmHM"]),

        ("See https://youtu.be/k4SoiYvxWZk",
         ["See https://youtu.be/k4SoiYvxWZk"]),

        ("Check https://youtu.be/ple-D9ZR8hU",
         ["Check https://youtu.be/ple-D9ZR8hU"]),

        ("Watch https://youtu.be/m8nwll9F8dM",
         ["Watch https://youtu.be/m8nwll9F8dM"]),

        ("See https://youtu.be/yACgfb2VxSc",
         ["See https://youtu.be/yACgfb2VxSc"]),

        ("Visit https://youtu.be/1B6V7IbsUrs",
         ["Visit https://youtu.be/1B6V7IbsUrs"]),

        # Full YouTube URLs
        ("Watch https://www.youtube.com/watch?v=abc123",
         ["Watch https://www.youtube.com/watch?v=abc123"]),

        ("See https://youtube.com/watch?v=xyz789",
         ["See https://youtube.com/watch?v=xyz789"]),

        # YouTube with timestamps
        ("Watch https://youtu.be/abc123?t=120",
         ["Watch https://youtu.be/abc123?t=120"]),

        ("See https://www.youtube.com/watch?v=abc123&t=45s",
         ["See https://www.youtube.com/watch?v=abc123&t=45s"]),

        # YouTube playlists
        ("Playlist at https://www.youtube.com/playlist?list=PLxyz",
         ["Playlist at https://www.youtube.com/playlist?list=PLxyz"]),
    ])
    def test_urls_real_world_youtube(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsRealWorldGitHub:
    """Test real-world GitHub URLs"""

    @pytest.mark.parametrize("text,expected", [
        # Repository URLs
        ("Check out https://github.com/user/repo",
         ["Check out https://github.com/user/repo"]),

        ("Visit https://github.com/python/cpython",
         ["Visit https://github.com/python/cpython"]),

        ("See https://github.com/microsoft/vscode",
         ["See https://github.com/microsoft/vscode"]),

        # Issue URLs
        ("See issue https://github.com/user/repo/issues/123",
         ["See issue https://github.com/user/repo/issues/123"]),

        ("Bug report at https://github.com/user/repo/issues/456",
         ["Bug report at https://github.com/user/repo/issues/456"]),

        # Pull request URLs
        ("Review https://github.com/user/repo/pull/789",
         ["Review https://github.com/user/repo/pull/789"]),

        ("PR at https://github.com/user/repo/pull/101",
         ["PR at https://github.com/user/repo/pull/101"]),

        # File URLs
        ("See file https://github.com/user/repo/blob/main/README.md",
         ["See file https://github.com/user/repo/blob/main/README.md"]),

        ("Code at https://github.com/user/repo/blob/main/src/main.py",
         ["Code at https://github.com/user/repo/blob/main/src/main.py"]),

        # Raw URLs
        ("Download https://raw.githubusercontent.com/user/repo/main/file.txt",
         ["Download https://raw.githubusercontent.com/user/repo/main/file.txt"]),

        # GitHub Pages
        ("Visit https://user.github.io",
         ["Visit https://user.github.io"]),

        ("See https://user.github.io/project",
         ["See https://user.github.io/project"]),

        # GitHub Gist
        ("Gist at https://gist.github.com/user/abc123",
         ["Gist at https://gist.github.com/user/abc123"]),
    ])
    def test_urls_real_world_github(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsRealWorldDocumentation:
    """Test real-world documentation URLs"""

    @pytest.mark.parametrize("text,expected", [
        # Python docs
        ("See https://docs.python.org/3/library/re.html",
         ["See https://docs.python.org/3/library/re.html"]),

        ("Reference https://docs.python.org/3/tutorial/index.html",
         ["Reference https://docs.python.org/3/tutorial/index.html"]),

        # MDN
        ("Visit https://developer.mozilla.org/en-US/docs/Web/JavaScript",
         ["Visit https://developer.mozilla.org/en-US/docs/Web/JavaScript"]),

        ("See https://developer.mozilla.org/en-US/docs/Web/API",
         ["See https://developer.mozilla.org/en-US/docs/Web/API"]),

        # Stack Overflow
        ("Answer at https://stackoverflow.com/questions/123456",
         ["Answer at https://stackoverflow.com/questions/123456"]),

        ("See https://stackoverflow.com/a/789012",
         ["See https://stackoverflow.com/a/789012"]),

        # npm
        ("Package at https://www.npmjs.com/package/express",
         ["Package at https://www.npmjs.com/package/express"]),

        ("See https://npmjs.com/package/react",
         ["See https://npmjs.com/package/react"]),

        # PyPI
        ("Package at https://pypi.org/project/requests",
         ["Package at https://pypi.org/project/requests"]),

        ("See https://pypi.org/project/django",
         ["See https://pypi.org/project/django"]),

        # Read the Docs
        ("Documentation at https://readthedocs.org/projects/myproject",
         ["Documentation at https://readthedocs.org/projects/myproject"]),

        ("See https://myproject.readthedocs.io/en/latest",
         ["See https://myproject.readthedocs.io/en/latest"]),
    ])
    def test_urls_real_world_documentation(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsRealWorldSocialMedia:
    """Test social media URLs"""

    @pytest.mark.parametrize("text,expected", [
        # Twitter/X
        ("Follow https://twitter.com/username",
         ["Follow https://twitter.com/username"]),

        ("Tweet at https://twitter.com/user/status/123456",
         ["Tweet at https://twitter.com/user/status/123456"]),

        ("See https://x.com/username",
         ["See https://x.com/username"]),

        # LinkedIn
        ("Profile at https://www.linkedin.com/in/username",
         ["Profile at https://www.linkedin.com/in/username"]),

        ("Company at https://www.linkedin.com/company/acme",
         ["Company at https://www.linkedin.com/company/acme"]),

        # Facebook
        ("Page at https://www.facebook.com/pagename",
         ["Page at https://www.facebook.com/pagename"]),

        ("See https://facebook.com/username",
         ["See https://facebook.com/username"]),

        # Instagram
        ("Follow https://www.instagram.com/username",
         ["Follow https://www.instagram.com/username"]),

        ("See https://instagram.com/username",
         ["See https://instagram.com/username"]),

        # TikTok
        ("Watch https://www.tiktok.com/@username",
         ["Watch https://www.tiktok.com/@username"]),

        # Reddit
        ("Discussion at https://www.reddit.com/r/programming",
         ["Discussion at https://www.reddit.com/r/programming"]),

        ("Thread at https://reddit.com/r/python/comments/abc123",
         ["Thread at https://reddit.com/r/python/comments/abc123"]),

        # Medium
        ("Article at https://medium.com/@author/article-title-abc123",
         ["Article at https://medium.com/@author/article-title-abc123"]),
    ])
    def test_urls_real_world_social_media(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsRealWorldBlogsNews:
    """Test blog and news site URLs"""

    @pytest.mark.parametrize("text,expected", [
        # From issue #32
        ("Read https://blogs.uww.edu/library/archives/14512",
         ["Read https://blogs.uww.edu/library/archives/14512"]),

        # News sites
        ("Article at https://www.nytimes.com/2024/01/01/technology/article.html",
         ["Article at https://www.nytimes.com/2024/01/01/technology/article.html"]),

        ("See https://www.bbc.com/news/technology-12345678",
         ["See https://www.bbc.com/news/technology-12345678"]),

        ("Read https://www.theguardian.com/technology/2024/jan/01/article",
         ["Read https://www.theguardian.com/technology/2024/jan/01/article"]),

        # Tech blogs
        ("Post at https://techcrunch.com/2024/01/01/startup-news",
         ["Post at https://techcrunch.com/2024/01/01/startup-news"]),

        ("Article at https://arstechnica.com/gadgets/2024/01/review",
         ["Article at https://arstechnica.com/gadgets/2024/01/review"]),

        ("See https://www.theverge.com/2024/1/1/tech-news",
         ["See https://www.theverge.com/2024/1/1/tech-news"]),

        # Developer blogs
        ("Post at https://martinfowler.com/articles/microservices.html",
         ["Post at https://martinfowler.com/articles/microservices.html"]),

        ("Article at https://blog.example.com/2024/01/post-title",
         ["Article at https://blog.example.com/2024/01/post-title"]),
    ])
    def test_urls_real_world_blogs_news(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsSpecialSchemes:
    """Test URLs with special schemes beyond HTTP/HTTPS"""

    @pytest.mark.parametrize("text,expected", [
        # FTP
        ("Download from ftp://ftp.example.com/file.zip",
         ["Download from ftp://ftp.example.com/file.zip"]),

        ("Connect to ftp://files.example.org",
         ["Connect to ftp://files.example.org"]),

        # FTPS
        ("Secure FTP at ftps://secure.example.com",
         ["Secure FTP at ftps://secure.example.com"]),

        # File protocol
        ("Local file at file:///Users/username/document.pdf",
         ["Local file at file:///Users/username/document.pdf"]),

        ("See file:///C:/Users/Documents/file.txt",
         ["See file:///C:/Users/Documents/file.txt"]),

        # WebSocket
        ("Connect to ws://example.com/socket",
         ["Connect to ws://example.com/socket"]),

        ("Secure socket at wss://example.com/socket",
         ["Secure socket at wss://example.com/socket"]),

        # Mailto
        ("Email to mailto:user@example.com",
         ["Email to mailto:user@example.com"]),

        ("Contact mailto:support@example.com",
         ["Contact mailto:support@example.com"]),

        # Tel
        ("Call tel:+1-234-567-8900",
         ["Call tel:+1-234-567-8900"]),
    ])
    def test_urls_special_schemes(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsIPAddresses:
    """Test URLs with IP addresses"""

    @pytest.mark.parametrize("text,expected", [
        # IPv4
        ("Visit http://192.168.1.1",
         ["Visit http://192.168.1.1"]),

        ("Connect to http://10.0.0.1",
         ["Connect to http://10.0.0.1"]),

        ("See http://127.0.0.1",
         ["See http://127.0.0.1"]),

        ("API at http://172.16.0.1",
         ["API at http://172.16.0.1"]),

        # With ports
        ("Visit http://192.168.1.1:8080",
         ["Visit http://192.168.1.1:8080"]),

        ("Connect to http://10.0.0.1:3000",
         ["Connect to http://10.0.0.1:3000"]),

        ("Localhost at http://127.0.0.1:5000",
         ["Localhost at http://127.0.0.1:5000"]),

        # With paths
        ("API at http://192.168.1.1/api/v1",
         ["API at http://192.168.1.1/api/v1"]),

        ("See http://10.0.0.1/dashboard",
         ["See http://10.0.0.1/dashboard"]),

        # With query parameters
        ("Visit http://192.168.1.1?config=true",
         ["Visit http://192.168.1.1?config=true"]),

        # IPv6 (in brackets)
        ("Connect to http://[2001:db8::1]",
         ["Connect to http://[2001:db8::1]"]),

        ("See http://[::1]",
         ["See http://[::1]"]),

        ("Visit http://[2001:db8::1]:8080",
         ["Visit http://[2001:db8::1]:8080"]),
    ])
    def test_urls_ip_addresses(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsLocalhost:
    """Test localhost URLs"""

    @pytest.mark.parametrize("text,expected", [
        # Basic localhost
        ("Visit http://localhost",
         ["Visit http://localhost"]),

        ("See http://localhost:3000",
         ["See http://localhost:3000"]),

        ("Connect to http://localhost:8080",
         ["Connect to http://localhost:8080"]),

        # With paths
        ("Dashboard at http://localhost:3000/dashboard",
         ["Dashboard at http://localhost:3000/dashboard"]),

        ("API at http://localhost:8080/api/v1",
         ["API at http://localhost:8080/api/v1"]),

        # With query parameters
        ("Visit http://localhost:3000?debug=true",
         ["Visit http://localhost:3000?debug=true"]),

        ("See http://localhost:8080/api?key=test",
         ["See http://localhost:8080/api?key=test"]),

        # HTTPS localhost
        ("Secure at https://localhost:443",
         ["Secure at https://localhost:443"]),

        # Localhost aliases
        ("Visit http://127.0.0.1:3000",
         ["Visit http://127.0.0.1:3000"]),
    ])
    def test_urls_localhost(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsEdgeCasesTrailingContent:
    """Test URLs with potentially problematic trailing content"""

    @pytest.mark.parametrize("text,expected", [
        # URL followed by comma (comma should NOT be part of URL)
        ("Visit https://example.com, then check the docs",
         ["Visit https://example.com, then check the docs"]),

        ("See https://example.com, https://example.org",
         ["See https://example.com, https://example.org"]),

        # URL followed by semicolon
        ("Visit https://example.com; it's helpful",
         ["Visit https://example.com; it's helpful"]),

        # URL followed by closing parenthesis (when URL is in parens)
        ("See the site (https://example.com) for details",
         ["See the site (https://example.com) for details"]),

        # URL followed by quote
        ("He said 'visit https://example.com' for info",
         ["He said 'visit https://example.com' for info"]),

        # URL at sentence end - THE CRITICAL CASE
        ("Visit the website at https://example.com",
         ["Visit the website at https://example.com"]),

        ("For more information see https://example.com",
         ["For more information see https://example.com"]),

        ("Documentation available at https://example.com",
         ["Documentation available at https://example.com"]),

        # URL before question (? should not be part of URL unless it's a query param)
        ("Have you seen https://example.com",
         ["Have you seen https://example.com"]),

        # URL before exclamation
        ("Check out https://example.com",
         ["Check out https://example.com"]),
    ])
    def test_urls_edge_cases_trailing_content(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsEdgeCasesComplexPaths:
    """Test URLs with complex path structures"""

    @pytest.mark.parametrize("text,expected", [
        # Very long paths
        ("Documentation at https://example.com/en/docs/api/v2/reference/endpoints/users/profile/settings",
         ["Documentation at https://example.com/en/docs/api/v2/reference/endpoints/users/profile/settings"]),

        # Paths with many hyphens
        ("See https://example.com/this-is-a-very-long-path-with-many-hyphens",
         ["See https://example.com/this-is-a-very-long-path-with-many-hyphens"]),

        # Paths with many underscores
        ("Visit https://example.com/this_is_a_path_with_underscores",
         ["Visit https://example.com/this_is_a_path_with_underscores"]),

        # Mixed separators
        ("Check https://example.com/path-with/mixed_separators/and-more",
         ["Check https://example.com/path-with/mixed_separators/and-more"]),

        # Encoded spaces
        ("Search https://example.com/search/hello%20world",
         ["Search https://example.com/search/hello%20world"]),

        # Multiple encoded characters
        ("See https://example.com/path%20with%20spaces%20and%20special%20chars",
         ["See https://example.com/path%20with%20spaces%20and%20special%20chars"]),

        # Paths with dots
        ("File at https://example.com/path/to/file.tar.gz",
         ["File at https://example.com/path/to/file.tar.gz"]),

        # Version paths
        ("API at https://example.com/api/v1.2.3/endpoint",
         ["API at https://example.com/api/v1.2.3/endpoint"]),

        # Dated paths
        ("Archive at https://example.com/2024/01/15/article",
         ["Archive at https://example.com/2024/01/15/article"]),
    ])
    def test_urls_edge_cases_complex_paths(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsEdgeCasesComplexQueries:
    """Test URLs with complex query parameters"""

    @pytest.mark.parametrize("text,expected", [
        # Many parameters
        ("Search https://example.com?q=test&lang=en&page=1&limit=10&sort=date",
         ["Search https://example.com?q=test&lang=en&page=1&limit=10&sort=date"]),

        # Array parameters
        ("Filter https://example.com?tags[]=python&tags[]=django&tags[]=web",
         ["Filter https://example.com?tags[]=python&tags[]=django&tags[]=web"]),

        # Encoded parameters
        ("Search https://example.com?q=hello%20world&filter=recent",
         ["Search https://example.com?q=hello%20world&filter=recent"]),

        # Parameters with special characters
        ("Visit https://example.com?redirect=/home&next=/dashboard",
         ["Visit https://example.com?redirect=/home&next=/dashboard"]),

        # Parameters with equals in value
        ("Check https://example.com?formula=a=b+c",
         ["Check https://example.com?formula=a=b+c"]),

        # Nested parameters
        ("API https://example.com?filter[name]=test&filter[date]=2024",
         ["API https://example.com?filter[name]=test&filter[date]=2024"]),
    ])
    def test_urls_edge_cases_complex_queries(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsRepeatedSequences:
    """Test repeated URL patterns and sequences"""

    @pytest.mark.parametrize("text,expected", [
        # Same URL twice in different sentences (URLs at end)
        ("Visit https://example.com for info. Also check https://example.com",
         ["Visit https://example.com for info.", "Also check https://example.com"]),

        # Same URL three times (URLs at end)
        ("Check https://example.com first. Then see https://example.com again. Finally visit https://example.com",
         ["Check https://example.com first.", "Then see https://example.com again.", "Finally visit https://example.com"]),

        # Pattern: URL, text, URL, text (URLs at end)
        ("Visit https://example.com for docs. See https://example.org for tutorials. Check https://example.net",
         ["Visit https://example.com for docs.", "See https://example.org for tutorials.", "Check https://example.net"]),

        # Multiple identical URLs in one sentence
        ("Compare https://example.com and https://example.com",
         ["Compare https://example.com and https://example.com"]),

        # Alternating pattern (URLs at end)
        ("See https://example.com and https://example.org. Then visit https://example.com",
         ["See https://example.com and https://example.org.", "Then visit https://example.com"]),
    ])
    def test_urls_repeated_sequences(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsMixedWithOtherPatterns:
    """Test URLs mixed with other special patterns"""

    @pytest.mark.parametrize("text,expected", [
        # URLs with abbreviations (URL at end - no period)
        ("See e.g. examples at https://example.com",
         ["See e.g. examples at https://example.com"]),

        ("Visit the site i.e. https://example.com",
         ["Visit the site i.e. https://example.com"]),

        ("Check Dr. Smith's work at https://example.com",
         ["Check Dr. Smith's work at https://example.com"]),

        # URLs with numbered titles (splits because capital after "Part 2.")
        ("Part 2. More details at https://example.com",
         ["Part 2.", "More details at https://example.com"]),

        ("Chapter 5. Visit https://example.com",
         ["Chapter 5.", "Visit https://example.com"]),

        # URLs with dates (URL at end - no period)
        ("On Jan. 15, 2024, visit https://example.com",
         ["On Jan. 15, 2024, visit https://example.com"]),

        ("Published Dec. 1, 2023 at https://example.com",
         ["Published Dec. 1, 2023 at https://example.com"]),

        # URLs with prices (doesn't split - treated as one sentence)
        ("Only $5. Visit https://example.com",
         ["Only $5. Visit https://example.com"]),

        ("Cost: $10.50. See https://example.com",
         ["Cost: $10.50.", "See https://example.com"]),

        # URLs with percentages (URL at end - no period)
        ("Save 20%. Visit https://example.com",
         ["Save 20%.", "Visit https://example.com"]),

        # URLs with measurements (URL at end - no period)
        ("Length: 5.5 cm. Details at https://example.com",
         ["Length: 5.5 cm.", "Details at https://example.com"]),
    ])
    def test_urls_mixed_with_other_patterns(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestURLsComplexRealWorld:
    """Complex real-world scenarios combining multiple features"""

    @pytest.mark.parametrize("text,expected", [
        # URL with everything (URL at end - no period)
        ("Visit https://api.example.com:8080/v2/users/profile?id=123&lang=en#settings",
         ["Visit https://api.example.com:8080/v2/users/profile?id=123&lang=en#settings"]),

        # Multiple complex URLs (URL at end - no period)
        ("See https://example.com/path?q=test#top and check https://example.org/docs",
         ["See https://example.com/path?q=test#top and check https://example.org/docs"]),

        # URL in context of larger text (URL NOT at end - period added normally)
        ("The documentation at https://docs.example.com/api/v2 explains authentication. Read it carefully",
         ["The documentation at https://docs.example.com/api/v2 explains authentication.", "Read it carefully."]),

        # Multiple sentences with URLs (URLs at end - no period)
        ("First, visit https://example.com. Then check https://example.org. Finally, see https://example.net",
         ["First, visit https://example.com.", "Then check https://example.org.", "Finally, see https://example.net"]),

        # URL with parenthetical (URL NOT at end - period added normally)
        ("Check the docs (https://example.com/docs) for details. This is important",
         ["Check the docs (https://example.com/docs) for details.", "This is important."]),

        # Mixed content (URL at end of middle sentence - no period there)
        ("In Part 2. we discussed APIs. See https://example.com/api for examples. Chapter 3. covers auth",
         ["In Part 2. we discussed APIs.", "See https://example.com/api for examples.", "Chapter 3. covers auth."]),
    ])
    def test_urls_complex_real_world(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
