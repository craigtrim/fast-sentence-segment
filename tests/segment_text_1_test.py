# -*- coding: UTF-8 -*-


from fast_sentence_segment import segment_text


def test_segment_text():

    input_text = """
        here is a dr. and m.d. & m.b.a who say something. where in the u.s is that st. - do you know? i dont know. Do you???'
    """

    results = segment_text(input_text, flatten=True)
    print(results)

    assert results == [
        'here is a dr. and m.d. & m.b.a who say something.',

        # 20221019; note the removal of '. - ' per segment_text_3_test
        'where in the u.s is that st. do you know?',
        'i dont know.',
        "Do you???'."
    ]


def main():
    test_segment_text()


if __name__ == "__main__":
    main()
