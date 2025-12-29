# -*- coding: UTF-8 -*-


from fast_sentence_segment import segment_text


def test_segment_text():

    input_text = """
        1. Border adjustments are a way to make sure that the carbon price on some product is paid whether that product was made domestically or imported from somewhere else. 2. When the world's governments agree that there is value in reducing emissions, it becomes harder-though far from impossible, as we have seen-to be the outlier who says, "I don't care. I'm going to keep emitting greenhouse gases."
    """

    results = segment_text(input_text, flatten=True)
    print(results)

    # 20221019; there is a defect in here but it's very complex to fix
    #           it would involve peering inside quoted lines within quoted text
    #           this would require real parser-like capabilities
    #           and unless well-tested has the potential to cause more problems
    assert results == [
        '1. Border adjustments are a way to make sure that the carbon price on some product is paid whether that product was made domestically or imported from somewhere else.',
        '2. When the world\'s governments agree that there is value in reducing emissions, it becomes harder-though far from impossible, as we have seen-to be the outlier who says, "I don\'t care.',
        'I\'m going to keep emitting greenhouse gases.".'
    ]


def main():
    test_segment_text()


if __name__ == "__main__":
    main()
