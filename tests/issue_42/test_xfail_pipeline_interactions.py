# -*- coding: UTF-8 -*-
"""Xfail tests for hard-wrap interactions with the full pipeline (issue #42).

These test the end-to-end segment_text() pipeline with passages that are
currently corrupted. After the fix, they should xpass.

Focus areas:
  AA. 2-space indent hard wraps (pipeline)
  BB. 8-space indent hard wraps (pipeline)
  CC. Tab-indent hard wraps (pipeline)
  DD. Trailing-space + 4-space (pipeline compound)
  EE. Multi-line 4-space passes through full pipeline
  FF. Mixed-indent pipeline tests

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

import pytest
from fast_sentence_segment import segment_text


class TestXfailPipelineInteractions:
    """Full-pipeline xfail tests for various indent and wrapping styles (issue #42)."""

    # ================================================================ AA. 2-space indent (pipeline)

    @pytest.mark.xfail(reason="2-space wrap: 'business.department' full pipeline (issue #42)")
    def test_2space_001(self):
        result = segment_text(
            "He worked in the business\n  department all his life.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'advertising.department' full pipeline (issue #42)")
    def test_2space_002(self):
        result = segment_text(
            "She managed the advertising\n  department for ten years.",
            flatten=True,
        )
        assert "advertising.department" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'fire.station' full pipeline (issue #42)")
    def test_2space_003(self):
        result = segment_text(
            "The alarm rang at the fire\n  station at midnight.",
            flatten=True,
        )
        assert "fire.station" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'post.office' full pipeline (issue #42)")
    def test_2space_004(self):
        result = segment_text(
            "She queued at the post\n  office to collect the parcel.",
            flatten=True,
        )
        assert "post.office" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'health.department' full pipeline (issue #42)")
    def test_2space_005(self):
        result = segment_text(
            "The health\n  department issued new guidelines.",
            flatten=True,
        )
        assert "health.department" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'town.council' full pipeline (issue #42)")
    def test_2space_006(self):
        result = segment_text(
            "He addressed the town\n  council on the housing question.",
            flatten=True,
        )
        assert "town.council" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'night.watchman' full pipeline (issue #42)")
    def test_2space_007(self):
        result = segment_text(
            "The night\n  watchman reported the break-in at six.",
            flatten=True,
        )
        assert "night.watchman" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'finance.committee' full pipeline (issue #42)")
    def test_2space_008(self):
        result = segment_text(
            "The finance\n  committee met on the first Monday.",
            flatten=True,
        )
        assert "finance.committee" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'foreign.office' full pipeline (issue #42)")
    def test_2space_009(self):
        result = segment_text(
            "He received instructions from the foreign\n  office.",
            flatten=True,
        )
        assert "foreign.office" not in " ".join(result)

    @pytest.mark.xfail(reason="2-space wrap: 'school.master' full pipeline (issue #42)")
    def test_2space_010(self):
        result = segment_text(
            "The school\n  master announced the results on Friday.",
            flatten=True,
        )
        assert "school.master" not in " ".join(result)

    # ================================================================ BB. 8-space indent (pipeline)

    @pytest.mark.xfail(reason="8-space wrap: 'business.department' full pipeline (issue #42)")
    def test_8space_001(self):
        result = segment_text(
            "He worked in the business\n        department all his life.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'advertising.department' full pipeline (issue #42)")
    def test_8space_002(self):
        result = segment_text(
            "She managed the advertising\n        department for ten years.",
            flatten=True,
        )
        assert "advertising.department" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'fire.station' full pipeline (issue #42)")
    def test_8space_003(self):
        result = segment_text(
            "The alarm rang at the fire\n        station at midnight.",
            flatten=True,
        )
        assert "fire.station" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'post.office' full pipeline (issue #42)")
    def test_8space_004(self):
        result = segment_text(
            "She queued at the post\n        office to collect the parcel.",
            flatten=True,
        )
        assert "post.office" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'health.department' full pipeline (issue #42)")
    def test_8space_005(self):
        result = segment_text(
            "The health\n        department issued new guidelines.",
            flatten=True,
        )
        assert "health.department" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'town.council' full pipeline (issue #42)")
    def test_8space_006(self):
        result = segment_text(
            "He addressed the town\n        council on the housing question.",
            flatten=True,
        )
        assert "town.council" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'night.watchman' full pipeline (issue #42)")
    def test_8space_007(self):
        result = segment_text(
            "The night\n        watchman reported the break-in at six.",
            flatten=True,
        )
        assert "night.watchman" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'finance.committee' full pipeline (issue #42)")
    def test_8space_008(self):
        result = segment_text(
            "The finance\n        committee met on the first Monday.",
            flatten=True,
        )
        assert "finance.committee" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'foreign.office' full pipeline (issue #42)")
    def test_8space_009(self):
        result = segment_text(
            "He received instructions from the foreign\n        office.",
            flatten=True,
        )
        assert "foreign.office" not in " ".join(result)

    @pytest.mark.xfail(reason="8-space wrap: 'school.master' full pipeline (issue #42)")
    def test_8space_010(self):
        result = segment_text(
            "The school\n        master announced the results on Friday.",
            flatten=True,
        )
        assert "school.master" not in " ".join(result)

    # ================================================================ CC. Tab indent (pipeline)

    @pytest.mark.xfail(reason="tab wrap: 'business.department' full pipeline (issue #42)")
    def test_tab_001(self):
        result = segment_text(
            "He worked in the business\n\tdepartment all his life.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'advertising.department' full pipeline (issue #42)")
    def test_tab_002(self):
        result = segment_text(
            "She managed the advertising\n\tdepartment for ten years.",
            flatten=True,
        )
        assert "advertising.department" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'fire.station' full pipeline (issue #42)")
    def test_tab_003(self):
        result = segment_text(
            "The alarm rang at the fire\n\tstation at midnight.",
            flatten=True,
        )
        assert "fire.station" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'post.office' full pipeline (issue #42)")
    def test_tab_004(self):
        result = segment_text(
            "She queued at the post\n\toffice to collect the parcel.",
            flatten=True,
        )
        assert "post.office" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'health.department' full pipeline (issue #42)")
    def test_tab_005(self):
        result = segment_text(
            "The health\n\tdepartment issued new guidelines.",
            flatten=True,
        )
        assert "health.department" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'town.council' full pipeline (issue #42)")
    def test_tab_006(self):
        result = segment_text(
            "He addressed the town\n\tcouncil on the housing question.",
            flatten=True,
        )
        assert "town.council" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'night.watchman' full pipeline (issue #42)")
    def test_tab_007(self):
        result = segment_text(
            "The night\n\twatchman reported the break-in at six.",
            flatten=True,
        )
        assert "night.watchman" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'finance.committee' full pipeline (issue #42)")
    def test_tab_008(self):
        result = segment_text(
            "The finance\n\tcommittee met on the first Monday.",
            flatten=True,
        )
        assert "finance.committee" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'foreign.office' full pipeline (issue #42)")
    def test_tab_009(self):
        result = segment_text(
            "He received instructions from the foreign\n\toffice.",
            flatten=True,
        )
        assert "foreign.office" not in " ".join(result)

    @pytest.mark.xfail(reason="tab wrap: 'school.master' full pipeline (issue #42)")
    def test_tab_010(self):
        result = segment_text(
            "The school\n\tmaster announced the results on Friday.",
            flatten=True,
        )
        assert "school.master" not in " ".join(result)

    # ================================================================ DD. Trailing-space + 4-space (pipeline)

    @pytest.mark.xfail(reason="trailing+4space: 'business.department' full pipeline (issue #42)")
    def test_trailing_4space_001(self):
        result = segment_text(
            "He worked in the business \n    department all his life.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'advertising.department' full pipeline (issue #42)")
    def test_trailing_4space_002(self):
        result = segment_text(
            "She managed the advertising \n    department for ten years.",
            flatten=True,
        )
        assert "advertising.department" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'fire.station' full pipeline (issue #42)")
    def test_trailing_4space_003(self):
        result = segment_text(
            "The alarm rang at the fire \n    station at midnight.",
            flatten=True,
        )
        assert "fire.station" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'post.office' full pipeline (issue #42)")
    def test_trailing_4space_004(self):
        result = segment_text(
            "She queued at the post \n    office to collect the parcel.",
            flatten=True,
        )
        assert "post.office" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'health.department' full pipeline (issue #42)")
    def test_trailing_4space_005(self):
        result = segment_text(
            "The health \n    department issued new guidelines.",
            flatten=True,
        )
        assert "health.department" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'town.council' full pipeline (issue #42)")
    def test_trailing_4space_006(self):
        result = segment_text(
            "He addressed the town \n    council on the housing question.",
            flatten=True,
        )
        assert "town.council" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'night.watchman' full pipeline (issue #42)")
    def test_trailing_4space_007(self):
        result = segment_text(
            "The night \n    watchman reported the break-in at six.",
            flatten=True,
        )
        assert "night.watchman" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'finance.committee' full pipeline (issue #42)")
    def test_trailing_4space_008(self):
        result = segment_text(
            "The finance \n    committee met on the first Monday.",
            flatten=True,
        )
        assert "finance.committee" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'foreign.office' full pipeline (issue #42)")
    def test_trailing_4space_009(self):
        result = segment_text(
            "He received instructions from the foreign \n    office.",
            flatten=True,
        )
        assert "foreign.office" not in " ".join(result)

    @pytest.mark.xfail(reason="trailing+4space: 'school.master' full pipeline (issue #42)")
    def test_trailing_4space_010(self):
        result = segment_text(
            "The school \n    master announced the results on Friday.",
            flatten=True,
        )
        assert "school.master" not in " ".join(result)

    # ================================================================ EE. Multi-line (pipeline)

    @pytest.mark.xfail(reason="multiline 4-space: Dreiser full pipeline (issue #42)")
    def test_multiline_001(self):
        result = segment_text(
            "Wanted: A number of bright young men to assist in the business\n"
            "    department during the Christmas holidays. Promotion possible.\n"
            "    Apply to Business Manager between 9 and 10 a.m.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text
        assert "possible.Apply" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: 3-line fiction passage (issue #42)")
    def test_multiline_002(self):
        result = segment_text(
            "She walked down the long corridor towards\n"
            "    the room at the end of the hall.\n"
            "    She knocked and waited.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "towards.the" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: 3-line business passage (issue #42)")
    def test_multiline_003(self):
        result = segment_text(
            "The committee met on three separate occasions\n"
            "    to discuss the proposed legislation.\n"
            "    No agreement was reached.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "occasions.to" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: 4-line passage (issue #42)")
    def test_multiline_004(self):
        result = segment_text(
            "He had lived in the town for twenty years\n"
            "    without once feeling truly at home.\n"
            "    His wife had adapted quickly.\n"
            "    He never did.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "years.without" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: journalism passage (issue #42)")
    def test_multiline_005(self):
        result = segment_text(
            "The report confirmed that the health\n"
            "    department had failed to act.\n"
            "    The minister denied knowledge.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "health.department" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: legal passage (issue #42)")
    def test_multiline_006(self):
        result = segment_text(
            "The contract shall be governed by the laws\n"
            "    of England and Wales.\n"
            "    All disputes shall be settled by arbitration.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "laws.of" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: science passage (issue #42)")
    def test_multiline_007(self):
        result = segment_text(
            "Results were analysed using a standard\n"
            "    regression model. No significant\n"
            "    difference was found.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "standard.regression" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: 5-line passage (issue #42)")
    def test_multiline_008(self):
        result = segment_text(
            "Wanted: A number of bright\n"
            "    young men to assist in the business\n"
            "    department during the Christmas\n"
            "    holidays. Promotion possible.\n"
            "    Apply to Business Manager.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text
        assert "Christmas.holidays" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: military passage (issue #42)")
    def test_multiline_009(self):
        result = segment_text(
            "The army crossed the river at dawn\n"
            "    and established a bridgehead.\n"
            "    By noon they held the ridge.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "dawn.and" not in full_text

    @pytest.mark.xfail(reason="multiline 4-space: domestic passage (issue #42)")
    def test_multiline_010(self):
        result = segment_text(
            "She arranged the flowers in the drawing\n"
            "    room while the guests arrived.\n"
            "    The evening passed pleasantly.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "drawing.room" not in full_text

    # ================================================================ FF. Mixed indent (pipeline)

    @pytest.mark.xfail(reason="mixed indent: first 4-space then no-indent (issue #42)")
    def test_mixed_001(self):
        result = segment_text(
            "He joined the business\n    department in January.\nHe left in March.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: first no-indent then 4-space (issue #42)")
    def test_mixed_002(self):
        result = segment_text(
            "She managed the advertising\ndepartment well.\n    Colleagues respected her.",
            flatten=True,
        )
        assert "advertising.department" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: 2-space then 4-space (issue #42)")
    def test_mixed_003(self):
        result = segment_text(
            "He ran the fire\n  station efficiently.\n    His deputy handled the rosters.",
            flatten=True,
        )
        assert "fire.station" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: tab then 4-space (issue #42)")
    def test_mixed_004(self):
        result = segment_text(
            "She visited the post\n\toffice.\n    The clerk was helpful.",
            flatten=True,
        )
        assert "post.office" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: 4-space then 8-space (issue #42)")
    def test_mixed_005(self):
        result = segment_text(
            "He consulted the town\n    council.\n        They agreed immediately.",
            flatten=True,
        )
        assert "town.council" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: 8-space then tab (issue #42)")
    def test_mixed_006(self):
        result = segment_text(
            "She led the health\n        department.\n\tPromotion followed quickly.",
            flatten=True,
        )
        assert "health.department" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: trailing+2-space then 4-space (issue #42)")
    def test_mixed_007(self):
        result = segment_text(
            "He chaired the finance \n  committee.\n    Minutes were duly recorded.",
            flatten=True,
        )
        assert "finance.committee" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: no-indent block of 3, middle 4-space (issue #42)")
    def test_mixed_008(self):
        result = segment_text(
            "He left the foreign\noffice.\n    Later he joined the bar.",
            flatten=True,
        )
        assert "foreign.office" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: trailing+tab then 4-space (issue #42)")
    def test_mixed_009(self):
        result = segment_text(
            "She attended the school \n\tmaster's class.\n    He was a good teacher.",
            flatten=True,
        )
        assert "school.master" not in " ".join(result)

    @pytest.mark.xfail(reason="mixed indent: 4-space with 2-trailing then no-indent (issue #42)")
    def test_mixed_010(self):
        result = segment_text(
            "He managed the night  \n    watchman's rota.\nAll guards reported to him.",
            flatten=True,
        )
        assert "night.watchman" not in " ".join(result)

    # ================================================================ GG. Stress variants (pipeline)

    @pytest.mark.xfail(reason="stress: 4-space wrap at very short word 'in.the' (issue #42)")
    def test_stress_001(self):
        result = segment_text(
            "He was employed in\n    the business department.",
            flatten=True,
        )
        assert "in.the" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap at preposition 'of.the' (issue #42)")
    def test_stress_002(self):
        result = segment_text(
            "She was in charge of\n    the advertising department.",
            flatten=True,
        )
        assert "of.the" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap at article 'a.number' (issue #42)")
    def test_stress_003(self):
        result = segment_text(
            "They wanted a\n    number of experienced staff.",
            flatten=True,
        )
        assert "a.number" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap mid-sentence business context (issue #42)")
    def test_stress_004(self):
        result = segment_text(
            "Assist in the business\n    department during the summer holidays.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap with question (issue #42)")
    def test_stress_005(self):
        result = segment_text(
            "Can you assist in the business\n    department this week?",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap in imperative sentence (issue #42)")
    def test_stress_006(self):
        result = segment_text(
            "Please apply to the Business\n    Manager before Friday.",
            flatten=True,
        )
        assert "Business.Manager" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap passive construction (issue #42)")
    def test_stress_007(self):
        result = segment_text(
            "Candidates are requested to apply to the Business\n    Manager.",
            flatten=True,
        )
        assert "Business.Manager" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap in reported speech (issue #42)")
    def test_stress_008(self):
        result = segment_text(
            "He said he worked in the business\n    department for many years.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap with em-dash context (issue #42)")
    def test_stress_009(self):
        result = segment_text(
            "The department — the business\n    department — was understaffed.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap parenthetical (issue #42)")
    def test_stress_010(self):
        result = segment_text(
            "She (head of the advertising\n    department) resigned abruptly.",
            flatten=True,
        )
        assert "advertising.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap in dialogue (issue #42)")
    def test_stress_011(self):
        result = segment_text(
            '"I work in the business\n    department," she said.',
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap after comma (issue #42)")
    def test_stress_012(self):
        result = segment_text(
            "After many years, she joined the business\n    department.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap after semicolon context (issue #42)")
    def test_stress_013(self):
        result = segment_text(
            "He worked long hours; his colleagues in the business\n    department did the same.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap in list context (issue #42)")
    def test_stress_014(self):
        result = segment_text(
            "The successful applicant will join the business\n    department or the sales team.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="stress: 4-space wrap followed by another 4-space (issue #42)")
    def test_stress_015(self):
        result = segment_text(
            "He transferred from the business\n    department to the advertising\n    department.",
            flatten=True,
        )
        full_text = " ".join(result)
        assert "business.department" not in full_text
        assert "advertising.department" not in full_text
