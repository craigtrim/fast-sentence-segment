# -*- coding: UTF-8 -*-
"""Pytest configuration and fixtures."""

import pytest
from fast_sentence_segment import segment_text


@pytest.fixture
def segment():
    """Provide the segmentation function for tests."""
    def _segment(text):
        return segment_text(text, flatten=True)
    return _segment
