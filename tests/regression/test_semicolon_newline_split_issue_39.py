# -*- coding: UTF-8 -*-
"""
Test suite for Issue #39: Semicolon/Colon + newline incorrectly merges verse lines.

When a line ends with a clause-terminal punctuation (`;` or `:`) followed by
a newline (`\n`), the two lines should be split into separate sentences rather
than merged into one.

Related GitHub Issue:
    #39 - Semicolon + newline incorrectly merges verse lines into single sentence
    https://github.com/craigtrim/fast-sentence-segment/issues/39

Test Structure (275 total tests):
    Group S  (S01–S70):  Semicolon + newline → split (core fix, currently failing)
    Group C  (C01–C50):  Colon + newline → split (core fix, currently failing)
    Group P  (P01–P30):  Period + newline → split (regression, currently passing)
    Group E  (E01–E20):  Exclamation + newline → split (regression, currently passing)
    Group Q  (Q01–Q20):  Question + newline → split (regression, currently passing)
    Group N  (N01–N30):  No terminal punct + newline → merge (regression, should NOT split)
    Group M  (M01–M30):  Multiple sequential lines with semicolons/colons
    Group MID(MID01–MID25): Semicolon in mid-sentence without newline → no split
"""

import pytest
from fast_sentence_segment import segment_text


# ---------------------------------------------------------------------------
# GROUP S: Semicolon + newline → should split into two sentences
# These tests are EXPECTED TO FAIL before the fix and PASS after.
# ---------------------------------------------------------------------------

