import pytest
from fast_sentence_segment import segment_text


class TestEbooksBuchan:
    """Integration tests mined from John Buchan ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1920s
    """

    def test_wrap_001_francis_writes(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: francis.writes
        passage = (
            "“Like most brothers, they fought. In the same letter Francis\n"
            "    writes: ‘You, who used with difficulty to part us after\n"
            "    fighting in old days, know what we were to each other’; and,\n"
            "    indeed, they had at bottom that love for each other which, it\n"
            "    seems to me, only twin brothers have; nor do I believe that\n"
            "    they were ever happy if for many hours they were separated."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "francis.writes" not in full_text

    def test_wrap_002_mother_when(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: mother.when
        passage = (
            "“I always received so much kindness from your father and mother\n"
            "    when I was young, that you may depend on my helping you as\n"
            "    much as I can; and when I am in England my house will always\n"
            "    produce a corner for you and a bottle of the best. You have\n"
            "    your brothers also to advise and help you. But to be successful\n"
            "    in life you must depend on your own exertions, and therefore I\n"
            "    hope you will work hard and learn to be punctual and support\n"
            "    your masters."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mother.when" not in full_text

    def test_wrap_003_pheasants_and(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: pheasants.and
        passage = (
            "“Read your Bibles, and shoot well ahead of the cock pheasants;\n"
            "    and if you are ever in any difficulty that your brothers can’t\n"
            "    help you in, come to your very affectionate"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pheasants.and" not in full_text

    def test_wrap_004_roberts_death(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: roberts.death
        passage = (
            "“P. S.—Since writing this, I have heard of dear Robert’s\n"
            "    death. He died a gallant death for his Queen and country....\n"
            "    Well! he is with God—and your mother—and there we can afford to\n"
            "    leave him.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "roberts.death" not in full_text

    def test_wrap_005_with_professors(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: with.professors
        passage = (
            "“I have learned one thing by my reading and conversation with\n"
            "    professors. You and I go at a subject all wrong. Don’t read\n"
            "    Life of Wellington and the history of his wars, but take a\n"
            "    period and study it as a whole.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "with.professors" not in full_text

    def test_wrap_006_about_america(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: about.america
        passage = (
            "“I had a good talk to Haldane late in the evening about\n"
            "    America, the Shipping Combine, etc. He said that the great\n"
            "    difference between the American and the Englishman was that\n"
            "    the American boy was always thinking how soon he could get on\n"
            "    in business, while the latter was always thinking how long he\n"
            "    could keep out of it...."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "about.america" not in full_text

    def test_wrap_007_jackson_his(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: jackson.his
        passage = (
            "“Met Harry Rawlinson in the Park. Talked of Stonewall Jackson,\n"
            "    his power as a leader of men and judge of character. Lee was\n"
            "    the thinker and Jackson the actor. Harry R. poked my pony in\n"
            "    the ribs and said, ‘What sort of thing is that?’ whereat my\n"
            "    beast promptly landed his a kick in the stomach.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "jackson.his" not in full_text

    def test_wrap_008_met_some(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: met.some
        passage = (
            "“After dinner went to an ‘At Home’ of Mrs. Sidney Webb. Met\n"
            "    some rum-looking coves there. Had a talk with Mrs. Webb\n"
            "    about fiscal policy. A Free Trader joined in, and I argued\n"
            "    disgracefully, proved nothing, expressed myself badly, and was\n"
            "    rather trodden on by the Free Trader, who knew his points.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "met.some" not in full_text

    def test_wrap_009_party_composed(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: party.composed
        passage = (
            "“Dined with Lady Salisbury in Arlington Street—a jolly party,\n"
            "    composed of Lord Hugh Cecil, Winston Churchill, Lady Mabel\n"
            "    Palmer, Neil Primrose, Lady Crewe, Lady Aldra Acheson, and Sir\n"
            "    Edgar Vincent. Sat next and bucked to Lady Aldra. W. Churchill\n"
            "    held forth at dinner to the whole table, discussing invasion.\n"
            "    Salisbury said he thought that if one was going to make a\n"
            "    speech one ought to do nothing else the whole day.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "party.composed" not in full_text

    def test_wrap_010_three_years(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: three.years
        passage = (
            "“Lastly, as to working it. Don’t fret about two or three\n"
            "    years’ seniority. You must risk something, especially in the\n"
            "    Cavalry. Officers seem to play leap-frog over one another in\n"
            "    the most surprising manner nowadays. So my advice is to take\n"
            "    the first chance you can of joining the 9th, either by transfer\n"
            "    or exchange.... Arrange to come and stay with me here for two\n"
            "    or three weeks, and we will do our best to push the matter\n"
            "    through.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "three.years" not in full_text

    def test_wrap_011_cannot_come(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: cannot.come
        passage = (
            "“I have to write a very sad letter to tell you that I cannot\n"
            "    come to India after all. The cursed City seems to have turned\n"
            "    round, and a small boom to be in progress. The result is that\n"
            "    the Charter Trust want me home.... I have thoroughly thought\n"
            "    the position over the last five days, and, greatly against my\n"
            "    will, decided to return."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "cannot.come" not in full_text

    def test_wrap_012_more_money(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: more.money
        passage = (
            "“(1.) I am comfortably off, and at present don’t want more\n"
            "    money. I am far more anxious to be a clever and common-sense\n"
            "    man with sufficient money than an ordinary rich ‘City man’;\n"
            "    and so it is far better for me to travel and see the world and\n"
            "    return to England in four months, which, after all, is not much\n"
            "    time to lose, when one has the remainder of one’s life to spend\n"
            "    in business."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "more.money" not in full_text

    def test_wrap_013_the_idea(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: the.idea
        passage = (
            "“(1.) I have worked hard for five years in the City with the\n"
            "    idea of making business my career; and to miss ‘good times’\n"
            "    when you have been through the ‘bad times’ and learned fairly\n"
            "    thoroughly your trade is the same thing as a soldier studying\n"
            "    soldiering during a long peace and then not going to the war\n"
            "    when the chance comes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.idea" not in full_text

    def test_wrap_014_been_besides(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: been.besides
        passage = (
            "“(2.) The idea of my travelling in America and Africa has been,\n"
            "    besides getting a good education, to learn the opportunities\n"
            "    that offer in the countries, to turn them to some good. I have\n"
            "    already lost a good chance by Americans having done well (and\n"
            "    especially the railways I saw) since I have been in Africa."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "been.besides" not in full_text

    def test_wrap_015_generals_mahon(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: generals.mahon
        passage = (
            "“Got to camp about 12.30. Most delightful situation. Generals\n"
            "    Mahon and Douglas Haig there, and we made many pals. At\n"
            "    5 p.m. F. G. and I went out riding and schooled the horses,\n"
            "    nearly slaying two wretched cattle in the attempt. Found a sow\n"
            "    and galloped after her. A jolly evening, and to bed early."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "generals.mahon" not in full_text

    def test_wrap_016_prospects_for(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: prospects.for
        passage = (
            "“I have been thinking about you and your future prospects\n"
            "    for some time, and I have quite come to the opinion that you\n"
            "    are wasted hunting for money. In England people are very\n"
            "    narrow-minded, and the ruling idea (especially in our family)\n"
            "    is that one must be rich."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "prospects.for" not in full_text

    def test_wrap_017_nice_but(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: nice.but
        passage = (
            "“I am beginning to think otherwise. To be rich is very nice,\n"
            "    but you are no happier, and you do your country no good.\n"
            "    Both C. and A. have been successful, but beyond buying extra\n"
            "    hunters, deer forests, and houses, to me they have not attained\n"
            "    a very high position. I would rather you chucked the City. I\n"
            "    think you should enter Parliament and work your way to the\n"
            "    Cabinet; I would far rather you succeeded in politics than in\n"
            "    the City."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "nice.but" not in full_text

    def test_wrap_018_you_advice(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: you.advice
        passage = (
            "“You know Hugh Cecil, Milner, and Co. They should all give you\n"
            "    advice. I hope you will think this over, and that your thoughts\n"
            "    will be guided rather by the amount you will help the nation\n"
            "    than by the amount with which you will fill your pocket."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.advice" not in full_text

    def test_wrap_019_general_uncle(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: general.uncle
        passage = (
            "“The Uncle                      General.\n"
            "    “Uncle Harry                    Admiral.\n"
            "    “First Cousin Jack Maxwell      General.\n"
            "    “Harold                         Colonel.\n"
            "    “R. G.                          Winner of Kadir.\n"
            "    “F. G.                             ”   ”  Championship.\n"
            "    “Cecil                          2nd in National."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "general.uncle" not in full_text

    def test_wrap_020_you_know(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: you.know
        passage = (
            "“I made great pals with Mrs. Asquith. I do not know if you\n"
            "    know her, but she is an absolute clinker. She dressed up as\n"
            "    a Spanish dancer, and did a pas seul before us all. What\n"
            "    will people say in about twenty years when they hear this! The\n"
            "    leading lady of the Government dancing a pas seul, while\n"
            "    the Chancellor of the Exchequer looked on! Hugh Cecil said he\n"
            "    thought he had dislocated the inner organs of his body from\n"
            "    laughter."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.know" not in full_text

    def test_wrap_021_which_have(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: which.have
        passage = (
            "“And now for secrets.... [Here follow certain matters which\n"
            "    have long ago been made public.] Read to-day’s Times, F.\n"
            "    G. There is about half a column on the political situation,\n"
            "    which gives you much of what I have written above. Asquith was\n"
            "    fearfully perturbed about how they got hold of it, for only\n"
            "    six people knew the situation—himself, Grey, Haldane, C.-B.,\n"
            "    Morley, Tweedmouth, and (proclaim it to your ancestors!) R. G."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "which.have" not in full_text

    def test_wrap_022_curzon_arrived(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: curzon.arrived
        passage = (
            "“Here is an amusing story of Lady Curzon. The day after Curzon\n"
            "    arrived there was a bad accident at Charing Cross. Half the\n"
            "    roof fell in, owing to a girder snapping. Lady Curzon said\n"
            "    wittily that ‘Brodrick must have cut that girder on purpose,\n"
            "    but—so like him—was a day late!’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "curzon.arrived" not in full_text

    def test_wrap_023_think_much(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: think.much
        passage = (
            "“There was a strong wind blowing down the ground which I think\n"
            "    much spoilt the game. At times it was very slow and sticky—I\n"
            "    think partly from the polo being so high class and each fellow\n"
            "    stopping the other one hitting out. The ball continually hit\n"
            "    a pony in the hock and bounded out, and we were several times\n"
            "    stopped for accidents."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "think.much" not in full_text

    def test_wrap_024_than_most(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: than.most
        passage = (
            "“I find I stick hardships and discomforts far better than\n"
            "    most. I have found my way about in this country by day and\n"
            "    by night—no easy matter. I can outstay most of the others as\n"
            "    regards fatigue. I seem to have got great confidence—far more\n"
            "    than before—and I look on myself as as good a player as anybody\n"
            "    else. Several chaps whom I used to look on as good I now look\n"
            "    on as very bad.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "than.most" not in full_text

    def test_wrap_025_herr_dernburgs(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: herr.dernburgs
        passage = (
            "“I think every serious person out here is awakened by Herr\n"
            "    Dernburg’s visit to this country. He is the Joe Chamberlain of\n"
            "    Germany. I believe that the Dutch luckily hate the Germans, and\n"
            "    will always support us against them.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "herr.dernburgs" not in full_text

    def test_wrap_026_our_army(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: our.army
        passage = (
            "“I am thinking of writing to Colonel Repington to wake up our\n"
            "    army about the use of machine guns. The nation which first\n"
            "    studies them and employs them scientifically in the next war\n"
            "    will gain an immense advantage over a nation which neglects\n"
            "    their use. At present, I fear, we will be in the same position\n"
            "    as the Austrians in 1866.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "our.army" not in full_text

    def test_wrap_027_for_four(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: for.four
        passage = (
            "“Whitney determined to try to win this cup four years ago. For\n"
            "    four years he has been collecting all the ponies he could, and\n"
            "    all his team has been trained to play together. The Waterburys\n"
            "    are two magnificent players. Larry is the champion racquet\n"
            "    player of America. They have played polo since they were ten,\n"
            "    and always together. To get the cup back we must do likewise.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "for.four" not in full_text

    def test_wrap_028_sportsmen_killed(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: sportsmen.killed
        passage = (
            "“The polo world mourns many fine players and good sportsmen\n"
            "    killed in the war, but for none is more sorrow and regret\n"
            "    expressed than for the gallant Twins. I knew Rivy intimately\n"
            "    for a considerable time before I met Francis. I think it was\n"
            "    in 1902 that his older brother Cecil asked me to take him to\n"
            "    Spring Hill and teach him the rudiments of polo. He came and\n"
            "    spent a happy month, working like a stable lad and putting his\n"
            "    whole heart and soul into his work."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sportsmen.killed" not in full_text

    def test_wrap_029_will_have(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: will.have
        passage = (
            "“I am not going to form any opinion until October, when I will\n"
            "    have had time for reflection. The Germans certainly beat us,\n"
            "    even our private soldiers, at drinking beer. I sat next to a\n"
            "    gentleman yesterday who drank five pints before I drank one\n"
            "    glass of water. He would have had a sixth, but when the sixth\n"
            "    was brought his wife took the glass and downed it before him.\n"
            "    The result is that a great many men and most women are as fat\n"
            "    as cattle...."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "will.have" not in full_text

    def test_wrap_030_restaurant_mass(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: restaurantsone.mass
        passage = (
            "“Berlin is one mass of demi-mondaines, cafés, restaurants—one\n"
            "    mass. The great entertainment place is the Palais de Dance.\n"
            "    It is most luxurious, and you might, if you did not look at\n"
            "    the women, think you were at a London ball. The women are most\n"
            "    respectable-looking, but you can see that if you want to dance\n"
            "    you will get plenty of exercise, as once round any of the\n"
            "    dancers is equal to about twice round Liverpool.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "restaurantsone.mass" not in full_text

    def test_wrap_031_rivy_and(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: rivy.and
        passage = (
            "“My dear Lord Grey, you were a very, very good friend to Rivy,\n"
            "    and you and your family have done all you could to enrich and\n"
            "    ennoble his life. He dearly loved you all, and valued nothing\n"
            "    more in the world than your friendship, and admired nothing\n"
            "    more than your character. I hope that since we can no more talk\n"
            "    of the ‘Twins’ you will always remember Rivy and accept the\n"
            "    gratitude of your broken-hearted friend.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rivy.and" not in full_text

    def test_wrap_032_the_streets(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: the.streets
        passage = (
            "“On arrival at Bailleul a terrible fire suddenly opened in the\n"
            "    streets, which was very alarming to us caged in the ambulance.\n"
            "    Luckily it proved only to be firing at an aeroplane. We were\n"
            "    taken to a convent, and my stretcher was put down, curiously\n"
            "    enough, alongside Basil Blackwood and Jack Wodehouse. Basil\n"
            "    Blackwood and I, I have since heard, were the only two to\n"
            "    escape that day from Messines.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.streets" not in full_text

    def test_wrap_033_bless_you(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: bless.you
        passage = (
            "“You have all my very, very best wishes and thoughts. God bless\n"
            "    you and keep you, and help you to remain the finest squadron in\n"
            "    the world—the only squadron that has got for itself already a\n"
            "    D.C.M., a Legion d’Honneur, a commission, and a V.C., for what\n"
            "    is won by the leaders belongs to the men. God bless you all.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bless.you" not in full_text

    def test_wrap_034_ponies_kitty(self):
        # Source: Francis and Riversdale Grenfell B a Memoir, wrap corruption: ponies.kitty
        passage = (
            "Ponies:\n"
            "    “Kitty,” 7, 8;\n"
            "    “Snipe,” 51;\n"
            "    “Barmaid,” 59, 61, 62;\n"
            "    “Cocos,” 61, 63;\n"
            "    “Recluse,” 62;\n"
            "    “Despair,” 111;\n"
            "    “Sweetbriar,” 113, 137;\n"
            "    “Cinderella,” 115, 140, 142, 143."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ponies.kitty" not in full_text

    def test_wrap_035_mane_but(self):
        # Source: Greenmantle, wrap corruption: mane.but
        passage = (
            "“Mony’s the ane for him maks mane,\n"
            "     But nane sall ken whar he is gane.\n"
            "     Ower his white banes, when they are bare,\n"
            "     The wind sall blaw for evermair.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mane.but" not in full_text

    def test_wrap_036_true_and(self):
        # Source: Greenmantle, wrap corruption: true.and
        passage = (
            "“He captured Harper’s Ferry, with his nineteen men so true,\n"
            "     And he frightened old Virginny till she trembled through and\n"
            "     through.\n"
            "     They hung him for a traitor, themselves the traitor crew,\n"
            "     But his soul goes marching along.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "true.and" not in full_text

    def test_wrap_037_all_cram(self):
        # Source: Huntingtower, wrap corruption: all.cram
        passage = (
            "\"What's a man's age? He must hurry more, that's all;\n"
            "       Cram in a day, what his youth took a year to hold:\n"
            "       When we mind labour, then only, we're too old--\n"
            "     What age had Methusalem when he begat Saul?\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.cram" not in full_text

    def test_wrap_038_ballet_the(self):
        # Source: Huntingtower, wrap corruption: ballet.the
        passage = (
            "\"Sunflowers, tall Grenadiers, ogle the roses' short-skirted ballet.\n"
            "     The fumes of dark sweet wine hidden in frail petals\n"
            "     Madden the drunkard bees.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ballet.the" not in full_text

    def test_wrap_039_song_after(self):
        # Source: Huntingtower, wrap corruption: song.after
        passage = (
            "\"Thou shalt hear a song\n"
            "    After a while which Gods may listen to;\n"
            "    But place the flask upon the board and wait\n"
            "    Until the stranger hath allayed his thirst,\n"
            "    For poets, grasshoppers and nightingales\n"
            "    Sing cheerily but when the throat is moist.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "song.after" not in full_text

    def test_wrap_040_bonny_toorooraro(self):
        # Source: Huntingtower, wrap corruption: bonny.tooroorarooraloo
        passage = (
            "\"The Boorjoys' brays are bonny,\n"
            "       Too-roo-ra-roo-raloo,\n"
            "     But the Worrkers o' the Worrld\n"
            "       Wull gar them a' look blue,\n"
            "     Wull gar them a' look blue,\n"
            "       And droon them in the sea,\n"
            "     And--for bonnie Annie Laurie\n"
            "       I'll lay me down and dee.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bonny.tooroorarooraloo" not in full_text

    def test_wrap_041_arise_wave(self):
        # Source: Huntingtower, wrap corruption: arise.wave
        passage = (
            "\"Proley Tarians, arise!\n"
            "     Wave the Red Flag to the skies,\n"
            "     Heed nae mair the Fat Man's lees,\n"
            "       Stap them doun his throat!\n"
            "     Nocht to loss except our chains,\n"
            "     We maun drain oor dearest veins--\n"
            "     A' the worrld shall be our gains----\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "arise.wave" not in full_text

    def test_wrap_042_leant_and(self):
        # Source: Huntingtower, wrap corruption: leant.and
        passage = (
            "\"And on her lover's arm she leant,\n"
            "       And round her waist she felt it fold,\n"
            "     And far across the hills they went\n"
            "       In that new world which is the old:\n"
            "     Across the hills, and far away\n"
            "       Beyond their utmost purple rim,\n"
            "     And deep into the dying day\n"
            "       The happy princess followed him.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "leant.and" not in full_text

    def test_wrap_043_sailorbred_and(self):
        # Source: John Burnet of Barns a Romance, wrap corruption: sailorbred.and
        passage = (
            "\"Oh, if my love were sailor-bred\n"
            "      And fared afar from home,\n"
            "    In perilous lands, by shoal and sands,\n"
            "      If he were sworn to roam,\n"
            "    Then, O, I'd hie me to a ship,\n"
            "      And sail upon the sea,\n"
            "    And keep his side in wind and tide\n"
            "      To bear him company."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sailorbred.and" not in full_text

    def test_wrap_044_gay_and(self):
        # Source: John Burnet of Barns a Romance, wrap corruption: gay.and
        passage = (
            "\"And if he were a soldier gay,\n"
            "      And tarried from the town,\n"
            "    And sought in wars, through death and scars,\n"
            "      To win for him renown,\n"
            "    I'd place his colours in my breast,\n"
            "      And ride by moor and lea,\n"
            "    And win his side, there to abide,\n"
            "      And bear him company."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gay.and" not in full_text

    def test_wrap_045_bairns_fell(self):
        # Source: John Burnet of Barns a Romance, wrap corruption: bairns.fell
        passage = (
            "Tam o' the Linn and a' his bairns\n"
            "    Fell into the fire in ilk ither's airms.\n"
            "    \"Eh,\" quoth the binmost, \"I have a het skin.\"\n"
            "    \"It's hetter below,\" quo' Tam o' the Linn."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bairns.fell" not in full_text

    def test_wrap_046_light_the(self):
        # Source: John Burnet of Barns a Romance, wrap corruption: light.the
        passage = (
            "\"First shall the heavens want starry light,\n"
            "      The seas be robbed of their waves;\n"
            "    The day want sun, the sun want bright,\n"
            "      The night want shade, and dead men graves;\n"
            "        The April, flowers and leaf and tree,\n"
            "        Before I false my faith to thee.\n"
            "          To thee, to thee.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "light.the" not in full_text

    def test_wrap_047_peace_and(self):
        # Source: John Burnet of Barns a Romance, wrap corruption: peace.and
        passage = (
            "\"First direful Hate shall turn to Peace,\n"
            "      And Love relent in deep disdain;\n"
            "    And Death his fatal stroke shall cease,\n"
            "      And Envy pity every pain;\n"
            "        And Pleasure mourn, and Sorrow smile,\n"
            "        Before I talk of any guile.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "peace.and" not in full_text

    def test_wrap_048_race_and(self):
        # Source: John Burnet of Barns a Romance, wrap corruption: race.and
        passage = (
            "\"First Time shall stay his stayless race,\n"
            "      And Winter bless his brows with corn;\n"
            "    And snow bemoisten July's face,\n"
            "      And Winter, Spring and Summer mourn.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "race.and" not in full_text

    def test_wrap_049_crew_will(self):
        # Source: Midwinter Certain Travellers in Old England, wrap corruption: crew.will
        passage = (
            "\"Diana and her darling crew\n"
            "    Will pluck your fingers fine,\n"
            "  And lead you forth right pleasantly\n"
            "    To drink the honey wine,--\n"
            "  To drink the honey wine, my dear,\n"
            "    And sup celestial air,\n"
            "  And dance as the young angels dance,\n"
            "    Ah, God, that I were there!\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "crew.will" not in full_text

    def test_wrap_050_much_that(self):
        # Source: Midwinter Certain Travellers in Old England, wrap corruption: much.that
        passage = (
            "\"O Love, they wrong thee much\n"
            "    That say thy sweet is bitter.\n"
            "  When thy rich fruit is such\n"
            "    As nothing can be sweeter.\n"
            "  Fair house of joy and bliss,\n"
            "  Where truest treasure is,\n"
            "    I do adore thee.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "much.that" not in full_text

    def test_wrap_051_news_twang(self):
        # Source: Midwinter Certain Travellers in Old England, wrap corruption: news.twang
        passage = (
            "\"O Brother Sawney, hear you the news?\n"
            "  Twang 'em, we'll bang 'em and\n"
            "    Hang 'em up all.\n"
            "  An army's just coming without any shoes,\n"
            "  Twang 'em, we'll bang 'em, and\n"
            "    Hang 'em up all.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "news.twang" not in full_text

    def test_wrap_052_the_vale(self):
        # Source: Poems Scots and English, wrap corruption: the.vale
        passage = (
            "(From Alexander Cargill, Elder of the Kirk of the Remnant in the\n"
            "    vale of Wae, to the Reverend Murdo Mucklethraw, Minister of the\n"
            "    aforesaid Kirk, anent the Great Case recently argued in the House\n"
            "    of Lords.)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.vale" not in full_text

    def test_wrap_053_bye_the(self):
        # Source: Poems Scots and English, wrap corruption: bye.the
        passage = (
            "For me, my lambin’-time was bye,\n"
            "    The muirland hay was nane sae high,\n"
            "    The men were thrang, the grund was dry,\n"
            "          Sae when ye spak,\n"
            "    And bade me gang and testify,\n"
            "          I heldna back."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bye.the" not in full_text

    def test_wrap_054_morn_reflectin(self):
        # Source: Poems Scots and English, wrap corruption: morn.reflectin
        passage = (
            "Wi’ dowie hert I left that morn,\n"
            "    Reflectin’ on the waefu’ scorn\n"
            "    The Kirk maun thole, her courts forlorn,\n"
            "          Her pillars broke,\n"
            "    While Amalek exalts his horn,\n"
            "          And fills his poke."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "morn.reflectin" not in full_text

    def test_wrap_055_sair_the(self):
        # Source: Poems Scots and English, wrap corruption: sair.the
        passage = (
            "I pondered the mischances sair\n"
            "    The Lord had garred puir Scotland bear\n"
            "    Frae English folk baith late and ear’\n"
            "          Sin’ Flodden year\n"
            "    To the twae beasts at Carlisle fair\n"
            "          I bocht ower dear."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sair.the" not in full_text

