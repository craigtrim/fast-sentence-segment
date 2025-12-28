# -*- coding: UTF-8 -*-
"""Error handling for invalid inputs."""

import pytest
from fast_sentence_segment import segment_text


class TestErrorHandling:
    """Error handling for invalid inputs."""

    def test_empty_string_raises(self):
        with pytest.raises(ValueError):
            segment_text("")

    def test_none_raises(self):
        with pytest.raises((ValueError, TypeError)):
            segment_text(None)

    def test_whitespace_only(self):
        # Whitespace-only returns empty result after stripping
        result = segment_text("   ", flatten=True)
        assert result == []
