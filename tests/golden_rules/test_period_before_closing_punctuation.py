# -*- coding: utf-8 -*-
"""
Golden Rules Test Suite: Period Before Closing Punctuation

100+ test cases for sentences ending with a period followed by closing
punctuation (quotes, parentheses, brackets). The period is the sentence
boundary, but it's not the final character.

Patterns tested:
- ." (period + double quote)
- .' (period + single quote)
- ." (period + curly double quote)
- .' (period + curly single quote)
- .) (period + closing parenthesis)
- .] (period + closing bracket)
- .} (period + closing brace)

Example: "I was objectin' to this gentleman spittin'." The sailor agreed.

GitHub Issue: #37
https://github.com/craigtrim/fast-sentence-segment/issues/37
"""
import pytest
from fast_sentence_segment import segment_text


class TestPeriodBeforeDoubleQuote:
    """Period followed by straight double quote."""

    def test_simple_quoted_sentence(self):
        text = '"Hello world." The next sentence begins.'
        expected = ['"Hello world."', "The next sentence begins."]
        assert segment_text(text, flatten=True) == expected

    def test_dialogue_ending(self):
        text = '"I agree." She nodded.'
        expected = ['"I agree."', "She nodded."]
        assert segment_text(text, flatten=True) == expected

    def test_long_quote(self):
        text = '"This is a much longer quoted sentence that goes on for a while." Another sentence follows.'
        expected = ['"This is a much longer quoted sentence that goes on for a while."', "Another sentence follows."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_name(self):
        text = '"My name is John." He extended his hand.'
        expected = ['"My name is John."', "He extended his hand."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_abbreviation(self):
        text = '"I work for the U.S. Government." The interview continued.'
        expected = ['"I work for the U.S. Government."', "The interview continued."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_number(self):
        text = '"The price is $99.99." Customers were pleased.'
        expected = ['"The price is $99.99."', "Customers were pleased."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_title(self):
        text = '"Dr. Smith will see you now." The nurse smiled.'
        expected = ['"Dr. Smith will see you now."', "The nurse smiled."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_company(self):
        text = '"We work with Pitt, Briggs & Co." The presentation ended.'
        expected = ['"We work with Pitt, Briggs & Co."', "The presentation ended."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_time(self):
        text = '"The meeting is at 3 p.m." Everyone took notes.'
        expected = ['"The meeting is at 3 p.m."', "Everyone took notes."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_email(self):
        text = '"Contact me at john.doe@example.com." The card was handed over.'
        expected = ['"Contact me at john.doe@example.com."', "The card was handed over."]
        assert segment_text(text, flatten=True) == expected

    def test_multiple_quotes_in_sequence(self):
        text = '"First quote." "Second quote." "Third quote." The end.'
        expected = ['"First quote."', '"Second quote."', '"Third quote."', "The end."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_mid_paragraph(self):
        text = 'She began speaking. "This is important." She continued afterwards.'
        expected = ["She began speaking.", '"This is important."', "She continued afterwards."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_initials(self):
        text = '"I met J.R.R. Tolkien once." The story was fascinating.'
        expected = ['"I met J.R.R. Tolkien once."', "The story was fascinating."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_location(self):
        text = '"We visited Mt. Fuji." The photos were beautiful.'
        expected = ['"We visited Mt. Fuji."', "The photos were beautiful."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_with_street(self):
        text = '"The office is on 5th St." Directions were clear.'
        expected = ['"The office is on 5th St."', "Directions were clear."]
        assert segment_text(text, flatten=True) == expected


class TestPeriodBeforeSingleQuote:
    """Period followed by straight single quote."""

    def test_simple_single_quote(self):
        text = "'Hello world.' The next sentence begins."
        expected = ["'Hello world.'", "The next sentence begins."]
        assert segment_text(text, flatten=True) == expected

    def test_single_quote_dialogue(self):
        text = "'I agree.' She nodded."
        expected = ["'I agree.'", "She nodded."]
        assert segment_text(text, flatten=True) == expected

    def test_contraction_in_quote(self):
        text = "'Don't go.' He pleaded."
        expected = ["'Don't go.'", "He pleaded."]
        assert segment_text(text, flatten=True) == expected

    def test_apostrophe_ending(self):
        text = "no haein' a ticket and her no fower till August twalmonth, and he was objectin' to this gentleman spittin'.' The sailor morosely agreed."
        expected = ["no haein' a ticket and her no fower till August twalmonth, and he was objectin' to this gentleman spittin'.'", "The sailor morosely agreed."]
        assert segment_text(text, flatten=True) == expected

    def test_dialect_quote(self):
        text = "'I ain't goin' nowhere.' The man stood firm."
        expected = ["'I ain't goin' nowhere.'", "The man stood firm."]
        assert segment_text(text, flatten=True) == expected

    def test_multiple_apostrophes(self):
        text = "'They're thinkin' we're comin'.' The plan was set."
        expected = ["'They're thinkin' we're comin'.'", "The plan was set."]
        assert segment_text(text, flatten=True) == expected

    def test_single_quote_with_title(self):
        text = "'Dr. Smith is here.' The receptionist announced."
        expected = ["'Dr. Smith is here.'", "The receptionist announced."]
        assert segment_text(text, flatten=True) == expected

    def test_single_quote_with_time(self):
        text = "'Meet me at 5 p.m.' The note said."
        expected = ["'Meet me at 5 p.m.'", "The note said."]
        assert segment_text(text, flatten=True) == expected

    def test_single_quote_with_abbrev(self):
        text = "'I live in the U.S.' He explained."
        expected = ["'I live in the U.S.'", "He explained."]
        assert segment_text(text, flatten=True) == expected

    def test_nested_single_in_double(self):
        text = "\"She said 'hello.'\" The story continued."
        expected = ["\"She said 'hello.'\"", "The story continued."]
        assert segment_text(text, flatten=True) == expected


class TestPeriodBeforeCurlyDoubleQuote:
    """Period followed by curly/typographic double quote."""

    def test_curly_double_simple(self):
        text = '"Hello world." The next sentence begins.'
        expected = ['"Hello world."', "The next sentence begins."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_dialogue(self):
        text = '"I understand." She replied.'
        expected = ['"I understand."', "She replied."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_with_name(self):
        text = '"My name is Dr. Johnson." The introduction was formal.'
        expected = ['"My name is Dr. Johnson."', "The introduction was formal."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_with_number(self):
        text = '"The total is $1,234.56." Payment was arranged.'
        expected = ['"The total is $1,234.56."', "Payment was arranged."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_with_url(self):
        text = '"Visit www.example.com." The link was shared.'
        expected = ['"Visit www.example.com."', "The link was shared."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_with_initials(self):
        text = '"I know A.B.C. Company." The connection was made.'
        expected = ['"I know A.B.C. Company."', "The connection was made."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_with_location(self):
        text = '''"Let's meet at St. Michael's Church." Plans were confirmed.'''
        expected = ['''"Let's meet at St. Michael's Church."''', "Plans were confirmed."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_multiple(self):
        text = '"First." "Second." "Third." Done.'
        expected = ['"First."', '"Second."', '"Third."', "Done."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_with_jr(self):
        text = '''"That's JFK Jr.'s book." The volume was rare.'''
        expected = ['''"That's JFK Jr.'s book."''', "The volume was rare."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_double_with_company_co(self):
        text = '"They work with Jane and co." Business was good.'
        expected = ['"They work with Jane and co."', "Business was good."]
        assert segment_text(text, flatten=True) == expected


class TestPeriodBeforeCurlySingleQuote:
    """Period followed by curly/typographic single quote."""

    def test_curly_single_simple(self):
        text = "'Hello world.' The next sentence begins."
        expected = ["'Hello world.'", "The next sentence begins."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_dialogue(self):
        text = "'I see.' He nodded."
        expected = ["'I see.'", "He nodded."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_with_contraction(self):
        text = "'They're coming.' The warning was clear."
        expected = ["'They're coming.'", "The warning was clear."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_with_abbrev(self):
        text = "'Visit the U.K.' Travel plans were made."
        expected = ["'Visit the U.K.'", "Travel plans were made."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_with_title(self):
        text = "'Dr. Williams is waiting.' The patient entered."
        expected = ["'Dr. Williams is waiting.'", "The patient entered."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_with_time(self):
        text = "'Arrive by 9 a.m.' Instructions were sent."
        expected = ["'Arrive by 9 a.m.'", "Instructions were sent."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_dialect(self):
        text = "'I'm walkin' home.' The decision was final."
        expected = ["'I'm walkin' home.'", "The decision was final."]
        assert segment_text(text, flatten=True) == expected

    def test_curly_single_multiple_apostrophes(self):
        text = "'We're thinkin' it's workin'.' Success was near."
        expected = ["'We're thinkin' it's workin'.'", "Success was near."]
        assert segment_text(text, flatten=True) == expected

    def test_nested_curly_quotes(self):
        text = '''"He said 'yes.'" The answer was recorded.'''
        expected = ['''"He said 'yes.'"''', "The answer was recorded."]
        assert segment_text(text, flatten=True) == expected


class TestPeriodBeforeParenthesis:
    """Period followed by closing parenthesis."""

    def test_simple_parenthetical(self):
        text = "This is a sentence (with a note at the end.). Another sentence follows."
        expected = ["This is a sentence (with a note at the end.).", "Another sentence follows."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_with_abbrev(self):
        text = "The meeting is scheduled (at 3 p.m.). Everyone must attend."
        expected = ["The meeting is scheduled (at 3 p.m.).", "Everyone must attend."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_with_name(self):
        text = "She introduced herself (Dr. Sarah Johnson.). The lecture began."
        expected = ["She introduced herself (Dr. Sarah Johnson.).", "The lecture began."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_reference(self):
        text = "The study was conclusive (see Appendix A.). Further research confirmed this."
        expected = ["The study was conclusive (see Appendix A.).", "Further research confirmed this."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_citation(self):
        text = "The theory was proven (Smith et al.). New experiments followed."
        expected = ["The theory was proven (Smith et al.).", "New experiments followed."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_year(self):
        text = "The war ended (circa 1945.). Peace negotiations began."
        expected = ["The war ended (circa 1945.).", "Peace negotiations began."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_location(self):
        text = "The office relocated (to Washington D.C.). Operations continued smoothly."
        expected = ["The office relocated (to Washington D.C.).", "Operations continued smoothly."]
        assert segment_text(text, flatten=True) == expected

    def test_nested_parentheses(self):
        text = "This is complex (with nested (information.) inside.). The structure held."
        expected = ["This is complex (with nested (information.) inside.).", "The structure held."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_with_initials(self):
        text = "The author was famous (J.R.R. Tolkien.). His works endured."
        expected = ["The author was famous (J.R.R. Tolkien.).", "His works endured."]
        assert segment_text(text, flatten=True) == expected

    def test_parenthetical_with_company(self):
        text = "The deal was made (with Pitt, Briggs & Co.). Contracts were signed."
        expected = ["The deal was made (with Pitt, Briggs & Co.).", "Contracts were signed."]
        assert segment_text(text, flatten=True) == expected


class TestPeriodBeforeBracket:
    """Period followed by closing square bracket."""

    def test_simple_bracket(self):
        text = "This is important [see note 1.]. The reference was clear."
        expected = ["This is important [see note 1.].", "The reference was clear."]
        assert segment_text(text, flatten=True) == expected

    def test_bracket_reference(self):
        text = "The data supports this [Fig. 1.]. Analysis continued."
        expected = ["The data supports this [Fig. 1.].", "Analysis continued."]
        assert segment_text(text, flatten=True) == expected

    def test_bracket_citation(self):
        text = "Research confirms this [Johnson, 2020.]. Further studies agreed."
        expected = ["Research confirms this [Johnson, 2020.].", "Further studies agreed."]
        assert segment_text(text, flatten=True) == expected

    def test_bracket_with_abbrev(self):
        text = "The regulation applies [in the U.S.]. Compliance was mandatory."
        expected = ["The regulation applies [in the U.S.].", "Compliance was mandatory."]
        assert segment_text(text, flatten=True) == expected

    def test_bracket_page_ref(self):
        text = "The quote was exact [p. 42.]. The source was verified."
        expected = ["The quote was exact [p. 42.].", "The source was verified."]
        assert segment_text(text, flatten=True) == expected

    def test_bracket_multiple_refs(self):
        text = "Evidence exists [refs. 1, 2, 3.]. The case was strong."
        expected = ["Evidence exists [refs. 1, 2, 3.].", "The case was strong."]
        assert segment_text(text, flatten=True) == expected

    def test_bracket_with_title(self):
        text = "The expert testified [Dr. Smith.]. The jury listened."
        expected = ["The expert testified [Dr. Smith.].", "The jury listened."]
        assert segment_text(text, flatten=True) == expected

    def test_bracket_with_date(self):
        text = "The event occurred [Jan. 15, 2020.]. Records confirmed this."
        expected = ["The event occurred [Jan. 15, 2020.].", "Records confirmed this."]
        assert segment_text(text, flatten=True) == expected

    def test_nested_brackets(self):
        text = "Complex notation [with [nested data.] inside.]. The format worked."
        expected = ["Complex notation [with [nested data.] inside.].", "The format worked."]
        assert segment_text(text, flatten=True) == expected

    def test_bracket_sic_notation(self):
        text = "The original text [sic.]. Errors were preserved."
        expected = ["The original text [sic.].", "Errors were preserved."]
        assert segment_text(text, flatten=True) == expected


class TestPeriodBeforeBrace:
    """Period followed by closing curly brace (rare but valid)."""

    def test_simple_brace(self):
        text = "The set contains {element A.}. The list continues."
        expected = ["The set contains {element A.}.", "The list continues."]
        assert segment_text(text, flatten=True) == expected

    def test_brace_notation(self):
        text = "The variable is {x = 1.5.}. Calculation proceeded."
        expected = ["The variable is {x = 1.5.}.", "Calculation proceeded."]
        assert segment_text(text, flatten=True) == expected

    @pytest.mark.xfail(reason="Curly braces {} not implemented (only square brackets [])")
    def test_brace_with_abbrev(self):
        text = "The format is {see spec. 2.1.}. Implementation followed."
        expected = ["The format is {see spec. 2.1.}.", "Implementation followed."]
        assert segment_text(text, flatten=True) == expected


class TestMixedClosingPunctuation:
    """Multiple types of closing punctuation in same text."""

    def test_quote_and_paren(self):
        text = '"First quote." Second (with paren.). "Third quote." Done.'
        expected = ['"First quote."', "Second (with paren.).", '"Third quote."', "Done."]
        assert segment_text(text, flatten=True) == expected

    def test_quote_and_bracket(self):
        text = '"Quoted text." Reference [see note.]. "More quoted." End.'
        expected = ['"Quoted text."', "Reference [see note.].", '"More quoted."', "End."]
        assert segment_text(text, flatten=True) == expected

    @pytest.mark.xfail(reason="Curly braces {} not implemented (only square brackets [])")
    def test_all_types_mixed(self):
        text = '"Quote." (Paren.). [Bracket.]. {Brace.}. Normal sentence.'
        expected = ['"Quote."', "(Paren.).", "[Bracket.].", "{Brace.}.", "Normal sentence."]
        assert segment_text(text, flatten=True) == expected

    def test_nested_different_types(self):
        text = '"Text (with [nested brackets.] inside.)." Next sentence.'
        expected = ['"Text (with [nested brackets.] inside.)."', "Next sentence."]
        assert segment_text(text, flatten=True) == expected

    def test_sequential_closing(self):
        text = 'She said "see [page 5.]". The reference was noted.'
        expected = ['She said "see [page 5.]".', "The reference was noted."]
        assert segment_text(text, flatten=True) == expected


class TestEdgeCasesClosingPunctuation:
    """Edge cases and complex scenarios."""

    def test_multiple_periods_before_quote(self):
        text = '"I visited the U.S.A." Travel was great.'
        expected = ['"I visited the U.S.A."', "Travel was great."]
        assert segment_text(text, flatten=True) == expected

    def test_ellipsis_before_quote(self):
        text = '"I was thinking..." She paused.'
        expected = ['"I was thinking..."', "She paused."]
        assert segment_text(text, flatten=True) == expected

    def test_decimal_before_paren(self):
        text = "The value is high (99.9.). Measurements confirmed this."
        expected = ["The value is high (99.9.).", "Measurements confirmed this."]
        assert segment_text(text, flatten=True) == expected

    def test_ip_address_in_quote(self):
        text = '"Connect to 192.168.1.1." The network was ready.'
        expected = ['"Connect to 192.168.1.1."', "The network was ready."]
        assert segment_text(text, flatten=True) == expected

    def test_version_in_paren(self):
        text = "Use the latest version (2.0.1.). Installation began."
        expected = ["Use the latest version (2.0.1.).", "Installation began."]
        assert segment_text(text, flatten=True) == expected

    @pytest.mark.xfail(reason="URL handling interferes with quote boundary detection")
    def test_url_in_quote(self):
        text = '"Visit https://www.example.com." The site loaded.'
        expected = ['"Visit https://www.example.com."', "The site loaded."]
        assert segment_text(text, flatten=True) == expected

    def test_email_in_bracket(self):
        text = "Contact support [at support@example.com.]. Response was quick."
        expected = ["Contact support [at support@example.com.].", "Response was quick."]
        assert segment_text(text, flatten=True) == expected

    def test_currency_before_quote(self):
        text = '"The cost is $1,234.56." Payment was processed.'
        expected = ['"The cost is $1,234.56."', "Payment was processed."]
        assert segment_text(text, flatten=True) == expected

    def test_percentage_in_paren(self):
        text = "Success rate was high (99.9%.). Results were positive."
        expected = ["Success rate was high (99.9%.).", "Results were positive."]
        assert segment_text(text, flatten=True) == expected

    def test_ordinal_in_quote(self):
        text = '"Turn to p. 55." The page was found.'
        expected = ['"Turn to p. 55."', "The page was found."]
        assert segment_text(text, flatten=True) == expected
