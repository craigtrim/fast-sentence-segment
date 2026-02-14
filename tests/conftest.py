# -*- coding: UTF-8 -*-
"""Pytest configuration and fixtures."""

import pytest
from fast_sentence_segment import segment_text


@pytest.fixture
def segment():
    """Provide the segmentation function for tests.

    Note: Uses split_dialog=False to maintain backward compatibility
    with existing test expectations that assume multi-sentence quotes
    are kept together.
    """
    def _segment(text):
        return segment_text(text, flatten=True, split_dialog=False)
    return _segment