class TestSemicolonNewlineSplit:
    """Semicolon followed by newline must split into separate sentences (Issue #39)."""

    def test_s01_exact_issue_example(self):
        """The exact example from the GitHub issue (King Lear via Hardy)."""
        text = 'As flies to wanton boys are we to the gods;\nThey kill us for their sport.'
        result = segment_text(text, flatten=True)
        assert result == ['As flies to wanton boys are we to the gods;', 'They kill us for their sport.']

    def test_s02_simple_two_line_verse(self):
        """Simple two-line verse split on semicolon."""
        text = 'The night is dark;\nThe stars are bright.'
        result = segment_text(text, flatten=True)
        assert result == ['The night is dark;', 'The stars are bright.']

    def test_s03_art_is_long_aphorism(self):
        """Classic aphorism: Art is long, life is short."""
        text = 'Life is short;\nArt is long.'
        result = segment_text(text, flatten=True)
        assert result == ['Life is short;', 'Art is long.']

    def test_s04_dickens_opening_lowercase_continuation(self):
        """Dickens-style prose with lowercase continuation after semicolon."""
        text = 'It was the best of times;\nit was the worst of times.'
        result = segment_text(text, flatten=True)
        assert result == ['It was the best of times;', 'it was the worst of times.']

    def test_s05_shakespeare_to_be_or_not(self):
        """Shakespeare verse with longer lines."""
        text = 'To be or not to be, that is the question;\nWhether tis nobler in the mind to suffer.'
        result = segment_text(text, flatten=True)
        assert result == [
            'To be or not to be, that is the question;',
            'Whether tis nobler in the mind to suffer.'
        ]

    def test_s06_biblical_love_is_patient(self):
        """Biblical verse with lowercase continuation."""
        text = 'Love is patient;\nlove is kind.'
        result = segment_text(text, flatten=True)
        assert result == ['Love is patient;', 'love is kind.']

    def test_s07_two_clauses_with_commas(self):
        """Both lines contain internal commas."""
        text = 'The sun rises in the east, setting at dusk;\nThe moon follows, filling the night.'
        result = segment_text(text, flatten=True)
        assert result == [
            'The sun rises in the east, setting at dusk;',
            'The moon follows, filling the night.'
        ]

    def test_s08_single_word_lines(self):
        """Single-word verses separated by semicolon."""
        text = 'Rise;\nFall.'
        result = segment_text(text, flatten=True)
        assert result == ['Rise;', 'Fall.']

    def test_s09_second_line_ends_with_question(self):
        """First line ends with semicolon, second with question mark."""
        text = 'We were brave;\nWere we not?'
        result = segment_text(text, flatten=True)
        assert result == ['We were brave;', 'Were we not?']

    def test_s10_second_line_ends_with_exclamation(self):
        """First line ends with semicolon, second with exclamation mark."""
        text = 'She wept;\nHe stood firm!'
        result = segment_text(text, flatten=True)
        assert result == ['She wept;', 'He stood firm!']

    def test_s11_numbers_in_lines(self):
        """Lines with ordinal numbers."""
        text = 'The 1st rule is silence;\nThe 2nd rule is patience.'
        result = segment_text(text, flatten=True)
        assert result == ['The 1st rule is silence;', 'The 2nd rule is patience.']

    def test_s12_came_saw_conquered_split(self):
        """Caesar's motto split across lines."""
        text = 'He came, he saw;\nhe conquered.'
        result = segment_text(text, flatten=True)
        assert result == ['He came, he saw;', 'he conquered.']

    def test_s13_possessive_apostrophes(self):
        """Lines with possessive apostrophes."""
        text = "Man's gotta do what man's gotta do;\nThat's the way of it."
        result = segment_text(text, flatten=True)
        assert result == ["Man's gotta do what man's gotta do;", "That's the way of it."]

    def test_s14_quotes_within_lines(self):
        """Quoted words within each line."""
        text = 'She said "yes";\nhe said "no".'
        result = segment_text(text, flatten=True)
        assert result == ['She said "yes";', 'he said "no".']

    def test_s15_archaic_english_verse(self):
        """Archaic English verse form."""
        text = 'Thou art my light;\nI am thy shadow.'
        result = segment_text(text, flatten=True)
        assert result == ['Thou art my light;', 'I am thy shadow.']

    def test_s16_ecclesiastes_rivers_to_sea(self):
        """Ecclesiastes-style verse."""
        text = 'The rivers run to the sea;\nYet the sea is not full.'
        result = segment_text(text, flatten=True)
        assert result == ['The rivers run to the sea;', 'Yet the sea is not full.']

    def test_s17_romeo_and_juliet_names(self):
        """Literary verse with proper names."""
        text = 'Romeo loved Juliet;\nJuliet loved Romeo.'
        result = segment_text(text, flatten=True)
        assert result == ['Romeo loved Juliet;', 'Juliet loved Romeo.']

    def test_s18_cogito_ergo_sum_parallel(self):
        """Parallel philosophical clauses."""
        text = 'I think therefore I am;\nI am therefore I think.'
        result = segment_text(text, flatten=True)
        assert result == ['I think therefore I am;', 'I am therefore I think.']

    def test_s19_beatitude_style(self):
        """Beatitude-style verse with For-connector."""
        text = 'Blessed are the meek;\nFor they shall inherit the earth.'
        result = segment_text(text, flatten=True)
        assert result == ['Blessed are the meek;', 'For they shall inherit the earth.']

    def test_s20_medical_prose_lowercase(self):
        """Medical/clinical prose with lowercase continuation."""
        text = 'The patient was stable;\nno further intervention was required.'
        result = segment_text(text, flatten=True)
        assert result == ['The patient was stable;', 'no further intervention was required.']

    def test_s21_latin_veni_vidi_vici(self):
        """Latin phrase split across lines."""
        text = 'Veni, vidi;\nvici.'
        result = segment_text(text, flatten=True)
        assert result == ['Veni, vidi;', 'vici.']

    def test_s22_alliterative_verse(self):
        """Alliterative verse with Peter Piper."""
        text = 'Peter Piper picked a peck;\nA peck of pickled peppers.'
        result = segment_text(text, flatten=True)
        assert result == ['Peter Piper picked a peck;', 'A peck of pickled peppers.']

    def test_s23_parenthetical_in_first_line(self):
        """Parenthetical expression within the first clause."""
        text = 'The old man (a veteran) spoke;\nthe crowd listened.'
        result = segment_text(text, flatten=True)
        assert result == ['The old man (a veteran) spoke;', 'the crowd listened.']

    def test_s24_work_rest_contrast(self):
        """Day/night contrast verse."""
        text = 'Work hard during the day;\nRest easy at night.'
        result = segment_text(text, flatten=True)
        assert result == ['Work hard during the day;', 'Rest easy at night.']

    def test_s25_strong_weak_parallel(self):
        """Strong/weak parallel structure."""
        text = 'The strong shall endure;\nthe weak shall adapt.'
        result = segment_text(text, flatten=True)
        assert result == ['The strong shall endure;', 'the weak shall adapt.']

    def test_s26_temporal_repetition(self):
        """Temporal verse with past/present."""
        text = 'She loved him once;\nshe loves him still.'
        result = segment_text(text, flatten=True)
        assert result == ['She loved him once;', 'she loves him still.']

    def test_s27_historical_reference(self):
        """Historical reference with proper nouns."""
        text = 'Caesar crossed the Rubicon;\nRome was changed forever.'
        result = segment_text(text, flatten=True)
        assert result == ['Caesar crossed the Rubicon;', 'Rome was changed forever.']

    def test_s28_scientific_fact(self):
        """Scientific fact with astronomical content."""
        text = 'The earth revolves around the sun;\nthe moon revolves around the earth.'
        result = segment_text(text, flatten=True)
        assert result == [
            'The earth revolves around the sun;',
            'the moon revolves around the earth.'
        ]

    def test_s29_word_vs_silence_contrast(self):
        """Literary contrast of word and silence."""
        text = 'In the beginning was the word and the word was good;\nIn the end was silence and silence was golden.'
        result = segment_text(text, flatten=True)
        assert result == [
            'In the beginning was the word and the word was good;',
            'In the end was silence and silence was golden.'
        ]

    def test_s30_cause_and_effect(self):
        """Simple cause and effect verse."""
        text = 'She planted the seeds;\nthey grew into tall oaks.'
        result = segment_text(text, flatten=True)
        assert result == ['She planted the seeds;', 'they grew into tall oaks.']

    def test_s31_however_transition(self):
        """However-transition after semicolon newline."""
        text = 'The plan seemed perfect;\nhowever, fate had other ideas.'
        result = segment_text(text, flatten=True)
        assert result == ['The plan seemed perfect;', 'however, fate had other ideas.']

    def test_s32_yet_transition(self):
        """Yet-transition verse."""
        text = 'The journey was long;\nyet they pressed on.'
        result = segment_text(text, flatten=True)
        assert result == ['The journey was long;', 'yet they pressed on.']

    def test_s33_therefore_connector(self):
        """Therefore-connector after semicolon."""
        text = 'The evidence was clear;\ntherefore the verdict was guilty.'
        result = segment_text(text, flatten=True)
        assert result == ['The evidence was clear;', 'therefore the verdict was guilty.']

    def test_s34_thus_connector(self):
        """Thus-connector verse."""
        text = 'All roads lead to Rome;\nthus the saying goes.'
        result = segment_text(text, flatten=True)
        assert result == ['All roads lead to Rome;', 'thus the saying goes.']

    def test_s35_minimal_verb_pair(self):
        """Minimal subject-verb pair verse."""
        text = 'He runs;\nshe walks.'
        result = segment_text(text, flatten=True)
        assert result == ['He runs;', 'she walks.']

    def test_s36_modal_verb_pair(self):
        """Modal verb repetition verse."""
        text = 'We must remember;\nwe must not forget.'
        result = segment_text(text, flatten=True)
        assert result == ['We must remember;', 'we must not forget.']

    def test_s37_conditional_anaphora(self):
        """Conditional clause anaphora."""
        text = 'When the rain falls, rivers swell;\nwhen rivers swell, floods follow.'
        result = segment_text(text, flatten=True)
        assert result == ['When the rain falls, rivers swell;', 'when rivers swell, floods follow.']

    def test_s38_memento_mori(self):
        """Short existential verse."""
        text = 'Time flies;\ndeath waits.'
        result = segment_text(text, flatten=True)
        assert result == ['Time flies;', 'death waits.']

    def test_s39_honor_thy_father(self):
        """Religious commandment verse."""
        text = 'Honor thy father;\nhonor thy mother.'
        result = segment_text(text, flatten=True)
        assert result == ['Honor thy father;', 'honor thy mother.']

    def test_s40_hardy_tess_context(self):
        """Prose in the style of Hardy (issue source text)."""
        text = 'Tess was a pure woman;\nher story proved it.'
        result = segment_text(text, flatten=True)
        assert result == ['Tess was a pure woman;', 'her story proved it.']

    def test_s41_chaucer_april_showers(self):
        """Chaucer-style opening verse."""
        text = 'When April with his showers sweet;\nHas pierced the drought of March to the root.'
        result = segment_text(text, flatten=True)
        assert result == [
            'When April with his showers sweet;',
            'Has pierced the drought of March to the root.'
        ]

    def test_s42_aeneid_opening(self):
        """Aeneid-style epic verse."""
        text = 'Arms and the man I sing;\nThe hero driven by fate.'
        result = segment_text(text, flatten=True)
        assert result == ['Arms and the man I sing;', 'The hero driven by fate.']

    def test_s43_dramatic_sword_action(self):
        """Dramatic action pair."""
        text = 'He drew his sword;\nShe stepped back.'
        result = segment_text(text, flatten=True)
        assert result == ['He drew his sword;', 'She stepped back.']

    def test_s44_simile_river(self):
        """Simile construction with river metaphor."""
        text = 'Life is like a river;\nit flows ever onward.'
        result = segment_text(text, flatten=True)
        assert result == ['Life is like a river;', 'it flows ever onward.']

    def test_s45_metaphor_ocean_mind(self):
        """Metaphor of ocean and thoughts."""
        text = 'The mind is an ocean;\nthoughts are the waves.'
        result = segment_text(text, flatten=True)
        assert result == ['The mind is an ocean;', 'thoughts are the waves.']

    def test_s46_dam_breaks(self):
        """Action/consequence verse."""
        text = 'The dam broke;\nthe valley flooded.'
        result = segment_text(text, flatten=True)
        assert result == ['The dam broke;', 'the valley flooded.']

    def test_s47_spoke_listened(self):
        """Minimal speaker/listener pair."""
        text = 'He spoke;\nshe listened.'
        result = segment_text(text, flatten=True)
        assert result == ['He spoke;', 'she listened.']

    def test_s48_swords_vs_words(self):
        """Contrast verse: swords vs words."""
        text = 'Some fight with swords;\nothers fight with words.'
        result = segment_text(text, flatten=True)
        assert result == ['Some fight with swords;', 'others fight with words.']

    def test_s49_long_first_line(self):
        """Long first clause, short second."""
        text = 'The old library stood at the corner of Elm Street and Main Avenue;\nit had seen a hundred years of history.'
        result = segment_text(text, flatten=True)
        assert result == [
            'The old library stood at the corner of Elm Street and Main Avenue;',
            'it had seen a hundred years of history.'
        ]

    def test_s50_short_first_long_second(self):
        """Short first clause, long second."""
        text = 'Time passed;\nThe seasons changed one by one until none could remember the beginning.'
        result = segment_text(text, flatten=True)
        assert result == [
            'Time passed;',
            'The seasons changed one by one until none could remember the beginning.'
        ]

    def test_s51_technical_algorithm_prose(self):
        """Technical writing with algorithmic content."""
        text = 'The algorithm runs in O(n log n) time;\nspace complexity is O(n).'
        result = segment_text(text, flatten=True)
        assert result == ['The algorithm runs in O(n log n) time;', 'space complexity is O(n).']

    def test_s52_legal_text(self):
        """Legal prose with clause-terminal semicolon."""
        text = 'The defendant shall appear before the court;\nfailure to appear constitutes contempt.'
        result = segment_text(text, flatten=True)
        assert result == [
            'The defendant shall appear before the court;',
            'failure to appear constitutes contempt.'
        ]

    def test_s53_academic_prose(self):
        """Academic prose conclusion."""
        text = 'The data supports the hypothesis;\nfurther study is recommended.'
        result = segment_text(text, flatten=True)
        assert result == ['The data supports the hypothesis;', 'further study is recommended.']

    def test_s54_journalism_vote(self):
        """Journalism-style vote report."""
        text = 'The committee voted in favor;\nthe measure passed unanimously.'
        result = segment_text(text, flatten=True)
        assert result == ['The committee voted in favor;', 'the measure passed unanimously.']

    def test_s55_medical_vitals(self):
        """Medical vitals notation."""
        text = 'Blood pressure was 120/80;\npulse was steady at 72.'
        result = segment_text(text, flatten=True)
        assert result == ['Blood pressure was 120/80;', 'pulse was steady at 72.']

    def test_s56_if_then_conditional_pair(self):
        """If-then conditional pair as verse."""
        text = 'If you seek wisdom, look within;\nif you seek knowledge, look without.'
        result = segment_text(text, flatten=True)
        assert result == [
            'If you seek wisdom, look within;',
            'if you seek knowledge, look without.'
        ]

    def test_s57_bread_and_wine(self):
        """Religious-style couplet with prepositions."""
        text = 'By bread and wine they lived;\nby love and faith they died.'
        result = segment_text(text, flatten=True)
        assert result == ['By bread and wine they lived;', 'by love and faith they died.']

    def test_s58_churchill_beaches(self):
        """Churchill-style anaphora (partial)."""
        text = 'We shall fight on the beaches;\nwe shall fight on the seas.'
        result = segment_text(text, flatten=True)
        assert result == ['We shall fight on the beaches;', 'we shall fight on the seas.']

    def test_s59_gettysburg_government(self):
        """Gettysburg-style governmental verse."""
        text = 'Government of the people;\nby the people.'
        result = segment_text(text, flatten=True)
        assert result == ['Government of the people;', 'by the people.']

    def test_s60_jfk_chiasmus(self):
        """JFK chiasmus style verse."""
        text = 'Ask not what your country can do for you;\nask what you can do for your country.'
        result = segment_text(text, flatten=True)
        assert result == [
            'Ask not what your country can do for you;',
            'ask what you can do for your country.'
        ]

    def test_s61_second_line_exclamatory(self):
        """Semicolon first line, exclamatory second."""
        text = 'He gathered his courage;\nCharge!'
        result = segment_text(text, flatten=True)
        assert result == ['He gathered his courage;', 'Charge!']

    def test_s62_second_line_interrogative(self):
        """Semicolon first line, question second."""
        text = 'She waited patiently;\nWould he ever return?'
        result = segment_text(text, flatten=True)
        assert result == ['She waited patiently;', 'Would he ever return?']

    def test_s63_parenthetical_in_second_line(self):
        """Parenthetical in the second (continuation) line."""
        text = 'The king gave the order;\nthe soldiers (weary as they were) obeyed.'
        result = segment_text(text, flatten=True)
        assert result == ['The king gave the order;', 'the soldiers (weary as they were) obeyed.']

    def test_s64_number_starts_second_line(self):
        """Second line begins with a number."""
        text = 'The vote was taken;\n42 members approved.'
        result = segment_text(text, flatten=True)
        assert result == ['The vote was taken;', '42 members approved.']

    def test_s65_dr_abbreviation_in_second_line(self):
        """Abbreviation (Dr.) in the second line — should not over-split."""
        text = 'The report was completed;\nDr. Smith signed off on it.'
        result = segment_text(text, flatten=True)
        assert result == ['The report was completed;', 'Dr. Smith signed off on it.']

    def test_s66_agreement_signed(self):
        """Agreement signed verse."""
        text = 'The agreement was signed;\nAll parties were satisfied.'
        result = segment_text(text, flatten=True)
        assert result == ['The agreement was signed;', 'All parties were satisfied.']

    def test_s67_wind_leaves_verse(self):
        """Nature imagery verse."""
        text = 'The wind howled through the trees;\nLeaves scattered like frightened birds.'
        result = segment_text(text, flatten=True)
        assert result == ['The wind howled through the trees;', 'Leaves scattered like frightened birds.']

    def test_s68_neither_transition(self):
        """Neither-connector after semicolon."""
        text = 'She was not rich;\nnor was she poor.'
        result = segment_text(text, flatten=True)
        assert result == ['She was not rich;', 'nor was she poor.']

    def test_s69_but_continuation(self):
        """But-continuation verse."""
        text = 'He was rich;\nbut he was not happy.'
        result = segment_text(text, flatten=True)
        assert result == ['He was rich;', 'but he was not happy.']

    def test_s70_iron_sharpens_iron(self):
        """Proverbs-style verse."""
        text = 'Iron sharpens iron;\nfriend sharpens friend.'
        result = segment_text(text, flatten=True)
        assert result == ['Iron sharpens iron;', 'friend sharpens friend.']


