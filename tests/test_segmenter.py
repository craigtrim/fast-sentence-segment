# -*- coding: UTF-8 -*-
from fast_sentence_segment import Segmenter


## ---------------------------------------------------------- ##
# Purpose:    Test Basic I/O
#             for complex and complete tokenization tests, use a regression suite
## ---------------------------------------------------------- ##


def execute(input_text: str,
            expected_output: str):

    actual_output = Segmenter().input_text(input_text)
    assert actual_output
    print(actual_output)

    assert actual_output == expected_output


def test_segmentation():
    execute(
        '"The $4.50 is paid in full tomorrow!" said Mr. Berluski',
        [[
            '"The $4.50 is paid in full tomorrow!" said Mr. Berluski.'
        ]])

    execute(
        'The Quick Fox.  The Lazy Dog',
        [['The Quick Fox.', 'The Lazy Dog.']])
