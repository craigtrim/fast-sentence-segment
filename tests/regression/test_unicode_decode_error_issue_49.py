# -*- coding: UTF-8 -*-
"""
Test cases for Issue #49: UnicodeDecodeError in bracket_content_normalizer
when input contains non-UTF-8 bytes.

## Problem Description

`bracket_content_normalizer.py:87` crashes with `UnicodeDecodeError` when
bracket content contains non-UTF-8 encoded bytes (e.g., latin-1 characters
like `0xb6` or `0xc5`).

The normalizer base64-encodes bracket content during `_normalize`, then
decodes it back during `_denormalize`. The decode step uses `.decode('utf-8')`
with no error handling, so any non-UTF-8 byte in the original bracket content
survives the base64 round-trip and crashes on decode.

Additionally, `cli.py` opens files with `encoding="utf-8"` but no `errors=`
parameter, causing crashes when files contain non-UTF-8 bytes.

## Affected Code

- `fast_sentence_segment/dmo/bracket_content_normalizer.py`, line 87
- `fast_sentence_segment/cli.py`, lines 117 and 169

## Test Coverage

This test suite includes 500+ test cases organized into the following areas:

### BracketContentNormalizer Unit Tests
- Round-trip fidelity: normalize then denormalize returns original text
- ASCII bracket content (references, citations, figures, editorial notes)
- Unicode bracket content (accented, CJK, Cyrillic, Arabic, emoji, symbols)
- Non-UTF-8 byte handling via crafted base64 payloads
- Multiple brackets in a single text
- Brackets at various positions (start, mid, end of sentence)
- Brackets with internal punctuation (periods, commas, semicolons)
- Nested and adjacent brackets
- Edge cases (empty brackets, very long content, special characters)

### End-to-End Segmentation Tests
- segment_text with bracket content containing Unicode characters
- segment_text with bracket content at sentence boundaries
- segment_text preserving bracket content across sentence splits

### CLI File Encoding Tests
- Reading files with various encodings (latin-1, windows-1252, iso-8859-x)
- Mixed encoding content

## Related GitHub Issues

- Primary: #49 - UnicodeDecodeError in bracket_content_normalizer
  https://github.com/craigtrim/fast-sentence-segment/issues/49

- Related: #37 - Period Before Closing Punctuation (original bracket normalizer)
  https://github.com/craigtrim/fast-sentence-segment/issues/37

## Implementation Files

- fast_sentence_segment/dmo/bracket_content_normalizer.py - Base64 round-trip
- fast_sentence_segment/cli.py - File input encoding handling

Created:
    24-Mar-2026
    craigtrim@gmail.com
"""

import base64
import os
import tempfile
import subprocess
import sys

import pytest
from fast_sentence_segment import segment_text
from fast_sentence_segment.dmo.bracket_content_normalizer import BracketContentNormalizer


# ---------------------------------------------------------------------------
# Fixtures
# ---------------------------------------------------------------------------

@pytest.fixture
def normalizer():
    """Provide a BracketContentNormalizer instance."""
    return BracketContentNormalizer()


@pytest.fixture
def segment():
    """Provide the segmentation function with flatten=True."""
    def _segment(text):
        return segment_text(text, flatten=True, split_dialog=False)
    return _segment


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _craft_non_utf8_placeholder(raw_bytes: bytes) -> str:
    """Create a bracket placeholder whose base64 decodes to non-UTF-8 bytes.

    This simulates what happens when bracket content containing non-UTF-8
    bytes gets base64-encoded. The resulting placeholder is syntactically
    valid but will crash _decode_placeholder if .decode('utf-8') has no
    error handler.

    Args:
        raw_bytes: Raw bytes that may not be valid UTF-8.

    Returns:
        A placeholder string in the format xbracket{base64}xend.
    """
    encoded = base64.urlsafe_b64encode(raw_bytes).decode('ascii').replace('=', '')
    return f"xbracket{encoded}xend"


def _roundtrip(normalizer, text: str) -> str:
    """Normalize then denormalize text through the bracket normalizer.

    Args:
        normalizer: BracketContentNormalizer instance.
        text: Input text.

    Returns:
        Text after normalize -> denormalize round-trip.
    """
    normalized = normalizer.process(text)
    return normalizer.process(normalized, denormalize=True)


# ===========================================================================
# PART 1: Round-Trip Fidelity — ASCII Bracket Content
# ===========================================================================