# ---------------------------------------------------------------------------
# GROUP C: Colon + newline → should split into two sentences
# These tests are EXPECTED TO FAIL before the fix and PASS after.
# ---------------------------------------------------------------------------

class TestColonNewlineSplit:
    """Colon followed by newline must split into separate sentences (Issue #39)."""

    def test_c01_speech_introduction(self):
        """Colon introduces quoted speech."""
        text = 'He spoke these words:\nHello, my friends.'
        result = segment_text(text, flatten=True)
        assert result == ['He spoke these words:', 'Hello, my friends.']

    def test_c02_simple_reply(self):
        """Dialogue reply introduction."""
        text = 'She replied:\nI am not afraid.'
        result = segment_text(text, flatten=True)
        assert result == ['She replied:', 'I am not afraid.']

    def test_c03_sign_reads(self):
        """Sign content introduction."""
        text = 'The sign read:\nNo trespassing.'
        result = segment_text(text, flatten=True)
        assert result == ['The sign read:', 'No trespassing.']

    def test_c04_single_word_following(self):
        """Colon followed by a single-word imperative."""
        text = 'His only thought was:\nSurvive.'
        result = segment_text(text, flatten=True)
        assert result == ['His only thought was:', 'Survive.']

    def test_c05_inscription_reads(self):
        """Inscription content."""
        text = 'The inscription read:\nHere lies a brave man.'
        result = segment_text(text, flatten=True)
        assert result == ['The inscription read:', 'Here lies a brave man.']

    def test_c06_note_label(self):
        """Note label introducing content."""
        text = 'Note:\nAll passengers must present their tickets.'
        result = segment_text(text, flatten=True)
        assert result == ['Note:', 'All passengers must present their tickets.']

    def test_c07_warning_label(self):
        """Warning label introducing content."""
        text = 'Warning:\nThis door is alarmed.'
        result = segment_text(text, flatten=True)
        assert result == ['Warning:', 'This door is alarmed.']

    def test_c08_result_label(self):
        """Result label introducing content."""
        text = 'Result:\nThe experiment was a success.'
        result = segment_text(text, flatten=True)
        assert result == ['Result:', 'The experiment was a success.']

    def test_c09_definition_label(self):
        """Definition label introducing content."""
        text = 'Definition:\nA sentence is a unit of meaning.'
        result = segment_text(text, flatten=True)
        assert result == ['Definition:', 'A sentence is a unit of meaning.']

    def test_c10_summary_label(self):
        """Summary label introducing content."""
        text = 'Summary:\nThe project met all its objectives.'
        result = segment_text(text, flatten=True)
        assert result == ['Summary:', 'The project met all its objectives.']

    def test_c11_doctor_concluded(self):
        """Medical conclusion introduction."""
        text = 'The doctor concluded:\nThe patient will make a full recovery.'
        result = segment_text(text, flatten=True)
        assert result == ['The doctor concluded:', 'The patient will make a full recovery.']

    def test_c12_poet_wrote(self):
        """Poetic attribution introduction."""
        text = 'The poet wrote:\nDeath be not proud.'
        result = segment_text(text, flatten=True)
        assert result == ['The poet wrote:', 'Death be not proud.']

    def test_c13_general_ordered(self):
        """Military order introduction."""
        text = 'The general ordered:\nAdvance at dawn.'
        result = segment_text(text, flatten=True)
        assert result == ['The general ordered:', 'Advance at dawn.']

    def test_c14_judge_ruled(self):
        """Legal ruling introduction."""
        text = 'The judge ruled:\nThe defendant is not guilty.'
        result = segment_text(text, flatten=True)
        assert result == ['The judge ruled:', 'The defendant is not guilty.']

    def test_c15_scientist_concluded(self):
        """Scientific conclusion introduction."""
        text = 'The scientist concluded:\nFurther research is warranted.'
        result = segment_text(text, flatten=True)
        assert result == ['The scientist concluded:', 'Further research is warranted.']

    def test_c16_asked_himself_question(self):
        """Internal question introduced by colon."""
        text = 'He asked himself:\nWas this the right choice?'
        result = segment_text(text, flatten=True)
        assert result == ['He asked himself:', 'Was this the right choice?']

    def test_c17_wondered_question(self):
        """Wonder introduced by colon with question."""
        text = 'She wondered:\nWould she ever see him again?'
        result = segment_text(text, flatten=True)
        assert result == ['She wondered:', 'Would she ever see him again?']

    def test_c18_question_remained(self):
        """Remaining question introduced by colon."""
        text = 'The question remained:\nHow long would this last?'
        result = segment_text(text, flatten=True)
        assert result == ['The question remained:', 'How long would this last?']

    def test_c19_fear_was_this(self):
        """Fear stated then elaborated."""
        text = 'His fear was this:\nWhat if he failed?'
        result = segment_text(text, flatten=True)
        assert result == ['His fear was this:', 'What if he failed?']

    def test_c20_answer_was_simple(self):
        """Simple answer introduced by colon."""
        text = 'The answer was simple:\nTry again.'
        result = segment_text(text, flatten=True)
        assert result == ['The answer was simple:', 'Try again.']

    def test_c21_telegram_said(self):
        """Telegram content introduction."""
        text = 'The telegram said:\nCome home immediately.'
        result = segment_text(text, flatten=True)
        assert result == ['The telegram said:', 'Come home immediately.']

    def test_c22_letter_began(self):
        """Letter opening introduction."""
        text = 'The letter began:\nDear Sir, I write with great urgency.'
        result = segment_text(text, flatten=True)
        assert result == ['The letter began:', 'Dear Sir, I write with great urgency.']

    def test_c23_motto_was(self):
        """Motto introduction."""
        text = 'The motto was:\nNever surrender.'
        result = segment_text(text, flatten=True)
        assert result == ['The motto was:', 'Never surrender.']

    def test_c24_headline_declared(self):
        """Newspaper headline introduction."""
        text = 'The headline declared:\nPeace at last.'
        result = segment_text(text, flatten=True)
        assert result == ['The headline declared:', 'Peace at last.']

    def test_c25_last_words_were(self):
        """Last words introduced by colon."""
        text = 'Her last words were:\nI loved you all.'
        result = segment_text(text, flatten=True)
        assert result == ['Her last words were:', 'I loved you all.']

    def test_c26_thought_to_himself(self):
        """Internal thought introduction."""
        text = 'He thought to himself:\nThis cannot be happening.'
        result = segment_text(text, flatten=True)
        assert result == ['He thought to himself:', 'This cannot be happening.']

    def test_c27_caption_read(self):
        """Image caption introduction."""
        text = 'The caption read:\nA moment frozen in time.'
        result = segment_text(text, flatten=True)
        assert result == ['The caption read:', 'A moment frozen in time.']

    def test_c28_old_proverb_says(self):
        """Proverb introduction."""
        text = 'The old proverb says:\nA stitch in time saves nine.'
        result = segment_text(text, flatten=True)
        assert result == ['The old proverb says:', 'A stitch in time saves nine.']

    def test_c29_rule_of_thumb(self):
        """Rule of thumb introduction."""
        text = 'The rule of thumb:\nMeasure twice, cut once.'
        result = segment_text(text, flatten=True)
        assert result == ['The rule of thumb:', 'Measure twice, cut once.']

    def test_c30_conclusion_label(self):
        """Academic conclusion label."""
        text = 'Conclusion:\nThe hypothesis was confirmed.'
        result = segment_text(text, flatten=True)
        assert result == ['Conclusion:', 'The hypothesis was confirmed.']

    def test_c31_introduction_label(self):
        """Academic introduction label."""
        text = 'Introduction:\nThis paper examines the impact of social media on modern discourse.'
        result = segment_text(text, flatten=True)
        assert result == [
            'Introduction:',
            'This paper examines the impact of social media on modern discourse.'
        ]

    def test_c32_chapter_one(self):
        """Chapter heading introduction."""
        text = 'Chapter One:\nThe world had changed.'
        result = segment_text(text, flatten=True)
        assert result == ['Chapter One:', 'The world had changed.']

    def test_c33_epilogue(self):
        """Epilogue heading introduction."""
        text = 'Epilogue:\nMany years later, they were still friends.'
        result = segment_text(text, flatten=True)
        assert result == ['Epilogue:', 'Many years later, they were still friends.']

    def test_c34_act_scene(self):
        """Stage play act/scene heading."""
        text = 'Act One, Scene One:\nThe stage is dark.'
        result = segment_text(text, flatten=True)
        assert result == ['Act One, Scene One:', 'The stage is dark.']

    def test_c35_narrator_label(self):
        """Narrator label introduction."""
        text = 'Narrator:\nIt was a dark and stormy night.'
        result = segment_text(text, flatten=True)
        assert result == ['Narrator:', 'It was a dark and stormy night.']

    def test_c36_stage_direction(self):
        """Stage direction introduction."""
        text = 'Stage direction:\nEnter Hamlet, alone.'
        result = segment_text(text, flatten=True)
        assert result == ['Stage direction:', 'Enter Hamlet, alone.']

    def test_c37_example_label(self):
        """Example label introduction."""
        text = 'Example:\nThe cat sat on the mat.'
        result = segment_text(text, flatten=True)
        assert result == ['Example:', 'The cat sat on the mat.']

    def test_c38_observation_label(self):
        """Observation label introduction."""
        text = 'Observation:\nThe birds flew south for the winter.'
        result = segment_text(text, flatten=True)
        assert result == ['Observation:', 'The birds flew south for the winter.']

    def test_c39_hypothesis_label(self):
        """Hypothesis label introduction."""
        text = 'Hypothesis:\nThe moon affects tidal patterns.'
        result = segment_text(text, flatten=True)
        assert result == ['Hypothesis:', 'The moon affects tidal patterns.']

    def test_c40_thesis_label(self):
        """Thesis label introduction."""
        text = 'Thesis:\nLanguage shapes thought as much as thought shapes language.'
        result = segment_text(text, flatten=True)
        assert result == ['Thesis:', 'Language shapes thought as much as thought shapes language.']

    def test_c41_first_principle(self):
        """First principle introduction."""
        text = 'First principle:\nDo no harm.'
        result = segment_text(text, flatten=True)
        assert result == ['First principle:', 'Do no harm.']

    def test_c42_contract_states(self):
        """Legal contract clause introduction."""
        text = 'The contract states:\nPayment is due within thirty days.'
        result = segment_text(text, flatten=True)
        assert result == ['The contract states:', 'Payment is due within thirty days.']

    def test_c43_instruction_manual(self):
        """Instruction manual step introduction."""
        text = 'The instruction manual says:\nInsert tab A into slot B.'
        result = segment_text(text, flatten=True)
        assert result == ['The instruction manual says:', 'Insert tab A into slot B.']

    def test_c44_policy_label(self):
        """Policy label introduction."""
        text = 'Policy:\nAll employees must wear identification badges.'
        result = segment_text(text, flatten=True)
        assert result == ['Policy:', 'All employees must wear identification badges.']

    def test_c45_mission_label(self):
        """Mission statement introduction."""
        text = 'Mission:\nTo boldly go where no one has gone before.'
        result = segment_text(text, flatten=True)
        assert result == ['Mission:', 'To boldly go where no one has gone before.']

    def test_c46_warning_label_children(self):
        """Product warning label."""
        text = 'The warning label read:\nKeep away from children.'
        result = segment_text(text, flatten=True)
        assert result == ['The warning label read:', 'Keep away from children.']

    def test_c47_his_promise(self):
        """Promise stated via colon introduction."""
        text = 'His promise:\nI will return.'
        result = segment_text(text, flatten=True)
        assert result == ['His promise:', 'I will return.']

    def test_c48_the_decree(self):
        """Decree introduction."""
        text = 'The decree:\nLet there be light.'
        result = segment_text(text, flatten=True)
        assert result == ['The decree:', 'Let there be light.']

    def test_c49_exclamatory_following(self):
        """Colon introduction followed by exclamatory content."""
        text = 'Her reaction:\nAbsolutely not!'
        result = segment_text(text, flatten=True)
        assert result == ['Her reaction:', 'Absolutely not!']

    def test_c50_interrogative_following(self):
        """Colon introduction followed by question content."""
        text = 'The riddle:\nWhat has roots as nobody sees?'
        result = segment_text(text, flatten=True)
        assert result == ['The riddle:', 'What has roots as nobody sees?']


