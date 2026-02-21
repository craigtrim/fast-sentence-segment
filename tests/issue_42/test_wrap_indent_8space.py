# -*- coding: UTF-8 -*-
"""Unit tests for NewlinesToPeriods with 8-space-indented continuation lines.

After the fix, stripping per-line whitespace means 8-space indents on
continuation lines produce a single space join, not 9 spaces → `". . . . ."`.

Currently FAILING (documents the desired post-fix behavior).

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestWrapIndent8Space:
    """Hard-wrapped lines where the continuation line has an 8-space indent."""

    def test_fiction_01(self):
        assert NewlinesToPeriods.process("She walked down the long\n        corridor.") == "She walked down the long corridor."

    def test_fiction_02(self):
        assert NewlinesToPeriods.process("He opened the heavy oak\n        door slowly.") == "He opened the heavy oak door slowly."

    def test_fiction_03(self):
        assert NewlinesToPeriods.process("The sun was setting behind\n        the mountains.") == "The sun was setting behind the mountains."

    def test_fiction_04(self):
        assert NewlinesToPeriods.process("A cold wind swept across\n        the courtyard.") == "A cold wind swept across the courtyard."

    def test_fiction_05(self):
        assert NewlinesToPeriods.process("She had not spoken since\n        the incident.") == "She had not spoken since the incident."

    def test_fiction_06(self):
        assert NewlinesToPeriods.process("He could hear voices coming\n        from the room above.") == "He could hear voices coming from the room above."

    def test_fiction_07(self):
        assert NewlinesToPeriods.process("The old man sat alone by\n        the dying fire.") == "The old man sat alone by the dying fire."

    def test_fiction_08(self):
        assert NewlinesToPeriods.process("Rain had been falling since\n        early morning.") == "Rain had been falling since early morning."

    def test_fiction_09(self):
        assert NewlinesToPeriods.process("Her hands trembled as she\n        read the letter.") == "Her hands trembled as she read the letter."

    def test_fiction_10(self):
        assert NewlinesToPeriods.process("The boy ran into the dark\n        forest without looking back.") == "The boy ran into the dark forest without looking back."

    def test_journalism_01(self):
        assert NewlinesToPeriods.process("The minister resigned amid\n        allegations of misconduct.") == "The minister resigned amid allegations of misconduct."

    def test_journalism_02(self):
        assert NewlinesToPeriods.process("Authorities confirmed that\n        no injuries were reported.") == "Authorities confirmed that no injuries were reported."

    def test_journalism_03(self):
        assert NewlinesToPeriods.process("Share prices fell sharply\n        on news of the merger.") == "Share prices fell sharply on news of the merger."

    def test_journalism_04(self):
        assert NewlinesToPeriods.process("The rescue team located\n        survivors after three days.") == "The rescue team located survivors after three days."

    def test_journalism_05(self):
        assert NewlinesToPeriods.process("Officials are expected to\n        meet again next week.") == "Officials are expected to meet again next week."

    def test_science_01(self):
        assert NewlinesToPeriods.process("The reaction was complete\n        after sixty minutes.") == "The reaction was complete after sixty minutes."

    def test_science_02(self):
        assert NewlinesToPeriods.process("Samples were analysed using\n        chromatography methods.") == "Samples were analysed using chromatography methods."

    def test_science_03(self):
        assert NewlinesToPeriods.process("The results confirmed\n        the original hypothesis.") == "The results confirmed the original hypothesis."

    def test_science_04(self):
        assert NewlinesToPeriods.process("Control subjects showed no\n        significant change.") == "Control subjects showed no significant change."

    def test_science_05(self):
        assert NewlinesToPeriods.process("The neural network was\n        trained on fifty thousand examples.") == "The neural network was trained on fifty thousand examples."

    def test_history_01(self):
        assert NewlinesToPeriods.process("The army crossed the river\n        at dawn on June fourth.") == "The army crossed the river at dawn on June fourth."

    def test_history_02(self):
        assert NewlinesToPeriods.process("The treaty was signed by\n        representatives of both powers.") == "The treaty was signed by representatives of both powers."

    def test_history_03(self):
        assert NewlinesToPeriods.process("By decade's end the\n        population had doubled.") == "By decade's end the population had doubled."

    def test_history_04(self):
        assert NewlinesToPeriods.process("The king died without\n        a legitimate heir.") == "The king died without a legitimate heir."

    def test_legal_01(self):
        assert NewlinesToPeriods.process("The party of the first part\n        agrees to deliver by Friday.") == "The party of the first part agrees to deliver by Friday."

    def test_legal_02(self):
        assert NewlinesToPeriods.process("Any dispute arising under\n        this agreement shall be arbitrated.") == "Any dispute arising under this agreement shall be arbitrated."

    def test_business_01(self):
        assert NewlinesToPeriods.process("Assist in the business\n        department during the holidays.") == "Assist in the business department during the holidays."

    def test_business_02(self):
        assert NewlinesToPeriods.process("The advertising\n        department was on the third floor.") == "The advertising department was on the third floor."

    def test_business_03(self):
        assert NewlinesToPeriods.process("She managed the marketing\n        team for a decade.") == "She managed the marketing team for a decade."

    def test_business_04(self):
        assert NewlinesToPeriods.process("Apply to the Personnel\n        Manager before the deadline.") == "Apply to the Personnel Manager before the deadline."

    # no-corruption assertions

    def test_no_corruption_01(self):
        result = NewlinesToPeriods.process("assist in the business\n        department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    def test_no_corruption_02(self):
        result = NewlinesToPeriods.process("the advertising\n        department.")
        assert "advertising.department" not in result
        assert result == "the advertising department."

    def test_no_corruption_03(self):
        result = NewlinesToPeriods.process("the marketing\n        team.")
        assert "marketing.team" not in result
        assert result == "the marketing team."

    def test_no_corruption_04(self):
        result = NewlinesToPeriods.process("the night\n        watchman.")
        assert "night.watchman" not in result
        assert result == "the night watchman."

    def test_no_corruption_05(self):
        result = NewlinesToPeriods.process("the fire\n        station.")
        assert "fire.station" not in result
        assert result == "the fire station."

    def test_no_corruption_06(self):
        result = NewlinesToPeriods.process("the foreign\n        office.")
        assert "foreign.office" not in result
        assert result == "the foreign office."

    def test_no_corruption_07(self):
        result = NewlinesToPeriods.process("the post\n        office.")
        assert "post.office" not in result
        assert result == "the post office."

    def test_no_corruption_08(self):
        result = NewlinesToPeriods.process("the town\n        council.")
        assert "town.council" not in result
        assert result == "the town council."

    def test_no_corruption_09(self):
        result = NewlinesToPeriods.process("the health\n        department.")
        assert "health.department" not in result
        assert result == "the health department."

    def test_no_corruption_10(self):
        result = NewlinesToPeriods.process("the finance\n        committee.")
        assert "finance.committee" not in result
        assert result == "the finance committee."

    def test_wrap_short_01(self):
        assert NewlinesToPeriods.process("He ran\n        fast.") == "He ran fast."

    def test_wrap_short_02(self):
        assert NewlinesToPeriods.process("She wept\n        bitterly.") == "She wept bitterly."

    def test_wrap_medium_01(self):
        assert NewlinesToPeriods.process("The storm lasted\n        for two days.") == "The storm lasted for two days."

    def test_wrap_medium_02(self):
        assert NewlinesToPeriods.process("He could not find\n        the missing page.") == "He could not find the missing page."

    def test_wrap_long_01(self):
        assert NewlinesToPeriods.process("The committee reviewed all\n        submitted applications carefully.") == "The committee reviewed all submitted applications carefully."

    def test_wrap_long_02(self):
        assert NewlinesToPeriods.process("She had spent three years\n        perfecting the technique.") == "She had spent three years perfecting the technique."

    def test_misc_01(self):
        assert NewlinesToPeriods.process("The new policy takes\n        effect from January.") == "The new policy takes effect from January."

    def test_misc_02(self):
        assert NewlinesToPeriods.process("Further details will be\n        announced in due course.") == "Further details will be announced in due course."

    def test_misc_03(self):
        assert NewlinesToPeriods.process("Tickets are available from\n        the box office.") == "Tickets are available from the box office."

    def test_misc_04(self):
        assert NewlinesToPeriods.process("Applications must be received\n        by the closing date.") == "Applications must be received by the closing date."

    def test_misc_05(self):
        assert NewlinesToPeriods.process("Admission is free for\n        children under twelve.") == "Admission is free for children under twelve."

    def test_misc_06(self):
        assert NewlinesToPeriods.process("The exhibition runs until\n        the end of the month.") == "The exhibition runs until the end of the month."

    def test_misc_07(self):
        assert NewlinesToPeriods.process("Please note that all\n        claims must be in writing.") == "Please note that all claims must be in writing."

    def test_misc_08(self):
        assert NewlinesToPeriods.process("This offer is subject\n        to availability.") == "This offer is subject to availability."

    def test_misc_09(self):
        assert NewlinesToPeriods.process("The exhibition runs from\n        Monday to Saturday.") == "The exhibition runs from Monday to Saturday."

    def test_misc_10(self):
        assert NewlinesToPeriods.process("Copies of the report\n        are on request.") == "Copies of the report are on request."
