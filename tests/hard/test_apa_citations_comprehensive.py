# -*- coding: UTF-8 -*-
"""Comprehensive APA citation format tests - Issue #31."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestAPACitationsComprehensive:
    """Comprehensive APA citation format tests covering all patterns."""

    @pytest.mark.parametrize("text,expected", [
        # BASIC AUTHOR-DATE PATTERNS
        # Single author with full first name
        ("Matolino, Bernard. (2011). The (Mal) Function of \"it\" in Ifeanyi Menkiti's Normative Account of Person.",
         ["Matolino, Bernard. (2011). The (Mal) Function of \"it\" in Ifeanyi Menkiti's Normative Account of Person."]),

        ("Smith, John. (2023). Introduction to Machine Learning.",
         ["Smith, John. (2023). Introduction to Machine Learning."]),

        # Single author with initials
        ("Smith, J. (2023). Advanced Topics in AI.",
         ["Smith, J. (2023). Advanced Topics in AI."]),

        ("Jones, A. B. (2020). The Theory of Everything.",
         ["Jones, A. B. (2020). The Theory of Everything."]),

        ("Williams, P. R. K. (2019). Multiple Initials Research.",
         ["Williams, P. R. K. (2019). Multiple Initials Research."]),

        # Two authors
        ("Jones, A., & Lee, B. (2019). Advanced Topics in AI.",
         ["Jones, A., & Lee, B. (2019). Advanced Topics in AI."]),

        ("Smith, J. R., & Brown, K. L. (2022). Collaborative Research Methods.",
         ["Smith, J. R., & Brown, K. L. (2022). Collaborative Research Methods."]),

        # Three authors
        ("Garcia, M., Rodriguez, P., & Martinez, L. (2021). Hispanic Studies.",
         ["Garcia, M., Rodriguez, P., & Martinez, L. (2021). Hispanic Studies."]),

        # Four authors
        ("Author, A., Author, B., Author, C., & Author, D. (2020). Team Research.",
         ["Author, A., Author, B., Author, C., & Author, D. (2020). Team Research."]),

        # Et al. format
        ("Johnson, P., et al. (2018). Large Research Team.",
         ["Johnson, P., et al. (2018). Large Research Team."]),

        ("Williams, K. M., et al. (2023). Comprehensive Study Results.",
         ["Williams, K. M., et al. (2023). Comprehensive Study Results."]),

        # ORGANIZATIONAL AUTHORS
        ("World Health Organization. (2020). Global Health Report.",
         ["World Health Organization. (2020). Global Health Report."]),

        ("American Psychological Association. (2019). Publication Manual.",
         ["American Psychological Association. (2019). Publication Manual."]),

        ("National Institute of Health. (2021). Medical Research Guidelines.",
         ["National Institute of Health. (2021). Medical Research Guidelines."]),

        ("U.S. Department of Education. (2022). Annual Education Report.",
         ["U.S. Department of Education. (2022). Annual Education Report."]),

        ("Centers for Disease Control. (2020). Pandemic Response Protocol.",
         ["Centers for Disease Control. (2020). Pandemic Response Protocol."]),

        ("United Nations Educational Scientific and Cultural Organization. (2023). World Heritage Sites.",
         ["United Nations Educational Scientific and Cultural Organization. (2023). World Heritage Sites."]),

        # DATES WITH MONTH AND DAY
        ("Smith, J. (2023, January). Monthly Publication.",
         ["Smith, J. (2023, January). Monthly Publication."]),

        ("Johnson, A. (2020, March 15). Daily News Article.",
         ["Johnson, A. (2020, March 15). Daily News Article."]),

        ("World Health Organization. (2020, March 15). Global Report.",
         ["World Health Organization. (2020, March 15). Global Report."]),

        pytest.param(
            "Garcia, M. (2019, December 31). Year End Analysis.",
            ["Garcia, M. (2019, December 31). Year End Analysis."],
            marks=pytest.mark.xfail(reason="APA citation pattern incorrectly detected as MLA")
        ),

        # SPECIAL DATE FORMATS
        ("Author, A. (n.d.). Undated Work.",
         ["Author, A. (n.d.). Undated Work."]),

        ("Smith, J. (in press). Forthcoming Publication.",
         ["Smith, J. (in press). Forthcoming Publication."]),

        # EDITION AND VOLUME PATTERNS
        ("Schiller, Gebhardt. (2023). Essentials of Economics (12th ed.).",
         ["Schiller, Gebhardt. (2023). Essentials of Economics (12th ed.)."]),

        ("Brown, K. (2022). Research Methods (2nd ed.).",
         ["Brown, K. (2022). Research Methods (2nd ed.)."]),

        ("Johnson, P. (2021). The Complete Series (Vol. 3).",
         ["Johnson, P. (2021). The Complete Series (Vol. 3)."]),

        ("Williams, M. (2020). Encyclopedia Set (Vols. 1-5).",
         ["Williams, M. (2020). Encyclopedia Set (Vols. 1-5)."]),

        ("Garcia, L. (2019). Handbook (Rev. ed.).",
         ["Garcia, L. (2019). Handbook (Rev. ed.)."]),

        # ONLINE SOURCE PATTERNS
        ("Smith, J. (2023). Digital Article. Retrieved from https://example.com/article",
         ["Smith, J. (2023). Digital Article. Retrieved from https://example.com/article"]),

        ("Brown, A. (2022). Online Research. https://doi.org/10.1234/example",
         ["Brown, A. (2022). Online Research. https://doi.org/10.1234/example"]),

        ("Johnson, K. (2021, May 10). Blog Post. Retrieved June 15, 2023, from https://blog.example.com",
         ["Johnson, K. (2021, May 10). Blog Post. Retrieved June 15, 2023, from https://blog.example.com"]),

        # NAME VARIATIONS
        # Hyphenated names
        ("Garcia-Martinez, A. (2020). Cultural Studies.",
         ["Garcia-Martinez, A. (2020). Cultural Studies."]),

        ("Smith-Johnson-Brown, K. (2019). Complex Name Study.",
         ["Smith-Johnson-Brown, K. (2019). Complex Name Study."]),

        # Names with suffixes
        ("King, M. L., Jr. (2018). Leadership Principles.",
         ["King, M. L., Jr. (2018). Leadership Principles."]),

        ("Smith, J. R., Sr. (2020). Family Research.",
         ["Smith, J. R., Sr. (2020). Family Research."]),

        ("Johnson, A. B., III. (2021). Generational Study.",
         ["Johnson, A. B., III. (2021). Generational Study."]),

        # Names with prefixes
        ("van der Berg, P. (2022). Dutch Literature.",
         ["van der Berg, P. (2022). Dutch Literature."]),

        ("de la Cruz, M. (2023). Spanish History.",
         ["de la Cruz, M. (2023). Spanish History."]),

        ("von Neumann, J. (2019). Mathematics Research.",
         ["von Neumann, J. (2019). Mathematics Research."]),

        # Single letter last names
        ("Lee, J. (2020). Short Name Study.",
         ["Lee, J. (2020). Short Name Study."]),

        # MULTIPLE CITATIONS IN SEQUENCE
        ("First citation. Smith, J. (2020). First Work. Second work follows. Brown, K. (2021). Second Work.",
         ["First citation.", "Smith, J. (2020). First Work.", "Second work follows.", "Brown, K. (2021). Second Work."]),

        # Same author, different years (a, b notation)
        ("Johnson, P. (2023a). First Publication.",
         ["Johnson, P. (2023a). First Publication."]),

        ("Johnson, P. (2023b). Second Publication.",
         ["Johnson, P. (2023b). Second Publication."]),

        # SUBTITLE PATTERNS
        ("Smith, J. (2020). Main Title: A Comprehensive Subtitle.",
         ["Smith, J. (2020). Main Title: A Comprehensive Subtitle."]),

        ("Brown, K. (2021). Research Methods: Theory and Practice in Modern Science.",
         ["Brown, K. (2021). Research Methods: Theory and Practice in Modern Science."]),

        # CITATIONS WITH EDITOR/TRANSLATOR INFO
        ("Smith, J. (Ed.). (2020). Anthology of Modern Literature.",
         ["Smith, J. (Ed.). (2020). Anthology of Modern Literature."]),

        ("Brown, K., & Jones, A. (Eds.). (2021). Collected Essays.",
         ["Brown, K., & Jones, A. (Eds.). (2021). Collected Essays."]),

        ("Garcia, M. (Trans.). (2019). Translated Works.",
         ["Garcia, M. (Trans.). (2019). Translated Works."]),

        # CHAPTER IN EDITED BOOK
        ("Smith, J. (2020). Chapter Title. In K. Brown (Ed.), Book Title (pp. 25-50).",
         ["Smith, J. (2020). Chapter Title. In K. Brown (Ed.), Book Title (pp. 25-50)."]),

        # JOURNAL ARTICLES
        ("Johnson, A. (2021). Article Title. Journal of Research, 15(3), 123-145.",
         ["Johnson, A. (2021). Article Title. Journal of Research, 15(3), 123-145."]),

        ("Williams, P., & Lee, S. (2022). Study Results. International Journal, 28(2), 45-67. https://doi.org/10.1234/example",
         ["Williams, P., & Lee, S. (2022). Study Results. International Journal, 28(2), 45-67. https://doi.org/10.1234/example"]),

        # CONFERENCE PAPERS
        ("Brown, K. (2020). Paper Title. In Proceedings of the Conference (pp. 100-110).",
         ["Brown, K. (2020). Paper Title. In Proceedings of the Conference (pp. 100-110)."]),

        pytest.param(
            "Smith, J., & Garcia, M. (2019, June). Presentation Title. Paper presented at Conference Name, City, State.",
            ["Smith, J., & Garcia, M. (2019, June). Presentation Title. Paper presented at Conference Name, City, State."],
            marks=pytest.mark.xfail(reason="APA conference citation pattern incorrectly detected as MLA")
        ),

        # DISSERTATIONS AND THESES
        ("Johnson, P. (2021). Dissertation Title (Doctoral dissertation). University Name.",
         ["Johnson, P. (2021). Dissertation Title (Doctoral dissertation). University Name."]),

        ("Williams, K. (2020). Thesis Title (Master's thesis, University Name). Retrieved from https://repository.edu",
         ["Williams, K. (2020). Thesis Title (Master's thesis, University Name). Retrieved from https://repository.edu"]),

        # REPORT FORMATS
        ("American Psychological Association. (2019). Report Title (Report No. 123). Publisher.",
         ["American Psychological Association. (2019). Report Title (Report No. 123). Publisher."]),

        # CITATIONS FOLLOWED BY TEXT
        ("Research shows findings. Smith, J. (2020). Important Work. This supports the theory.",
         ["Research shows findings.", "Smith, J. (2020). Important Work.", "This supports the theory."]),

        # MULTIPLE WORKS BY SAME AUTHOR
        ("Smith, J. (2019). Early Work. Smith, J. (2020). Later Work. Smith, J. (2021). Recent Work.",
         ["Smith, J. (2019). Early Work.", "Smith, J. (2020). Later Work.", "Smith, J. (2021). Recent Work."]),
    ])
    def test_apa_citations_comprehensive(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """Test comprehensive APA citation patterns."""
        assert segment(text) == expected