# ---------------------------------------------------------------------------
# GROUP P: Period + newline → split (REGRESSION: must keep working after fix)
# ---------------------------------------------------------------------------

class TestPeriodNewlineSplitRegression:
    """Period followed by newline must continue to split correctly (regression)."""

    def test_p01_simple_two_sentences(self):
        text = 'She walked home.\nHe followed close behind.'
        result = segment_text(text, flatten=True)
        assert result == ['She walked home.', 'He followed close behind.']

    def test_p02_sun_set(self):
        text = 'The sun set.\nDarkness fell.'
        result = segment_text(text, flatten=True)
        assert result == ['The sun set.', 'Darkness fell.']

    def test_p03_book_finished(self):
        text = 'He finished the book.\nShe started a new one.'
        result = segment_text(text, flatten=True)
        assert result == ['He finished the book.', 'She started a new one.']

    def test_p04_war_ended(self):
        text = 'The war ended.\nPeace was declared.'
        result = segment_text(text, flatten=True)
        assert result == ['The war ended.', 'Peace was declared.']

    def test_p05_rain_fell(self):
        text = 'Rain fell all night.\nBy morning the streets were flooded.'
        result = segment_text(text, flatten=True)
        assert result == ['Rain fell all night.', 'By morning the streets were flooded.']

    def test_p06_sang_beautifully(self):
        text = 'She sang beautifully.\nThe audience applauded.'
        result = segment_text(text, flatten=True)
        assert result == ['She sang beautifully.', 'The audience applauded.']

    def test_p07_opened_door(self):
        text = 'He opened the door.\nLight flooded in.'
        result = segment_text(text, flatten=True)
        assert result == ['He opened the door.', 'Light flooded in.']

    def test_p08_train_arrived(self):
        text = 'The train arrived on time.\nPassengers rushed aboard.'
        result = segment_text(text, flatten=True)
        assert result == ['The train arrived on time.', 'Passengers rushed aboard.']

    def test_p09_read_letter(self):
        text = 'She read the letter.\nTears filled her eyes.'
        result = segment_text(text, flatten=True)
        assert result == ['She read the letter.', 'Tears filled her eyes.']

    def test_p10_experiment_succeeded(self):
        text = 'The experiment succeeded.\nScientists celebrated the breakthrough.'
        result = segment_text(text, flatten=True)
        assert result == ['The experiment succeeded.', 'Scientists celebrated the breakthrough.']

    def test_p11_child_laughed(self):
        text = 'The child laughed.\nHer mother smiled.'
        result = segment_text(text, flatten=True)
        assert result == ['The child laughed.', 'Her mother smiled.']

    def test_p12_deep_breath(self):
        text = 'He took a deep breath.\nThen he jumped.'
        result = segment_text(text, flatten=True)
        assert result == ['He took a deep breath.', 'Then he jumped.']

    def test_p13_fire_crackled(self):
        text = 'The fire crackled.\nWarmth spread through the room.'
        result = segment_text(text, flatten=True)
        assert result == ['The fire crackled.', 'Warmth spread through the room.']

    def test_p14_picked_up_phone(self):
        text = 'She picked up the phone.\nThere was no one there.'
        result = segment_text(text, flatten=True)
        assert result == ['She picked up the phone.', 'There was no one there.']

    def test_p15_clock_struck_midnight(self):
        text = 'The old clock struck midnight.\nThe ball ended.'
        result = segment_text(text, flatten=True)
        assert result == ['The old clock struck midnight.', 'The ball ended.']

    def test_p16_packed_bags(self):
        text = 'He packed his bags.\nShe watched from the window.'
        result = segment_text(text, flatten=True)
        assert result == ['He packed his bags.', 'She watched from the window.']

    def test_p17_letter_sealed(self):
        text = 'The letter was sealed.\nIt was delivered the next day.'
        result = segment_text(text, flatten=True)
        assert result == ['The letter was sealed.', 'It was delivered the next day.']

    def test_p18_bell_rang(self):
        text = 'The bell rang.\nStudents filed into the classroom.'
        result = segment_text(text, flatten=True)
        assert result == ['The bell rang.', 'Students filed into the classroom.']

    def test_p19_turned_key(self):
        text = 'She turned the key.\nThe engine roared to life.'
        result = segment_text(text, flatten=True)
        assert result == ['She turned the key.', 'The engine roared to life.']

    def test_p20_curtain_rose(self):
        text = 'The curtain rose.\nThe play began.'
        result = segment_text(text, flatten=True)
        assert result == ['The curtain rose.', 'The play began.']

    def test_p21_signed_contract(self):
        text = 'He signed the contract.\nThe deal was done.'
        result = segment_text(text, flatten=True)
        assert result == ['He signed the contract.', 'The deal was done.']

    def test_p22_tide_came_in(self):
        text = 'The tide came in.\nThe sandcastle washed away.'
        result = segment_text(text, flatten=True)
        assert result == ['The tide came in.', 'The sandcastle washed away.']

    def test_p23_closed_eyes(self):
        text = 'She closed her eyes.\nShe dreamed of distant places.'
        result = segment_text(text, flatten=True)
        assert result == ['She closed her eyes.', 'She dreamed of distant places.']

    def test_p24_mountain_loomed(self):
        text = 'The mountain loomed ahead.\nThey pressed on regardless.'
        result = segment_text(text, flatten=True)
        assert result == ['The mountain loomed ahead.', 'They pressed on regardless.']

    def test_p25_finished_painting(self):
        text = 'He finished the painting.\nIt was his finest work.'
        result = segment_text(text, flatten=True)
        assert result == ['He finished the painting.', 'It was his finest work.']

    def test_p26_vote_counted(self):
        text = 'The vote was counted.\nThe winner was announced.'
        result = segment_text(text, flatten=True)
        assert result == ['The vote was counted.', 'The winner was announced.']

    def test_p27_planted_seeds(self):
        text = 'She planted the seeds in spring.\nBy summer they had bloomed.'
        result = segment_text(text, flatten=True)
        assert result == ['She planted the seeds in spring.', 'By summer they had bloomed.']

    def test_p28_read_headline(self):
        text = 'He read the headline.\nHe could not believe his eyes.'
        result = segment_text(text, flatten=True)
        assert result == ['He read the headline.', 'He could not believe his eyes.']

    def test_p29_fog_lifted(self):
        text = 'The fog lifted at noon.\nThe harbor was visible again.'
        result = segment_text(text, flatten=True)
        assert result == ['The fog lifted at noon.', 'The harbor was visible again.']

    def test_p30_final_words(self):
        text = 'She spoke her final words.\nThen she was gone.'
        result = segment_text(text, flatten=True)
        assert result == ['She spoke her final words.', 'Then she was gone.']


