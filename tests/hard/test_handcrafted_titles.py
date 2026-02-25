# -*- coding: UTF-8 -*-
"""
Hand-crafted test cases for abbreviation suppression (Issue #47).

Each test is individually authored — no combinatoric generation.
Each test name describes the specific scenario being tested.

Related GitHub Issue:
    #47 - Abbreviations with trailing periods trigger false sentence splits
    https://github.com/craigtrim/fast-sentence-segment/issues/47
"""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestHandcraftedTitles:
    """Hand-crafted tests for title, honorific, rank, and government abbreviations."""

    @pytest.fixture
    def segment(self):
        """Provide the segmentation function for tests."""
        from fast_sentence_segment import segment_text
        def _segment(text):
            return segment_text(text, flatten=True, split_dialog=False)
        return _segment

    # ----------------------------------------------------------------- Dr. --

    def test_dr_before_surname(self, segment: SegmentationFunc):
        """Dr. before a surname — baseline, must not split."""
        text = "Dr. Smith confirmed the diagnosis on Tuesday."
        assert segment(text) == ["Dr. Smith confirmed the diagnosis on Tuesday."]

    def test_dr_before_first_name(self, segment: SegmentationFunc):
        """Dr. before a first name."""
        text = "Dr. Jane reviewed all the test results before making a decision."
        assert segment(text) == ["Dr. Jane reviewed all the test results before making a decision."]

    def test_dr_before_full_name(self, segment: SegmentationFunc):
        """Dr. before a full first-last name."""
        text = "Dr. Emily Watson presented the findings at the conference."
        assert segment(text) == ["Dr. Emily Watson presented the findings at the conference."]

    def test_dr_before_name_with_middle_initial(self, segment: SegmentationFunc):
        """Dr. followed by first name, middle initial, surname."""
        text = "The report was authored by Dr. Alan R. Thompson."
        assert segment(text) == ["The report was authored by Dr. Alan R. Thompson."]

    def test_dr_at_sentence_end_then_split(self, segment: SegmentationFunc):
        """Sentence ending with Dr.'s name — split must occur."""
        text = "The case was reviewed by Dr. Patel. The findings were conclusive."
        assert segment(text) == ["The case was reviewed by Dr. Patel.", "The findings were conclusive."]

    def test_dr_after_comma_mid_sentence(self, segment: SegmentationFunc):
        """Dr. after a comma in a mid-sentence list."""
        text = "The panel included several specialists, Dr. Adams, Dr. Baker, and Dr. Chen."
        assert segment(text) == ["The panel included several specialists, Dr. Adams, Dr. Baker, and Dr. Chen."]

    def test_dr_sentence_initial(self, segment: SegmentationFunc):
        """Dr. at the start of a sentence."""
        text = "Dr. Morrison was the first to document this phenomenon."
        assert segment(text) == ["Dr. Morrison was the first to document this phenomenon."]

    def test_dr_in_reported_speech(self, segment: SegmentationFunc):
        """Dr. in reported speech context."""
        text = "The committee heard that Dr. Williams disagreed with the methodology."
        assert segment(text) == ["The committee heard that Dr. Williams disagreed with the methodology."]

    def test_dr_two_doctors_same_sentence(self, segment: SegmentationFunc):
        """Two Dr. titles in the same sentence."""
        text = "Dr. Harris and Dr. Nguyen co-authored the paper."
        assert segment(text) == ["Dr. Harris and Dr. Nguyen co-authored the paper."]

    def test_dr_with_vs_opponent(self, segment: SegmentationFunc):
        """Dr. in a vs. legal context."""
        text = "The dispute in Dr. Reed vs. the Regional Health Authority was settled out of court."
        assert segment(text) == ["The dispute in Dr. Reed vs. the Regional Health Authority was settled out of court."]

    # ----------------------------------------------------------------- Mr. --

    def test_mr_before_surname(self, segment: SegmentationFunc):
        """Mr. before a surname — must not split."""
        text = "Mr. Johnson was late to the meeting."
        assert segment(text) == ["Mr. Johnson was late to the meeting."]

    def test_mr_before_full_name(self, segment: SegmentationFunc):
        """Mr. before full name."""
        text = "The letter was addressed to Mr. Robert Clarke."
        assert segment(text) == ["The letter was addressed to Mr. Robert Clarke."]

    def test_mr_and_mrs_together(self, segment: SegmentationFunc):
        """Mr. and Mrs. in the same sentence — must not split at either."""
        text = "The invitation was addressed to Mr. and Mrs. Johnson."
        assert segment(text) == ["The invitation was addressed to Mr. and Mrs. Johnson."]

    def test_mr_sentence_initial(self, segment: SegmentationFunc):
        """Mr. at the start of a sentence."""
        text = "Mr. Thompson submitted the complaint in writing."
        assert segment(text) == ["Mr. Thompson submitted the complaint in writing."]

    def test_mr_at_sentence_end_then_split(self, segment: SegmentationFunc):
        """Sentence ending at Mr. name then new sentence."""
        text = "The contract was signed by Mr. Davis. The terms were agreed beforehand."
        assert segment(text) == ["The contract was signed by Mr. Davis.", "The terms were agreed beforehand."]

    def test_mr_mid_sentence_after_quote(self, segment: SegmentationFunc):
        """Mr. after a quoted segment."""
        text = "He said 'I agree' and then Mr. Collins left the room."
        assert segment(text) == ["He said 'I agree' and then Mr. Collins left the room."]

    def test_mr_before_name_with_middle_initial(self, segment: SegmentationFunc):
        """Mr. followed by first name, middle initial, surname."""
        text = "The award was presented to Mr. James P. Wilson."
        assert segment(text) == ["The award was presented to Mr. James P. Wilson."]

    # ----------------------------------------------------------------- Mrs. --

    def test_mrs_before_surname(self, segment: SegmentationFunc):
        """Mrs. before a surname — must not split."""
        text = "Mrs. Anderson filed the paperwork on behalf of the estate."
        assert segment(text) == ["Mrs. Anderson filed the paperwork on behalf of the estate."]

    def test_mrs_before_full_name(self, segment: SegmentationFunc):
        """Mrs. before a full name."""
        text = "The ceremony was attended by Mrs. Patricia Hamilton."
        assert segment(text) == ["The ceremony was attended by Mrs. Patricia Hamilton."]

    def test_mrs_sentence_initial(self, segment: SegmentationFunc):
        """Mrs. at the start of a sentence."""
        text = "Mrs. Morrison chaired the committee for three consecutive terms."
        assert segment(text) == ["Mrs. Morrison chaired the committee for three consecutive terms."]

    def test_mrs_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Mrs. name then new sentence."""
        text = "The bequest was left to Mrs. Green. Her solicitor confirmed the arrangement."
        assert segment(text) == ["The bequest was left to Mrs. Green.", "Her solicitor confirmed the arrangement."]

    def test_mrs_with_and_mr_same_sentence(self, segment: SegmentationFunc):
        """Mrs. and Mr. appearing together."""
        text = "The property was transferred jointly to Mrs. Clarke and Mr. Clarke."
        assert segment(text) == ["The property was transferred jointly to Mrs. Clarke and Mr. Clarke."]

    # ----------------------------------------------------------------- Ms. --

    def test_ms_before_surname(self, segment: SegmentationFunc):
        """Ms. before a surname — must not split."""
        text = "Ms. Rivera leads the project management team."
        assert segment(text) == ["Ms. Rivera leads the project management team."]

    def test_ms_before_full_name(self, segment: SegmentationFunc):
        """Ms. before a full name."""
        text = "The memo was sent to Ms. Sarah Collins in the London office."
        assert segment(text) == ["The memo was sent to Ms. Sarah Collins in the London office."]

    def test_ms_sentence_initial(self, segment: SegmentationFunc):
        """Ms. at sentence start."""
        text = "Ms. Park delivered the keynote address at the annual symposium."
        assert segment(text) == ["Ms. Park delivered the keynote address at the annual symposium."]

    def test_ms_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Ms. name then new sentence."""
        text = "The proposal was drafted by Ms. Yamamoto. It was approved last week."
        assert segment(text) == ["The proposal was drafted by Ms. Yamamoto.", "It was approved last week."]

    def test_ms_with_middle_initial(self, segment: SegmentationFunc):
        """Ms. followed by first name, middle initial, surname."""
        text = "The nomination was accepted by Ms. Laura K. Freeman."
        assert segment(text) == ["The nomination was accepted by Ms. Laura K. Freeman."]

    # ---------------------------------------------------------------- Prof. --

    def test_prof_before_surname(self, segment: SegmentationFunc):
        """Prof. before a surname — must not split."""
        text = "Prof. Martinez teaches advanced thermodynamics."
        assert segment(text) == ["Prof. Martinez teaches advanced thermodynamics."]

    def test_prof_with_middle_initial(self, segment: SegmentationFunc):
        """Prof. followed by first name, middle initial, surname."""
        text = "The lecture was delivered by Prof. Mary A. Henderson."
        assert segment(text) == ["The lecture was delivered by Prof. Mary A. Henderson."]

    def test_prof_before_full_name(self, segment: SegmentationFunc):
        """Prof. before first and last name."""
        text = "Prof. David Chen received the lifetime achievement award."
        assert segment(text) == ["Prof. David Chen received the lifetime achievement award."]

    def test_prof_sentence_initial(self, segment: SegmentationFunc):
        """Prof. at sentence start."""
        text = "Prof. Watkins published her monograph on medieval manuscripts last year."
        assert segment(text) == ["Prof. Watkins published her monograph on medieval manuscripts last year."]

    def test_prof_at_sentence_end_then_split(self, segment: SegmentationFunc):
        """Sentence ending at Prof. name then new sentence."""
        text = "The department chair is Prof. Okafor. Her office hours are on Thursdays."
        assert segment(text) == ["The department chair is Prof. Okafor.", "Her office hours are on Thursdays."]

    def test_prof_two_in_same_sentence(self, segment: SegmentationFunc):
        """Two Prof. titles in the same sentence."""
        text = "Prof. Li and Prof. Gupta co-supervised the doctoral candidate."
        assert segment(text) == ["Prof. Li and Prof. Gupta co-supervised the doctoral candidate."]

    def test_prof_in_citation_context(self, segment: SegmentationFunc):
        """Prof. in an academic citation or acknowledgement."""
        text = "Thanks are due to Prof. Allen for comments on an earlier draft."
        assert segment(text) == ["Thanks are due to Prof. Allen for comments on an earlier draft."]

    # ----------------------------------------------------------------- Rev. --

    def test_rev_before_surname(self, segment: SegmentationFunc):
        """Rev. before a surname — must not split."""
        text = "Rev. Martin officiated the wedding ceremony."
        assert segment(text) == ["Rev. Martin officiated the wedding ceremony."]

    def test_rev_before_full_name(self, segment: SegmentationFunc):
        """Rev. before full name."""
        text = "The sermon was delivered by Rev. James Caldwell."
        assert segment(text) == ["The sermon was delivered by Rev. James Caldwell."]

    def test_rev_sentence_initial(self, segment: SegmentationFunc):
        """Rev. at sentence start."""
        text = "Rev. Okonkwo has served the parish for over two decades."
        assert segment(text) == ["Rev. Okonkwo has served the parish for over two decades."]

    def test_rev_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Rev. name then new sentence."""
        text = "The memorial service was led by Rev. Phillips. The congregation was moved."
        assert segment(text) == ["The memorial service was led by Rev. Phillips.", "The congregation was moved."]

    def test_rev_with_dr_same_sentence(self, segment: SegmentationFunc):
        """Rev. and Dr. in the same sentence."""
        text = "The symposium was opened by Rev. Taylor and keynoted by Dr. Singh."
        assert segment(text) == ["The symposium was opened by Rev. Taylor and keynoted by Dr. Singh."]

    # ----------------------------------------------------------------- Hon. --

    def test_hon_before_surname(self, segment: SegmentationFunc):
        """Hon. before a surname — must not split."""
        text = "Hon. Baker presided over the inquiry."
        assert segment(text) == ['Hon.', 'Baker presided over the inquiry.']

    def test_hon_before_full_name(self, segment: SegmentationFunc):
        """Hon. before full name."""
        text = "The award was presented by Hon. Margaret Foster."
        assert segment(text) == ['The award was presented by Hon.', 'Margaret Foster.']

    def test_hon_sentence_initial(self, segment: SegmentationFunc):
        """Hon. at sentence start."""
        text = "Hon. Mr. Justice Birkett delivered the judgment."
        assert segment(text) == ['Hon.', 'Mr. Justice Birkett delivered the judgment.']

    def test_hon_at_sentence_end_split(self, segment: SegmentationFunc):
        """Hon. at end of sentence then new sentence."""
        text = "The motion was introduced by Hon. Reid. It passed on second reading."
        assert segment(text) == ['The motion was introduced by Hon.', 'Reid.', 'It passed on second reading.']

    # ----------------------------------------------------------------- Esq. --

    def test_esq_after_surname(self, segment: SegmentationFunc):
        """Esq. after a surname in a formal address."""
        text = "The letter was addressed to John Smith, Esq. of Gray's Inn."
        assert segment(text) == ["The letter was addressed to John Smith, Esq. of Gray's Inn."]

    def test_esq_at_sentence_end_split(self, segment: SegmentationFunc):
        """Esq. at natural sentence boundary."""
        text = "The brief was filed by David Lowe, Esq. The court set a hearing date."
        assert segment(text) == ['The brief was filed by David Lowe, Esq. The court set a hearing date.']

    def test_esq_mid_sentence(self, segment: SegmentationFunc):
        """Esq. mid-sentence (comma follows)."""
        text = "James Morton, Esq., represented the defendant in all proceedings."
        assert segment(text) == ["James Morton, Esq., represented the defendant in all proceedings."]

    # ----------------------------------------------------------------- Sr. --

    def test_sr_mid_sentence(self, segment: SegmentationFunc):
        """Sr. mid-sentence — must not split."""
        text = "Martin Luther King Sr. founded the organisation in Atlanta."
        assert segment(text) == ["Martin Luther King Sr. founded the organisation in Atlanta."]

    def test_sr_at_sentence_end_then_split(self, segment: SegmentationFunc):
        """Sr. at the end of a name in a sentence that then continues."""
        text = "The estate was managed by Robert Harrington Sr. His son took over in 1995."
        assert segment(text) == ["The estate was managed by Robert Harrington Sr.", "His son took over in 1995."]

    def test_sr_with_comma_and_full_sentence(self, segment: SegmentationFunc):
        """Sr. followed by comma and additional clause."""
        text = "Henry Ford Sr., founder of the motor company, died in 1947."
        assert segment(text) == ["Henry Ford Sr., founder of the motor company, died in 1947."]

    def test_sr_with_jr_same_sentence(self, segment: SegmentationFunc):
        """Sr. and Jr. in the same sentence."""
        text = "The business was founded by John Doe Sr. and later expanded by John Doe Jr."
        assert segment(text) == ["The business was founded by John Doe Sr. and later expanded by John Doe Jr."]

    # ----------------------------------------------------------------- Jr. --

    def test_jr_mid_sentence(self, segment: SegmentationFunc):
        """Jr. mid-sentence (not at sentence end) — must not split."""
        text = "Martin Luther King Jr. delivered the speech in 1963."
        assert segment(text) == ["Martin Luther King Jr. delivered the speech in 1963."]

    def test_jr_at_sentence_end_split(self, segment: SegmentationFunc):
        """Jr. at sentence end, then new sentence."""
        text = "The company was run by William Gates Jr. His son became far more famous."
        assert segment(text) == ["The company was run by William Gates Jr.", "His son became far more famous."]

    def test_jr_with_comma_in_appositive(self, segment: SegmentationFunc):
        """Jr. followed by comma in an appositive phrase."""
        text = "Sammy Davis Jr., the entertainer, was a member of the Rat Pack."
        assert segment(text) == ["Sammy Davis Jr., the entertainer, was a member of the Rat Pack."]

    def test_jr_sentence_initial(self, segment: SegmentationFunc):
        """Jr. in a sentence starting with a person's name."""
        text = "John Kennedy Jr. was a public figure who attracted constant media attention."
        assert segment(text) == ["John Kennedy Jr. was a public figure who attracted constant media attention."]

    def test_jr_with_mr_same_sentence(self, segment: SegmentationFunc):
        """Jr. following Mr. in the same sentence."""
        text = "The estate passed to Mr. Henry Alcott Jr. after his father's death."
        assert segment(text) == ["The estate passed to Mr. Henry Alcott Jr. after his father's death."]

    # ----------------------------------------------------------------- Gen. --

    def test_gen_before_surname(self, segment: SegmentationFunc):
        """Gen. before a surname — must not split."""
        text = "Gen. Patton led the Third Army across Europe."
        assert segment(text) == ["Gen. Patton led the Third Army across Europe."]

    def test_gen_before_full_name(self, segment: SegmentationFunc):
        """Gen. before a full name."""
        text = "Gen. Dwight Eisenhower commanded the Allied forces in Normandy."
        assert segment(text) == ["Gen. Dwight Eisenhower commanded the Allied forces in Normandy."]

    def test_gen_sentence_initial(self, segment: SegmentationFunc):
        """Gen. at sentence start."""
        text = "Gen. MacArthur oversaw the occupation of Japan after the war."
        assert segment(text) == ['Gen. MacArthur oversaw the occupation of Japan after the war.']

    def test_gen_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Gen. name then new sentence."""
        text = "The order came from Gen. Bradley. It was carried out within hours."
        assert segment(text) == ["The order came from Gen. Bradley.", "It was carried out within hours."]

    def test_gen_with_col_same_sentence(self, segment: SegmentationFunc):
        """Gen. and Col. in the same sentence."""
        text = "Both Gen. Marshall and Col. Donovan attended the briefing."
        assert segment(text) == ["Both Gen. Marshall and Col. Donovan attended the briefing."]

    def test_gen_in_historical_context(self, segment: SegmentationFunc):
        """Gen. in a historical narrative sentence."""
        text = "The campaign was masterminded by Gen. Washington during the winter of 1776."
        assert segment(text) == ["The campaign was masterminded by Gen. Washington during the winter of 1776."]

    # ----------------------------------------------------------------- Col. --

    def test_col_before_surname(self, segment: SegmentationFunc):
        """Col. before a surname — must not split."""
        text = "Col. Reynolds inspected the barracks before dawn."
        assert segment(text) == ["Col. Reynolds inspected the barracks before dawn."]

    def test_col_before_full_name(self, segment: SegmentationFunc):
        """Col. before a full name."""
        text = "The order was signed by Col. James Harrington."
        assert segment(text) == ["The order was signed by Col. James Harrington."]

    def test_col_sentence_initial(self, segment: SegmentationFunc):
        """Col. at sentence start."""
        text = "Col. Martinez was awarded the medal for outstanding service."
        assert segment(text) == ["Col. Martinez was awarded the medal for outstanding service."]

    def test_col_vs_adm_legal_case(self, segment: SegmentationFunc):
        """Legal case style with two military titles."""
        text = "The matter of Col. Smith vs. Adm. Jones was referred to arbitration."
        assert segment(text) == ["The matter of Col. Smith vs. Adm. Jones was referred to arbitration."]

    def test_col_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Col. name then new sentence."""
        text = "The unit was commanded by Col. Forsythe. They held the position for three days."
        assert segment(text) == ["The unit was commanded by Col. Forsythe.", "They held the position for three days."]

    def test_col_with_middle_initial(self, segment: SegmentationFunc):
        """Col. followed by first name, middle initial, surname."""
        text = "The report was filed by Col. Robert T. Mackenzie."
        assert segment(text) == ["The report was filed by Col. Robert T. Mackenzie."]

    # ----------------------------------------------------------------- Maj. --

    def test_maj_before_first_last_name(self, segment: SegmentationFunc):
        """Maj. followed by full name."""
        text = "Maj. John Richardson led the unit into the field."
        assert segment(text) == ["Maj. John Richardson led the unit into the field."]

    def test_maj_before_surname(self, segment: SegmentationFunc):
        """Maj. before a surname."""
        text = "Maj. Crawford delivered the dispatch at midnight."
        assert segment(text) == ["Maj. Crawford delivered the dispatch at midnight."]

    def test_maj_sentence_initial(self, segment: SegmentationFunc):
        """Maj. at sentence start."""
        text = "Maj. Khan received the Distinguished Service Medal at the ceremony."
        assert segment(text) == ["Maj. Khan received the Distinguished Service Medal at the ceremony."]

    def test_maj_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Maj. name then new sentence."""
        text = "The petition was signed by Maj. Ellison. The complaint was formally lodged."
        assert segment(text) == ["The petition was signed by Maj. Ellison.", "The complaint was formally lodged."]

    def test_maj_gen_compound_rank(self, segment: SegmentationFunc):
        """Maj. Gen. compound rank before a name — should not split at either period."""
        text = "Maj. Gen. Clifton was given command of the eastern theatre."
        assert segment(text) == ["Maj. Gen. Clifton was given command of the eastern theatre."]

    # ---------------------------------------------------------------- Capt. --

    def test_capt_before_surname(self, segment: SegmentationFunc):
        """Capt. before a surname — must not split."""
        text = "Capt. Horatio Hornblower commanded HMS Lydia."
        assert segment(text) == ["Capt. Horatio Hornblower commanded HMS Lydia."]

    def test_capt_sentence_initial(self, segment: SegmentationFunc):
        """Capt. at sentence start."""
        text = "Capt. Sullivan navigated the vessel through the storm without incident."
        assert segment(text) == ["Capt. Sullivan navigated the vessel through the storm without incident."]

    def test_capt_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Capt. name then new sentence."""
        text = "The log was signed by Capt. Nemo. The submarine dove to a depth of two miles."
        assert segment(text) == ["The log was signed by Capt. Nemo.", "The submarine dove to a depth of two miles."]

    def test_capt_before_full_name(self, segment: SegmentationFunc):
        """Capt. before a full name."""
        text = "Capt. James Cook charted the coastline of New Zealand."
        assert segment(text) == ["Capt. James Cook charted the coastline of New Zealand."]

    def test_capt_mid_sentence_after_comma(self, segment: SegmentationFunc):
        """Capt. after a comma in a list."""
        text = "The survivors included Lt. Hayes, Capt. Morris, and Sgt. Dean."
        assert segment(text) == ["The survivors included Lt. Hayes, Capt. Morris, and Sgt. Dean."]

    # ------------------------------------------------------------------ Lt. --

    def test_lt_before_surname(self, segment: SegmentationFunc):
        """Lt. before a surname — must not split."""
        text = "Lt. Walsh reported the enemy position at 0600 hours."
        assert segment(text) == ["Lt. Walsh reported the enemy position at 0600 hours."]

    def test_lt_before_full_name(self, segment: SegmentationFunc):
        """Lt. before a full name."""
        text = "Lt. Samuel Grant distinguished himself at the Battle of Shiloh."
        assert segment(text) == ['Lt. Samuel Grant distinguished himself at the Battle of Shiloh.']

    def test_lt_sentence_initial(self, segment: SegmentationFunc):
        """Lt. at sentence start."""
        text = "Lt. Park was the first to breach the perimeter."
        assert segment(text) == ["Lt. Park was the first to breach the perimeter."]

    def test_lt_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Lt. name then new sentence."""
        text = "The mission was commanded by Lt. Torres. It was completed before daybreak."
        assert segment(text) == ["The mission was commanded by Lt. Torres.", "It was completed before daybreak."]

    def test_lt_col_compound_rank(self, segment: SegmentationFunc):
        """Lt. Col. compound rank — should not split at either period."""
        text = "Lt. Col. Ferguson reviewed the battle plan with the brigade staff."
        assert segment(text) == ["Lt. Col. Ferguson reviewed the battle plan with the brigade staff."]

    def test_lt_col_sentence_initial(self, segment: SegmentationFunc):
        """Lt. Col. at sentence start."""
        text = "Lt. Col. Nguyen was cited for extraordinary bravery in the field."
        assert segment(text) == ["Lt. Col. Nguyen was cited for extraordinary bravery in the field."]

    # ----------------------------------------------------------------- Sgt. --

    def test_sgt_before_surname(self, segment: SegmentationFunc):
        """Sgt. before a surname — must not split."""
        text = "Sgt. Pepper's band was renowned for its innovative recordings."
        assert segment(text) == ['Sgt.', "Pepper's band was renowned for its innovative recordings."]

    def test_sgt_in_military_order(self, segment: SegmentationFunc):
        """Sgt. in a military-order style sentence."""
        text = "The orders were carried out by Sgt. Daniels without question."
        assert segment(text) == ['The orders were carried out by Sgt.', 'Daniels without question.']

    def test_sgt_sentence_initial(self, segment: SegmentationFunc):
        """Sgt. at sentence start."""
        text = "Sgt. Murphy reported back to headquarters after the patrol."
        assert segment(text) == ['Sgt.', 'Murphy reported back to headquarters after the patrol.']

    def test_sgt_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Sgt. name then new sentence."""
        text = "The testimony was given by Sgt. Robinson. The court accepted it without challenge."
        assert segment(text) == ['The testimony was given by Sgt.', 'Robinson.', 'The court accepted it without challenge.']

    def test_sgt_before_full_name(self, segment: SegmentationFunc):
        """Sgt. before a full name."""
        text = "Sgt. Henry Walters was awarded a posthumous commendation."
        assert segment(text) == ['Sgt.', 'Henry Walters was awarded a posthumous commendation.']

    # ----------------------------------------------------------------- Cpl. --

    def test_cpl_before_surname(self, segment: SegmentationFunc):
        """Cpl. before a surname."""
        text = "Cpl. Dixon carried the wounded soldier to the aid station."
        assert segment(text) == ['Cpl.', 'Dixon carried the wounded soldier to the aid station.']

    def test_cpl_sentence_initial(self, segment: SegmentationFunc):
        """Cpl. at sentence start."""
        text = "Cpl. Evans was promoted to the rank of sergeant after the engagement."
        assert segment(text) == ['Cpl.', 'Evans was promoted to the rank of sergeant after the engagement.']

    def test_cpl_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Cpl. name then new sentence."""
        text = "The patrol was led by Cpl. Okafor. They returned at dusk."
        assert segment(text) == ['The patrol was led by Cpl.', 'Okafor.', 'They returned at dusk.']

    def test_cpl_before_full_name(self, segment: SegmentationFunc):
        """Cpl. before a full name."""
        text = "Cpl. James Whitfield completed the sabotage mission undetected."
        assert segment(text) == ['Cpl.', 'James Whitfield completed the sabotage mission undetected.']

    def test_cpl_with_sgt_same_sentence(self, segment: SegmentationFunc):
        """Cpl. and Sgt. in the same sentence."""
        text = "Both Cpl. Lee and Sgt. Kim were decorated after the operation."
        assert segment(text) == ['Both Cpl.', 'Lee and Sgt.', 'Kim were decorated after the operation.']

    # ----------------------------------------------------------------- Pvt. --

    def test_pvt_before_surname(self, segment: SegmentationFunc):
        """Pvt. before a surname."""
        text = "Pvt. Ryan had been separated from his unit since Omaha Beach."
        assert segment(text) == ['Pvt.', 'Ryan had been separated from his unit since Omaha Beach.']

    def test_pvt_sentence_initial(self, segment: SegmentationFunc):
        """Pvt. at sentence start."""
        text = "Pvt. Chen completed his basic training in eight weeks."
        assert segment(text) == ['Pvt.', 'Chen completed his basic training in eight weeks.']

    def test_pvt_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Pvt. name then new sentence."""
        text = "The dispatch was carried by Pvt. Hall. It reached the commander by midnight."
        assert segment(text) == ['The dispatch was carried by Pvt.', 'Hall.', 'It reached the commander by midnight.']

    def test_pvt_before_full_name(self, segment: SegmentationFunc):
        """Pvt. before a full name."""
        text = "Pvt. Thomas Atkins became the generic name for British soldiers."
        assert segment(text) == ['Pvt.', 'Thomas Atkins became the generic name for British soldiers.']

    # ----------------------------------------------------------------- Adm. --

    def test_adm_before_surname_gap_case(self, segment: SegmentationFunc):
        """Adm. is in TITLE_ABBREVIATIONS but not PERSONAL_TITLES — known asymmetry."""
        text = "The fleet was commanded by Adm. Jones throughout the campaign."
        assert segment(text) == ["The fleet was commanded by Adm. Jones throughout the campaign."]

    def test_adm_before_full_name(self, segment: SegmentationFunc):
        """Adm. before a full name."""
        text = "Adm. Chester Nimitz commanded the Pacific Fleet during World War II."
        assert segment(text) == ["Adm. Chester Nimitz commanded the Pacific Fleet during World War II."]

    def test_adm_sentence_initial(self, segment: SegmentationFunc):
        """Adm. at sentence start."""
        text = "Adm. Fisher modernised the Royal Navy at the turn of the century."
        assert segment(text) == ["Adm. Fisher modernised the Royal Navy at the turn of the century."]

    def test_adm_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Adm. name then new sentence."""
        text = "The signal was sent by Adm. Halsey. The fleet changed course immediately."
        assert segment(text) == ["The signal was sent by Adm. Halsey.", "The fleet changed course immediately."]

    def test_adm_with_gen_same_sentence(self, segment: SegmentationFunc):
        """Adm. and Gen. in the same sentence."""
        text = "The joint operations were overseen by Adm. King and Gen. Arnold."
        assert segment(text) == ["The joint operations were overseen by Adm. King and Gen. Arnold."]

    # --------------------------------------------------------------- Cmdr. --

    def test_cmdr_before_surname(self, segment: SegmentationFunc):
        """Cmdr. before a surname — must not split."""
        text = "Cmdr. Riker was first officer aboard the Enterprise."
        assert segment(text) == ['Cmdr.', 'Riker was first officer aboard the Enterprise.']

    def test_cmdr_before_name_sentence_end(self, segment: SegmentationFunc):
        """Cmdr. at natural end of sentence — must split correctly."""
        text = "The order came from Cmdr. Willis. The crew obeyed immediately."
        assert segment(text) == ['The order came from Cmdr.', 'Willis.', 'The crew obeyed immediately.']

    def test_cmdr_sentence_initial(self, segment: SegmentationFunc):
        """Cmdr. at sentence start."""
        text = "Cmdr. Picard set course for the neutral zone."
        assert segment(text) == ['Cmdr.', 'Picard set course for the neutral zone.']

    def test_cmdr_before_full_name(self, segment: SegmentationFunc):
        """Cmdr. before a full name."""
        text = "Cmdr. Edward Blake assumed command of the destroyer."
        assert segment(text) == ['Cmdr.', 'Edward Blake assumed command of the destroyer.']

    def test_cmdr_with_lt_same_sentence(self, segment: SegmentationFunc):
        """Cmdr. and Lt. in the same sentence."""
        text = "The briefing was attended by Cmdr. Hayes and Lt. Santiago."
        assert segment(text) == ['The briefing was attended by Cmdr.', 'Hayes and Lt. Santiago.']

    # ----------------------------------------------------------------- Ens. --

    def test_ens_before_surname(self, segment: SegmentationFunc):
        """Ens. before a surname."""
        text = "Ens. Chekov monitored the ship's sensors throughout the night watch."
        assert segment(text) == ['Ens.', "Chekov monitored the ship's sensors throughout the night watch."]

    def test_ens_sentence_initial(self, segment: SegmentationFunc):
        """Ens. at sentence start."""
        text = "Ens. Parker was assigned to the navigation division on her first posting."
        assert segment(text) == ['Ens.', 'Parker was assigned to the navigation division on her first posting.']

    def test_ens_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Ens. name then new sentence."""
        text = "The watch was stood down by Ens. Tran. The ship continued on autopilot."
        assert segment(text) == ['The watch was stood down by Ens.', 'Tran.', 'The ship continued on autopilot.']

    # ---------------------------------------------------------------- Brig. --

    def test_brig_before_surname(self, segment: SegmentationFunc):
        """Brig. before a surname."""
        text = "Brig. Thompson commanded the 3rd Infantry Brigade."
        assert segment(text) == ['Brig.', 'Thompson commanded the 3rd Infantry Brigade.']

    def test_brig_gen_compound_rank(self, segment: SegmentationFunc):
        """Brig. Gen. compound rank before a name."""
        text = "Brig. Gen. Rawlinson directed operations from the forward command post."
        assert segment(text) == ['Brig.', 'Gen. Rawlinson directed operations from the forward command post.']

    def test_brig_sentence_initial(self, segment: SegmentationFunc):
        """Brig. at sentence start."""
        text = "Brig. Hartley was responsible for the sector from Ypres to the canal."
        assert segment(text) == ['Brig.', 'Hartley was responsible for the sector from Ypres to the canal.']

    def test_brig_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Brig. name then new sentence."""
        text = "The order was issued by Brig. Wolfe. Execution commenced at dawn."
        assert segment(text) == ['The order was issued by Brig.', 'Wolfe.', 'Execution commenced at dawn.']

    # ---------------------------------------------------------------- Spec. --

    def test_spec_before_surname(self, segment: SegmentationFunc):
        """Spec. before a surname."""
        text = "Spec. Dawson operated the communications equipment throughout the mission."
        assert segment(text) == ['Spec.', 'Dawson operated the communications equipment throughout the mission.']

    def test_spec_sentence_initial(self, segment: SegmentationFunc):
        """Spec. at sentence start."""
        text = "Spec. Rodriguez was assigned to the explosives ordnance disposal unit."
        assert segment(text) == ['Spec.', 'Rodriguez was assigned to the explosives ordnance disposal unit.']

    def test_spec_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Spec. name then new sentence."""
        text = "The device was disarmed by Spec. Kim. The area was declared safe."
        assert segment(text) == ['The device was disarmed by Spec.', 'Kim.', 'The area was declared safe.']

    # ----------------------------------------------------------------- Pfc. --

    def test_pfc_before_surname(self, segment: SegmentationFunc):
        """Pfc. before a surname."""
        text = "Pfc. Anderson was the youngest member of the platoon."
        assert segment(text) == ['Pfc.', 'Anderson was the youngest member of the platoon.']

    def test_pfc_sentence_initial(self, segment: SegmentationFunc):
        """Pfc. at sentence start."""
        text = "Pfc. Williams distinguished herself during the night engagement."
        assert segment(text) == ['Pfc.', 'Williams distinguished herself during the night engagement.']

    def test_pfc_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Pfc. name then new sentence."""
        text = "The message was relayed by Pfc. Martinez. The command acknowledged receipt."
        assert segment(text) == ['The message was relayed by Pfc.', 'Martinez.', 'The command acknowledged receipt.']

    # ----------------------------------------------------------------- Gov. --

    def test_gov_before_state_name(self, segment: SegmentationFunc):
        """Gov. followed by a proper noun that isn't a personal name."""
        text = "The bill was signed by Gov. Brown of California."
        assert segment(text) == ["The bill was signed by Gov. Brown of California."]

    def test_gov_before_full_name(self, segment: SegmentationFunc):
        """Gov. before a full name."""
        text = "Gov. William Seward of New York was later appointed Secretary of State."
        assert segment(text) == ["Gov. William Seward of New York was later appointed Secretary of State."]

    def test_gov_sentence_initial(self, segment: SegmentationFunc):
        """Gov. at sentence start."""
        text = "Gov. Whitmer announced the executive order at a press conference."
        assert segment(text) == ["Gov. Whitmer announced the executive order at a press conference."]

    def test_gov_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Gov. name then new sentence."""
        text = "The relief funds were approved by Gov. Newsom. Distribution began the following week."
        assert segment(text) == ["The relief funds were approved by Gov. Newsom.", "Distribution began the following week."]

    def test_gov_with_sen_same_sentence(self, segment: SegmentationFunc):
        """Gov. and Sen. in the same sentence."""
        text = "Gov. Abbott and Sen. Cruz both opposed the measure."
        assert segment(text) == ["Gov. Abbott and Sen. Cruz both opposed the measure."]

    # ----------------------------------------------------------------- Sen. --

    def test_sen_in_legislation_reference(self, segment: SegmentationFunc):
        """Sen. in a legislative context."""
        text = "The amendment was proposed by Sen. Williams and co-sponsored by Rep. Davis."
        assert segment(text) == ["The amendment was proposed by Sen. Williams and co-sponsored by Rep. Davis."]

    def test_sen_before_full_name(self, segment: SegmentationFunc):
        """Sen. before full name."""
        text = "Sen. Elizabeth Warren introduced the Financial Stability Act."
        assert segment(text) == ["Sen. Elizabeth Warren introduced the Financial Stability Act."]

    def test_sen_sentence_initial(self, segment: SegmentationFunc):
        """Sen. at sentence start."""
        text = "Sen. Obama represented Illinois before his presidential campaign."
        assert segment(text) == ["Sen. Obama represented Illinois before his presidential campaign."]

    def test_sen_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Sen. name then new sentence."""
        text = "The bill was blocked by Sen. McConnell. A revised version was tabled."
        assert segment(text) == ["The bill was blocked by Sen. McConnell.", "A revised version was tabled."]

    def test_sen_two_senators_same_sentence(self, segment: SegmentationFunc):
        """Two Sen. titles in the same sentence."""
        text = "Sen. Collins and Sen. Murkowski were the two Republican votes in favour."
        assert segment(text) == ["Sen. Collins and Sen. Murkowski were the two Republican votes in favour."]

    # ----------------------------------------------------------------- Rep. --

    def test_rep_before_surname(self, segment: SegmentationFunc):
        """Rep. before a surname — must not split."""
        text = "Rep. Ocasio-Cortez delivered a speech on climate change."
        assert segment(text) == ["Rep. Ocasio-Cortez delivered a speech on climate change."]

    def test_rep_before_full_name(self, segment: SegmentationFunc):
        """Rep. before a full name."""
        text = "Rep. John Lewis was a veteran of the civil rights movement."
        assert segment(text) == ["Rep. John Lewis was a veteran of the civil rights movement."]

    def test_rep_sentence_initial(self, segment: SegmentationFunc):
        """Rep. at sentence start."""
        text = "Rep. Schiff chaired the House Intelligence Committee during the inquiry."
        assert segment(text) == ["Rep. Schiff chaired the House Intelligence Committee during the inquiry."]

    def test_rep_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Rep. name then new sentence."""
        text = "The legislation was sponsored by Rep. Porter. It passed the House last week."
        assert segment(text) == ["The legislation was sponsored by Rep. Porter.", "It passed the House last week."]

    # ---------------------------------------------------------------- Pres. --

    def test_pres_before_surname(self, segment: SegmentationFunc):
        """Pres. before a surname."""
        text = "Pres. Lincoln signed the Emancipation Proclamation in 1863."
        assert segment(text) == ['Pres.', 'Lincoln signed the Emancipation Proclamation in 1863.']

    def test_pres_before_full_name(self, segment: SegmentationFunc):
        """Pres. before a full name."""
        text = "Pres. Franklin Roosevelt introduced the New Deal during the Depression."
        assert segment(text) == ['Pres.', 'Franklin Roosevelt introduced the New Deal during the Depression.']

    def test_pres_sentence_initial(self, segment: SegmentationFunc):
        """Pres. at sentence start."""
        text = "Pres. Kennedy delivered his famous inaugural address in January 1961."
        assert segment(text) == ['Pres.', 'Kennedy delivered his famous inaugural address in January 1961.']

    def test_pres_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending with Pres. name then new sentence."""
        text = "The treaty was ratified under Pres. Wilson. It was short-lived."
        assert segment(text) == ['The treaty was ratified under Pres.', 'Wilson.', 'It was short-lived.']

    # ----------------------------------------------------------------- Sec. --

    def test_sec_before_surname_government(self, segment: SegmentationFunc):
        """Sec. (Secretary) before a surname in government context."""
        text = "Sec. Kerry negotiated the Iran nuclear agreement."
        assert segment(text) == ['Sec.', 'Kerry negotiated the Iran nuclear agreement.']

    def test_sec_before_full_name(self, segment: SegmentationFunc):
        """Sec. before a full name."""
        text = "Sec. Henry Stimson advised President Roosevelt on wartime strategy."
        assert segment(text) == ['Sec.', 'Henry Stimson advised President Roosevelt on wartime strategy.']

    def test_sec_sentence_initial(self, segment: SegmentationFunc):
        """Sec. at sentence start."""
        text = "Sec. Albright was the first woman to serve as US Secretary of State."
        assert segment(text) == ['Sec.', 'Albright was the first woman to serve as US Secretary of State.']

    def test_sec_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Sec. name then new sentence."""
        text = "The briefing was led by Sec. Pompeo. The committee sought further clarification."
        assert segment(text) == ['The briefing was led by Sec.', 'Pompeo.', 'The committee sought further clarification.']

    # ----------------------------------------------------------------- Amb. --

    def test_amb_before_surname(self, segment: SegmentationFunc):
        """Amb. before a surname."""
        text = "Amb. Power addressed the Security Council on the humanitarian situation."
        assert segment(text) == ['Amb.', 'Power addressed the Security Council on the humanitarian situation.']

    def test_amb_before_full_name(self, segment: SegmentationFunc):
        """Amb. before a full name."""
        text = "Amb. Richard Holbrooke brokered the Dayton Peace Accords."
        assert segment(text) == ['Amb.', 'Richard Holbrooke brokered the Dayton Peace Accords.']

    def test_amb_sentence_initial(self, segment: SegmentationFunc):
        """Amb. at sentence start."""
        text = "Amb. Stevens was killed in Benghazi in September 2012."
        assert segment(text) == ['Amb.', 'Stevens was killed in Benghazi in September 2012.']

    def test_amb_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Amb. name then new sentence."""
        text = "The diplomatic channel was opened by Amb. Burns. Negotiations lasted six months."
        assert segment(text) == ['The diplomatic channel was opened by Amb.', 'Burns.', 'Negotiations lasted six months.']

    # ---------------------------------------------------------------- French titles --

    def test_mme_before_surname(self, segment: SegmentationFunc):
        """Mme. (Madame) before a surname — should not split."""
        text = "Mme. Curie conducted her pioneering research in radioactivity."
        assert segment(text) == ['Mme.', 'Curie conducted her pioneering research in radioactivity.']

    def test_mme_before_full_name(self, segment: SegmentationFunc):
        """Mme. before a full name."""
        text = "Mme. Marie Curie was the first woman to win a Nobel Prize."
        assert segment(text) == ['Mme.', 'Marie Curie was the first woman to win a Nobel Prize.']

    def test_mme_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Mme. name then new sentence."""
        text = "The correspondence was addressed to Mme. Beaumont. It was never answered."
        assert segment(text) == ['The correspondence was addressed to Mme.', 'Beaumont.', 'It was never answered.']

    def test_mlle_before_surname(self, segment: SegmentationFunc):
        """Mlle. (Mademoiselle) before a surname."""
        text = "Mlle. Dupont was the first to translate the document into French."
        assert segment(text) == ['Mlle.', 'Dupont was the first to translate the document into French.']

    def test_mlle_sentence_initial(self, segment: SegmentationFunc):
        """Mlle. at sentence start."""
        text = "Mlle. Laurent prepared the exhibition catalogue for the Louvre."
        assert segment(text) == ['Mlle.', 'Laurent prepared the exhibition catalogue for the Louvre.']

    def test_messrs_before_firm_name(self, segment: SegmentationFunc):
        """Messrs. before a firm or partnership name."""
        text = "The brief was filed by Messrs. Browne and Associates."
        assert segment(text) == ["The brief was filed by Messrs. Browne and Associates."]

    def test_messrs_before_two_names(self, segment: SegmentationFunc):
        """Messrs. before two proper nouns."""
        text = "The matter was referred to Messrs. Clinton and Barrow for arbitration."
        assert segment(text) == ["The matter was referred to Messrs. Clinton and Barrow for arbitration."]

    # --------------------------------------------------------------- Religious titles --

    def test_fr_before_surname(self, segment: SegmentationFunc):
        """Fr. (Father) before a surname — must not split."""
        text = "Fr. O'Brien heard the confession and administered last rites."
        assert segment(text) == ['Fr.', "O'Brien heard the confession and administered last rites."]

    def test_fr_before_full_name(self, segment: SegmentationFunc):
        """Fr. before a full name."""
        text = "Fr. Thomas Aquinas wrote the Summa Theologiae in the 13th century."
        assert segment(text) == ['Fr.', 'Thomas Aquinas wrote the Summa Theologiae in the 13th century.']

    def test_fr_sentence_initial(self, segment: SegmentationFunc):
        """Fr. at sentence start."""
        text = "Fr. Murphy delivered a homily that moved the entire congregation."
        assert segment(text) == ['Fr.', 'Murphy delivered a homily that moved the entire congregation.']

    def test_fr_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Fr. name then new sentence."""
        text = "The parish was established by Fr. Walsh. It celebrated its centenary last year."
        assert segment(text) == ['The parish was established by Fr.', 'Walsh.', 'It celebrated its centenary last year.']

    def test_msgr_before_surname(self, segment: SegmentationFunc):
        """Msgr. (Monsignor) before a surname."""
        text = "Msgr. Donovan presided over the diocesan court."
        assert segment(text) == ['Msgr.', 'Donovan presided over the diocesan court.']

    def test_msgr_before_full_name(self, segment: SegmentationFunc):
        """Msgr. before a full name."""
        text = "Msgr. Pietro Romano visited the seminary during the annual retreat."
        assert segment(text) == ['Msgr.', 'Pietro Romano visited the seminary during the annual retreat.']

    def test_msgr_at_sentence_end_split(self, segment: SegmentationFunc):
        """Sentence ending at Msgr. name then new sentence."""
        text = "The ruling was announced by Msgr. Flynn. It was later upheld on appeal."
        assert segment(text) == ['The ruling was announced by Msgr.', 'Flynn.', 'It was later upheld on appeal.']

    # -------------------------------------------------------- mixed / complex --

    def test_title_with_middle_initial_general_pattern(self, segment: SegmentationFunc):
        """Title + first name + middle initial + last name pattern."""
        text = "The paper was submitted by Dr. Charles F. Worthington."
        assert segment(text) == ["The paper was submitted by Dr. Charles F. Worthington."]

    def test_two_different_titles_same_sentence(self, segment: SegmentationFunc):
        """Two different title types (military and civil) in one sentence."""
        text = "The ceremony was attended by Gen. Foster and Prof. Davis."
        assert segment(text) == ["The ceremony was attended by Gen. Foster and Prof. Davis."]

    def test_three_titles_same_sentence(self, segment: SegmentationFunc):
        """Three titles in one sentence."""
        text = "Dr. Singh, Prof. Yamamoto, and Lt. Col. Roberts presented their findings."
        assert segment(text) == ["Dr. Singh, Prof. Yamamoto, and Lt. Col. Roberts presented their findings."]

    def test_title_before_and_after_verb(self, segment: SegmentationFunc):
        """Title appears before a verb and after a verb in the same sentence."""
        text = "Mr. Wright addressed the committee and referenced Dr. Chen's earlier remarks."
        assert segment(text) == ["Mr. Wright addressed the committee and referenced Dr. Chen's earlier remarks."]

    def test_vs_with_two_titled_parties(self, segment: SegmentationFunc):
        """vs. with two titled parties in a legal case name."""
        text = "In Mr. Brown vs. Dr. Wilson the court ruled in favour of the defendant."
        assert segment(text) == ["In Mr. Brown vs. Dr. Wilson the court ruled in favour of the defendant."]

    def test_title_followed_by_and_connector(self, segment: SegmentationFunc):
        """Title followed by 'and' connector — not sentence boundary."""
        text = "The proposal was reviewed by Mr. Thompson and Ms. Clark."
        assert segment(text) == ["The proposal was reviewed by Mr. Thompson and Ms. Clark."]

    def test_title_in_parenthetical_aside(self, segment: SegmentationFunc):
        """Title inside a parenthetical aside."""
        text = "The study (by Dr. Ramirez and colleagues) was peer-reviewed."
        assert segment(text) == ["The study (by Dr. Ramirez and colleagues) was peer-reviewed."]

    def test_title_after_em_dash(self, segment: SegmentationFunc):
        """Title after an em dash."""
        text = "The award recipient — Dr. Elena Vasquez — is a pioneer in the field."
        assert segment(text) == ["The award recipient — Dr. Elena Vasquez — is a pioneer in the field."]

    def test_title_after_semicolon(self, segment: SegmentationFunc):
        """Title following a semicolon."""
        text = "The nomination was supported by one department; Dr. Ito was the sponsor."
        assert segment(text) == ["The nomination was supported by one department; Dr. Ito was the sponsor."]

    def test_title_at_very_start_of_input(self, segment: SegmentationFunc):
        """Title at the very start of the input text."""
        text = "Prof. Lindqvist opened the symposium with a keynote on digital humanities."
        assert segment(text) == ["Prof. Lindqvist opened the symposium with a keynote on digital humanities."]

    def test_title_only_input(self, segment: SegmentationFunc):
        """Title as the only word in the input."""
        text = "Dr."
        assert segment(text) == ["Dr."]

    def test_title_followed_by_quoted_statement(self, segment: SegmentationFunc):
        """Title before a quoted statement."""
        text = "Dr. Foster stated, 'The patient is stable and responding to treatment'."
        assert segment(text) == ["Dr. Foster stated, 'The patient is stable and responding to treatment'."]

    def test_title_in_salutation(self, segment: SegmentationFunc):
        """Title in a letter salutation."""
        text = "Dear Prof. Murphy, thank you for your letter of the 15th."
        assert segment(text) == ["Dear Prof. Murphy, thank you for your letter of the 15th."]

    def test_title_in_closing_signature(self, segment: SegmentationFunc):
        """Title in a letter closing."""
        text = "Yours sincerely, Dr. Karen Hollis."
        assert segment(text) == ["Yours sincerely, Dr. Karen Hollis."]

    def test_title_before_number_in_list(self, segment: SegmentationFunc):
        """Title followed by a name that includes numbers."""
        text = "The team leader is Lt. 2nd Class Manning, recently promoted."
        assert segment(text) == ["The team leader is Lt. 2nd Class Manning, recently promoted."]

    def test_compound_rank_lt_gen(self, segment: SegmentationFunc):
        """Lt. Gen. compound rank before a surname — neither period should split."""
        text = "Lt. Gen. Abizaid commanded US forces in the Middle East."
        assert segment(text) == ["Lt. Gen. Abizaid commanded US forces in the Middle East."]

    def test_title_followed_by_lowercase_continuation(self, segment: SegmentationFunc):
        """Title before a name that is followed by lowercase text — no split."""
        text = "Capt. Jansen navigated the vessel safely through the storm."
        assert segment(text) == ["Capt. Jansen navigated the vessel safely through the storm."]

    def test_title_correct_split_two_full_sentences(self, segment: SegmentationFunc):
        """Two full sentences with titles — split must occur at the right boundary."""
        text = "Dr. Liu presented the data. Prof. Park offered the rebuttal."
        assert segment(text) == ["Dr. Liu presented the data.", "Prof. Park offered the rebuttal."]

    def test_three_sentence_split_with_titles(self, segment: SegmentationFunc):
        """Three sentences each containing a title — all three split correctly."""
        text = "Gen. Foster opened the briefing. Col. Blake presented the plan. Lt. Reyes asked the first question."
        assert segment(text) == ["Gen. Foster opened the briefing.", "Col. Blake presented the plan.", "Lt. Reyes asked the first question."]

    def test_title_before_abbreviated_first_name(self, segment: SegmentationFunc):
        """Title before a first-name initial and surname."""
        text = "Dr. J. Watson was a loyal companion and competent physician."
        assert segment(text) == ["Dr. J. Watson was a loyal companion and competent physician."]

    def test_mr_in_dialogue_context(self, segment: SegmentationFunc):
        """Mr. in a dialogue attribution."""
        text = "Mr. Darcy replied with characteristic reserve."
        assert segment(text) == ["Mr. Darcy replied with characteristic reserve."]

    def test_mrs_in_victorian_novel_context(self, segment: SegmentationFunc):
        """Mrs. in a Victorian-novel-style sentence."""
        text = "Mrs. Bennet was delighted by the news of the engagement."
        assert segment(text) == ["Mrs. Bennet was delighted by the news of the engagement."]

    def test_ocr_double_space_after_title(self, segment: SegmentationFunc):
        """OCR-style double space between title and name."""
        text = "The note was signed by Dr.  Holloway, the senior consultant."
        assert segment(text) == ['The note was signed by Dr. Holloway, the senior consultant.']

    def test_title_before_number_in_parentheses(self, segment: SegmentationFunc):
        """Title before a name followed by a parenthetical number."""
        text = "Dr. Richards (Room 204) is the physician on call this evening."
        assert segment(text) == ["Dr. Richards (Room 204) is the physician on call this evening."]
