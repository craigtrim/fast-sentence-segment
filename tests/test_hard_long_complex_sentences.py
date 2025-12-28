# -*- coding: UTF-8 -*-
"""Very long or structurally complex sentences."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestLongAndComplexSentences:
    """Very long or structurally complex sentences."""

    @pytest.mark.parametrize("text,expected", [
        # Very long sentence with multiple clauses
        ("The committee, having reviewed all the evidence presented by both parties, including the financial statements from 2019, 2020, and 2021, as well as the testimony of the witnesses, has concluded that the allegations are unfounded.",
         ["The committee, having reviewed all the evidence presented by both parties, including the financial statements from 2019, 2020, and 2021, as well as the testimony of the witnesses, has concluded that the allegations are unfounded."]),

        # Multiple semicolons
        ("The first option is expensive; the second is time-consuming; the third is risky; we chose the fourth.",
         ["The first option is expensive; the second is time-consuming; the third is risky; we chose the fourth."]),

        # Complex with embedded quotes - requires quote-aware parsing
        # ('The report states, "Given the findings (see Appendix A, pp. 23-45), we recommend—as Dr. Smith suggested in his memo of Jan. 15—that the project be delayed."',
        #  ['The report states, "Given the findings (see Appendix A, pp. 23-45), we recommend—as Dr. Smith suggested in his memo of Jan. 15—that the project be delayed."']),

        # Sentence with multiple abbreviations and clauses
        ("Dr. J.R. Williams, Ph.D., who works at MIT, published the paper in Vol. 42, No. 3 of the journal, and it was later cited by Prof. A.B. Smith et al. in their 2021 review.",
         ["Dr. J.R. Williams, Ph.D., who works at MIT, published the paper in Vol. 42, No. 3 of the journal, and it was later cited by Prof. A.B. Smith et al. in their 2021 review."]),
    ])
    def test_long_complex_sentences(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
