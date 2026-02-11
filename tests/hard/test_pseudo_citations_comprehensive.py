# -*- coding: UTF-8 -*-
"""Comprehensive pseudo-citation and informal format tests - Issue #31."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestPseudoCitationsComprehensive:
    """Comprehensive pseudo-citation and informal format tests."""

    @pytest.mark.parametrize("text,expected", [
        # JOURNALISTIC/NEWS STYLE
        ("By John Smith, Published March 15, 2023.",
         ["By John Smith, Published March 15, 2023."]),

        ("By Sarah Johnson, March 10, 2020.",
         ["By Sarah Johnson, March 10, 2020."]),

        ("Article by Kevin Brown | December 5, 2021.",
         ["Article by Kevin Brown | December 5, 2021."]),

        ("Written by Maria Garcia - April 20, 2019.",
         ["Written by Maria Garcia - April 20, 2019."]),

        ("Published by Robert Lee on May 1, 2022.",
         ["Published by Robert Lee on May 1, 2022."]),

        ("By The Editorial Board, Updated Jan. 15, 2023.",
         ["By The Editorial Board, Updated Jan. 15, 2023."]),

        pytest.param(
            "Staff Writer, Associated Press. March 2020.",
            ["Staff Writer, Associated Press. March 2020."],
            marks=pytest.mark.xfail(reason="Pseudo-citation pattern incorrectly detected as MLA")
        ),

        # BLOG/WEB STYLE
        ("Posted by Alex Turner on November 12, 2021.",
         ["Posted by Alex Turner on November 12, 2021."]),

        ("Author: Jennifer Williams (May 2020).",
         ["Author: Jennifer Williams (May 2020)."]),

        ("Written by Thomas Brown | Last updated: June 15, 2023.",
         ["Written by Thomas Brown | Last updated: June 15, 2023."]),

        ("Author - Date - Title Format Test.",
         ["Author - Date - Title Format Test."]),

        ("By username123, posted Feb 2022.",
         ["By username123, posted Feb 2022."]),

        ("Contributed by Dr. Sarah Lee. March 10, 2021.",
         ["Contributed by Dr. Sarah Lee. March 10, 2021."]),

        # LEGAL CITATIONS
        ("Plaintiff v. Defendant, 123 F.3d 456 (9th Cir. 2020).",
         ["Plaintiff v. Defendant, 123 F.3d 456 (9th Cir. 2020)."]),

        ("Brown v. Board of Education, 347 U.S. 483 (1954).",
         ["Brown v. Board of Education, 347 U.S. 483 (1954)."]),

        ("Smith v. Jones, 500 F.Supp.2d 100 (S.D.N.Y. 2019).",
         ["Smith v. Jones, 500 F.Supp.2d 100 (S.D.N.Y. 2019)."]),

        ("Miranda v. Arizona, 384 U.S. 436 (1966).",
         ["Miranda v. Arizona, 384 U.S. 436 (1966)."]),

        ("42 U.S.C. § 1983 (2018).",
         ["42 U.S.C. § 1983 (2018)."]),

        pytest.param(
            "Cal. Penal Code § 187 (West 2020).",
            ["Cal. Penal Code § 187 (West 2020)."],
            marks=pytest.mark.xfail(reason="Legal citation pattern incorrectly detected as MLA")
        ),

        ("Restatement (Second) of Contracts § 90 (1981).",
         ["Restatement (Second) of Contracts § 90 (1981)."]),

        # TECHNICAL/ACADEMIC INFORMAL
        ("Author A, Author B (2020) \"Title of Paper\".",
         ["Author A, Author B (2020) \"Title of Paper\"."]),

        pytest.param(
            "Smith et al. 2019. Results and Discussion.",
            ["Smith et al. 2019. Results and Discussion."],
            marks=pytest.mark.xfail(reason="Technical citation pattern incorrectly detected as MLA")
        ),

        ("[1] Johnson, K. (2020). Technical Report.",
         ["[1] Johnson, K. (2020). Technical Report."]),

        ("[2] Brown, A., Lee, S. (2021). Methodology.",
         ["[2] Brown, A., Lee, S. (2021). Methodology."]),

        pytest.param(
            "(1) Smith, J. Research Findings. 2020.",
            ["(1) Smith, J. Research Findings. 2020."],
            marks=pytest.mark.xfail(reason="Numbered citation pattern incorrectly detected as MLA")
        ),

        ("¹ Garcia, M. Historical Analysis. 2019.",
         ["¹ Garcia, M. Historical Analysis. 2019."]),

        ("² Williams, P. et al. Comprehensive Study. 2021.",
         ["² Williams, P. et al. Comprehensive Study. 2021."]),

        # PATENT CITATIONS
        pytest.param(
            "Smith, John M. (2020). Innovative Device. U.S. Patent No. 10,123,456.",
            ["Smith, John M. (2020). Innovative Device. U.S. Patent No. 10,123,456."],
            marks=pytest.mark.xfail(reason="Patent citation pattern incorrectly detected as MLA")
        ),

        pytest.param(
            "Johnson, A. B. & Lee, C. D. Method and Apparatus. Patent No. US9876543B2, Filed May 15, 2019.",
            ["Johnson, A. B. & Lee, C. D. Method and Apparatus. Patent No. US9876543B2, Filed May 15, 2019."],
            marks=pytest.mark.xfail(reason="Patent citation pattern incorrectly detected as MLA")
        ),

        pytest.param(
            "Garcia, M. (2021). System and Method. European Patent No. EP3456789.",
            ["Garcia, M. (2021). System and Method. European Patent No. EP3456789."],
            marks=pytest.mark.xfail(reason="European patent citation pattern incorrectly detected as MLA")
        ),

        # CONFERENCE/PROCEEDINGS INFORMAL
        ("Smith, J. (2020). Title. Presented at Conference Name, City, State.",
         ["Smith, J. (2020). Title. Presented at Conference Name, City, State."]),

        pytest.param(
            "Brown, K., Garcia, M. (2019, June). Paper Title. Conference Proceedings, pp. 100-110.",
            ["Brown, K., Garcia, M. (2019, June). Paper Title. Conference Proceedings, pp. 100-110."],
            marks=pytest.mark.xfail(reason="Conference citation pattern incorrectly detected as MLA")
        ),

        pytest.param(
            "Williams, P. et al. (2021). Poster Presentation. Annual Meeting, Location.",
            ["Williams, P. et al. (2021). Poster Presentation. Annual Meeting, Location."],
            marks=pytest.mark.xfail(reason="Conference citation pattern incorrectly detected as MLA")
        ),

        # SOCIAL MEDIA STYLE
        pytest.param(
            "@username. (2023, Mar 15). Tweet content.",
            ["@username. (2023, Mar 15). Tweet content."],
            marks=pytest.mark.xfail(reason="Social media citation pattern incorrectly detected as MLA")
        ),

        ("Posted by @user123 on March 10, 2023.",
         ["Posted by @user123 on March 10, 2023."]),

        # ARCHIVE/MANUSCRIPT CITATIONS
        pytest.param(
            "Letter from Abraham Lincoln to Mary Todd Lincoln (April 16, 1848). Lincoln Papers, Library of Congress.",
            ["Letter from Abraham Lincoln to Mary Todd Lincoln (April 16, 1848). Lincoln Papers, Library of Congress."],
            marks=pytest.mark.xfail(reason="Archive citation pattern incorrectly detected as MLA")
        ),

        pytest.param(
            "Manuscript Collection. Box 5, Folder 12. Archive Name, 1920.",
            ["Manuscript Collection. Box 5, Folder 12. Archive Name, 1920."],
            marks=pytest.mark.xfail(reason="Manuscript citation pattern incorrectly detected as MLA")
        ),

        # MIXED FORMAT CITATIONS
        pytest.param(
            "Source: Johnson, K. - 2020 - \"Article Title\" - Journal Name.",
            ["Source: Johnson, K. - 2020 - \"Article Title\" - Journal Name."],
            marks=pytest.mark.xfail(reason="Mixed format citation pattern incorrectly detected as MLA")
        ),

        ("Ref: Smith (2019), Brown (2020), Garcia (2021).",
         ["Ref: Smith (2019), Brown (2020), Garcia (2021)."]),

        # PRESS RELEASE STYLE
        pytest.param(
            "Company Name. (2023, January 15). Press Release Title [Press release].",
            ["Company Name. (2023, January 15). Press Release Title [Press release]."],
            marks=pytest.mark.xfail(reason="Press release citation pattern incorrectly detected as MLA")
        ),

        # INTERVIEW CITATIONS
        pytest.param(
            "Personal interview with Dr. Sarah Johnson. Conducted March 15, 2023.",
            ["Personal interview with Dr. Sarah Johnson. Conducted March 15, 2023."],
            marks=pytest.mark.xfail(reason="Interview citation pattern incorrectly detected as MLA")
        ),

        ("Johnson, Mark. Telephone interview. 10 May 2020.",
         ["Johnson, Mark. Telephone interview. 10 May 2020."]),

        # EMAIL CITATIONS
        ("Smith, Jane. \"Re: Research Question.\" Received by John Doe, 15 Mar. 2023.",
         ["Smith, Jane. \"Re: Research Question.\" Received by John Doe, 15 Mar. 2023."]),

        # LECTURE/SPEECH CITATIONS
        ("Brown, Kevin. \"Lecture Title.\" Guest Lecture, University Name, 20 Apr. 2023.",
         ["Brown, Kevin. \"Lecture Title.\" Guest Lecture, University Name, 20 Apr. 2023."]),

        # WIKIPEDIA STYLE
        pytest.param(
            "\"Article Title.\" Wikipedia, Wikimedia Foundation, 15 Mar. 2023, en.wikipedia.org/wiki/Article.",
            ["\"Article Title.\" Wikipedia, Wikimedia Foundation, 15 Mar. 2023, en.wikipedia.org/wiki/Article."],
            marks=pytest.mark.xfail(reason="Wikipedia citation pattern incorrectly detected as MLA")
        ),

        # DATABASE/SOFTWARE CITATIONS
        pytest.param(
            "Software Name. Version 2.0. Company Name, 2023.",
            ["Software Name. Version 2.0. Company Name, 2023."],
            marks=pytest.mark.xfail(reason="Software citation pattern incorrectly detected as MLA")
        ),

        pytest.param(
            "Database Name [Database]. Publisher, 2020. Accessed 15 June 2023.",
            ["Database Name [Database]. Publisher, 2020. Accessed 15 June 2023."],
            marks=pytest.mark.xfail(reason="Database citation pattern incorrectly detected as MLA")
        ),

        # MUSIC/AUDIO CITATIONS
        ("Artist Name. \"Song Title.\" Album Name, Record Label, 2020.",
         ["Artist Name. \"Song Title.\" Album Name, Record Label, 2020."]),

        pytest.param(
            "Podcast Name. Hosted by Host Name, Episode 42, Network Name, 15 Mar. 2023.",
            ["Podcast Name. Hosted by Host Name, Episode 42, Network Name, 15 Mar. 2023."],
            marks=pytest.mark.xfail(reason="Podcast citation pattern incorrectly detected as MLA")
        ),

        # VIDEO/MULTIMEDIA
        pytest.param(
            "\"Video Title.\" YouTube, uploaded by Channel Name, 15 Mar. 2023, www.youtube.com/watch?v=abc123.",
            ["\"Video Title.\" YouTube, uploaded by Channel Name, 15 Mar. 2023, www.youtube.com/watch?v=abc123."],
            marks=pytest.mark.xfail(reason="YouTube citation pattern incorrectly detected as MLA")
        ),

        # ART CITATIONS
        pytest.param(
            "Artist Name. Title of Artwork. 1920, Museum Name, City.",
            ["Artist Name. Title of Artwork. 1920, Museum Name, City."],
            marks=pytest.mark.xfail(reason="Art citation pattern incorrectly detected as MLA")
        ),

        # MAP/CHART CITATIONS
        pytest.param(
            "Map Title. Cartographer Name, Publisher, 2020.",
            ["Map Title. Cartographer Name, Publisher, 2020."],
            marks=pytest.mark.xfail(reason="Map citation pattern incorrectly detected as MLA")
        ),

        # ADVERTISEMENT CITATIONS
        pytest.param(
            "Company Name. Advertisement for Product. Magazine Name, May 2023, p. 42.",
            ["Company Name. Advertisement for Product. Magazine Name, May 2023, p. 42."],
            marks=pytest.mark.xfail(reason="Advertisement citation pattern incorrectly detected as MLA")
        ),

        # PERFORMANCE CITATIONS
        pytest.param(
            "Play Title. By Playwright Name, directed by Director Name, Theatre Name, City, 15 May 2023.",
            ["Play Title. By Playwright Name, directed by Director Name, Theatre Name, City, 15 May 2023."],
            marks=pytest.mark.xfail(reason="Performance citation pattern incorrectly detected as MLA")
        ),

        # TWEET/POST CITATIONS
        pytest.param(
            "@RealName (Username). \"Tweet text here.\" Twitter, 15 Mar. 2023, 3:42 p.m., twitter.com/username/status/123.",
            ["@RealName (Username). \"Tweet text here.\" Twitter, 15 Mar. 2023, 3:42 p.m., twitter.com/username/status/123."],
            marks=pytest.mark.xfail(reason="Twitter citation pattern incorrectly detected as MLA")
        ),

        # REPOSITORY/CODE CITATIONS
        pytest.param(
            "Username. \"Repository Name.\" GitHub, 2023, github.com/username/repo.",
            ["Username. \"Repository Name.\" GitHub, 2023, github.com/username/repo."],
            marks=pytest.mark.xfail(reason="GitHub citation pattern incorrectly detected as MLA")
        ),

        # STANDARD/SPECIFICATION CITATIONS
        pytest.param(
            "ISO 8601:2019. Data elements and interchange formats.",
            ["ISO 8601:2019. Data elements and interchange formats."],
            marks=pytest.mark.xfail(reason="ISO standard citation pattern incorrectly detected as MLA")
        ),

        pytest.param(
            "IEEE 802.11. Wireless LAN Standard. 2020.",
            ["IEEE 802.11. Wireless LAN Standard. 2020."],
            marks=pytest.mark.xfail(reason="IEEE standard citation pattern incorrectly detected as MLA")
        ),

        # MULTIPLE CITATIONS IN TEXT
        pytest.param(
            "Research shows this. By Smith, 2020. Further evidence appears. By Brown, 2021. The conclusion follows.",
            ["Research shows this.", "By Smith, 2020.", "Further evidence appears.", "By Brown, 2021.", "The conclusion follows."],
            marks=pytest.mark.xfail(reason="Multiple pseudo-citations in text incorrectly segmented")
        ),
    ])
    def test_pseudo_citations_comprehensive(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """Test comprehensive pseudo-citation and informal format patterns."""
        assert segment(text) == expected
