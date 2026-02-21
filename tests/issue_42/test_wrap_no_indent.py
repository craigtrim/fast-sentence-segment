# -*- coding: UTF-8 -*-
"""Unit tests for NewlinesToPeriods with plain hard-wrapped lines (no indent).

Every input contains a single `\n` with no leading whitespace on the continuation
line. The expected output is always the same text with `\n` replaced by a single
space. These cases exercise the basic newline-to-space path and verify no period
corruption occurs.

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestWrapNoIndent:
    """Hard-wrapped lines with no indentation on the continuation line."""

    # ------------------------------------------------------------------ fiction

    def test_fiction_wrap_after_article_01(self):
        assert NewlinesToPeriods.process("She opened the\ndoor slowly.") == "She opened the door slowly."

    def test_fiction_wrap_after_article_02(self):
        assert NewlinesToPeriods.process("He picked up a\npencil from the desk.") == "He picked up a pencil from the desk."

    def test_fiction_wrap_after_preposition_01(self):
        assert NewlinesToPeriods.process("She walked down the long\ncorridor towards the exit.") == "She walked down the long corridor towards the exit."

    def test_fiction_wrap_after_preposition_02(self):
        assert NewlinesToPeriods.process("The letter lay on\nthe table unopened.") == "The letter lay on the table unopened."

    def test_fiction_wrap_after_preposition_03(self):
        assert NewlinesToPeriods.process("He stood at\nthe edge of the cliff.") == "He stood at the edge of the cliff."

    def test_fiction_wrap_after_preposition_04(self):
        assert NewlinesToPeriods.process("They travelled through\nthe mountains for three days.") == "They travelled through the mountains for three days."

    def test_fiction_wrap_after_preposition_05(self):
        assert NewlinesToPeriods.process("She waited by\nthe window all afternoon.") == "She waited by the window all afternoon."

    def test_fiction_wrap_mid_noun_phrase_01(self):
        assert NewlinesToPeriods.process("The old brick\nhouse stood alone.") == "The old brick house stood alone."

    def test_fiction_wrap_mid_noun_phrase_02(self):
        assert NewlinesToPeriods.process("A number of bright young\nmen applied for the position.") == "A number of bright young men applied for the position."

    def test_fiction_wrap_mid_noun_phrase_03(self):
        assert NewlinesToPeriods.process("The narrow cobbled\nstreet wound through the village.") == "The narrow cobbled street wound through the village."

    def test_fiction_wrap_mid_noun_phrase_04(self):
        assert NewlinesToPeriods.process("Her dark blue\neyes betrayed no emotion.") == "Her dark blue eyes betrayed no emotion."

    def test_fiction_wrap_mid_noun_phrase_05(self):
        assert NewlinesToPeriods.process("A tall iron\ngate blocked the entrance.") == "A tall iron gate blocked the entrance."

    def test_fiction_wrap_after_verb_01(self):
        assert NewlinesToPeriods.process("He replied\nwithout hesitation.") == "He replied without hesitation."

    def test_fiction_wrap_after_verb_02(self):
        assert NewlinesToPeriods.process("She smiled\nand turned away.") == "She smiled and turned away."

    def test_fiction_wrap_after_verb_03(self):
        assert NewlinesToPeriods.process("The crowd cheered\nas the horse crossed the line.") == "The crowd cheered as the horse crossed the line."

    def test_fiction_wrap_after_verb_04(self):
        assert NewlinesToPeriods.process("He hesitated\nbefore answering the question.") == "He hesitated before answering the question."

    def test_fiction_wrap_after_verb_05(self):
        assert NewlinesToPeriods.process("The ship sailed\ninto the harbour at dawn.") == "The ship sailed into the harbour at dawn."

    def test_fiction_wrap_after_adjective_01(self):
        assert NewlinesToPeriods.process("It was a warm\nand pleasant evening.") == "It was a warm and pleasant evening."

    def test_fiction_wrap_after_adjective_02(self):
        assert NewlinesToPeriods.process("The room was cold\nand dimly lit.") == "The room was cold and dimly lit."

    def test_fiction_wrap_after_adjective_03(self):
        assert NewlinesToPeriods.process("She wore a long\nred dress to the ball.") == "She wore a long red dress to the ball."

    def test_fiction_wrap_after_conjunction_01(self):
        assert NewlinesToPeriods.process("He was tired but\nhe refused to rest.") == "He was tired but he refused to rest."

    def test_fiction_wrap_after_conjunction_02(self):
        assert NewlinesToPeriods.process("The sun had set and\nthe streets were empty.") == "The sun had set and the streets were empty."

    def test_fiction_wrap_after_conjunction_03(self):
        assert NewlinesToPeriods.process("She could laugh or\nshe could weep.") == "She could laugh or she could weep."

    def test_fiction_wrap_after_conjunction_04(self):
        assert NewlinesToPeriods.process("The door was locked yet\nhe tried it again.") == "The door was locked yet he tried it again."

    def test_fiction_wrap_after_adverb_01(self):
        assert NewlinesToPeriods.process("She spoke softly\nso as not to wake the child.") == "She spoke softly so as not to wake the child."

    def test_fiction_wrap_after_adverb_02(self):
        assert NewlinesToPeriods.process("He moved quickly\nthrough the crowd.") == "He moved quickly through the crowd."

    def test_fiction_wrap_after_adverb_03(self):
        assert NewlinesToPeriods.process("They arrived late\nand found the hall already full.") == "They arrived late and found the hall already full."

    def test_fiction_wrap_after_comma_01(self):
        assert NewlinesToPeriods.process("Well, it was clear\nthat she had made up her mind.") == "Well, it was clear that she had made up her mind."

    def test_fiction_wrap_after_comma_02(self):
        assert NewlinesToPeriods.process("After a long pause,\nshe finally spoke.") == "After a long pause, she finally spoke."

    def test_fiction_wrap_after_comma_03(self):
        assert NewlinesToPeriods.process("He sat down, placed his hat\non the table, and waited.") == "He sat down, placed his hat on the table, and waited."

    def test_fiction_wrap_after_comma_04(self):
        assert NewlinesToPeriods.process("By the time they reached the inn,\nit was nearly midnight.") == "By the time they reached the inn, it was nearly midnight."

    def test_fiction_wrap_short_line_01(self):
        assert NewlinesToPeriods.process("He ran\nfast.") == "He ran fast."

    def test_fiction_wrap_short_line_02(self):
        assert NewlinesToPeriods.process("She wept\nbitterly.") == "She wept bitterly."

    def test_fiction_wrap_short_line_03(self):
        assert NewlinesToPeriods.process("It rained\nall day.") == "It rained all day."

    def test_fiction_wrap_long_line_01(self):
        assert NewlinesToPeriods.process("The enormous mahogany writing-desk that had\nbeen his grandfather's stood against the far wall.") == "The enormous mahogany writing-desk that had been his grandfather's stood against the far wall."

    def test_fiction_wrap_long_line_02(self):
        assert NewlinesToPeriods.process("Her expression changed so suddenly and so\ncompletely that even he, who knew her best, was startled.") == "Her expression changed so suddenly and so completely that even he, who knew her best, was startled."

    def test_fiction_wrap_at_70_chars_01(self):
        assert NewlinesToPeriods.process("He had lived in the town for twenty years without once\nfeeling truly at home.") == "He had lived in the town for twenty years without once feeling truly at home."

    def test_fiction_wrap_at_70_chars_02(self):
        assert NewlinesToPeriods.process("The trial lasted three weeks and attracted reporters\nfrom as far away as London.") == "The trial lasted three weeks and attracted reporters from as far away as London."

    def test_fiction_wrap_at_72_chars_01(self):
        assert NewlinesToPeriods.process("She understood immediately what he had meant by his\nremarks at dinner the night before.") == "She understood immediately what he had meant by his remarks at dinner the night before."

    def test_fiction_wrap_possessive_01(self):
        assert NewlinesToPeriods.process("The captain's\ncabin was at the stern.") == "The captain's cabin was at the stern."

    # ------------------------------------------------------------- dialogue / letters

    def test_dialogue_wrap_after_said_01(self):
        assert NewlinesToPeriods.process('"I cannot believe it,\' he said quietly.') == '"I cannot believe it,\' he said quietly.'

    def test_dialogue_wrap_attribution_01(self):
        assert NewlinesToPeriods.process("She answered with\na slight smile.") == "She answered with a slight smile."

    def test_dialogue_wrap_attribution_02(self):
        assert NewlinesToPeriods.process("He leaned forward and\nwhispered something in her ear.") == "He leaned forward and whispered something in her ear."

    def test_letter_wrap_01(self):
        assert NewlinesToPeriods.process("I write to inform you of\nmy intention to resign.") == "I write to inform you of my intention to resign."

    def test_letter_wrap_02(self):
        assert NewlinesToPeriods.process("Please find enclosed the\ndocuments you requested.") == "Please find enclosed the documents you requested."

    def test_letter_wrap_03(self):
        assert NewlinesToPeriods.process("I remain, as ever, your most\nobedient servant.") == "I remain, as ever, your most obedient servant."

    def test_letter_wrap_04(self):
        assert NewlinesToPeriods.process("It is with great regret that\nI must decline your kind invitation.") == "It is with great regret that I must decline your kind invitation."

    def test_letter_wrap_05(self):
        assert NewlinesToPeriods.process("Your last letter arrived on\nthe morning of the fifteenth.") == "Your last letter arrived on the morning of the fifteenth."

    # ------------------------------------------------------------------- journalism

    def test_news_wrap_headline_body_01(self):
        assert NewlinesToPeriods.process("The president announced yesterday that\nnew measures would be introduced.") == "The president announced yesterday that new measures would be introduced."

    def test_news_wrap_headline_body_02(self):
        assert NewlinesToPeriods.process("Investigators say the fire broke out\nin the early hours of the morning.") == "Investigators say the fire broke out in the early hours of the morning."

    def test_news_wrap_headline_body_03(self):
        assert NewlinesToPeriods.process("Three people were injured when\na van mounted the pavement.") == "Three people were injured when a van mounted the pavement."

    def test_news_wrap_headline_body_04(self):
        assert NewlinesToPeriods.process("The company reported record profits\nfor the third consecutive quarter.") == "The company reported record profits for the third consecutive quarter."

    def test_news_wrap_headline_body_05(self):
        assert NewlinesToPeriods.process("Officials confirmed that negotiations\nwould resume next week.") == "Officials confirmed that negotiations would resume next week."

    def test_news_wrap_headline_body_06(self):
        assert NewlinesToPeriods.process("The bill passed by a narrow margin\nof just six votes.") == "The bill passed by a narrow margin of just six votes."

    def test_news_wrap_headline_body_07(self):
        assert NewlinesToPeriods.process("Thousands of commuters faced delays\nafter signal failures halted trains.") == "Thousands of commuters faced delays after signal failures halted trains."

    def test_news_wrap_headline_body_08(self):
        assert NewlinesToPeriods.process("A spokesman for the ministry said\nthe decision was final.") == "A spokesman for the ministry said the decision was final."

    def test_news_wrap_headline_body_09(self):
        assert NewlinesToPeriods.process("The summit will be held in Geneva\nat the end of the month.") == "The summit will be held in Geneva at the end of the month."

    def test_news_wrap_headline_body_10(self):
        assert NewlinesToPeriods.process("Campaigners gathered outside parliament\nto protest the new legislation.") == "Campaigners gathered outside parliament to protest the new legislation."

    def test_news_wrap_quote_01(self):
        assert NewlinesToPeriods.process("He told reporters: the situation is\nunder control.") == "He told reporters: the situation is under control."

    def test_news_wrap_source_attribution_01(self):
        assert NewlinesToPeriods.process("According to a senior official who\nspoke on condition of anonymity.") == "According to a senior official who spoke on condition of anonymity."

    def test_news_wrap_dateline_01(self):
        assert NewlinesToPeriods.process("NEW YORK — The Federal Reserve said\nit would hold rates steady.") == "NEW YORK — The Federal Reserve said it would hold rates steady."

    def test_news_wrap_number_01(self):
        assert NewlinesToPeriods.process("More than two thousand people\nattended the vigil.") == "More than two thousand people attended the vigil."

    def test_news_wrap_number_02(self):
        assert NewlinesToPeriods.process("The fund raised over three million\ndollars in a single evening.") == "The fund raised over three million dollars in a single evening."

    # --------------------------------------------------------------- scientific

    def test_science_wrap_methodology_01(self):
        assert NewlinesToPeriods.process("The samples were incubated at\nroom temperature for forty-eight hours.") == "The samples were incubated at room temperature for forty-eight hours."

    def test_science_wrap_methodology_02(self):
        assert NewlinesToPeriods.process("Results were analysed using\na standard regression model.") == "Results were analysed using a standard regression model."

    def test_science_wrap_methodology_03(self):
        assert NewlinesToPeriods.process("The experiment was repeated three\ntimes to confirm reproducibility.") == "The experiment was repeated three times to confirm reproducibility."

    def test_science_wrap_methodology_04(self):
        assert NewlinesToPeriods.process("Data were collected over a period\nof six months from twelve sites.") == "Data were collected over a period of six months from twelve sites."

    def test_science_wrap_result_01(self):
        assert NewlinesToPeriods.process("The group receiving the treatment\nshowed significantly better outcomes.") == "The group receiving the treatment showed significantly better outcomes."

    def test_science_wrap_result_02(self):
        assert NewlinesToPeriods.process("No significant difference was found\nbetween the two conditions.") == "No significant difference was found between the two conditions."

    def test_science_wrap_conclusion_01(self):
        assert NewlinesToPeriods.process("These findings suggest that\nearly intervention is beneficial.") == "These findings suggest that early intervention is beneficial."

    def test_science_wrap_conclusion_02(self):
        assert NewlinesToPeriods.process("Further research is needed to\nclarify the underlying mechanism.") == "Further research is needed to clarify the underlying mechanism."

    def test_science_wrap_technical_01(self):
        assert NewlinesToPeriods.process("The algorithm has a time complexity\nof O(n log n) in the average case.") == "The algorithm has a time complexity of O(n log n) in the average case."

    def test_science_wrap_technical_02(self):
        assert NewlinesToPeriods.process("Signal-to-noise ratio was measured\nat each frequency in the spectrum.") == "Signal-to-noise ratio was measured at each frequency in the spectrum."

    def test_science_wrap_technical_03(self):
        assert NewlinesToPeriods.process("The protein was extracted using\na standard buffer solution.") == "The protein was extracted using a standard buffer solution."

    def test_science_wrap_hypothesis_01(self):
        assert NewlinesToPeriods.process("We hypothesised that exposure to\nblue light would disrupt sleep cycles.") == "We hypothesised that exposure to blue light would disrupt sleep cycles."

    def test_science_wrap_passive_01(self):
        assert NewlinesToPeriods.process("The specimens were stored in\nliquid nitrogen until analysis.") == "The specimens were stored in liquid nitrogen until analysis."

    def test_science_wrap_passive_02(self):
        assert NewlinesToPeriods.process("Participants were randomly assigned\nto one of three experimental groups.") == "Participants were randomly assigned to one of three experimental groups."

    def test_science_wrap_measurement_01(self):
        assert NewlinesToPeriods.process("The mean response time was\n324 milliseconds with a standard deviation of 41.") == "The mean response time was 324 milliseconds with a standard deviation of 41."

    # ---------------------------------------------------------------- historical

    def test_history_wrap_narrative_01(self):
        assert NewlinesToPeriods.process("The army crossed the river at\ndawn on the fourth of June.") == "The army crossed the river at dawn on the fourth of June."

    def test_history_wrap_narrative_02(self):
        assert NewlinesToPeriods.process("The treaty was signed by\nrepresentatives of both powers.") == "The treaty was signed by representatives of both powers."

    def test_history_wrap_narrative_03(self):
        assert NewlinesToPeriods.process("By the end of the decade the\npopulation had doubled in size.") == "By the end of the decade the population had doubled in size."

    def test_history_wrap_narrative_04(self):
        assert NewlinesToPeriods.process("The king died without a legitimate\nheir and the succession was disputed.") == "The king died without a legitimate heir and the succession was disputed."

    def test_history_wrap_narrative_05(self):
        assert NewlinesToPeriods.process("Trade routes across the desert\nwere established in the first century.") == "Trade routes across the desert were established in the first century."

    def test_history_wrap_date_01(self):
        assert NewlinesToPeriods.process("On the fourteenth of July\nthe Bastille was stormed.") == "On the fourteenth of July the Bastille was stormed."

    def test_history_wrap_date_02(self):
        assert NewlinesToPeriods.process("In the spring of 1815\nNapoleon escaped from Elba.") == "In the spring of 1815 Napoleon escaped from Elba."

    def test_history_wrap_place_01(self):
        assert NewlinesToPeriods.process("The battle took place on the\nplains outside the city walls.") == "The battle took place on the plains outside the city walls."

    def test_history_wrap_quote_01(self):
        assert NewlinesToPeriods.process("The general declared that the city\nwould not surrender under any terms.") == "The general declared that the city would not surrender under any terms."

    def test_history_wrap_consequence_01(self):
        assert NewlinesToPeriods.process("The famine resulted in the death\nof over a million people.") == "The famine resulted in the death of over a million people."

    # ----------------------------------------------------------------- legal / formal

    def test_legal_wrap_clause_01(self):
        assert NewlinesToPeriods.process("The party of the first part agrees\nto deliver the goods by Friday.") == "The party of the first part agrees to deliver the goods by Friday."

    def test_legal_wrap_clause_02(self):
        assert NewlinesToPeriods.process("Notwithstanding any prior agreement,\nthis contract supersedes all others.") == "Notwithstanding any prior agreement, this contract supersedes all others."

    def test_legal_wrap_clause_03(self):
        assert NewlinesToPeriods.process("The defendant entered a plea\nof not guilty to all charges.") == "The defendant entered a plea of not guilty to all charges."

    def test_legal_wrap_clause_04(self):
        assert NewlinesToPeriods.process("Any dispute arising under this\nagreement shall be referred to arbitration.") == "Any dispute arising under this agreement shall be referred to arbitration."

    def test_legal_wrap_clause_05(self):
        assert NewlinesToPeriods.process("The court found in favour of\nthe plaintiff on all counts.") == "The court found in favour of the plaintiff on all counts."

    def test_legal_wrap_clause_06(self):
        assert NewlinesToPeriods.process("This deed is made this day between\nthe parties named herein.") == "This deed is made this day between the parties named herein."

    def test_legal_wrap_recital_01(self):
        assert NewlinesToPeriods.process("WHEREAS the parties wish to set out\nthe terms of their arrangement.") == "WHEREAS the parties wish to set out the terms of their arrangement."

    # -------------------------------------------------------------- travel writing

    def test_travel_wrap_description_01(self):
        assert NewlinesToPeriods.process("The road wound up through pine\nforests to a mountain plateau.") == "The road wound up through pine forests to a mountain plateau."

    def test_travel_wrap_description_02(self):
        assert NewlinesToPeriods.process("The harbour was lined with colourful\nboats and smelled of fish and salt.") == "The harbour was lined with colourful boats and smelled of fish and salt."

    def test_travel_wrap_description_03(self):
        assert NewlinesToPeriods.process("We arrived at the village after\na three-hour climb in the heat.") == "We arrived at the village after a three-hour climb in the heat."

    def test_travel_wrap_description_04(self):
        assert NewlinesToPeriods.process("The cathedral dominates the skyline\nand can be seen from miles away.") == "The cathedral dominates the skyline and can be seen from miles away."

    def test_travel_wrap_description_05(self):
        assert NewlinesToPeriods.process("From the terrace we could see\nthe entire valley spread below us.") == "From the terrace we could see the entire valley spread below us."

    def test_travel_wrap_description_06(self):
        assert NewlinesToPeriods.process("The market opens at dawn and\ncloses by noon before the heat sets in.") == "The market opens at dawn and closes by noon before the heat sets in."

    def test_travel_wrap_observation_01(self):
        assert NewlinesToPeriods.process("The locals regard strangers with\ncurious but friendly interest.") == "The locals regard strangers with curious but friendly interest."

    def test_travel_wrap_observation_02(self):
        assert NewlinesToPeriods.process("Few tourists venture this far\nfrom the main road.") == "Few tourists venture this far from the main road."

    # -------------------------------------------------------------- instructional / recipe

    def test_recipe_wrap_step_01(self):
        assert NewlinesToPeriods.process("Add the flour and mix until\na smooth dough forms.") == "Add the flour and mix until a smooth dough forms."

    def test_recipe_wrap_step_02(self):
        assert NewlinesToPeriods.process("Bake in a preheated oven at\n180 degrees for thirty minutes.") == "Bake in a preheated oven at 180 degrees for thirty minutes."

    def test_recipe_wrap_step_03(self):
        assert NewlinesToPeriods.process("Allow to cool before slicing\nor the centre will be too moist.") == "Allow to cool before slicing or the centre will be too moist."

    def test_recipe_wrap_step_04(self):
        assert NewlinesToPeriods.process("Heat the oil in a pan over\nmedium heat until shimmering.") == "Heat the oil in a pan over medium heat until shimmering."

    def test_recipe_wrap_step_05(self):
        assert NewlinesToPeriods.process("Season with salt and pepper and\nserve immediately while hot.") == "Season with salt and pepper and serve immediately while hot."

    def test_instructions_wrap_01(self):
        assert NewlinesToPeriods.process("Insert the key and turn clockwise\nuntil you hear a click.") == "Insert the key and turn clockwise until you hear a click."

    def test_instructions_wrap_02(self):
        assert NewlinesToPeriods.process("Press and hold the button for\nthree seconds to confirm.") == "Press and hold the button for three seconds to confirm."

    def test_instructions_wrap_03(self):
        assert NewlinesToPeriods.process("Remove the battery cover by\nsliding it towards the arrow.") == "Remove the battery cover by sliding it towards the arrow."

    # -------------------------------------------------------------- various lengths

    def test_very_short_wrap_01(self):
        assert NewlinesToPeriods.process("Go\nnow.") == "Go now."

    def test_very_short_wrap_02(self):
        assert NewlinesToPeriods.process("Run\nfast.") == "Run fast."

    def test_very_short_wrap_03(self):
        assert NewlinesToPeriods.process("Wait\nhere.") == "Wait here."

    def test_short_wrap_01(self):
        assert NewlinesToPeriods.process("Come in\nand sit.") == "Come in and sit."

    def test_short_wrap_02(self):
        assert NewlinesToPeriods.process("Not now\nthank you.") == "Not now thank you."

    def test_medium_wrap_01(self):
        assert NewlinesToPeriods.process("He picked up the book\nand put it on the shelf.") == "He picked up the book and put it on the shelf."

    def test_medium_wrap_02(self):
        assert NewlinesToPeriods.process("The children played outside\nuntil the sun went down.") == "The children played outside until the sun went down."

    def test_medium_wrap_03(self):
        assert NewlinesToPeriods.process("She could not remember\nwhere she had put the key.") == "She could not remember where she had put the key."

    def test_long_wrap_01(self):
        assert NewlinesToPeriods.process("The committee met in secret on three separate occasions\nto discuss the implications of the proposed legislation.") == "The committee met in secret on three separate occasions to discuss the implications of the proposed legislation."

    def test_long_wrap_02(self):
        assert NewlinesToPeriods.process("He had always believed that hard work and perseverance\nwould eventually bring their own reward.") == "He had always believed that hard work and perseverance would eventually bring their own reward."

    def test_long_wrap_03(self):
        assert NewlinesToPeriods.process("The delegation arrived at the conference having already\nagreed on the main points of their position.") == "The delegation arrived at the conference having already agreed on the main points of their position."

    # -------------------------------------------------------------- wrap at exact positions

    def test_wrap_at_50_chars_01(self):
        assert NewlinesToPeriods.process("The government announced its plan to\nreduce carbon emissions.") == "The government announced its plan to reduce carbon emissions."

    def test_wrap_at_55_chars_01(self):
        assert NewlinesToPeriods.process("She discovered the letter tucked beneath\nthe loose floorboard.") == "She discovered the letter tucked beneath the loose floorboard."

    def test_wrap_at_60_chars_01(self):
        assert NewlinesToPeriods.process("The house had been empty for more than twenty\nyears before they bought it.") == "The house had been empty for more than twenty years before they bought it."

    def test_wrap_at_65_chars_01(self):
        assert NewlinesToPeriods.process("They found a trapdoor concealed beneath the\noriental rug in the study.") == "They found a trapdoor concealed beneath the oriental rug in the study."

    def test_wrap_at_68_chars_01(self):
        assert NewlinesToPeriods.process("No one had expected the election result to be\nso decisive.") == "No one had expected the election result to be so decisive."

    def test_wrap_at_72_chars_02(self):
        assert NewlinesToPeriods.process("The ancient library contained thousands of manuscripts\nnot yet catalogued.") == "The ancient library contained thousands of manuscripts not yet catalogued."

    def test_wrap_at_76_chars_01(self):
        assert NewlinesToPeriods.process("She spent the better part of three weeks transcribing\nthe original text.") == "She spent the better part of three weeks transcribing the original text."

    def test_wrap_at_80_chars_01(self):
        assert NewlinesToPeriods.process("The final report was submitted to the committee on the\nmorning of the deadline.") == "The final report was submitted to the committee on the morning of the deadline."

    # -------------------------------------------------------------- hyphenated words in context

    def test_well_known_wrap_01(self):
        assert NewlinesToPeriods.process("It was a well-known\nfact in the town.") == "It was a well-known fact in the town."

    def test_long_established_wrap_01(self):
        assert NewlinesToPeriods.process("The long-established\ntradition was finally abandoned.") == "The long-established tradition was finally abandoned."

    # -------------------------------------------------------------- numbers and dates

    def test_number_wrap_01(self):
        assert NewlinesToPeriods.process("Over three hundred\npeople attended the ceremony.") == "Over three hundred people attended the ceremony."

    def test_number_wrap_02(self):
        assert NewlinesToPeriods.process("The population reached\ntwo million by 1900.") == "The population reached two million by 1900."

    def test_date_wrap_01(self):
        assert NewlinesToPeriods.process("It happened on 14 March\n1879 in Ulm.") == "It happened on 14 March 1879 in Ulm."

    def test_date_wrap_02(self):
        assert NewlinesToPeriods.process("The war ended on November\n11th 1918.") == "The war ended on November 11th 1918."

    # -------------------------------------------------------------- names and titles

    def test_name_wrap_01(self):
        assert NewlinesToPeriods.process("The letter was addressed to\nMargaret Thornton.") == "The letter was addressed to Margaret Thornton."

    def test_name_wrap_02(self):
        assert NewlinesToPeriods.process("He introduced himself as\nProfessor Williams.") == "He introduced himself as Professor Williams."

    def test_name_wrap_03(self):
        assert NewlinesToPeriods.process("The book was dedicated to\nhis mother and father.") == "The book was dedicated to his mother and father."

    def test_place_name_wrap_01(self):
        assert NewlinesToPeriods.process("They boarded a train to\nNew York at six in the morning.") == "They boarded a train to New York at six in the morning."

    def test_place_name_wrap_02(self):
        assert NewlinesToPeriods.process("The conference was held in\nBuenos Aires that year.") == "The conference was held in Buenos Aires that year."

    # -------------------------------------------------------------- occupation / business

    def test_business_wrap_01(self):
        assert NewlinesToPeriods.process("The advertising\ndepartment was on the third floor.") == "The advertising department was on the third floor."

    def test_business_wrap_02(self):
        assert NewlinesToPeriods.process("Members of the\naccounting team were present.") == "Members of the accounting team were present."

    def test_business_wrap_03(self):
        assert NewlinesToPeriods.process("She managed the\nmarketing department for ten years.") == "She managed the marketing department for ten years."

    def test_business_wrap_04(self):
        assert NewlinesToPeriods.process("Apply to the\nPersonnel Manager by Friday.") == "Apply to the Personnel Manager by Friday."

    def test_business_wrap_05(self):
        assert NewlinesToPeriods.process("The sales\nfigures for the quarter were good.") == "The sales figures for the quarter were good."

    def test_business_wrap_06(self):
        assert NewlinesToPeriods.process("Wanted: bright young men to assist in\nthe business department.") == "Wanted: bright young men to assist in the business department."

    # -------------------------------------------------------------- after open parenthesis

    def test_paren_wrap_01(self):
        assert NewlinesToPeriods.process("The rule (established in\n1842) still applies today.") == "The rule (established in 1842) still applies today."

    def test_paren_wrap_02(self):
        assert NewlinesToPeriods.process("Her decision (which surprised\neveryone) was final.") == "Her decision (which surprised everyone) was final."

    # -------------------------------------------------------------- miscellaneous edge cases

    def test_no_newline_passthrough(self):
        assert NewlinesToPeriods.process("No newlines here at all.") == "No newlines here at all."

    def test_empty_string(self):
        assert NewlinesToPeriods.process("") == ""

    def test_only_newline(self):
        assert NewlinesToPeriods.process("\n") == " "

    def test_newline_at_start(self):
        assert NewlinesToPeriods.process("\nHello world.") == " Hello world."

    def test_newline_at_end(self):
        assert NewlinesToPeriods.process("Hello world.\n") == "Hello world. "

    def test_multiple_newlines_01(self):
        assert NewlinesToPeriods.process("Line one.\nLine two.\nLine three.") == "Line one. Line two. Line three."

    def test_multiple_newlines_02(self):
        assert NewlinesToPeriods.process("First\nsecond\nthird") == "First second third"

    def test_wrap_single_char_word_01(self):
        assert NewlinesToPeriods.process("I\nwent.") == "I went."

    def test_wrap_single_char_word_02(self):
        assert NewlinesToPeriods.process("He gave a\ntoy.") == "He gave a toy."

    def test_wrap_number_to_word_01(self):
        assert NewlinesToPeriods.process("He read 300\npages in a week.") == "He read 300 pages in a week."

    def test_wrap_word_to_number_01(self):
        assert NewlinesToPeriods.process("She was born in\n1884 in Paris.") == "She was born in 1884 in Paris."

    def test_wrap_ellipsis_context_01(self):
        assert NewlinesToPeriods.process("He wondered if...\nno, it could not be.") == "He wondered if... no, it could not be."

    def test_wrap_dash_context_01(self):
        assert NewlinesToPeriods.process("The answer — if there was one —\nwould take years to find.") == "The answer — if there was one — would take years to find."

    def test_wrap_after_open_quote_01(self):
        assert NewlinesToPeriods.process('"What do you mean\nby that?" she asked.') == '"What do you mean by that?" she asked.'

    def test_wrap_before_close_quote_01(self):
        assert NewlinesToPeriods.process('He said "I will not\nsurrender."') == 'He said "I will not surrender."'

    # -------------------------------------------------------------- different subjects/domains

    def test_medical_wrap_01(self):
        assert NewlinesToPeriods.process("The patient was admitted with\nchest pain and shortness of breath.") == "The patient was admitted with chest pain and shortness of breath."

    def test_medical_wrap_02(self):
        assert NewlinesToPeriods.process("A course of antibiotics was\nprescribed for ten days.") == "A course of antibiotics was prescribed for ten days."

    def test_medical_wrap_03(self):
        assert NewlinesToPeriods.process("The scan showed no sign of\nmalignancy in the affected tissue.") == "The scan showed no sign of malignancy in the affected tissue."

    def test_education_wrap_01(self):
        assert NewlinesToPeriods.process("Students are required to submit\ntheir assignments by the deadline.") == "Students are required to submit their assignments by the deadline."

    def test_education_wrap_02(self):
        assert NewlinesToPeriods.process("The examination will cover all\ntopics from the first semester.") == "The examination will cover all topics from the first semester."

    def test_sport_wrap_01(self):
        assert NewlinesToPeriods.process("The team won the championship\nfor the third year running.") == "The team won the championship for the third year running."

    def test_sport_wrap_02(self):
        assert NewlinesToPeriods.process("He scored in the final minute to\nensure his side's survival.") == "He scored in the final minute to ensure his side's survival."

    def test_technology_wrap_01(self):
        assert NewlinesToPeriods.process("The software update introduced\nseveral new security patches.") == "The software update introduced several new security patches."

    def test_technology_wrap_02(self):
        assert NewlinesToPeriods.process("Users are advised to restart their\ndevices after installation.") == "Users are advised to restart their devices after installation."

    def test_environment_wrap_01(self):
        assert NewlinesToPeriods.process("Rising sea levels threaten\ncoastal communities worldwide.") == "Rising sea levels threaten coastal communities worldwide."

    def test_environment_wrap_02(self):
        assert NewlinesToPeriods.process("The glacier has retreated by\nmore than two kilometres since 1980.") == "The glacier has retreated by more than two kilometres since 1980."

    def test_economics_wrap_01(self):
        assert NewlinesToPeriods.process("Inflation rose to its highest\nlevel in thirty years.") == "Inflation rose to its highest level in thirty years."

    def test_economics_wrap_02(self):
        assert NewlinesToPeriods.process("The central bank cut interest rates\nby half a percentage point.") == "The central bank cut interest rates by half a percentage point."

    def test_philosophy_wrap_01(self):
        assert NewlinesToPeriods.process("The question of free will has\noccupied philosophers for centuries.") == "The question of free will has occupied philosophers for centuries."

    def test_music_wrap_01(self):
        assert NewlinesToPeriods.process("The symphony was performed\nto a standing ovation.") == "The symphony was performed to a standing ovation."

    def test_art_wrap_01(self):
        assert NewlinesToPeriods.process("The painting was acquired by\nthe museum in 1923.") == "The painting was acquired by the museum in 1923."

    def test_architecture_wrap_01(self):
        assert NewlinesToPeriods.process("The tower was built in\nthe Gothic style during the fourteenth century.") == "The tower was built in the Gothic style during the fourteenth century."

    def test_agriculture_wrap_01(self):
        assert NewlinesToPeriods.process("The harvest was poor due to\ndrought throughout the summer months.") == "The harvest was poor due to drought throughout the summer months."

    def test_military_wrap_01(self):
        assert NewlinesToPeriods.process("The regiment was ordered to\nadvance at first light.") == "The regiment was ordered to advance at first light."

    def test_religion_wrap_01(self):
        assert NewlinesToPeriods.process("The pilgrimage attracts thousands\nof visitors each year.") == "The pilgrimage attracts thousands of visitors each year."

    def test_geography_wrap_01(self):
        assert NewlinesToPeriods.process("The river rises in the mountains\nand flows south to the sea.") == "The river rises in the mountains and flows south to the sea."

    def test_geography_wrap_02(self):
        assert NewlinesToPeriods.process("The island is separated from the\nmainland by a narrow channel.") == "The island is separated from the mainland by a narrow channel."

    def test_biography_wrap_01(self):
        assert NewlinesToPeriods.process("He was born in a small village\nnear the border in 1843.") == "He was born in a small village near the border in 1843."

    def test_biography_wrap_02(self):
        assert NewlinesToPeriods.process("After studying law in Paris she\nreturned to her homeland.") == "After studying law in Paris she returned to her homeland."

    def test_autobiography_wrap_01(self):
        assert NewlinesToPeriods.process("I remember the day clearly as\nif it had happened yesterday.") == "I remember the day clearly as if it had happened yesterday."

    def test_memoir_wrap_01(self):
        assert NewlinesToPeriods.process("My father never spoke of\nthe war years.") == "My father never spoke of the war years."

    def test_diary_wrap_01(self):
        assert NewlinesToPeriods.process("Tuesday. Woke at six and\nwent straight to the fields.") == "Tuesday. Woke at six and went straight to the fields."

    def test_politics_wrap_01(self):
        assert NewlinesToPeriods.process("The opposition called for a vote\nof no confidence in the government.") == "The opposition called for a vote of no confidence in the government."

    def test_economics_b_wrap_01(self):
        assert NewlinesToPeriods.process("Trade between the two nations\nhas grown steadily over the decade.") == "Trade between the two nations has grown steadily over the decade."

    def test_psychology_wrap_01(self):
        assert NewlinesToPeriods.process("Children exposed to early stress\nshowed higher levels of cortisol.") == "Children exposed to early stress showed higher levels of cortisol."

    def test_sociology_wrap_01(self):
        assert NewlinesToPeriods.process("Urban migration accelerated during\nthe second half of the century.") == "Urban migration accelerated during the second half of the century."

    def test_wrap_after_whether_01(self):
        assert NewlinesToPeriods.process("He did not know whether\nto laugh or cry.") == "He did not know whether to laugh or cry."

    def test_wrap_after_while_01(self):
        assert NewlinesToPeriods.process("While walking through the park\nshe noticed the dog was missing.") == "While walking through the park she noticed the dog was missing."

    def test_wrap_after_although_01(self):
        assert NewlinesToPeriods.process("Although the evidence was slim\nthe jury returned a guilty verdict.") == "Although the evidence was slim the jury returned a guilty verdict."

    def test_wrap_after_because_01(self):
        assert NewlinesToPeriods.process("She stayed indoors because\nthe weather was too cold.") == "She stayed indoors because the weather was too cold."

    def test_wrap_after_since_01(self):
        assert NewlinesToPeriods.process("Since arriving in the city he\nhad found no work.") == "Since arriving in the city he had found no work."

    def test_wrap_after_when_01(self):
        assert NewlinesToPeriods.process("When the bell rang she\nput down her pen.") == "When the bell rang she put down her pen."

    def test_wrap_after_where_01(self):
        assert NewlinesToPeriods.process("He could not recall where\nhe had last seen the document.") == "He could not recall where he had last seen the document."

    def test_wrap_after_if_01(self):
        assert NewlinesToPeriods.process("If the weather holds we\nshall start tomorrow.") == "If the weather holds we shall start tomorrow."

    def test_wrap_after_unless_01(self):
        assert NewlinesToPeriods.process("Unless you act now the\nopportunity will be lost.") == "Unless you act now the opportunity will be lost."

    def test_wrap_after_until_01(self):
        assert NewlinesToPeriods.process("She waited at the station until\nthe last train had departed.") == "She waited at the station until the last train had departed."

    def test_wrap_after_before_01(self):
        assert NewlinesToPeriods.process("He checked the map before\nsetting off into the forest.") == "He checked the map before setting off into the forest."

    def test_wrap_after_after_01(self):
        assert NewlinesToPeriods.process("After the meeting they\nwent for coffee together.") == "After the meeting they went for coffee together."

    def test_wrap_compound_noun_01(self):
        assert NewlinesToPeriods.process("The office\nmanager reviewed the report.") == "The office manager reviewed the report."

    def test_wrap_compound_noun_02(self):
        assert NewlinesToPeriods.process("The fire\nstation was on the corner.") == "The fire station was on the corner."

    def test_wrap_compound_noun_03(self):
        assert NewlinesToPeriods.process("The post\noffice opened at nine.") == "The post office opened at nine."

    def test_wrap_compound_noun_04(self):
        assert NewlinesToPeriods.process("The night\nwatchman made his rounds.") == "The night watchman made his rounds."

    def test_wrap_compound_noun_05(self):
        assert NewlinesToPeriods.process("The book\nkeeper checked the ledgers.") == "The book keeper checked the ledgers."

    def test_advertisement_wrap_01(self):
        assert NewlinesToPeriods.process("Wanted: A number of bright young men to\nassist in the business department.") == "Wanted: A number of bright young men to assist in the business department."

    def test_advertisement_wrap_02(self):
        assert NewlinesToPeriods.process("Apply to the Business Manager\nbetween 9 and 10 a.m.") == "Apply to the Business Manager between 9 and 10 a.m."

    def test_advertisement_wrap_03(self):
        assert NewlinesToPeriods.process("Promotion possible for the right\ncandidate.") == "Promotion possible for the right candidate."

    def test_wrap_after_however_01(self):
        assert NewlinesToPeriods.process("However, she could not\nbring herself to agree.") == "However, she could not bring herself to agree."

    def test_wrap_after_therefore_01(self):
        assert NewlinesToPeriods.process("Therefore he decided to\npostpone the journey.") == "Therefore he decided to postpone the journey."

    def test_wrap_after_moreover_01(self):
        assert NewlinesToPeriods.process("Moreover the evidence clearly\npointed in one direction.") == "Moreover the evidence clearly pointed in one direction."

    def test_wrap_after_nevertheless_01(self):
        assert NewlinesToPeriods.process("Nevertheless she pressed on\nwith the investigation.") == "Nevertheless she pressed on with the investigation."

    def test_wrap_after_furthermore_01(self):
        assert NewlinesToPeriods.process("Furthermore the company had\nfailed to disclose the risk.") == "Furthermore the company had failed to disclose the risk."

    def test_no_corruption_word_boundary_01(self):
        """Verify no word.word corruption in simple wrap."""
        result = NewlinesToPeriods.process("assist in the business\ndepartment during the holidays.")
        assert "business.department" not in result
        assert result == "assist in the business department during the holidays."

    def test_no_corruption_word_boundary_02(self):
        """Verify no word.word corruption — wrap after adjective."""
        result = NewlinesToPeriods.process("bright young\nmen to assist.")
        assert "young.men" not in result
        assert result == "bright young men to assist."

    def test_no_corruption_word_boundary_03(self):
        """Verify no word.word corruption — wrap after preposition."""
        result = NewlinesToPeriods.process("assist in\nthe business.")
        assert "in.the" not in result
        assert result == "assist in the business."
