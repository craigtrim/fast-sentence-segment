# -*- coding: UTF-8 -*-


from fast_sentence_segment.dmo import NumberedListNormalizer


def test_component():

    input_text = """
        1. Border adjustments are a way to make sure that the carbon price on some product is paid whether that product was made domestically or imported from somewhere else. 2. When the world's governments agree that there is value in reducing emissions, it becomes harder-though far from impossible, as we have seen-to be the outlier who says, "I don't care. I'm going to keep emitting greenhouse gases."
    """

    output_text = NumberedListNormalizer().process(input_text)

    assert output_text == """
        1_ Border adjustments are a way to make sure that the carbon price on some product is paid whether that product was made domestically or imported from somewhere else. 2_ When the world's governments agree that there is value in reducing emissions, it becomes harder-though far from impossible, as we have seen-to be the outlier who says, "I don't care. I'm going to keep emitting greenhouse gases."
    """

    output_text = NumberedListNormalizer().process(output_text, denormalize=True)

    assert output_text == input_text


def main():
    test_component()


if __name__ == "__main__":
    main()
