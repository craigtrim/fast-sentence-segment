# -*- coding: UTF-8 -*-
"""Real-world text samples."""

from fast_sentence_segment import segment_text


class TestRealWorldExamples:
    """Real-world text samples."""

    def test_news_paragraph(self):
        text = """
        The president announced new policies today.
        These changes will affect millions of citizens.
        Experts are divided on the impact.
        """
        result = segment_text(text, flatten=True)
        assert result == [
            "The president announced new policies today.",
            "These changes will affect millions of citizens.",
            "Experts are divided on the impact."
        ]

    def test_technical_writing(self):
        text = "Install Python 3.9 or higher. Run pip install package. Configure settings."
        result = segment_text(text, flatten=True)
        assert result == [
            "Install Python 3.9 or higher.",
            "Run pip install package.",
            "Configure settings."
        ]

    def test_legal_text(self):
        text = "Section 1.2.3 states the following. The party of the first part agrees. See Appendix A."
        result = segment_text(text, flatten=True)
        assert result == [
            "Section 1.2.3 states the following.",
            "The party of the first part agrees.",
            "See Appendix A."
        ]

    def test_email_style(self):
        text = "Hi John. Thanks for your email. I will review and get back to you. Best regards."
        result = segment_text(text, flatten=True)
        assert result == [
            "Hi John.",
            "Thanks for your email.",
            "I will review and get back to you.",
            "Best regards."
        ]
