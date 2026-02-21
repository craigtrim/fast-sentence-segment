# -*- coding: utf-8 -*-
"""
Golden Rules Test Suite: Quote Attribution

50+ test cases for detecting when text after a closing quote is
attribution (lowercase = same sentence) vs new sentence (capitalized).

Key insight: When a quote ends with punctuation and the next word is
lowercase, it's typically attribution ("she said") and should NOT
be split into a new sentence.

Reference: pySBD Golden Rules 24-26
GitHub Issue: #17
"""
import pytest
from fast_sentence_segment import segment_text


class TestLowercaseAttribution:
    """When the word after closing quote is lowercase, it's attribution."""

    def test_single_quote_she_said(self):
        """Rule 24: Single quote with lowercase attribution."""
        text = "She turned to him, 'This is great.' she said."
        expected = ["She turned to him, 'This is great.' she said."]
        assert segment_text(text, flatten=True) == expected

    def test_double_quote_she_said(self):
        """Rule 25: Double quote with lowercase attribution."""
        text = 'She turned to him, "This is great." she said.'
        expected = ['She turned to him, "This is great." she said.']
        assert segment_text(text, flatten=True) == expected

    def test_he_said(self):
        text = '"I am here," he said.'
        expected = ['"I am here," he said.']
        assert segment_text(text, flatten=True) == expected

    def test_she_whispered(self):
        text = '"Be quiet," she whispered.'
        expected = ['"Be quiet," she whispered.']
        assert segment_text(text, flatten=True) == expected

    def test_he_replied(self):
        text = '"Yes," he replied.'
        expected = ['"Yes," he replied.']
        assert segment_text(text, flatten=True) == expected

    def test_she_asked(self):
        text = '"Are you sure?" she asked.'
        expected = ['"Are you sure?" she asked.']
        assert segment_text(text, flatten=True) == expected

    def test_he_shouted(self):
        text = '"Stop!" he shouted.'
        expected = ['"Stop!" he shouted.']
        assert segment_text(text, flatten=True) == expected

    def test_they_responded(self):
        text = '"We agree," they responded.'
        expected = ['"We agree," they responded.']
        assert segment_text(text, flatten=True) == expected

    def test_she_continued(self):
        text = '"And then," she continued, "we left."'
        expected = ['"And then," she continued, "we left."']
        assert segment_text(text, flatten=True) == expected

    def test_he_added(self):
        text = '"One more thing," he added.'
        expected = ['"One more thing," he added.']
        assert segment_text(text, flatten=True) == expected

    def test_she_murmured(self):
        text = '"I see," she murmured.'
        expected = ['"I see," she murmured.']
        assert segment_text(text, flatten=True) == expected

    def test_he_muttered(self):
        text = '"Whatever," he muttered.'
        expected = ['"Whatever," he muttered.']
        assert segment_text(text, flatten=True) == expected

    def test_she_exclaimed(self):
        text = '"How wonderful!" she exclaimed.'
        expected = ['"How wonderful!" she exclaimed.']
        assert segment_text(text, flatten=True) == expected

    def test_he_wondered(self):
        text = '"Is that so?" he wondered.'
        expected = ['"Is that so?" he wondered.']
        assert segment_text(text, flatten=True) == expected


class TestCapitalizedNewSentence:
    """When the word after closing quote is capitalized, it's a new sentence."""

    def test_capital_she(self):
        """Rule 26: Capitalized word after quote = new sentence."""
        text = 'She turned to him, "This is great." She held the book out.'
        expected = ['She turned to him, "This is great."', "She held the book out."]
        assert segment_text(text, flatten=True) == expected

    def test_capital_he(self):
        text = '"I understand." He nodded.'
        expected = ['"I understand."', "He nodded."]
        assert segment_text(text, flatten=True) == expected

    def test_capital_the(self):
        text = '"Goodbye." The door closed.'
        expected = ['"Goodbye."', "The door closed."]
        assert segment_text(text, flatten=True) == expected

    def test_capital_name(self):
        text = '"Hello." John waved.'
        expected = ['"Hello."', "John waved."]
        assert segment_text(text, flatten=True) == expected

    def test_capital_it(self):
        text = '"Done." It was over.'
        expected = ['"Done."', "It was over."]
        assert segment_text(text, flatten=True) == expected

    def test_capital_they(self):
        text = '"Let\'s go." They left immediately.'
        expected = ['"Let\'s go."', "They left immediately."]
        assert segment_text(text, flatten=True) == expected

    def test_capital_we(self):
        text = '"Agreed." We shook hands.'
        expected = ['"Agreed."', "We shook hands."]
        assert segment_text(text, flatten=True) == expected

    def test_capital_after_question(self):
        text = '"What time is it?" The clock showed noon.'
        expected = ['"What time is it?"', "The clock showed noon."]
        assert segment_text(text, flatten=True) == expected

    def test_capital_after_exclamation(self):
        text = '"Watch out!" The car swerved.'
        expected = ['"Watch out!"', "The car swerved."]
        assert segment_text(text, flatten=True) == expected


