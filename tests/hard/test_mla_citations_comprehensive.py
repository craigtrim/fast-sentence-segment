# -*- coding: UTF-8 -*-
"""Comprehensive MLA citation format tests - Issue #31."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestMLACitationsComprehensive:
    """Comprehensive MLA citation format tests covering all patterns."""

    @pytest.mark.parametrize("text,expected", [
        # BASIC BOOK CITATIONS
        # Single author
        ("Hemingway, Ernest. The Sun Also Rises. Scribner, 1926.",
         ["Hemingway, Ernest. The Sun Also Rises. Scribner, 1926."]),

        ("Morrison, Toni. Beloved. Knopf, 1987.",
         ["Morrison, Toni. Beloved. Knopf, 1987."]),

        ("Orwell, George. Nineteen Eighty-Four. Secker and Warburg, 1949.",
         ["Orwell, George. Nineteen Eighty-Four. Secker and Warburg, 1949."]),

        # Two authors
        pytest.param(
            "Smith, John, and Mary Johnson. Research Methods. Academic Press, 2020.",
            ["Smith, John, and Mary Johnson. Research Methods. Academic Press, 2020."],
            marks=pytest.mark.xfail(reason="MLA citation with two authors incorrectly segmented")
        ),

        pytest.param(
            "Brown, Kevin, and Sarah Williams. Modern Literature. Oxford UP, 2019.",
            ["Brown, Kevin, and Sarah Williams. Modern Literature. Oxford UP, 2019."],
            marks=pytest.mark.xfail(reason="MLA citation with two authors incorrectly segmented")
        ),

        # Three authors
        pytest.param(
            "Garcia, Maria, Peter Lee, and Anna Chen. Cultural Studies. Norton, 2021.",
            ["Garcia, Maria, Peter Lee, and Anna Chen. Cultural Studies. Norton, 2021."],
            marks=pytest.mark.xfail(reason="MLA citation with three authors incorrectly segmented")
        ),

        # Four or more authors (et al.)
        pytest.param(
            "Johnson, Robert, et al. Team Research. Cambridge UP, 2022.",
            ["Johnson, Robert, et al. Team Research. Cambridge UP, 2022."],
            marks=pytest.mark.xfail(reason="MLA citation with et al. incorrectly segmented")
        ),

        # BOOK WITH EDITION
        ("Williams, Karen. Psychology Today. 5th ed., Pearson, 2020.",
         ["Williams, Karen. Psychology Today. 5th ed., Pearson, 2020."]),

        ("Smith, Alexander. Physics Fundamentals. Rev. ed., McGraw-Hill, 2019.",
         ["Smith, Alexander. Physics Fundamentals. Rev. ed., McGraw-Hill, 2019."]),

        # BOOK WITH EDITOR
        ("Shakespeare, William. The Complete Works. Edited by Stephen Greenblatt, Norton, 2015.",
         ["Shakespeare, William. The Complete Works. Edited by Stephen Greenblatt, Norton, 2015."]),

        ("Plato. The Republic. Edited by G. R. F. Ferrari, translated by Tom Griffith, Cambridge UP, 2000.",
         ["Plato. The Republic. Edited by G. R. F. Ferrari, translated by Tom Griffith, Cambridge UP, 2000."]),

        # EDITED ANTHOLOGY
        pytest.param(
            "Brown, Michael, editor. Modern Essays. Houghton Mifflin, 2018.",
            ["Brown, Michael, editor. Modern Essays. Houghton Mifflin, 2018."],
            marks=pytest.mark.xfail(reason="MLA citation with editor role incorrectly segmented")
        ),

        pytest.param(
            "Garcia, Lisa, and Tom Wilson, editors. Contemporary Voices. Bedford, 2020.",
            ["Garcia, Lisa, and Tom Wilson, editors. Contemporary Voices. Bedford, 2020."],
            marks=pytest.mark.xfail(reason="MLA citation with editors role incorrectly segmented")
        ),

        # CHAPTER IN EDITED BOOK
        ("Smith, Jane. \"Chapter Title.\" Book Title, edited by John Doe, Publisher, 2019, pp. 25-50.",
         ["Smith, Jane. \"Chapter Title.\" Book Title, edited by John Doe, Publisher, 2019, pp. 25-50."]),

        ("Johnson, Mark. \"Critical Analysis.\" The Anthology, edited by Sarah Brown and Kevin Lee, Norton, 2021, pp. 100-125.",
         ["Johnson, Mark. \"Critical Analysis.\" The Anthology, edited by Sarah Brown and Kevin Lee, Norton, 2021, pp. 100-125."]),

        # JOURNAL ARTICLES
        ("Williams, Patricia. \"Article Title.\" Journal of Research, vol. 15, no. 3, 2020, pp. 123-145.",
         ["Williams, Patricia. \"Article Title.\" Journal of Research, vol. 15, no. 3, 2020, pp. 123-145."]),

        ("Lee, Steven, and Anna Garcia. \"Study Results.\" International Journal, vol. 28, 2021, pp. 45-67.",
         ["Lee, Steven, and Anna Garcia. \"Study Results.\" International Journal, vol. 28, 2021, pp. 45-67."]),

        ("Brown, Kevin. \"Research Findings.\" Science Today, vol. 42, no. 2, Spring 2019, pp. 89-102.",
         ["Brown, Kevin. \"Research Findings.\" Science Today, vol. 42, no. 2, Spring 2019, pp. 89-102."]),

        # MAGAZINE ARTICLES
        ("Johnson, Alice. \"Feature Story.\" Time, 15 Mar. 2020, pp. 22-28.",
         ["Johnson, Alice. \"Feature Story.\" Time, 15 Mar. 2020, pp. 22-28."]),

        ("Smith, Robert. \"Current Events.\" National Geographic, June 2021, pp. 50-65.",
         ["Smith, Robert. \"Current Events.\" National Geographic, June 2021, pp. 50-65."]),

        # NEWSPAPER ARTICLES
        ("Williams, Karen. \"Breaking News.\" The New York Times, 10 Jan. 2020, p. A1.",
         ["Williams, Karen. \"Breaking News.\" The New York Times, 10 Jan. 2020, p. A1."]),

        ("Garcia, Luis. \"Local Report.\" Chicago Tribune, 5 May 2019, pp. B3-B4.",
         ["Garcia, Luis. \"Local Report.\" Chicago Tribune, 5 May 2019, pp. B3-B4."]),

        # WEB SOURCES
        ("Brown, Sarah. \"Article Title.\" Website Name, Publisher, 15 Mar. 2020, www.example.com/article. Accessed 10 June 2021.",
         ["Brown, Sarah. \"Article Title.\" Website Name, Publisher, 15 Mar. 2020, www.example.com/article. Accessed 10 June 2021."]),

        ("Johnson, Mark. \"Blog Post.\" Blog Name, 5 Apr. 2021, www.blog.com/post.",
         ["Johnson, Mark. \"Blog Post.\" Blog Name, 5 Apr. 2021, www.blog.com/post."]),

        pytest.param(
            "National Science Foundation. \"Research Report.\" NSF, 2020, www.nsf.gov/report. Accessed 15 Aug. 2021.",
            ["National Science Foundation. \"Research Report.\" NSF, 2020, www.nsf.gov/report. Accessed 15 Aug. 2021."],
            marks=pytest.mark.xfail(reason="MLA web citation with organizational author incorrectly segmented")
        ),

        # NO AUTHOR (TITLE FIRST)
        pytest.param(
            "\"Anonymous Article.\" Journal Name, vol. 10, 2020, pp. 50-60.",
            ["\"Anonymous Article.\" Journal Name, vol. 10, 2020, pp. 50-60."],
            marks=pytest.mark.xfail(reason="MLA citation with title first incorrectly segmented")
        ),

        pytest.param(
            "\"Corporate Report.\" Company Website, 2021, www.company.com.",
            ["\"Corporate Report.\" Company Website, 2021, www.company.com."],
            marks=pytest.mark.xfail(reason="MLA web citation with title first incorrectly segmented")
        ),

        # CORPORATE AUTHOR
        pytest.param(
            "American Medical Association. Health Guidelines. AMA Press, 2020.",
            ["American Medical Association. Health Guidelines. AMA Press, 2020."],
            marks=pytest.mark.xfail(reason="MLA citation with corporate author incorrectly segmented")
        ),

        pytest.param(
            "United Nations. Global Report. UN Publishing, 2019.",
            ["United Nations. Global Report. UN Publishing, 2019."],
            marks=pytest.mark.xfail(reason="MLA citation with corporate author incorrectly segmented")
        ),

        # NAMES WITH SUFFIXES
        pytest.param(
            "King, Martin Luther, Jr. \"Letter from Birmingham Jail.\" Why We Can't Wait, Harper, 1964, pp. 77-100.",
            ["King, Martin Luther, Jr. \"Letter from Birmingham Jail.\" Why We Can't Wait, Harper, 1964, pp. 77-100."],
            marks=pytest.mark.xfail(reason="MLA citation with name suffix incorrectly segmented")
        ),

        ("Smith, John, Sr. Family History. Private Press, 2018.",
         ["Smith, John, Sr. Family History. Private Press, 2018."]),

        # NAMES WITH HYPHENS
        ("Garcia-Martinez, Ana. Cultural Identity. Norton, 2020.",
         ["Garcia-Martinez, Ana. Cultural Identity. Norton, 2020."]),

        # MULTIVOLUME WORKS
        ("Johnson, Peter. Encyclopedia of Science. Vol. 3, Academic Press, 2019.",
         ["Johnson, Peter. Encyclopedia of Science. Vol. 3, Academic Press, 2019."]),

        ("Williams, Sarah. Complete Works. 5 vols., Oxford UP, 2018.",
         ["Williams, Sarah. Complete Works. 5 vols., Oxford UP, 2018."]),

        # SERIES
        ("Brown, Kevin. Book Title. Modern Literature Series, Cambridge UP, 2020.",
         ["Brown, Kevin. Book Title. Modern Literature Series, Cambridge UP, 2020."]),

        # TRANSLATION
        ("Camus, Albert. The Stranger. Translated by Matthew Ward, Vintage, 1989.",
         ["Camus, Albert. The Stranger. Translated by Matthew Ward, Vintage, 1989."]),

        ("García Márquez, Gabriel. One Hundred Years of Solitude. Translated by Gregory Rabassa, Harper, 1970.",
         ["García Márquez, Gabriel. One Hundred Years of Solitude. Translated by Gregory Rabassa, Harper, 1970."]),

        # REPUBLISHED BOOK
        ("Austen, Jane. Pride and Prejudice. 1813. Modern Library, 2000.",
         ["Austen, Jane. Pride and Prejudice. 1813. Modern Library, 2000."]),

        # DISSERTATION OR THESIS
        ("Smith, Jennifer. The Research Question. 2020. Harvard U, PhD dissertation.",
         ["Smith, Jennifer. The Research Question. 2020. Harvard U, PhD dissertation."]),

        ("Johnson, Mark. Analysis of Data. 2019. MIT, Master's thesis.",
         ["Johnson, Mark. Analysis of Data. 2019. MIT, Master's thesis."]),

        # CONFERENCE PAPER
        ("Williams, Patricia. \"Paper Title.\" Conference Proceedings, edited by John Doe, Academic Press, 2020, pp. 150-165.",
         ["Williams, Patricia. \"Paper Title.\" Conference Proceedings, edited by John Doe, Academic Press, 2020, pp. 150-165."]),

        # REVIEW
        ("Brown, Kevin. \"Review of Book Title, by Author Name.\" Journal, vol. 20, 2021, pp. 200-202.",
         ["Brown, Kevin. \"Review of Book Title, by Author Name.\" Journal, vol. 20, 2021, pp. 200-202."]),

        # INTRODUCTION, PREFACE, FOREWORD, OR AFTERWORD
        ("Smith, John. Introduction. The Complete Works, by William Shakespeare, Norton, 2015, pp. xi-xxv.",
         ["Smith, John. Introduction. The Complete Works, by William Shakespeare, Norton, 2015, pp. xi-xxv."]),

        # MULTIPLE CITATIONS IN SEQUENCE
        ("First citation here. Hemingway, Ernest. The Sun Also Rises. Scribner, 1926. Next work follows. Morrison, Toni. Beloved. Knopf, 1987.",
         ["First citation here.", "Hemingway, Ernest. The Sun Also Rises. Scribner, 1926.", "Next work follows.", "Morrison, Toni. Beloved. Knopf, 1987."]),

        # BOOK WITH SUBTITLE
        ("Smith, Jane. Main Title: A Comprehensive Subtitle. Publisher, 2020.",
         ["Smith, Jane. Main Title: A Comprehensive Subtitle. Publisher, 2020."]),

        # MULTIPLE PUBLISHERS
        ("Brown, Kevin. Research Methods. Oxford UP / MIT Press, 2019.",
         ["Brown, Kevin. Research Methods. Oxford UP / MIT Press, 2019."]),

        # GOVERNMENT PUBLICATION
        ("United States, Congress, Senate. Committee Report. Government Printing Office, 2020.",
         ["United States, Congress, Senate. Committee Report. Government Printing Office, 2020."]),

        # SACRED TEXT
        pytest.param(
            "The Bible. Authorized King James Version, Oxford UP, 1998.",
            ["The Bible. Authorized King James Version, Oxford UP, 1998."],
            marks=pytest.mark.xfail(reason="MLA sacred text citation incorrectly segmented")
        ),

        # FILM OR VIDEO
        pytest.param(
            "The Matrix. Directed by The Wachowskis, Warner Bros., 1999.",
            ["The Matrix. Directed by The Wachowskis, Warner Bros., 1999."],
            marks=pytest.mark.xfail(reason="MLA film citation incorrectly segmented")
        ),

        # MULTIPLE WORKS BY SAME AUTHOR
        pytest.param(
            "Smith, John. Early Work. Press A, 2018. Smith, John. Later Work. Press B, 2020.",
            ["Smith, John. Early Work. Press A, 2018.", "Smith, John. Later Work. Press B, 2020."],
            marks=pytest.mark.xfail(reason="MLA detector over-normalizes multiple citations")
        ),

        # CROSS-REFERENCE
        ("Johnson, Mark. \"Chapter.\" Brown, editor, pp. 50-75.",
         ["Johnson, Mark. \"Chapter.\" Brown, editor, pp. 50-75."]),

        # BOOK IN A SERIES WITH VOLUME AND ISSUE
        ("Williams, Sarah. \"Article.\" Series Title, vol. 10, no. 2, Publisher, 2020, pp. 100-120.",
         ["Williams, Sarah. \"Article.\" Series Title, vol. 10, no. 2, Publisher, 2020, pp. 100-120."]),
    ])
    def test_mla_citations_comprehensive(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """Test comprehensive MLA citation patterns."""
        assert segment(text) == expected
