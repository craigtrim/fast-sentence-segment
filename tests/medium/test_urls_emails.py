# -*- coding: UTF-8 -*-
"""Text containing URLs and email addresses."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestURLsAndEmails:
    """Text containing URLs and email addresses."""

    @pytest.mark.parametrize("text,expected", [
        # Simple URLs
        ("Visit www.example.com for details.",
         ["Visit www.example.com for details."]),
        ("Go to google.com now.", ["Go to google.com now."]),

        # URLs with http
        ("Check out http://example.com today.",
         ["Check out http://example.com today."]),
        ("Visit https://secure.example.com for more.",
         ["Visit https://secure.example.com for more."]),

        # URLs followed by sentences
        ("Visit example.com for info. Call us if needed.",
         ["Visit example.com for info.", "Call us if needed."]),

        # Email addresses
        ("Email us at info@example.com today.",
         ["Email us at info@example.com today."]),
        ("Contact support@company.com for help.",
         ["Contact support@company.com for help."]),

        # Email followed by sentence
        ("Write to me at john@example.com. I'll reply soon.",
         ["Write to me at john@example.com.", "I'll reply soon."]),

        # Multiple URLs or emails
        ("Visit site1.com or site2.com for options.",
         ["Visit site1.com or site2.com for options."]),
        ("Email john@co.com or jane@co.com for help.",
         ["Email john@co.com or jane@co.com for help."]),
    ])
    def test_urls_and_emails(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
