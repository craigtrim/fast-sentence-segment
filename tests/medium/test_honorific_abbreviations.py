# -*- coding: UTF-8 -*-
"""Honorifics and titles that contain periods but don't end sentences."""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestHonorificAbbreviations:
    """Honorifics and titles that contain periods but don't end sentences."""

    @pytest.mark.parametrize("text,expected", [
        # Dr.
        ("Dr. Smith is here.", ["Dr. Smith is here."]),
        ("I saw Dr. Johnson yesterday.", ["I saw Dr. Johnson yesterday."]),
        ("Dr. Smith is here. He will see you now.",
         ["Dr. Smith is here.", "He will see you now."]),
        ("Call Dr. Williams. She can help.",
         ["Call Dr. Williams.", "She can help."]),

        # Mr.
        ("Mr. Brown arrived late.", ["Mr. Brown arrived late."]),
        ("I spoke with Mr. Davis. He agreed.",
         ["I spoke with Mr. Davis.", "He agreed."]),
        ("Mr. and Mrs. Smith are here.",
         ["Mr. and Mrs. Smith are here."]),

        # Mrs.
        ("Mrs. Johnson called.", ["Mrs. Johnson called."]),
        ("I met Mrs. Chen today. She was kind.",
         ["I met Mrs. Chen today.", "She was kind."]),

        # Ms.
        ("Ms. Garcia is the manager.", ["Ms. Garcia is the manager."]),
        ("Talk to Ms. Lee. She knows the details.",
         ["Talk to Ms. Lee.", "She knows the details."]),

        # Prof.
        ("Prof. Anderson teaches physics.", ["Prof. Anderson teaches physics."]),
        ("I took Prof. Martin's class. It was excellent.",
         ["I took Prof. Martin's class.", "It was excellent."]),

        # Multiple honorifics
        ("Dr. Smith and Mr. Jones arrived. Mrs. Brown greeted them.",
         ["Dr. Smith and Mr. Jones arrived.", "Mrs. Brown greeted them."]),
        ("Prof. Lee, Dr. Kim, and Mr. Park attended the meeting.",
         ["Prof. Lee, Dr. Kim, and Mr. Park attended the meeting."]),

        # Jr. and Sr.
        ("John Smith Jr. is here.", ["John Smith Jr. is here."]),
        ("Robert Davis Sr. founded the company.",
         ["Robert Davis Sr. founded the company."]),
        ("John Jr. and his father arrived. They looked alike.",
         ["John Jr. and his father arrived.", "They looked alike."]),
    ])
    def test_honorific_abbreviations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected
