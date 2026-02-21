# -*- coding: UTF-8 -*-
"""Unit tests for NewlinesToPeriods across systematic column width variations.

Hard-wrapping occurs at different column widths depending on the tool and era:
  30, 40, 50, 55, 60, 65, 68, 70, 72, 74, 76, 78, 80 characters.

Each test uses a 4-space indent (the primary bug trigger) at a specific
column width, verifying clean single-space join after the fix.

Currently FAILING (documents the desired post-fix behavior).

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestWrapColumnWidths:
    """Systematic column-width variations with 4-space-indented continuation lines."""

    # ---------------------------------------------------------------- wrap at ~30 chars

    def test_col30_fiction_01(self):
        assert NewlinesToPeriods.process("She walked\n    down the corridor.") == "She walked down the corridor."

    def test_col30_fiction_02(self):
        assert NewlinesToPeriods.process("He opened\n    the heavy door.") == "He opened the heavy door."

    def test_col30_fiction_03(self):
        assert NewlinesToPeriods.process("The sun\n    was setting fast.") == "The sun was setting fast."

    def test_col30_business_01(self):
        result = NewlinesToPeriods.process("the business\n    department.")
        assert "business.department" not in result
        assert result == "the business department."

    def test_col30_business_02(self):
        result = NewlinesToPeriods.process("the marketing\n    team.")
        assert "marketing.team" not in result
        assert result == "the marketing team."

    def test_col30_news_01(self):
        assert NewlinesToPeriods.process("The minister\n    resigned today.") == "The minister resigned today."

    def test_col30_science_01(self):
        assert NewlinesToPeriods.process("The reaction\n    was complete.") == "The reaction was complete."

    def test_col30_history_01(self):
        assert NewlinesToPeriods.process("The army\n    crossed the river.") == "The army crossed the river."

    def test_col30_legal_01(self):
        assert NewlinesToPeriods.process("The contract\n    is binding.") == "The contract is binding."

    def test_col30_misc_01(self):
        assert NewlinesToPeriods.process("Apply to\n    the manager.") == "Apply to the manager."

    # ---------------------------------------------------------------- wrap at ~40 chars

    def test_col40_fiction_01(self):
        assert NewlinesToPeriods.process("She walked down the long\n    corridor.") == "She walked down the long corridor."

    def test_col40_fiction_02(self):
        assert NewlinesToPeriods.process("He opened the heavy oak\n    door slowly.") == "He opened the heavy oak door slowly."

    def test_col40_fiction_03(self):
        assert NewlinesToPeriods.process("A cold wind swept across\n    the courtyard.") == "A cold wind swept across the courtyard."

    def test_col40_fiction_04(self):
        assert NewlinesToPeriods.process("She had not spoken since\n    the incident.") == "She had not spoken since the incident."

    def test_col40_business_01(self):
        result = NewlinesToPeriods.process("assist in the business\n    department.")
        assert "business.department" not in result
        assert result == "assist in the business department."

    def test_col40_business_02(self):
        result = NewlinesToPeriods.process("she managed the marketing\n    department.")
        assert "marketing.department" not in result
        assert result == "she managed the marketing department."

    def test_col40_news_01(self):
        assert NewlinesToPeriods.process("The minister resigned amid\n    allegations.") == "The minister resigned amid allegations."

    def test_col40_science_01(self):
        assert NewlinesToPeriods.process("The reaction was complete\n    after sixty minutes.") == "The reaction was complete after sixty minutes."

    def test_col40_history_01(self):
        assert NewlinesToPeriods.process("The army crossed the river\n    at dawn.") == "The army crossed the river at dawn."

    def test_col40_legal_01(self):
        assert NewlinesToPeriods.process("The contract shall be\n    governed by English law.") == "The contract shall be governed by English law."

    # ---------------------------------------------------------------- wrap at ~50 chars

    def test_col50_fiction_01(self):
        assert NewlinesToPeriods.process("She walked down the long dark\n    corridor.") == "She walked down the long dark corridor."

    def test_col50_fiction_02(self):
        assert NewlinesToPeriods.process("He could hear voices coming from\n    the room above.") == "He could hear voices coming from the room above."

    def test_col50_fiction_03(self):
        assert NewlinesToPeriods.process("The boy ran into the dark forest\n    without looking back.") == "The boy ran into the dark forest without looking back."

    def test_col50_fiction_04(self):
        assert NewlinesToPeriods.process("Rain had been falling since early\n    that morning.") == "Rain had been falling since early that morning."

    def test_col50_fiction_05(self):
        assert NewlinesToPeriods.process("Nobody answered when he knocked\n    on the door.") == "Nobody answered when he knocked on the door."

    def test_col50_business_01(self):
        result = NewlinesToPeriods.process("Wanted: bright young men to assist\n    in the business department.")
        assert "assist.in" not in result
        assert result == "Wanted: bright young men to assist in the business department."

    def test_col50_news_01(self):
        assert NewlinesToPeriods.process("Three people were injured when\n    a van mounted the pavement.") == "Three people were injured when a van mounted the pavement."

    def test_col50_science_01(self):
        assert NewlinesToPeriods.process("Results were analysed using a\n    standard regression model.") == "Results were analysed using a standard regression model."

    def test_col50_history_01(self):
        assert NewlinesToPeriods.process("The treaty was signed by representatives\n    of both powers.") == "The treaty was signed by representatives of both powers."

    def test_col50_legal_01(self):
        assert NewlinesToPeriods.process("The party of the first part agrees\n    to deliver by Friday.") == "The party of the first part agrees to deliver by Friday."

    # ---------------------------------------------------------------- wrap at ~55 chars

    def test_col55_fiction_01(self):
        assert NewlinesToPeriods.process("She had not visited the town since\n    her childhood.") == "She had not visited the town since her childhood."

    def test_col55_fiction_02(self):
        assert NewlinesToPeriods.process("The clock struck midnight and the\n    lights went out.") == "The clock struck midnight and the lights went out."

    def test_col55_fiction_03(self):
        assert NewlinesToPeriods.process("Three days passed before anyone\n    noticed he was gone.") == "Three days passed before anyone noticed he was gone."

    def test_col55_fiction_04(self):
        assert NewlinesToPeriods.process("She folded the letter and placed\n    it in her pocket.") == "She folded the letter and placed it in her pocket."

    def test_col55_business_01(self):
        result = NewlinesToPeriods.process("Wanted: A number of bright young men\n    to assist in the business department.")
        assert "young.men" not in result
        assert result == "Wanted: A number of bright young men to assist in the business department."

    def test_col55_news_01(self):
        assert NewlinesToPeriods.process("The company reported record profits\n    for the third quarter.") == "The company reported record profits for the third quarter."

    def test_col55_science_01(self):
        assert NewlinesToPeriods.process("The experiment was repeated three times\n    to confirm reproducibility.") == "The experiment was repeated three times to confirm reproducibility."

    def test_col55_history_01(self):
        assert NewlinesToPeriods.process("By the end of the decade the population\n    had doubled in size.") == "By the end of the decade the population had doubled in size."

    def test_col55_legal_01(self):
        assert NewlinesToPeriods.process("Any dispute arising under this agreement\n    shall be referred to arbitration.") == "Any dispute arising under this agreement shall be referred to arbitration."

    def test_col55_travel_01(self):
        assert NewlinesToPeriods.process("The road wound up through pine forests\n    to a mountain plateau.") == "The road wound up through pine forests to a mountain plateau."

    # ---------------------------------------------------------------- wrap at ~60 chars

    def test_col60_fiction_01(self):
        assert NewlinesToPeriods.process("The house had been empty for more than twenty\n    years before they bought it.") == "The house had been empty for more than twenty years before they bought it."

    def test_col60_fiction_02(self):
        assert NewlinesToPeriods.process("She stared at the portrait for a long\n    time without speaking.") == "She stared at the portrait for a long time without speaking."

    def test_col60_fiction_03(self):
        assert NewlinesToPeriods.process("The carriage stopped outside the inn\n    at dusk and a man stepped out.") == "The carriage stopped outside the inn at dusk and a man stepped out."

    def test_col60_fiction_04(self):
        assert NewlinesToPeriods.process("Beyond the gate lay a wild and overgrown\n    garden.") == "Beyond the gate lay a wild and overgrown garden."

    def test_col60_fiction_05(self):
        assert NewlinesToPeriods.process("All the while she kept her eyes fixed\n    on the horizon.") == "All the while she kept her eyes fixed on the horizon."

    def test_col60_business_01(self):
        result = NewlinesToPeriods.process("Wanted: A number of bright young men to\n    assist in the business department.")
        assert "to.assist" not in result
        assert result == "Wanted: A number of bright young men to assist in the business department."

    def test_col60_news_01(self):
        assert NewlinesToPeriods.process("Officials confirmed that negotiations\n    would resume next week.") == "Officials confirmed that negotiations would resume next week."

    def test_col60_science_01(self):
        assert NewlinesToPeriods.process("Data were collected over a period of six\n    months from twelve sites.") == "Data were collected over a period of six months from twelve sites."

    def test_col60_history_01(self):
        assert NewlinesToPeriods.process("The king died without a legitimate heir\n    and the succession was disputed.") == "The king died without a legitimate heir and the succession was disputed."

    def test_col60_legal_01(self):
        assert NewlinesToPeriods.process("Notwithstanding any prior agreement,\n    this contract supersedes all others.") == "Notwithstanding any prior agreement, this contract supersedes all others."

    # ---------------------------------------------------------------- wrap at ~65 chars

    def test_col65_fiction_01(self):
        assert NewlinesToPeriods.process("They found a trapdoor concealed beneath the\n    oriental rug in the study.") == "They found a trapdoor concealed beneath the oriental rug in the study."

    def test_col65_fiction_02(self):
        assert NewlinesToPeriods.process("She left before dawn without waking\n    the others who slept soundly.") == "She left before dawn without waking the others who slept soundly."

    def test_col65_fiction_03(self):
        assert NewlinesToPeriods.process("The candle burned low in the draughty\n    room as she continued reading.") == "The candle burned low in the draughty room as she continued reading."

    def test_col65_business_01(self):
        result = NewlinesToPeriods.process("Wanted: A number of bright young men to assist\n    in the business department.")
        assert "assist.in" not in result
        assert result == "Wanted: A number of bright young men to assist in the business department."

    def test_col65_news_01(self):
        assert NewlinesToPeriods.process("The bill passed by a narrow margin of\n    just six votes.") == "The bill passed by a narrow margin of just six votes."

    def test_col65_science_01(self):
        assert NewlinesToPeriods.process("The group receiving the treatment showed\n    significantly better outcomes.") == "The group receiving the treatment showed significantly better outcomes."

    def test_col65_history_01(self):
        assert NewlinesToPeriods.process("Trade routes across the desert were\n    established in the first century.") == "Trade routes across the desert were established in the first century."

    def test_col65_legal_01(self):
        assert NewlinesToPeriods.process("The court found in favour of the plaintiff\n    on all counts.") == "The court found in favour of the plaintiff on all counts."

    def test_col65_travel_01(self):
        assert NewlinesToPeriods.process("From the terrace we could see the entire\n    valley spread below us.") == "From the terrace we could see the entire valley spread below us."

    def test_col65_letter_01(self):
        assert NewlinesToPeriods.process("I remain, as ever, your most obedient\n    servant.") == "I remain, as ever, your most obedient servant."

    # ---------------------------------------------------------------- wrap at ~68 chars

    def test_col68_fiction_01(self):
        assert NewlinesToPeriods.process("No one had expected the election result to be\n    so decisive.") == "No one had expected the election result to be so decisive."

    def test_col68_fiction_02(self):
        assert NewlinesToPeriods.process("She spent the better part of three weeks\n    transcribing the original text.") == "She spent the better part of three weeks transcribing the original text."

    def test_col68_business_01(self):
        result = NewlinesToPeriods.process("Wanted: A number of bright young men to assist in\n    the business department.")
        assert "in.the" not in result
        assert result == "Wanted: A number of bright young men to assist in the business department."

    def test_col68_news_01(self):
        assert NewlinesToPeriods.process("Thousands of commuters faced delays after\n    signal failures halted trains.") == "Thousands of commuters faced delays after signal failures halted trains."

    def test_col68_science_01(self):
        assert NewlinesToPeriods.process("These findings suggest that early\n    intervention is beneficial.") == "These findings suggest that early intervention is beneficial."

    # ---------------------------------------------------------------- wrap at ~70 chars (standard Gutenberg)

    def test_col70_dreiser_exact(self):
        result = NewlinesToPeriods.process(
            "Wanted: A number of bright young men to assist in the business\n"
            "    department during the Christmas holidays."
        )
        assert "business.department" not in result
        assert result == "Wanted: A number of bright young men to assist in the business department during the Christmas holidays."

    def test_col70_fiction_01(self):
        assert NewlinesToPeriods.process("He had lived in the town for twenty years without once\n    feeling truly at home.") == "He had lived in the town for twenty years without once feeling truly at home."

    def test_col70_fiction_02(self):
        assert NewlinesToPeriods.process("The trial lasted three weeks and attracted reporters\n    from as far away as London.") == "The trial lasted three weeks and attracted reporters from as far away as London."

    def test_col70_fiction_03(self):
        assert NewlinesToPeriods.process("She understood immediately what he had meant by his\n    remarks at dinner the night before.") == "She understood immediately what he had meant by his remarks at dinner the night before."

    def test_col70_fiction_04(self):
        assert NewlinesToPeriods.process("The enormous mahogany writing-desk that had been his\n    grandfather's stood against the far wall.") == "The enormous mahogany writing-desk that had been his grandfather's stood against the far wall."

    def test_col70_news_01(self):
        assert NewlinesToPeriods.process("The summit will be held in Geneva at the end\n    of the month.") == "The summit will be held in Geneva at the end of the month."

    def test_col70_science_01(self):
        assert NewlinesToPeriods.process("Participants were randomly assigned to one of\n    three experimental groups.") == "Participants were randomly assigned to one of three experimental groups."

    def test_col70_history_01(self):
        assert NewlinesToPeriods.process("On the fourteenth of July the Bastille was\n    stormed by the crowd.") == "On the fourteenth of July the Bastille was stormed by the crowd."

    def test_col70_legal_01(self):
        assert NewlinesToPeriods.process("This deed is made this day between\n    the parties named herein.") == "This deed is made this day between the parties named herein."

    def test_col70_travel_01(self):
        assert NewlinesToPeriods.process("The cathedral dominates the skyline and\n    can be seen from miles away.") == "The cathedral dominates the skyline and can be seen from miles away."

    # ---------------------------------------------------------------- wrap at ~72 chars

    def test_col72_fiction_01(self):
        assert NewlinesToPeriods.process("The ancient library contained thousands of manuscripts\n    not yet catalogued.") == "The ancient library contained thousands of manuscripts not yet catalogued."

    def test_col72_fiction_02(self):
        assert NewlinesToPeriods.process("Her expression changed so suddenly and so completely\n    that even he was startled.") == "Her expression changed so suddenly and so completely that even he was startled."

    def test_col72_business_01(self):
        result = NewlinesToPeriods.process(
            "Wanted: A number of bright young men to assist in the\n"
            "    business department during the holidays."
        )
        assert "the.business" not in result
        assert result == "Wanted: A number of bright young men to assist in the business department during the holidays."

    def test_col72_news_01(self):
        assert NewlinesToPeriods.process("A spokesman for the ministry said the decision\n    was final.") == "A spokesman for the ministry said the decision was final."

    def test_col72_science_01(self):
        assert NewlinesToPeriods.process("The mean response time was 324 milliseconds with\n    a standard deviation of 41.") == "The mean response time was 324 milliseconds with a standard deviation of 41."

    # ---------------------------------------------------------------- wrap at ~76 chars

    def test_col76_fiction_01(self):
        assert NewlinesToPeriods.process("She spent the better part of three weeks transcribing\n    the original text.") == "She spent the better part of three weeks transcribing the original text."

    def test_col76_fiction_02(self):
        assert NewlinesToPeriods.process("He had always believed that hard work and perseverance\n    would bring its reward.") == "He had always believed that hard work and perseverance would bring its reward."

    def test_col76_business_01(self):
        result = NewlinesToPeriods.process(
            "Wanted: A number of bright young men to assist in the business\n"
            "    department."
        )
        assert "business.department" not in result
        assert result == "Wanted: A number of bright young men to assist in the business department."

    def test_col76_news_01(self):
        assert NewlinesToPeriods.process("Campaigners gathered outside parliament to protest\n    the new legislation.") == "Campaigners gathered outside parliament to protest the new legislation."

    def test_col76_science_01(self):
        assert NewlinesToPeriods.process("The algorithm has a time complexity of O(n log n)\n    in the average case.") == "The algorithm has a time complexity of O(n log n) in the average case."

    # ---------------------------------------------------------------- wrap at ~80 chars

    def test_col80_fiction_01(self):
        assert NewlinesToPeriods.process("The final report was submitted to the committee on the\n    morning of the deadline.") == "The final report was submitted to the committee on the morning of the deadline."

    def test_col80_fiction_02(self):
        assert NewlinesToPeriods.process("The delegation arrived at the conference having already\n    agreed on the main points.") == "The delegation arrived at the conference having already agreed on the main points."

    def test_col80_business_01(self):
        result = NewlinesToPeriods.process(
            "Wanted: A number of bright young men to assist in the business department\n"
            "    during the Christmas holidays."
        )
        assert "department.during" not in result
        assert result == "Wanted: A number of bright young men to assist in the business department during the Christmas holidays."

    def test_col80_news_01(self):
        assert NewlinesToPeriods.process("The prime minister called the result a great victory\n    for the country.") == "The prime minister called the result a great victory for the country."

    def test_col80_science_01(self):
        assert NewlinesToPeriods.process("Signal-to-noise ratio was measured at each frequency\n    in the spectrum.") == "Signal-to-noise ratio was measured at each frequency in the spectrum."

    def test_col80_history_01(self):
        assert NewlinesToPeriods.process("The famine resulted in the death of over a million\n    people in three years.") == "The famine resulted in the death of over a million people in three years."

    def test_col80_legal_01(self):
        assert NewlinesToPeriods.process("The defendant entered a plea of not guilty to\n    all charges brought against him.") == "The defendant entered a plea of not guilty to all charges brought against him."

    def test_col80_travel_01(self):
        assert NewlinesToPeriods.process("The market opens at dawn and closes by noon\n    before the heat sets in.") == "The market opens at dawn and closes by noon before the heat sets in."

    def test_col80_recipe_01(self):
        assert NewlinesToPeriods.process("Allow to cool before slicing or the centre\n    will be too moist to cut cleanly.") == "Allow to cool before slicing or the centre will be too moist to cut cleanly."

    def test_col80_instructions_01(self):
        assert NewlinesToPeriods.process("Press and hold the power button for three seconds\n    until the indicator light flashes.") == "Press and hold the power button for three seconds until the indicator light flashes."
