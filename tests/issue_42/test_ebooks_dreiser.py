import pytest
from fast_sentence_segment import segment_text


class TestEbooksDreiser:
    """Integration tests mined from Theodore Dreiser ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1910s
    """

    def test_wrap_001_business_department(self):
        # Source: A Book About Myself, wrap corruption: business.department
        passage = (
            "Wanted: A number of bright young men to assist in the business\n"
            "    department during the Christmas holidays. Promotion possible.\n"
            "    Apply to Business Manager between 9 and 10 a.m."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "business.department" not in full_text

    def test_wrap_002_know_that(self):
        # Source: A Book About Myself, wrap corruption: know.that
        passage = (
            "“Anyhow, Theo, that isn’t what I’m writing you for. You know\n"
            "    that you haven’t been just the same to me as you once were. I\n"
            "    know how you feel. I have felt it too. I want to know if you\n"
            "    won’t send me back the letters I wrote you. You won’t want them\n"
            "    now. Please send them, Theo, and believe I am as ever your\n"
            "    friend,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "know.that" not in full_text

    def test_wrap_003_street_the(self):
        # Source: A Book About Myself, wrap corruption: street.the
        passage = (
            "“I stood by the window last night and looked out on the street.\n"
            "    The moon was shining and those dead trees over the way were\n"
            "    waving in the wind. I saw the moon on that little pool of water\n"
            "    over in the field. It looked like silver. Oh, Theo, I wish I\n"
            "    were dead.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "street.the" not in full_text

    def test_wrap_004_strike_you(self):
        # Source: A Book About Myself, wrap corruption: strike.you
        passage = (
            "“Tomorrow is my wedding-day. Tomorrow at twelve. This may strike\n"
            "    you as strange. Well, I have waited—I don’t know how long—it has\n"
            "    seemed like years to me—for some word, but I knew it was not to\n"
            "    be. Your last letter showed me that. I knew that you did not\n"
            "    intend to return, and so I went back to Mr. ——. I had to. What\n"
            "    else have I to look forward to? You know how unhappy I am here\n"
            "    with my family, now that you are gone, in spite of how much they\n"
            "    care for me."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "strike.you" not in full_text

    def test_wrap_005_ever_write(self):
        # Source: A Book About Myself, wrap corruption: ever.write
        passage = (
            "“But I must say good-bye. This is the last letter I shall ever\n"
            "    write you. Don’t send my letters now—tear them up. It is too\n"
            "    late. Oh, if you only knew how hard it has been to bring myself\n"
            "    to this!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ever.write" not in full_text

    def test_wrap_006_open_hearth(self):
        # Source: A Book About Myself, wrap corruption: open.hearth
        passage = (
            "“A train of hot metal, being hauled from a mixing-house to open\n"
            "    hearth No. 2, was side-swiped by a yard engine near the 48-inch\n"
            "    mill. The impact tilted the ladles of some of the cars and the\n"
            "    hot metal spilled in a pool of water along the track. Antony\n"
            "    Brosak, Constantine Czernik and Kafros Maskar were seriously\n"
            "    wounded by the exploding metal.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "open.hearth" not in full_text

    def test_wrap_007_heaven_from(self):
        # Source: A Hoosier Holiday, wrap corruption: heaven.from
        passage = (
            "“Great treasure halls hath Zeus in heaven,\n"
            "  From whence to man strange dooms are given \n"
            "    Past hope or fear.\n"
            "  And the end looked for cometh not,\n"
            "  And a path is there where no man thought. \n"
            "    So hath it fallen here.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "heaven.from" not in full_text

    def test_wrap_008_storm_clouds(self):
        # Source: A Hoosier Holiday, wrap corruption: storm.clouds
        passage = (
            "\"The adventurous sun took heaven by storm,\n"
            "                Clouds scattered largesses of rain,\n"
            "              The sounding cities, rich and warm,\n"
            "                Smouldered and glittered in the plain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "storm.clouds" not in full_text

    def test_wrap_009_wind_sometimes(self):
        # Source: A Hoosier Holiday, wrap corruption: wind.sometimes
        passage = (
            "\"Sometimes it was a wandering wind,\n"
            "                Sometimes the fragrance of the pine,\n"
            "              Sometimes the thought how others sinned,\n"
            "                That turned her sweet blood into wine."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "wind.sometimes" not in full_text

    def test_wrap_010_serenade_complainin(self):
        # Source: A Hoosier Holiday, wrap corruption: serenade.complaining
        passage = (
            "\"Sometimes she heard a serenade,\n"
            "                Complaining, sweetly, far away.\n"
            "              She said, ‘A young man woos a maid’;\n"
            "                And dreamt of love till break of day."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "serenade.complaining" not in full_text

    def test_wrap_011_unfurled_and(self):
        # Source: A Hoosier Holiday, wrap corruption: unfurled.and
        passage = (
            "“For still night’s starry scroll unfurled,\n"
            "                And still the day came like a flood:\n"
            "              It was the greatness of the world\n"
            "                That made her long to use her blood.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "unfurled.and" not in full_text

    def test_wrap_012_under_the(self):
        # Source: A Traveler at Forty, wrap corruption: under.the
        passage = (
            "The young woman who thinks she wants to see the Pope goes under\n"
            "    the name of Margaret,--but I wouldn’t try very hard to bring it\n"
            "    about, because if Margaret went, my daughter would want to go,\n"
            "    and if Margaret and my daughter went, my wife would feel out in\n"
            "    the cold. (The old man can stand it.)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "under.the" not in full_text

    def test_wrap_013_unless_you(self):
        # Source: A Traveler at Forty, wrap corruption: unless.you
        passage = (
            "But don’t try to get that Papal interview for Margaret unless\n"
            "    you can get it for all the ladies. You will introduce a serpent\n"
            "    into my paradise."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "unless.you" not in full_text

    def test_wrap_014_striking_twelve(self):
        # Source: A Traveler at Forty, wrap corruption: striking.twelve
        passage = (
            "The Grand Canal under a glittering moon. The clocks striking\n"
            "    twelve. A horde of black gondolas. Lovely cries. The rest is\n"
            "    silence. Moon picking out the ripples in silver and black.\n"
            "    Think of these old stone steps, white marble stained green,\n"
            "    laved by the waters of the sea these hundreds of years. A long,\n"
            "    narrow street of water. A silent boat passing. And this is a\n"
            "    city of a hundred and sixty thousand!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "striking.twelve" not in full_text

    def test_wrap_015_and_quadrifoil(self):
        # Source: A Traveler at Forty, wrap corruption: and.quadrifoil
        passage = (
            "Wonderful painted arch doorways and windows. Trefoil and\n"
            "    quadrifoil decorations. An old iron gate with some statues\n"
            "    behind it. A balcony with flowers. The Bridge of Sighs! Nothing\n"
            "    could be so perfect as a city of water."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.quadrifoil" not in full_text

    def test_wrap_016_know_what(self):
        # Source: A Traveler at Forty, wrap corruption: know.what
        passage = (
            "The Lagoon at midnight under a full moon. Now I think I know\n"
            "    what Venice is at its best. Distant lights, distant voices.\n"
            "    Some one singing. There are pianos in this sea-isle city,\n"
            "    playing at midnight. Just now a man silhouetted blackly, under\n"
            "    a dark arch. Our gondola takes us into the very hallway of the\n"
            "    Royal-Danieli."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "know.what" not in full_text

    def test_wrap_017_pure_music(self):
        # Source: A Traveler at Forty, wrap corruption: pure.music
        passage = (
            "A gondolier selling vegetables and crying his wares is pure\n"
            "    music. At my feet white steps laved by whitish-blue water.\n"
            "    Tall, cool, damp walls, ten feet apart. Cool, wet, red brick\n"
            "    pavements. The sun shining above makes one realize how lovely\n"
            "    and cool it is here; and birds singing everywhere."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pure.music" not in full_text

    def test_wrap_018_lime_stone(self):
        # Source: A Traveler at Forty, wrap corruption: lime.stone
        passage = (
            "Gondolas doing everything, carrying casks, coal, lumber, lime,\n"
            "    stone, flour, bricks, and boxed supplies generally, and others\n"
            "    carrying vegetables, fruit, kindling and flowers. Only now I\n"
            "    saw a boat slipping by crowded with red geraniums."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lime.stone" not in full_text

    def test_wrap_019_colonnades_trefoils(self):
        # Source: A Traveler at Forty, wrap corruption: colonnades.trefoils
        passage = (
            "Lovely pointed windows and doors; houses, with colonnades,\n"
            "    trefoils, quadrifoils, and exquisite fluted cornices to match,\n"
            "    making every house that strictly adheres to them a jewel. It is\n"
            "    Gothic, crossed with Moorish and Byzantine fancy. Some of them\n"
            "    take on the black and white of London smoke, though why I have\n"
            "    no idea. Others being colored richly at first are weathered by\n"
            "    time into lovely half-colors or tones."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "colonnades.trefoils" not in full_text

    def test_wrap_020_here_latticewor(self):
        # Source: A Traveler at Forty, wrap corruption: here.latticework
        passage = (
            "Latticework is everywhere, and it so obviously belongs here.\n"
            "    Latticework in the churches, the houses, the public buildings.\n"
            "    Venice loves it. It is oriental and truly beautiful."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "here.latticework" not in full_text

    def test_wrap_021_seaweed_how(self):
        # Source: A Traveler at Forty, wrap corruption: seaweed.how
        passage = (
            "Bells over the water, the lap of waves, the smell of seaweed.\n"
            "    How soft and elevated and ethereal voices sound at this time.\n"
            "    An Italian sailor, sitting on the grass looking out over it\n"
            "    all, has his arms about his girl."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "seaweed.how" not in full_text

    def test_wrap_022_cause_you(self):
        # Source: An American Tragedy V 1, wrap corruption: cause.you
        passage = (
            "I'll call for it in a few days. I sign this way so as not to cause\n"
            "    you or me any more trouble, see? But as soon as I feel more sure\n"
            "    that this other thing has blown over, I'll use my own name again,\n"
            "    sure."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "cause.you" not in full_text

    def test_wrap_023_that_you(self):
        # Source: An American Tragedy V 1, wrap corruption: that.you
        passage = (
            "I was surprised and so glad to get my boy's letter and to know that\n"
            "    you were alive and safe. I had hoped and prayed so that you would\n"
            "    return to the straight and narrow path--the only path that will\n"
            "    ever lead you to success and happiness of any kind, and that God\n"
            "    would let me hear from you as safe and well and working somewhere\n"
            "    and doing well. And now he has rewarded my prayers. I knew he\n"
            "    would. Blessed be His holy name."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.you" not in full_text

    def test_wrap_024_here_now(self):
        # Source: An American Tragedy V 1, wrap corruption: here.now
        passage = (
            "As you see, we are now in Denver. We have a mission of our own here\n"
            "    now with housing quarters for all of us. Besides we have a few\n"
            "    rooms to rent which Esta, and you know she is now Mrs. Nixon, of\n"
            "    course, takes care of. She has a fine little boy who reminds your\n"
            "    father and me of you so much when you were a baby. He does little\n"
            "    things that are you all over again so many times that we almost\n"
            "    feel that you are with us again--as you were. It is comforting,\n"
            "    too, sometimes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "here.now" not in full_text

    def test_wrap_025_know_all(self):
        # Source: An American Tragedy V 1, wrap corruption: know.all
        passage = (
            "I want to hear from you often, Clyde. Please write and let us know\n"
            "    all about you and how you are getting along. Won't you? Of course\n"
            "    we love you as much as ever, and will do our best always to try to\n"
            "    guide you right. We want you to succeed more than you know, but we\n"
            "    also want you to be a good boy, and live a clean, righteous life,\n"
            "    for, my son, what matter it if a man gaineth the whole world and\n"
            "    loseth his own soul?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "know.all" not in full_text

    def test_wrap_026_always_with(self):
        # Source: An American Tragedy V 1, wrap corruption: always.with
        passage = (
            "Write your mother, Clyde, and bear in mind that her love is always\n"
            "    with you--guiding you--pleading with you to do right in the name of\n"
            "    the Lord."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "always.with" not in full_text

    def test_wrap_027_please_look(self):
        # Source: An American Tragedy V 1, wrap corruption: please.look
        passage = (
            "\"Please, Clyde, don't be mad at me, will you? Please don't. Please\n"
            "    look at me and speak to me, won't you? I'm so sorry about last\n"
            "    night, really I am--terribly. And I must see you to-night at the\n"
            "    end of Elm Street at 8.30 if you can, will you? I have something to\n"
            "    tell you. Please do come. And please do look at me and tell me you\n"
            "    will, even though you are angry. You won't be sorry. I love you so.\n"
            "    You know I do."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "please.look" not in full_text

    def test_wrap_028_club_will(self):
        # Source: An American Tragedy V 1, wrap corruption: club.will
        passage = (
            "_The Now and Then Club\n"
            "                          Will Hold Its First\n"
            "                          Winter Dinner Dance\n"
            "                            At the Home of\n"
            "                           Douglas Trumbull\n"
            "                           135 Wykeagy Ave.\n"
            "                        On Thursday, December 4\n"
            "                       You Are Cordially Invited\n"
            "             Will You Kindly Reply to Miss Jill Trumbull?_"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "club.will" not in full_text

    def test_wrap_029_coat_belonging(self):
        # Source: An American Tragedy V 2, wrap corruption: coat.belonging
        passage = (
            "\"The girl's brown leather traveling bag, as well as a hat and coat\n"
            "    belonging to her, were left, the bag in the ticket agent's room\n"
            "    at Gun Lodge, which is the railway station five miles east of Big\n"
            "    Bittern, and the hat and coat in the coatroom of the inn at the\n"
            "    Lake, whereas Graham or Golden is said to have taken his suitcase\n"
            "    with him into the boat."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "coat.belonging" not in full_text

    def test_wrap_030_and_guides(self):
        # Source: An American Tragedy V 2, wrap corruption: and.guides
        passage = (
            "\"Golden or Graham, as described by innkeepers and guests and\n"
            "    guides at Grass Lake and Big Bittern, is not more than twenty-four\n"
            "    or twenty-five years of age, slender, dark, and not more than\n"
            "    five feet eight or nine inches tall. At the time he arrived he\n"
            "    was dressed in a light gray suit, tan shoes, and a straw hat and\n"
            "    carried a brown suitcase to which was attached an umbrella and some\n"
            "    other object, presumably a cane."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.guides" not in full_text

    def test_wrap_031_almost_overwhelmi(self):
        # Source: An American Tragedy V 2, wrap corruption: almost.overwhelming
        passage = (
            "\"Subsequent to the indictment, Griffiths, who in spite of almost\n"
            "    overwhelming evidence, has persisted in asserting that the alleged\n"
            "    crime was an accident, and who, accompanied by his counsel, Alvin\n"
            "    Belknap, and Reuben Jephson, of this city, was arraigned before\n"
            "    Supreme Court Justice Oberwaltzer, pleaded not guilty. He was\n"
            "    remanded for trial, which was set for October 15th."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "almost.overwhelming" not in full_text

    def test_wrap_032_all_the(self):
        # Source: An American Tragedy V 2, wrap corruption: all.the
        passage = (
            "\"For I tell you, Clyde, I am sick, very. I feel faint nearly all\n"
            "    the time. And besides, I am so worried as to what I shall do if you\n"
            "    don't come that I am nearly out of my mind.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.the" not in full_text

    def test_wrap_033_and_that(self):
        # Source: An American Tragedy V 2, wrap corruption: and.that
        passage = (
            "\"Clyde, I know that you don't care for me any more like you did and\n"
            "    that you are wishing things could be different. And yet, what am\n"
            "    I to do? I know you'll say that it has all been as much my fault\n"
            "    as yours. And the world, if it knew, might think so, too. But how\n"
            "    often did I beg you not to make me do what I did not want to do,\n"
            "    and which I was afraid even then I would regret, although I loved\n"
            "    you too much to let you go, if you still insisted on having your\n"
            "    way.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.that" not in full_text

    def test_wrap_034_last_year(self):
        # Source: An American Tragedy V 2, wrap corruption: last.year
        passage = (
            "\"Oh, Clyde, Clyde, life is so different to-day to what it was last\n"
            "    year. Think--then we were going to Crum and those other lakes over\n"
            "    near Fonda and Gloversville and Little Falls, but now--now. Only\n"
            "    just now some boy and girl friends of Tom's and Emily's came by to\n"
            "    get them to go after strawberries, and when I saw them go and knew\n"
            "    I couldn't, and that I couldn't be like that any more ever, I cried\n"
            "    and cried, ever so long.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "last.year" not in full_text

    def test_wrap_035_lovingkind_according(self):
        # Source: An American Tragedy V 2, wrap corruption: lovingkindness.according
        passage = (
            "\"Have mercy upon me, O God, according to thy loving-kindness;\n"
            "    according unto the multitude of thy tender mercies, blot out my\n"
            "    transgressions.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lovingkindness.according" not in full_text

    def test_wrap_036_thy_sight(self):
        # Source: An American Tragedy V 2, wrap corruption: thy.sight
        passage = (
            "\"Against Thee, Thee only have I sinned, and done this evil in thy\n"
            "    sight, that Thou mightest be justified when Thou speakest and be\n"
            "    clear when Thou judgest.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thy.sight" not in full_text

    def test_wrap_037_and_pleasure(self):
        # Source: An American Tragedy V 2, wrap corruption: and.pleasure
        passage = (
            "If the young men of this country could only know the joy and\n"
            "    pleasure of a Christian life, I know they would do all in their\n"
            "    power to become earnest, active Christians, and would strive to\n"
            "    live as Christ would have them live."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.pleasure" not in full_text

    def test_wrap_038_from_facing(self):
        # Source: An American Tragedy V 2, wrap corruption: from.facing
        passage = (
            "There is not one thing I have left undone which will bar me from\n"
            "    facing my God, knowing that my sins are forgiven, for I have been\n"
            "    free and frank in my talks with my spiritual adviser, and God knows\n"
            "    where I stand."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "from.facing" not in full_text

    def test_wrap_039_was_just(self):
        # Source: Chains B Lesser Novels and Stories, wrap corruption: was.just
        passage = (
            "“_This is me, Mersereau, come back at last to get you! Pringle was\n"
            " just an excuse of mine to let you know I was coming, and so was that\n"
            " hand in that old house, in Issaqueena County. It was mine! I will be\n"
            " with you from now on. Don’t think I will ever leave you!_”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "was.just" not in full_text

    def test_wrap_040_follow_thee(self):
        # Source: Chains B Lesser Novels and Stories, wrap corruption: follow.thee
        passage = (
            "“O, thou blessed that contains no demon, but a fairy! When I follow\n"
            " thee thou takest me into regions overlooking Paradise. My sorrows are\n"
            " as nothing. My rags are become as robes of silk. My feet are shod, not\n"
            " worn and bleeding. I lift up my head——O Flower of Paradise! O Flower\n"
            " of Paradise!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "follow.thee" not in full_text

    def test_wrap_041_caliph_seeks(self):
        # Source: Chains B Lesser Novels and Stories, wrap corruption: caliph.seeks
        passage = (
            "“‘Know, O Commander of the Faithful, that the one whom the caliph\n"
            " seeks is here among his people free from harm. He respects the will\n"
            " of the caliph and his good intentions, but is restrained by fear. He\n"
            " therefore requests that instead of being commanded to reveal himself\n"
            " the caliph devise a way and appoint a time where in darkness and\n"
            " without danger to himself he may behold the face of the one to whom he\n"
            " is to reveal himself. It must be that none are present to seize him."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "caliph.seeks" not in full_text

    def test_wrap_042_and_think(self):
        # Source: Free and Other Stories, wrap corruption: and.think
        passage = (
            "You don’t want the letters. There are only six of them, anyhow, and\n"
            " think, they’re all I have of you to cheer me on my travels. What good\n"
            " would they be to you--little bits of notes telling me you’re sure to\n"
            " meet me--but me--think of me! If I send them to you, you’ll tear them\n"
            " up, whereas if you leave them with me I can dab them with musk and\n"
            " ambergris and keep them in a little silver box, always beside me."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.think" not in full_text

    def test_wrap_043_are_how(self):
        # Source: Free and Other Stories, wrap corruption: are.how
        passage = (
            "Ah, Shirley dear, you really don’t know how sweet I think you are,\n"
            " how dear! There isn’t a thing we have ever done together that isn’t\n"
            " as clear in my mind as this great big skyscraper over the way here in\n"
            " Pittsburgh, and far more pleasing. In fact, my thoughts of you are the\n"
            " most precious and delicious things I have, Shirley."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "are.how" not in full_text

    def test_wrap_044_because_only(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: because.only
        passage = (
            "“_Faithful monogamy must ever be woman’s standard in love, because\n"
            "     only in its still certainty can she fitly prepare and keep the\n"
            "     place for her child._”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "because.only" not in full_text

    def test_wrap_045_keys_conception(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: keys.conception
        passage = (
            "_What would be the result were we generally to adopt Ellen Key’s\n"
            "     conception of marriage: “Marriage is only moral when it grows from\n"
            "     an inner necessity, and not from outward pressure?”_"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "keys.conception" not in full_text

    def test_wrap_046_true_love(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: true.love
        passage = (
            "_Would a succession of unions, expressing different phases of true\n"
            "     love, be of higher value to the individual soul and to the life of\n"
            "     the race than one unbroken although loveless marriage?_"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "true.love" not in full_text

    def test_wrap_047_successive_marriages(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: successive.marriages
        passage = (
            "_If the answer is Yes, are the children better served by successive\n"
            "     marriages than by a home where parents are held together if not by\n"
            "     love by a sense of duty to their children?_"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "successive.marriages" not in full_text

    def test_wrap_048_hast_done(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: hast.done
        passage = (
            "Jehovah to the Serpent, Genesis iii, 14;15: “_Because thou hast\n"
            "     done this_” (urged Eve to seek wisdom by eating of the Fruit of the\n"
            "     Tree of Knowledge) “_thou art cursed above all cattle, and every\n"
            "     beast of the field; upon thy belly shalt thou go, and dust shalt\n"
            "     thou eat all the days of thy life; and I will put enmity between\n"
            "     thee and the woman, and between thy seed and her seed; it shall\n"
            "     bruise thy head and thou shalt bruise his heel_.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hast.done" not in full_text

    def test_wrap_049_the_fruit(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: the.fruit
        passage = (
            "Jehovah to Eve, for attempting to obtain wisdom via eating the\n"
            "     Fruit of the Tree, Genesis iv, 16: “_I will greatly multiply thy\n"
            "     sorrow and thy conception; in sorrow shalt thou bring forth\n"
            "     children; and thy desire shall be to thy husband and he shall rule\n"
            "     over thee_.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.fruit" not in full_text

    def test_wrap_050_eve_because(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: eve.because
        passage = (
            "Jehovah to Adam, because of his following the advice of Eve:\n"
            "     “_Because thou hast hearkened unto the voice of thy wife and hast\n"
            "     eaten of the Tree, cursed is the ground for thy sake; in sorrow\n"
            "     shalt thou eat of it all the days of thy life; thorns and thistles\n"
            "     shall it bring forth to thee, and thou shalt eat the herb of the\n"
            "     field. In the sweat of thy face shalt thou eat bread till thou\n"
            "     return unto the ground._”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "eve.because" not in full_text

    def test_wrap_051_plain_upon(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: plain.upon
        passage = (
            "He is! He is! It is so plain\n"
            "    Upon His Throne He doth remain!\n"
            "    By day or night, in dark or light,\n"
            "    We feel His presence shining bright!\n"
            "        All’s well with the world!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "plain.upon" not in full_text

    def test_wrap_052_behold_the(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: behold.the
        passage = (
            "’Tis now that we with joy behold\n"
            "    The earth of virtue yield fourfold\n"
            "    Of truth and right the crop is great--\n"
            "    Indeed, enough the world to sate!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "behold.the" not in full_text

    def test_wrap_053_least_since(self):
        # Source: Hey Rub a Dub Dub a Book of the Mystery and Wonder and Terror of Life, wrap corruption: least.since
        passage = (
            "’Tis six full centuries at least\n"
            "    Since un-Eugenic weddings ceased;\n"
            "    And now each youth and maid you see\n"
            "    Is married full Eugenic-ly.\n"
            "    In us behold the perfect fruitage\n"
            "    That followed on the former brute-age!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "least.since" not in full_text

    def test_wrap_054_wait_until(self):
        # Source: Sister Carrie a Novel, wrap corruption: wait.until
        passage = (
            "“Dear Sir: We beg to inform you that we are instructed to wait\n"
            "     until to-morrow (Thursday) at one o’clock, before filing suit\n"
            "     against you, on behalf of Mrs. Julia Hurstwood, for divorce and\n"
            "     alimony. If we do not hear from you before that time we shall\n"
            "     consider that you do not wish to compromise the matter in any way\n"
            "     and act accordingly."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "wait.until" not in full_text

    def test_wrap_055_she_wrote(self):
        # Source: Sister Carrie a Novel, wrap corruption: she.wrote
        passage = (
            "“You do not need to have me explain why I did not meet you,” she\n"
            "     wrote in part. “How could you deceive me so? You cannot expect me\n"
            "     to have anything more to do with you. I wouldn’t under any\n"
            "     circumstances. Oh, how could you act so?” she added in a burst of\n"
            "     feeling. “You have caused me more misery than you can think. I\n"
            "     hope you will get over your infatuation for me. We must not meet\n"
            "     any more. Good-bye.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "she.wrote" not in full_text

