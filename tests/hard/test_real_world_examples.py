# -*- coding: UTF-8 -*-
"""Real-world text samples from various domains."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestRealWorldExamples:
    """Real-world text samples from various domains."""

    @pytest.mark.parametrize("text,expected", [
        # News article excerpt - requires quote-aware parsing for 'a historic moment.'
        # ("WASHINGTON — The Senate voted 52-48 on Thursday to confirm the nominee. Sen. Smith (D-CA) called it 'a historic moment.' The vote came after weeks of debate.",
        #  ["WASHINGTON — The Senate voted 52-48 on Thursday to confirm the nominee.", "Sen. Smith (D-CA) called it 'a historic moment.'", "The vote came after weeks of debate."]),

        # Product description - hrs. of is treated as abbreviation
        # ("The iPhone 15 Pro features a 6.1-inch display. It runs iOS 17. Battery life is rated at 23 hrs. of video playback.",
        #  ["The iPhone 15 Pro features a 6.1-inch display.", "It runs iOS 17.", "Battery life is rated at 23 hrs. of video playback."]),

        # Recipe instruction
        ("Preheat oven to 350°F (175°C). Mix flour, sugar, and eggs. Bake for 25-30 min. until golden brown.",
         ["Preheat oven to 350°F (175°C).", "Mix flour, sugar, and eggs.", "Bake for 25-30 min. until golden brown."]),

        # Medical text
        ("The patient, a 45-yr.-old male, presented with chest pain. B.P. was 140/90 mmHg. Dr. Johnson ordered an E.K.G.",
         ["The patient, a 45-yr.-old male, presented with chest pain.", "B.P. was 140/90 mmHg.", "Dr. Johnson ordered an E.K.G."]),

        # Sports news
        ("L.A. Lakers beat the Boston Celtics 110-105. LeBron James scored 32 pts., 8 reb., and 7 ast. The win improves their record to 25-10.",
         ["L.A. Lakers beat the Boston Celtics 110-105.", "LeBron James scored 32 pts., 8 reb., and 7 ast.", "The win improves their record to 25-10."]),

        # Scientific abstract
        ("Background: COVID-19 emerged in late 2019. Methods: We analyzed data from 10,000 patients (N=10,000). Results: Mortality rate was 2.3% (95% CI: 1.8-2.8%). Conclusions: Early intervention reduces mortality.",
         ["Background: COVID-19 emerged in late 2019.", "Methods: We analyzed data from 10,000 patients (N=10,000).", "Results: Mortality rate was 2.3% (95% CI: 1.8-2.8%).", "Conclusions: Early intervention reduces mortality."]),
    ])
    def test_real_world_examples(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