class TestMixedDialogue:
    """Mixed dialogue with attribution and new sentences."""

    def test_attribution_then_new_sentence(self):
        text = '"I see," she said. The room fell silent.'
        expected = ['"I see," she said.', "The room fell silent."]
        assert segment_text(text, flatten=True) == expected

    def test_new_sentence_then_attribution(self):
        text = 'The door opened. "Hello," she said.'
        expected = ["The door opened.", '"Hello," she said.']
        assert segment_text(text, flatten=True) == expected

    def test_multiple_quotes_mixed(self):
        text = '"First," she said. "Second." He nodded.'
        expected = ['"First," she said.', '"Second."', "He nodded."]
        assert segment_text(text, flatten=True) == expected

    def test_back_and_forth(self):
        text = '"Yes," he said. "No," she replied. They argued.'
        expected = ['"Yes," he said.', '"No," she replied.', "They argued."]
        assert segment_text(text, flatten=True) == expected

    def test_complex_dialogue(self):
        text = '"I think," she began, "that we should go." He agreed. "Let\'s leave," he said.'
        expected = ['"I think," she began, "that we should go."', "He agreed.", '"Let\'s leave," he said.']
        assert segment_text(text, flatten=True) == expected


class TestSingleQuotes:
    """Tests specifically for single-quoted dialogue."""

    def test_single_quote_lowercase(self):
        text = "'I agree,' he said."
        expected = ["'I agree,' he said."]
        assert segment_text(text, flatten=True) == expected

    def test_single_quote_capital(self):
        text = "'I agree.' He nodded."
        expected = ["'I agree.'", "He nodded."]
        assert segment_text(text, flatten=True) == expected

    def test_nested_single_double(self):
        text = "\"She said 'hello,'\" he explained."
        expected = ["\"She said 'hello,'\" he explained."]
        assert segment_text(text, flatten=True) == expected

    def test_apostrophe_vs_quote(self):
        """Apostrophe in contraction vs single quote."""
        text = "'Don't go,' she pleaded."
        expected = ["'Don't go,' she pleaded."]
        assert segment_text(text, flatten=True) == expected


