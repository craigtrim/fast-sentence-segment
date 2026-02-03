# -*- coding: UTF-8 -*-
"""Numbers with decimals should NOT trigger splits."""

from fast_sentence_segment import segment_text


class TestNumbers:
    """Numbers with decimals should NOT trigger splits."""

    def test_currency(self):
        result = segment_text("The price is $4.50 today.", flatten=True)
        assert result == ["The price is $4.50 today."]

    def test_decimal(self):
        result = segment_text("Pi is approximately 3.14159 in value.", flatten=True)
        assert result == ["Pi is approximately 3.14159 in value."]

    def test_percentage(self):
        result = segment_text("Growth was 5.5% last year.", flatten=True)
        assert result == ["Growth was 5.5% last year."]

    # ──────────────────────────────────────────────────────────────────────────
    # Decimal numbers
    # ──────────────────────────────────────────────────────────────────────────

    def test_decimal_at_start(self):
        """Decimal number at sentence start."""
        result = segment_text("3.14 is pi. It is important.", flatten=True)
        assert "3.14" in result[0]

    def test_decimal_at_end(self):
        """Decimal number at sentence end."""
        result = segment_text("The value was 9.99. That was high.", flatten=True)
        assert len(result) == 2
        assert "9.99" in result[0]

    def test_multiple_decimals(self):
        """Multiple decimal numbers."""
        result = segment_text("He scored 3.5 and 4.5 points.", flatten=True)
        assert len(result) == 1

    def test_long_decimal(self):
        """Long decimal number."""
        result = segment_text("Pi is 3.14159265359 approximately.", flatten=True)
        assert len(result) == 1

    def test_decimal_with_leading_zero(self):
        """Decimal with leading zero."""
        result = segment_text("The rate is 0.05 percent.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Currency
    # ──────────────────────────────────────────────────────────────────────────

    def test_dollar_amount(self):
        """Dollar amount with cents."""
        result = segment_text("It costs $19.99 today.", flatten=True)
        assert len(result) == 1

    def test_euro_amount(self):
        """Euro amount with cents."""
        result = segment_text("It costs €19.99 today.", flatten=True)
        assert len(result) == 1

    def test_pound_amount(self):
        """Pound amount with pence."""
        result = segment_text("It costs £19.99 today.", flatten=True)
        assert len(result) == 1

    def test_large_currency(self):
        """Large currency amount."""
        result = segment_text("The house costs $1,234,567.89 today.", flatten=True)
        assert len(result) == 1

    def test_currency_at_sentence_end(self):
        """Currency at sentence end."""
        result = segment_text("Total is $50.00. Please pay.", flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # Version numbers
    # ──────────────────────────────────────────────────────────────────────────

    def test_version_two_parts(self):
        """Two-part version number."""
        result = segment_text("Use version 2.0 now.", flatten=True)
        assert len(result) == 1
        assert "2.0" in result[0]

    def test_version_three_parts(self):
        """Three-part version number."""
        result = segment_text("Install Python 3.11.5 today.", flatten=True)
        assert len(result) == 1

    def test_version_with_v(self):
        """Version with v prefix."""
        result = segment_text("Download v1.2.3 now.", flatten=True)
        assert len(result) == 1

    def test_version_at_sentence_end(self):
        """Version at sentence end."""
        result = segment_text("We use 3.0. It is stable.", flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # IP addresses
    # ──────────────────────────────────────────────────────────────────────────

    def test_ip_address(self):
        """Standard IP address."""
        result = segment_text("Connect to 192.168.1.1 now.", flatten=True)
        assert len(result) == 1
        assert "192.168.1.1" in result[0]

    def test_ip_localhost(self):
        """Localhost IP."""
        result = segment_text("Server is at 127.0.0.1 locally.", flatten=True)
        assert len(result) == 1

    def test_ip_at_sentence_end(self):
        """IP address at sentence end."""
        result = segment_text("Use 10.0.0.1. It works.", flatten=True)
        assert len(result) == 2

    # ──────────────────────────────────────────────────────────────────────────
    # Phone numbers
    # ──────────────────────────────────────────────────────────────────────────

    def test_phone_with_dots(self):
        """Phone number with dots."""
        result = segment_text("Call 555.123.4567 today.", flatten=True)
        assert len(result) == 1

    def test_phone_with_dashes(self):
        """Phone number with dashes."""
        result = segment_text("Call 555-123-4567 today.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Ranges and ratios
    # ──────────────────────────────────────────────────────────────────────────

    def test_number_range(self):
        """Number range with dash."""
        result = segment_text("Read pages 10-20 carefully.", flatten=True)
        assert len(result) == 1

    def test_ratio(self):
        """Ratio with colon."""
        result = segment_text("The ratio is 3:1 today.", flatten=True)
        assert len(result) == 1

    def test_time_format(self):
        """Time in 12-hour format."""
        result = segment_text("Meet at 3:30 today.", flatten=True)
        assert len(result) == 1

    def test_time_with_am_pm(self):
        """Time with AM/PM."""
        result = segment_text("Meet at 3:30 p.m. today.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Ordinal numbers
    # ──────────────────────────────────────────────────────────────────────────

    def test_ordinal_first(self):
        """First ordinal."""
        result = segment_text("This is the 1st time.", flatten=True)
        assert len(result) == 1

    def test_ordinal_second(self):
        """Second ordinal."""
        result = segment_text("This is the 2nd place.", flatten=True)
        assert len(result) == 1

    def test_ordinal_third(self):
        """Third ordinal."""
        result = segment_text("This is the 3rd attempt.", flatten=True)
        assert len(result) == 1

    def test_ordinal_general(self):
        """General ordinal."""
        result = segment_text("This is the 21st century.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Scientific notation
    # ──────────────────────────────────────────────────────────────────────────

    def test_scientific_notation(self):
        """Scientific notation."""
        result = segment_text("The value is 1.5e10 exactly.", flatten=True)
        assert len(result) == 1

    def test_scientific_negative_exponent(self):
        """Scientific notation with negative exponent."""
        result = segment_text("The value is 3.2e-5 precisely.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Fractions
    # ──────────────────────────────────────────────────────────────────────────

    def test_fraction_half(self):
        """Fraction one half."""
        result = segment_text("Use 1/2 cup flour.", flatten=True)
        assert len(result) == 1

    def test_fraction_quarter(self):
        """Fraction one quarter."""
        result = segment_text("Add 1/4 teaspoon salt.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Numbers with units
    # ──────────────────────────────────────────────────────────────────────────

    def test_distance_miles(self):
        """Distance in miles."""
        result = segment_text("Drive 5.5 miles north.", flatten=True)
        assert len(result) == 1

    def test_weight_kg(self):
        """Weight in kilograms."""
        result = segment_text("It weighs 2.5 kg exactly.", flatten=True)
        assert len(result) == 1

    def test_temperature(self):
        """Temperature with decimal."""
        result = segment_text("It is 98.6 degrees outside.", flatten=True)
        assert len(result) == 1

    # ──────────────────────────────────────────────────────────────────────────
    # Edge cases
    # ──────────────────────────────────────────────────────────────────────────

    def test_number_at_very_end(self):
        """Number at absolute end before period."""
        result = segment_text("The answer is 42. Next question.", flatten=True)
        assert len(result) == 2

    def test_consecutive_numbers(self):
        """Consecutive numbers."""
        result = segment_text("Values are 1.1, 2.2, and 3.3 here.", flatten=True)
        assert len(result) == 1

    def test_negative_decimal(self):
        """Negative decimal number."""
        result = segment_text("Temperature fell to -5.5 degrees.", flatten=True)
        assert len(result) == 1

    def test_positive_sign(self):
        """Positive sign before number."""
        result = segment_text("Growth was +3.5 percent.", flatten=True)
        assert len(result) == 1
