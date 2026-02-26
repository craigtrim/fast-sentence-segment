# -*- coding: UTF-8 -*-
"""Unit tests for NewlinesToPeriods with tab-indented continuation lines.

Note: In the full pipeline, tabs are converted to spaces BEFORE NewlinesToPeriods
runs. But when testing the component in isolation, the tab arrives as-is.
After the fix, `line.strip()` handles tabs the same as spaces.

Currently FAILING (documents the desired post-fix behavior).

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestWrapIndentTab:
    """Hard-wrapped lines where the continuation line has a tab indent."""

    # ---------------------------------------------------------------- single tab

    def test_fiction_single_tab_01(self):
        assert NewlinesToPeriods.process("She walked down the long\n\tcorridor.") == "She walked down the long corridor."

    def test_fiction_single_tab_02(self):
        assert NewlinesToPeriods.process("He opened the heavy\n\tdoor slowly.") == "He opened the heavy door slowly."

    def test_fiction_single_tab_03(self):
        assert NewlinesToPeriods.process("The sun was setting\n\tbehind the mountains.") == "The sun was setting behind the mountains."

    def test_fiction_single_tab_04(self):
        assert NewlinesToPeriods.process("A cold wind swept\n\tacross the courtyard.") == "A cold wind swept across the courtyard."

    def test_fiction_single_tab_05(self):
        assert NewlinesToPeriods.process("She had not spoken\n\tsince the incident.") == "She had not spoken since the incident."

    def test_fiction_single_tab_06(self):
        assert NewlinesToPeriods.process("He could hear voices\n\tfrom the room above.") == "He could hear voices from the room above."

    def test_fiction_single_tab_07(self):
        assert NewlinesToPeriods.process("The old man sat\n\talone by the fire.") == "The old man sat alone by the fire."

    def test_fiction_single_tab_08(self):
        assert NewlinesToPeriods.process("Rain had been falling\n\tsince early morning.") == "Rain had been falling since early morning."

    def test_fiction_single_tab_09(self):
        assert NewlinesToPeriods.process("Her hands trembled\n\tas she read the telegram.") == "Her hands trembled as she read the telegram."

    def test_fiction_single_tab_10(self):
        assert NewlinesToPeriods.process("The boy ran into\n\tthe dark forest.") == "The boy ran into the dark forest."

    def test_journalism_tab_01(self):
        assert NewlinesToPeriods.process("The minister resigned\n\tamid allegations.") == "The minister resigned amid allegations."

    def test_journalism_tab_02(self):
        assert NewlinesToPeriods.process("Authorities confirmed\n\tno injuries were reported.") == "Authorities confirmed no injuries were reported."

    def test_journalism_tab_03(self):
        assert NewlinesToPeriods.process("Share prices fell\n\ton news of the merger.") == "Share prices fell on news of the merger."

    def test_journalism_tab_04(self):
        assert NewlinesToPeriods.process("Officials are expected\n\tto meet next week.") == "Officials are expected to meet next week."

    def test_journalism_tab_05(self):
        assert NewlinesToPeriods.process("The summit will be\n\theld in Geneva.") == "The summit will be held in Geneva."

    def test_science_tab_01(self):
        assert NewlinesToPeriods.process("The reaction was\n\tcomplete after sixty minutes.") == "The reaction was complete after sixty minutes."

    def test_science_tab_02(self):
        assert NewlinesToPeriods.process("Results were analysed\n\tusing regression.") == "Results were analysed using regression."

    def test_science_tab_03(self):
        assert NewlinesToPeriods.process("The results confirmed\n\tthe hypothesis.") == "The results confirmed the hypothesis."

    def test_science_tab_04(self):
        assert NewlinesToPeriods.process("No significant difference\n\twas found.") == "No significant difference was found."

    def test_science_tab_05(self):
        assert NewlinesToPeriods.process("Participants were randomly\n\tassigned to groups.") == "Participants were randomly assigned to groups."

    def test_history_tab_01(self):
        assert NewlinesToPeriods.process("The army crossed\n\tthe river at dawn.") == "The army crossed the river at dawn."

    def test_history_tab_02(self):
        assert NewlinesToPeriods.process("The treaty was\n\tsigned by both powers.") == "The treaty was signed by both powers."

    def test_legal_tab_01(self):
        assert NewlinesToPeriods.process("The contract shall\n\tbe governed by English law.") == "The contract shall be governed by English law."

    def test_legal_tab_02(self):
        assert NewlinesToPeriods.process("All disputes shall\n\tbe settled by arbitration.") == "All disputes shall be settled by arbitration."

    def test_business_tab_01(self):
        assert NewlinesToPeriods.process("Assist in the business\n\tdepartment during the holidays.") == "Assist in the business department during the holidays."

    def test_business_tab_02(self):
        assert NewlinesToPeriods.process("The advertising\n\tdepartment was on the third floor.") == "The advertising department was on the third floor."

    def test_business_tab_03(self):
        assert NewlinesToPeriods.process("Apply to the Personnel\n\tManager before Friday.") == "Apply to the Personnel Manager before Friday."

    # ---------------------------------------------------------------- double tab

    def test_double_tab_01(self):
        assert NewlinesToPeriods.process("She walked down\n\t\tthe long corridor.") == "She walked down the long corridor."

    def test_double_tab_02(self):
        assert NewlinesToPeriods.process("He could not find\n\t\tthe missing page.") == "He could not find the missing page."

    def test_double_tab_03(self):
        assert NewlinesToPeriods.process("The storm lasted\n\t\tfor two days.") == "The storm lasted for two days."

    def test_double_tab_04(self):
        assert NewlinesToPeriods.process("Assist in the\n\t\tbusiness department.") == "Assist in the business department."

    def test_double_tab_05(self):
        assert NewlinesToPeriods.process("She had not spoken\n\t\tsince the incident.") == "She had not spoken since the incident."

    # ---------------------------------------------------------------- tab + spaces mixed

    def test_tab_then_spaces_01(self):
        assert NewlinesToPeriods.process("She walked down\n\t  the corridor.") == "She walked down the corridor."

    def test_tab_then_spaces_02(self):
        assert NewlinesToPeriods.process("He found the key\n\t  under the mat.") == "He found the key under the mat."

    def test_spaces_then_tab_01(self):
        assert NewlinesToPeriods.process("She waited by\n    \tthe window.") == "She waited by the window."

    def test_spaces_then_tab_02(self):
        assert NewlinesToPeriods.process("He ran quickly\n  \tto the exit.") == "He ran quickly to the exit."

    # ---------------------------------------------------------------- no-corruption assertions

    def test_no_corruption_business_dept(self):
        result = NewlinesToPeriods.process("assist in the business\n\tdepartment.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    def test_no_corruption_advertising_dept(self):
        result = NewlinesToPeriods.process("the advertising\n\tdepartment.")
        assert "advertising.department" not in result
        assert result == "the advertising department."

    def test_no_corruption_fire_station(self):
        result = NewlinesToPeriods.process("the fire\n\tstation.")
        assert "fire.station" not in result
        assert result == "the fire station."

    def test_no_corruption_post_office(self):
        result = NewlinesToPeriods.process("the post\n\toffice.")
        assert "post.office" not in result
        assert result == "the post office."

    def test_no_corruption_night_watchman(self):
        result = NewlinesToPeriods.process("the night\n\twatchman.")
        assert "night.watchman" not in result
        assert result == "the night watchman."

    def test_no_corruption_double_tab(self):
        result = NewlinesToPeriods.process("assist in the business\n\t\tdepartment.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    # ---------------------------------------------------------------- miscellaneous

    def test_misc_01(self):
        assert NewlinesToPeriods.process("The new policy takes\n\teffect from January.") == "The new policy takes effect from January."

    def test_misc_02(self):
        assert NewlinesToPeriods.process("Further details will\n\tbe announced in due course.") == "Further details will be announced in due course."

    def test_misc_03(self):
        assert NewlinesToPeriods.process("Tickets are available\n\tfrom the box office.") == "Tickets are available from the box office."

    def test_misc_04(self):
        assert NewlinesToPeriods.process("Applications must be\n\treceived by the deadline.") == "Applications must be received by the deadline."

    def test_misc_05(self):
        assert NewlinesToPeriods.process("Admission is free\n\tfor children under twelve.") == "Admission is free for children under twelve."

    def test_misc_06(self):
        assert NewlinesToPeriods.process("The exhibition runs\n\tuntil end of month.") == "The exhibition runs until end of month."

    def test_misc_07(self):
        assert NewlinesToPeriods.process("Please note all\n\tclaims must be written.") == "Please note all claims must be written."

    def test_misc_08(self):
        assert NewlinesToPeriods.process("This offer is\n\tsubject to availability.") == "This offer is subject to availability."

    def test_misc_09(self):
        assert NewlinesToPeriods.process("Opening hours may\n\tvary on holidays.") == "Opening hours may vary on holidays."

    def test_misc_10(self):
        assert NewlinesToPeriods.process("Copies of the report\n\tare available.") == "Copies of the report are available."
