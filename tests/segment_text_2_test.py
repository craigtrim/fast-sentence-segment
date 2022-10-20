# -*- coding: UTF-8 -*-


from fast_sentence_segment import segment_text


def test_segment_text():

    input_text = """
        1. Border adjustments are a way to make sure that the carbon price on some product is paid whether that product was made domestically or imported from somewhere else. 2. When the world's governments agree that there is value in reducing emissions, it becomes harder-though far from impossible, as we have seen-to be the outlier who says, "I don't care. I'm going to keep emitting greenhouse gases."
    """

    [print(x) for x in segment_text(input_text)]

    # assert segment_text(input_text) == [
    #     [
    #         'here is a dr. and m.d. & m.b.a who say something.',
    #         'where in the u.s is that st. - do you know?',
    #         'i dont know.',
    #         "Do you???'."
    #     ]
    # ]

    # assert segment_text(input_text, flatten=True) == [
    #     'here is a dr. and m.d. & m.b.a who say something.',
    #     'where in the u.s is that st. - do you know?',
    #     'i dont know.',
    #     "Do you???'."
    # ]


def main():
    test_segment_text()


if __name__ == "__main__":
    main()
