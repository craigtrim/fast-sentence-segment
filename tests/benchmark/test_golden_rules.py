# -*- coding: utf-8 -*-
"""
Golden Rules Benchmark Test

Tests fast-sentence-segment against the pySBD Golden Rules Set -
the standard benchmark for sentence boundary detection edge cases.

Reference: https://github.com/nipunsadvilkar/pySBD
Paper: "PySBD: Pragmatic Sentence Boundary Disambiguation" (EMNLP 2020)
"""
import pytest
from fast_sentence_segment import segment_text


# Golden Rules from pySBD - 48 edge case tests
GOLDEN_RULES = [
    # Rule 1: Simple sentences
    (1, "Hello World. My name is Jonas.",
     ["Hello World.", "My name is Jonas."]),

    # Rule 2: Question mark
    (2, "What is your name? My name is Jonas.",
     ["What is your name?", "My name is Jonas."]),

    # Rule 3: Exclamation mark
    (3, "There it is! I found it.",
     ["There it is!", "I found it."]),

    # Rule 4: Single letter abbreviation (middle initial)
    (4, "My name is Jonas E. Smith.",
     ["My name is Jonas E. Smith."]),

    # Rule 5: Page abbreviation
    (5, "Please turn to p. 55.",
     ["Please turn to p. 55."]),

    # Rule 6: Company abbreviation with question
    (6, "Were Jane and co. at the party?",
     ["Were Jane and co. at the party?"]),

    # Rule 7: Company abbreviation (& Co.)
    (7, "They closed the deal with Pitt, Briggs & Co. at noon.",
     ["They closed the deal with Pitt, Briggs & Co. at noon."]),

    # Rule 8: Company abbreviation followed by sentence
    (8, "Let's ask Jane and co. They should know.",
     ["Let's ask Jane and co.", "They should know."]),

    # Rule 9: Company abbreviation followed by "It"
    (9, "They closed the deal with Pitt, Briggs & Co. It closed yesterday.",
     ["They closed the deal with Pitt, Briggs & Co.", "It closed yesterday."]),

    # Rule 10: Mountain abbreviation
    (10, "I can see Mt. Fuji from here.",
     ["I can see Mt. Fuji from here."]),

    # Rule 11: Saint and street abbreviations
    (11, "St. Michael's Church is on 5th st. near the light.",
     ["St. Michael's Church is on 5th st. near the light."]),

    # Rule 12: Jr. with possessive
    (12, "That is JFK Jr.'s book.",
     ["That is JFK Jr.'s book."]),

    # Rule 13: U.S.A. abbreviation
    (13, "I visited the U.S.A. last year.",
     ["I visited the U.S.A. last year."]),

    # Rule 14: E.U. followed by question
    (14, "I live in the E.U. How about you?",
     ["I live in the E.U.", "How about you?"]),

    # Rule 15: U.S. followed by question
    (15, "I live in the U.S. How about you?",
     ["I live in the U.S.", "How about you?"]),

    # Rule 16: U.S. Government (no sentence break)
    (16, "I work for the U.S. Government in Virginia.",
     ["I work for the U.S. Government in Virginia."]),

    # Rule 17: U.S. followed by "for"
    (17, "I have lived in the U.S. for 20 years.",
     ["I have lived in the U.S. for 20 years."]),

    # Rule 18: THE HOLY GRAIL - a.m./p.m. with Mr./Mrs.
    # No segmenter has ever passed this one!
    (18, "At 5 a.m. Mr. Smith went to the bank. He left the bank at 6 P.M. Mr. Smith then went to the store.",
     ["At 5 a.m. Mr. Smith went to the bank.",
      "He left the bank at 6 P.M.",
      "Mr. Smith then went to the store."]),

    # Rule 19: Money with decimals
    (19, "She has $100.00 in her bag.",
     ["She has $100.00 in her bag."]),

    # Rule 20: Money followed by sentence
    (20, "She has $100.00. It is in her bag.",
     ["She has $100.00.", "It is in her bag."]),

    # Rule 21: Parenthetical sentence inside
    (21, "He teaches science (He previously worked for 5 years as an engineer.) at the local University.",
     ["He teaches science (He previously worked for 5 years as an engineer.) at the local University."]),

    # Rule 22: Email address
    (22, "Her email is Jane.Doe@example.com. I sent her an email.",
     ["Her email is Jane.Doe@example.com.", "I sent her an email."]),

    # Rule 23: URL
    (23, "The site is: https://www.example.50.com/new-site/awesome_content.html. Please check it out.",
     ["The site is: https://www.example.50.com/new-site/awesome_content.html.", "Please check it out."]),

    # Rule 24: Single quotes dialogue (no break)
    (24, "She turned to him, 'This is great.' she said.",
     ["She turned to him, 'This is great.' she said."]),

    # Rule 25: Double quotes dialogue (no break)
    (25, 'She turned to him, "This is great." she said.',
     ['She turned to him, "This is great." she said.']),

    # Rule 26: Double quotes dialogue with break
    (26, 'She turned to him, "This is great." She held the book out to show him.',
     ['She turned to him, "This is great."', "She held the book out to show him."]),

    # Rule 27: Multiple exclamation marks
    (27, "Hello!! Long time no see.",
     ["Hello!!", "Long time no see."]),

    # Rule 28: Multiple question marks
    (28, "Hello?? Who is there?",
     ["Hello??", "Who is there?"]),

    # Rule 29: Mixed !?
    (29, "Hello!? Is that you?",
     ["Hello!?", "Is that you?"]),

    # Rule 30: Mixed ?!
    (30, "Hello?! Is that you?",
     ["Hello?!", "Is that you?"]),

    # Rule 31: Numbered list with .)
    (31, "1.) The first item 2.) The second item",
     ["1.) The first item", "2.) The second item"]),

    # Rule 32: Numbered list with .) and periods
    (32, "1.) The first item. 2.) The second item.",
     ["1.) The first item.", "2.) The second item."]),

    # Rule 33: Numbered list with )
    (33, "1) The first item 2) The second item",
     ["1) The first item", "2) The second item"]),

    # Rule 34: Numbered list with ) and periods
    (34, "1) The first item. 2) The second item.",
     ["1) The first item.", "2) The second item."]),

    # Rule 35: Numbered list with .
    (35, "1. The first item 2. The second item",
     ["1. The first item", "2. The second item"]),

    # Rule 36: Numbered list with . and periods
    (36, "1. The first item. 2. The second item.",
     ["1. The first item.", "2. The second item."]),

    # Rule 37: Bullet points with numbers
    (37, "• 9. The first item • 10. The second item",
     ["• 9. The first item", "• 10. The second item"]),

    # Rule 38: Hyphen bullet points
    (38, "⁃9. The first item ⁃10. The second item",
     ["⁃9. The first item", "⁃10. The second item"]),

    # Rule 39: Alphabetical list
    (39, "a. The first item b. The second item c. The third list item",
     ["a. The first item", "b. The second item", "c. The third list item"]),

    # Rule 40: N°. number with periods
    (40, "You can find it at N°. 1026.253.553. That is where the treasure is.",
     ["You can find it at N°. 1026.253.553.", "That is where the treasure is."]),

    # Rule 41: Yahoo! company name
    (41, "She works at Yahoo! in the accounting department.",
     ["She works at Yahoo! in the accounting department."]),

    # Rule 42: "I" as word vs initial
    (42, "We make a good team, you and I. Did you see Albert I. Jones yesterday?",
     ["We make a good team, you and I.", "Did you see Albert I. Jones yesterday?"]),

    # Rule 43: Ellipsis in quotes (curly quotes)
    (43, 'Thoreau argues that by simplifying one\'s life, "the laws of the universe will appear less complex. . . ."',
     ['Thoreau argues that by simplifying one\'s life, "the laws of the universe will appear less complex. . . ."']),

    # Rule 44: Brackets with citation
    (44, '"Bohr [...] used the analogy of parallel stairways [...]" (Smith 55).',
     ['"Bohr [...] used the analogy of parallel stairways [...]" (Smith 55).']),

    # Rule 45: Ellipsis at sentence end
    (45, "If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . . Next sentence.",
     ["If words are left off at the end of a sentence, and that is all that is omitted, indicate the omission with ellipsis marks (preceded and followed by a space) and then indicate the end of the sentence with a period . . . .",
      "Next sentence."]),

    # Rule 46: Four dots ellipsis
    (46, "I never meant that.... She left the store.",
     ["I never meant that....", "She left the store."]),

    # Rule 47: Multiple ellipses mid-sentence
    (47, "I wasn't really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn't mean it.",
     ["I wasn't really ... well, what I mean...see . . . what I'm saying, the thing is . . . I didn't mean it."]),

    # Rule 48: Ellipsis spanning sentences
    (48, "One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds. . . . The practice was not abandoned. . . .",
     ["One further habit which was somewhat weakened . . . was that of combining words into self-interpreting compounds.",
      ". . . The practice was not abandoned. . . ."]),
]


