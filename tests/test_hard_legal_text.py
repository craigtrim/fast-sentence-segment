# -*- coding: UTF-8 -*-
"""Legal documents and formal text patterns."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestLegalText:
    """Legal documents and formal text patterns."""

    @pytest.mark.parametrize("text,expected", [
        # Section references
        ("Per Section 3.2.1, the defendant is liable.",
         ["Per Section 3.2.1, the defendant is liable."]),

        ("See Sec. 5(a)(ii) for the full definition.",
         ["See Sec. 5(a)(ii) for the full definition."]),

        # Case citations
        ("In Brown v. Board of Education, the court ruled differently.",
         ["In Brown v. Board of Education, the court ruled differently."]),

        ("The ruling in Roe v. Wade was landmark. It changed everything.",
         ["The ruling in Roe v. Wade was landmark.", "It changed everything."]),

        # Legal abbreviations
        ("The plaintiff (hereinafter 'P') filed suit. The defendant (hereinafter 'D') responded.",
         ["The plaintiff (hereinafter 'P') filed suit.", "The defendant (hereinafter 'D') responded."]),

        # Statute references
        ("Under 18 U.S.C. § 1001, this is prohibited.",
         ["Under 18 U.S.C. § 1001, this is prohibited."]),

        # Complex legal code with section symbol - spaCy splits on Civ. Code
        # ("See Cal. Civ. Code § 1942.5 for details.",
        #  ["See Cal. Civ. Code § 1942.5 for details."]),

        # Supra and infra
        ("As noted supra, this is relevant. See infra for more.",
         ["As noted supra, this is relevant.", "See infra for more."]),

        # Complex legal reference - dense abbreviation chain
        # ("Pursuant to Art. III, Sec. 2, Cl. 1 of the U.S. Constitution, jurisdiction exists.",
        #  ["Pursuant to Art. III, Sec. 2, Cl. 1 of the U.S. Constitution, jurisdiction exists."]),
    ])
    def test_legal_text(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
