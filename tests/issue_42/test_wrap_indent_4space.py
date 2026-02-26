# -*- coding: UTF-8 -*-
"""Unit tests for NewlinesToPeriods with 4-space-indented continuation lines.

The 4-space block-quote indent is the PRIMARY trigger for the corruption in
issue #42. When a hard-wrapped line has `\n    ` (newline + 4 spaces), the
current pipeline produces `word.word` corruption via a 3-component interaction:
NewlinesToPeriods → _clean_spacing → BulletPointCleaner.

After the fix, NewlinesToPeriods strips per-line whitespace before joining so
these cases always produce a single space between the wrapped words.

Currently FAILING (documents the desired post-fix behavior).

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestWrapIndent4Space:
    """Hard-wrapped lines where the continuation line has a 4-space (Gutenberg) indent."""

    # ---------------------------------------------------------------- the exact dreiser case

    def test_dreiser_exact(self):
        assert NewlinesToPeriods.process(
            "assist in the business\n    department during the Christmas holidays."
        ) == "assist in the business department during the Christmas holidays."

    def test_dreiser_full_sentence(self):
        assert NewlinesToPeriods.process(
            "Wanted: A number of bright young men to assist in the business\n    department during the Christmas holidays."
        ) == "Wanted: A number of bright young men to assist in the business department during the Christmas holidays."

    def test_dreiser_no_period_corruption(self):
        result = NewlinesToPeriods.process(
            "assist in the business\n    department during the Christmas holidays."
        )
        assert "business.department" not in result

    # ---------------------------------------------------------------- fiction

    def test_fiction_wrap_after_preposition_01(self):
        assert NewlinesToPeriods.process("She walked down the long\n    corridor.") == "She walked down the long corridor."

    def test_fiction_wrap_after_preposition_02(self):
        assert NewlinesToPeriods.process("He stood at\n    the edge of the cliff.") == "He stood at the edge of the cliff."

    def test_fiction_wrap_after_preposition_03(self):
        assert NewlinesToPeriods.process("The letter lay on\n    the table.") == "The letter lay on the table."

    def test_fiction_wrap_after_preposition_04(self):
        assert NewlinesToPeriods.process("They walked through\n    the forest in silence.") == "They walked through the forest in silence."

    def test_fiction_wrap_after_preposition_05(self):
        assert NewlinesToPeriods.process("She waited by\n    the window.") == "She waited by the window."

    def test_fiction_wrap_after_preposition_06(self):
        assert NewlinesToPeriods.process("He sat beside\n    the dying fire.") == "He sat beside the dying fire."

    def test_fiction_wrap_mid_noun_phrase_01(self):
        assert NewlinesToPeriods.process("The old brick\n    house stood alone.") == "The old brick house stood alone."

    def test_fiction_wrap_mid_noun_phrase_02(self):
        assert NewlinesToPeriods.process("A tall iron\n    gate blocked the entrance.") == "A tall iron gate blocked the entrance."

    def test_fiction_wrap_mid_noun_phrase_03(self):
        assert NewlinesToPeriods.process("The narrow cobbled\n    street wound through the village.") == "The narrow cobbled street wound through the village."

    def test_fiction_wrap_mid_noun_phrase_04(self):
        assert NewlinesToPeriods.process("Her dark blue\n    eyes betrayed nothing.") == "Her dark blue eyes betrayed nothing."

    def test_fiction_wrap_mid_noun_phrase_05(self):
        assert NewlinesToPeriods.process("A cold north\n    wind began to blow.") == "A cold north wind began to blow."

    def test_fiction_wrap_mid_noun_phrase_06(self):
        assert NewlinesToPeriods.process("The heavy oak\n    door stood ajar.") == "The heavy oak door stood ajar."

    def test_fiction_wrap_after_verb_01(self):
        assert NewlinesToPeriods.process("She smiled\n    and turned away.") == "She smiled and turned away."

    def test_fiction_wrap_after_verb_02(self):
        assert NewlinesToPeriods.process("He replied\n    without hesitation.") == "He replied without hesitation."

    def test_fiction_wrap_after_verb_03(self):
        assert NewlinesToPeriods.process("The ship sailed\n    into the harbour.") == "The ship sailed into the harbour."

    def test_fiction_wrap_after_verb_04(self):
        assert NewlinesToPeriods.process("She hesitated\n    before answering.") == "She hesitated before answering."

    def test_fiction_wrap_after_verb_05(self):
        assert NewlinesToPeriods.process("He shouted\n    across the courtyard.") == "He shouted across the courtyard."

    def test_fiction_wrap_after_adjective_01(self):
        assert NewlinesToPeriods.process("The room was cold\n    and dimly lit.") == "The room was cold and dimly lit."

    def test_fiction_wrap_after_adjective_02(self):
        assert NewlinesToPeriods.process("She wore a long\n    red dress.") == "She wore a long red dress."

    def test_fiction_wrap_after_adjective_03(self):
        assert NewlinesToPeriods.process("It was a warm\n    summer evening.") == "It was a warm summer evening."

    def test_fiction_wrap_after_conjunction_01(self):
        assert NewlinesToPeriods.process("He was tired but\n    refused to rest.") == "He was tired but refused to rest."

    def test_fiction_wrap_after_conjunction_02(self):
        assert NewlinesToPeriods.process("The sun had set and\n    the streets were empty.") == "The sun had set and the streets were empty."

    def test_fiction_wrap_after_conjunction_03(self):
        assert NewlinesToPeriods.process("She could laugh or\n    she could weep.") == "She could laugh or she could weep."

    def test_fiction_wrap_after_comma_01(self):
        assert NewlinesToPeriods.process("After a long pause,\n    she finally spoke.") == "After a long pause, she finally spoke."

    def test_fiction_wrap_after_comma_02(self):
        assert NewlinesToPeriods.process("By midnight,\n    the house was silent.") == "By midnight, the house was silent."

    def test_fiction_wrap_after_comma_03(self):
        assert NewlinesToPeriods.process("He sat down, placed his hat\n    on the table.") == "He sat down, placed his hat on the table."

    def test_fiction_wrap_long_01(self):
        assert NewlinesToPeriods.process(
            "The enormous mahogany writing-desk stood\n    against the far wall."
        ) == "The enormous mahogany writing-desk stood against the far wall."

    def test_fiction_wrap_long_02(self):
        assert NewlinesToPeriods.process(
            "Her expression changed so suddenly that\n    even he was startled."
        ) == "Her expression changed so suddenly that even he was startled."

    def test_fiction_wrap_long_03(self):
        assert NewlinesToPeriods.process(
            "He had lived in the town for twenty years\n    without once feeling at home."
        ) == "He had lived in the town for twenty years without once feeling at home."

    def test_fiction_wrap_short_01(self):
        assert NewlinesToPeriods.process("He ran\n    fast.") == "He ran fast."

    def test_fiction_wrap_short_02(self):
        assert NewlinesToPeriods.process("She wept\n    bitterly.") == "She wept bitterly."

    def test_fiction_wrap_short_03(self):
        assert NewlinesToPeriods.process("It rained\n    all day.") == "It rained all day."

    # ---------------------------------------------------------------- journalism

    def test_news_01(self):
        assert NewlinesToPeriods.process(
            "The president announced that new\n    measures would be introduced."
        ) == "The president announced that new measures would be introduced."

    def test_news_02(self):
        assert NewlinesToPeriods.process(
            "Investigators say the fire broke out\n    in the early hours."
        ) == "Investigators say the fire broke out in the early hours."

    def test_news_03(self):
        assert NewlinesToPeriods.process(
            "Three people were injured when\n    a van mounted the pavement."
        ) == "Three people were injured when a van mounted the pavement."

    def test_news_04(self):
        assert NewlinesToPeriods.process(
            "The company reported record profits\n    for the third quarter."
        ) == "The company reported record profits for the third quarter."

    def test_news_05(self):
        assert NewlinesToPeriods.process(
            "Officials confirmed that negotiations\n    would resume next week."
        ) == "Officials confirmed that negotiations would resume next week."

    def test_news_06(self):
        assert NewlinesToPeriods.process(
            "The bill passed by a narrow\n    margin of six votes."
        ) == "The bill passed by a narrow margin of six votes."

    def test_news_07(self):
        assert NewlinesToPeriods.process(
            "Thousands of commuters faced delays\n    after signal failures."
        ) == "Thousands of commuters faced delays after signal failures."

    def test_news_08(self):
        assert NewlinesToPeriods.process(
            "The summit will be held in Geneva\n    at the end of the month."
        ) == "The summit will be held in Geneva at the end of the month."

    def test_news_09(self):
        assert NewlinesToPeriods.process(
            "Campaigners gathered outside parliament\n    to protest the legislation."
        ) == "Campaigners gathered outside parliament to protest the legislation."

    def test_news_10(self):
        assert NewlinesToPeriods.process(
            "The fund raised over three million\n    dollars in a single evening."
        ) == "The fund raised over three million dollars in a single evening."

    # ---------------------------------------------------------------- scientific

    def test_science_01(self):
        assert NewlinesToPeriods.process(
            "The samples were incubated at\n    room temperature for forty-eight hours."
        ) == "The samples were incubated at room temperature for forty-eight hours."

    def test_science_02(self):
        assert NewlinesToPeriods.process(
            "Results were analysed using\n    a standard regression model."
        ) == "Results were analysed using a standard regression model."

    def test_science_03(self):
        assert NewlinesToPeriods.process(
            "Data were collected over a period\n    of six months from twelve sites."
        ) == "Data were collected over a period of six months from twelve sites."

    def test_science_04(self):
        assert NewlinesToPeriods.process(
            "The group receiving treatment\n    showed significantly better outcomes."
        ) == "The group receiving treatment showed significantly better outcomes."

    def test_science_05(self):
        assert NewlinesToPeriods.process(
            "No significant difference was found\n    between the two conditions."
        ) == "No significant difference was found between the two conditions."

    def test_science_06(self):
        assert NewlinesToPeriods.process(
            "Further research is needed to\n    clarify the underlying mechanism."
        ) == "Further research is needed to clarify the underlying mechanism."

    def test_science_07(self):
        assert NewlinesToPeriods.process(
            "The algorithm has time complexity\n    of O(n log n) in the average case."
        ) == "The algorithm has time complexity of O(n log n) in the average case."

    def test_science_08(self):
        assert NewlinesToPeriods.process(
            "Participants were randomly assigned\n    to one of three groups."
        ) == "Participants were randomly assigned to one of three groups."

    def test_science_09(self):
        assert NewlinesToPeriods.process(
            "The effect was statistically\n    significant at the p < 0.01 level."
        ) == "The effect was statistically significant at the p < 0.01 level."

    def test_science_10(self):
        assert NewlinesToPeriods.process(
            "Signal-to-noise ratio was measured\n    at each frequency."
        ) == "Signal-to-noise ratio was measured at each frequency."

    # ---------------------------------------------------------------- historical

    def test_history_01(self):
        assert NewlinesToPeriods.process(
            "The army crossed the river at\n    dawn on the fourth of June."
        ) == "The army crossed the river at dawn on the fourth of June."

    def test_history_02(self):
        assert NewlinesToPeriods.process(
            "The treaty was signed by\n    representatives of both powers."
        ) == "The treaty was signed by representatives of both powers."

    def test_history_03(self):
        assert NewlinesToPeriods.process(
            "By the end of the decade the\n    population had doubled."
        ) == "By the end of the decade the population had doubled."

    def test_history_04(self):
        assert NewlinesToPeriods.process(
            "The king died without a legitimate\n    heir and the succession was disputed."
        ) == "The king died without a legitimate heir and the succession was disputed."

    def test_history_05(self):
        assert NewlinesToPeriods.process(
            "Trade routes across the desert\n    were established in the first century."
        ) == "Trade routes across the desert were established in the first century."

    def test_history_06(self):
        assert NewlinesToPeriods.process(
            "The battle took place on the\n    plains outside the city walls."
        ) == "The battle took place on the plains outside the city walls."

    def test_history_07(self):
        assert NewlinesToPeriods.process(
            "The famine resulted in the death\n    of over a million people."
        ) == "The famine resulted in the death of over a million people."

    # ---------------------------------------------------------------- legal / formal

    def test_legal_01(self):
        assert NewlinesToPeriods.process(
            "The party of the first part agrees\n    to deliver the goods by Friday."
        ) == "The party of the first part agrees to deliver the goods by Friday."

    def test_legal_02(self):
        assert NewlinesToPeriods.process(
            "Notwithstanding any prior agreement,\n    this contract supersedes all others."
        ) == "Notwithstanding any prior agreement, this contract supersedes all others."

    def test_legal_03(self):
        assert NewlinesToPeriods.process(
            "The defendant entered a plea\n    of not guilty to all charges."
        ) == "The defendant entered a plea of not guilty to all charges."

    def test_legal_04(self):
        assert NewlinesToPeriods.process(
            "Any dispute arising under this\n    agreement shall be referred to arbitration."
        ) == "Any dispute arising under this agreement shall be referred to arbitration."

    def test_legal_05(self):
        assert NewlinesToPeriods.process(
            "The court found in favour of\n    the plaintiff on all counts."
        ) == "The court found in favour of the plaintiff on all counts."

    # ---------------------------------------------------------------- business / advertisement

    def test_business_advert_01(self):
        assert NewlinesToPeriods.process(
            "Wanted: bright young men to assist in the business\n    department during the Christmas holidays."
        ) == "Wanted: bright young men to assist in the business department during the Christmas holidays."

    def test_business_advert_02(self):
        assert NewlinesToPeriods.process(
            "Apply to Business Manager between\n    9 and 10 a.m."
        ) == "Apply to Business Manager between 9 and 10 a.m."

    def test_business_advert_03(self):
        assert NewlinesToPeriods.process(
            "Promotion possible for the right\n    candidate with drive."
        ) == "Promotion possible for the right candidate with drive."

    def test_business_01(self):
        assert NewlinesToPeriods.process(
            "The advertising\n    department was on the third floor."
        ) == "The advertising department was on the third floor."

    def test_business_02(self):
        assert NewlinesToPeriods.process(
            "She managed the\n    marketing department for ten years."
        ) == "She managed the marketing department for ten years."

    def test_business_03(self):
        assert NewlinesToPeriods.process(
            "Members of the\n    accounting team attended."
        ) == "Members of the accounting team attended."

    def test_business_04(self):
        assert NewlinesToPeriods.process(
            "The sales\n    figures for the quarter were strong."
        ) == "The sales figures for the quarter were strong."

    def test_business_05(self):
        assert NewlinesToPeriods.process(
            "Apply to the Personnel\n    Manager before the deadline."
        ) == "Apply to the Personnel Manager before the deadline."

    # ---------------------------------------------------------------- travel

    def test_travel_01(self):
        assert NewlinesToPeriods.process(
            "The road wound up through pine\n    forests to a plateau."
        ) == "The road wound up through pine forests to a plateau."

    def test_travel_02(self):
        assert NewlinesToPeriods.process(
            "We arrived at the village after\n    a three-hour climb."
        ) == "We arrived at the village after a three-hour climb."

    def test_travel_03(self):
        assert NewlinesToPeriods.process(
            "The cathedral dominates the skyline\n    and can be seen from miles away."
        ) == "The cathedral dominates the skyline and can be seen from miles away."

    def test_travel_04(self):
        assert NewlinesToPeriods.process(
            "From the terrace we could see\n    the entire valley."
        ) == "From the terrace we could see the entire valley."

    def test_travel_05(self):
        assert NewlinesToPeriods.process(
            "The harbour was lined with\n    colourful boats."
        ) == "The harbour was lined with colourful boats."

    # ---------------------------------------------------------------- recipe / instructional

    def test_recipe_01(self):
        assert NewlinesToPeriods.process(
            "Add the flour and mix until\n    a smooth dough forms."
        ) == "Add the flour and mix until a smooth dough forms."

    def test_recipe_02(self):
        assert NewlinesToPeriods.process(
            "Bake in a preheated oven at\n    180 degrees for thirty minutes."
        ) == "Bake in a preheated oven at 180 degrees for thirty minutes."

    def test_recipe_03(self):
        assert NewlinesToPeriods.process(
            "Allow to cool before slicing\n    or the centre will collapse."
        ) == "Allow to cool before slicing or the centre will collapse."

    def test_recipe_04(self):
        assert NewlinesToPeriods.process(
            "Heat the oil in a pan over\n    medium heat until shimmering."
        ) == "Heat the oil in a pan over medium heat until shimmering."

    def test_recipe_05(self):
        assert NewlinesToPeriods.process(
            "Season with salt and pepper and\n    serve immediately."
        ) == "Season with salt and pepper and serve immediately."

    # ---------------------------------------------------------------- various compound nouns (corruption-prone)

    def test_compound_noun_office_01(self):
        result = NewlinesToPeriods.process("the post\n    office closed at noon.")
        assert "post.office" not in result
        assert result == "the post office closed at noon."

    def test_compound_noun_fire_01(self):
        result = NewlinesToPeriods.process("the fire\n    station was nearby.")
        assert "fire.station" not in result
        assert result == "the fire station was nearby."

    def test_compound_noun_book_01(self):
        result = NewlinesToPeriods.process("the book\n    keeper checked the accounts.")
        assert "book.keeper" not in result
        assert result == "the book keeper checked the accounts."

    def test_compound_noun_night_01(self):
        result = NewlinesToPeriods.process("the night\n    watchman made his rounds.")
        assert "night.watchman" not in result
        assert result == "the night watchman made his rounds."

    def test_compound_noun_door_01(self):
        result = NewlinesToPeriods.process("the door\n    keeper stood aside.")
        assert "door.keeper" not in result
        assert result == "the door keeper stood aside."

    def test_compound_noun_town_01(self):
        result = NewlinesToPeriods.process("the town\n    council met on Monday.")
        assert "town.council" not in result
        assert result == "the town council met on Monday."

    def test_compound_noun_trade_01(self):
        result = NewlinesToPeriods.process("the trade\n    union called a meeting.")
        assert "trade.union" not in result
        assert result == "the trade union called a meeting."

    def test_compound_noun_law_01(self):
        result = NewlinesToPeriods.process("the law\n    firm had twelve partners.")
        assert "law.firm" not in result
        assert result == "the law firm had twelve partners."

    def test_compound_noun_health_01(self):
        result = NewlinesToPeriods.process("the health\n    department issued a warning.")
        assert "health.department" not in result
        assert result == "the health department issued a warning."

    def test_compound_noun_finance_01(self):
        result = NewlinesToPeriods.process("the finance\n    committee approved the budget.")
        assert "finance.committee" not in result
        assert result == "the finance committee approved the budget."

    def test_compound_noun_war_01(self):
        result = NewlinesToPeriods.process("the war\n    department issued orders.")
        assert "war.department" not in result
        assert result == "the war department issued orders."

    def test_compound_noun_foreign_01(self):
        result = NewlinesToPeriods.process("the foreign\n    office sent a telegram.")
        assert "foreign.office" not in result
        assert result == "the foreign office sent a telegram."

    def test_compound_noun_home_01(self):
        result = NewlinesToPeriods.process("the home\n    secretary made a statement.")
        assert "home.secretary" not in result
        assert result == "the home secretary made a statement."

    def test_compound_noun_prime_01(self):
        result = NewlinesToPeriods.process("the prime\n    minister addressed the nation.")
        assert "prime.minister" not in result
        assert result == "the prime minister addressed the nation."

    def test_compound_noun_police_01(self):
        result = NewlinesToPeriods.process("the police\n    constable approached.")
        assert "police.constable" not in result
        assert result == "the police constable approached."

    # ---------------------------------------------------------------- wrap column widths

    def test_wrap_at_40_chars_01(self):
        assert NewlinesToPeriods.process(
            "He could not find the key\n    anywhere."
        ) == "He could not find the key anywhere."

    def test_wrap_at_50_chars_01(self):
        assert NewlinesToPeriods.process(
            "She had never seen anything quite like\n    it before."
        ) == "She had never seen anything quite like it before."

    def test_wrap_at_55_chars_01(self):
        assert NewlinesToPeriods.process(
            "The document was filed in the wrong\n    cabinet."
        ) == "The document was filed in the wrong cabinet."

    def test_wrap_at_60_chars_01(self):
        assert NewlinesToPeriods.process(
            "Nobody had expected the announcement to\n    come so soon."
        ) == "Nobody had expected the announcement to come so soon."

    def test_wrap_at_65_chars_01(self):
        assert NewlinesToPeriods.process(
            "The library held thousands of volumes\n    never yet catalogued."
        ) == "The library held thousands of volumes never yet catalogued."

    def test_wrap_at_68_chars_01(self):
        assert NewlinesToPeriods.process(
            "She had spent three weeks transcribing\n    the original text."
        ) == "She had spent three weeks transcribing the original text."

    def test_wrap_at_70_chars_01(self):
        assert NewlinesToPeriods.process(
            "The committee met on three separate\n    occasions in secret."
        ) == "The committee met on three separate occasions in secret."

    def test_wrap_at_72_chars_01(self):
        assert NewlinesToPeriods.process(
            "He had always believed that hard work\n    would bring its reward."
        ) == "He had always believed that hard work would bring its reward."

    def test_wrap_at_75_chars_01(self):
        assert NewlinesToPeriods.process(
            "The delegation arrived having already\n    agreed on their position."
        ) == "The delegation arrived having already agreed on their position."

    def test_wrap_at_80_chars_01(self):
        assert NewlinesToPeriods.process(
            "The final report was submitted to the\n    committee that morning."
        ) == "The final report was submitted to the committee that morning."

    # ---------------------------------------------------------------- domain variety

    def test_medical_01(self):
        assert NewlinesToPeriods.process(
            "The patient was admitted with\n    chest pain and breathlessness."
        ) == "The patient was admitted with chest pain and breathlessness."

    def test_medical_02(self):
        assert NewlinesToPeriods.process(
            "A course of antibiotics was\n    prescribed for ten days."
        ) == "A course of antibiotics was prescribed for ten days."

    def test_education_01(self):
        assert NewlinesToPeriods.process(
            "Students must submit assignments\n    by the published deadline."
        ) == "Students must submit assignments by the published deadline."

    def test_sport_01(self):
        assert NewlinesToPeriods.process(
            "The team won the championship\n    for the third year running."
        ) == "The team won the championship for the third year running."

    def test_technology_01(self):
        assert NewlinesToPeriods.process(
            "The software update introduced\n    several new security patches."
        ) == "The software update introduced several new security patches."

    def test_environment_01(self):
        assert NewlinesToPeriods.process(
            "Rising sea levels threaten\n    coastal communities worldwide."
        ) == "Rising sea levels threaten coastal communities worldwide."

    def test_economics_01(self):
        assert NewlinesToPeriods.process(
            "Inflation rose to its highest\n    level in thirty years."
        ) == "Inflation rose to its highest level in thirty years."

    def test_politics_01(self):
        assert NewlinesToPeriods.process(
            "The opposition called for\n    a vote of no confidence."
        ) == "The opposition called for a vote of no confidence."

    def test_psychology_01(self):
        assert NewlinesToPeriods.process(
            "Children exposed to early stress\n    showed higher cortisol levels."
        ) == "Children exposed to early stress showed higher cortisol levels."

    def test_geography_01(self):
        assert NewlinesToPeriods.process(
            "The river rises in the mountains\n    and flows south to the sea."
        ) == "The river rises in the mountains and flows south to the sea."

    def test_biography_01(self):
        assert NewlinesToPeriods.process(
            "He was born in a small village\n    near the border in 1843."
        ) == "He was born in a small village near the border in 1843."

    def test_military_01(self):
        assert NewlinesToPeriods.process(
            "The regiment was ordered to\n    advance at first light."
        ) == "The regiment was ordered to advance at first light."

    def test_religion_01(self):
        assert NewlinesToPeriods.process(
            "The pilgrimage attracts thousands\n    of visitors each year."
        ) == "The pilgrimage attracts thousands of visitors each year."

    def test_agriculture_01(self):
        assert NewlinesToPeriods.process(
            "The harvest was poor due to\n    drought throughout summer."
        ) == "The harvest was poor due to drought throughout summer."

    def test_architecture_01(self):
        assert NewlinesToPeriods.process(
            "The tower was built in the\n    Gothic style in the fourteenth century."
        ) == "The tower was built in the Gothic style in the fourteenth century."

    def test_music_01(self):
        assert NewlinesToPeriods.process(
            "The symphony was performed\n    to a standing ovation."
        ) == "The symphony was performed to a standing ovation."

    def test_art_01(self):
        assert NewlinesToPeriods.process(
            "The painting was acquired by\n    the museum in 1923."
        ) == "The painting was acquired by the museum in 1923."

    def test_philosophy_01(self):
        assert NewlinesToPeriods.process(
            "The question of free will has\n    occupied philosophers for centuries."
        ) == "The question of free will has occupied philosophers for centuries."

    def test_memoir_01(self):
        assert NewlinesToPeriods.process(
            "My father never spoke of\n    the war years."
        ) == "My father never spoke of the war years."

    def test_diary_01(self):
        assert NewlinesToPeriods.process(
            "Woke at six and went straight\n    to the fields."
        ) == "Woke at six and went straight to the fields."

    def test_letter_01(self):
        assert NewlinesToPeriods.process(
            "I write to inform you of\n    my intention to resign."
        ) == "I write to inform you of my intention to resign."

    def test_letter_02(self):
        assert NewlinesToPeriods.process(
            "Please find enclosed the\n    documents you requested."
        ) == "Please find enclosed the documents you requested."

    def test_letter_03(self):
        assert NewlinesToPeriods.process(
            "I remain, as ever, your most\n    obedient servant."
        ) == "I remain, as ever, your most obedient servant."

    def test_misc_01(self):
        assert NewlinesToPeriods.process(
            "The new policy takes\n    effect from January."
        ) == "The new policy takes effect from January."

    def test_misc_02(self):
        assert NewlinesToPeriods.process(
            "Further details will be\n    announced in due course."
        ) == "Further details will be announced in due course."

    def test_misc_03(self):
        assert NewlinesToPeriods.process(
            "Tickets are available from\n    the box office."
        ) == "Tickets are available from the box office."

    def test_misc_04(self):
        assert NewlinesToPeriods.process(
            "Applications must be received\n    by the closing date."
        ) == "Applications must be received by the closing date."

    def test_misc_05(self):
        assert NewlinesToPeriods.process(
            "Admission is free for\n    children under twelve."
        ) == "Admission is free for children under twelve."

    def test_misc_06(self):
        assert NewlinesToPeriods.process(
            "Opening hours may vary\n    during public holidays."
        ) == "Opening hours may vary during public holidays."

    def test_misc_07(self):
        assert NewlinesToPeriods.process(
            "Please note that all claims\n    must be made in writing."
        ) == "Please note that all claims must be made in writing."

    def test_misc_08(self):
        assert NewlinesToPeriods.process(
            "This offer is subject to\n    availability."
        ) == "This offer is subject to availability."

    def test_misc_09(self):
        assert NewlinesToPeriods.process(
            "The exhibition runs until\n    the end of the month."
        ) == "The exhibition runs until the end of the month."

    def test_misc_10(self):
        assert NewlinesToPeriods.process(
            "Copies of the report are\n    available on request."
        ) == "Copies of the report are available on request."
