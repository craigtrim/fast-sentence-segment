# -*- coding: UTF-8 -*-


from fast_sentence_segment import segment_text


def test_segment_text():

    input_text = """
        here is a dr. and m.d. & m.b.a who say something. where in the u.s is that st. - do you know? i dont know. Do you???'
    """

    [print(x) for x in segment_text(input_text)]

    assert segment_text(input_text) == [
        [
            'here is a dr. and m.d. & m.b.a who say something.',
            'where in the u.s is that st. - do you know?',
            'i dont know.',
            "Do you???'."
        ]
    ]

    assert segment_text(input_text, flatten=True) == [
        'here is a dr. and m.d. & m.b.a who say something.',
        'where in the u.s is that st. - do you know?',
        'i dont know.',
        "Do you???'."
    ]


def main():
    test_segment_text()


if __name__ == "__main__":
    main()
