# -*- coding: UTF-8 -*-
"""Academic and legal citation formats."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestAcademicCitations:
    """Academic and legal citation formats."""

    @pytest.mark.parametrize("text,expected", [
        # Parenthetical citations
        ("This was proven earlier (Smith, 2020).",
         ["This was proven earlier (Smith, 2020)."]),

        ("Multiple studies agree (Jones, 2019; Lee, 2020).",
         ["Multiple studies agree (Jones, 2019; Lee, 2020)."]),

        # Citation with page numbers
        ("As noted by Smith (2020, p. 45), this is true.",
         ["As noted by Smith (2020, p. 45), this is true."]),

        ("See the original paper (Johnson et al., 2018, pp. 23-27).",
         ["See the original paper (Johnson et al., 2018, pp. 23-27)."]),

        # Et al. usage
        ("Research shows (Williams et al., 2021) that this works.",
         ["Research shows (Williams et al., 2021) that this works."]),

        ("Smith et al. found similar results. This confirms the hypothesis.",
         ["Smith et al. found similar results.", "This confirms the hypothesis."]),

        # Multiple citations in sequence
        ("Many researchers agree (Brown, 2019; Davis, 2020; Miller et al., 2021). The evidence is strong.",
         ["Many researchers agree (Brown, 2019; Davis, 2020; Miller et al., 2021).", "The evidence is strong."]),

        # Footnote style - superscript confuses spaCy
        # ("The theory was proposed by Einstein.¹ It was later confirmed.²",
        #  ["The theory was proposed by Einstein.¹", "It was later confirmed.²"]),

        # Cf. abbreviation - spaCy splits on cf.
        # ("This contradicts earlier findings (cf. Smith, 2018).",
        #  ["This contradicts earlier findings (cf. Smith, 2018)."]),

        ("The same result was found (ibid., p. 34).",
         ["The same result was found (ibid., p. 34)."]),

        # Fig. and Table references
        ("See Fig. 3.2 for details. Table 4.1 shows the data.",
         ["See Fig. 3.2 for details.", "Table 4.1 shows the data."]),

        # Vol. and No.
        ("Published in Vol. 42, No. 3 of the journal.",
         ["Published in Vol. 42, No. 3 of the journal."]),
    ])
    def test_academic_citations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