# ---------------------------------------------------------------------------
# GROUP E: Exclamation + newline → split (REGRESSION)
# ---------------------------------------------------------------------------

class TestExclamationNewlineSplitRegression:
    """Exclamation followed by newline must continue to split correctly (regression)."""

    def test_e01_fire_run(self):
        text = 'Fire!\nRun for your lives.'
        result = segment_text(text, flatten=True)
        assert result == ['Fire!', 'Run for your lives.']

    def test_e02_won_race(self):
        text = 'He won the race!\nThe crowd went wild.'
        result = segment_text(text, flatten=True)
        assert result == ['He won the race!', 'The crowd went wild.']

    def test_e03_she_was_free(self):
        text = 'She was free!\nThe prison gates opened wide.'
        result = segment_text(text, flatten=True)
        assert result == ['She was free!', 'The prison gates opened wide.']

    def test_e04_eureka(self):
        text = 'Eureka!\nThe solution was at hand.'
        result = segment_text(text, flatten=True)
        assert result == ['Eureka!', 'The solution was at hand.']

    def test_e05_watch_out(self):
        text = 'Watch out!\nThe car is coming.'
        result = segment_text(text, flatten=True)
        assert result == ['Watch out!', 'The car is coming.']

    def test_e06_help(self):
        text = 'Help!\nSomeone call the police.'
        result = segment_text(text, flatten=True)
        assert result == ['Help!', 'Someone call the police.']

    def test_e07_silence(self):
        text = 'Silence!\nThe judge has spoken.'
        result = segment_text(text, flatten=True)
        assert result == ['Silence!', 'The judge has spoken.']

    def test_e08_victory(self):
        text = 'Victory!\nThe battle was over.'
        result = segment_text(text, flatten=True)
        assert result == ['Victory!', 'The battle was over.']

    def test_e09_charge(self):
        text = 'Charge!\nThe army surged forward.'
        result = segment_text(text, flatten=True)
        assert result == ['Charge!', 'The army surged forward.']

    def test_e10_halt(self):
        text = 'Halt!\nWho goes there?'
        result = segment_text(text, flatten=True)
        assert result == ['Halt!', 'Who goes there?']

    def test_e11_amazing(self):
        text = 'Amazing!\nI never expected that.'
        result = segment_text(text, flatten=True)
        assert result == ['Amazing!', 'I never expected that.']

    def test_e12_what_a_sight(self):
        text = 'What a sight!\nThe city stretched before them.'
        result = segment_text(text, flatten=True)
        assert result == ['What a sight!', 'The city stretched before them.']

    def test_e13_well_done(self):
        text = 'Well done!\nYou have passed the test.'
        result = segment_text(text, flatten=True)
        assert result == ['Well done!', 'You have passed the test.']

    def test_e14_how_wonderful(self):
        text = 'How wonderful!\nShe clapped her hands with joy.'
        result = segment_text(text, flatten=True)
        assert result == ['How wonderful!', 'She clapped her hands with joy.']

    def test_e15_impossible(self):
        text = 'Impossible!\nHe stared in disbelief.'
        result = segment_text(text, flatten=True)
        assert result == ['Impossible!', 'He stared in disbelief.']

    def test_e16_run(self):
        text = 'Run!\nDo not look back.'
        result = segment_text(text, flatten=True)
        assert result == ['Run!', 'Do not look back.']

    def test_e17_stop(self):
        text = 'Stop!\nThis has gone too far.'
        result = segment_text(text, flatten=True)
        assert result == ['Stop!', 'This has gone too far.']

    def test_e18_forward(self):
        text = 'Forward!\nThere is no retreat.'
        result = segment_text(text, flatten=True)
        assert result == ['Forward!', 'There is no retreat.']

    def test_e19_all_is_lost(self):
        text = 'All is lost!\nOr so it seemed.'
        result = segment_text(text, flatten=True)
        assert result == ['All is lost!', 'Or so it seemed.']

    def test_e20_look(self):
        text = 'Look!\nOver there, in the shadows.'
        result = segment_text(text, flatten=True)
        assert result == ['Look!', 'Over there, in the shadows.']


# ---------------------------------------------------------------------------
# GROUP Q: Question + newline → split (REGRESSION)
# ---------------------------------------------------------------------------