class TestGoldenRules:
    """Test fast-sentence-segment against the Golden Rules benchmark."""

    @pytest.mark.parametrize("rule_num,text,expected", GOLDEN_RULES)
    def test_golden_rule(self, rule_num, text, expected):
        """Test individual golden rule.

        Note: Golden rules use split_dialog=False to match original pySBD
        expectations which keep multi-sentence quotes together.
        """
        result = segment_text(text, flatten=True, split_dialog=False)
        assert result == expected, f"Rule {rule_num} failed"


def run_benchmark():
    """Run benchmark and print detailed results."""
    passed = 0
    failed = 0
    results = []

    print("\n" + "="*80)
    print("GOLDEN RULES BENCHMARK - fast-sentence-segment")
    print("="*80 + "\n")

    for rule_num, text, expected in GOLDEN_RULES:
        try:
            result = segment_text(text, flatten=True)
            if result == expected:
                passed += 1
                status = "✓ PASS"
                results.append((rule_num, True, None))
            else:
                failed += 1
                status = "✗ FAIL"
                results.append((rule_num, False, {"expected": expected, "got": result}))
                print(f"\nRule {rule_num}: {status}")
                print(f"  Input:    {text[:70]}{'...' if len(text) > 70 else ''}")
                print(f"  Expected: {expected}")
                print(f"  Got:      {result}")
        except Exception as e:
            failed += 1
            results.append((rule_num, False, {"error": str(e)}))
            print(f"\nRule {rule_num}: ✗ ERROR - {e}")

    total = passed + failed
    accuracy = (passed / total) * 100

    print("\n" + "="*80)
    print(f"RESULTS: {passed}/{total} passed ({accuracy:.2f}%)")
    print("="*80)

    # Summary of failed rules
    if failed > 0:
        print(f"\nFailed rules: {[r[0] for r in results if not r[1]]}")

    return accuracy, results


if __name__ == "__main__":
    run_benchmark()
