# -*- coding: UTF-8 -*-
"""Xfail tests for hard-wrap boundary cases in NewlinesToPeriods (issue #42).

These tests target word-boundary transitions at the wrap point that are
currently corrupted by the pipeline. After the fix (strip-per-line in
NewlinesToPeriods), all should xpass.

Covers:
  P. Verb + preposition at wrap boundary
  Q. Adjective + noun at wrap boundary
  R. Noun + verb at wrap boundary (end of clause)
  S. Conjunction + continuation
  T. Determiners / articles at wrap boundary
  U. Numbers and quantities at wrap boundary
  V. Proper noun compounds at wrap boundary
  W. Profession / title compounds
  X. Time and date expressions at wrap boundary
  Y. Compound verb phrases at wrap boundary
  Z. Idiomatic phrases at wrap boundary

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

import pytest
from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods
from fast_sentence_segment import segment_text


class TestXfailBoundaryCases:
    """Xfail tests for word-boundary wrap corruption (issue #42)."""

    # ================================================================ P. Verb + preposition

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'looked.across' (issue #42)")
    def test_verb_prep_001(self):
        assert NewlinesToPeriods.process(
            "He looked\n    across the wide valley."
        ) == "He looked across the wide valley."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'walked.into' (issue #42)")
    def test_verb_prep_002(self):
        assert NewlinesToPeriods.process(
            "She walked\n    into the crowded room."
        ) == "She walked into the crowded room."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'sat.beside' (issue #42)")
    def test_verb_prep_003(self):
        assert NewlinesToPeriods.process(
            "He sat\n    beside her in the theatre."
        ) == "He sat beside her in the theatre."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'reached.for' (issue #42)")
    def test_verb_prep_004(self):
        assert NewlinesToPeriods.process(
            "She reached\n    for the book on the shelf."
        ) == "She reached for the book on the shelf."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'listened.to' (issue #42)")
    def test_verb_prep_005(self):
        assert NewlinesToPeriods.process(
            "He listened\n    to the sound of the rain."
        ) == "He listened to the sound of the rain."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'called.for' (issue #42)")
    def test_verb_prep_006(self):
        assert NewlinesToPeriods.process(
            "She called\n    for assistance immediately."
        ) == "She called for assistance immediately."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'applied.to' (issue #42)")
    def test_verb_prep_007(self):
        assert NewlinesToPeriods.process(
            "He applied\n    to the Business Manager between nine and ten."
        ) == "He applied to the Business Manager between nine and ten."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'handed.over' (issue #42)")
    def test_verb_prep_008(self):
        assert NewlinesToPeriods.process(
            "She handed\n    over the keys without a word."
        ) == "She handed over the keys without a word."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'turned.away' (issue #42)")
    def test_verb_prep_009(self):
        assert NewlinesToPeriods.process(
            "He turned\n    away from the window."
        ) == "He turned away from the window."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'headed.towards' (issue #42)")
    def test_verb_prep_010(self):
        assert NewlinesToPeriods.process(
            "She headed\n    towards the station at a run."
        ) == "She headed towards the station at a run."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'stood.before' (issue #42)")
    def test_verb_prep_011(self):
        assert NewlinesToPeriods.process(
            "He stood\n    before the magistrate in silence."
        ) == "He stood before the magistrate in silence."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'ran.through' (issue #42)")
    def test_verb_prep_012(self):
        assert NewlinesToPeriods.process(
            "She ran\n    through the list one more time."
        ) == "She ran through the list one more time."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'waited.for' (issue #42)")
    def test_verb_prep_013(self):
        assert NewlinesToPeriods.process(
            "He waited\n    for the reply until dusk."
        ) == "He waited for the reply until dusk."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'spoke.of' (issue #42)")
    def test_verb_prep_014(self):
        assert NewlinesToPeriods.process(
            "She spoke\n    of old friends with great warmth."
        ) == "She spoke of old friends with great warmth."

    @pytest.mark.xfail(reason="4-space wrap: verb+prep 'cared.for' (issue #42)")
    def test_verb_prep_015(self):
        assert NewlinesToPeriods.process(
            "She cared\n    for her mother throughout the illness."
        ) == "She cared for her mother throughout the illness."

    # ================================================================ Q. Adjective + noun

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'young.men' (issue #42)")
    def test_adj_noun_001(self):
        assert NewlinesToPeriods.process(
            "A number of bright young\n    men applied for the post."
        ) == "A number of bright young men applied for the post."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'long.corridor' (issue #42)")
    def test_adj_noun_002(self):
        assert NewlinesToPeriods.process(
            "She walked down the long\n    corridor towards the exit."
        ) == "She walked down the long corridor towards the exit."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'dark.forest' (issue #42)")
    def test_adj_noun_003(self):
        assert NewlinesToPeriods.process(
            "He entered the dark\n    forest without a lantern."
        ) == "He entered the dark forest without a lantern."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'heavy.door' (issue #42)")
    def test_adj_noun_004(self):
        assert NewlinesToPeriods.process(
            "He pushed open the heavy\n    door and stepped inside."
        ) == "He pushed open the heavy door and stepped inside."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'cold.wind' (issue #42)")
    def test_adj_noun_005(self):
        assert NewlinesToPeriods.process(
            "A cold\n    wind swept through the narrow street."
        ) == "A cold wind swept through the narrow street."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'bright.sun' (issue #42)")
    def test_adj_noun_006(self):
        assert NewlinesToPeriods.process(
            "The bright\n    sun was already high when they set out."
        ) == "The bright sun was already high when they set out."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'quiet.street' (issue #42)")
    def test_adj_noun_007(self):
        assert NewlinesToPeriods.process(
            "They lived on a quiet\n    street behind the market."
        ) == "They lived on a quiet street behind the market."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'distant.hills' (issue #42)")
    def test_adj_noun_008(self):
        assert NewlinesToPeriods.process(
            "She could see the distant\n    hills through the mist."
        ) == "She could see the distant hills through the mist."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'small.room' (issue #42)")
    def test_adj_noun_009(self):
        assert NewlinesToPeriods.process(
            "He was shown into a small\n    room at the back of the house."
        ) == "He was shown into a small room at the back of the house."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'old.woman' (issue #42)")
    def test_adj_noun_010(self):
        assert NewlinesToPeriods.process(
            "An old\n    woman sat by the gate knitting."
        ) == "An old woman sat by the gate knitting."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'tall.man' (issue #42)")
    def test_adj_noun_011(self):
        assert NewlinesToPeriods.process(
            "A tall\n    man entered without knocking."
        ) == "A tall man entered without knocking."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'narrow.lane' (issue #42)")
    def test_adj_noun_012(self):
        assert NewlinesToPeriods.process(
            "They turned into a narrow\n    lane behind the churchyard."
        ) == "They turned into a narrow lane behind the churchyard."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'large.estate' (issue #42)")
    def test_adj_noun_013(self):
        assert NewlinesToPeriods.process(
            "He inherited a large\n    estate in the north of the county."
        ) == "He inherited a large estate in the north of the county."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'bitter.cold' (issue #42)")
    def test_adj_noun_014(self):
        assert NewlinesToPeriods.process(
            "The bitter\n    cold kept them indoors for three days."
        ) == "The bitter cold kept them indoors for three days."

    @pytest.mark.xfail(reason="4-space wrap: adj+noun 'empty.house' (issue #42)")
    def test_adj_noun_015(self):
        assert NewlinesToPeriods.process(
            "He stood outside the empty\n    house for a long time."
        ) == "He stood outside the empty house for a long time."

    # ================================================================ R. Noun + verb (end of clause)

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'door.opened' (issue #42)")
    def test_noun_verb_001(self):
        assert NewlinesToPeriods.process(
            "Suddenly the door\n    opened and he stepped in."
        ) == "Suddenly the door opened and he stepped in."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'clock.struck' (issue #42)")
    def test_noun_verb_002(self):
        assert NewlinesToPeriods.process(
            "At that moment the clock\n    struck twelve."
        ) == "At that moment the clock struck twelve."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'rain.fell' (issue #42)")
    def test_noun_verb_003(self):
        assert NewlinesToPeriods.process(
            "All night long the rain\n    fell without ceasing."
        ) == "All night long the rain fell without ceasing."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'sun.rose' (issue #42)")
    def test_noun_verb_004(self):
        assert NewlinesToPeriods.process(
            "Just before five the sun\n    rose above the eastern hills."
        ) == "Just before five the sun rose above the eastern hills."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'fire.burned' (issue #42)")
    def test_noun_verb_005(self):
        assert NewlinesToPeriods.process(
            "In the grate a small fire\n    burned steadily all evening."
        ) == "In the grate a small fire burned steadily all evening."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'wind.howled' (issue #42)")
    def test_noun_verb_006(self):
        assert NewlinesToPeriods.process(
            "Outside the wind\n    howled through the trees."
        ) == "Outside the wind howled through the trees."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'crowd.gathered' (issue #42)")
    def test_noun_verb_007(self):
        assert NewlinesToPeriods.process(
            "Within minutes a crowd\n    gathered at the corner."
        ) == "Within minutes a crowd gathered at the corner."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'light.appeared' (issue #42)")
    def test_noun_verb_008(self):
        assert NewlinesToPeriods.process(
            "Far ahead a faint light\n    appeared through the fog."
        ) == "Far ahead a faint light appeared through the fog."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'horse.stopped' (issue #42)")
    def test_noun_verb_009(self):
        assert NewlinesToPeriods.process(
            "Without warning the horse\n    stopped dead in its tracks."
        ) == "Without warning the horse stopped dead in its tracks."

    @pytest.mark.xfail(reason="4-space wrap: noun+verb 'silence.fell' (issue #42)")
    def test_noun_verb_010(self):
        assert NewlinesToPeriods.process(
            "At his words a deep silence\n    fell over the assembly."
        ) == "At his words a deep silence fell over the assembly."

    # ================================================================ S. Conjunction at wrap

    @pytest.mark.xfail(reason="4-space wrap: conj 'and.the' continuation (issue #42)")
    def test_conj_001(self):
        assert NewlinesToPeriods.process(
            "He rose from his chair and\n    the others followed his lead."
        ) == "He rose from his chair and the others followed his lead."

    @pytest.mark.xfail(reason="4-space wrap: conj 'but.she' continuation (issue #42)")
    def test_conj_002(self):
        assert NewlinesToPeriods.process(
            "He insisted it was unnecessary but\n    she refused to be persuaded."
        ) == "He insisted it was unnecessary but she refused to be persuaded."

    @pytest.mark.xfail(reason="4-space wrap: conj 'or.the' continuation (issue #42)")
    def test_conj_003(self):
        assert NewlinesToPeriods.process(
            "You must either agree or\n    the matter goes to arbitration."
        ) == "You must either agree or the matter goes to arbitration."

    @pytest.mark.xfail(reason="4-space wrap: conj 'yet.he' continuation (issue #42)")
    def test_conj_004(self):
        assert NewlinesToPeriods.process(
            "She had every reason to refuse yet\n    he could not bring himself to ask."
        ) == "She had every reason to refuse yet he could not bring himself to ask."

    @pytest.mark.xfail(reason="4-space wrap: conj 'so.they' continuation (issue #42)")
    def test_conj_005(self):
        assert NewlinesToPeriods.process(
            "The weather turned bad so\n    they postponed the excursion."
        ) == "The weather turned bad so they postponed the excursion."

    @pytest.mark.xfail(reason="4-space wrap: conj 'while.the' continuation (issue #42)")
    def test_conj_006(self):
        assert NewlinesToPeriods.process(
            "He read the papers while\n    the others played cards."
        ) == "He read the papers while the others played cards."

    @pytest.mark.xfail(reason="4-space wrap: conj 'although.she' continuation (issue #42)")
    def test_conj_007(self):
        assert NewlinesToPeriods.process(
            "He pressed on although\n    she warned him of the risk."
        ) == "He pressed on although she warned him of the risk."

    @pytest.mark.xfail(reason="4-space wrap: conj 'because.he' continuation (issue #42)")
    def test_conj_008(self):
        assert NewlinesToPeriods.process(
            "She stayed behind because\n    he had asked her to wait."
        ) == "She stayed behind because he had asked her to wait."

    @pytest.mark.xfail(reason="4-space wrap: conj 'since.the' continuation (issue #42)")
    def test_conj_009(self):
        assert NewlinesToPeriods.process(
            "Nothing had changed since\n    the family moved away."
        ) == "Nothing had changed since the family moved away."

    @pytest.mark.xfail(reason="4-space wrap: conj 'until.she' continuation (issue #42)")
    def test_conj_010(self):
        assert NewlinesToPeriods.process(
            "He waited until\n    she returned before speaking."
        ) == "He waited until she returned before speaking."

    # ================================================================ T. Determiners at wrap

    @pytest.mark.xfail(reason="4-space wrap: det 'the.business' (issue #42)")
    def test_det_001(self):
        assert NewlinesToPeriods.process(
            "He managed the\n    business with great efficiency."
        ) == "He managed the business with great efficiency."

    @pytest.mark.xfail(reason="4-space wrap: det 'a.number' (issue #42)")
    def test_det_002(self):
        assert NewlinesToPeriods.process(
            "They employed a\n    number of skilled craftsmen."
        ) == "They employed a number of skilled craftsmen."

    @pytest.mark.xfail(reason="4-space wrap: det 'this.matter' (issue #42)")
    def test_det_003(self):
        assert NewlinesToPeriods.process(
            "She would not speak of this\n    matter any further."
        ) == "She would not speak of this matter any further."

    @pytest.mark.xfail(reason="4-space wrap: det 'every.morning' (issue #42)")
    def test_det_004(self):
        assert NewlinesToPeriods.process(
            "He walked there every\n    morning without fail."
        ) == "He walked there every morning without fail."

    @pytest.mark.xfail(reason="4-space wrap: det 'each.day' (issue #42)")
    def test_det_005(self):
        assert NewlinesToPeriods.process(
            "She wrote in her journal each\n    day before retiring."
        ) == "She wrote in her journal each day before retiring."

    @pytest.mark.xfail(reason="4-space wrap: det 'no.further' (issue #42)")
    def test_det_006(self):
        assert NewlinesToPeriods.process(
            "He said there was no\n    further need to discuss it."
        ) == "He said there was no further need to discuss it."

    @pytest.mark.xfail(reason="4-space wrap: det 'some.weeks' (issue #42)")
    def test_det_007(self):
        assert NewlinesToPeriods.process(
            "After some\n    weeks the letter arrived at last."
        ) == "After some weeks the letter arrived at last."

    @pytest.mark.xfail(reason="4-space wrap: det 'any.reply' (issue #42)")
    def test_det_008(self):
        assert NewlinesToPeriods.process(
            "He had not received any\n    reply to his enquiry."
        ) == "He had not received any reply to his enquiry."

    @pytest.mark.xfail(reason="4-space wrap: det 'their.departure' (issue #42)")
    def test_det_009(self):
        assert NewlinesToPeriods.process(
            "Nothing was said about their\n    departure until the morning."
        ) == "Nothing was said about their departure until the morning."

    @pytest.mark.xfail(reason="4-space wrap: det 'its.contents' (issue #42)")
    def test_det_010(self):
        assert NewlinesToPeriods.process(
            "He examined the box and its\n    contents with great care."
        ) == "He examined the box and its contents with great care."

    # ================================================================ U. Numbers / quantities

    @pytest.mark.xfail(reason="4-space wrap: num 'twenty.years' (issue #42)")
    def test_num_001(self):
        assert NewlinesToPeriods.process(
            "He had lived there for twenty\n    years without once leaving."
        ) == "He had lived there for twenty years without once leaving."

    @pytest.mark.xfail(reason="4-space wrap: num 'three.hundred' (issue #42)")
    def test_num_002(self):
        assert NewlinesToPeriods.process(
            "She inherited three\n    hundred acres from her uncle."
        ) == "She inherited three hundred acres from her uncle."

    @pytest.mark.xfail(reason="4-space wrap: num 'forty.miles' (issue #42)")
    def test_num_003(self):
        assert NewlinesToPeriods.process(
            "The nearest town was forty\n    miles away across the heath."
        ) == "The nearest town was forty miles away across the heath."

    @pytest.mark.xfail(reason="4-space wrap: num 'nine.o'clock' (issue #42)")
    def test_num_004(self):
        assert NewlinesToPeriods.process(
            "Apply to the Business Manager between nine and ten\n    o'clock in the morning."
        ) == "Apply to the Business Manager between nine and ten o'clock in the morning."

    @pytest.mark.xfail(reason="4-space wrap: num 'six.weeks' (issue #42)")
    def test_num_005(self):
        assert NewlinesToPeriods.process(
            "The voyage took six\n    weeks in favourable winds."
        ) == "The voyage took six weeks in favourable winds."

    @pytest.mark.xfail(reason="4-space wrap: num 'fifty.men' (issue #42)")
    def test_num_006(self):
        assert NewlinesToPeriods.process(
            "The regiment lost fifty\n    men in the engagement."
        ) == "The regiment lost fifty men in the engagement."

    @pytest.mark.xfail(reason="4-space wrap: num 'two.hundred' (issue #42)")
    def test_num_007(self):
        assert NewlinesToPeriods.process(
            "She had saved two\n    hundred pounds over ten years."
        ) == "She had saved two hundred pounds over ten years."

    @pytest.mark.xfail(reason="4-space wrap: num 'ten.shillings' (issue #42)")
    def test_num_008(self):
        assert NewlinesToPeriods.process(
            "The weekly wage was ten\n    shillings and sixpence."
        ) == "The weekly wage was ten shillings and sixpence."

    @pytest.mark.xfail(reason="4-space wrap: num 'fifteen.minutes' (issue #42)")
    def test_num_009(self):
        assert NewlinesToPeriods.process(
            "He arrived fifteen\n    minutes before the appointed hour."
        ) == "He arrived fifteen minutes before the appointed hour."

    @pytest.mark.xfail(reason="4-space wrap: num 'a.thousand' (issue #42)")
    def test_num_010(self):
        assert NewlinesToPeriods.process(
            "He could not raise a\n    thousand pounds at short notice."
        ) == "He could not raise a thousand pounds at short notice."

    # ================================================================ V. Proper noun compounds

    @pytest.mark.xfail(reason="4-space wrap: proper 'New.York' corruption (issue #42)")
    def test_proper_001(self):
        assert NewlinesToPeriods.process(
            "She had always wanted to visit New\n    York in the spring."
        ) == "She had always wanted to visit New York in the spring."

    @pytest.mark.xfail(reason="4-space wrap: proper 'North.America' corruption (issue #42)")
    def test_proper_002(self):
        assert NewlinesToPeriods.process(
            "He planned to emigrate to North\n    America before the end of the year."
        ) == "He planned to emigrate to North America before the end of the year."

    @pytest.mark.xfail(reason="4-space wrap: proper 'South.Africa' corruption (issue #42)")
    def test_proper_003(self):
        assert NewlinesToPeriods.process(
            "He served in South\n    Africa during the Boer War."
        ) == "He served in South Africa during the Boer War."

    @pytest.mark.xfail(reason="4-space wrap: proper 'New.Zealand' corruption (issue #42)")
    def test_proper_004(self):
        assert NewlinesToPeriods.process(
            "They emigrated to New\n    Zealand and never returned."
        ) == "They emigrated to New Zealand and never returned."

    @pytest.mark.xfail(reason="4-space wrap: proper 'West.Indies' corruption (issue #42)")
    def test_proper_005(self):
        assert NewlinesToPeriods.process(
            "He made his fortune in the West\n    Indies as a sugar planter."
        ) == "He made his fortune in the West Indies as a sugar planter."

    @pytest.mark.xfail(reason="4-space wrap: proper 'East.India' corruption (issue #42)")
    def test_proper_006(self):
        assert NewlinesToPeriods.process(
            "He worked for the East\n    India Company for twenty years."
        ) == "He worked for the East India Company for twenty years."

    @pytest.mark.xfail(reason="4-space wrap: proper 'British.Columbia' corruption (issue #42)")
    def test_proper_007(self):
        assert NewlinesToPeriods.process(
            "They settled in British\n    Columbia on the Pacific coast."
        ) == "They settled in British Columbia on the Pacific coast."

    @pytest.mark.xfail(reason="4-space wrap: proper 'Cape.Town' corruption (issue #42)")
    def test_proper_008(self):
        assert NewlinesToPeriods.process(
            "The ship put in at Cape\n    Town to take on provisions."
        ) == "The ship put in at Cape Town to take on provisions."

    @pytest.mark.xfail(reason="4-space wrap: proper 'Hong.Kong' corruption (issue #42)")
    def test_proper_009(self):
        assert NewlinesToPeriods.process(
            "He had been stationed in Hong\n    Kong for three years."
        ) == "He had been stationed in Hong Kong for three years."

    @pytest.mark.xfail(reason="4-space wrap: proper 'St.Petersburg' corruption (issue #42)")
    def test_proper_010(self):
        assert NewlinesToPeriods.process(
            "She had spent a winter in St\n    Petersburg at the Imperial court."
        ) == "She had spent a winter in St Petersburg at the Imperial court."

    # ================================================================ W. Profession / title

    @pytest.mark.xfail(reason="4-space wrap: title 'Business.Manager' (issue #42)")
    def test_title_001(self):
        assert NewlinesToPeriods.process(
            "Apply to the Business\n    Manager between nine and ten a.m."
        ) == "Apply to the Business Manager between nine and ten a.m."

    @pytest.mark.xfail(reason="4-space wrap: title 'General.Manager' (issue #42)")
    def test_title_002(self):
        assert NewlinesToPeriods.process(
            "He was appointed General\n    Manager after the reorganisation."
        ) == "He was appointed General Manager after the reorganisation."

    @pytest.mark.xfail(reason="4-space wrap: title 'Advertising.Manager' (issue #42)")
    def test_title_003(self):
        assert NewlinesToPeriods.process(
            "She reported to the Advertising\n    Manager on a daily basis."
        ) == "She reported to the Advertising Manager on a daily basis."

    @pytest.mark.xfail(reason="4-space wrap: title 'Sales.Manager' (issue #42)")
    def test_title_004(self):
        assert NewlinesToPeriods.process(
            "He was promoted to Sales\n    Manager after five years."
        ) == "He was promoted to Sales Manager after five years."

    @pytest.mark.xfail(reason="4-space wrap: title 'Chief.Clerk' (issue #42)")
    def test_title_005(self):
        assert NewlinesToPeriods.process(
            "She applied for the post of Chief\n    Clerk at the firm."
        ) == "She applied for the post of Chief Clerk at the firm."

    @pytest.mark.xfail(reason="4-space wrap: title 'Senior.Partner' (issue #42)")
    def test_title_006(self):
        assert NewlinesToPeriods.process(
            "He became Senior\n    Partner at the age of fifty."
        ) == "He became Senior Partner at the age of fifty."

    @pytest.mark.xfail(reason="4-space wrap: title 'Deputy.Chairman' (issue #42)")
    def test_title_007(self):
        assert NewlinesToPeriods.process(
            "He was appointed Deputy\n    Chairman of the committee."
        ) == "He was appointed Deputy Chairman of the committee."

    @pytest.mark.xfail(reason="4-space wrap: title 'Head.Teacher' (issue #42)")
    def test_title_008(self):
        assert NewlinesToPeriods.process(
            "She had served as Head\n    Teacher for twenty years."
        ) == "She had served as Head Teacher for twenty years."

    @pytest.mark.xfail(reason="4-space wrap: title 'Company.Secretary' (issue #42)")
    def test_title_009(self):
        assert NewlinesToPeriods.process(
            "He was retained as Company\n    Secretary at an annual salary."
        ) == "He was retained as Company Secretary at an annual salary."

    @pytest.mark.xfail(reason="4-space wrap: title 'Managing.Director' (issue #42)")
    def test_title_010(self):
        assert NewlinesToPeriods.process(
            "She had risen to the post of Managing\n    Director in just ten years."
        ) == "She had risen to the post of Managing Director in just ten years."

    # ================================================================ X. Time / date expressions

    @pytest.mark.xfail(reason="4-space wrap: time 'Christmas.holidays' (issue #42)")
    def test_time_001(self):
        assert NewlinesToPeriods.process(
            "They would return after the Christmas\n    holidays at the end of January."
        ) == "They would return after the Christmas holidays at the end of January."

    @pytest.mark.xfail(reason="4-space wrap: time 'Easter.week' (issue #42)")
    def test_time_002(self):
        assert NewlinesToPeriods.process(
            "The event was planned for Easter\n    week in late April."
        ) == "The event was planned for Easter week in late April."

    @pytest.mark.xfail(reason="4-space wrap: time 'harvest.season' (issue #42)")
    def test_time_003(self):
        assert NewlinesToPeriods.process(
            "All hands were hired for the harvest\n    season in September."
        ) == "All hands were hired for the harvest season in September."

    @pytest.mark.xfail(reason="4-space wrap: time 'bank.holiday' (issue #42)")
    def test_time_004(self):
        assert NewlinesToPeriods.process(
            "The office was closed for the August bank\n    holiday."
        ) == "The office was closed for the August bank holiday."

    @pytest.mark.xfail(reason="4-space wrap: time 'midsummer.night' (issue #42)")
    def test_time_005(self):
        assert NewlinesToPeriods.process(
            "They celebrated on mid summer\n    night with a bonfire."
        ) == "They celebrated on mid summer night with a bonfire."

    @pytest.mark.xfail(reason="4-space wrap: time 'winter.quarter' (issue #42)")
    def test_time_006(self):
        assert NewlinesToPeriods.process(
            "Accounts were settled at the end of the winter\n    quarter."
        ) == "Accounts were settled at the end of the winter quarter."

    @pytest.mark.xfail(reason="4-space wrap: time 'morning.papers' (issue #42)")
    def test_time_007(self):
        assert NewlinesToPeriods.process(
            "He read the morning\n    papers with his coffee."
        ) == "He read the morning papers with his coffee."

    @pytest.mark.xfail(reason="4-space wrap: time 'evening.edition' (issue #42)")
    def test_time_008(self):
        assert NewlinesToPeriods.process(
            "She bought the evening\n    edition at the bookstall."
        ) == "She bought the evening edition at the bookstall."

    @pytest.mark.xfail(reason="4-space wrap: time 'Sunday.service' (issue #42)")
    def test_time_009(self):
        assert NewlinesToPeriods.process(
            "The family attended the Sunday\n    service at the local church."
        ) == "The family attended the Sunday service at the local church."

    @pytest.mark.xfail(reason="4-space wrap: time 'market.day' (issue #42)")
    def test_time_010(self):
        assert NewlinesToPeriods.process(
            "She drove into town on market\n    day and sold all her eggs."
        ) == "She drove into town on market day and sold all her eggs."

    # ================================================================ Y. Compound verb phrases

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'took.charge' (issue #42)")
    def test_verbal_001(self):
        assert NewlinesToPeriods.process(
            "He took\n    charge of the department without hesitation."
        ) == "He took charge of the department without hesitation."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'gave.notice' (issue #42)")
    def test_verbal_002(self):
        assert NewlinesToPeriods.process(
            "She gave\n    notice on the last day of the month."
        ) == "She gave notice on the last day of the month."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'made.good' (issue #42)")
    def test_verbal_003(self):
        assert NewlinesToPeriods.process(
            "He made\n    good his promise within the week."
        ) == "He made good his promise within the week."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'carried.out' (issue #42)")
    def test_verbal_004(self):
        assert NewlinesToPeriods.process(
            "The orders were carefully carried\n    out by the staff."
        ) == "The orders were carefully carried out by the staff."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'brought.forward' (issue #42)")
    def test_verbal_005(self):
        assert NewlinesToPeriods.process(
            "The meeting was brought\n    forward by two weeks."
        ) == "The meeting was brought forward by two weeks."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'put.forward' (issue #42)")
    def test_verbal_006(self):
        assert NewlinesToPeriods.process(
            "A new proposal was put\n    forward at the evening session."
        ) == "A new proposal was put forward at the evening session."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'called.upon' (issue #42)")
    def test_verbal_007(self):
        assert NewlinesToPeriods.process(
            "He was called\n    upon to address the committee."
        ) == "He was called upon to address the committee."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'passed.over' (issue #42)")
    def test_verbal_008(self):
        assert NewlinesToPeriods.process(
            "He felt he had been passed\n    over for the promotion."
        ) == "He felt he had been passed over for the promotion."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'set.aside' (issue #42)")
    def test_verbal_009(self):
        assert NewlinesToPeriods.process(
            "All personal considerations must be set\n    aside for the common good."
        ) == "All personal considerations must be set aside for the common good."

    @pytest.mark.xfail(reason="4-space wrap: phrasal 'laid.down' (issue #42)")
    def test_verbal_010(self):
        assert NewlinesToPeriods.process(
            "The rules were clearly laid\n    down in the original charter."
        ) == "The rules were clearly laid down in the original charter."

    # ================================================================ Z. Idiomatic phrases

    @pytest.mark.xfail(reason="4-space wrap: idiom 'business.department' Dreiser (issue #42)")
    def test_idiom_001(self):
        result = segment_text(
            "Wanted: A number of bright young men to assist in the business\n"
            "    department during the Christmas holidays.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'Promotion.possible' (issue #42)")
    def test_idiom_002(self):
        result = segment_text(
            "Promotion possible.\n"
            "    Apply to Business Manager between 9 and 10 a.m.",
            flatten=True,
        )
        assert "possible.Apply" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'health.department' (issue #42)")
    def test_idiom_003(self):
        result = segment_text(
            "The local health\n    department issued an urgent warning.",
            flatten=True,
        )
        assert "health.department" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'finance.committee' (issue #42)")
    def test_idiom_004(self):
        result = segment_text(
            "The finance\n    committee approved the budget unanimously.",
            flatten=True,
        )
        assert "finance.committee" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'fire.station' pipeline (issue #42)")
    def test_idiom_005(self):
        result = segment_text(
            "The alarm sounded at the fire\n    station at two in the morning.",
            flatten=True,
        )
        assert "fire.station" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'post.office' pipeline (issue #42)")
    def test_idiom_006(self):
        result = segment_text(
            "She went to the post\n    office to buy stamps and send parcels.",
            flatten=True,
        )
        assert "post.office" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'night.watchman' pipeline (issue #42)")
    def test_idiom_007(self):
        result = segment_text(
            "The night\n    watchman made his rounds without incident.",
            flatten=True,
        )
        assert "night.watchman" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'town.council' pipeline (issue #42)")
    def test_idiom_008(self):
        result = segment_text(
            "He stood for election to the town\n    council in the autumn.",
            flatten=True,
        )
        assert "town.council" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'foreign.office' pipeline (issue #42)")
    def test_idiom_009(self):
        result = segment_text(
            "The telegram arrived from the foreign\n    office at midnight.",
            flatten=True,
        )
        assert "foreign.office" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: idiom 'board.members' pipeline (issue #42)")
    def test_idiom_010(self):
        result = segment_text(
            "All board\n    members were present at the extraordinary meeting.",
            flatten=True,
        )
        assert "board.members" not in " ".join(result)

    # ================================================================ Extra: assorted short clauses

    @pytest.mark.xfail(reason="4-space wrap: short clause 'quite.right' (issue #42)")
    def test_extra_001(self):
        assert NewlinesToPeriods.process(
            "He was quite\n    right to refuse the offer."
        ) == "He was quite right to refuse the offer."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'very.well' (issue #42)")
    def test_extra_002(self):
        assert NewlinesToPeriods.process(
            "She knew perfectly very\n    well what he meant."
        ) == "She knew perfectly very well what he meant."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'more.than' (issue #42)")
    def test_extra_003(self):
        assert NewlinesToPeriods.process(
            "It would cost him more\n    than he could afford."
        ) == "It would cost him more than he could afford."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'much.better' (issue #42)")
    def test_extra_004(self):
        assert NewlinesToPeriods.process(
            "He felt much\n    better after a good night's rest."
        ) == "He felt much better after a good night's rest."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'quite.certain' (issue #42)")
    def test_extra_005(self):
        assert NewlinesToPeriods.process(
            "She was quite\n    certain she had locked the door."
        ) == "She was quite certain she had locked the door."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'rather.long' (issue #42)")
    def test_extra_006(self):
        assert NewlinesToPeriods.process(
            "It had been a rather\n    long and tiring journey."
        ) == "It had been a rather long and tiring journey."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'somewhat.surprised' (issue #42)")
    def test_extra_007(self):
        assert NewlinesToPeriods.process(
            "He was somewhat\n    surprised by the warmth of the welcome."
        ) == "He was somewhat surprised by the warmth of the welcome."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'entirely.wrong' (issue #42)")
    def test_extra_008(self):
        assert NewlinesToPeriods.process(
            "She had been entirely\n    wrong about the matter."
        ) == "She had been entirely wrong about the matter."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'barely.enough' (issue #42)")
    def test_extra_009(self):
        assert NewlinesToPeriods.process(
            "There was barely\n    enough light to see by."
        ) == "There was barely enough light to see by."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'nearly.finished' (issue #42)")
    def test_extra_010(self):
        assert NewlinesToPeriods.process(
            "He was nearly\n    finished when the bell rang."
        ) == "He was nearly finished when the bell rang."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'almost.certain' (issue #42)")
    def test_extra_011(self):
        assert NewlinesToPeriods.process(
            "She was almost\n    certain she recognised the voice."
        ) == "She was almost certain she recognised the voice."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'clearly.understood' (issue #42)")
    def test_extra_012(self):
        assert NewlinesToPeriods.process(
            "It was clearly\n    understood by all present."
        ) == "It was clearly understood by all present."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'perfectly.clear' (issue #42)")
    def test_extra_013(self):
        assert NewlinesToPeriods.process(
            "The instructions were perfectly\n    clear on the point."
        ) == "The instructions were perfectly clear on the point."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'directly.responsible' (issue #42)")
    def test_extra_014(self):
        assert NewlinesToPeriods.process(
            "He was held directly\n    responsible for the loss."
        ) == "He was held directly responsible for the loss."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'wholly.inadequate' (issue #42)")
    def test_extra_015(self):
        assert NewlinesToPeriods.process(
            "The response was wholly\n    inadequate and she said so."
        ) == "The response was wholly inadequate and she said so."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'absolutely.necessary' (issue #42)")
    def test_extra_016(self):
        assert NewlinesToPeriods.process(
            "It was absolutely\n    necessary to act without delay."
        ) == "It was absolutely necessary to act without delay."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'strictly.forbidden' (issue #42)")
    def test_extra_017(self):
        assert NewlinesToPeriods.process(
            "Entry to the building was strictly\n    forbidden after six o'clock."
        ) == "Entry to the building was strictly forbidden after six o'clock."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'deeply.grateful' (issue #42)")
    def test_extra_018(self):
        assert NewlinesToPeriods.process(
            "She said she was deeply\n    grateful for everything he had done."
        ) == "She said she was deeply grateful for everything he had done."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'highly.recommended' (issue #42)")
    def test_extra_019(self):
        assert NewlinesToPeriods.process(
            "The hotel was highly\n    recommended by the travel agency."
        ) == "The hotel was highly recommended by the travel agency."

    @pytest.mark.xfail(reason="4-space wrap: short clause 'widely.known' (issue #42)")
    def test_extra_020(self):
        assert NewlinesToPeriods.process(
            "It was widely\n    known that he had left the service."
        ) == "It was widely known that he had left the service."