class TestQuestionNewlineSplitRegression:
    """Question mark followed by newline must continue to split correctly (regression)."""

    def test_q01_are_you_ready(self):
        text = 'Are you ready?\nThen let us begin.'
        result = segment_text(text, flatten=True)
        assert result == ['Are you ready?', 'Then let us begin.']

    def test_q02_what_time(self):
        text = 'What time is it?\nThe clock shows noon.'
        result = segment_text(text, flatten=True)
        assert result == ['What time is it?', 'The clock shows noon.']

    def test_q03_who_was_there(self):
        text = 'Who was there?\nNo one could say.'
        result = segment_text(text, flatten=True)
        assert result == ['Who was there?', 'No one could say.']

    def test_q04_where_did_they_go(self):
        text = 'Where did they go?\nNo trace was left behind.'
        result = segment_text(text, flatten=True)
        assert result == ['Where did they go?', 'No trace was left behind.']

    def test_q05_why_did_she_leave(self):
        text = 'Why did she leave?\nThe question haunted him for years.'
        result = segment_text(text, flatten=True)
        assert result == ['Why did she leave?', 'The question haunted him for years.']

    def test_q06_how_did_this_happen(self):
        text = 'How did this happen?\nThe investigation would take months.'
        result = segment_text(text, flatten=True)
        assert result == ['How did this happen?', 'The investigation would take months.']

    def test_q07_to_be_or_not(self):
        text = 'To be or not to be?\nThat is the question.'
        result = segment_text(text, flatten=True)
        assert result == ['To be or not to be?', 'That is the question.']

    def test_q08_anyone_out_there(self):
        text = 'Is anyone out there?\nShe called into the darkness.'
        result = segment_text(text, flatten=True)
        assert result == ['Is anyone out there?', 'She called into the darkness.']

    def test_q09_can_you_hear_me(self):
        text = 'Can you hear me?\nHe waited for an answer.'
        result = segment_text(text, flatten=True)
        assert result == ['Can you hear me?', 'He waited for an answer.']

    def test_q10_what_does_it_mean(self):
        text = 'What does it mean?\nNone of us knew.'
        result = segment_text(text, flatten=True)
        assert result == ['What does it mean?', 'None of us knew.']

    def test_q11_will_she_come_back(self):
        text = 'Will she come back?\nOnly time would tell.'
        result = segment_text(text, flatten=True)
        assert result == ['Will she come back?', 'Only time would tell.']

    def test_q12_seen_before(self):
        text = 'Have you seen this before?\nThe detective studied the photograph.'
        result = segment_text(text, flatten=True)
        assert result == ['Have you seen this before?', 'The detective studied the photograph.']

    def test_q13_is_this_the_end(self):
        text = 'Is this the end?\nOr merely the beginning?'
        result = segment_text(text, flatten=True)
        assert result == ['Is this the end?', 'Or merely the beginning?']

    def test_q14_believe_in_fate(self):
        text = 'Do you believe in fate?\nShe asked with a wistful smile.'
        result = segment_text(text, flatten=True)
        assert result == ['Do you believe in fate?', 'She asked with a wistful smile.']

    def test_q15_what_would_you_do(self):
        text = 'What would you do?\nHe posed the question gravely.'
        result = segment_text(text, flatten=True)
        assert result == ['What would you do?', 'He posed the question gravely.']

    def test_q16_alone_in_universe(self):
        text = 'Are we alone in the universe?\nThe telescope pointed at the stars.'
        result = segment_text(text, flatten=True)
        assert result == ['Are we alone in the universe?', 'The telescope pointed at the stars.']

    def test_q17_which_path(self):
        text = 'Which path will you choose?\nBoth lead to the same destination.'
        result = segment_text(text, flatten=True)
        assert result == ['Which path will you choose?', 'Both lead to the same destination.']

    def test_q18_when_will_it_end(self):
        text = 'When will it end?\nNo one could predict the answer.'
        result = segment_text(text, flatten=True)
        assert result == ['When will it end?', 'No one could predict the answer.']

    def test_q19_was_it_worth_it(self):
        text = 'Was it worth it?\nHe could not say.'
        result = segment_text(text, flatten=True)
        assert result == ['Was it worth it?', 'He could not say.']

    def test_q20_do_you_understand(self):
        text = 'Do you understand?\nShe nodded slowly.'
        result = segment_text(text, flatten=True)
        assert result == ['Do you understand?', 'She nodded slowly.']


# ---------------------------------------------------------------------------
# GROUP N: No terminal punctuation + newline → should NOT split (REGRESSION)
# ---------------------------------------------------------------------------

class TestNoTerminalPunctNewlineMergesRegression:
    """Hard-wrapped prose with no terminal punct must remain merged (regression)."""

    def test_n01_walked_down(self):
        text = 'The man walked slowly down\nthe long and winding road.'
        result = segment_text(text, flatten=True)
        assert result == ['The man walked slowly down the long and winding road.']

    def test_n02_basket_on_head(self):
        text = 'She carried the heavy basket on\nher head, walking upright.'
        result = segment_text(text, flatten=True)
        assert result == ['She carried the heavy basket on her head, walking upright.']

    def test_n03_in_the_beginning(self):
        text = 'In the beginning God created\nthe heavens and the earth.'
        result = segment_text(text, flatten=True)
        assert result == ['In the beginning God created the heavens and the earth.']

    def test_n04_tree_in_field(self):
        text = 'The great tree stood in the\nmiddle of the field.'
        result = segment_text(text, flatten=True)
        assert result == ['The great tree stood in the middle of the field.']

    def test_n05_leather_bound_book(self):
        text = 'He opened the old leather-bound\nbook and began to read.'
        result = segment_text(text, flatten=True)
        assert result == ['He opened the old leather-bound book and began to read.']

    def test_n06_children_played(self):
        text = 'The children played happily in\nthe meadow all afternoon.'
        result = segment_text(text, flatten=True)
        assert result == ['The children played happily in the meadow all afternoon.']

    def test_n07_known_for_wisdom(self):
        text = 'She was known throughout the\nkingdom for her wisdom.'
        result = segment_text(text, flatten=True)
        assert result == ['She was known throughout the kingdom for her wisdom.']

    def test_n08_old_sailor_stories(self):
        text = 'The old sailor told his stories\nto anyone who would listen.'
        result = segment_text(text, flatten=True)
        assert result == ['The old sailor told his stories to anyone who would listen.']

    def test_n09_rain_upon_earth(self):
        text = 'Rain began to fall upon the\ndry and thirsty earth.'
        result = segment_text(text, flatten=True)
        assert result == ['Rain began to fall upon the dry and thirsty earth.']

    def test_n10_library_thousands(self):
        text = 'The library contained thousands of\nbooks on every subject imaginable.'
        result = segment_text(text, flatten=True)
        assert result == ['The library contained thousands of books on every subject imaginable.']

    def test_n11_thought_about_her(self):
        text = 'He thought about her every day\nfor the rest of his life.'
        result = segment_text(text, flatten=True)
        assert result == ['He thought about her every day for the rest of his life.']

    def test_n12_river_wound(self):
        text = 'The river wound its way through\nthe green valleys and hills.'
        result = segment_text(text, flatten=True)
        assert result == ['The river wound its way through the green valleys and hills.']

    def test_n13_eagles_circled(self):
        text = 'High above the city, eagles\ncircled on warm thermals.'
        result = segment_text(text, flatten=True)
        assert result == ['High above the city, eagles circled on warm thermals.']

    def test_n14_old_woman_remembered(self):
        text = 'The old woman remembered the\ndays of her youth fondly.'
        result = segment_text(text, flatten=True)
        assert result == ['The old woman remembered the days of her youth fondly.']

    def test_n15_stars_appeared(self):
        text = 'Stars began to appear in the\nsky as evening fell.'
        result = segment_text(text, flatten=True)
        assert result == ['Stars began to appear in the sky as evening fell.']

    def test_n16_built_his_house(self):
        text = 'He built his house with care and\nlaid the foundation on solid ground.'
        result = segment_text(text, flatten=True)
        assert result == ['He built his house with care and laid the foundation on solid ground.']

    def test_n17_dress_of_silk(self):
        text = 'She wore a dress of blue\nsilk that shimmered in the light.'
        result = segment_text(text, flatten=True)
        assert result == ['She wore a dress of blue silk that shimmered in the light.']

    def test_n18_mountain_rose(self):
        text = 'The mountain rose majestically\nfrom the surrounding plain.'
        result = segment_text(text, flatten=True)
        assert result == ['The mountain rose majestically from the surrounding plain.']

    def test_n19_smoke_from_chimney(self):
        text = 'Smoke rose from the chimney\nof the old farmhouse.'
        result = segment_text(text, flatten=True)
        assert result == ['Smoke rose from the chimney of the old farmhouse.']

    def test_n20_detective_studied(self):
        text = 'The detective studied the clues\nleft at the scene of the crime.'
        result = segment_text(text, flatten=True)
        assert result == ['The detective studied the clues left at the scene of the crime.']

    def test_n21_reached_into_pocket(self):
        text = 'He reached into his pocket and\nfound the key he had been seeking.'
        result = segment_text(text, flatten=True)
        assert result == ['He reached into his pocket and found the key he had been seeking.']

    def test_n22_book_worn_with_age(self):
        text = 'The book was worn with age, its\npages yellowed and fragile.'
        result = segment_text(text, flatten=True)
        assert result == ['The book was worn with age, its pages yellowed and fragile.']

    def test_n23_ships_in_harbor(self):
        text = 'All the ships in the harbor were\ndestroyed in the storm.'
        result = segment_text(text, flatten=True)
        assert result == ['All the ships in the harbor were destroyed in the storm.']

    def test_n24_professor_lectured(self):
        text = 'The professor lectured for an\nhour on the theory of relativity.'
        result = segment_text(text, flatten=True)
        assert result == ['The professor lectured for an hour on the theory of relativity.']

    def test_n25_walked_through_forest(self):
        text = 'They walked through the forest in\nsilence, listening to the birds.'
        result = segment_text(text, flatten=True)
        assert result == ['They walked through the forest in silence, listening to the birds.']

    def test_n26_under_the_bridge(self):
        text = 'Under the bridge, the\nwater flowed silently.'
        result = segment_text(text, flatten=True)
        assert result == ['Under the bridge, the water flowed silently.']

    def test_n27_ruins_hidden(self):
        text = 'The ancient ruins lay\nhidden beneath the jungle.'
        result = segment_text(text, flatten=True)
        assert result == ['The ancient ruins lay hidden beneath the jungle.']

    def test_n28_far_from_civilization(self):
        text = 'Far from civilization, the\nexplorers made camp.'
        result = segment_text(text, flatten=True)
        assert result == ['Far from civilization, the explorers made camp.']

    def test_n29_verdict_delivered(self):
        text = 'The verdict was delivered\nafter three hours of deliberation.'
        result = segment_text(text, flatten=True)
        assert result == ['The verdict was delivered after three hours of deliberation.']

    def test_n30_thunder_rolled(self):
        text = 'Thunder rolled across\nthe empty plain.'
        result = segment_text(text, flatten=True)
        assert result == ['Thunder rolled across the empty plain.']


