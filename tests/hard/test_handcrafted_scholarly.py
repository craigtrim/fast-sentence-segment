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


class TestHandcraftedScholarly:
    """Hand-crafted tests for Latin and scholarly abbreviations."""

    @pytest.fixture
    def segment(self):
        """Provide the segmentation function for tests."""
        from fast_sentence_segment import segment_text
        def _segment(text):
            return segment_text(text, flatten=True, split_dialog=False)
        return _segment

    # ------------------------------------------------------------------ cf. --

    def test_cf_canvas_lms_cross_reference(self, segment: SegmentationFunc):
        """cf. in Canvas LMS cross-reference boilerplate — the exact motivating case for issue #47.

        Note: The pipeline appends a period to input text that lacks terminal punctuation
        (SpacyDocSegmenter behaviour), so the output includes a trailing period even though
        the input did not.  The key requirement is that the text is returned as a SINGLE
        sentence without a false split at the cf. boundary.
        """
        text = "Readings as listed on this overview page: cf. Week 1 Overview"
        assert segment(text) == ["Readings as listed on this overview page: cf. Week 1 Overview."]

    def test_cf_after_semicolon(self, segment: SegmentationFunc):
        """cf. following a semicolon should not split."""
        text = "The first approach failed; cf. Method B for a working alternative."
        assert segment(text) == ["The first approach failed; cf. Method B for a working alternative."]

    def test_cf_followed_by_week_number(self, segment: SegmentationFunc):
        """cf. Week N pattern — the exact pattern from issue #47."""
        text = "For prior material cf. Week 7 Overview in the course portal."
        assert segment(text) == ["For prior material cf. Week 7 Overview in the course portal."]

    def test_cf_after_colon_with_chapter(self, segment: SegmentationFunc):
        """cf. after colon introducing a chapter reference."""
        text = "For more detail on this topic: cf. Chapter 3 of the handbook."
        assert segment(text) == ["For more detail on this topic: cf. Chapter 3 of the handbook."]

    def test_cf_sentence_initial_before_proper_noun(self, segment: SegmentationFunc):
        """cf. at sentence start before a proper noun."""
        text = "cf. Aristotle, Nicomachean Ethics, Book II for a contrasting view."
        assert segment(text) == ["cf. Aristotle, Nicomachean Ethics, Book II for a contrasting view."]

    def test_cf_mid_clause_before_author_name(self, segment: SegmentationFunc):
        """cf. mid-clause before an author surname."""
        text = "The argument has been contested by many scholars, cf. Thompson 2018, and remains open."
        assert segment(text) == ["The argument has been contested by many scholars, cf. Thompson 2018, and remains open."]

    def test_cf_after_em_dash(self, segment: SegmentationFunc):
        """cf. after an em dash should not split."""
        text = "The evidence is compelling — cf. Appendix A for the full dataset."
        assert segment(text) == ["The evidence is compelling — cf. Appendix A for the full dataset."]

    def test_cf_in_parenthetical_aside(self, segment: SegmentationFunc):
        """cf. inside parentheses should not split."""
        text = "The mechanism (cf. Figure 4) operates through enzymatic cleavage."
        assert segment(text) == ["The mechanism (cf. Figure 4) operates through enzymatic cleavage."]

    def test_cf_with_page_number(self, segment: SegmentationFunc):
        """cf. followed by a page number should not split."""
        text = "This aligns with the established protocol, cf. p. 47 of the guidelines."
        assert segment(text) == ["This aligns with the established protocol, cf. p. 47 of the guidelines."]

    def test_cf_with_section_reference(self, segment: SegmentationFunc):
        """cf. followed by a section reference."""
        text = "The definition differs slightly here; cf. Section 2.3 above."
        assert segment(text) == ["The definition differs slightly here; cf. Section 2.3 above."]

    def test_cf_with_proper_noun_place(self, segment: SegmentationFunc):
        """cf. before a proper noun place name."""
        text = "A similar effect has been observed elsewhere, cf. Rome Declaration 2003."
        assert segment(text) == ["A similar effect has been observed elsewhere, cf. Rome Declaration 2003."]

    def test_cf_in_footnote_context(self, segment: SegmentationFunc):
        """cf. in a footnote-style reference fragment."""
        text = "cf. Green 2010, p. 88 for an opposing interpretation of these findings."
        assert segment(text) == ["cf. Green 2010, p. 88 for an opposing interpretation of these findings."]

    def test_cf_in_bibliography_entry(self, segment: SegmentationFunc):
        """cf. appearing in a bibliography entry."""
        text = "For secondary literature cf. Williams, The Modern Essay, Oxford 2005."
        assert segment(text) == ["For secondary literature cf. Williams, The Modern Essay, Oxford 2005."]

    def test_cf_before_table_reference(self, segment: SegmentationFunc):
        """cf. before a Table reference."""
        text = "The frequency distribution differs; cf. Table 2 for the breakdown by cohort."
        assert segment(text) == ["The frequency distribution differs; cf. Table 2 for the breakdown by cohort."]

    def test_cf_with_endnote_reference(self, segment: SegmentationFunc):
        """cf. in endnote running text."""
        text = "cf. Note 14 in the original edition for a fuller discussion of this point."
        assert segment(text) == ["cf. Note 14 in the original edition for a fuller discussion of this point."]

    def test_cf_split_across_two_sentences(self, segment: SegmentationFunc):
        """Two sentences where cf. belongs to the first — split must occur at the full stop."""
        text = "This is a point worth noting, cf. Smith 2010. The next chapter addresses the implications."
        assert segment(text) == ["This is a point worth noting, cf. Smith 2010.", "The next chapter addresses the implications."]

    def test_cf_after_comma_before_year(self, segment: SegmentationFunc):
        """cf. after comma before a four-digit year."""
        text = "The methodology was adapted, cf. 2017 revision of the standards."
        assert segment(text) == ["The methodology was adapted, cf. 2017 revision of the standards."]

    def test_cf_after_colon_before_author(self, segment: SegmentationFunc):
        """cf. after colon before an author name."""
        text = "See related discussions: cf. Miller on the sociological implications."
        assert segment(text) == ["See related discussions: cf. Miller on the sociological implications."]

    def test_cf_two_abbreviations_same_sentence(self, segment: SegmentationFunc):
        """cf. and ibid. in the same sentence."""
        text = "cf. ibid. p. 23 for the original formulation of this concept."
        assert segment(text) == ["cf. ibid. p. 23 for the original formulation of this concept."]

    # ---------------------------------------------------------------- et al. --

    def test_et_al_before_year(self, segment: SegmentationFunc):
        """et al. before a year in an inline citation."""
        text = "This was confirmed by Smith et al. 2019 in a landmark study."
        assert segment(text) == ["This was confirmed by Smith et al. 2019 in a landmark study."]

    def test_et_al_with_comma_after(self, segment: SegmentationFunc):
        """et al., with trailing comma — common in APA citations."""
        text = "According to Jones et al., 2021, the results were significant."
        assert segment(text) == ["According to Jones et al., 2021, the results were significant."]

    def test_et_al_before_parenthetical_year(self, segment: SegmentationFunc):
        """et al. before parenthetical year — APA in-text."""
        text = "The study by Brown et al. (2020) confirmed the earlier findings."
        assert segment(text) == ["The study by Brown et al. (2020) confirmed the earlier findings."]

    def test_et_al_at_end_of_sentence(self, segment: SegmentationFunc):
        """et al. at sentence end — should trigger a split before the next sentence."""
        text = "This was demonstrated by Zhang et al. The methodology is outlined in Section 3."
        assert segment(text) == ["This was demonstrated by Zhang et al.", "The methodology is outlined in Section 3."]

    def test_et_al_in_parenthetical_citation(self, segment: SegmentationFunc):
        """et al. inside a parenthetical citation block."""
        text = "Several studies support this view (Garcia et al. 2018; Huang et al. 2020)."
        assert segment(text) == ["Several studies support this view (Garcia et al. 2018; Huang et al. 2020)."]

    def test_et_al_before_comma_and_page(self, segment: SegmentationFunc):
        """et al. followed by comma and page citation."""
        text = "As noted by Davis et al., pp. 112-115, the trend is consistent."
        assert segment(text) == ["As noted by Davis et al., pp. 112-115, the trend is consistent."]

    def test_et_al_beginning_of_sentence(self, segment: SegmentationFunc):
        """et al. following subject at start of sentence."""
        text = "Wilson et al. concluded that the intervention had no measurable effect."
        assert segment(text) == ["Wilson et al. concluded that the intervention had no measurable effect."]

    def test_et_al_with_volume_and_page(self, segment: SegmentationFunc):
        """et al. with vol. and pp. all in one reference fragment."""
        text = "See Kim et al. vol. 8, pp. 301-320 for experimental details."
        assert segment(text) == ["See Kim et al. vol. 8, pp. 301-320 for experimental details."]

    def test_et_al_two_citations_semicolon(self, segment: SegmentationFunc):
        """Two et al. citations separated by semicolon."""
        text = "Prior work (Lee et al. 2015; Park et al. 2017) established the baseline."
        assert segment(text) == ["Prior work (Lee et al. 2015; Park et al. 2017) established the baseline."]

    def test_et_al_in_running_text_before_capital(self, segment: SegmentationFunc):
        """et al. in running text where next word is a capitalized noun."""
        text = "The paper by Evans et al. Showed that early intervention was effective."
        assert segment(text) == ["The paper by Evans et al. Showed that early intervention was effective."]

    def test_et_al_preceded_by_and(self, segment: SegmentationFunc):
        """et al. in a compound author list with 'and'."""
        text = "The review by Adams, Baker, and Carter et al. spans three decades of research."
        assert segment(text) == ["The review by Adams, Baker, and Carter et al. spans three decades of research."]

    def test_et_al_followed_by_wrote(self, segment: SegmentationFunc):
        """et al. followed by a verb in running prose."""
        text = "Singh et al. wrote the definitive treatment of this subject in 2003."
        assert segment(text) == ["Singh et al. wrote the definitive treatment of this subject in 2003."]

    def test_et_al_with_ibid_follow(self, segment: SegmentationFunc):
        """et al. citation followed by ibid. reference."""
        text = "Rodriguez et al. 2014, p. 5; ibid. p. 12 for the counter-argument."
        assert segment(text) == ["Rodriguez et al. 2014, p. 5; ibid. p. 12 for the counter-argument."]

    def test_et_al_in_footnote_with_page(self, segment: SegmentationFunc):
        """et al. in a footnote fragment with page number."""
        text = "Cf. Jackson et al. 2009, p. 88 for a more detailed treatment."
        assert segment(text) == ["Cf. Jackson et al. 2009, p. 88 for a more detailed treatment."]

    def test_et_al_before_dash_and_rest(self, segment: SegmentationFunc):
        """et al. before an em-dash continuation."""
        text = "The findings of Harris et al. — replicated in 2022 — are now considered canonical."
        assert segment(text) == ["The findings of Harris et al. — replicated in 2022 — are now considered canonical."]

    def test_et_al_two_sentences_split(self, segment: SegmentationFunc):
        """Proper split when full sentence follows et al. fragment."""
        text = "Refer to Clark et al. for the complete data. This study extends their work."
        assert segment(text) == ["Refer to Clark et al. for the complete data.", "This study extends their work."]

    # ----------------------------------------------------------------- viz. --

    def test_viz_introduces_example(self, segment: SegmentationFunc):
        """viz. introducing a specific example should not split."""
        text = "Three species were identified, viz. Homo sapiens, Pan troglodytes, and Gorilla gorilla."
        assert segment(text) == ["Three species were identified, viz. Homo sapiens, Pan troglodytes, and Gorilla gorilla."]

    def test_viz_after_colon_before_proper_noun(self, segment: SegmentationFunc):
        """viz. after a colon before a proper noun."""
        text = "The solution has one name: viz. Hegel's dialectic of recognition."
        assert segment(text) == ["The solution has one name: viz. Hegel's dialectic of recognition."]

    def test_viz_in_legal_definition(self, segment: SegmentationFunc):
        """viz. used in a legal definition clause."""
        text = "The parties to this agreement, viz. the Licensor and the Licensee, agree as follows."
        assert segment(text) == ["The parties to this agreement, viz. the Licensor and the Licensee, agree as follows."]

    def test_viz_in_philosophy_text(self, segment: SegmentationFunc):
        """viz. in a philosophical argument introducing a term."""
        text = "There is one concept that unifies these observations, viz. the notion of intentionality."
        assert segment(text) == ["There is one concept that unifies these observations, viz. the notion of intentionality."]

    def test_viz_mid_sentence_before_list(self, segment: SegmentationFunc):
        """viz. mid-sentence introducing an enumeration."""
        text = "Two factors matter, viz. timing and scale, and both must be addressed."
        assert segment(text) == ["Two factors matter, viz. timing and scale, and both must be addressed."]

    def test_viz_after_semicolon(self, segment: SegmentationFunc):
        """viz. following a semicolon."""
        text = "Only one variable was manipulated; viz. the concentration of the reagent."
        assert segment(text) == ["Only one variable was manipulated; viz. the concentration of the reagent."]

    def test_viz_sentence_initial(self, segment: SegmentationFunc):
        """viz. at the start of a sentence fragment."""
        text = "viz. the original manuscript, held at the British Library, contains the correction."
        assert segment(text) == ["viz. the original manuscript, held at the British Library, contains the correction."]

    def test_viz_with_cf_in_same_sentence(self, segment: SegmentationFunc):
        """viz. and cf. both in the same sentence."""
        text = "One principle dominates here, viz. proportionality, cf. Article 5 of the Charter."
        assert segment(text) == ["One principle dominates here, viz. proportionality, cf. Article 5 of the Charter."]

    def test_viz_introducing_proper_name(self, segment: SegmentationFunc):
        """viz. introducing a proper name."""
        text = "The founder of the discipline, viz. Saussure, established these distinctions."
        assert segment(text) == ["The founder of the discipline, viz. Saussure, established these distinctions."]

    def test_viz_followed_by_numeral(self, segment: SegmentationFunc):
        """viz. followed by a numeral."""
        text = "The dataset has exactly one outlier, viz. 1047, which skews the mean."
        assert segment(text) == ["The dataset has exactly one outlier, viz. 1047, which skews the mean."]

    def test_viz_two_sentences_boundary(self, segment: SegmentationFunc):
        """Sentence boundary after viz. clause — second sentence must split cleanly."""
        text = "One method works here, viz. gradient descent. The proof is given in the appendix."
        assert segment(text) == ["One method works here, viz. gradient descent.", "The proof is given in the appendix."]

    # ---------------------------------------------------------------- ibid. --

    def test_ibid_mid_footnote(self, segment: SegmentationFunc):
        """ibid. mid-footnote should not trigger a split."""
        text = "See ibid. Chapter 4 for the relevant passage."
        assert segment(text) == ["See ibid. Chapter 4 for the relevant passage."]

    def test_ibid_with_page_number(self, segment: SegmentationFunc):
        """ibid. followed by page number."""
        text = "The same argument appears in ibid. p. 78 of that edition."
        assert segment(text) == ["The same argument appears in ibid. p. 78 of that edition."]

    def test_ibid_sentence_initial(self, segment: SegmentationFunc):
        """ibid. at sentence start."""
        text = "ibid. p. 103 provides a clear restatement of the principle."
        assert segment(text) == ["ibid. p. 103 provides a clear restatement of the principle."]

    def test_ibid_in_parentheses(self, segment: SegmentationFunc):
        """ibid. inside parentheses."""
        text = "The claim is repeated almost verbatim (ibid. p. 34)."
        assert segment(text) == ["The claim is repeated almost verbatim (ibid. p. 34)."]

    def test_ibid_with_comma_and_page(self, segment: SegmentationFunc):
        """ibid., page format."""
        text = "The same wording appears in ibid., p. 199 without alteration."
        assert segment(text) == ["The same wording appears in ibid., p. 199 without alteration."]

    def test_ibid_after_semicolon(self, segment: SegmentationFunc):
        """ibid. after semicolon in a note — must not split."""
        text = "See Smith 2008, p. 12; ibid. pp. 45-46 for the extended argument."
        assert segment(text) == ["See Smith 2008, p. 12; ibid. pp. 45-46 for the extended argument."]

    def test_ibid_before_proper_noun(self, segment: SegmentationFunc):
        """ibid. before a proper noun — should not split."""
        text = "The passage echoes ibid. Plato's formulation of the Form of Good."
        assert segment(text) == ["The passage echoes ibid. Plato's formulation of the Form of Good."]

    def test_ibid_followed_by_volume(self, segment: SegmentationFunc):
        """ibid. followed by a volume reference."""
        text = "ibid. vol. 3, p. 22 covers the same ground from a different angle."
        assert segment(text) == ["ibid. vol. 3, p. 22 covers the same ground from a different angle."]

    def test_ibid_in_legal_footnote(self, segment: SegmentationFunc):
        """ibid. in a legal footnote context."""
        text = "See ibid. at 234-235 for the court's reasoning on the second ground."
        assert segment(text) == ["See ibid. at 234-235 for the court's reasoning on the second ground."]

    def test_ibid_followed_by_section(self, segment: SegmentationFunc):
        """ibid. followed by Section reference."""
        text = "ibid. Section 4.2 restates the key propositions in simpler terms."
        assert segment(text) == ["ibid. Section 4.2 restates the key propositions in simpler terms."]

    # --------------------------------------------------------------- op. cit. --

    def test_op_cit_basic(self, segment: SegmentationFunc):
        """op. cit. basic usage should not split."""
        text = "The same point is made in Smith, op. cit. p. 45."
        assert segment(text) == ["The same point is made in Smith, op. cit. p. 45."]

    def test_op_cit_after_author_name(self, segment: SegmentationFunc):
        """op. cit. after an author surname."""
        text = "As argued by Johnson, op. cit. the theory is incomplete."
        assert segment(text) == ["As argued by Johnson, op. cit. the theory is incomplete."]

    def test_op_cit_with_page_range(self, segment: SegmentationFunc):
        """op. cit. with a page range."""
        text = "See Williams, op. cit. pp. 112-118 for the relevant data."
        assert segment(text) == ["See Williams, op. cit. pp. 112-118 for the relevant data."]

    def test_op_cit_in_parentheses(self, segment: SegmentationFunc):
        """op. cit. inside parentheses."""
        text = "The finding is contested (Brown, op. cit. p. 9) by more recent scholarship."
        assert segment(text) == ["The finding is contested (Brown, op. cit. p. 9) by more recent scholarship."]

    def test_op_cit_sentence_initial(self, segment: SegmentationFunc):
        """op. cit. at sentence start."""
        text = "op. cit. Davis p. 67 argues for a more nuanced reading."
        assert segment(text) == ["op. cit. Davis p. 67 argues for a more nuanced reading."]

    def test_op_cit_after_semicolon(self, segment: SegmentationFunc):
        """op. cit. following a semicolon."""
        text = "For the earlier view see Harris 1998; op. cit. Martin p. 23 revises this."
        assert segment(text) == ["For the earlier view see Harris 1998; op. cit. Martin p. 23 revises this."]

    def test_op_cit_before_proper_noun(self, segment: SegmentationFunc):
        """op. cit. before a proper noun."""
        text = "Anderson, op. cit. London 1994 is the standard reference for this period."
        assert segment(text) == ["Anderson, op. cit. London 1994 is the standard reference for this period."]

    def test_op_cit_with_chapter_reference(self, segment: SegmentationFunc):
        """op. cit. with a chapter reference."""
        text = "See Thompson, op. cit. Chapter 5 for the full argument."
        assert segment(text) == ["See Thompson, op. cit. Chapter 5 for the full argument."]

    # --------------------------------------------------------------- loc. cit. --

    def test_loc_cit_basic(self, segment: SegmentationFunc):
        """loc. cit. basic usage in a footnote-style reference."""
        text = "The phrase was taken from Miller, loc. cit. p. 34."
        assert segment(text) == ["The phrase was taken from Miller, loc. cit. p. 34."]

    def test_loc_cit_in_running_text(self, segment: SegmentationFunc):
        """loc. cit. in running academic prose."""
        text = "As previously discussed in loc. cit. Section 2, the evidence supports this reading."
        assert segment(text) == ["As previously discussed in loc. cit. Section 2, the evidence supports this reading."]

    def test_loc_cit_after_semicolon(self, segment: SegmentationFunc):
        """loc. cit. following a semicolon."""
        text = "See Martin 2001; loc. cit. Taylor, for the broader context."
        assert segment(text) == ["See Martin 2001; loc. cit. Taylor, for the broader context."]

    def test_loc_cit_in_parentheses(self, segment: SegmentationFunc):
        """loc. cit. inside parentheses."""
        text = "This is confirmed (loc. cit. p. 199) by the author's own later work."
        assert segment(text) == ["This is confirmed (loc. cit. p. 199) by the author's own later work."]

    def test_loc_cit_before_proper_noun(self, segment: SegmentationFunc):
        """loc. cit. before a proper noun — should not split."""
        text = "loc. cit. Barnes argues this point with particular force."
        assert segment(text) == ["loc. cit. Barnes argues this point with particular force."]

    def test_loc_cit_with_volume_number(self, segment: SegmentationFunc):
        """loc. cit. with a volume number."""
        text = "See Mitchell, loc. cit. vol. 2, p. 55 for the fuller argument."
        assert segment(text) == ["See Mitchell, loc. cit. vol. 2, p. 55 for the fuller argument."]

    def test_loc_cit_sentence_end_followed_by_new(self, segment: SegmentationFunc):
        """Sentence ending after loc. cit. reference then a new sentence."""
        text = "The exact wording appears in loc. cit. Wilson. The next chapter reinterprets it."
        assert segment(text) == ["The exact wording appears in loc. cit. Wilson.", "The next chapter reinterprets it."]

    def test_loc_cit_with_page_range(self, segment: SegmentationFunc):
        """loc. cit. with a page range."""
        text = "loc. cit. Carter, pp. 77-82, provides the definitive account."
        assert segment(text) == ["loc. cit. Carter, pp. 77-82, provides the definitive account."]

    # ----------------------------------------------------------------- N.B. --

    def test_nb_at_sentence_start_before_proper(self, segment: SegmentationFunc):
        """N.B. at sentence start before a proper noun — should not split."""
        text = "N.B. This regulation applies only to European Union member states."
        assert segment(text) == ["N.B. This regulation applies only to European Union member states."]

    def test_nb_mid_sentence_after_comma(self, segment: SegmentationFunc):
        """N.B. mid-sentence after a comma."""
        text = "The form must be submitted in triplicate, N.B. all copies must be signed."
        assert segment(text) == ["The form must be submitted in triplicate, N.B. all copies must be signed."]

    def test_nb_in_parentheses(self, segment: SegmentationFunc):
        """N.B. inside parentheses."""
        text = "The deadline is strict (N.B. No extensions will be granted)."
        assert segment(text) == ["The deadline is strict (N.B. No extensions will be granted)."]

    def test_nb_lowercase_at_start(self, segment: SegmentationFunc):
        """n.b. lowercase variant at sentence start."""
        text = "n.b. The figures cited here are from the 2020 census."
        assert segment(text) == ["n.b. The figures cited here are from the 2020 census."]

    def test_nb_before_date(self, segment: SegmentationFunc):
        """N.B. before a date."""
        text = "N.B. January 2024 marks the effective date of the new policy."
        assert segment(text) == ["N.B. January 2024 marks the effective date of the new policy."]

    def test_nb_two_sentences(self, segment: SegmentationFunc):
        """N.B. note followed by a second full sentence — must split."""
        text = "N.B. This caveat applies to all cases. The main rule is stated above."
        assert segment(text) == ["N.B. This caveat applies to all cases.", "The main rule is stated above."]

    def test_nb_after_semicolon(self, segment: SegmentationFunc):
        """N.B. after a semicolon."""
        text = "Proceed with caution in all cases; N.B. Section 4.7 lists the exceptions."
        assert segment(text) == ["Proceed with caution in all cases; N.B. Section 4.7 lists the exceptions."]

    def test_nb_in_academic_paper_note(self, segment: SegmentationFunc):
        """N.B. in an academic paper marginal note."""
        text = "N.B. All translations from Greek are my own unless otherwise indicated."
        assert segment(text) == ["N.B. All translations from Greek are my own unless otherwise indicated."]

    # ----------------------------------------------------------------- sic. --

    def test_sic_in_square_brackets_mid_sentence(self, segment: SegmentationFunc):
        """[sic] mid-sentence inside brackets."""
        text = "The original states 'their [sic] is no alternative to this method'."
        assert segment(text) == ["The original states 'their [sic] is no alternative to this method'."]

    def test_sic_after_misspelling_mid_text(self, segment: SegmentationFunc):
        """sic. after a quoted misspelling in running text."""
        text = "The manuscript reads 'the kinge sic. commanded the troops to advance'."
        assert segment(text) == ["The manuscript reads 'the kinge sic. commanded the troops to advance'."]

    def test_sic_with_bracket_form_before_proper(self, segment: SegmentationFunc):
        """[sic.] bracket form before a proper noun."""
        text = "He wrote 'The United States [sic.] America leads in innovation'."
        assert segment(text) == ["He wrote 'The United States [sic.] America leads in innovation'."]

    def test_sic_at_end_of_quote_before_new_sentence(self, segment: SegmentationFunc):
        """[sic] at end of a quotation followed by new sentence."""
        text = "The author claims 'it was always their [sic] intention'. This is disputed."
        assert segment(text) == ["The author claims 'it was always their [sic] intention'.", "This is disputed."]

    def test_sic_in_academic_editing_context(self, segment: SegmentationFunc):
        """sic. used in an editorial context."""
        text = "The letter reads: 'I done sic. everything in my power to prevent it'."
        assert segment(text) == ["The letter reads: 'I done sic. everything in my power to prevent it'."]

    def test_sic_surrounded_by_parentheses(self, segment: SegmentationFunc):
        """(sic) surrounded by parentheses in prose."""
        text = "The report states that results were 'unambigiously (sic) positive'."
        assert segment(text) == ["The report states that results were 'unambigiously (sic) positive'."]

    def test_sic_in_historical_document_transcription(self, segment: SegmentationFunc):
        """sic. in transcription of historical document."""
        text = "The charter reads: 'All persones sic. within the bounds of the citie shall obey'."
        assert segment(text) == ["The charter reads: 'All persones sic. within the bounds of the citie shall obey'."]

    def test_sic_before_comma(self, segment: SegmentationFunc):
        """sic. before a comma in a citation."""
        text = "He described it as 'a beautifull sic., luminous landscape'."
        assert segment(text) == ["He described it as 'a beautifull sic., luminous landscape'."]

    # ----------------------------------------------------------- ca. / c. (circa) --

    def test_ca_before_year(self, segment: SegmentationFunc):
        """ca. (circa) before a year should not split."""
        text = "The mosaic dates to ca. 300 CE, during the late Roman period."
        assert segment(text) == ["The mosaic dates to ca. 300 CE, during the late Roman period."]

    def test_c_circa_before_year(self, segment: SegmentationFunc):
        """c. (circa) before a year in historical writing."""
        text = "The text was composed c. 1450 in the scriptorium at Monte Cassino."
        assert segment(text) == ["The text was composed c. 1450 in the scriptorium at Monte Cassino."]

    def test_ca_before_decade(self, segment: SegmentationFunc):
        """ca. before a decade reference."""
        text = "The tradition flourished ca. 1800s in central Europe."
        assert segment(text) == ["The tradition flourished ca. 1800s in central Europe."]

    def test_ca_in_art_history_caption(self, segment: SegmentationFunc):
        """ca. in an art history caption or note."""
        text = "Portrait of a Lady, oil on canvas, ca. 1720, artist unknown."
        assert segment(text) == ["Portrait of a Lady, oil on canvas, ca. 1720, artist unknown."]

    def test_c_before_proper_noun_century(self, segment: SegmentationFunc):
        """c. before a proper noun that starts a century description."""
        text = "The technique was developed c. Renaissance Italy and spread northward."
        assert segment(text) == ["The technique was developed c. Renaissance Italy and spread northward."]

    def test_ca_sentence_initial(self, segment: SegmentationFunc):
        """ca. at sentence start."""
        text = "ca. 4000 BCE, the first writing systems appeared in Mesopotamia."
        assert segment(text) == ["ca. 4000 BCE, the first writing systems appeared in Mesopotamia."]

    def test_ca_in_parentheses(self, segment: SegmentationFunc):
        """ca. inside parentheses."""
        text = "The instrument (ca. 1680, by Stradivari) is housed in Vienna."
        assert segment(text) == ["The instrument (ca. 1680, by Stradivari) is housed in Vienna."]

    def test_c_before_date_range(self, segment: SegmentationFunc):
        """c. before a date range."""
        text = "The dynasty ruled c. 206 BCE – 220 CE, a span of four centuries."
        assert segment(text) == ["The dynasty ruled c. 206 BCE – 220 CE, a span of four centuries."]

    # ----------------------------------------------------------------- vol. --

    def test_vol_before_arabic_numeral(self, segment: SegmentationFunc):
        """vol. followed by an Arabic numeral — must not split."""
        text = "The study appears in vol. 12 of the journal."
        assert segment(text) == ["The study appears in vol. 12 of the journal."]

    def test_vol_before_roman_numeral(self, segment: SegmentationFunc):
        """vol. followed by a Roman numeral — must not split."""
        text = "See vol. III of the collected works for the correspondence."
        assert segment(text) == ["See vol. III of the collected works for the correspondence."]

    def test_vol_with_no_citation(self, segment: SegmentationFunc):
        """vol. and no. in the same citation reference."""
        text = "Published in vol. 5, no. 2 of Linguistic Inquiry."
        assert segment(text) == ["Published in vol. 5, no. 2 of Linguistic Inquiry."]

    def test_vol_in_bibliography_entry(self, segment: SegmentationFunc):
        """vol. in a bibliography entry."""
        text = "The Collected Works of John Stuart Mill, vol. 4, Toronto 1967."
        assert segment(text) == ["The Collected Works of John Stuart Mill, vol. 4, Toronto 1967."]

    def test_vol_after_et_al_citation(self, segment: SegmentationFunc):
        """vol. following an et al. citation."""
        text = "See Brown et al. vol. 7 for the experimental protocol."
        assert segment(text) == ["See Brown et al. vol. 7 for the experimental protocol."]

    def test_vol_at_sentence_start(self, segment: SegmentationFunc):
        """vol. at the start of a reference sentence — must not split."""
        text = "vol. 2 of this series has been translated into twelve languages."
        assert segment(text) == ["vol. 2 of this series has been translated into twelve languages."]

    def test_vol_before_page_range(self, segment: SegmentationFunc):
        """vol. combined with pp. in a complete citation — must not split."""
        text = "The paper appears in vol. 18, pp. 234-256 of the proceedings."
        assert segment(text) == ["The paper appears in vol. 18, pp. 234-256 of the proceedings."]

    def test_vol_in_parenthetical_citation(self, segment: SegmentationFunc):
        """vol. inside a parenthetical citation."""
        text = "This argument has been contested (Miller, vol. 3, p. 98)."
        assert segment(text) == ["This argument has been contested (Miller, vol. 3, p. 98)."]

    def test_vol_two_sentences_split(self, segment: SegmentationFunc):
        """vol. in first sentence — must not split within sentence, splits at sentence boundary."""
        text = "The data is in vol. 2 of the atlas. The methodology is in vol. 3."
        assert segment(text) == ["The data is in vol. 2 of the atlas.", "The methodology is in vol. 3."]

    def test_vol_with_caps_after(self, segment: SegmentationFunc):
        """vol. followed by a capitalized proper noun title — must not split."""
        text = "See the discussion in vol. Annals of Science, issue 14."
        assert segment(text) == ["See the discussion in vol. Annals of Science, issue 14."]

    # ------------------------------------------------------------------ p. --

    def test_p_single_page_citation(self, segment: SegmentationFunc):
        """p. single page reference should not split."""
        text = "The argument is restated on p. 77 of the revised edition."
        assert segment(text) == ["The argument is restated on p. 77 of the revised edition."]

    def test_p_after_comma_in_apa_citation(self, segment: SegmentationFunc):
        """p. after comma in APA-style parenthetical citation."""
        text = "The claim appears to be overstated (Johnson, 2019, p. 112)."
        assert segment(text) == ["The claim appears to be overstated (Johnson, 2019, p. 112)."]

    def test_p_at_start_of_footnote(self, segment: SegmentationFunc):
        """p. at start of a footnote fragment."""
        text = "p. 34 provides the earliest attestation of this usage."
        assert segment(text) == ["p. 34 provides the earliest attestation of this usage."]

    def test_p_before_roman_numeral(self, segment: SegmentationFunc):
        """p. before a Roman numeral page number."""
        text = "The preface begins on p. xii of the 1989 edition."
        assert segment(text) == ["The preface begins on p. xii of the 1989 edition."]

    def test_p_with_ibid_context(self, segment: SegmentationFunc):
        """p. following ibid. reference."""
        text = "ibid. p. 203 confirms the same pattern in the western data."
        assert segment(text) == ["ibid. p. 203 confirms the same pattern in the western data."]

    def test_p_followed_by_proper_noun(self, segment: SegmentationFunc):
        """p. followed by a proper noun — should not split."""
        text = "The passage on p. Rome's founding myth is especially revealing."
        assert segment(text) == ["The passage on p. Rome's founding myth is especially revealing."]

    def test_p_in_multilingual_context(self, segment: SegmentationFunc):
        """p. in a multilingual reference string."""
        text = "See also Garcia 2001, p. 15, for the Spanish-language perspective."
        assert segment(text) == ["See also Garcia 2001, p. 15, for the Spanish-language perspective."]

    def test_p_two_sentences_correct_split(self, segment: SegmentationFunc):
        """Two sentences with p. in first — split must occur at period after complete sentence."""
        text = "The formula appears on p. 45 in the standard reference. All subsequent authors cite this page."
        assert segment(text) == ["The formula appears on p. 45 in the standard reference.", "All subsequent authors cite this page."]

    # ----------------------------------------------------------------- pp. --

    def test_pp_range_in_citation(self, segment: SegmentationFunc):
        """pp. in a page range citation — must not split."""
        text = "The argument is developed on pp. 34–56 of the monograph."
        assert segment(text) == ["The argument is developed on pp. 34–56 of the monograph."]

    def test_pp_in_parenthetical_apa(self, segment: SegmentationFunc):
        """pp. in a parenthetical APA-style citation."""
        text = "This interpretation is challenged by others (Davis, 2020, pp. 88-91)."
        assert segment(text) == ["This interpretation is challenged by others (Davis, 2020, pp. 88-91)."]

    def test_pp_before_roman_numeral_range(self, segment: SegmentationFunc):
        """pp. before a Roman numeral range — must not split."""
        text = "The introduction spans pp. i-xxiv and is essential reading."
        assert segment(text) == ["The introduction spans pp. i-xxiv and is essential reading."]

    def test_pp_in_mla_citation(self, segment: SegmentationFunc):
        """pp. in an MLA-style citation fragment."""
        text = "Smith, John. The Long Arc. New York: Penguin, 2019. pp. 44-67."
        assert segment(text) == ["Smith, John. The Long Arc. New York: Penguin, 2019. pp. 44-67."]

    def test_pp_followed_by_proper_noun(self, segment: SegmentationFunc):
        """pp. followed by a proper-noun title — must not split."""
        text = "The comparison is drawn on pp. Table 3 of the supplementary materials."
        assert segment(text) == ["The comparison is drawn on pp. Table 3 of the supplementary materials."]

    def test_pp_with_et_al_citation(self, segment: SegmentationFunc):
        """pp. in a citation that also includes et al."""
        text = "See Thompson et al. pp. 201-215 for the experimental data."
        assert segment(text) == ["See Thompson et al. pp. 201-215 for the experimental data."]

    def test_pp_two_references_in_sequence(self, segment: SegmentationFunc):
        """Two pp. references in the same sentence."""
        text = "The claim appears on pp. 12-15 and is elaborated on pp. 67-72."
        assert segment(text) == ["The claim appears on pp. 12-15 and is elaborated on pp. 67-72."]

    def test_pp_followed_by_year_after_split(self, segment: SegmentationFunc):
        """pp. at end of a citation clause followed by a new sentence."""
        text = "The definition is given on pp. 5-6. The second chapter extends this."
        assert segment(text) == ["The definition is given on pp. 5-6.", "The second chapter extends this."]

    def test_pp_before_arabic_with_dash(self, segment: SegmentationFunc):
        """pp. with hyphenated page range — must not split."""
        text = "The relevant section occupies pp. 102-130 of the volume."
        assert segment(text) == ["The relevant section occupies pp. 102-130 of the volume."]

    def test_pp_sentence_initial(self, segment: SegmentationFunc):
        """pp. at sentence start — must not split."""
        text = "pp. 45-78 contain the most detailed exposition of the theory."
        assert segment(text) == ["pp. 45-78 contain the most detailed exposition of the theory."]

    # ----------------------------------------------------------------- no. --

    def test_no_before_arabic_numeral(self, segment: SegmentationFunc):
        """no. followed by an Arabic numeral — should not split."""
        text = "Published in vol. 5, no. 3 of the European Journal of Linguistics."
        assert segment(text) == ["Published in vol. 5, no. 3 of the European Journal of Linguistics."]

    def test_no_in_legal_case_number(self, segment: SegmentationFunc):
        """no. in a legal case number."""
        text = "The case, no. 19-CV-0014, was filed in the Southern District."
        assert segment(text) == ["The case, no. 19-CV-0014, was filed in the Southern District."]

    def test_no_in_patent_reference(self, segment: SegmentationFunc):
        """no. in a patent reference."""
        text = "The invention is described in US Patent no. 7,891,234."
        assert segment(text) == ["The invention is described in US Patent no. 7,891,234."]

    def test_no_followed_by_proper_noun(self, segment: SegmentationFunc):
        """no. followed by a proper noun — must not split."""
        text = "Entry no. Alpha remains unclassified in the current taxonomy."
        assert segment(text) == ["Entry no. Alpha remains unclassified in the current taxonomy."]

    def test_no_in_orchestra_program_note(self, segment: SegmentationFunc):
        """no. in an orchestra program note."""
        text = "Beethoven's Symphony no. 9 was premiered in Vienna in 1824."
        assert segment(text) == ["Beethoven's Symphony no. 9 was premiered in Vienna in 1824."]

    def test_no_sentence_initial(self, segment: SegmentationFunc):
        """no. at start of a sentence fragment."""
        text = "no. 42 on the list corresponds to the highest-scoring entry."
        assert segment(text) == ["no. 42 on the list corresponds to the highest-scoring entry."]

    def test_no_two_sentences_split(self, segment: SegmentationFunc):
        """no. in first sentence, second sentence splits correctly."""
        text = "The journal issue is no. 4 of this year's volume. It features three major papers."
        assert segment(text) == ["The journal issue is no. 4 of this year's volume.", "It features three major papers."]

    def test_no_before_roman_numeral(self, segment: SegmentationFunc):
        """no. before a Roman numeral identifier — must not split."""
        text = "Entry no. XIV in the register contains the original deed."
        assert segment(text) == ["Entry no. XIV in the register contains the original deed."]

    def test_no_in_academic_series(self, segment: SegmentationFunc):
        """no. in an academic series reference."""
        text = "The volume belongs to Series B, no. 7, of the monograph series."
        assert segment(text) == ["The volume belongs to Series B, no. 7, of the monograph series."]

    def test_no_caps_form_before_numeral(self, segment: SegmentationFunc):
        """No. capitalized before a numeral."""
        text = "Case No. 1042 was transferred to the appellate division."
        assert segment(text) == ["Case No. 1042 was transferred to the appellate division."]

    # ----------------------------------------------------------------- fig. --

    def test_fig_before_number_mid_sentence(self, segment: SegmentationFunc):
        """fig. before a number mid-sentence."""
        text = "The data plotted in fig. 3 confirms the hypothesis."
        assert segment(text) == ["The data plotted in fig. 3 confirms the hypothesis."]

    def test_fig_before_decimal_reference(self, segment: SegmentationFunc):
        """fig. before a decimal figure reference — must not split."""
        text = "As illustrated in fig. 2.4, the curve reaches a plateau."
        assert segment(text) == ["As illustrated in fig. 2.4, the curve reaches a plateau."]

    def test_fig_sentence_initial(self, segment: SegmentationFunc):
        """fig. at start of a caption-like sentence — must not split."""
        text = "fig. 1 shows the overall distribution of the data."
        assert segment(text) == ["fig. 1 shows the overall distribution of the data."]

    def test_fig_in_parenthetical(self, segment: SegmentationFunc):
        """fig. inside parentheses."""
        text = "The structure is well-preserved (fig. 4a) and shows clear layering."
        assert segment(text) == ["The structure is well-preserved (fig. 4a) and shows clear layering."]

    def test_fig_caps_before_proper(self, segment: SegmentationFunc):
        """Fig. capitalized before a reference — must not split."""
        text = "Fig. A1 in the appendix provides additional supporting data."
        assert segment(text) == ["Fig. A1 in the appendix provides additional supporting data."]

    def test_fig_with_cf_in_same_sentence(self, segment: SegmentationFunc):
        """fig. with cf. in the same sentence — must not split."""
        text = "cf. fig. 3 for the schematic diagram of the apparatus."
        assert segment(text) == ["cf. fig. 3 for the schematic diagram of the apparatus."]

    def test_fig_two_sentences_split(self, segment: SegmentationFunc):
        """fig. reference followed by second sentence — split at natural boundary."""
        text = "The results are summarised in fig. 5. This supports the main hypothesis."
        assert segment(text) == ["The results are summarised in fig. 5.", "This supports the main hypothesis."]

    def test_fig_before_letter_label(self, segment: SegmentationFunc):
        """fig. before a letter label (fig. A, fig. B) — must not split."""
        text = "The process is shown in fig. B and described in the text below."
        assert segment(text) == ["The process is shown in fig. B and described in the text below."]

    # ----------------------------------------------------------------- ch. --

    def test_ch_before_numeral(self, segment: SegmentationFunc):
        """ch. before a numeral — should not split."""
        text = "The concept is introduced in ch. 3 and elaborated in ch. 5."
        assert segment(text) == ["The concept is introduced in ch. 3 and elaborated in ch. 5."]

    def test_ch_at_sentence_start(self, segment: SegmentationFunc):
        """ch. at start of a reference sentence."""
        text = "ch. 7 examines the long-term consequences of this policy."
        assert segment(text) == ["ch. 7 examines the long-term consequences of this policy."]

    def test_ch_in_parenthetical(self, segment: SegmentationFunc):
        """ch. inside a parenthetical aside."""
        text = "This point (ch. 2) is developed further in later sections."
        assert segment(text) == ["This point (ch. 2) is developed further in later sections."]

    def test_ch_before_roman_numeral(self, segment: SegmentationFunc):
        """ch. before a Roman numeral chapter reference — must not split."""
        text = "See ch. IV for the discussion of primary sources."
        assert segment(text) == ["See ch. IV for the discussion of primary sources."]

    def test_ch_followed_by_proper_noun(self, segment: SegmentationFunc):
        """ch. followed by a proper noun title — must not split."""
        text = "The topic is covered in ch. Methodology and its subsections."
        assert segment(text) == ["The topic is covered in ch. Methodology and its subsections."]

    def test_ch_two_sentences_split(self, segment: SegmentationFunc):
        """ch. reference followed by a second sentence."""
        text = "The argument is set out in ch. 1. The evidence is assessed in ch. 2."
        assert segment(text) == ["The argument is set out in ch. 1.", "The evidence is assessed in ch. 2."]

    # ---------------------------------------------------------------- sec. --

    def test_sec_before_number(self, segment: SegmentationFunc):
        """sec. before a section number — must not split."""
        text = "The requirement is stated in sec. 4.2 of the standard."
        assert segment(text) == ["The requirement is stated in sec. 4.2 of the standard."]

    def test_sec_at_sentence_start(self, segment: SegmentationFunc):
        """sec. at sentence start before a numeral."""
        text = "sec. 3 outlines the theoretical framework for the analysis."
        assert segment(text) == ["sec. 3 outlines the theoretical framework for the analysis."]

    def test_sec_in_legal_citation(self, segment: SegmentationFunc):
        """sec. in a legal statute citation."""
        text = "The offence is defined under sec. 12(3) of the Criminal Code."
        assert segment(text) == ["The offence is defined under sec. 12(3) of the Criminal Code."]

    def test_sec_in_parentheses(self, segment: SegmentationFunc):
        """sec. inside a parenthetical aside."""
        text = "The exclusion (sec. 8.1) does not apply to charitable organisations."
        assert segment(text) == ["The exclusion (sec. 8.1) does not apply to charitable organisations."]

    def test_sec_followed_by_proper_noun(self, segment: SegmentationFunc):
        """sec. followed by a proper noun heading — must not split."""
        text = "The key constraint appears in sec. Methods and is stated precisely."
        assert segment(text) == ["The key constraint appears in sec. Methods and is stated precisely."]

    def test_sec_two_references_in_sentence(self, segment: SegmentationFunc):
        """Two sec. references in the same sentence."""
        text = "See sec. 2.1 and sec. 3.4 for the relevant definitions."
        assert segment(text) == ["See sec. 2.1 and sec. 3.4 for the relevant definitions."]

    # --------------------------------------------------------------- para. --

    def test_para_before_numeral(self, segment: SegmentationFunc):
        """para. before a numeral — should not split."""
        text = "The obligation arises under para. 12 of the agreement."
        assert segment(text) == ["The obligation arises under para. 12 of the agreement."]

    def test_para_in_legal_brief(self, segment: SegmentationFunc):
        """para. in a legal brief paragraph reference."""
        text = "As argued in para. 45 of the claimant's skeleton, the test is met."
        assert segment(text) == ["As argued in para. 45 of the claimant's skeleton, the test is met."]

    def test_para_in_parentheses(self, segment: SegmentationFunc):
        """para. inside parentheses in an academic text."""
        text = "The provision (para. 7) was inserted by amendment in 2018."
        assert segment(text) == ["The provision (para. 7) was inserted by amendment in 2018."]

    def test_para_at_sentence_start(self, segment: SegmentationFunc):
        """para. at sentence start."""
        text = "para. 3 of the statute has been widely interpreted as covering digital assets."
        assert segment(text) == ["para. 3 of the statute has been widely interpreted as covering digital assets."]

    def test_para_followed_by_proper_noun(self, segment: SegmentationFunc):
        """para. followed by a proper noun — must not split."""
        text = "The duty is established in para. Schedule 2 of the regulations."
        assert segment(text) == ["The duty is established in para. Schedule 2 of the regulations."]

    def test_para_two_sentences_split(self, segment: SegmentationFunc):
        """para. in first sentence, second sentence splits correctly."""
        text = "The definition is given in para. 4 of the Act. The courts have interpreted it broadly."
        assert segment(text) == ["The definition is given in para. 4 of the Act.", "The courts have interpreted it broadly."]

    # ----------------------------------------------------------------- ed. --

    def test_ed_before_proper_name(self, segment: SegmentationFunc):
        """ed. before an editor's name should not split."""
        text = "The collection was assembled by Smith, ed. John Brown, Cambridge 2005."
        assert segment(text) == ["The collection was assembled by Smith, ed. John Brown, Cambridge 2005."]

    def test_ed_in_bibliographic_entry(self, segment: SegmentationFunc):
        """ed. in a bibliography entry."""
        text = "Essays on Modernism, ed. Williams, London: Routledge, 2012."
        assert segment(text) == ["Essays on Modernism, ed. Williams, London: Routledge, 2012."]

    def test_eds_multiple_editors(self, segment: SegmentationFunc):
        """eds. for multiple editors — should not split."""
        text = "The anthology was compiled by Green and White, eds. Oxford 2018."
        assert segment(text) == ["The anthology was compiled by Green and White, eds. Oxford 2018."]

    def test_ed_rev_in_same_entry(self, segment: SegmentationFunc):
        """ed. and rev. in the same bibliographic entry."""
        text = "A Grammar of English, ed. Smith, rev. Johnson, New York 1999."
        assert segment(text) == ["A Grammar of English, ed. Smith, rev. Johnson, New York 1999."]

    def test_trans_before_name(self, segment: SegmentationFunc):
        """trans. before a translator's name."""
        text = "The novel was rendered into English by, trans. Mary Hill, Penguin 2002."
        assert segment(text) == ["The novel was rendered into English by, trans. Mary Hill, Penguin 2002."]

    def test_trans_in_parenthetical(self, segment: SegmentationFunc):
        """trans. inside a parenthetical citation."""
        text = "The term (trans. 'recognition') captures the core of the concept."
        assert segment(text) == ["The term (trans. 'recognition') captures the core of the concept."]

    def test_rev_before_edition_year(self, segment: SegmentationFunc):
        """rev. before edition information."""
        text = "The textbook was substantially updated in the rev. 3rd edition, 2015."
        assert segment(text) == ["The textbook was substantially updated in the rev. 3rd edition, 2015."]

    def test_repr_in_bibliographic_entry(self, segment: SegmentationFunc):
        """repr. in a bibliographic entry."""
        text = "First published 1934; repr. New York: Dover, 1987."
        assert segment(text) == ["First published 1934; repr. New York: Dover, 1987."]

    # ----------------------------------------------------------------- bk. / pt. --

    def test_bk_before_numeral(self, segment: SegmentationFunc):
        """bk. before a numeral in a classical reference."""
        text = "The passage is found in Aristotle's Metaphysics, bk. 7, ch. 3."
        assert segment(text) == ["The passage is found in Aristotle's Metaphysics, bk. 7, ch. 3."]

    def test_bk_before_proper_noun(self, segment: SegmentationFunc):
        """bk. before a proper noun — should not split."""
        text = "In bk. Odyssey Homer describes the encounter with Circe."
        assert segment(text) == ["In bk. Odyssey Homer describes the encounter with Circe."]

    def test_pt_before_numeral(self, segment: SegmentationFunc):
        """pt. before a numeral in a multi-part work."""
        text = "The analysis continues in pt. 2 of this study."
        assert segment(text) == ["The analysis continues in pt. 2 of this study."]

    def test_pt_before_roman_numeral(self, segment: SegmentationFunc):
        """pt. before a Roman numeral — must not split."""
        text = "The second volume covers pt. III and pt. IV of the argument."
        assert segment(text) == ["The second volume covers pt. III and pt. IV of the argument."]

    # ----------------------------------------------------------------- ser. --

    def test_ser_before_numeral_in_bibliography(self, segment: SegmentationFunc):
        """ser. before a series number in a bibliographic entry."""
        text = "The report belongs to ser. 4, no. 12 of the working paper series."
        assert segment(text) == ["The report belongs to ser. 4, no. 12 of the working paper series."]

    def test_ser_before_proper_noun(self, segment: SegmentationFunc):
        """ser. before a proper noun series title."""
        text = "The coin is classified under ser. Roman Imperial in the catalogue."
        assert segment(text) == ["The coin is classified under ser. Roman Imperial in the catalogue."]

    # ----------------------------------------------------------------- fn. --

    def test_fn_before_numeral(self, segment: SegmentationFunc):
        """fn. before a footnote number."""
        text = "See fn. 14 for the full discussion of this terminological question."
        assert segment(text) == ["See fn. 14 for the full discussion of this terminological question."]

    def test_fn_in_parentheses(self, segment: SegmentationFunc):
        """fn. inside parentheses."""
        text = "The exception (fn. 3) was added in the second edition."
        assert segment(text) == ["The exception (fn. 3) was added in the second edition."]

    # ----------------------------------------------------------------- app. --

    def test_app_before_letter_label(self, segment: SegmentationFunc):
        """app. before a letter label."""
        text = "The raw data are provided in app. A of this article."
        assert segment(text) == ["The raw data are provided in app. A of this article."]

    def test_app_before_proper_noun(self, segment: SegmentationFunc):
        """app. before a proper noun in appendix reference."""
        text = "See app. Glossary for definitions of technical terms used."
        assert segment(text) == ["See app. Glossary for definitions of technical terms used."]

    # ----------------------------------------------------------------- illus. --

    def test_illus_before_name(self, segment: SegmentationFunc):
        """illus. before an illustrator name."""
        text = "The edition was illustrated by, illus. Thomas Bewick, London 1797."
        assert segment(text) == ["The edition was illustrated by, illus. Thomas Bewick, London 1797."]

    def test_illus_before_numeral(self, segment: SegmentationFunc):
        """illus. before a figure number."""
        text = "The technique is shown in illus. 7 of the artist's manual."
        assert segment(text) == ["The technique is shown in illus. 7 of the artist's manual."]

    # ----------------------------------------------------------------- q.v. --

    def test_qv_cross_reference(self, segment: SegmentationFunc):
        """q.v. cross-reference in an encyclopedia-style text."""
        text = "For the relevant doctrine, q.v. Res judicata in this volume."
        assert segment(text) == ["For the relevant doctrine, q.v. Res judicata in this volume."]

    def test_qv_in_parentheses(self, segment: SegmentationFunc):
        """q.v. inside parentheses."""
        text = "The same principle (q.v. Proportionality) governs all these cases."
        assert segment(text) == ["The same principle (q.v. Proportionality) governs all these cases."]

    # ----------------------------------------------------------------- fl. --

    def test_fl_before_date_in_biography(self, segment: SegmentationFunc):
        """fl. (floruit) before a date in a biographical note."""
        text = "The painter, fl. 1520-1545, is known only from contract records."
        assert segment(text) == ["The painter, fl. 1520-1545, is known only from contract records."]

    def test_fl_before_century(self, segment: SegmentationFunc):
        """fl. before a century reference."""
        text = "The scholar fl. 12th century produced several influential glosses."
        assert segment(text) == ["The scholar fl. 12th century produced several influential glosses."]

    # ----------------------------------------------------------------- s.v. --

    def test_sv_in_dictionary_entry(self, segment: SegmentationFunc):
        """s.v. in a dictionary cross-reference."""
        text = "The usage is documented, s.v. 'virtue' in the Oxford Latin Dictionary."
        assert segment(text) == ["The usage is documented, s.v. 'virtue' in the Oxford Latin Dictionary."]

    def test_sv_before_proper_noun_entry(self, segment: SegmentationFunc):
        """s.v. before a proper noun dictionary entry."""
        text = "See Liddell-Scott s.v. Logos for the full semantic range."
        assert segment(text) == ["See Liddell-Scott s.v. Logos for the full semantic range."]

    # ----------------------------------------------------------------- id. / ead. --

    def test_id_same_author_reference(self, segment: SegmentationFunc):
        """id. (idem) same-author reference should not split."""
        text = "The earlier study (id. 2015, p. 34) reached the same conclusion."
        assert segment(text) == ["The earlier study (id. 2015, p. 34) reached the same conclusion."]

    def test_ead_feminine_form_reference(self, segment: SegmentationFunc):
        """ead. (eadem) feminine same-author reference."""
        text = "A revised account was given in ead. The Theory Reconsidered, 2018."
        assert segment(text) == ["A revised account was given in ead. The Theory Reconsidered, 2018."]

    # ----------------------------------------------------------------- ff. --

    def test_ff_pages_following(self, segment: SegmentationFunc):
        """ff. (following pages) should not split."""
        text = "The argument begins on p. 34 ff. and continues for several chapters."
        assert segment(text) == ["The argument begins on p. 34 ff. and continues for several chapters."]

    def test_ff_after_section_number(self, segment: SegmentationFunc):
        """ff. after a section number."""
        text = "See sec. 3.1 ff. for the complete derivation."
        assert segment(text) == ["See sec. 3.1 ff. for the complete derivation."]

    # ----------------------------------------------------------------- a.k.a. --

    def test_aka_in_parentheses(self, segment: SegmentationFunc):
        """a.k.a. inside parentheses."""
        text = "The substance (a.k.a. acetylsalicylic acid) is commonly available."
        assert segment(text) == ["The substance (a.k.a. acetylsalicylic acid) is commonly available."]

    def test_aka_mid_sentence(self, segment: SegmentationFunc):
        """a.k.a. mid-sentence."""
        text = "The programme a.k.a. Project Horizon was classified until 2001."
        assert segment(text) == ["The programme a.k.a. Project Horizon was classified until 2001."]

    # ----------------------------------------------------------------- q.e.d. --

    def test_qed_at_proof_end(self, segment: SegmentationFunc):
        """q.e.d. at the end of a proof."""
        text = "Therefore P implies Q, and Q implies R. q.e.d."
        assert segment(text) == ["Therefore P implies Q, and Q implies R.", "q.e.d."]

    def test_qed_in_running_text(self, segment: SegmentationFunc):
        """q.e.d. used rhetorically in running text."""
        text = "The contradiction is obvious, q.e.d., and the argument collapses."
        assert segment(text) == ["The contradiction is obvious, q.e.d., and the argument collapses."]

    # ----------------------------------------------------------------- i.e. --

    def test_ie_mid_sentence_before_noun(self, segment: SegmentationFunc):
        """i.e. mid-sentence before a noun phrase."""
        text = "The procedure must be completed within the statutory period, i.e. 30 days from notice."
        assert segment(text) == ["The procedure must be completed within the statutory period, i.e. 30 days from notice."]

    def test_ie_before_proper_noun(self, segment: SegmentationFunc):
        """i.e. before a proper noun — should not split."""
        text = "The regulation applies to the relevant authority, i.e. Parliament, not the executive."
        assert segment(text) == ["The regulation applies to the relevant authority, i.e. Parliament, not the executive."]

    def test_ie_in_parentheses(self, segment: SegmentationFunc):
        """i.e. inside parentheses."""
        text = "The specimen dates to the early period (i.e. before 500 BCE)."
        assert segment(text) == ["The specimen dates to the early period (i.e. before 500 BCE)."]

    def test_ie_at_sentence_start(self, segment: SegmentationFunc):
        """i.e. at sentence start."""
        text = "i.e. the original source has not been located in any library catalogue."
        assert segment(text) == ["i.e. the original source has not been located in any library catalogue."]

    def test_ie_followed_by_quoted_text(self, segment: SegmentationFunc):
        """i.e. followed by quoted text."""
        text = "The phrase means something specific here, i.e. 'the power to compel'."
        assert segment(text) == ["The phrase means something specific here, i.e. 'the power to compel'."]

    # ----------------------------------------------------------------- e.g. --

    def test_eg_mid_sentence_before_noun(self, segment: SegmentationFunc):
        """e.g. mid-sentence before a noun phrase."""
        text = "Several languages show this feature, e.g. Finnish, Hungarian, and Turkish."
        assert segment(text) == ["Several languages show this feature, e.g. Finnish, Hungarian, and Turkish."]

    def test_eg_before_proper_noun(self, segment: SegmentationFunc):
        """e.g. before a proper noun — should not split."""
        text = "The rule applies to all parliamentary democracies, e.g. Germany, Canada, and Sweden."
        assert segment(text) == ["The rule applies to all parliamentary democracies, e.g. Germany, Canada, and Sweden."]

    def test_eg_in_parentheses(self, segment: SegmentationFunc):
        """e.g. inside parentheses."""
        text = "The transformation may take many forms (e.g. reduction, passivisation, topicalisation)."
        assert segment(text) == ["The transformation may take many forms (e.g. reduction, passivisation, topicalisation)."]

    def test_eg_at_sentence_start(self, segment: SegmentationFunc):
        """e.g. at sentence start."""
        text = "e.g. the following three cases all demonstrate the same underlying phenomenon."
        assert segment(text) == ["e.g. the following three cases all demonstrate the same underlying phenomenon."]

    def test_eg_followed_by_year(self, segment: SegmentationFunc):
        """e.g. followed by a year."""
        text = "The pattern appears in several works (e.g. 1987, 2004, 2019)."
        assert segment(text) == ["The pattern appears in several works (e.g. 1987, 2004, 2019)."]

    # ------------------------------------------- cross-abbreviation combos --

    def test_cf_and_et_al_same_sentence(self, segment: SegmentationFunc):
        """cf. and et al. both in the same sentence."""
        text = "cf. Smith et al. 2015 for the most comprehensive treatment of this topic."
        assert segment(text) == ["cf. Smith et al. 2015 for the most comprehensive treatment of this topic."]

    def test_vol_pp_no_all_in_citation(self, segment: SegmentationFunc):
        """vol., pp., and no. all in the same citation — must not split."""
        text = "Published in vol. 12, no. 3, pp. 45-67 of the journal."
        assert segment(text) == ["Published in vol. 12, no. 3, pp. 45-67 of the journal."]

    def test_eg_and_cf_same_sentence(self, segment: SegmentationFunc):
        """e.g. and cf. both appearing in the same sentence."""
        text = "Examples abound, e.g. in French and German; cf. Table 3 for a full list."
        assert segment(text) == ["Examples abound, e.g. in French and German; cf. Table 3 for a full list."]

    def test_nb_and_cf_same_sentence(self, segment: SegmentationFunc):
        """N.B. and cf. both in the same sentence."""
        text = "N.B. This figure differs from the source data; cf. Appendix B."
        assert segment(text) == ["N.B. This figure differs from the source data; cf. Appendix B."]

    def test_ie_and_viz_same_sentence(self, segment: SegmentationFunc):
        """i.e. and viz. both in the same sentence."""
        text = "The principle, i.e. proportionality, has one key application, viz. administrative law."
        assert segment(text) == ["The principle, i.e. proportionality, has one key application, viz. administrative law."]

    def test_ca_and_fl_same_sentence(self, segment: SegmentationFunc):
        """ca. and fl. both in a biographical sentence."""
        text = "The artist, fl. 1490-1520, was working in Venice ca. 1500."
        assert segment(text) == ["The artist, fl. 1490-1520, was working in Venice ca. 1500."]

    def test_ibid_and_p_same_sentence(self, segment: SegmentationFunc):
        """ibid. and p. both in the same reference."""
        text = "ibid. p. 45 gives a fuller account of the argument summarised here."
        assert segment(text) == ["ibid. p. 45 gives a fuller account of the argument summarised here."]

    def test_et_al_vol_pp_triple_combo(self, segment: SegmentationFunc):
        """Three abbreviations: et al., vol., and pp. in a single sentence — must not split."""
        text = "Zhang et al. vol. 9, pp. 101-115 provides the primary dataset for our analysis."
        assert segment(text) == ["Zhang et al. vol. 9, pp. 101-115 provides the primary dataset for our analysis."]

    def test_cf_sec_no_triple_combo(self, segment: SegmentationFunc):
        """Three abbreviations: cf., sec., and no. in a single sentence — must not split."""
        text = "cf. sec. 4 of Report no. 7 for the relevant findings."
        assert segment(text) == ["cf. sec. 4 of Report no. 7 for the relevant findings."]

    def test_nb_eg_viz_triple_combo(self, segment: SegmentationFunc):
        """Three abbreviations: N.B., e.g., and viz. in a single sentence."""
        text = "N.B. certain exceptions apply, e.g. in maritime law, viz. the law of salvage."
        assert segment(text) == ["N.B. certain exceptions apply, e.g. in maritime law, viz. the law of salvage."]

    # -------------------------------- correct splits (should split) --

    def test_two_full_sentences_no_abbreviation(self, segment: SegmentationFunc):
        """Two full sentences with no abbreviations — must split correctly."""
        text = "The hypothesis was confirmed. The data supports the model."
        assert segment(text) == ["The hypothesis was confirmed.", "The data supports the model."]

    def test_cf_first_sentence_then_full_second(self, segment: SegmentationFunc):
        """cf. in first sentence, followed by full second sentence — split at period."""
        text = "For background reading cf. Chapter 1. The present chapter develops the argument further."
        assert segment(text) == ["For background reading cf. Chapter 1.", "The present chapter develops the argument further."]

    def test_et_al_first_full_sentence_then_second(self, segment: SegmentationFunc):
        """et al. in first sentence, followed by a second full sentence."""
        text = "The review by Carter et al. covers the period 1980-2010. Subsequent work is not included."
        assert segment(text) == ["The review by Carter et al. covers the period 1980-2010.", "Subsequent work is not included."]

    def test_vol_first_sentence_then_second(self, segment: SegmentationFunc):
        """vol. in first sentence — must not split within sentence; splits at sentence boundary."""
        text = "The main source is vol. 3 of the encyclopedia. Translations are cited from the German."
        assert segment(text) == ["The main source is vol. 3 of the encyclopedia.", "Translations are cited from the German."]

    def test_three_sentences_with_abbreviations(self, segment: SegmentationFunc):
        """Three sentences each containing abbreviations — all three must separate."""
        text = "The data appears in vol. 5. See ibid. p. 34 for a correction. All other figures match."
        assert segment(text) == ["The data appears in vol. 5.", "See ibid. p. 34 for a correction.", "All other figures match."]

    def test_sentence_ending_abbreviation_then_proper_start(self, segment: SegmentationFunc):
        """Sentence that ends naturally after a reference, then new sentence starting with proper noun."""
        text = "Full details are in cf. Smith 2010. Professor Jones disagreed with this reading."
        assert segment(text) == ["Full details are in cf. Smith 2010.", "Professor Jones disagreed with this reading."]

    # --------------------------------- abbreviation-at-boundary edge cases --

    def test_cf_only_input(self, segment: SegmentationFunc):
        """cf. as the entire input — single fragment."""
        text = "cf."
        assert segment(text) == ["cf."]

    def test_et_al_only_input(self, segment: SegmentationFunc):
        """et al. as the entire input."""
        text = "et al."
        assert segment(text) == ["et al."]

    def test_vol_only_input(self, segment: SegmentationFunc):
        """vol. as the entire input."""
        text = "vol."
        assert segment(text) == ["vol."]

    def test_abbreviation_at_very_start_of_long_sentence(self, segment: SegmentationFunc):
        """Abbreviation as the very first token of a long sentence."""
        text = "cf. the detailed analysis in Smith 2009 which covers all relevant prior literature."
        assert segment(text) == ["cf. the detailed analysis in Smith 2009 which covers all relevant prior literature."]

    def test_abbreviation_at_very_end_of_long_sentence(self, segment: SegmentationFunc):
        """Full sentence ending with an abbreviation — must terminate cleanly."""
        text = "The complete bibliography is provided in the vol."
        assert segment(text) == ["The complete bibliography is provided in the vol."]

    def test_multiple_abbreviations_no_sentence_break(self, segment: SegmentationFunc):
        """Five abbreviations in a single sentence — must not split anywhere."""
        text = "cf. ibid. p. 34; cf. also vol. 2, no. 5, pp. 12-15 for corroborating evidence."
        assert segment(text) == ["cf. ibid. p. 34; cf. also vol. 2, no. 5, pp. 12-15 for corroborating evidence."]

    def test_scholarly_abbrev_before_quoted_text(self, segment: SegmentationFunc):
        """Abbreviation followed by quoted text — should not split."""
        text = "The author concludes, cf. 'The evidence is inconclusive at this stage'."
        assert segment(text) == ["The author concludes, cf. 'The evidence is inconclusive at this stage'."]

    def test_eg_before_quoted_example(self, segment: SegmentationFunc):
        """e.g. before a quoted example string."""
        text = "The pattern appears in many forms, e.g. 'This is one example of the phenomenon'."
        assert segment(text) == ["The pattern appears in many forms, e.g. 'This is one example of the phenomenon'."]

    def test_cf_before_number_in_parentheses(self, segment: SegmentationFunc):
        """cf. followed by a number in parentheses."""
        text = "The case is analogous, cf. (3) in the list of axioms."
        assert segment(text) == ["The case is analogous, cf. (3) in the list of axioms."]

    def test_p_before_number_in_parentheses(self, segment: SegmentationFunc):
        """p. followed by a number in parentheses."""
        text = "The result appears on p. (45) in the electronic edition with non-standard pagination."
        assert segment(text) == ["The result appears on p. (45) in the electronic edition with non-standard pagination."]

    def test_ocr_double_space_after_cf(self, segment: SegmentationFunc):
        """OCR-style double space between cf. and following word.

        _clean_spacing treats every double-space as a sentence delimiter
        (replace '  ' -> '. ').  "reads  cf." becomes "reads. cf." and
        "Week 2  Overview" becomes "Week 2. Overview".  The pipeline segments
        at each injected period, yielding three fragments.
        """
        text = "The original passage reads  cf.  Week 2  Overview for the source."
        assert segment(text) == [
            "The original passage reads.",
            "cf. Week 2.",
            "Overview for the source.",
        ]

    def test_ocr_double_space_after_et_al(self, segment: SegmentationFunc):
        """OCR-style double space after et al.

        _clean_spacing converts the double-space before "et" to '. ', making
        "Smith. et al.".  spaCy splits at "Smith." and "et al." is kept with
        its continuation as one sentence via the et al. merge pattern.
        """
        text = "Smith  et al.  2020 provides the most complete treatment."
        assert segment(text) == [
            "Smith.",
            "et al. 2020 provides the most complete treatment.",
        ]

    def test_p_followed_by_capital_proper_noun_complex(self, segment: SegmentationFunc):
        """p. followed by a capitalised proper name — no split."""
        text = "See especially p. Chapters devoted to the French Revolution for context."
        assert segment(text) == ["See especially p. Chapters devoted to the French Revolution for context."]

    def test_cf_followed_by_capitalised_title(self, segment: SegmentationFunc):
        """cf. followed by capitalised title — must not split."""
        text = "The framing derives from cf. The Structure of Scientific Revolutions."
        assert segment(text) == ["The framing derives from cf. The Structure of Scientific Revolutions."]

    def test_et_al_before_capitalised_verb(self, segment: SegmentationFunc):
        """et al. followed by a capitalised verb form that looks like a sentence start."""
        text = "Garcia et al. Reported a statistically significant increase in the treated group."
        assert segment(text) == ["Garcia et al. Reported a statistically significant increase in the treated group."]

    def test_nb_before_quoted_sentence(self, segment: SegmentationFunc):
        """N.B. followed by a quoted sentence."""
        text = "N.B. 'These figures have not been independently verified'."
        assert segment(text) == ["N.B. 'These figures have not been independently verified'."]

    def test_viz_followed_by_quoted_example(self, segment: SegmentationFunc):
        """viz. followed by a quoted example."""
        text = "The principle has one formulation, viz. 'Do no harm in the course of treatment'."
        assert segment(text) == ["The principle has one formulation, viz. 'Do no harm in the course of treatment'."]

    def test_ed_before_capital_name(self, segment: SegmentationFunc):
        """ed. before a capitalized name — should not split."""
        text = "The Collected Letters, ed. Patricia Walker, was published in 2014."
        assert segment(text) == ["The Collected Letters, ed. Patricia Walker, was published in 2014."]

    def test_trans_before_capital_name(self, segment: SegmentationFunc):
        """trans. before a capitalized name."""
        text = "The Critique of Pure Reason, trans. Norman Kemp Smith, remains the standard translation."
        assert segment(text) == ["The Critique of Pure Reason, trans. Norman Kemp Smith, remains the standard translation."]

    def test_repr_before_capital_place(self, segment: SegmentationFunc):
        """repr. before a capitalised place name."""
        text = "Originally published 1952; repr. New York: Dover Publications, 1994."
        assert segment(text) == ["Originally published 1952; repr. New York: Dover Publications, 1994."]

    def test_illus_before_capital_name(self, segment: SegmentationFunc):
        """illus. before a capitalised name."""
        text = "The tale was illustrated by illus. Arthur Rackham and published in 1908."
        assert segment(text) == ["The tale was illustrated by illus. Arthur Rackham and published in 1908."]

    def test_sc_parenthetical_abbreviation(self, segment: SegmentationFunc):
        """sc. (scilicet) in a parenthetical clarification."""
        text = "The defendant (sc. the second party named) bears the burden of proof."
        assert segment(text) == ["The defendant (sc. the second party named) bears the burden of proof."]

    def test_sc_mid_sentence_clarification(self, segment: SegmentationFunc):
        """sc. mid-sentence as a clarification."""
        text = "The quaestor, sc. the financial officer, supervised the accounts."
        assert segment(text) == ["The quaestor, sc. the financial officer, supervised the accounts."]

    def test_ad_loc_in_commentary(self, segment: SegmentationFunc):
        """ad loc. in a classical commentary context."""
        text = "Virgil, Aeneid II.20, ad loc. Servius notes the allusion to Homer."
        assert segment(text) == ["Virgil, Aeneid II.20, ad loc. Servius notes the allusion to Homer."]

    def test_ad_loc_in_parentheses(self, segment: SegmentationFunc):
        """ad loc. inside parentheses in scholarly text."""
        text = "The scholiast comments (ad loc.) that the text is corrupt at this point."
        assert segment(text) == ["The scholiast comments (ad loc.) that the text is corrupt at this point."]

    def test_rip_in_biographical_note(self, segment: SegmentationFunc):
        """r.i.p. in a biographical or memorial note."""
        text = "John Smith, r.i.p. 2019, was a leading scholar of Byzantine history."
        assert segment(text) == ["John Smith, r.i.p. 2019, was a leading scholar of Byzantine history."]

    def test_ps_in_letter_footnote(self, segment: SegmentationFunc):
        """P.S. at the start of a postscript in a letter."""
        text = "P.S. Please disregard the earlier version of the table."
        assert segment(text) == ["P.S. Please disregard the earlier version of the table."]

    def test_ps_two_sentence_letter_ending(self, segment: SegmentationFunc):
        """P.S. followed by multiple sentences in a letter postscript."""
        text = "P.S. The enclosure was omitted by mistake. Please find it attached."
        assert segment(text) == ["P.S. The enclosure was omitted by mistake.", "Please find it attached."]

    def test_et_seq_after_page_number(self, segment: SegmentationFunc):
        """et seq. (and following) after a page number."""
        text = "See p. 45 et seq. for the complete argument on this point."
        assert segment(text) == ["See p. 45 et seq. for the complete argument on this point."]

    def test_et_seq_after_section_number(self, segment: SegmentationFunc):
        """et seq. after a section number."""
        text = "The provisions of sec. 12 et seq. govern the licensing requirements."
        assert segment(text) == ["The provisions of sec. 12 et seq. govern the licensing requirements."]