class TestCurlyQuotes:
    """Tests for typographic/curly quotes."""

    def test_curly_double_attribution(self):
        text = '"This is great," she said.'
        expected = ['"This is great," she said.']
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_new_sentence(self):
        text = '"This is great." She smiled.'
        expected = ['"This is great."', "She smiled."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_attribution(self):
        text = "'This is great,' she said."
        expected = ["'This is great,' she said."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_new_sentence(self):
        text = "'This is great.' She smiled."
        expected = ["'This is great.'", "She smiled."]
        assert segment_text(text, flatten=True) == expected

    def test_mixed_curly_straight(self):
        text = '"Hello," she said. "Goodbye."'
        expected = ['"Hello," she said.', '"Goodbye."']
        assert segment_text(text, flatten=True) == expected


class TestAttributionVerbs:
    """Various attribution verbs that should be recognized."""

    def test_said(self):
        text = '"Hello," said John.'
        expected = ['"Hello," said John.']
        assert segment_text(text, flatten=True) == expected

    def test_asked(self):
        text = '"Why?" asked Mary.'
        expected = ['"Why?" asked Mary.']
        assert segment_text(text, flatten=True) == expected

    def test_replied(self):
        text = '"Because," replied Tom.'
        expected = ['"Because," replied Tom.']
        assert segment_text(text, flatten=True) == expected

    def test_answered(self):
        text = '"Yes," answered the teacher.'
        expected = ['"Yes," answered the teacher.']
        assert segment_text(text, flatten=True) == expected

    def test_whispered(self):
        text = '"Shh," whispered Sarah.'
        expected = ['"Shh," whispered Sarah.']
        assert segment_text(text, flatten=True) == expected

    def test_shouted(self):
        text = '"Run!" shouted the guard.'
        expected = ['"Run!" shouted the guard.']
        assert segment_text(text, flatten=True) == expected

    def test_cried(self):
        text = '"Help!" cried the child.'
        expected = ['"Help!" cried the child.']
        assert segment_text(text, flatten=True) == expected

    def test_called(self):
        text = '"Over here," called the guide.'
        expected = ['"Over here," called the guide.']
        assert segment_text(text, flatten=True) == expected

    def test_explained(self):
        text = '"It works like this," explained the expert.'
        expected = ['"It works like this," explained the expert.']
        assert segment_text(text, flatten=True) == expected

    def test_noted(self):
        text = '"Interesting," noted the professor.'
        expected = ['"Interesting," noted the professor.']
        assert segment_text(text, flatten=True) == expected


class TestEdgeCases:
    """Edge cases and tricky scenarios."""

    def test_quote_with_ellipsis_attribution(self):
        text = '"I wonder..." she mused.'
        expected = ['"I wonder..." she mused.']
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_ellipsis_new_sentence(self):
        text = '"I wonder..." She looked away.'
        expected = ['"I wonder..."', "She looked away."]
        assert segment_text(text, flatten=True) == expected

    def test_empty_quote(self):
        text = '"," she said.'
        expected = ['"," she said.']
        assert segment_text(text, flatten=True) == expected

    def test_quote_only_punctuation(self):
        text = '"!" he gasped.'
        expected = ['"!" he gasped.']
        assert segment_text(text, flatten=True) == expected

    def test_abbreviation_after_quote(self):
        text = '"We should go to the U.S." Dr. Smith suggested.'
        expected = ['"We should go to the U.S."', "Dr. Smith suggested."]
        assert segment_text(text, flatten=True) == expected

    def test_number_after_quote(self):
        text = '"That costs $100." 50 people complained.'
        expected = ['"That costs $100."', "50 people complained."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_attribution(self):
        text = '"I agree" (she nodded) "completely."'
        expected = ['"I agree" (she nodded) "completely."']
        assert segment_text(text, flatten=True) == expected

    def test_attribution_with_adverb(self):
        text = '"I see," she said quietly.'
        expected = ['"I see," she said quietly.']
        assert segment_text(text, flatten=True) == expected

    def test_attribution_with_clause(self):
        text = '"I see," she said, turning away.'
        expected = ['"I see," she said, turning away.']
        assert segment_text(text, flatten=True) == expected

    def test_question_lowercase_after(self):
        text = '"Is that right?" she wondered aloud.'
        expected = ['"Is that right?" she wondered aloud.']
        assert segment_text(text, flatten=True) == expected

    def test_exclamation_lowercase_after(self):
        text = '"Amazing!" she breathed.'
        expected = ['"Amazing!" she breathed.']
        assert segment_text(text, flatten=True) == expected

    def test_multiple_sentences_in_quote(self):
        text = '"First thing. Second thing," she said.'
        expected = ['"First thing. Second thing," she said.']
        assert segment_text(text, flatten=True, split_dialog=False) == expected

    def test_name_lowercase_after(self):
        """Names are capitalized but still attribution."""
        text = '"Hello," said john.'  # Intentionally lowercase
        expected = ['"Hello," said john.']
        assert segment_text(text, flatten=True) == expected

    def test_inverted_attribution(self):
        """Attribution before quote."""
        text = 'She said, "Hello."'
        expected = ['She said, "Hello."']
        assert segment_text(text, flatten=True) == expected

    def test_inverted_then_new_sentence(self):
        text = 'She said, "Hello." The room was quiet.'
        expected = ['She said, "Hello."', "The room was quiet."]
        assert segment_text(text, flatten=True) == expected