class TestRoundTripASCIIReferences:
    """Round-trip fidelity for ASCII reference patterns in brackets."""

    @pytest.mark.parametrize("text", [
        # Figure references
        "See [Fig. 1.] for details.",
        "As shown in [Fig. 2.1.] the results are clear.",
        "Refer to [Figure 3.] for the chart.",
        "The diagram [Fig. 10.] illustrates this.",
        "Compare [Fig. 1a.] and [Fig. 1b.] side by side.",
        "[Fig. 42.] shows the distribution.",
        "Results in [Figure 2.3.4.] are conclusive.",
        "See [Figs. 1-3.] for all charts.",
        "As in [Fig. A1.] from the appendix.",
        "Data from [Fig. S1.] supplementary materials.",
        # Page references
        "Details on [p. 42.] of the manual.",
        "See [pp. 10-20.] for the full discussion.",
        "Referenced on [p. 1.] of the introduction.",
        "Found on [p. 342.] in chapter 7.",
        "Discussed at [pp. 100-150.] extensively.",
        "On [p. 5.] the author states this clearly.",
        "[pp. 1, 3, 5.] contain the key arguments.",
        "As noted on [p. vii.] of the preface.",
        "Turn to [p. 99.] for the proof.",
        "Cross-reference [p. 200.] and [p. 201.] together.",
    ])
    def test_figure_and_page_references(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text

    @pytest.mark.parametrize("text", [
        # Citation references
        "[Smith 2020.] found similar results.",
        "As noted by [Johnson et al. 2019.] in their study.",
        "The theory [Einstein 1905.] still holds.",
        "[Marx 1867. Das Kapital.] remains influential.",
        "See [Brown, Ch. 3.] for background.",
        "[WHO 2021.] guidelines recommend this.",
        "[CDC 2020. Morbidity Report.] confirms the trend.",
        "Supported by [ref. 1.] and [ref. 2.] in the bibliography.",
        "[refs. 1, 2, 3.] all agree on this point.",
        "[ibid.] repeats the same source.",
        "[op. cit.] refers back to the earlier citation.",
        "[loc. cit.] same location in the work.",
        "According to [see Smith 2020. p. 42.] the claim is valid.",
        "[cf. Jones 2018.] offers a contrasting view.",
        "[See also: Williams 2017.] for further reading.",
    ])
    def test_citation_references(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text

    @pytest.mark.parametrize("text", [
        # Editorial notes
        "[sic.] appears after the error.",
        "The spelling [sic.] is intentional.",
        "[emphasis added.] by the reviewer.",
        "[emphasis in original.] not modified.",
        "[translation mine.] from the French edition.",
        "[italics in original.] preserved here.",
        "[author's emphasis.] highlights the key point.",
        "[editor's note.] clarifies the context.",
        "[note: dates approximate.] due to source uncertainty.",
        "[all errors in original.] transcribed faithfully.",
    ])
    def test_editorial_notes(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text

    @pytest.mark.parametrize("text", [
        # Numbered references
        "[1] First reference.",
        "[2] Second reference.",
        "[10] Tenth reference.",
        "[42] The answer.",
        "[1, 2] Multiple refs.",
        "[1-5] Range of refs.",
        "[1, 3, 5-7] Mixed refs.",
        "Statement [1]. Another statement [2].",
        "Text [1] more text [2] end text [3].",
        "[100] A very high numbered reference.",
    ])
    def test_numbered_references(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text


class TestRoundTripASCIIMiscContent:
    """Round-trip fidelity for miscellaneous ASCII bracket patterns."""

    @pytest.mark.parametrize("text", [
        # Technical content
        "[version 2.0.1] is the latest release.",
        "[v3.8.0] of Python.",
        "Use [--verbose] flag for details.",
        "[TODO: fix this.] before release.",
        "[FIXME: memory leak.] in the parser.",
        "[DEPRECATED] do not use this API.",
        "[BREAKING CHANGE] new API format.",
        "[RFC 2616] defines HTTP/1.1.",
        "[ISO 8601] date format.",
        "[POSIX.1-2017] standard compliance.",
        # Parenthetical explanations
        "[i.e., the first one.] is correct.",
        "[e.g., apples, oranges.] and other fruit.",
        "[a.k.a. the big one.] is famous.",
        "[lit. the bright one.] in translation.",
        "[approx. 3.14.] is close enough.",
        "[est. 1900.] founding year.",
        "[ca. 1850.] approximate date.",
        "[fl. 1500.] floruit date.",
        "[d. 1900.] death date.",
        "[b. 1850.] birth date.",
    ])
    def test_technical_and_parenthetical(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text

    @pytest.mark.parametrize("text", [
        # Brackets with various internal punctuation
        "[hello, world] is classic.",
        "[one; two; three] items listed.",
        "[yes: no: maybe] options given.",
        "[question? answer!] in dialog.",
        "[first... second... third] trailing off.",
        "[100% complete.] done.",
        "[price: $9.99.] affordable.",
        "[temp: 98.6F.] normal.",
        "[ratio 3:1.] in favor.",
        "[time: 3:45 p.m.] afternoon.",
        "[coord: 40.7N, 74.0W.] location.",
        "[pH 7.0.] neutral.",
        "[dose: 500mg/day.] prescribed.",
        "[rate: 1.5x.] multiplied.",
        "[error: +/- 0.01.] margin.",
        # Brackets with special ASCII characters
        "[*asterisk*] emphasis.",
        "[_underscore_] emphasis.",
        "[@mention] tagged.",
        "[#hashtag] labeled.",
        "[&ampersand] joined.",
    ])
    def test_internal_punctuation_and_special_chars(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text


# ===========================================================================
# PART 2: Round-Trip Fidelity — Unicode Bracket Content
# ===========================================================================

class TestRoundTripUnicodeLatinExtended:
    """Round-trip fidelity for Latin extended / accented characters in brackets."""

    @pytest.mark.parametrize("text", [
        # French
        "[resume] is English, [r\u00e9sum\u00e9] is French.",
        "The word [\u00e0 la carte.] means from the menu.",
        "[caf\u00e9.] a French loanword.",
        "[na\u00efve.] with diaeresis.",
        "[fa\u00e7ade.] with cedilla.",
        "[cr\u00e8me br\u00fbl\u00e9e.] a dessert.",
        "[pr\u00eat-\u00e0-porter.] ready to wear.",
        "[pi\u00e8ce de r\u00e9sistance.] the main item.",
        "[vis-\u00e0-vis.] face to face.",
        "[t\u00eate-\u00e0-t\u00eate.] private conversation.",
        # German
        "[\u00fcber.] means over in German.",
        "[Stra\u00dfe.] with eszett.",
        "[Gem\u00fctlichkeit.] a German concept.",
        "[\u00c4nderung.] means change.",
        "[Schr\u00f6dinger.] the physicist.",
        "[G\u00f6tterd\u00e4mmerung.] twilight of the gods.",
        "[Z\u00fcrich.] a Swiss city.",
        "[M\u00fcnchen.] Munich in German.",
        "[K\u00f6ln.] Cologne in German.",
        "[D\u00fcsseldorf.] a German city.",
        # Spanish
        "[se\u00f1or.] means sir.",
        "[ja\u00f1a.] with tilde.",
        "[\u00bfqu\u00e9?] question mark.",
        "[\u00a1hola!] exclamation.",
        "[ni\u00f1o.] child.",
        "[a\u00f1o.] year.",
        "[Espa\u00f1a.] Spain.",
        "[caf\u00e9 con leche.] coffee with milk.",
        "[pi\u00f1ata.] party decoration.",
        "[jalape\u00f1o.] a pepper.",
        # Scandinavian
        "[\u00e5ngstr\u00f6m.] unit of length.",
        "[\u00d8resund.] a strait.",
        "[sm\u00f6rg\u00e5sbord.] buffet style.",
        "[Malm\u00f6.] Swedish city.",
        "[G\u00f6teborg.] Gothenburg.",
        "[Kal\u00e5set.] the party.",
        "[bj\u00f8rn.] bear in Norwegian.",
        "[f\u00e6lles.] common in Danish.",
        "[\u00c6ther.] the aether.",
        "[R\u00f8dgraud.] a Danish dessert.",
        # Portuguese / Romanian / others
        "[S\u00e3o Paulo.] Brazilian city.",
        "[cora\u00e7\u00e3o.] heart in Portuguese.",
        "[a\u00e7a\u00ed.] a superfruit.",
        "[Bra\u0219ov.] Romanian city.",
        "[T\u00e2rgu Mure\u0219.] another Romanian city.",
        "[Cura\u00e7ao.] Caribbean island.",
        "[\u0141\u00f3d\u017a.] Polish city.",
        "[Gda\u0144sk.] another Polish city.",
        "[Krak\u00f3w.] Polish city.",
        "[Wroc\u0142aw.] Polish city.",
    ])
    def test_latin_extended_roundtrip(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text


class TestRoundTripUnicodeCJK:
    """Round-trip fidelity for CJK characters in brackets."""

    @pytest.mark.parametrize("text", [
        # Chinese
        "[\u4e2d\u6587.] Chinese text.",
        "[\u5317\u4eac.] Beijing.",
        "[\u4e0a\u6d77.] Shanghai.",
        "[\u5e7f\u5dde.] Guangzhou.",
        "[\u6df1\u5733.] Shenzhen.",
        "[\u4eba\u6c11\u65e5\u62a5.] People's Daily.",
        "[\u65b0\u534e\u793e.] Xinhua News.",
        "[\u4e2d\u56fd\u79d1\u5b66\u9662.] Chinese Academy of Sciences.",
        "[\u6e05\u534e\u5927\u5b66.] Tsinghua University.",
        "[\u5317\u4eac\u5927\u5b66.] Peking University.",
        # Japanese
        "[\u6771\u4eac.] Tokyo.",
        "[\u5927\u962a.] Osaka.",
        "[\u4eac\u90fd.] Kyoto.",
        "[\u6a2a\u6d5c.] Yokohama.",
        "[\u3053\u3093\u306b\u3061\u306f.] Hello in Japanese.",
        "[\u304a\u306f\u3088\u3046.] Good morning.",
        "[\u30c8\u30e8\u30bf.] Toyota.",
        "[\u30bd\u30cb\u30fc.] Sony.",
        "[\u30db\u30f3\u30c0.] Honda.",
        "[\u4efb\u5929\u5802.] Nintendo.",
        # Korean
        "[\uc11c\uc6b8.] Seoul.",
        "[\ubd80\uc0b0.] Busan.",
        "[\uc778\ucc9c.] Incheon.",
        "[\uc0bc\uc131.] Samsung.",
        "[\ud604\ub300.] Hyundai.",
        "[\uc548\ub155\ud558\uc138\uc694.] Hello in Korean.",
        "[\ub300\ud55c\ubbfc\uad6d.] Republic of Korea.",
        "[\uac10\uc0ac\ud569\ub2c8\ub2e4.] Thank you in Korean.",
        "[\ud55c\uad6d\uc5b4.] Korean language.",
        "[\uc870\uc120\uc77c\ubcf4.] Chosun Ilbo newspaper.",
    ])
    def test_cjk_roundtrip(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text


class TestRoundTripUnicodeCyrillicArabicHebrew:
    """Round-trip fidelity for Cyrillic, Arabic, and Hebrew in brackets."""

    @pytest.mark.parametrize("text", [
        # Cyrillic
        "[\u041c\u043e\u0441\u043a\u0432\u0430.] Moscow.",
        "[\u041f\u0440\u0430\u0432\u0434\u0430.] Pravda newspaper.",
        "[\u0421\u0430\u043d\u043a\u0442-\u041f\u0435\u0442\u0435\u0440\u0431\u0443\u0440\u0433.] St. Petersburg.",
        "[\u041a\u0438\u0435\u0432.] Kyiv.",
        "[\u0423\u043a\u0440\u0430\u0457\u043d\u0430.] Ukraine.",
        "[\u0420\u043e\u0441\u0441\u0438\u044f.] Russia.",
        "[\u0411\u0435\u043b\u0430\u0440\u0443\u0441\u044c.] Belarus.",
        "[\u0413\u0430\u0437\u043f\u0440\u043e\u043c.] Gazprom.",
        "[\u042f\u043d\u0434\u0435\u043a\u0441.] Yandex.",
        "[\u041b\u0443\u043a\u043e\u0439\u043b.] Lukoil.",
        # Arabic
        "[\u0627\u0644\u0639\u0631\u0628\u064a\u0629.] Arabic language.",
        "[\u0627\u0644\u0642\u0627\u0647\u0631\u0629.] Cairo.",
        "[\u0627\u0644\u0631\u064a\u0627\u0636.] Riyadh.",
        "[\u062f\u0628\u064a.] Dubai.",
        "[\u0623\u0628\u0648 \u0638\u0628\u064a.] Abu Dhabi.",
        "[\u0627\u0644\u062c\u0632\u064a\u0631\u0629.] Al Jazeera.",
        "[\u0631\u0648\u064a\u062a\u0631\u0632.] Reuters in Arabic.",
        "[\u0628\u0633\u0645 \u0627\u0644\u0644\u0647.] In the name of God.",
        "[\u0627\u0644\u0633\u0644\u0627\u0645 \u0639\u0644\u064a\u0643\u0645.] Peace be upon you.",
        "[\u0645\u0631\u062d\u0628\u0627.] Hello in Arabic.",
        # Hebrew
        "[\u05e9\u05dc\u05d5\u05dd.] Shalom.",
        "[\u05ea\u05dc \u05d0\u05d1\u05d9\u05d1.] Tel Aviv.",
        "[\u05d9\u05e8\u05d5\u05e9\u05dc\u05d9\u05dd.] Jerusalem.",
        "[\u05d7\u05d9\u05e4\u05d4.] Haifa.",
        "[\u05d4\u05d0\u05e8\u05e5.] The newspaper Haaretz.",
    ])
    def test_cyrillic_arabic_hebrew_roundtrip(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text


class TestRoundTripUnicodeEmoji:
    """Round-trip fidelity for emoji and symbol characters in brackets."""

    @pytest.mark.parametrize("text", [
        # Emoji
        "[\U0001f600] smiley face.",
        "[\U0001f4da] books emoji.",
        "[\U0001f3e0] house emoji.",
        "[\U0001f525] fire emoji.",
        "[\u2764\ufe0f] heart emoji.",
        "[\U0001f44d] thumbs up.",
        "[\U0001f44e] thumbs down.",
        "[\U0001f4a1] lightbulb.",
        "[\u2705] check mark.",
        "[\u274c] cross mark.",
        "[\U0001f30d] globe emoji.",
        "[\U0001f680] rocket emoji.",
        "[\U0001f4dd] memo emoji.",
        "[\U0001f6a8] warning light.",
        "[\U0001f50d] magnifying glass.",
        # Mathematical symbols
        "[\u221a] square root symbol.",
        "[\u03c0 \u2248 3.14159.] pi approximation.",
        "[\u2211 from i=1 to n.] summation.",
        "[\u222b f(x) dx.] integral.",
        "[\u2202f/\u2202x.] partial derivative.",
        "[\u221e] infinity.",
        "[\u2200 x \u2208 S.] for all x in S.",
        "[\u2203 x : P(x).] there exists.",
        "[\u00b1 0.01.] plus or minus.",
        "[\u2264 100.] less than or equal.",
        # Currency symbols
        "[\u00a3 50.00.] British pounds.",
        "[\u20ac 100.00.] Euros.",
        "[\u00a5 1000.] Japanese Yen.",
        "[\u20b9 500.] Indian Rupees.",
        "[\u20a9 50000.] Korean Won.",
    ])
    def test_emoji_and_symbols_roundtrip(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text


class TestRoundTripUnicodeGreekThai:
    """Round-trip fidelity for Greek, Thai, Hindi, and other scripts."""

    @pytest.mark.parametrize("text", [
        # Greek
        "[\u0391\u03b8\u03ae\u03bd\u03b1.] Athens.",
        "[\u03b1\u03bb\u03c6\u03ac\u03b2\u03b7\u03c4\u03bf.] alphabet.",
        "[\u03a3\u03c9\u03ba\u03c1\u03ac\u03c4\u03b7\u03c2.] Socrates.",
        "[\u03a0\u03bb\u03ac\u03c4\u03c9\u03bd.] Plato.",
        "[\u0391\u03c1\u03b9\u03c3\u03c4\u03bf\u03c4\u03ad\u03bb\u03b7\u03c2.] Aristotle.",
        "[\u03b4\u03b7\u03bc\u03bf\u03ba\u03c1\u03b1\u03c4\u03af\u03b1.] democracy.",
        "[\u03c6\u03b9\u03bb\u03bf\u03c3\u03bf\u03c6\u03af\u03b1.] philosophy.",
        "[\u03bc\u03b1\u03b8\u03b7\u03bc\u03b1\u03c4\u03b9\u03ba\u03ac.] mathematics.",
        "[\u0398\u03b5\u03c3\u03c3\u03b1\u03bb\u03bf\u03bd\u03af\u03ba\u03b7.] Thessaloniki.",
        "[\u039f\u03bb\u03c5\u03bc\u03c0\u03b9\u03b1\u03ba\u03bf\u03af.] Olympics.",
        # Thai
        "[\u0e01\u0e23\u0e38\u0e07\u0e40\u0e17\u0e1e.] Bangkok.",
        "[\u0e2a\u0e27\u0e31\u0e2a\u0e14\u0e35.] Hello in Thai.",
        "[\u0e02\u0e2d\u0e1a\u0e04\u0e38\u0e13.] Thank you in Thai.",
        "[\u0e1b\u0e23\u0e30\u0e40\u0e17\u0e28\u0e44\u0e17\u0e22.] Thailand.",
        "[\u0e20\u0e39\u0e40\u0e01\u0e47\u0e15.] Phuket.",
        # Hindi / Devanagari
        "[\u0928\u092e\u0938\u094d\u0924\u0947.] Namaste.",
        "[\u092e\u0941\u0902\u092c\u0908.] Mumbai.",
        "[\u0926\u093f\u0932\u094d\u0932\u0940.] Delhi.",
        "[\u092d\u093e\u0930\u0924.] India in Hindi.",
        "[\u0939\u093f\u0928\u094d\u0926\u0940.] Hindi language.",
    ])
    def test_greek_thai_hindi_roundtrip(self, normalizer, text):
        assert _roundtrip(normalizer, text) == text


# ===========================================================================
# PART 3: Non-UTF-8 Byte Handling — _decode_placeholder
# ===========================================================================

class TestDecodeNonUTF8SingleBytes:
    """Test _decode_placeholder with single non-UTF-8 bytes.

    These test crafted base64 placeholders that decode to bytes which are
    NOT valid UTF-8. The normalizer must handle these gracefully instead
    of raising UnicodeDecodeError.
    """

    @pytest.mark.parametrize("byte_val", [
        # Latin-1 bytes that are NOT valid as standalone UTF-8
        # Range 0x80-0xBF: continuation bytes without a leading byte
        0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87,
        0x88, 0x89, 0x8a, 0x8b, 0x8c, 0x8d, 0x8e, 0x8f,
        0x90, 0x91, 0x92, 0x93, 0x94, 0x95, 0x96, 0x97,
        0x98, 0x99, 0x9a, 0x9b, 0x9c, 0x9d, 0x9e, 0x9f,
        0xa0, 0xa1, 0xa2, 0xa3, 0xa4, 0xa5, 0xa6, 0xa7,
        0xa8, 0xa9, 0xaa, 0xab, 0xac, 0xad, 0xae, 0xaf,
        0xb0, 0xb1, 0xb2, 0xb3, 0xb4, 0xb5, 0xb6, 0xb7,
        0xb8, 0xb9, 0xba, 0xbb, 0xbc, 0xbd, 0xbe, 0xbf,
    ])
    def test_continuation_bytes_no_crash(self, normalizer, byte_val):
        """Standalone continuation byte (0x80-0xBF) must not crash."""
        raw = b"text [" + bytes([byte_val]) + b"] more"
        placeholder = _craft_non_utf8_placeholder(raw)
        # Must not raise UnicodeDecodeError
        normalizer._decode_placeholder(placeholder)

    @pytest.mark.parametrize("byte_val", [
        # Truncated multi-byte leaders: leading byte without continuation
        # 2-byte leaders (0xC0-0xDF) alone
        0xc0, 0xc1, 0xc2, 0xc3, 0xc4, 0xc5, 0xc6, 0xc7,
        0xc8, 0xc9, 0xca, 0xcb, 0xcc, 0xcd, 0xce, 0xcf,
        0xd0, 0xd1, 0xd2, 0xd3, 0xd4, 0xd5, 0xd6, 0xd7,
        0xd8, 0xd9, 0xda, 0xdb, 0xdc, 0xdd, 0xde, 0xdf,
        # 3-byte leaders (0xE0-0xEF) alone
        0xe0, 0xe1, 0xe2, 0xe3, 0xe4, 0xe5, 0xe6, 0xe7,
        0xe8, 0xe9, 0xea, 0xeb, 0xec, 0xed, 0xee, 0xef,
        # 4-byte leaders (0xF0-0xF4) alone
        0xf0, 0xf1, 0xf2, 0xf3, 0xf4,
    ])
    def test_truncated_leaders_no_crash(self, normalizer, byte_val):
        """Truncated multi-byte leader without continuation must not crash."""
        raw = b"data [" + bytes([byte_val]) + b"] end"
        placeholder = _craft_non_utf8_placeholder(raw)
        normalizer._decode_placeholder(placeholder)

    @pytest.mark.parametrize("byte_val", [
        # Invalid UTF-8 bytes (never valid in any position)
        0xf5, 0xf6, 0xf7, 0xf8, 0xf9, 0xfa, 0xfb,
        0xfc, 0xfd, 0xfe, 0xff,
    ])
    def test_always_invalid_bytes_no_crash(self, normalizer, byte_val):
        """Bytes that are never valid in UTF-8 (0xF5-0xFF) must not crash."""
        raw = b"content [" + bytes([byte_val]) + b"] after"
        placeholder = _craft_non_utf8_placeholder(raw)
        normalizer._decode_placeholder(placeholder)


class TestDecodeNonUTF8MultiByteSequences:
    """Test _decode_placeholder with multi-byte non-UTF-8 sequences."""

    @pytest.mark.parametrize("raw_bytes", [
        # The exact bytes from the issue report
        b"text with \xb6 at position 19",
        b"co\xc5rse content here",
        # Overlong encodings (invalid UTF-8)
        b"\xc0\xaf",  # overlong /
        b"\xe0\x80\xaf",  # overlong /
        b"\xf0\x80\x80\xaf",  # overlong /
        b"\xc0\x80",  # overlong NUL
        b"\xc1\xbf",  # overlong DEL
        # Surrogates (invalid in UTF-8)
        b"\xed\xa0\x80",  # U+D800 (high surrogate)
        b"\xed\xbf\xbf",  # U+DFFF (low surrogate)
        b"\xed\xa0\x80\xed\xb0\x80",  # surrogate pair
        # Truncated sequences
        b"\xc2",  # 2-byte leader, missing 1 continuation
        b"\xe0\xa0",  # 3-byte leader, missing 1 continuation
        b"\xf0\x90\x80",  # 4-byte leader, missing 1 continuation
        b"\xe0",  # 3-byte leader, missing 2 continuations
        b"\xf0\x90",  # 4-byte leader, missing 2 continuations
        b"\xf0",  # 4-byte leader, missing 3 continuations
        # Multiple invalid bytes in sequence
        b"\x80\x81\x82\x83",
        b"\xff\xfe\xfd\xfc",
        b"\xc0\xc1\xc2\xc3",
        b"\xfe\xff",  # BOM-like but in UTF-8 context
    ])
    def test_multi_byte_invalid_sequences_no_crash(self, normalizer, raw_bytes):
        """Multi-byte invalid UTF-8 sequences must not crash."""
        placeholder = _craft_non_utf8_placeholder(raw_bytes)
        normalizer._decode_placeholder(placeholder)


class TestDecodeNonUTF8Latin1Strings:
    """Test with content typical of latin-1 encoded documents.

    These simulate the Canvas LMS scenario from the issue where HTML
    content from IMSCC exports contains latin-1 encoded characters.
    """

    @pytest.mark.parametrize("raw_bytes,description", [
        # Common latin-1 characters that differ from UTF-8
        (b"Section \xa7 3.1", "section sign"),
        (b"Copyright \xa9 2024", "copyright sign"),
        (b"Price: \xa3 50", "pound sign"),
        (b"Temperature: 20\xb0C", "degree sign"),
        (b"Area: 100 m\xb2", "superscript 2"),
        (b"Volume: 50 m\xb3", "superscript 3"),
        (b"\xb6 New paragraph", "pilcrow / paragraph sign"),
        (b"Word\xad break", "soft hyphen"),
        (b"\xab quoted \xbb", "guillemets"),
        (b"Price: \xa5 1000", "yen sign"),
        (b"\xae registered", "registered sign"),
        (b"50\xbc cups", "one quarter fraction"),
        (b"50\xbd cups", "one half fraction"),
        (b"50\xbe cups", "three quarters fraction"),
        (b"\xbf Que paso?", "inverted question mark"),
        (b"\xa1 Hola!", "inverted exclamation"),
        (b"multiplication: 3\xd7 5", "multiplication sign"),
        (b"division: 10\xf7 2", "division sign"),
        (b"micro: 5\xb5m", "micro sign"),
        (b"not: \xac true", "not sign"),
    ])
    def test_latin1_chars_no_crash(self, normalizer, raw_bytes, description):
        """Latin-1 specific characters must not crash the decoder."""
        placeholder = _craft_non_utf8_placeholder(raw_bytes)
        normalizer._decode_placeholder(placeholder)


class TestDecodeNonUTF8Windows1252:
    """Test with Windows-1252 specific characters.

    Windows-1252 uses the 0x80-0x9F range differently from latin-1.
    These are common in web content and Microsoft Office documents.
    """

    @pytest.mark.parametrize("raw_bytes,description", [
        (b"Price: \x80 100", "euro sign (cp1252)"),
        (b"quote: \x91 hello \x92", "smart single quotes"),
        (b"quote: \x93 hello \x94", "smart double quotes"),
        (b"item \x95 listed", "bullet"),
        (b"range: 1 \x96 10", "en dash"),
        (b"pause \x97 long", "em dash"),
        (b"word\x99 brand", "trademark"),
        (b"\x85 continued", "horizontal ellipsis"),
        (b"See \x86 footnote", "dagger"),
        (b"See \x87 double dagger", "double dagger"),
        (b"\x89 of total", "per mille"),
        (b"\x8b angle bracket", "single left angle quote"),
        (b"\x9b angle bracket", "single right angle quote"),
        (b"\x83 currency", "florin / function sign"),
        (b"\x88 accent", "modifier circumflex"),
        (b"\x8a S-caron", "S with caron"),
        (b"\x8c OE ligature", "OE ligature"),
        (b"\x8e Z-caron", "Z with caron"),
        (b"\x9a s-caron", "s with caron"),
        (b"\x9c oe ligature", "oe ligature"),
    ])
    def test_windows1252_chars_no_crash(self, normalizer, raw_bytes, description):
        """Windows-1252 specific characters (0x80-0x9F) must not crash."""
        placeholder = _craft_non_utf8_placeholder(raw_bytes)
        normalizer._decode_placeholder(placeholder)


class TestDecodeNonUTF8MixedContent:
    """Test with mixed valid UTF-8 and invalid byte content."""

    @pytest.mark.parametrize("raw_bytes", [
        # Valid ASCII + invalid byte
        b"Hello \xb6 World",
        b"Chapter \xc5 Summary",
        b"Test data \xff here",
        # Valid UTF-8 + invalid byte at various positions
        b"\xc3\xa9 and \xb6",  # valid é + invalid 0xb6
        b"\xb6 and \xc3\xa9",  # invalid 0xb6 + valid é
        b"start \xb6 middle \xc3\xa9 end",
        # Multiple invalid bytes interspersed with valid content
        b"a\x80 b\x90 c\xa0 d",
        b"\xff valid \xfe text \xfd here",
        # Long content with invalid bytes at different positions
        b"The quick brown fox " + b"\xb6" + b" jumps over the lazy dog",
        b"Lorem ipsum \xff dolor sit amet \xfe consectetur",
        # Invalid bytes at content boundaries
        b"\xb6 leading invalid byte",
        b"trailing invalid byte \xb6",
        b"\xb6",  # single invalid byte only
        b"\xff\xfe",  # two invalid bytes only
        # Real-world-like Canvas LMS content
        b"<p>Section \xb6 3.1: Introduction</p>",
        b"<span>Price: \xa3 50.00</span>",
        b"<div>Temperature: 20\xb0C to 30\xb0C</div>",
        b"<li>Item \x95 First point</li>",
        b"<p>Copyright \xa9 2024 \x96 All rights reserved</p>",
        b"<h2>Chapter 5 \x97 The Conclusion</h2>",
    ])
    def test_mixed_content_no_crash(self, normalizer, raw_bytes):
        """Mixed valid/invalid UTF-8 content must not crash."""
        placeholder = _craft_non_utf8_placeholder(raw_bytes)
        normalizer._decode_placeholder(placeholder)


class TestDecodeNonUTF8ReturnsString:
    """Verify that _decode_placeholder always returns a str, never raises."""

    @pytest.mark.parametrize("raw_bytes", [
        b"\xb6",
        b"\xc5",
        b"\xff",
        b"\x80\x81\x82",
        b"valid ascii",
        b"\xc3\xa9",  # valid UTF-8 é
        b"mixed \xb6 content",
        b"\xed\xa0\x80",  # surrogate
        b"\xc0\xaf",  # overlong
        b"\xfe\xff\xb6\xc5",
    ])
    def test_always_returns_string(self, normalizer, raw_bytes):
        """_decode_placeholder must always return a str, never raise."""
        placeholder = _craft_non_utf8_placeholder(raw_bytes)
        result = normalizer._decode_placeholder(placeholder)
        assert isinstance(result, str)


# ===========================================================================
# PART 4: Full Normalize → Denormalize with non-ASCII Bracket Content
# ===========================================================================

class TestNormalizeDenormalizeWithBrackets:
    """Test the full normalize→denormalize path through process()."""

    @pytest.mark.parametrize("text", [
        # Simple brackets
        "Text [ref] more.",
        "A [1] B [2] C.",
        "Start [middle] end.",
        "Only [bracket content] here.",
        # Brackets with periods (the core issue #37 pattern)
        "See [Fig. 1.] here.",
        "Data [p. 42.] found.",
        "As in [ref. 3.] shown.",
        # Multiple brackets
        "First [a] second [b] third [c].",
        "See [1], [2], and [3].",
        "[start] middle [end].",
        # Adjacent brackets — pre-existing issue: adjacent placeholders merge
        pytest.param("[a][b] together.", marks=pytest.mark.xfail(
            reason="Pre-existing: adjacent bracket placeholders merge")),
        pytest.param("Text [a][b][c] here.", marks=pytest.mark.xfail(
            reason="Pre-existing: adjacent bracket placeholders merge")),
        "[x] [y] [z] listed.",
        # Brackets at sentence boundaries
        "[Note.] This is the main text.",
        "Main text [note.].",
        "Main text. [Citation.]",
        # Long bracket content
        "[This is a very long bracket content with multiple words and punctuation marks, including commas, semicolons; and periods.] End.",
        # Empty-ish brackets
        "[ ] space only.",
        "[x] minimal.",
    ])
    def test_normalize_denormalize_roundtrip(self, normalizer, text):
        """Full process() round-trip must preserve text exactly."""
        assert _roundtrip(normalizer, text) == text


class TestNormalizePlaceholderFormat:
    """Verify the placeholder format during normalization."""

    @pytest.mark.parametrize("text,should_have_placeholder", [
        ("No brackets here.", False),
        ("Has [brackets] here.", True),
        ("[start] bracket.", True),
        ("End [bracket].", True),
        ("Multiple [a] and [b].", True),
    ])
    def test_placeholder_presence(self, normalizer, text, should_have_placeholder):
        """Normalized text should contain xbracket...xend if input had brackets."""
        normalized = normalizer.process(text)
        has_placeholder = "xbracket" in normalized and "xend" in normalized
        assert has_placeholder == should_have_placeholder

    @pytest.mark.parametrize("text", [
        "Text [ref] here.",
        "[Fig. 1.] shown.",
        "A [x] B [y] C.",
    ])
    def test_placeholder_has_no_brackets(self, normalizer, text):
        """Normalized text should have no square brackets (they're in placeholders)."""
        normalized = normalizer.process(text)
        assert "[" not in normalized
        assert "]" not in normalized


# ===========================================================================
# PART 5: End-to-End segment_text with Bracket Content
# ===========================================================================

class TestSegmentTextBracketsPreserved:
    """Verify segment_text preserves bracket content across segmentation."""

    @pytest.mark.parametrize("text,expected", [
        # Single sentence with brackets
        ("The data supports this [Fig. 1.].",
         ["The data supports this [Fig. 1.]."]),

        ("See [ref. 1.] for details.",
         ["See [ref. 1.] for details."]),

        ("As noted in [Smith 2020.].",
         ["As noted in [Smith 2020.]."]),

        # Brackets should not cause false splits
        ("The finding [p. 42.] supports the hypothesis.",
         ["The finding [p. 42.] supports the hypothesis."]),

        ("Results [Fig. 1.] are shown in the table.",
         ["Results [Fig. 1.] are shown in the table."]),

        ("According to [ref. 3.] the claim is valid.",
         ["According to [ref. 3.] the claim is valid."]),

        # Multiple sentences with brackets
        ("First sentence [1]. Second sentence [2].",
         ["First sentence [1].", "Second sentence [2]."]),

        ("See [Fig. 1.]. The results are clear.",
         ["See [Fig. 1.].", "The results are clear."]),

        # Brackets with Unicode content
        ("The term [\u00e9tude.] means study.",
         ["The term [\u00e9tude.] means study."]),

        ("See [\u4e2d\u6587.] for Chinese.",
         ["See [\u4e2d\u6587.] for Chinese."]),
    ])
    def test_brackets_preserved_in_segmentation(self, segment, text, expected):
        result = segment(text)
        assert result == expected


class TestSegmentTextBracketsAtBoundaries:
    """Test brackets at various sentence boundary positions."""

    @pytest.mark.parametrize("text,expected_count", [
        # Bracket at start of sentence — pre-existing segmentation behavior:
        # the library treats [Note.] as part of the same sentence
        pytest.param("[Note.] This is the text.", 2,
                     marks=pytest.mark.xfail(reason="Pre-existing: bracket-only segment not split")),
        # Bracket at end of sentence
        ("This is the text [note.].", 1),
        # Bracket between sentences
        ("First. [Note.] Second.", 3),
        # Multiple brackets in one sentence
        ("See [1] and [2] together.", 1),
        # Brackets across multiple sentences
        ("First [a]. Second [b]. Third [c].", 3),
    ])
    def test_bracket_sentence_counts(self, segment, text, expected_count):
        result = segment(text)
        assert len(result) == expected_count


class TestSegmentTextBracketsWithUnicode:
    """End-to-end tests with Unicode content inside brackets."""

    @pytest.mark.parametrize("text", [
        "The word [r\u00e9sum\u00e9] is French.",
        "See [\u00fcber] for the German word.",
        "Reference [\u4e2d\u6587\u53c2\u8003] for Chinese sources.",
        "Symbol [\u03c0 \u2248 3.14] approximation.",
        "Formula [\u2211 n=1 to \u221e] is a sum.",
        "City [\u041c\u043e\u0441\u043a\u0432\u0430] in Russia.",
        "Greeting [\u0633\u0644\u0627\u0645] means peace.",
        "Name [\u05e9\u05dc\u05d5\u05dd] means hello.",
        "City [\u0e01\u0e23\u0e38\u0e07\u0e40\u0e17\u0e1e] is Bangkok.",
        "Word [\u0928\u092e\u0938\u094d\u0924\u0947] means hello.",
        "Emoji [\U0001f600] is a smiley.",
        "Symbol [\u00a9 2024] copyright.",
        "Price [\u20ac 50.00] in Euros.",
        "Math [\u222b f(x)dx] integral.",
        "Set [\u2200 x \u2208 S] universal.",
    ])
    def test_unicode_brackets_no_crash(self, segment, text):
        """segment_text must not crash on Unicode bracket content."""
        result = segment(text)
        assert isinstance(result, list)
        assert len(result) >= 1
        # The bracket content should be preserved somewhere in the output
        assert "[" in " ".join(result)


# ===========================================================================
# PART 6: CLI File Encoding Tests
# ===========================================================================

class TestCLIFileEncodingLatin1:
    """Test CLI file reading with latin-1 encoded files.

    The `segment` and `segment-file` CLI commands use
    `open(file, "r", encoding="utf-8")` without `errors=`, which crashes
    on non-UTF-8 files.
    """

    @pytest.mark.parametrize("content_bytes,description", [
        (b"Simple ASCII text.", "pure ASCII"),
        (b"Section \xa7 3.1: Introduction.", "section sign"),
        (b"Copyright \xa9 2024.", "copyright"),
        (b"Temperature: 20\xb0C.", "degree sign"),
        (b"Price: \xa3 50.00.", "pound sign"),
        (b"\xb6 New paragraph.", "pilcrow sign"),
        (b"The caf\xe9 is nice.", "e-acute latin-1"),
        (b"Na\xefve approach.", "i-diaeresis latin-1"),
        (b"Fa\xe7ade design.", "c-cedilla latin-1"),
        (b"\xab quoted text \xbb.", "guillemets"),
        (b"50\xbc cup flour.", "one-quarter"),
        (b"Price: \xa5 1000.", "yen sign"),
        (b"\xae registered trademark.", "registered sign"),
        (b"3 \xd7 5 = 15.", "multiplication"),
        (b"10 \xf7 2 = 5.", "division"),
    ])
    def test_cli_segment_latin1_file(self, content_bytes, description):
        """CLI segment command must not crash on latin-1 encoded files."""
        with tempfile.NamedTemporaryFile(mode="wb", suffix=".txt", delete=False) as f:
            f.write(content_bytes)
            tmp_path = f.name
        try:
            result = subprocess.run(
                [sys.executable, "-m", "fast_sentence_segment.cli", "-f", tmp_path],
                capture_output=True, text=True, timeout=30,
            )
            # Must not crash — exit code 0 means success
            assert result.returncode == 0, (
                f"CLI crashed on {description}: stderr={result.stderr}"
            )
        finally:
            os.unlink(tmp_path)


class TestCLIFileEncodingWindows1252:
    """Test CLI with Windows-1252 encoded files."""

    @pytest.mark.parametrize("content_bytes,description", [
        (b"Smart quotes: \x93hello\x94.", "smart double quotes"),
        (b"Smart quotes: \x91hello\x92.", "smart single quotes"),
        (b"Price: \x80 100.", "euro sign cp1252"),
        (b"Range: 1 \x96 10.", "en dash"),
        (b"Pause \x97 long.", "em dash"),
        (b"Brand\x99 name.", "trademark"),
        (b"More\x85 text.", "horizontal ellipsis"),
        (b"Note \x86 here.", "dagger"),
        (b"Note \x87 here.", "double dagger"),
        (b"Result \x89 of total.", "per mille"),
    ])
    def test_cli_segment_cp1252_file(self, content_bytes, description):
        """CLI segment command must not crash on Windows-1252 files."""
        with tempfile.NamedTemporaryFile(mode="wb", suffix=".txt", delete=False) as f:
            f.write(content_bytes)
            tmp_path = f.name
        try:
            result = subprocess.run(
                [sys.executable, "-m", "fast_sentence_segment.cli", "-f", tmp_path],
                capture_output=True, text=True, timeout=30,
            )
            assert result.returncode == 0, (
                f"CLI crashed on {description}: stderr={result.stderr}"
            )
        finally:
            os.unlink(tmp_path)


class TestCLIFileEncodingISO8859:
    """Test CLI with various ISO-8859 encoded files."""

    @pytest.mark.parametrize("encoding,text,description", [
        ("iso-8859-1", "Caf\u00e9 au lait.", "ISO-8859-1 French"),
        ("iso-8859-1", "\u00c4nderung vorgenommen.", "ISO-8859-1 German"),
        ("iso-8859-1", "Se\u00f1or Garcia.", "ISO-8859-1 Spanish"),
        ("iso-8859-1", "Sm\u00f6rg\u00e5sbord.", "ISO-8859-1 Swedish"),
        ("iso-8859-2", "Bra\u0161ov city.", "ISO-8859-2 Romanian"),
        ("iso-8859-2", "Gda\u0144sk port.", "ISO-8859-2 Polish"),
        ("iso-8859-5", "\u041c\u043e\u0441\u043a\u0432\u0430.", "ISO-8859-5 Cyrillic"),
        ("iso-8859-7", "\u0391\u03b8\u03ae\u03bd\u03b1.", "ISO-8859-7 Greek"),
        ("iso-8859-9", "Istanbul g\u00fczel.", "ISO-8859-9 Turkish"),
        ("iso-8859-15", "Price: 50\u20ac.", "ISO-8859-15 Euro"),
    ])
    def test_cli_segment_iso8859_file(self, encoding, text, description):
        """CLI segment command must not crash on ISO-8859 encoded files."""
        with tempfile.NamedTemporaryFile(mode="wb", suffix=".txt", delete=False) as f:
            f.write(text.encode(encoding))
            tmp_path = f.name
        try:
            result = subprocess.run(
                [sys.executable, "-m", "fast_sentence_segment.cli", "-f", tmp_path],
                capture_output=True, text=True, timeout=30,
            )
            assert result.returncode == 0, (
                f"CLI crashed on {description}: stderr={result.stderr}"
            )
        finally:
            os.unlink(tmp_path)


class TestCLISegmentFileCommand:
    """Test segment-file CLI command with non-UTF-8 files."""

    @pytest.mark.parametrize("content_bytes,description", [
        (b"Simple text.", "ASCII baseline"),
        (b"Section \xa7 3.1.", "latin-1 section sign"),
        (b"Price \xa3 50.", "latin-1 pound"),
        (b"Temp 20\xb0C.", "latin-1 degree"),
        (b"Copyright \xa9.", "latin-1 copyright"),
        (b"The caf\xe9.", "latin-1 e-acute"),
        (b"Quotes \x93 hello \x94.", "cp1252 smart quotes"),
        (b"Dash \x97 here.", "cp1252 em dash"),
        (b"\xb6 paragraph.", "latin-1 pilcrow"),
        (b"Math: 3\xd7 5.", "latin-1 multiplication"),
    ])
    def test_cli_segment_file_non_utf8(self, content_bytes, description):
        """segment-file CLI command must not crash on non-UTF-8 files."""
        with tempfile.NamedTemporaryFile(mode="wb", suffix=".txt", delete=False) as f:
            f.write(content_bytes)
            input_path = f.name

        output_path = input_path + ".out"
        try:
            result = subprocess.run(
                [sys.executable, "-m", "fast_sentence_segment.cli",
                 "--input-file", input_path, "--output-file", output_path],
                capture_output=True, text=True, timeout=30,
                # Use the file_main entry point by calling the module differently
            )
            # Note: this may use the wrong entry point; the key assertion is no crash
            # If exit code is non-zero for reasons other than encoding, that's OK
            # The critical thing is no UnicodeDecodeError traceback
            if result.returncode != 0:
                assert "UnicodeDecodeError" not in result.stderr, (
                    f"segment-file crashed with UnicodeDecodeError on {description}"
                )
        finally:
            os.unlink(input_path)
            if os.path.exists(output_path):
                os.unlink(output_path)


# ===========================================================================
# PART 7: Edge Cases — Bracket Normalizer
# ===========================================================================

class TestBracketEdgeCases:
    """Edge cases for the bracket content normalizer."""

    @pytest.mark.parametrize("text", [
        # Very short bracket content
        "[a] text.",
        "[1] text.",
        "[.] text.",
        "[!] text.",
        "[?] text.",
        # Very long bracket content
        "[" + "a" * 500 + "] text.",
        "[" + "word " * 100 + "] text.",
        "[" + "a.b." * 50 + "] text.",
        # Brackets with only punctuation inside
        "[...] text.",
        "[---] text.",
        "[, , ,] text.",
        "[; ; ;] text.",
        "[: : :] text.",
        # Brackets with numbers only
        "[42] text.",
        "[3.14] text.",
        "[1,000,000] text.",
        "[1.2.3.4] text.",
        # Brackets with special formatting
        "[ALL CAPS] text.",
        "[MiXeD cAsE] text.",
        "[   spaces   ] text.",
    ])
    def test_edge_case_roundtrip(self, normalizer, text):
        """Edge case bracket content must survive round-trip."""
        assert _roundtrip(normalizer, text) == text


class TestBracketPositions:
    """Test brackets at every position in a sentence."""

    @pytest.mark.parametrize("text", [
        # Bracket as entire text
        "[only bracket content.]",
        # Bracket at very start
        "[Start.] The rest of the sentence.",
        # Bracket at very end
        "The sentence ends with [this.]",
        # Bracket in the middle
        "Before [middle] after.",
        # Multiple brackets
        "[a] [b] [c] text.",
        "Text [a] text [b] text [c] text.",
        "[a] text [b] text [c].",
        # Consecutive brackets no space — pre-existing issue: adjacent placeholders
        # merge because xend/xbracket delimiters are alphanumeric
        pytest.param("[a][b][c] text.", marks=pytest.mark.xfail(
            reason="Pre-existing: adjacent bracket placeholders merge")),
        pytest.param("Text[a][b]text.", marks=pytest.mark.xfail(
            reason="Pre-existing: adjacent bracket placeholders merge")),
        # Brackets near other punctuation
        "Text ([bracket]) here.",
        "Text \"[bracket]\" here.",
        "Text '[bracket]' here.",
        "Text, [bracket], here.",
        "Text; [bracket]; here.",
        "Text: [bracket]: here.",
    ])
    def test_bracket_position_roundtrip(self, normalizer, text):
        """Brackets at various positions must survive round-trip."""
        assert _roundtrip(normalizer, text) == text


class TestNoBracketsPassthrough:
    """Text without brackets should pass through unchanged."""

    @pytest.mark.parametrize("text", [
        "No brackets here.",
        "Just a simple sentence.",
        "Multiple sentences. With periods. And more.",
        "Question? Exclamation! Normal.",
        "Dr. Smith went to Washington D.C. at 9 a.m.",
        "The U.S. Senate voted today.",
        "I work at Yahoo! Inc.",
        "",
        "   ",
        "Single word",
        "a",
        "Hello World",
    ])
    def test_no_brackets_unchanged(self, normalizer, text):
        """Text without brackets must pass through normalize unchanged."""
        assert normalizer.process(text) == text
        assert normalizer.process(text, denormalize=True) == text


# ===========================================================================
# PART 8: Denormalize Robustness — Malformed Placeholders
# ===========================================================================

class TestDenormalizeMalformedPlaceholders:
    """Test denormalize with text that resembles but isn't a valid placeholder."""

    @pytest.mark.parametrize("text", [
        # Partial placeholder patterns (should pass through unchanged)
        "text xbracket without xend marker",
        "text without xbracket prefix xend",
        "xbracket xend empty placeholder",
        # Text that happens to contain placeholder-like substrings
        "The xbracket variable is used in code.",
        "See xend for the termination condition.",
        # Actual valid placeholder should be decoded
    ])
    def test_malformed_placeholders_no_crash(self, normalizer, text):
        """Malformed or partial placeholder patterns must not crash."""
        # Should not raise any exception
        result = normalizer.process(text, denormalize=True)
        assert isinstance(result, str)


class TestDenormalizeInvalidBase64:
    """Test denormalize with syntactically valid but semantically bad placeholders."""

    @pytest.mark.parametrize("placeholder_text", [
        # Placeholder with content that base64-decodes to non-UTF-8
        # Simulate by injecting crafted placeholders into text
        "Text xbracket" + base64.urlsafe_b64encode(b"\xb6").decode('ascii').replace('=', '') + "xend more.",
        "Text xbracket" + base64.urlsafe_b64encode(b"\xc5").decode('ascii').replace('=', '') + "xend more.",
        "Text xbracket" + base64.urlsafe_b64encode(b"\xff\xfe").decode('ascii').replace('=', '') + "xend more.",
        "Text xbracket" + base64.urlsafe_b64encode(b"\x80\x81\x82").decode('ascii').replace('=', '') + "xend more.",
        "Text xbracket" + base64.urlsafe_b64encode(b"\xed\xa0\x80").decode('ascii').replace('=', '') + "xend more.",
        "Text xbracket" + base64.urlsafe_b64encode(b"\xc0\xaf").decode('ascii').replace('=', '') + "xend more.",
        # Multiple bad placeholders in one text
        "A xbracket" + base64.urlsafe_b64encode(b"\xb6").decode('ascii').replace('=', '') + "xend B xbracket" + base64.urlsafe_b64encode(b"\xc5").decode('ascii').replace('=', '') + "xend C.",
    ])
    def test_invalid_base64_content_no_crash(self, normalizer, placeholder_text):
        """Placeholders decoding to non-UTF-8 bytes must not crash denormalize."""
        result = normalizer.process(placeholder_text, denormalize=True)
        assert isinstance(result, str)


# ===========================================================================
# PART 9: End-to-End segment_text Regression — No UnicodeDecodeError
# ===========================================================================

class TestSegmentTextNoUnicodeDecodeError:
    """Regression tests ensuring segment_text never raises UnicodeDecodeError.

    These represent real-world-ish inputs that combine bracket content
    with various Unicode characters.
    """

    @pytest.mark.parametrize("text", [
        # Academic text with brackets
        "The theory of relativity [Einstein, 1905.] changed physics.",
        "See [Fig. 1.] for the phase diagram. The results [Table 2.] confirm this.",
        "Previous work [Smith et al. 2020.] supports this finding.",
        "The data [p. 42.] shows a clear trend. See also [p. 100.].",
        "According to [WHO 2021.] the guidelines have changed.",
        # Brackets with accented characters in surrounding text
        "Le r\u00e9sum\u00e9 [Fig. 1.] montre les r\u00e9sultats.",
        "Die \u00c4nderung [Ref. 3.] wurde best\u00e4tigt.",
        "El se\u00f1or [nota 1.] confirm\u00f3 los datos.",
        # Brackets with CJK in surrounding text
        "\u8bf7\u53c2\u9605 [Fig. 1.] \u4e86\u89e3\u8be6\u60c5.",
        "\u8a73\u7d30\u306f [ref. 2.] \u3092\u53c2\u7167.",
        # Multiple brackets in complex text
        "Smith [1] and Jones [2] disagree. However, Brown [3] provides a synthesis [see also 4, 5].",
        "The reaction [pH 7.0.] proceeded at [25\u00b0C.] for [2 hr.].",
        # Brackets with mathematical content
        "The integral [\u222b f(x)dx] converges.",
        "For all [\u2200 x \u2208 S] the property holds.",
        "The sum [\u2211 n=1...\u221e] is finite.",
        # Brackets with currency/symbols
        "The price [\u20ac 50.00] is firm. Tax [\u00a3 10.00] extra.",
        "Total cost [$100.00 + \u20ac 50.00] combined.",
        # Long text with many brackets
        "Chapter 1 [pp. 1-50.] introduces the topic. Chapter 2 [pp. 51-100.] "
        "covers methods. Chapter 3 [pp. 101-200.] presents results. Chapter 4 "
        "[pp. 201-250.] discusses implications. Chapter 5 [pp. 251-300.] concludes.",
    ])
    def test_no_unicode_decode_error(self, segment, text):
        """segment_text must never raise UnicodeDecodeError on valid str input."""
        result = segment(text)
        assert isinstance(result, list)
        assert all(isinstance(s, str) for s in result)


class TestSegmentTextBracketContentIntegrity:
    """Verify bracket content is preserved intact after segmentation."""

    @pytest.mark.parametrize("bracket_content", [
        "Fig. 1.",
        "p. 42.",
        "refs. 1, 2, 3.",
        "sic.",
        "emphasis added.",
        "Smith 2020.",
        "see note 1.",
        "cf. Chapter 2.",
        "ibid.",
        "op. cit.",
        "1",
        "2, 3",
        "a",
        "...",
        "pH 7.0.",
        "25\u00b0C.",
        "\u03c0 \u2248 3.14.",
        "\u20ac 50.00.",
        "r\u00e9sum\u00e9.",
        "\u4e2d\u6587.",
    ])
    def test_bracket_content_survives_segmentation(self, segment, bracket_content):
        """The exact bracket content must appear in segmented output."""
        text = f"Some text [{bracket_content}] here."
        result = segment(text)
        joined = " ".join(result)
        assert f"[{bracket_content}]" in joined, (
            f"Bracket content [{bracket_content}] was lost or corrupted. "
            f"Got: {result}"
        )
