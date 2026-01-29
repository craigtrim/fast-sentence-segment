# -*- coding: UTF-8 -*-
"""Technical and software documentation patterns."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestTechnicalDocumentation:
    """Technical and software documentation patterns."""

    @pytest.mark.parametrize("text,expected", [
        # File paths
        ("Navigate to /usr/local/bin/ for the executable.",
         ["Navigate to /usr/local/bin/ for the executable."]),

        ("The config is in C:\\Users\\Admin\\config.ini. Edit it carefully.",
         ["The config is in C:\\Users\\Admin\\config.ini.", "Edit it carefully."]),

        # Code references
        ("Call the function foo.bar() to initialize.",
         ["Call the function foo.bar() to initialize."]),

        ("The method obj.process() returns null. Check the input.",
         ["The method obj.process() returns null.", "Check the input."]),

        # Version numbers with multiple dots
        ("Upgrade to v2.3.4.1 for the fix.",
         ["Upgrade to v2.3.4.1 for the fix."]),

        ("Version 10.15.7 introduced this bug. Version 10.15.8 fixed it.",
         ["Version 10.15.7 introduced this bug.", "Version 10.15.8 fixed it."]),

        # IP addresses
        ("Connect to 192.168.1.1 for the router.",
         ["Connect to 192.168.1.1 for the router."]),

        ("The server at 10.0.0.1 is down. Try 10.0.0.2 instead.",
         ["The server at 10.0.0.1 is down.", "Try 10.0.0.2 instead."]),

        # Technical abbreviations
        ("The API returns HTTP 200 OK. Other codes indicate errors.",
         ["The API returns HTTP 200 OK.", "Other codes indicate errors."]),

        # Command line examples
        ("Run npm install first. Then run npm start.",
         ["Run npm install first.", "Then run npm start."]),

        # Complex technical reference
        ("See RFC 2616, Sec. 14.9 for HTTP caching headers.",
         ["See RFC 2616, Sec. 14.9 for HTTP caching headers."]),
    ])
    def test_technical_documentation(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