# ---------------------------------------------------------------------------
# GROUP M: Multiple sequential lines (3+ lines with semicolons/colons)
# ---------------------------------------------------------------------------

class TestMultipleSequentialLines:
    """Multiple consecutive lines each ending with semicolons or colons."""

    def test_m01_veni_vidi_vici(self):
        """Three-part Latin phrase split on semicolons."""
        text = 'Veni;\nvidi;\nvici.'
        result = segment_text(text, flatten=True)
        assert result == ['Veni;', 'vidi;', 'vici.']

    def test_m02_four_line_existential(self):
        """Four-line existential verse."""
        text = 'We live;\nwe love;\nwe suffer;\nwe die.'
        result = segment_text(text, flatten=True)
        assert result == ['We live;', 'we love;', 'we suffer;', 'we die.']

    def test_m03_four_line_nature_verse(self):
        """Four-line nature verse with semicolons."""
        text = 'The night is dark;\nThe wind is cold;\nThe stars shine bright;\nThe world grows old.'
        result = segment_text(text, flatten=True)
        assert result == [
            'The night is dark;',
            'The wind is cold;',
            'The stars shine bright;',
            'The world grows old.'
        ]

    def test_m04_churchill_three_lines(self):
        """Three-line Churchill-style anaphora."""
        text = 'We shall fight on the beaches;\nwe shall fight on the landing grounds;\nwe shall fight in the fields.'
        result = segment_text(text, flatten=True)
        assert result == [
            'We shall fight on the beaches;',
            'we shall fight on the landing grounds;',
            'we shall fight in the fields.'
        ]

    def test_m05_fire_ice_silence(self):
        """Three-element sequence: fire, ice, silence."""
        text = 'First came fire;\nthen came ice;\nfinally came silence.'
        result = segment_text(text, flatten=True)
        assert result == ['First came fire;', 'then came ice;', 'finally came silence.']

    def test_m06_love_faith_courage(self):
        """Three virtues verse."""
        text = 'Love is blind;\nfaith is strong;\ncourage endures.'
        result = segment_text(text, flatten=True)
        assert result == ['Love is blind;', 'faith is strong;', 'courage endures.']

    def test_m07_seasons_verse(self):
        """Three-season verse (spring/summer/autumn)."""
        text = 'In spring the flowers bloom;\nin summer the fruit grows;\nin autumn the leaves fall.'
        result = segment_text(text, flatten=True)
        assert result == [
            'In spring the flowers bloom;',
            'in summer the fruit grows;',
            'in autumn the leaves fall.'
        ]

    def test_m08_day_night_hope(self):
        """Day/night/hope three-part verse."""
        text = 'By day we toil;\nby night we dream;\nand always we hope.'
        result = segment_text(text, flatten=True)
        assert result == ['By day we toil;', 'by night we dream;', 'and always we hope.']

    def test_m09_two_dialogues_four_lines(self):
        """Two dialogue introductions in four lines."""
        text = 'He declared:\nI am not afraid.\nShe replied:\nNeither am I.'
        result = segment_text(text, flatten=True)
        assert result == ['He declared:', 'I am not afraid.', 'She replied:', 'Neither am I.']

    def test_m10_mixed_semicolons_and_periods(self):
        """Alternating semicolons and periods across four lines."""
        text = 'The moon is high;\nthe stars are bright.\nThe night is long;\nthe day is light.'
        result = segment_text(text, flatten=True)
        assert result == [
            'The moon is high;',
            'the stars are bright.',
            'The night is long;',
            'the day is light.'
        ]

    def test_m11_five_line_verse(self):
        """Five-line verse ending with and."""
        text = 'Rise;\nshine;\nlive;\nlove;\nand be at peace.'
        result = segment_text(text, flatten=True)
        assert result == ['Rise;', 'shine;', 'live;', 'love;', 'and be at peace.']

    def test_m12_king_spoke_feast(self):
        """King introduces feast, all rejoice."""
        text = 'The king spoke:\nLet the feast begin.\nAll rejoiced.'
        result = segment_text(text, flatten=True)
        assert result == ['The king spoke:', 'Let the feast begin.', 'All rejoiced.']

    def test_m13_sonnet_18_opening(self):
        """Shakespeare Sonnet 18 opening couplet."""
        text = "Shall I compare thee to a summer's day;\nThou art more lovely and more temperate.\nRough winds do shake the darling buds of May;\nAnd summer's lease hath all too short a date."
        result = segment_text(text, flatten=True)
        assert result == [
            "Shall I compare thee to a summer's day;",
            'Thou art more lovely and more temperate.',
            "Rough winds do shake the darling buds of May;",
            "And summer's lease hath all too short a date."
        ]

    def test_m14_truth_lie_contrast(self):
        """Truth/lie contrast across four lines."""
        text = 'The truth is simple;\nthe lie is complex.\nHonesty costs little;\ndishonesty costs everything.'
        result = segment_text(text, flatten=True)
        assert result == [
            'The truth is simple;',
            'the lie is complex.',
            'Honesty costs little;',
            'dishonesty costs everything.'
        ]

    def test_m15_know_control_give(self):
        """Three-part maxim: know, control, give."""
        text = 'Know yourself;\ncontrol yourself;\ngive yourself.'
        result = segment_text(text, flatten=True)
        assert result == ['Know yourself;', 'control yourself;', 'give yourself.']

    def test_m16_she_said_he_said(self):
        """Dialogue exchange across four lines."""
        text = 'She said:\nI love you.\nHe said:\nI know.'
        result = segment_text(text, flatten=True)
        assert result == ['She said:', 'I love you.', 'He said:', 'I know.']

    def test_m17_step_one_step_two(self):
        """Instruction steps across four lines."""
        text = 'Step one:\nGather your materials.\nStep two:\nAssemble carefully.'
        result = segment_text(text, flatten=True)
        assert result == ['Step one:', 'Gather your materials.', 'Step two:', 'Assemble carefully.']

    def test_m18_eat_sleep_work_repeat(self):
        """Four-word imperative sequence."""
        text = 'Eat;\nsleep;\nwork;\nrepeat.'
        result = segment_text(text, flatten=True)
        assert result == ['Eat;', 'sleep;', 'work;', 'repeat.']

    def test_m19_hollow_men_verse(self):
        """Eliot-style hollow men verse."""
        text = 'We are the hollow men;\nwe are the stuffed men.\nLeaning together;\nheadpiece filled with straw.'
        result = segment_text(text, flatten=True)
        assert result == [
            'We are the hollow men;',
            'we are the stuffed men.',
            'Leaning together;',
            'headpiece filled with straw.'
        ]

    def test_m20_beauty_is_truth_keats(self):
        """Keats-style beauty/truth verse."""
        text = 'Beauty is truth;\ntruth beauty.\nThat is all ye know on earth;\nand all ye need to know.'
        result = segment_text(text, flatten=True)
        assert result == [
            'Beauty is truth;',
            'truth beauty.',
            'That is all ye know on earth;',
            'and all ye need to know.'
        ]

    def test_m21_read_practice_improve(self):
        """Instruction/result pairs."""
        text = 'Read:\nLearn.\nPractice:\nImprove.'
        result = segment_text(text, flatten=True)
        assert result == ['Read:', 'Learn.', 'Practice:', 'Improve.']

    def test_m22_thine_is_the_kingdom(self):
        """Lord's Prayer ending three-part doxology."""
        text = 'For thine is the kingdom;\nand the power;\nand the glory;\nfor ever and ever.'
        result = segment_text(text, flatten=True)
        assert result == [
            'For thine is the kingdom;',
            'and the power;',
            'and the glory;',
            'for ever and ever.'
        ]

    def test_m23_first_courage_then_strength(self):
        """Catalog of four virtues."""
        text = 'First comes courage;\nthen comes strength;\nthen comes wisdom;\nand finally, peace.'
        result = segment_text(text, flatten=True)
        assert result == [
            'First comes courage;',
            'then comes strength;',
            'then comes wisdom;',
            'and finally, peace.'
        ]

    def test_m24_she_ran_he_chased(self):
        """Three-part action sequence."""
        text = 'She ran;\nhe chased;\nbut she was faster.'
        result = segment_text(text, flatten=True)
        assert result == ['She ran;', 'he chased;', 'but she was faster.']

    def test_m25_call_and_response(self):
        """Question/answer call-and-response."""
        text = 'Who will help?\nAll will help.\nWho will lead?\nOne must lead.'
        result = segment_text(text, flatten=True)
        assert result == ['Who will help?', 'All will help.', 'Who will lead?', 'One must lead.']

    def test_m26_do_unto_others(self):
        """Golden Rule two-couplet verse."""
        text = 'Do unto others;\nas you would have them do unto you.\nFor this is the law;\nand the prophets.'
        result = segment_text(text, flatten=True)
        assert result == [
            'Do unto others;',
            'as you would have them do unto you.',
            'For this is the law;',
            'and the prophets.'
        ]

    def test_m27_journey_thousand_miles(self):
        """Journey proverb interspersed with short lines."""
        text = 'The journey of a thousand miles begins with a single step;\npersevere.\nEvery mountain can be climbed if you take it one step at a time;\nbelieve.'
        result = segment_text(text, flatten=True)
        assert result == [
            'The journey of a thousand miles begins with a single step;',
            'persevere.',
            'Every mountain can be climbed if you take it one step at a time;',
            'believe.'
        ]

    def test_m28_she_walks_in_beauty(self):
        """Byron she-walks-in-beauty opening couplet."""
        text = 'She walks in beauty like the night;\nOf cloudless climes and starry skies.'
        result = segment_text(text, flatten=True)
        assert result == [
            'She walks in beauty like the night;',
            'Of cloudless climes and starry skies.'
        ]

    def test_m29_proverbs_iron_sharpens(self):
        """Proverbs-style two-line verse."""
        text = 'Iron sharpens iron;\nand friend sharpens friend.'
        result = segment_text(text, flatten=True)
        assert result == ['Iron sharpens iron;', 'and friend sharpens friend.']

    def test_m30_question_answer_pairs(self):
        """Two question/answer pairs in four lines."""
        text = 'Who builds?\nThe mason builds.\nWho destroys?\nTime destroys.'
        result = segment_text(text, flatten=True)
        assert result == ['Who builds?', 'The mason builds.', 'Who destroys?', 'Time destroys.']


