# -*- coding: UTF-8 -*-
"""Unit tests for NewlinesToPeriods with 2-space-indented continuation lines.

Each input has a hard-wrap where the continuation line is indented with 2 spaces.
After the fix, NewlinesToPeriods strips per-line whitespace before joining, so the
result must be a single space between the wrapped words — not 3 spaces (1 inserted
+ 2 indent), and not a period.

Currently FAILING (documents the desired post-fix behavior).

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestWrapIndent2Space:
    """Hard-wrapped lines where the continuation line has a 2-space indent."""

    # ------------------------------------------------------------------ fiction

    def test_fiction_01(self):
        assert NewlinesToPeriods.process("She walked down the long\n  corridor.") == "She walked down the long corridor."

    def test_fiction_02(self):
        assert NewlinesToPeriods.process("He opened the heavy oak\n  door slowly.") == "He opened the heavy oak door slowly."

    def test_fiction_03(self):
        assert NewlinesToPeriods.process("The sun was setting behind\n  the mountains.") == "The sun was setting behind the mountains."

    def test_fiction_04(self):
        assert NewlinesToPeriods.process("A cold wind swept across\n  the empty courtyard.") == "A cold wind swept across the empty courtyard."

    def test_fiction_05(self):
        assert NewlinesToPeriods.process("She had not spoken since\n  the incident last week.") == "She had not spoken since the incident last week."

    def test_fiction_06(self):
        assert NewlinesToPeriods.process("He could hear voices coming\n  from the room above.") == "He could hear voices coming from the room above."

    def test_fiction_07(self):
        assert NewlinesToPeriods.process("The old man sat alone by\n  the dying fire.") == "The old man sat alone by the dying fire."

    def test_fiction_08(self):
        assert NewlinesToPeriods.process("Rain had been falling since\n  early that morning.") == "Rain had been falling since early that morning."

    def test_fiction_09(self):
        assert NewlinesToPeriods.process("Her hands trembled as she\n  read the telegram.") == "Her hands trembled as she read the telegram."

    def test_fiction_10(self):
        assert NewlinesToPeriods.process("The boy ran into the dark\n  forest without looking back.") == "The boy ran into the dark forest without looking back."

    def test_fiction_11(self):
        assert NewlinesToPeriods.process("Nobody answered when he\n  knocked on the door.") == "Nobody answered when he knocked on the door."

    def test_fiction_12(self):
        assert NewlinesToPeriods.process("The clock struck midnight\n  and the lights went out.") == "The clock struck midnight and the lights went out."

    def test_fiction_13(self):
        assert NewlinesToPeriods.process("Three days passed before\n  anyone noticed he was gone.") == "Three days passed before anyone noticed he was gone."

    def test_fiction_14(self):
        assert NewlinesToPeriods.process("She folded the letter and\n  placed it in her pocket.") == "She folded the letter and placed it in her pocket."

    def test_fiction_15(self):
        assert NewlinesToPeriods.process("He stared at the portrait\n  for a long time.") == "He stared at the portrait for a long time."

    def test_fiction_16(self):
        assert NewlinesToPeriods.process("The carriage stopped outside\n  the inn at dusk.") == "The carriage stopped outside the inn at dusk."

    def test_fiction_17(self):
        assert NewlinesToPeriods.process("She left before dawn without\n  waking the others.") == "She left before dawn without waking the others."

    def test_fiction_18(self):
        assert NewlinesToPeriods.process("The candle burned low in\n  the draughty room.") == "The candle burned low in the draughty room."

    def test_fiction_19(self):
        assert NewlinesToPeriods.process("Beyond the gate lay a wild\n  and overgrown garden.") == "Beyond the gate lay a wild and overgrown garden."

    def test_fiction_20(self):
        assert NewlinesToPeriods.process("All the while she kept her\n  eyes fixed on the horizon.") == "All the while she kept her eyes fixed on the horizon."

    # ------------------------------------------------------------ journalism

    def test_journalism_01(self):
        assert NewlinesToPeriods.process("The minister resigned amid\n  allegations of misconduct.") == "The minister resigned amid allegations of misconduct."

    def test_journalism_02(self):
        assert NewlinesToPeriods.process("Authorities confirmed that no\n  injuries had been reported.") == "Authorities confirmed that no injuries had been reported."

    def test_journalism_03(self):
        assert NewlinesToPeriods.process("Share prices fell sharply on\n  news of the merger collapse.") == "Share prices fell sharply on news of the merger collapse."

    def test_journalism_04(self):
        assert NewlinesToPeriods.process("The rescue team located the\n  survivors after a three-day search.") == "The rescue team located the survivors after a three-day search."

    def test_journalism_05(self):
        assert NewlinesToPeriods.process("Officials are expected to meet\n  again early next week.") == "Officials are expected to meet again early next week."

    def test_journalism_06(self):
        assert NewlinesToPeriods.process("The verdict was greeted with\n  protests outside the courtroom.") == "The verdict was greeted with protests outside the courtroom."

    def test_journalism_07(self):
        assert NewlinesToPeriods.process("Flood waters reached record\n  levels in several districts.") == "Flood waters reached record levels in several districts."

    def test_journalism_08(self):
        assert NewlinesToPeriods.process("The company confirmed it was\n  in talks with potential buyers.") == "The company confirmed it was in talks with potential buyers."

    def test_journalism_09(self):
        assert NewlinesToPeriods.process("Three suspects have been\n  arrested in connection with the theft.") == "Three suspects have been arrested in connection with the theft."

    def test_journalism_10(self):
        assert NewlinesToPeriods.process("The prime minister called the\n  result a great victory for the party.") == "The prime minister called the result a great victory for the party."

    # ------------------------------------------------------------ scientific

    def test_science_01(self):
        assert NewlinesToPeriods.process("The reaction was complete after\n  sixty minutes at room temperature.") == "The reaction was complete after sixty minutes at room temperature."

    def test_science_02(self):
        assert NewlinesToPeriods.process("Samples were analysed using\n  high-performance liquid chromatography.") == "Samples were analysed using high-performance liquid chromatography."

    def test_science_03(self):
        assert NewlinesToPeriods.process("The results confirmed the\n  original hypothesis.") == "The results confirmed the original hypothesis."

    def test_science_04(self):
        assert NewlinesToPeriods.process("Control subjects showed no\n  significant change over the period.") == "Control subjects showed no significant change over the period."

    def test_science_05(self):
        assert NewlinesToPeriods.process("The neural network was trained\n  on a dataset of fifty thousand examples.") == "The neural network was trained on a dataset of fifty thousand examples."

    def test_science_06(self):
        assert NewlinesToPeriods.process("Dose-response curves were\n  plotted for each compound.") == "Dose-response curves were plotted for each compound."

    def test_science_07(self):
        assert NewlinesToPeriods.process("The observations were consistent\n  with the theoretical prediction.") == "The observations were consistent with the theoretical prediction."

    def test_science_08(self):
        assert NewlinesToPeriods.process("Tissue sections were stained\n  using the standard haematoxylin protocol.") == "Tissue sections were stained using the standard haematoxylin protocol."

    def test_science_09(self):
        assert NewlinesToPeriods.process("The effect was statistically\n  significant at the p < 0.05 level.") == "The effect was statistically significant at the p < 0.05 level."

    def test_science_10(self):
        assert NewlinesToPeriods.process("Cell viability was assessed\n  using a fluorescence assay.") == "Cell viability was assessed using a fluorescence assay."

    # ------------------------------------------------------------ historical

    def test_history_01(self):
        assert NewlinesToPeriods.process("The emperor issued a decree\n  forbidding all foreign trade.") == "The emperor issued a decree forbidding all foreign trade."

    def test_history_02(self):
        assert NewlinesToPeriods.process("The city was besieged for\n  seven months before it fell.") == "The city was besieged for seven months before it fell."

    def test_history_03(self):
        assert NewlinesToPeriods.process("The explorer set sail from\n  Lisbon in the spring of 1498.") == "The explorer set sail from Lisbon in the spring of 1498."

    def test_history_04(self):
        assert NewlinesToPeriods.process("Peace negotiations began in\n  Geneva in October of that year.") == "Peace negotiations began in Geneva in October of that year."

    def test_history_05(self):
        assert NewlinesToPeriods.process("The revolution spread quickly\n  to the neighbouring provinces.") == "The revolution spread quickly to the neighbouring provinces."

    # ------------------------------------------------------------ legal / formal

    def test_legal_01(self):
        assert NewlinesToPeriods.process("The contract shall be governed\n  by the laws of England and Wales.") == "The contract shall be governed by the laws of England and Wales."

    def test_legal_02(self):
        assert NewlinesToPeriods.process("All disputes shall be settled\n  by binding arbitration.") == "All disputes shall be settled by binding arbitration."

    def test_legal_03(self):
        assert NewlinesToPeriods.process("The vendor warrants that the\n  goods are free from defect.") == "The vendor warrants that the goods are free from defect."

    def test_legal_04(self):
        assert NewlinesToPeriods.process("No liability shall arise where\n  the loss was unforeseeable.") == "No liability shall arise where the loss was unforeseeable."

    def test_legal_05(self):
        assert NewlinesToPeriods.process("The parties agree that time\n  is of the essence.") == "The parties agree that time is of the essence."

    # ------------------------------------------------------------ instructional

    def test_instructions_01(self):
        assert NewlinesToPeriods.process("Connect the cable to the\n  port labelled AUX.") == "Connect the cable to the port labelled AUX."

    def test_instructions_02(self):
        assert NewlinesToPeriods.process("Allow the adhesive to dry\n  for at least two hours.") == "Allow the adhesive to dry for at least two hours."

    def test_instructions_03(self):
        assert NewlinesToPeriods.process("Switch off the power before\n  removing the cover.") == "Switch off the power before removing the cover."

    def test_instructions_04(self):
        assert NewlinesToPeriods.process("Repeat the process until\n  all the pieces are joined.") == "Repeat the process until all the pieces are joined."

    def test_instructions_05(self):
        assert NewlinesToPeriods.process("Tighten the bolt with\n  a 10mm spanner.") == "Tighten the bolt with a 10mm spanner."

    # ------------------------------------------------------------ business / advertisement

    def test_business_01(self):
        assert NewlinesToPeriods.process("Assist in the business\n  department during the holidays.") == "Assist in the business department during the holidays."

    def test_business_02(self):
        assert NewlinesToPeriods.process("Apply to the Personnel\n  Manager before Friday.") == "Apply to the Personnel Manager before Friday."

    def test_business_03(self):
        assert NewlinesToPeriods.process("The advertising\n  budget was increased by ten percent.") == "The advertising budget was increased by ten percent."

    def test_business_04(self):
        assert NewlinesToPeriods.process("She joined the marketing\n  team in January.") == "She joined the marketing team in January."

    def test_business_05(self):
        assert NewlinesToPeriods.process("The annual report is\n  available on request.") == "The annual report is available on request."

    # ------------------------------------------------------------ varied lengths

    def test_short_wrap_01(self):
        assert NewlinesToPeriods.process("He ran\n  fast.") == "He ran fast."

    def test_short_wrap_02(self):
        assert NewlinesToPeriods.process("She wept\n  bitterly.") == "She wept bitterly."

    def test_medium_wrap_01(self):
        assert NewlinesToPeriods.process("The storm lasted for\n  two days.") == "The storm lasted for two days."

    def test_medium_wrap_02(self):
        assert NewlinesToPeriods.process("He could not find the\n  missing page.") == "He could not find the missing page."

    def test_long_wrap_01(self):
        assert NewlinesToPeriods.process("The committee reviewed all of the\n  submitted applications carefully.") == "The committee reviewed all of the submitted applications carefully."

    def test_long_wrap_02(self):
        assert NewlinesToPeriods.process("She had spent three years perfecting\n  the technique before publishing.") == "She had spent three years perfecting the technique before publishing."

    # ------------------------------------------------------------ no-corruption assertions

    def test_no_corruption_01(self):
        result = NewlinesToPeriods.process("assist in the business\n  department during the holidays.")
        assert "business.department" not in result
        assert result == "assist in the business department during the holidays."

    def test_no_corruption_02(self):
        result = NewlinesToPeriods.process("bright young\n  men applied.")
        assert "young.men" not in result
        assert result == "bright young men applied."

    def test_no_corruption_03(self):
        result = NewlinesToPeriods.process("the advertising\n  department.")
        assert "advertising.department" not in result
        assert result == "the advertising department."

    def test_no_corruption_04(self):
        result = NewlinesToPeriods.process("the marketing\n  team.")
        assert "marketing.team" not in result
        assert result == "the marketing team."

    def test_no_corruption_05(self):
        result = NewlinesToPeriods.process("the research\n  findings.")
        assert "research.findings" not in result
        assert result == "the research findings."

    def test_no_corruption_06(self):
        result = NewlinesToPeriods.process("the accounting\n  department.")
        assert "accounting.department" not in result
        assert result == "the accounting department."

    def test_no_corruption_07(self):
        result = NewlinesToPeriods.process("the personnel\n  manager.")
        assert "personnel.manager" not in result
        assert result == "the personnel manager."

    def test_no_corruption_08(self):
        result = NewlinesToPeriods.process("the sales\n  figures.")
        assert "sales.figures" not in result
        assert result == "the sales figures."

    def test_no_corruption_09(self):
        result = NewlinesToPeriods.process("the night\n  watchman.")
        assert "night.watchman" not in result
        assert result == "the night watchman."

    def test_no_corruption_10(self):
        result = NewlinesToPeriods.process("the fire\n  station.")
        assert "fire.station" not in result
        assert result == "the fire station."

    # ------------------------------------------------------------ wrap at various positions

    def test_wrap_at_50_chars_01(self):
        assert NewlinesToPeriods.process("The suspect was seen leaving the building\n  at around eleven in the evening.") == "The suspect was seen leaving the building at around eleven in the evening."

    def test_wrap_at_55_chars_01(self):
        assert NewlinesToPeriods.process("She had not visited the town since\n  her childhood.") == "She had not visited the town since her childhood."

    def test_wrap_at_60_chars_01(self):
        assert NewlinesToPeriods.process("The bridge had stood for four hundred\n  years without incident.") == "The bridge had stood for four hundred years without incident."

    def test_wrap_at_65_chars_01(self):
        assert NewlinesToPeriods.process("No one who had witnessed the scene\n  would easily forget it.") == "No one who had witnessed the scene would easily forget it."

    def test_wrap_at_70_chars_01(self):
        assert NewlinesToPeriods.process("The document had been classified for\n  fifty years.") == "The document had been classified for fifty years."

    def test_wrap_at_75_chars_01(self):
        assert NewlinesToPeriods.process("She had always hoped to travel but\n  never found the opportunity.") == "She had always hoped to travel but never found the opportunity."

    def test_wrap_at_80_chars_01(self):
        assert NewlinesToPeriods.process("He had served the company faithfully\n  for thirty years.") == "He had served the company faithfully for thirty years."

    # ------------------------------------------------------------ miscellaneous

    def test_misc_01(self):
        assert NewlinesToPeriods.process("The new policy takes\n  effect from January.") == "The new policy takes effect from January."

    def test_misc_02(self):
        assert NewlinesToPeriods.process("Please note that all\n  claims must be made in writing.") == "Please note that all claims must be made in writing."

    def test_misc_03(self):
        assert NewlinesToPeriods.process("Further details will be\n  announced in due course.") == "Further details will be announced in due course."

    def test_misc_04(self):
        assert NewlinesToPeriods.process("This offer is subject to\n  availability.") == "This offer is subject to availability."

    def test_misc_05(self):
        assert NewlinesToPeriods.process("Tickets are available from\n  the box office.") == "Tickets are available from the box office."

    def test_misc_06(self):
        assert NewlinesToPeriods.process("The exhibition runs until\n  the end of the month.") == "The exhibition runs until the end of the month."

    def test_misc_07(self):
        assert NewlinesToPeriods.process("Applications must be received\n  by the closing date.") == "Applications must be received by the closing date."

    def test_misc_08(self):
        assert NewlinesToPeriods.process("Copies of the report are\n  available on request.") == "Copies of the report are available on request."

    def test_misc_09(self):
        assert NewlinesToPeriods.process("Admission is free for\n  children under twelve.") == "Admission is free for children under twelve."

    def test_misc_10(self):
        assert NewlinesToPeriods.process("Opening hours may vary\n  during public holidays.") == "Opening hours may vary during public holidays."
