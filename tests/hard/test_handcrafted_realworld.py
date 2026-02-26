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


class TestHandcraftedRealWorld:
    """Hand-crafted real-world mixed-domain tests for abbreviation suppression."""

    @pytest.fixture
    def segment(self):
        """Provide the segmentation function for tests."""
        from fast_sentence_segment import segment_text
        def _segment(text):
            return segment_text(text, flatten=True, split_dialog=False)
        return _segment

    # ------------------------------------------------ Canvas LMS patterns --

    def test_canvas_lms_week_reference_pattern_1(self, segment: SegmentationFunc):
        """Exact Canvas LMS cross-reference pattern from issue #47."""
        text = "Readings as listed on this overview page: cf. Week 1 Overview"
        assert segment(text) == ['Readings as listed on this overview page: cf. Week 1 Overview.']

    def test_canvas_lms_week_reference_pattern_2(self, segment: SegmentationFunc):
        """cf. Week N at end of a longer Canvas instruction sentence."""
        text = "Please review the supplementary readings before the session: cf. Week 3 Overview for context."
        assert segment(text) == ["Please review the supplementary readings before the session: cf. Week 3 Overview for context."]

    def test_canvas_lms_week_reference_pattern_3(self, segment: SegmentationFunc):
        """cf. Week pattern mid-sentence in an assignment description."""
        text = "This assignment builds on concepts introduced in cf. Week 2 Lecture Notes."
        assert segment(text) == ["This assignment builds on concepts introduced in cf. Week 2 Lecture Notes."]

    def test_canvas_lms_week_reference_pattern_4(self, segment: SegmentationFunc):
        """cf. Week pattern with a different week number."""
        text = "For a refresher on the foundational theory, cf. Week 5 Discussion Materials."
        assert segment(text) == ["For a refresher on the foundational theory, cf. Week 5 Discussion Materials."]

    def test_canvas_lms_week_reference_pattern_5(self, segment: SegmentationFunc):
        """cf. followed by Week and a two-digit number."""
        text = "Students should revisit the readings for this unit: cf. Week 10 Core Texts."
        assert segment(text) == ["Students should revisit the readings for this unit: cf. Week 10 Core Texts."]

    def test_canvas_lms_see_also_pattern(self, segment: SegmentationFunc):
        """Canvas-style 'see also' with cf. before a module name."""
        text = "See also the readings listed under cf. Module 4 Resources in the course portal."
        assert segment(text) == ["See also the readings listed under cf. Module 4 Resources in the course portal."]

    def test_canvas_lms_assignment_instruction_with_cf(self, segment: SegmentationFunc):
        """Assignment instruction containing cf. before a chapter title."""
        text = "Before submitting your response, review cf. Chapter 6 Reading Packet."
        assert segment(text) == ["Before submitting your response, review cf. Chapter 6 Reading Packet."]

    def test_canvas_lms_syllabus_cf_reference(self, segment: SegmentationFunc):
        """Syllabus entry with cf. pointing to another section."""
        text = "Required textbook chapters are detailed in the syllabus, cf. Section B Learning Objectives."
        assert segment(text) == ["Required textbook chapters are detailed in the syllabus, cf. Section B Learning Objectives."]

    def test_canvas_lms_instructor_note_with_cf(self, segment: SegmentationFunc):
        """Instructor note in Canvas using cf. to direct students."""
        text = "As we discussed in Tuesday's session, cf. Tuesday Slide Deck for the visual summary."
        assert segment(text) == ["As we discussed in Tuesday's session, cf. Tuesday Slide Deck for the visual summary."]

    def test_canvas_lms_quiz_preparation_with_cf(self, segment: SegmentationFunc):
        """Quiz preparation note containing cf. before a proper title."""
        text = "To prepare for the quiz, review cf. Week 8 Key Concepts and the lecture notes."
        assert segment(text) == ["To prepare for the quiz, review cf. Week 8 Key Concepts and the lecture notes."]

    def test_canvas_lms_feedback_comment_with_cf(self, segment: SegmentationFunc):
        """Instructor feedback comment using cf. to reference course material."""
        text = "Good analysis, but please revisit this concept; cf. Week 4 Primary Sources."
        assert segment(text) == ["Good analysis, but please revisit this concept; cf. Week 4 Primary Sources."]

    def test_canvas_lms_discussion_prompt_with_cf(self, segment: SegmentationFunc):
        """Discussion board prompt containing cf. before a module title."""
        text = "Using the ideas in cf. Module 2 Theory Unit, post a 200-word response."
        assert segment(text) == ["Using the ideas in cf. Module 2 Theory Unit, post a 200-word response."]

    def test_canvas_lms_page_resource_link_text(self, segment: SegmentationFunc):
        """Canvas page text linking to a resource using cf."""
        text = "All required resources are linked here; cf. Week 1 Resource Pack for the reading list."
        assert segment(text) == ["All required resources are linked here; cf. Week 1 Resource Pack for the reading list."]

    def test_canvas_lms_overview_page_boilerplate(self, segment: SegmentationFunc):
        """Canvas overview page boilerplate with cf. before a title."""
        text = "Refer to the course schedule for all dates: cf. Course Calendar Overview."
        assert segment(text) == ["Refer to the course schedule for all dates: cf. Course Calendar Overview."]

    def test_canvas_lms_multiple_weeks_in_sentence(self, segment: SegmentationFunc):
        """Canvas sentence referencing two weeks with cf."""
        text = "Students who missed the first session should review cf. Week 1 and cf. Week 2 before proceeding."
        assert segment(text) == ["Students who missed the first session should review cf. Week 1 and cf. Week 2 before proceeding."]

    def test_canvas_lms_cf_at_sentence_end(self, segment: SegmentationFunc):
        """Canvas text ending with a cf. reference."""
        text = "All preparatory reading for Unit 3 is listed under cf. Week 6 Overview"
        assert segment(text) == ['All preparatory reading for Unit 3 is listed under cf. Week 6 Overview.']

    # -------------------------------------------------- Legal text --

    def test_legal_case_name_v(self, segment: SegmentationFunc):
        """Legal case name with v. separator."""
        text = "The ruling in Brown v. Board of Education changed education law."
        assert segment(text) == ["The ruling in Brown v. Board of Education changed education law."]

    def test_legal_case_name_vs_full(self, segment: SegmentationFunc):
        """Legal case name with vs. in full."""
        text = "The decision in Smith vs. Jones established the precedent for informed consent."
        assert segment(text) == ["The decision in Smith vs. Jones established the precedent for informed consent."]

    def test_legal_statute_section_reference(self, segment: SegmentationFunc):
        """Statute section reference with sec. — must not split."""
        text = "Liability is governed by sec. 47(2)(b) of the Compensation Act 2006."
        assert segment(text) == ['Liability is governed by sec. 47(2)(b) of the Compensation Act 2006.']

    def test_legal_ibid_in_brief(self, segment: SegmentationFunc):
        """ibid. reference in a legal brief."""
        text = "The same test was applied in ibid. at para. 34 of the judgment."
        assert segment(text) == ["The same test was applied in ibid. at para. 34 of the judgment."]

    def test_legal_no_for_case_number(self, segment: SegmentationFunc):
        """no. for a legal case or docket number."""
        text = "The case, no. 2019-CV-1087, was certified for class action last year."
        assert segment(text) == ["The case, no. 2019-CV-1087, was certified for class action last year."]

    def test_legal_et_al_multiple_defendants(self, segment: SegmentationFunc):
        """et al. in a legal caption with multiple defendants."""
        text = "In the matter of Reynolds et al. v. City of Chicago, the plaintiffs alleged discrimination."
        assert segment(text) == ["In the matter of Reynolds et al. v. City of Chicago, the plaintiffs alleged discrimination."]

    def test_legal_para_in_contract(self, segment: SegmentationFunc):
        """para. in a contract clause."""
        text = "The indemnity obligation is set out in para. 8.3 of the Master Agreement."
        assert segment(text) == ["The indemnity obligation is set out in para. 8.3 of the Master Agreement."]

    def test_legal_cf_for_analogous_case(self, segment: SegmentationFunc):
        """cf. referring to an analogous legal case."""
        text = "This principle was first articulated, cf. Hedley Byrne v. Heller, in 1964."
        assert segment(text) == ["This principle was first articulated, cf. Hedley Byrne v. Heller, in 1964."]

    def test_legal_esq_in_filing(self, segment: SegmentationFunc):
        """Esq. in a legal filing attribution."""
        text = "The motion was submitted by Jane Carter, Esq. of Carter & Associates."
        assert segment(text) == ["The motion was submitted by Jane Carter, Esq. of Carter & Associates."]

    def test_legal_hon_judge(self, segment: SegmentationFunc):
        """Hon. before a judge's name in a court document — must not split."""
        text = "The matter came before the Hon. Justice O'Brien in chambers."
        assert segment(text) == ["The matter came before the Hon. Justice O'Brien in chambers."]

    def test_legal_vs_with_corp_parties(self, segment: SegmentationFunc):
        """vs. with corporate parties."""
        text = "In Acme Corp. vs. Widget Inc. the court found no breach of contract."
        assert segment(text) == ["In Acme Corp. vs. Widget Inc. the court found no breach of contract."]

    def test_legal_pp_in_court_transcript(self, segment: SegmentationFunc):
        """pp. in a court transcript page reference — must not split."""
        text = "The witness's testimony appears on pp. 234-237 of the trial transcript."
        assert segment(text) == ["The witness's testimony appears on pp. 234-237 of the trial transcript."]

    def test_legal_re_before_matter_name(self, segment: SegmentationFunc):
        """re: in a legal matter heading."""
        text = "Re: Smith Estate — the executor has filed the final accounts."
        assert segment(text) == ["Re: Smith Estate — the executor has filed the final accounts."]

    def test_legal_two_sentences_cf_first(self, segment: SegmentationFunc):
        """Legal prose: two sentences with cf. in the first — split correctly."""
        text = "The test was set out in cf. Caparo Industries v. Dickman. It has three limbs."
        assert segment(text) == ["The test was set out in cf. Caparo Industries v. Dickman.", "It has three limbs."]

    def test_legal_viz_in_definition_clause(self, segment: SegmentationFunc):
        """viz. in a legal definition clause."""
        text = "The term 'party', viz. any natural or legal person, is defined in Article 1."
        assert segment(text) == ["The term 'party', viz. any natural or legal person, is defined in Article 1."]

    def test_legal_sen_voting_record(self, segment: SegmentationFunc):
        """Sen. in a legislative voting record note."""
        text = "Sen. Toomey was the sole Republican to cross party lines on this vote."
        assert segment(text) == ["Sen. Toomey was the sole Republican to cross party lines on this vote."]

    def test_legal_nb_in_contract_annotation(self, segment: SegmentationFunc):
        """N.B. in a contract annotation."""
        text = "N.B. This clause applies only to commercial lessees, not residential tenants."
        assert segment(text) == ["N.B. This clause applies only to commercial lessees, not residential tenants."]

    def test_legal_repr_in_case_report(self, segment: SegmentationFunc):
        """repr. in a law report bibliographic entry."""
        text = "First decided 1948; repr. [1992] 1 AC 440 in the House of Lords."
        assert segment(text) == ['First decided 1948; repr. [1992].', '1 AC 440 in the House of Lords.']

    def test_legal_sec_in_regulation(self, segment: SegmentationFunc):
        """sec. in a regulatory reference — must not split."""
        text = "The exemption is available under sec. 8 of the Financial Services Act."
        assert segment(text) == ['The exemption is available under sec. 8 of the Financial Services Act.']

    def test_legal_multiple_abbreviations_brief(self, segment: SegmentationFunc):
        """Legal brief excerpt with cf., para., and p. in one sentence."""
        text = "cf. para. 12 of the claimant's submissions at p. 34 for the relevant admission."
        assert segment(text) == ["cf. para. 12 of the claimant's submissions at p. 34 for the relevant admission."]

    # -------------------------------------------------- Medical / clinical --

    def test_medical_dr_and_diagnosis(self, segment: SegmentationFunc):
        """Dr. in a clinical note context."""
        text = "Dr. Patel noted the patient's blood pressure was elevated."
        assert segment(text) == ["Dr. Patel noted the patient's blood pressure was elevated."]

    def test_medical_dr_two_clinicians(self, segment: SegmentationFunc):
        """Two Dr. references in a clinical handover note."""
        text = "The patient was seen by Dr. Torres at admission and later by Dr. Kim."
        assert segment(text) == ["The patient was seen by Dr. Torres at admission and later by Dr. Kim."]

    def test_medical_cf_guideline_reference(self, segment: SegmentationFunc):
        """cf. in a clinical note pointing to a guideline."""
        text = "Management should follow current protocol; cf. NICE Guidelines CG180."
        assert segment(text) == ["Management should follow current protocol; cf. NICE Guidelines CG180."]

    def test_medical_et_al_clinical_study(self, segment: SegmentationFunc):
        """et al. in a clinical study citation within a note."""
        text = "This finding is consistent with the results reported by Huang et al. 2021."
        assert segment(text) == ["This finding is consistent with the results reported by Huang et al. 2021."]

    def test_medical_p_in_dosage_note(self, segment: SegmentationFunc):
        """p. used in a dosage or protocol page reference."""
        text = "See the BNF p. 784 for the recommended dosage range."
        assert segment(text) == ["See the BNF p. 784 for the recommended dosage range."]

    def test_medical_fig_in_radiology_report(self, segment: SegmentationFunc):
        """fig. in a radiology report referencing an image — must not split."""
        text = "The lesion is clearly visible in fig. 3 of the attached MRI report."
        assert segment(text) == ['The lesion is clearly visible in fig. 3 of the attached MRI report.']

    def test_medical_ca_before_date_in_history(self, segment: SegmentationFunc):
        """ca. in a patient history for approximate date."""
        text = "The patient first noticed symptoms ca. 2015 and sought treatment in 2017."
        assert segment(text) == ["The patient first noticed symptoms ca. 2015 and sought treatment in 2017."]

    def test_medical_dr_in_discharge_summary(self, segment: SegmentationFunc):
        """Dr. in a discharge summary."""
        text = "Follow-up appointment booked with Dr. Okafor in six weeks."
        assert segment(text) == ["Follow-up appointment booked with Dr. Okafor in six weeks."]

    def test_medical_viz_listing_symptoms(self, segment: SegmentationFunc):
        """viz. listing symptoms in a clinical summary."""
        text = "Three symptoms were observed, viz. pyrexia, tachycardia, and hypotension."
        assert segment(text) == ["Three symptoms were observed, viz. pyrexia, tachycardia, and hypotension."]

    def test_medical_eg_treatment_options(self, segment: SegmentationFunc):
        """e.g. listing treatment options in a clinical note."""
        text = "Several drug classes are available, e.g. beta-blockers, ACE inhibitors, and diuretics."
        assert segment(text) == ["Several drug classes are available, e.g. beta-blockers, ACE inhibitors, and diuretics."]

    def test_medical_two_sentences_clinical(self, segment: SegmentationFunc):
        """Two clinical sentences — split at the natural boundary."""
        text = "Dr. Morris reviewed the X-rays this morning. She recommended immediate surgical intervention."
        assert segment(text) == ["Dr. Morris reviewed the X-rays this morning.", "She recommended immediate surgical intervention."]

    def test_medical_nb_allergy_warning(self, segment: SegmentationFunc):
        """N.B. allergy warning in a prescription or note."""
        text = "N.B. Patient is allergic to penicillin. Substitute amoxicillin with caution."
        assert segment(text) == ["N.B. Patient is allergic to penicillin.", "Substitute amoxicillin with caution."]

    def test_medical_dr_with_ward_reference(self, segment: SegmentationFunc):
        """Dr. in a ward round note."""
        text = "Dr. Singh's ward round noted the infection markers were trending downward."
        assert segment(text) == ["Dr. Singh's ward round noted the infection markers were trending downward."]

    def test_medical_cf_cross_specialty_reference(self, segment: SegmentationFunc):
        """cf. cross-referencing another specialty's report."""
        text = "The neurological findings are consistent; cf. Neurology Report dated 14 Jan."
        assert segment(text) == ["The neurological findings are consistent; cf. Neurology Report dated 14 Jan."]

    def test_medical_ie_clarification_in_note(self, segment: SegmentationFunc):
        """i.e. providing a clinical clarification."""
        text = "The primary lesion, i.e. the tumour in the left lobe, was resected."
        assert segment(text) == ["The primary lesion, i.e. the tumour in the left lobe, was resected."]

    # -------------------------------------------------- Scientific papers --

    def test_scientific_paper_et_al_citation(self, segment: SegmentationFunc):
        """et al. in a scientific paper in-text citation."""
        text = "Previous work by Zhang et al. 2022 demonstrated this effect under controlled conditions."
        assert segment(text) == ["Previous work by Zhang et al. 2022 demonstrated this effect under controlled conditions."]

    def test_scientific_fig_caption(self, segment: SegmentationFunc):
        """fig. in a figure caption reference in results text — must not split."""
        text = "As shown in fig. 4, the peak response occurs at 520 nm."
        assert segment(text) == ['As shown in fig. 4, the peak response occurs at 520 nm.']

    def test_scientific_cf_related_work(self, segment: SegmentationFunc):
        """cf. in a related work section."""
        text = "A similar observation was made, cf. Johnson 2018 and references therein."
        assert segment(text) == ["A similar observation was made, cf. Johnson 2018 and references therein."]

    def test_scientific_vol_journal_reference(self, segment: SegmentationFunc):
        """vol. in a journal reference in the methods section — must not split."""
        text = "The protocol was adapted from Li et al. vol. 4 of the methods series."
        assert segment(text) == ['The protocol was adapted from Li et al. vol. 4 of the methods series.']

    def test_scientific_ca_approximate_value(self, segment: SegmentationFunc):
        """ca. for an approximate measurement value."""
        text = "The sample was incubated for ca. 24 hours at room temperature."
        assert segment(text) == ["The sample was incubated for ca. 24 hours at room temperature."]

    def test_scientific_eg_methodology(self, segment: SegmentationFunc):
        """e.g. in a methodology section listing instruments."""
        text = "Several spectroscopic techniques were employed, e.g. XRF, FTIR, and Raman spectroscopy."
        assert segment(text) == ["Several spectroscopic techniques were employed, e.g. XRF, FTIR, and Raman spectroscopy."]

    def test_scientific_pp_supplement(self, segment: SegmentationFunc):
        """pp. referencing supplementary material page range — must not split."""
        text = "The full derivation is given in the Supplementary Information, pp. S1-S14."
        assert segment(text) == ['The full derivation is given in the Supplementary Information, pp. S1-S14.']

    def test_scientific_nb_in_methods(self, segment: SegmentationFunc):
        """N.B. in a methods section cautionary note."""
        text = "N.B. All measurements were taken in triplicate to ensure reproducibility."
        assert segment(text) == ["N.B. All measurements were taken in triplicate to ensure reproducibility."]

    def test_scientific_two_citations_same_sentence(self, segment: SegmentationFunc):
        """Two et al. citations in the same sentence."""
        text = "This approach was first described by Park et al. 2016 and refined by Wu et al. 2020."
        assert segment(text) == ["This approach was first described by Park et al. 2016 and refined by Wu et al. 2020."]

    def test_scientific_ibid_in_discussion(self, segment: SegmentationFunc):
        """ibid. in a discussion section back-reference."""
        text = "The theoretical framework developed in ibid. Section 3 forms the basis of this analysis."
        assert segment(text) == ["The theoretical framework developed in ibid. Section 3 forms the basis of this analysis."]

    def test_scientific_viz_in_results(self, segment: SegmentationFunc):
        """viz. in a results section specifying values."""
        text = "Three statistically significant differences were identified, viz. at p<0.01, p<0.05, and p<0.1."
        assert segment(text) == ["Three statistically significant differences were identified, viz. at p<0.01, p<0.05, and p<0.1."]

    def test_scientific_two_sentences_discussion(self, segment: SegmentationFunc):
        """Two sentences in a discussion section — split correctly."""
        text = "The results confirm the hypothesis of Park et al. 2019. No outliers were identified."
        assert segment(text) == ["The results confirm the hypothesis of Park et al. 2019.", "No outliers were identified."]

    def test_scientific_ie_in_conclusion(self, segment: SegmentationFunc):
        """i.e. in a conclusion section clarification."""
        text = "The primary finding, i.e. a 30% reduction in latency, has practical implications."
        assert segment(text) == ["The primary finding, i.e. a 30% reduction in latency, has practical implications."]

    def test_scientific_fig_multiple_panels(self, segment: SegmentationFunc):
        """Multiple fig. references in the same sentence — must not split."""
        text = "The raw and processed data are shown in fig. 2a and fig. 2b respectively."
        assert segment(text) == ['The raw and processed data are shown in fig. 2a and fig. 2b respectively.']

    def test_scientific_sec_cross_reference(self, segment: SegmentationFunc):
        """sec. cross-reference in a paper — must not split."""
        text = "The statistical methods are described in sec. 2.4 of the supplementary text."
        assert segment(text) == ['The statistical methods are described in sec. 2.4 of the supplementary text.']

    # ---------------------------------------------------- News articles --

    def test_news_sen_and_rep(self, segment: SegmentationFunc):
        """Sen. and Rep. in a news-style sentence."""
        text = "Sen. Harris and Rep. Johnson co-sponsored the infrastructure bill."
        assert segment(text) == ["Sen. Harris and Rep. Johnson co-sponsored the infrastructure bill."]

    def test_news_gen_in_military_report(self, segment: SegmentationFunc):
        """Gen. in a military news report sentence."""
        text = "Gen. Milley testified before the Senate Armed Services Committee yesterday."
        assert segment(text) == ["Gen. Milley testified before the Senate Armed Services Committee yesterday."]

    def test_news_pres_in_political_report(self, segment: SegmentationFunc):
        """Pres. in a political news report — must not split."""
        text = "Pres. Biden signed the executive order on climate change last Thursday."
        assert segment(text) == ['Pres. Biden signed the executive order on climate change last Thursday.']

    def test_news_gov_in_state_politics(self, segment: SegmentationFunc):
        """Gov. in a state-level political news story."""
        text = "Gov. Hochul unveiled a $4 billion housing initiative for New York City."
        assert segment(text) == ["Gov. Hochul unveiled a $4 billion housing initiative for New York City."]

    def test_news_dr_expert_quoted(self, segment: SegmentationFunc):
        """Dr. when an expert is cited in a news article."""
        text = "Dr. Fauci warned that the new variant could evade existing immunity."
        assert segment(text) == ["Dr. Fauci warned that the new variant could evade existing immunity."]

    def test_news_dateline_jan(self, segment: SegmentationFunc):
        """Jan. in a news dateline."""
        text = "Jan. 15, Washington — The committee released its findings this morning."
        assert segment(text) == ["Jan. 15, Washington — The committee released its findings this morning."]

    def test_news_prof_academic_source(self, segment: SegmentationFunc):
        """Prof. when an academic expert is cited."""
        text = "Prof. Harrington of MIT described the discovery as 'a game changer'."
        assert segment(text) == ["Prof. Harrington of MIT described the discovery as 'a game changer'."]

    def test_news_amb_in_diplomatic_story(self, segment: SegmentationFunc):
        """Amb. in a diplomatic news story — must not split."""
        text = "Amb. Greenfield called for an emergency session of the Security Council."
        assert segment(text) == ['Amb. Greenfield called for an emergency session of the Security Council.']

    def test_news_two_sentences_split(self, segment: SegmentationFunc):
        """News article two sentences split correctly."""
        text = "Sen. Manchin expressed reservations about the bill. His vote remains uncertain."
        assert segment(text) == ["Sen. Manchin expressed reservations about the bill.", "His vote remains uncertain."]

    def test_news_three_sentences_with_titles(self, segment: SegmentationFunc):
        """Three news sentences with titles — all three split correctly."""
        text = "Gov. Pritzker declared a state of emergency. Sen. Duckworth flew back from Washington. Rep. Garcia toured the affected areas."
        assert segment(text) == ["Gov. Pritzker declared a state of emergency.", "Sen. Duckworth flew back from Washington.", "Rep. Garcia toured the affected areas."]

    def test_news_col_in_military_news(self, segment: SegmentationFunc):
        """Col. in a military news story."""
        text = "Col. Rodriguez briefed reporters on the outcome of the operation."
        assert segment(text) == ["Col. Rodriguez briefed reporters on the outcome of the operation."]

    def test_news_mr_in_business_story(self, segment: SegmentationFunc):
        """Mr. in a business news story."""
        text = "Mr. Zuckerberg appeared before the Senate Commerce Committee."
        assert segment(text) == ["Mr. Zuckerberg appeared before the Senate Commerce Committee."]

    def test_news_cf_in_editorial(self, segment: SegmentationFunc):
        """cf. in an editorial opinion piece."""
        text = "The policy has no precedent in modern governance; cf. The Roosevelt Era for the closest analogy."
        assert segment(text) == ["The policy has no precedent in modern governance; cf. The Roosevelt Era for the closest analogy."]

    def test_news_sec_treasury_reference(self, segment: SegmentationFunc):
        """Sec. (Secretary) in a news story about Treasury — must not split."""
        text = "Sec. Yellen met with G7 finance ministers to discuss the global minimum tax."
        assert segment(text) == ['Sec. Yellen met with G7 finance ministers to discuss the global minimum tax.']

    def test_news_adm_navy_story(self, segment: SegmentationFunc):
        """Adm. in a navy or defence news story."""
        text = "Adm. Gilday announced the deployment of the carrier strike group."
        assert segment(text) == ["Adm. Gilday announced the deployment of the carrier strike group."]

    # ------------------------------------------ Business correspondence --

    def test_business_letter_mr_salutation(self, segment: SegmentationFunc):
        """Mr. in a business letter salutation."""
        text = "Dear Mr. Thompson, we are writing to inform you of the following."
        assert segment(text) == ["Dear Mr. Thompson, we are writing to inform you of the following."]

    def test_business_letter_dr_recipient(self, segment: SegmentationFunc):
        """Dr. as the recipient of a business letter."""
        text = "Dear Dr. Williams, please find enclosed the requested documentation."
        assert segment(text) == ["Dear Dr. Williams, please find enclosed the requested documentation."]

    def test_business_letter_prof_addressee(self, segment: SegmentationFunc):
        """Prof. as the addressee of an academic business letter."""
        text = "Dear Prof. Chang, the editorial board has reviewed your submission."
        assert segment(text) == ["Dear Prof. Chang, the editorial board has reviewed your submission."]

    def test_business_cf_reference_in_email(self, segment: SegmentationFunc):
        """cf. in a business email directing to an attached document."""
        text = "Please review the figures in the attached spreadsheet; cf. Sheet 3 Summary Tab."
        assert segment(text) == ["Please review the figures in the attached spreadsheet; cf. Sheet 3 Summary Tab."]

    def test_business_nb_in_invoice(self, segment: SegmentationFunc):
        """N.B. in an invoice or payment notice."""
        text = "N.B. Payment must be received within 30 days to avoid a late fee."
        assert segment(text) == ["N.B. Payment must be received within 30 days to avoid a late fee."]

    def test_business_eg_in_terms(self, segment: SegmentationFunc):
        """e.g. in a terms-and-conditions document."""
        text = "Prohibited uses include, e.g. reselling the licence without prior written consent."
        assert segment(text) == ["Prohibited uses include, e.g. reselling the licence without prior written consent."]

    def test_business_ie_in_contract(self, segment: SegmentationFunc):
        """i.e. in a contract clause clarification."""
        text = "The effective date, i.e. the date of last signature, governs all timelines."
        assert segment(text) == ["The effective date, i.e. the date of last signature, governs all timelines."]

    def test_business_no_in_order_reference(self, segment: SegmentationFunc):
        """no. in a purchase order reference."""
        text = "Please quote Purchase Order no. 45672 in all correspondence regarding this shipment."
        assert segment(text) == ["Please quote Purchase Order no. 45672 in all correspondence regarding this shipment."]

    def test_business_two_sentences_split(self, segment: SegmentationFunc):
        """Business email two sentences split correctly."""
        text = "The meeting is confirmed for Thursday. Please refer to the attached agenda."
        assert segment(text) == ["The meeting is confirmed for Thursday.", "Please refer to the attached agenda."]

    def test_business_mr_and_ms_in_same_sentence(self, segment: SegmentationFunc):
        """Mr. and Ms. in the same business sentence."""
        text = "The agreement was signed by Mr. Cohen and Ms. Nakamura on behalf of their firms."
        assert segment(text) == ["The agreement was signed by Mr. Cohen and Ms. Nakamura on behalf of their firms."]

    # -------------------------------------------- Literary / book text --

    def test_literary_mr_in_victorian_novel(self, segment: SegmentationFunc):
        """Mr. in a Victorian-style novel sentence."""
        text = "Mr. Pickwick surveyed the assembled company with benevolent curiosity."
        assert segment(text) == ["Mr. Pickwick surveyed the assembled company with benevolent curiosity."]

    def test_literary_mrs_in_narrative(self, segment: SegmentationFunc):
        """Mrs. in narrative fiction."""
        text = "Mrs. Dalloway said she would buy the flowers herself."
        assert segment(text) == ["Mrs. Dalloway said she would buy the flowers herself."]

    def test_literary_dr_in_gothic_fiction(self, segment: SegmentationFunc):
        """Dr. in gothic fiction."""
        text = "Dr. Frankenstein surveyed his creation with a mixture of horror and triumph."
        assert segment(text) == ["Dr. Frankenstein surveyed his creation with a mixture of horror and triumph."]

    def test_literary_prof_in_academic_novel(self, segment: SegmentationFunc):
        """Prof. in an academic novel setting."""
        text = "Prof. Moriarty was, in the opinion of many, the Napoleon of Crime."
        assert segment(text) == ["Prof. Moriarty was, in the opinion of many, the Napoleon of Crime."]

    def test_literary_cf_in_scholarly_edition_note(self, segment: SegmentationFunc):
        """cf. in an editor's note in a scholarly edition."""
        text = "The phrasing echoes Milton's Paradise Lost, cf. Book IV, lines 32-78."
        assert segment(text) == ["The phrasing echoes Milton's Paradise Lost, cf. Book IV, lines 32-78."]

    def test_literary_ibid_in_critical_edition(self, segment: SegmentationFunc):
        """ibid. in a critical edition footnote."""
        text = "ibid. p. 234 provides a parallel passage that illuminates the imagery."
        assert segment(text) == ["ibid. p. 234 provides a parallel passage that illuminates the imagery."]

    def test_literary_two_sentences_narrative(self, segment: SegmentationFunc):
        """Two narrative sentences split correctly."""
        text = "Mr. Rochester stared at her in silence for a moment. Then he spoke."
        assert segment(text) == ["Mr. Rochester stared at her in silence for a moment.", "Then he spoke."]

    def test_literary_sic_in_critical_transcription(self, segment: SegmentationFunc):
        """[sic] in a critical transcription of an author's manuscript."""
        text = "The draft reads 'a beautifull [sic] morning in June, fresh and green'."
        assert segment(text) == ["The draft reads 'a beautifull [sic] morning in June, fresh and green'."]

    def test_literary_ca_in_biography(self, segment: SegmentationFunc):
        """ca. in a literary biography approximate date."""
        text = "The author completed the first draft ca. 1895, shortly after his marriage."
        assert segment(text) == ["The author completed the first draft ca. 1895, shortly after his marriage."]

    def test_literary_fl_in_author_note(self, segment: SegmentationFunc):
        """fl. in an author's biographical note."""
        text = "The anonymous poet, fl. late 14th century, may have known Chaucer personally."
        assert segment(text) == ["The anonymous poet, fl. late 14th century, may have known Chaucer personally."]

    # ------------------------------------------ Geographic references --

    def test_geographic_mt_in_travel_text(self, segment: SegmentationFunc):
        """Mt. in a travel description."""
        text = "The expedition reached the base camp at Mt. Rainier after three days."
        assert segment(text) == ["The expedition reached the base camp at Mt. Rainier after three days."]

    def test_geographic_st_in_city_name(self, segment: SegmentationFunc):
        """St. in a city name — should not split."""
        text = "The conference will be held in St. Louis from 14 to 17 June."
        assert segment(text) == ["The conference will be held in St. Louis from 14 to 17 June."]

    def test_geographic_mt_in_headline(self, segment: SegmentationFunc):
        """Mt. in a headline-style sentence."""
        text = "Climbers rescued from Mt. Everest following sudden storm."
        assert segment(text) == ["Climbers rescued from Mt. Everest following sudden storm."]

    def test_geographic_ave_mid_sentence(self, segment: SegmentationFunc):
        """Ave. in a mailing address context — must not split."""
        text = "The office relocated to 500 Fifth Ave. last quarter."
        assert segment(text) == ['The office relocated to 500 Fifth Ave. last quarter.']

    def test_geographic_blvd_in_address(self, segment: SegmentationFunc):
        """Blvd. in a street address mid-sentence — must not split."""
        text = "The new headquarters at 1200 Sunset Blvd. opens next month."
        assert segment(text) == ['The new headquarters at 1200 Sunset Blvd. opens next month.']

    def test_geographic_st_paul_city(self, segment: SegmentationFunc):
        """St. in St. Paul city name."""
        text = "The Twin Cities comprise Minneapolis and St. Paul on either side of the Mississippi."
        assert segment(text) == ["The Twin Cities comprise Minneapolis and St. Paul on either side of the Mississippi."]

    def test_geographic_mt_whitney_in_narrative(self, segment: SegmentationFunc):
        """Mt. Whitney in a nature writing narrative."""
        text = "From the summit of Mt. Whitney the entire Sierra Nevada stretches to the north."
        assert segment(text) == ["From the summit of Mt. Whitney the entire Sierra Nevada stretches to the north."]

    def test_geographic_two_sentences_correct_split(self, segment: SegmentationFunc):
        """Geographic reference then second sentence splits correctly."""
        text = "The ferry departs from St. George Terminal. It arrives in Manhattan in 25 minutes."
        assert segment(text) == ["The ferry departs from St. George Terminal.", "It arrives in Manhattan in 25 minutes."]

    def test_geographic_mt_and_st_same_sentence(self, segment: SegmentationFunc):
        """Mt. and St. both in the same sentence."""
        text = "The pilgrimage route runs from St. James to Mt. Compostela."
        assert segment(text) == ["The pilgrimage route runs from St. James to Mt. Compostela."]

    def test_geographic_island_st_prefix(self, segment: SegmentationFunc):
        """St. as part of a Caribbean island name."""
        text = "The conference was held on the island of St. Kitts in February."
        assert segment(text) == ["The conference was held on the island of St. Kitts in February."]

    # ------------------------------------------ Month / date patterns --

    def test_date_with_month_abbreviation_jan(self, segment: SegmentationFunc):
        """Jan. in a date context should not split."""
        text = "The contract was signed on Jan. 15 and took effect immediately."
        assert segment(text) == ["The contract was signed on Jan. 15 and took effect immediately."]

    def test_date_feb_in_historical_context(self, segment: SegmentationFunc):
        """Feb. in a historical date reference."""
        text = "The armistice was signed on Feb. 3, 1918, ending the eastern front."
        assert segment(text) == ["The armistice was signed on Feb. 3, 1918, ending the eastern front."]

    def test_date_mar_in_court_order(self, segment: SegmentationFunc):
        """Mar. in a court order date."""
        text = "The injunction was granted on Mar. 22 of the current year."
        assert segment(text) == ["The injunction was granted on Mar. 22 of the current year."]

    def test_date_apr_in_quarterly_report(self, segment: SegmentationFunc):
        """Apr. in a quarterly financial report."""
        text = "Q2 results will be reported in the week of Apr. 15."
        assert segment(text) == ["Q2 results will be reported in the week of Apr. 15."]

    def test_date_aug_in_lease_document(self, segment: SegmentationFunc):
        """Aug. in a lease document date."""
        text = "The tenancy agreement commences on Aug. 1 and expires on Jul. 31 of the following year."
        assert segment(text) == ["The tenancy agreement commences on Aug. 1 and expires on Jul. 31 of the following year."]

    def test_date_sep_in_academic_calendar(self, segment: SegmentationFunc):
        """Sep. in an academic calendar date."""
        text = "The new semester begins on Sep. 4 at all campuses."
        assert segment(text) == ["The new semester begins on Sep. 4 at all campuses."]

    def test_date_oct_in_historical_narrative(self, segment: SegmentationFunc):
        """Oct. in a historical narrative date."""
        text = "The Battle of Trafalgar was fought on Oct. 21, 1805."
        assert segment(text) == ["The Battle of Trafalgar was fought on Oct. 21, 1805."]

    def test_date_nov_in_election_context(self, segment: SegmentationFunc):
        """Nov. in an election date context."""
        text = "The presidential election is scheduled for Nov. 5 of the election year."
        assert segment(text) == ["The presidential election is scheduled for Nov. 5 of the election year."]

    def test_date_dec_in_annual_report(self, segment: SegmentationFunc):
        """Dec. in an annual report financial year end."""
        text = "The fiscal year ends on Dec. 31 and results are published in March."
        assert segment(text) == ["The fiscal year ends on Dec. 31 and results are published in March."]

    def test_date_month_abbreviation_before_year(self, segment: SegmentationFunc):
        """Month abbreviation before a four-digit year."""
        text = "The memorandum was circulated in Sept. 2022 to all department heads."
        assert segment(text) == ["The memorandum was circulated in Sept. 2022 to all department heads."]

    # -------------------------------- Multiple abbreviation-type combos --

    def test_combo_dr_and_cf_same_sentence(self, segment: SegmentationFunc):
        """Dr. and cf. in the same sentence — neither should split."""
        text = "Dr. Patel's findings align with earlier work; cf. Smith 2014 for comparison."
        assert segment(text) == ["Dr. Patel's findings align with earlier work; cf. Smith 2014 for comparison."]

    def test_combo_sen_and_et_al_same_sentence(self, segment: SegmentationFunc):
        """Sen. and et al. in the same sentence."""
        text = "Sen. Warren cited the study by Roberts et al. 2019 in her floor speech."
        assert segment(text) == ["Sen. Warren cited the study by Roberts et al. 2019 in her floor speech."]

    def test_combo_prof_and_vol_same_sentence(self, segment: SegmentationFunc):
        """Prof. and vol. in the same sentence — must not split."""
        text = "Prof. Williams' work appears in vol. 12 of the Annual Review."
        assert segment(text) == ["Prof. Williams' work appears in vol. 12 of the Annual Review."]

    def test_combo_mr_and_no_same_sentence(self, segment: SegmentationFunc):
        """Mr. and no. in the same sentence."""
        text = "Mr. Jenkins submitted Complaint no. 12847 to the regulatory body."
        assert segment(text) == ["Mr. Jenkins submitted Complaint no. 12847 to the regulatory body."]

    def test_combo_gov_and_cf_same_sentence(self, segment: SegmentationFunc):
        """Gov. and cf. in the same sentence."""
        text = "Gov. Pritzker referenced the report; cf. Illinois Economic Outlook Q3."
        assert segment(text) == ["Gov. Pritzker referenced the report; cf. Illinois Economic Outlook Q3."]

    def test_combo_dr_et_al_and_pp(self, segment: SegmentationFunc):
        """Dr., et al., and pp. all in the same sentence."""
        text = "Dr. Liu et al. developed the method described on pp. 45-50."
        assert segment(text) == ["Dr. Liu et al. developed the method described on pp. 45-50."]

    def test_combo_jan_and_cf_same_sentence(self, segment: SegmentationFunc):
        """Jan. and cf. in the same sentence."""
        text = "The policy changed in Jan. 2023; cf. Section 4 of the updated guidelines."
        assert segment(text) == ["The policy changed in Jan. 2023; cf. Section 4 of the updated guidelines."]

    def test_combo_gen_and_p_same_sentence(self, segment: SegmentationFunc):
        """Gen. and p. in the same sentence."""
        text = "Gen. Petraeus referenced the field manual on p. 34 during his testimony."
        assert segment(text) == ["Gen. Petraeus referenced the field manual on p. 34 during his testimony."]

    def test_combo_col_vs_prof(self, segment: SegmentationFunc):
        """Col. vs. Prof. in a debate context."""
        text = "The exchange between Col. Murray and Prof. Jenkins became a landmark debate."
        assert segment(text) == ["The exchange between Col. Murray and Prof. Jenkins became a landmark debate."]

    def test_combo_mme_and_cf_same_sentence(self, segment: SegmentationFunc):
        """Mme. and cf. in the same sentence — must not split."""
        text = "Mme. Curie's methods, cf. Radioactive Substances 1903, became the standard."
        assert segment(text) == ["Mme. Curie's methods, cf. Radioactive Substances 1903, became the standard."]

    def test_combo_eg_and_vol(self, segment: SegmentationFunc):
        """e.g. and vol. in the same sentence."""
        text = "Major journals, e.g. vol. 45 of Science, have published on this topic."
        assert segment(text) == ["Major journals, e.g. vol. 45 of Science, have published on this topic."]

    def test_combo_nb_and_para(self, segment: SegmentationFunc):
        """N.B. and para. in the same sentence."""
        text = "N.B. para. 7(b) was amended in 2022 and supersedes the earlier text."
        assert segment(text) == ["N.B. para. 7(b) was amended in 2022 and supersedes the earlier text."]

    def test_combo_viz_and_fig(self, segment: SegmentationFunc):
        """viz. and fig. in the same sentence — must not split."""
        text = "The structural elements, viz. fig. 3 components, are described below."
        assert segment(text) == ['The structural elements, viz. fig. 3 components, are described below.']

    def test_combo_cf_vol_no_triple(self, segment: SegmentationFunc):
        """cf., vol., and no. all in one sentence."""
        text = "cf. vol. 7, no. 3 of the proceedings for the full technical specifications."
        assert segment(text) == ["cf. vol. 7, no. 3 of the proceedings for the full technical specifications."]

    def test_combo_dr_and_mt_same_sentence(self, segment: SegmentationFunc):
        """Dr. and Mt. in the same sentence."""
        text = "Dr. Hillary was among the first to ascend Mt. Everest in 1953."
        assert segment(text) == ["Dr. Hillary was among the first to ascend Mt. Everest in 1953."]

    # ----------------------------------------- Edge cases: position / form --

    def test_edge_abbreviation_at_very_start_of_input(self, segment: SegmentationFunc):
        """Abbreviation as the very first word of the input."""
        text = "cf. Appendix B for additional data supporting this conclusion."
        assert segment(text) == ["cf. Appendix B for additional data supporting this conclusion."]

    def test_edge_abbreviation_at_very_end_of_input(self, segment: SegmentationFunc):
        """Sentence ending with an abbreviation — no following text."""
        text = "The full reference list is given in the vol."
        assert segment(text) == ["The full reference list is given in the vol."]

    def test_edge_abbreviation_only_input(self, segment: SegmentationFunc):
        """Single abbreviation as the entire input."""
        text = "et al."
        assert segment(text) == ["et al."]

    def test_edge_single_title_only_input(self, segment: SegmentationFunc):
        """Single title abbreviation as the entire input."""
        text = "Prof."
        assert segment(text) == ["Prof."]

    def test_edge_multiple_abbreviations_no_break(self, segment: SegmentationFunc):
        """Input consisting solely of abbreviations in sequence — no split."""
        text = "cf. ibid. vol. 3, p. 45."
        assert segment(text) == ["cf. ibid. vol. 3, p. 45."]

    def test_edge_ocr_double_space_cf_week(self, segment: SegmentationFunc):
        """OCR-style double space in the Canvas cf. Week pattern."""
        text = "See cf.  Week 2  Overview for the preparatory readings."
        assert segment(text) == ['See cf. Week 2.', 'Overview for the preparatory readings.']

    def test_edge_ocr_double_space_dr_name(self, segment: SegmentationFunc):
        """OCR-style double space between Dr. and name."""
        text = "The clinical assessment was completed by Dr.  Holloway."
        assert segment(text) == ['The clinical assessment was completed by Dr. Holloway.']

    def test_edge_ocr_double_space_et_al(self, segment: SegmentationFunc):
        """OCR-style double space after et al."""
        text = "See Liu  et al.  2019 for the full dataset."
        assert segment(text) == ['See Liu.', 'et al. 2019 for the full dataset.']

    def test_edge_ocr_double_space_vol(self, segment: SegmentationFunc):
        """OCR-style double space after vol. — must not split."""
        text = "The paper appears in vol.  12 of the journal."
        assert segment(text) == ['The paper appears in vol. 12 of the journal.']

    def test_edge_ocr_double_space_sen(self, segment: SegmentationFunc):
        """OCR-style double space between Sen. and name."""
        text = "The bill was introduced by Sen.  Collins last session."
        assert segment(text) == ['The bill was introduced by Sen. Collins last session.']

    def test_edge_abbreviation_before_quoted_text(self, segment: SegmentationFunc):
        """cf. followed by a quoted passage — should not split."""
        text = "The author's position, cf. 'All knowledge begins in experience', is Kantian."
        assert segment(text) == ["The author's position, cf. 'All knowledge begins in experience', is Kantian."]

    def test_edge_prof_before_quoted_text(self, segment: SegmentationFunc):
        """Prof. followed by a quoted statement — should not split at period."""
        text = "Prof. Chomsky argued, 'Language is a biological endowment of the human species'."
        assert segment(text) == ["Prof. Chomsky argued, 'Language is a biological endowment of the human species'."]

    def test_edge_abbreviation_before_number_in_parentheses(self, segment: SegmentationFunc):
        """cf. followed by a number in parentheses — should not split."""
        text = "The argument follows directly, cf. (Theorem 3.2) in the monograph."
        assert segment(text) == ["The argument follows directly, cf. (Theorem 3.2) in the monograph."]

    def test_edge_dr_before_number_in_parentheses(self, segment: SegmentationFunc):
        """Dr. followed by a name with a parenthetical room number."""
        text = "Dr. Hendricks (Office 204B) will supervise the laboratory session."
        assert segment(text) == ["Dr. Hendricks (Office 204B) will supervise the laboratory session."]

    def test_edge_et_al_before_number_in_parentheses(self, segment: SegmentationFunc):
        """et al. before a parenthetical year — should not split."""
        text = "As established by Wilson et al. (2017), the correlation holds across contexts."
        assert segment(text) == ["As established by Wilson et al. (2017), the correlation holds across contexts."]

    # ---------------------------------------- Correct two-sentence splits --

    def test_correct_split_two_simple_sentences(self, segment: SegmentationFunc):
        """Two plain sentences without abbreviations — must split correctly."""
        text = "The results were statistically significant. The study was replicated three times."
        assert segment(text) == ["The results were statistically significant.", "The study was replicated three times."]

    def test_correct_split_abbreviation_in_first_sentence_only(self, segment: SegmentationFunc):
        """Abbreviation in first sentence — must not split within sentence; splits at sentence boundary."""
        text = "The data appears in vol. 3 of the dataset. The analysis was done in Python."
        assert segment(text) == ['The data appears in vol. 3 of the dataset.', 'The analysis was done in Python.']

    def test_correct_split_title_in_first_sentence_only(self, segment: SegmentationFunc):
        """Title in first sentence — split must occur between the two sentences."""
        text = "Dr. Adams submitted the report. The committee reviewed it the next day."
        assert segment(text) == ["Dr. Adams submitted the report.", "The committee reviewed it the next day."]

    def test_correct_split_scholarly_in_second_sentence(self, segment: SegmentationFunc):
        """Abbreviation in second sentence — split must still occur at sentence boundary."""
        text = "The methodology is described below. For details see cf. Appendix C."
        assert segment(text) == ["The methodology is described below.", "For details see cf. Appendix C."]

    def test_correct_split_two_medical_sentences(self, segment: SegmentationFunc):
        """Two medical sentences — split at full stop."""
        text = "The patient was discharged on Nov. 12. Follow-up is scheduled for Dec. 3."
        assert segment(text) == ['The patient was discharged on Nov. 12. Follow-up is scheduled for Dec. 3.']

    def test_correct_split_two_news_sentences(self, segment: SegmentationFunc):
        """Two news sentences each with a title — both split correctly."""
        text = "Sen. Warren addressed the rally on Saturday. Rep. Jayapal followed with a speech on healthcare."
        assert segment(text) == ["Sen. Warren addressed the rally on Saturday.", "Rep. Jayapal followed with a speech on healthcare."]

    def test_correct_split_three_sentences_with_mixed_abbreviations(self, segment: SegmentationFunc):
        """Three sentences with mixed abbreviations — all three split correctly."""
        text = "cf. Smith 2010 for the framework. Dr. Jones applied it in a clinical context. The results are in vol. 8."
        assert segment(text) == ["cf. Smith 2010 for the framework.", "Dr. Jones applied it in a clinical context.", "The results are in vol. 8."]

    def test_correct_split_legal_two_sentences(self, segment: SegmentationFunc):
        """Two legal sentences — split at the natural boundary."""
        text = "The court found in favour of the claimant per sec. 12. An appeal was lodged immediately."
        assert segment(text) == ["The court found in favour of the claimant per sec. 12.", "An appeal was lodged immediately."]

    def test_correct_split_business_two_sentences(self, segment: SegmentationFunc):
        """Two business sentences — split at the natural boundary."""
        text = "Mr. Hopkins will chair the meeting. Ms. Reyes will take minutes."
        assert segment(text) == ["Mr. Hopkins will chair the meeting.", "Ms. Reyes will take minutes."]

    def test_correct_split_geographic_two_sentences(self, segment: SegmentationFunc):
        """Geographic reference then second sentence splits correctly."""
        text = "The summit of Mt. McKinley was reached at noon. The descent began an hour later."
        assert segment(text) == ["The summit of Mt. McKinley was reached at noon.", "The descent began an hour later."]

    def test_correct_split_cf_before_four_more_sentences(self, segment: SegmentationFunc):
        """cf. in a first sentence followed by three more sentences."""
        text = "For context, cf. Chapter 2. The background is complex. Several schools of thought exist. They will each be examined."
        assert segment(text) == ["For context, cf. Chapter 2.", "The background is complex.", "Several schools of thought exist.", "They will each be examined."]

    def test_correct_split_et_al_then_two_more_sentences(self, segment: SegmentationFunc):
        """et al. in first, then two more sentences."""
        text = "The approach was first used by Park et al. 2015. It was later refined. Current practice follows the refined version."
        assert segment(text) == ["The approach was first used by Park et al. 2015.", "It was later refined.", "Current practice follows the refined version."]

    # ---------------------------------------- Additional edge / domain tests --

    def test_eg_in_educational_instruction(self, segment: SegmentationFunc):
        """e.g. in an educational instruction sentence."""
        text = "Students should cite primary sources, e.g. Shakespeare's First Folio or Hobbes's Leviathan."
        assert segment(text) == ["Students should cite primary sources, e.g. Shakespeare's First Folio or Hobbes's Leviathan."]

    def test_ie_in_syllabus_clarification(self, segment: SegmentationFunc):
        """i.e. in a syllabus clarification sentence."""
        text = "Late submissions, i.e. anything after midnight Friday, will not be accepted."
        assert segment(text) == ["Late submissions, i.e. anything after midnight Friday, will not be accepted."]

    def test_cf_in_bibliography_comment(self, segment: SegmentationFunc):
        """cf. used in a bibliography annotation comment."""
        text = "For a more recent account cf. Henderson 2022, which revises the earlier chronology."
        assert segment(text) == ["For a more recent account cf. Henderson 2022, which revises the earlier chronology."]

    def test_canvas_lms_cf_before_module_number(self, segment: SegmentationFunc):
        """cf. before a module number on a Canvas page."""
        text = "For the preparatory material refer to cf. Module 3 Introduction."
        assert segment(text) == ["For the preparatory material refer to cf. Module 3 Introduction."]

    def test_legal_vol_in_law_reports(self, segment: SegmentationFunc):
        """vol. in a law report citation — must not split."""
        text = "The case is reported at [2003] vol. 1 AC 15."
        assert segment(text) == ['The case is reported at [2003] vol. 1 AC 15.']

    def test_medical_pp_in_clinical_guideline(self, segment: SegmentationFunc):
        """pp. in a clinical guideline page reference."""
        text = "The dosing tables are reproduced from the BNF, pp. 234-238."
        assert segment(text) == ["The dosing tables are reproduced from the BNF, pp. 234-238."]

    def test_scientific_no_in_catalog(self, segment: SegmentationFunc):
        """no. in a scientific catalogue number."""
        text = "The specimen is catalogued as no. NH-34872 in the Natural History Museum collection."
        assert segment(text) == ["The specimen is catalogued as no. NH-34872 in the Natural History Museum collection."]

    def test_news_pres_at_sentence_end_split(self, segment: SegmentationFunc):
        """Pres. before surname — splits at real sentence boundary after surname."""
        text = "The veto was cast by Pres. Carter. Congress overrode it the same week."
        assert segment(text) == ['The veto was cast by Pres. Carter.', 'Congress overrode it the same week.']

    def test_edge_cf_before_roman_numeral(self, segment: SegmentationFunc):
        """cf. before a Roman numeral — should not split."""
        text = "The technique is described, cf. Appendix IV, and demonstrated in the video."
        assert segment(text) == ["The technique is described, cf. Appendix IV, and demonstrated in the video."]

    def test_edge_ms_before_quoted_text(self, segment: SegmentationFunc):
        """Ms. before a name followed by a quoted statement."""
        text = "Ms. Park stated, 'The deadline has been extended to the end of the month'."
        assert segment(text) == ["Ms. Park stated, 'The deadline has been extended to the end of the month'."]