# ---------------------------------------------------------------------------
# GROUP MID: Semicolon in mid-sentence WITHOUT newline → must NOT split
# These are regression tests. The fix must not over-split on `;` alone.
# ---------------------------------------------------------------------------

class TestSemicolonMidSentenceNoSplit:
    """Semicolon in the middle of a single line (no newline) must NOT split."""

    def test_mid01_simple_pair(self):
        text = 'He was tall; she was short.'
        result = segment_text(text, flatten=True)
        assert result == ['He was tall; she was short.']

    def test_mid02_triple_clause(self):
        text = 'The cat slept; the dog barked; the owner sighed.'
        result = segment_text(text, flatten=True)
        assert result == ['The cat slept; the dog barked; the owner sighed.']

    def test_mid03_to_err_is_human(self):
        text = 'To err is human; to forgive divine.'
        result = segment_text(text, flatten=True)
        assert result == ['To err is human; to forgive divine.']

    def test_mid04_greatness_tricolon(self):
        text = 'Some are born great; some achieve greatness; some have greatness thrust upon them.'
        result = segment_text(text, flatten=True)
        assert result == ['Some are born great; some achieve greatness; some have greatness thrust upon them.']

    def test_mid05_cities_tricolon(self):
        text = 'Paris is beautiful; Rome is ancient; London is grand.'
        result = segment_text(text, flatten=True)
        assert result == ['Paris is beautiful; Rome is ancient; London is grand.']

    def test_mid06_deadline_missed(self):
        text = 'The deadline was Monday; they submitted Thursday.'
        result = segment_text(text, flatten=True)
        assert result == ['The deadline was Monday; they submitted Thursday.']

    def test_mid07_right_wrong(self):
        text = 'She was right; he was wrong.'
        result = segment_text(text, flatten=True)
        assert result == ['She was right; he was wrong.']

    def test_mid08_body_found(self):
        text = 'The body was found at dawn; the investigation began immediately.'
        result = segment_text(text, flatten=True)
        assert result == ['The body was found at dawn; the investigation began immediately.']

    def test_mid09_art_is_long(self):
        text = 'Art is long; life is short.'
        result = segment_text(text, flatten=True)
        assert result == ['Art is long; life is short.']

    def test_mid10_i_came_i_saw(self):
        text = 'I came; I saw; I conquered.'
        result = segment_text(text, flatten=True)
        assert result == ['I came; I saw; I conquered.']

    def test_mid11_sun_rises_sets(self):
        text = 'The sun rises; the sun sets; days pass.'
        result = segment_text(text, flatten=True)
        assert result == ['The sun rises; the sun sets; days pass.']

    def test_mid12_one_door_closes(self):
        text = 'One door closes; another opens.'
        result = segment_text(text, flatten=True)
        assert result == ['One door closes; another opens.']

    def test_mid13_mind_willing(self):
        text = 'The mind is willing; the flesh is weak.'
        result = segment_text(text, flatten=True)
        assert result == ['The mind is willing; the flesh is weak.']

    def test_mid14_dreams_inspire(self):
        text = 'Dreams inspire; reality constrains.'
        result = segment_text(text, flatten=True)
        assert result == ['Dreams inspire; reality constrains.']

    def test_mid15_evidence_clear(self):
        text = 'The evidence was clear; the verdict was just.'
        result = segment_text(text, flatten=True)
        assert result == ['The evidence was clear; the verdict was just.']

    def test_mid16_memory_fades(self):
        text = 'Memory fades; writing endures.'
        result = segment_text(text, flatten=True)
        assert result == ['Memory fades; writing endures.']

    def test_mid17_silence_is_golden(self):
        text = 'Silence is golden; speech is silver.'
        result = segment_text(text, flatten=True)
        assert result == ['Silence is golden; speech is silver.']

    def test_mid18_youth_is_fleeting(self):
        text = 'Youth is fleeting; wisdom accumulates.'
        result = segment_text(text, flatten=True)
        assert result == ['Youth is fleeting; wisdom accumulates.']

    def test_mid19_hammer_tricolon(self):
        text = 'The hammer strikes; the iron bends; the shape is formed.'
        result = segment_text(text, flatten=True)
        assert result == ['The hammer strikes; the iron bends; the shape is formed.']

    def test_mid20_fortune_favors(self):
        text = 'Fortune favors the brave; hesitation invites failure.'
        result = segment_text(text, flatten=True)
        assert result == ['Fortune favors the brave; hesitation invites failure.']

    def test_mid21_we_spoke_disagreed(self):
        text = 'We spoke; we disagreed; we parted ways.'
        result = segment_text(text, flatten=True)
        assert result == ['We spoke; we disagreed; we parted ways.']

    def test_mid22_first_rule_accuracy(self):
        text = 'The first rule is accuracy; the second is clarity.'
        result = segment_text(text, flatten=True)
        assert result == ['The first rule is accuracy; the second is clarity.']

    def test_mid23_seasons_mountains(self):
        text = 'Seasons change; people change; only the mountains remain.'
        result = segment_text(text, flatten=True)
        assert result == ['Seasons change; people change; only the mountains remain.']

    def test_mid24_knowledge_grows(self):
        text = 'Knowledge grows; wisdom deepens; understanding broadens.'
        result = segment_text(text, flatten=True)
        assert result == ['Knowledge grows; wisdom deepens; understanding broadens.']

    def test_mid25_lived_loved_died(self):
        text = 'He lived well; he loved truly; he died peacefully.'
        result = segment_text(text, flatten=True)
        assert result == ['He lived well; he loved truly; he died peacefully.']
