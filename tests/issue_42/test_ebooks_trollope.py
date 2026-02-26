import pytest
from fast_sentence_segment import segment_text


class TestEbooksTrollope:
    """Integration tests mined from Anthony Trollope ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1860s
    """

    def test_wrap_001_the_novel(self):
        # Source: An Autobiography of Anthony Trollope, wrap corruption: the.novel
        passage = (
            "As, however, I understand you have nearly finished the\n"
            "   novel La Vendée, perhaps you will favour me with a sight\n"
            "   of it when convenient.--I remain, &c. &c."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.novel" not in full_text

    def test_wrap_002_post_office(self):
        # Source: An Autobiography of Anthony Trollope, wrap corruption: post.office
        passage = (
            "[Footnpte 8: During the period of my service in the Post\n"
            "   Office I did very much special work for which I never asked\n"
            "   any remuneration,--and never received any, though payments for\n"
            "   special services were common in the department at that time.\n"
            "   But if there was to be a question of such remuneration, I did\n"
            "   not choose that my work should be valued at the price put upon\n"
            "   it by Mr. Hill.]"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "post.office" not in full_text

    def test_wrap_003_much_regret(self):
        # Source: An Autobiography of Anthony Trollope, wrap corruption: much.regret
        passage = (
            "In accepting your resignation, which he does with much\n"
            "   regret, the Duke of Montrose desires me to convey to you\n"
            "   his own sense of the value of your services, and to state\n"
            "   how alive he is to the loss which will be sustained by the\n"
            "   department in which you have long been an ornament, and\n"
            "   where your place will with difficulty be replaced."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "much.regret" not in full_text

    def test_wrap_004_short_our(self):
        # Source: An Autobiography of Anthony Trollope, wrap corruption: short.our
        passage = (
            "\"Years as they roll cut all our pleasures short;\n"
            "    Our pleasant mirth, our loves, our wine, our sport.\n"
            "    And then they stretch their power, and crush at last\n"
            "    Even the power of singing of the past.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "short.our" not in full_text

    def test_wrap_005_side_ive(self):
        # Source: An Autobiography of Anthony Trollope, wrap corruption: side.ive
        passage = (
            "\"I've lived about the covert side,\n"
            "    I've ridden straight, and ridden fast;\n"
            "    Now breeches, boots, and scarlet pride\n"
            "    Are but mementoes of the past.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "side.ive" not in full_text

    def test_wrap_006_that_nothing(self):
        # Source: An Eye for an Eye, wrap corruption: that.nothing
        passage = (
            "I daresay nothing shall come of it, and I'm sure I hope that\n"
            "   nothing may. But I thought it best to tell you. Pray do not let him\n"
            "   know that you have heard from me. Young men are so very particular\n"
            "   about things, and I don't know what he might say of me if he knew\n"
            "   that I had written home to you about his private affairs. All the\n"
            "   same if I can be of any service to you, pray let me know. Excuse\n"
            "   haste. And believe me to be,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.nothing" not in full_text

    def test_wrap_007_marry_she(self):
        # Source: An Eye for an Eye, wrap corruption: marry.she
        passage = (
            "There is a young lady here whom it is intended that I shall marry.\n"
            "   She is the pink of propriety and really very pretty;--but you need\n"
            "   not be a bit jealous. The joke is that my brother is furiously in\n"
            "   love with her, and that I fancy she would be just as much in love\n"
            "   with him only that she's told not to.--A thousand kisses."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "marry.she" not in full_text

    def test_wrap_008_marty_was(self):
        # Source: An Eye for an Eye, wrap corruption: marty.was
        passage = (
            "There is no news at all to send you from Liscannor. Father Marty\n"
            "   was up here yesterday and says that your boat is all safe at\n"
            "   Lahinch. He says that Barney Morony is an idle fellow, but as he\n"
            "   has nothing to do he can't help being idle. You should come back\n"
            "   and not let him be idle any more. I think the sea gulls know that\n"
            "   you are away, because they are wheeling and screaming about louder\n"
            "   and bolder than ever."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "marty.was" not in full_text

    def test_wrap_009_you_should(self):
        # Source: An Eye for an Eye, wrap corruption: you.should
        passage = (
            "Mother said at once that it was a matter of course that you\n"
            "   should go to England; but your friend, whose name we never heard,\n"
            "   said that you had sent him especially to promise that you would\n"
            "   write quite immediately, and that you would come back very soon.\n"
            "   I do not know what he will think of me, because I asked him\n"
            "   whether he was quite, quite sure that you would come back. If he\n"
            "   thinks that I love you better than my own soul, he only thinks\n"
            "   the truth."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.should" not in full_text

    def test_wrap_010_outside_the(self):
        # Source: An Eye for an Eye, wrap corruption: outside.the
        passage = (
            "I am not ill as I was when you were here. But I never go outside\n"
            "   the door now. I never shall go outside the door again till you\n"
            "   come. I don't care now for going out upon the rocks. I don't care\n"
            "   even for the birds as you are not here to watch them with me. I\n"
            "   sit with the skin of the seal you gave me behind my head, and I\n"
            "   pretend to sleep. But though I am quite still for hours I am not\n"
            "   asleep, but thinking always of you."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "outside.the" not in full_text

    def test_wrap_011_father_and(self):
        # Source: An Eye for an Eye, wrap corruption: father.and
        passage = (
            "We have neither seen or heard anything more of my father,\n"
            "   and Father Marty says that you have managed about that very\n"
            "   generously. You are always generous and good. I was so wretched\n"
            "   all that day, that I thought I should have died. You will not\n"
            "   think ill of your Kate, will you, because her father is bad?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "father.and" not in full_text

    def test_wrap_012_all_the(self):
        # Source: An Eye for an Eye, wrap corruption: all.the
        passage = (
            "I call upon you, my lord, in the most solemn manner, with all\n"
            "   the energy and anxiety of a mother,--of one who will be of all\n"
            "   women the most broken-hearted if you wrong her,--to write at\n"
            "   once and let me know when you will be here to keep your promise.\n"
            "   For the sake of your own offspring I implore you not to delay."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.the" not in full_text

    def test_wrap_013_afternoon_probably(self):
        # Source: An Old Mans Love, wrap corruption: afternoon.probably
        passage = (
            "DEAR MR JOHN GORDON,--I shall be in town this afternoon,\n"
            "   probably by the same train which will bring this letter,\n"
            "   and will do myself the honour of calling upon you at your\n"
            "   club the next day at twelve.--I am, dear Mr John Gordon,\n"
            "   faithfully yours,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "afternoon.probably" not in full_text

    def test_wrap_014_you_expressed(self):
        # Source: An Old Mans Love, wrap corruption: you.expressed
        passage = (
            "I have never told you that I loved you, nor have you\n"
            "   expressed your willingness to receive my love. Dear Mary,\n"
            "   how shall it be? No doubt I do count upon you in my very\n"
            "   heart as being my own. After this week of troubles it\n"
            "   seems as though I can look back upon a former time in\n"
            "   which you and I had talked to one another as though we had\n"
            "   been lovers. May I not think that it was so? May it not be\n"
            "   so? May I not call you my Mary?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.expressed" not in full_text

    def test_wrap_015_that_you(self):
        # Source: An Old Mans Love, wrap corruption: that.you
        passage = (
            "And indeed between man and man, as I would say, only that\n"
            "   you are not a man, have I not a right to assume that it\n"
            "   is so? I told him that it was so down at Croker's Hall,\n"
            "   and he did not contradict me. And now he has been the most\n"
            "   indiscreet of men, and has allowed all your secrets to\n"
            "   escape from his breast. He has told me that you love me,\n"
            "   and has bade me do as seems good to me in speaking to you\n"
            "   of my love."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.you" not in full_text

    def test_wrap_016_would_wish(self):
        # Source: An Old Mans Love, wrap corruption: would.wish
        passage = (
            "Let me have a line from you to say that it is as I would\n"
            "   wish it, and name a day in which I may come to visit you.\n"
            "   I shall now remain in London only to obey your behests. As\n"
            "   to my future life, I can settle nothing till I can discuss\n"
            "   it with you, as it will be your life also. God bless you,\n"
            "   my own one.--Yours affectionately,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "would.wish" not in full_text

    def test_wrap_017_your_wife(self):
        # Source: An Old Mans Love, wrap corruption: your.wife
        passage = (
            "You know that I love you, and am willing to become your\n"
            "   wife. What can I say to you now, except that it is so. It\n"
            "   is so. And in saying that, I have told you everything as\n"
            "   to myself. Of him I can only say, that his regard for me\n"
            "   has been more tender even than that of a father.--Yours\n"
            "   always most lovingly,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "your.wife" not in full_text

    def test_wrap_018_coliseum_today(self):
        # Source: Ayalas Angel, wrap corruption: coliseum.today
        passage = (
            "You don't know how unhappy you made me at the Coliseum\n"
            "   to-day. I don't think you ought to turn against me when\n"
            "   you know what I have to bear. It is turning against me\n"
            "   to talk as you did. Of course it means nothing; but you\n"
            "   shouldn't do it. It never never could mean anything. I\n"
            "   hope you will be good-natured and kind to me, and then I\n"
            "   shall be so much obliged to you. If you won't say anything\n"
            "   more like that I will forget it altogether."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "coliseum.today" not in full_text

    def test_wrap_019_why_should(self):
        # Source: Ayalas Angel, wrap corruption: why.should
        passage = (
            "As for my mother I don't think she would say a word. Why\n"
            "   should she? But I am not the sort of man to be talked out\n"
            "   of my intentions in such a matter as this. I have set my\n"
            "   heart upon having you and nothing will ever turn me off."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "why.should" not in full_text

    def test_wrap_020_will_love(self):
        # Source: Ayalas Angel, wrap corruption: will.love
        passage = (
            "Dearest Ayala, let me have one look to say that you will\n"
            "   love me, and I shall be the happiest man in England. I\n"
            "   think you so beautiful! I do, indeed. The governor has\n"
            "   always said that if I would settle down and marry there\n"
            "   should be lots of money. What could I do better with it\n"
            "   than make my darling look as grand as the best of them."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "will.love" not in full_text

    def test_wrap_021_and_margaret(self):
        # Source: Ayalas Angel, wrap corruption: and.margaret
        passage = (
            "I will not write to dear Lucy herself because you and\n"
            "   Margaret can explain it all so much better,--if you will\n"
            "   consent to our plan. Ayala also will write to her sister.\n"
            "   But pray tell her from me that I will love her very dearly\n"
            "   if she will come to me. And indeed I have loved Ayala\n"
            "   almost as though she were my own, only we have not been\n"
            "   quite able to hit it off together."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.margaret" not in full_text

    def test_wrap_022_has_told(self):
        # Source: Ayalas Angel, wrap corruption: has.told
        passage = (
            "Oh, I have such things to write to you! Aunt Emmeline has\n"
            "   told it all to Uncle Reginald. You are to come and be the\n"
            "   princess, and I am to go and be the milkmaid at home. I am\n"
            "   quite content that it should be so because I know that it\n"
            "   will be the best. You ought to be a princess and I ought\n"
            "   to be a milkmaid."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "has.told" not in full_text

    def test_wrap_023_and_dignified(self):
        # Source: Ayalas Angel, wrap corruption: and.dignified
        passage = (
            "And you will make a beautiful grand lady, quiescent and\n"
            "   dignified as a grand lady ought to be. At any rate it\n"
            "   would be impossible that I should remain here. Tom is bad\n"
            "   enough, but to be told that I encourage him is more than I\n"
            "   can bear."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.dignified" not in full_text

    def test_wrap_024_and_telling(self):
        # Source: Ayalas Angel, wrap corruption: and.telling
        passage = (
            "I shall see you very soon, but I cannot help writing and\n"
            "   telling it to you all. Give my love to Aunt Dosett. If she\n"
            "   will consent to receive me I will endeavour to be good to\n"
            "   her. In the meantime good-bye."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.telling" not in full_text

    def test_wrap_025_month_sir(self):
        # Source: Ayalas Angel, wrap corruption: month.sir
        passage = (
            "We shall start for Glenbogie on the 10th of next month.\n"
            "   Sir Thomas wishes you to join us on the 20th if you can,\n"
            "   and stay till the end of the month. We shall be a little\n"
            "   crowded at first, and therefore cannot name an earlier\n"
            "   day."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "month.sir" not in full_text

    def test_wrap_026_more_than(self):
        # Source: Ayalas Angel, wrap corruption: more.than
        passage = (
            "I am particularly to warn you that this means nothing more\n"
            "   than a simple invitation. I know what passed between you\n"
            "   and Sir Thomas, and he hasn't at all changed his mind. I\n"
            "   think it right to tell you this. If you like to speak to\n"
            "   him again when you are at Glenbogie of course you can."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "more.than" not in full_text

    def test_wrap_027_you_are(self):
        # Source: Ayalas Angel, wrap corruption: you.are
        passage = (
            "Papa, you see, hasn't cut up so very rough, after all. You\n"
            "   are to be allowed to come and help to slaughter grouse,\n"
            "   which will be better than going to that stupid Tyrol.\n"
            "   If you want to draw somebody's back head you can do it\n"
            "   there. Isn't it a joke papa's giving way like that all in\n"
            "   a moment? He gets so fierce sometimes that we think he's\n"
            "   going to eat everybody. Then he has to come down, and he\n"
            "   gets eaten worse than anybody else."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.are" not in full_text

    def test_wrap_028_come_here(self):
        # Source: Ayalas Angel, wrap corruption: come.here
        passage = (
            "Of course, as you're asked to Glenbogie, you can come\n"
            "   here as often as you like. I shall ride on Thursday and\n"
            "   Friday. I shall expect you exactly at six, just under the\n"
            "   Memorial. You can't come home to dinner, you know, because\n"
            "   he might flare up; but you can turn in at lunch every day\n"
            "   you please except Saturday and Sunday. I intend to be so\n"
            "   jolly down at Glenbogie. You mustn't be shooting always."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "come.here" not in full_text

    def test_wrap_029_this_weather(self):
        # Source: Ayalas Angel, wrap corruption: this.weather
        passage = (
            "As for riding, I don't dare to sit upon a horse this\n"
            "   weather. Nobody but a woman can stand it. Indeed, now I\n"
            "   think of it, I sold my horse last week to pay the fellow\n"
            "   I buy paints from. I've got the saddle and bridle, and if\n"
            "   I stick them up upon a rail, under the trees, it would be\n"
            "   better than any horse while the thermometer is near 80.\n"
            "   All the ladies could come round and talk to one so nicely."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "this.weather" not in full_text

    def test_wrap_030_and_nobody(self):
        # Source: Ayalas Angel, wrap corruption: and.nobody
        passage = (
            "I hate lunch, because it makes me red in the face, and\n"
            "   nobody will give me my breakfast before eleven at the\n"
            "   earliest. But I'll come in about three as often as you\n"
            "   like to have me. I think I perhaps shall run over to the\n"
            "   Tyrol after Glenbogie. A man must go somewhere when he has\n"
            "   been turned out in that fashion. There are so many babies\n"
            "   at Buncombe Hall!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.nobody" not in full_text

    def test_wrap_031_coz_frank(self):
        # Source: Ayalas Angel, wrap corruption: coz.frank
        passage = (
            "it will be told by is to be your poor unfortunate coz,\n"
            "   Frank Houston. Who's going to whimper? Haven't I known\n"
            "   all along what was to come? It has not been my lot in\n"
            "   life to see a flower and pick it because I love it. But\n"
            "   a good head of cabbage when you're hungry is wholesome\n"
            "   food.--Your loving cousin, but not loving as he oughtn't\n"
            "   to love,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "coz.frank" not in full_text

    def test_wrap_032_come_off(self):
        # Source: Ayalas Angel, wrap corruption: come.off
        passage = (
            "We tried to have Ayala here, but I fear it will not come\n"
            "   off. Lady Albury was good-natured, but at last she did not\n"
            "   quite like writing to Mrs. Dosett. So mamma wrote, but the\n"
            "   lady's answer was very stiff. She thought it better for\n"
            "   Ayala to remain among her own friends. Poor Ayala! It is\n"
            "   clear that a knight will be wanted to go in armour, and\n"
            "   get her out of prison. I will leave it to you to say who\n"
            "   must be the knight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "come.off" not in full_text

    def test_wrap_033_shall_remain(self):
        # Source: Ayalas Angel, wrap corruption: shall.remain
        passage = (
            "On the first of October we go back to London, and shall\n"
            "   remain till the end of November. They have asked Nina to\n"
            "   come again in November in order that she may see a hunt. I\n"
            "   know that means that she will try to jump over something,\n"
            "   and have her leg broken. You must be here and not allow\n"
            "   it. If she does come here I shall perhaps go down to\n"
            "   Brighton for a fortnight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shall.remain" not in full_text

    def test_wrap_034_miserable_why(self):
        # Source: Ayalas Angel, wrap corruption: miserable.why
        passage = (
            "They won't let me go! Oh, my darling, I am so miserable!\n"
            "   Why should they not let me go, when people are so kind, so\n"
            "   very kind, as Lady Albury and your dear mamma? I feel as\n"
            "   though I should like to run from the house, and never come\n"
            "   back, even though I had to die in the streets. I was so\n"
            "   happy when I got your letter and Lady Albury's, and now I\n"
            "   am so wretched! I cannot write to Lady Albury. You must\n"
            "   just tell her, with many thanks from me, that they will\n"
            "   not let me go!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "miserable.why" not in full_text

    def test_wrap_035_has_set(self):
        # Source: Ayalas Angel, wrap corruption: has.set
        passage = (
            "He has proposed to her, and she has rejected him. He has\n"
            "   set his heart upon the matter, and I am most anxious that\n"
            "   he should succeed, because I know him to be a man who\n"
            "   will not easily brook disappointment where he has set his\n"
            "   heart. Of all men I know he is the most steadfast in his\n"
            "   purpose."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "has.set" not in full_text

    def test_wrap_036_use_your(self):
        # Source: Ayalas Angel, wrap corruption: use.your
        passage = (
            "I have thought it right to tell you this. You will use\n"
            "   your own judgment in saying what you think fit to your\n"
            "   niece. Should she be made to understand that her own\n"
            "   immediate friends approve of the offer, she would probably\n"
            "   be induced to accept it. I have not heard my cousin say\n"
            "   what may be his future plans. I think it possible that,\n"
            "   as he is quite in earnest, he will not take one repulse.\n"
            "   Should he ask again, I hope that your niece may receive\n"
            "   him with altered views."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "use.your" not in full_text

    def test_wrap_037_think_that(self):
        # Source: Ayalas Angel, wrap corruption: think.that
        passage = (
            "What ought to be done? Of course, I don't like to think\n"
            "   that you should be kept waiting. I am not sure that I\n"
            "   quite like it myself. I will do anything you propose, and\n"
            "   am not afraid of running a little risk. If we could get\n"
            "   married without his knowing anything about it, I am sure\n"
            "   he would give the money afterwards,--because he is always\n"
            "   so good-natured in the long run, and so generous. He can\n"
            "   be very savage, but he would be sure to forgive."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "think.that" not in full_text

    def test_wrap_038_shall_not(self):
        # Source: Ayalas Angel, wrap corruption: shall.not
        passage = (
            "I want to see you on most important business. If I shall\n"
            "   not be troubling you, I will call upon you to-morrow at\n"
            "   ten o'clock, before I go to my place of business."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shall.not" not in full_text

    def test_wrap_039_england_because(self):
        # Source: Ayalas Angel, wrap corruption: england.because
        passage = (
            "Of course, I know that duels cannot be fought in England\n"
            "   because of the law. I am sorry that the law should have\n"
            "   been altered, because it allows so many cowards to escape\n"
            "   the punishment they deserve."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "england.because" not in full_text

    def test_wrap_040_the_world(self):
        # Source: Ayalas Angel, wrap corruption: the.world
        passage = (
            "France, Belgium, Italy, the United States, and all the\n"
            "   world, are open! I will meet you wherever you may choose\n"
            "   to arrange a meeting. I presume that you will prefer\n"
            "   pistols."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.world" not in full_text

    def test_wrap_041_who_will(self):
        # Source: Ayalas Angel, wrap corruption: who.will
        passage = (
            "I send this by the hands of my friend, Mr. Faddle, who\n"
            "   will be prepared to make arrangements with you, or with\n"
            "   any friend on your behalf. He will bring back your reply,\n"
            "   which no doubt will be satisfactory.--I am, Sir, your most\n"
            "   obedient servant,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "who.will" not in full_text

    def test_wrap_042_circumstan_should(self):
        # Source: Ayalas Angel, wrap corruption: circumstances.should
        passage = (
            "I may as well go on to declare that under no circumstances\n"
            "   should I fight a duel with you. If I thought I had done\n"
            "   wrong in the matter I would beg your pardon. I can't\n"
            "   do that as it is,--though I am most anxious to appease\n"
            "   you,--because I have done you no wrong."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "circumstances.should" not in full_text

    def test_wrap_043_time_before(self):
        # Source: Ayalas Angel, wrap corruption: time.before
        passage = (
            "And, perhaps, with another object;--to gain a little time\n"
            "   before I plunge into the stern necessity of answering all\n"
            "   that you say in your very comprehensive letter of five\n"
            "   lines. The first four lines I have answered. There will be\n"
            "   no such Mrs. Frank Houston as that suggested. And then, as\n"
            "   to the last line. Of course, you will see me again, and\n"
            "   that very speedily. So it would seem that the whole letter\n"
            "   is answered."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "time.before" not in full_text

    def test_wrap_044_can_manage(self):
        # Source: Ayalas Angel, wrap corruption: can.manage
        passage = (
            "I will come to you about three on Sunday. If you can\n"
            "   manage that your brother should go out and make his calls,\n"
            "   and your sister attend divine service in the afternoon, it\n"
            "   would be a comfort."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "can.manage" not in full_text

    def test_wrap_045_may_change(self):
        # Source: Ayalas Angel, wrap corruption: may.change
        passage = (
            "You have changed your mind so often that of course you may\n"
            "   change it again. I am sure that Imogene expects that you\n"
            "   will. Indeed I can hardly believe that you intend to be\n"
            "   such a Quixote. But at any rate I have done my duty. She\n"
            "   is old enough to look after herself, but as long as she\n"
            "   lives with me as my sister I shall tell her what I think;\n"
            "   and until she becomes your wife,--which I hope she never\n"
            "   will be,--I shall tell you the same."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "may.change" not in full_text

    def test_wrap_046_mamma_seems(self):
        # Source: Ayalas Angel, wrap corruption: mamma.seems
        passage = (
            "At any rate, pray write immediately;--and do come! Mamma\n"
            "   seems to think that papa will give way because I am so\n"
            "   ill. If so, I shall think my illness the luckiest thing\n"
            "   in the world.--You must believe, dearest Frank, that I am\n"
            "   now, as ever, yours most affectionately,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mamma.seems" not in full_text

    def test_wrap_047_coming_down(self):
        # Source: Ayalas Angel, wrap corruption: coming.down
        passage = (
            "Colonel Stubbs will be here, and, as he will be coming\n"
            "   down on the twentieth, would be glad to travel by the same\n"
            "   train, so that he may look after your ticket and your\n"
            "   luggage, and be your slave for the occasion. He will leave\n"
            "   the Paddington Station by the 4 P.M. train if that will\n"
            "   suit you."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "coming.down" not in full_text

    def test_wrap_048_little_affair(self):
        # Source: Ayalas Angel, wrap corruption: little.affair
        passage = (
            "We all think that he behaved beautifully in that little\n"
            "   affair at the Haymarket theatre. I should not mention it\n"
            "   only that everybody has heard of it. Almost any other man\n"
            "   would have struck the poor fellow again; but he is one\n"
            "   of the very few who always know what to do at the moment\n"
            "   without taking time to think of it."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "little.affair" not in full_text

    def test_wrap_049_certain_gentleman(self):
        # Source: Ayalas Angel, wrap corruption: certain.gentleman
        passage = (
            "I am very glad of what you tell me about the certain\n"
            "   gentleman, because I don't think I could have been happy\n"
            "   at Stalham if he had been there. It surprised me so much\n"
            "   that I could not think that he meant it in earnest. We\n"
            "   never hardly spoke to each other when we were in the house\n"
            "   together."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "certain.gentleman" not in full_text

    def test_wrap_050_mention_there(self):
        # Source: Ayalas Angel, wrap corruption: mention.there
        passage = (
            "I will come down by an earlier train than you mention.\n"
            "   There is one at 2.15, and then I need not be in the dark\n"
            "   all the way. You need not say anything about this to\n"
            "   Colonel Stubbs, because I do not at all mind travelling by\n"
            "   myself.--Yours affectionately,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mention.there" not in full_text

    def test_wrap_051_not_engaged(self):
        # Source: Ayalas Angel, wrap corruption: not.engaged
        passage = (
            "As far as I know, or her aunt, your cousin Ayala is not\n"
            "   engaged to marry any one. But I should deceive you if I\n"
            "   did not add my belief that she is resolved not to accept\n"
            "   the offer you have done her the honour to make her."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "not.engaged" not in full_text

    def test_wrap_052_that_women(self):
        # Source: Ayalas Angel, wrap corruption: that.women
        passage = (
            "Enticed! Of course you have enticed me. I suppose that\n"
            "   women do as a rule entice men, either to their advantage\n"
            "   or disadvantage. I will leave it to you to say whether\n"
            "   you believe that such enticement, if it be allowed its\n"
            "   full scope, will lead to one or the other as far as I am\n"
            "   concerned. I never was so happy as when I felt that you\n"
            "   had enticed me back to the hopes of former days."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.women" not in full_text

    def test_wrap_053_will_want(self):
        # Source: Ayalas Angel, wrap corruption: will.want
        passage = (
            "As you are going to be married too, you, I suppose, will\n"
            "   want some new finery. I therefore send a cheque. Write\n"
            "   your name on the back of it, and give it to your uncle. He\n"
            "   will let you have the money as you want it."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "will.want" not in full_text

    def test_wrap_054_telegraph_for(self):
        # Source: Barchester Towers, wrap corruption: telegraph.for
        passage = (
            "By Electric Telegraph.\n"
            "   For the Earl of ----, Downing Street, or elsewhere.\n"
            "   The Bishop of Barchester is dead.\n"
            "   Message sent by the Rev. Septimus Harding."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "telegraph.for" not in full_text

    def test_wrap_055_tomorrow_morning(self):
        # Source: Barchester Towers, wrap corruption: tomorrow.morning
        passage = (
            "Will you favour me by calling on me at the palace to-morrow\n"
            "   morning at 9:30 A.M. The bishop wishes me to speak to you\n"
            "   touching the hospital. I hope you will excuse my naming so\n"
            "   early an hour. I do so as my time is greatly occupied. If,\n"
            "   however, it is positively inconvenient to you, I will change\n"
            "   it to 10. You will, perhaps, be kind enough to let me have a\n"
            "   note in reply."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tomorrow.morning" not in full_text

