# -*- coding: UTF-8 -*-


from fast_sentence_segment import segment_text


def test_segment_text():

    input_text = """
        -The U.S. government does more to drive the supply of energy innovation than anyone else. -It is the biggest funder and performer of energy research and development, with twelve different federal agencies involved in research. -The federal government also plays a central role in driving the demand for green products and policies.
    """

    results = segment_text(input_text, flatten=True)
    print(results)

    assert results == [
        'The U.S. government does more to drive the supply of energy innovation than anyone else.',
        'It is the biggest funder and performer of energy research and development, with twelve different federal agencies involved in research.',
        'The federal government also plays a central role in driving the demand for green products and policies.'
    ]


def main():
    test_segment_text()


if __name__ == "__main__":
    main()
