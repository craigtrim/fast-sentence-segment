# -*- coding: UTF-8 -*-
"""Comprehensive citation edge case tests - Issue #31."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestCitationEdgeCasesComprehensive:
    """Comprehensive citation edge case tests for tricky patterns."""

    @pytest.mark.parametrize("text,expected", [
        # PARENTHETICAL YEARS AFTER PERIODS - CORE ISSUE #31
        ("Matolino, Bernard. (2011). The Function.",
         ["Matolino, Bernard. (2011). The Function."]),

        ("Smith, John. (2023). Title.",
         ["Smith, John. (2023). Title."]),

        ("Organization Name. (2020). Report.",
         ["Organization Name. (2020). Report."]),

        ("Author, F. M. (2019, March). Monthly.",
         ["Author, F. M. (2019, March). Monthly."]),

        ("Johnson, A. B. (2021, April 15). Daily.",
         ["Johnson, A. B. (2021, April 15). Daily."]),

        # MULTIPLE PARENTHETICALS
        ("Author, F. (2020). (Additional note). Title.",
         ["Author, F. (2020). (Additional note). Title."]),

        ("Smith, J. (2019). Title (with subtitle). (And more).",
         ["Smith, J. (2019). Title (with subtitle). (And more)."]),

        # ABBREVIATIONS THAT LOOK LIKE INITIALS
        ("Dr. Smith. (2020). Medical Research.",
         ["Dr. Smith. (2020). Medical Research."]),

        ("Prof. Johnson et al. (2019). Academic Study.",
         ["Prof. Johnson et al. (2019). Academic Study."]),

        ("St. Mary's Hospital. (2021). Annual Report.",
         ["St. Mary's Hospital. (2021). Annual Report."]),

        ("Mt. Vernon Press. (2020). Publication Guidelines.",
         ["Mt. Vernon Press. (2020). Publication Guidelines."]),

        ("Rev. Dr. King, Jr. (2018). Theological Analysis.",
         ["Rev. Dr. King, Jr. (2018). Theological Analysis."]),

        # MULTIPLE SENTENCES IN CITATIONS
        ("Author. (2020). Title: A subtitle. More information follows. Publisher.",
         ["Author. (2020). Title: A subtitle. More information follows. Publisher."]),

        ("Smith, J. (2019). Main Work. See also related work. In Proceedings.",
         ["Smith, J. (2019). Main Work. See also related work. In Proceedings."]),

        # NUMERIC AND SPECIAL DATE PATTERNS
        ("Author. (2023a). First work of year.",
         ["Author. (2023a). First work of year."]),

        ("Author. (2023b). Second work of year.",
         ["Author. (2023b). Second work of year."]),

        ("Smith, J. (2023c). Third work.",
         ["Smith, J. (2023c). Third work."]),

        ("Brown, K. (1999-2001). Longitudinal Study.",
         ["Brown, K. (1999-2001). Longitudinal Study."]),

        ("Garcia, M. (c. 2000). Approximate Date Work.",
         ["Garcia, M. (c. 2000). Approximate Date Work."]),

        ("Johnson, P. (2023, April 15-16). Conference.",
         ["Johnson, P. (2023, April 15-16). Conference."]),

        # INSTITUTIONAL NAMES WITH PERIODS
        ("U.S. Department. (2020). Federal Report.",
         ["U.S. Department. (2020). Federal Report."]),

        ("U.K. Parliament. (2019). Legislative Review.",
         ["U.K. Parliament. (2019). Legislative Review."]),

        ("A.C.L.U. (2021). Legal Brief.",
         ["A.C.L.U. (2021). Legal Brief."]),

        ("N.A.S.A. (2022). Mission Report.",
         ["N.A.S.A. (2022). Mission Report."]),

        ("U.N. Security Council. (2020). Resolution.",
         ["U.N. Security Council. (2020). Resolution."]),

        ("N.I.H. (2021). Health Guidelines.",
         ["N.I.H. (2021). Health Guidelines."]),

        # QUOTES AND TITLES WITH PERIODS IN CITATIONS
        ("Author. (2020). \"Title with sentence. And another.\" Journal.",
         ["Author. (2020). \"Title with sentence. And another.\" Journal."]),

        ("Smith, J. (2019). Dr. Jekyll and Mr. Hyde. Publisher.",
         ["Smith, J. (2019). Dr. Jekyll and Mr. Hyde. Publisher."]),

        ("Brown, K. (2021). \"Question? Answer.\" Magazine.",
         ["Brown, K. (2021). \"Question? Answer.\" Magazine."]),

        # CITATIONS WITH MULTIPLE AUTHOR ABBREVIATIONS
        ("Smith, J., Jr., Brown, K., Sr., & Lee, M. L., III. (2020). Family Study.",
         ["Smith, J., Jr., Brown, K., Sr., & Lee, M. L., III. (2020). Family Study."]),

        # CITATIONS AT SENTENCE BOUNDARIES
        ("This is text before. Smith, J. (2020). Citation Title. This is after.",
         ["This is text before.", "Smith, J. (2020). Citation Title.", "This is after."]),

        ("Text continues. Brown, K. (2019). Work. More text.",
         ["Text continues.", "Brown, K. (2019). Work.", "More text."]),

        # CITATIONS WITH URLs
        ("Author. (2020). Title. https://doi.org/10.1234/example.",
         ["Author. (2020). Title. https://doi.org/10.1234/example."]),

        ("Smith, J. (2021). Work. Retrieved from www.example.com.",
         ["Smith, J. (2021). Work. Retrieved from www.example.com."]),

        # MIXED CITATION AND REGULAR TEXT
        ("Normal sentence ends here. Johnson, A. (2020). Citation text. Another sentence.",
         ["Normal sentence ends here.", "Johnson, A. (2020). Citation text.", "Another sentence."]),

        # CITATIONS WITH VOLUME AND ISSUE NUMBERS
        ("Author. (2020). Title. Journal, 15(3), 123-145.",
         ["Author. (2020). Title. Journal, 15(3), 123-145."]),

        ("Smith, J., & Brown, K. (2019). Article. Magazine, Vol. 42, No. 2, pp. 50-60.",
         ["Smith, J., & Brown, K. (2019). Article. Magazine, Vol. 42, No. 2, pp. 50-60."]),

        # CITATION WITH EDITOR ABBREVIATIONS
        ("Author. (2020). Chapter. In K. Brown (Ed.), Book.",
         ["Author. (2020). Chapter. In K. Brown (Ed.), Book."]),

        ("Smith, J. (2019). Section. In A. Johnson & B. Lee (Eds.), Anthology.",
         ["Smith, J. (2019). Section. In A. Johnson & B. Lee (Eds.), Anthology."]),

        # VERY SHORT AUTHOR NAMES
        ("Li, J. (2020). Chinese Literature Study.",
         ["Li, J. (2020). Chinese Literature Study."]),

        ("Wu, A. B. (2021). Research.",
         ["Wu, A. B. (2021). Research."]),

        ("O, K. (2019). Minimal Name.",
         ["O, K. (2019). Minimal Name."]),

        # VERY LONG AUTHOR NAMES
        ("van der Waals-Schmidt-Johannsen, P. K. M. (2020). Complex Name Study.",
         ["van der Waals-Schmidt-Johannsen, P. K. M. (2020). Complex Name Study."]),

        # CITATIONS WITH AMPERSAND VS AND
        ("Smith, J., & Brown, K. (2020). APA Style.",
         ["Smith, J., & Brown, K. (2020). APA Style."]),

        ("Smith, John, and Karen Brown. (2020). MLA Style.",
         ["Smith, John, and Karen Brown. (2020). MLA Style."]),

        # CITATIONS WITH PARENTHETICAL AUTHORS
        ("(Anonymous). (2020). Secret Report.",
         ["(Anonymous). (2020). Secret Report."]),

        # MULTIPLE PERIODS IN CLOSE PROXIMITY
        ("Smith, J. R. K. L. M. (2020). Many Initials.",
         ["Smith, J. R. K. L. M. (2020). Many Initials."]),

        ("U.S.A. Today Inc. (2021). Company Report.",
         ["U.S.A. Today Inc. (2021). Company Report."]),

        # CITATIONS WITH BRACKETS
        ("Author. (2020). Title [Special Edition].",
         ["Author. (2020). Title [Special Edition]."]),

        ("Smith, J. [Username]. (2021). Online Post.",
         ["Smith, J. [Username]. (2021). Online Post."]),

        # CITATIONS WITH SLASHES
        ("Author. (2020/2021). Cross-Year Publication.",
         ["Author. (2020/2021). Cross-Year Publication."]),

        # CITATIONS WITH QUESTION OR EXCLAMATION IN TITLE
        ("Smith, J. (2020). What Is Truth? Publisher.",
         ["Smith, J. (2020). What Is Truth? Publisher."]),

        ("Brown, K. (2019). Eureka! A Discovery. Journal.",
         ["Brown, K. (2019). Eureka! A Discovery. Journal."]),

        # NO DATE VARIATIONS
        ("Author. (n.d.). No Date Work.",
         ["Author. (n.d.). No Date Work."]),

        ("Smith, J. (n.d.-a). First undated.",
         ["Smith, J. (n.d.-a). First undated."]),

        ("Smith, J. (n.d.-b). Second undated.",
         ["Smith, J. (n.d.-b). Second undated."]),

        # FORTHCOMING PUBLICATIONS
        ("Author. (in press). Future Work.",
         ["Author. (in press). Future Work."]),

        ("Smith, J. (forthcoming). Upcoming Publication.",
         ["Smith, J. (forthcoming). Upcoming Publication."]),

        # SEASON DATES
        ("Brown, K. (2020, Spring). Seasonal Publication.",
         ["Brown, K. (2020, Spring). Seasonal Publication."]),

        ("Garcia, M. (2019, Fall/Winter). Multi-Season Issue.",
         ["Garcia, M. (2019, Fall/Winter). Multi-Season Issue."]),

        # PERSONAL COMMUNICATIONS (NOT IN REFERENCE LIST)
        ("A. Smith (personal communication, March 15, 2020).",
         ["A. Smith (personal communication, March 15, 2020)."]),

        # REPRINT EDITIONS
        ("Author. (2020). Title (Original work published 1950).",
         ["Author. (2020). Title (Original work published 1950)."]),

        # TRANSLATED WORKS WITH ORIGINAL DATE
        ("Author. (2020). Title (A. Translator, Trans.; Original work published 1900).",
         ["Author. (2020). Title (A. Translator, Trans.; Original work published 1900)."]),

        # ADVANCE ONLINE PUBLICATION
        ("Smith, J. (2023). Title. Journal. Advance online publication.",
         ["Smith, J. (2023). Title. Journal. Advance online publication."]),

        # CITATIONS WITH EMOJI OR SPECIAL CHARACTERS
        ("Author★. (2020). Special Character Name.",
         ["Author★. (2020). Special Character Name."]),

        # VERY LONG ORGANIZATIONAL NAMES
        ("International Federation of Library Associations and Institutions. (2020). Standards.",
         ["International Federation of Library Associations and Institutions. (2020). Standards."]),

        # INITIALS WITHOUT SPACES
        ("Smith, J.R.K. (2020). No Space Initials.",
         ["Smith, J.R.K. (2020). No Space Initials."]),

        # MIDDLE NAMES SPELLED OUT
        ("Smith, John Robert. (2020). Full Middle Name.",
         ["Smith, John Robert. (2020). Full Middle Name."]),

        ("Garcia, Maria Elena Sofia. (2021). Multiple Middle Names.",
         ["Garcia, Maria Elena Sofia. (2021). Multiple Middle Names."]),

        # COMPOUND LAST NAMES
        ("Smith-Jones-Brown, K. (2020). Triple Compound.",
         ["Smith-Jones-Brown, K. (2020). Triple Compound."]),

        # APOSTROPHES IN NAMES
        ("O'Brien, P. (2020). Irish Name.",
         ["O'Brien, P. (2020). Irish Name."]),

        ("D'Angelo, M. (2021). Italian Name.",
         ["D'Angelo, M. (2021). Italian Name."]),

        # NAMES WITH MAC/MC
        ("MacArthur, J. (2020). Scottish Name.",
         ["MacArthur, J. (2020). Scottish Name."]),

        ("McDonald, K. (2019). Mc Prefix.",
         ["McDonald, K. (2019). Mc Prefix."]),

        # NAMES FROM DIFFERENT CULTURES
        ("Nguyen, T. H. (2020). Vietnamese Name.",
         ["Nguyen, T. H. (2020). Vietnamese Name."]),

        ("al-Rahman, A. (2021). Arabic Name.",
         ["al-Rahman, A. (2021). Arabic Name."]),

        ("ibn Battuta, M. (2019). Historical Arabic Name.",
         ["ibn Battuta, M. (2019). Historical Arabic Name."]),
    ])
    def test_citation_edge_cases_comprehensive(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """Test comprehensive citation edge cases."""
        assert segment(text) == expected
