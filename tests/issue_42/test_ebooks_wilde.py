import pytest
from fast_sentence_segment import segment_text


class TestEbooksWilde:
    """Integration tests mined from Oscar Wilde ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1890s
    """

    def test_wrap_001_art_rare(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: art.rare
        passage = (
            "'Mid France's miracles of art,\n"
            "       Rare trophies won from art's own land,\n"
            "    I've lived to see with burning heart\n"
            "       The fog-bred poor triumphant stand,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "art.rare" not in full_text

    def test_wrap_002_victoire_brillaient(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: victoire.brillaient
        passage = (
            "Dans nos palais, ou, pres de la victoire,\n"
            "    Brillaient les arts, doux fruits des beaux climats,\n"
            "    J'ai vu du Nord les peuplades sans gloire,\n"
            "    De leurs manteaux secouer les frimas."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "victoire.brillaient" not in full_text

    def test_wrap_003_role_our(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: role.our
        passage = (
            "Whom have we here in conqueror's role?\n"
            "    Our grand old marquis, bless his soul!\n"
            "    Whose grand old charger (mark his bone!)\n"
            "    Has borne him back to claim his own.\n"
            "    Note, if you please, the grand old style\n"
            "    In which he nears his grand old pile;\n"
            "    With what an air of grand old state\n"
            "    He waves that blade immaculate!\n"
            "       Hats off, hats off, for my lord to pass,\n"
            "       The grand old Marquis of Carabas!--"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "role.our" not in full_text

    def test_wrap_004_dew_and(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: dew.and
        passage = (
            "If thou wilt be the falling dew\n"
            "       And fall on me alway,\n"
            "    Then I will be the white, white rose\n"
            "       On yonder thorny spray.\n"
            "    If thou wilt be the white, white rose\n"
            "       On yonder thorny spray,\n"
            "    Then I will be the honey-bee\n"
            "       And kiss thee all the day."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dew.and" not in full_text

    def test_wrap_005_honeybee_and(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: honeybee.and
        passage = (
            "If thou wilt be the honey-bee\n"
            "       And kiss me all the day,\n"
            "    Then I will be in yonder heaven\n"
            "       The star of brightest ray.\n"
            "    If thou wilt be in yonder heaven\n"
            "       The star of brightest ray,\n"
            "    Then I will be the dawn, and we\n"
            "       Shall meet at break of day."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "honeybee.and" not in full_text

    def test_wrap_006_lade_silk(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: lade.silk
        passage = (
            "Gold and pearls my vessel lade,\n"
            "       Silk and cloth the cargo be,\n"
            "    All the sails are of brocade\n"
            "       Coming from beyond the sea;\n"
            "    And the helm of finest gold,\n"
            "    Made a wonder to behold.\n"
            "       Fast awhile in slumber lie;\n"
            "       Sleep, my child, and hushaby."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lade.silk" not in full_text

    def test_wrap_007_soon_you(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: soon.you
        passage = (
            "After you were born full soon,\n"
            "       You were christened all aright;\n"
            "    Godmother she was the moon,\n"
            "       Godfather the sun so bright.\n"
            "    All the stars in heaven told\n"
            "    Wore their necklaces of gold.\n"
            "       Fast awhile in slumber lie;\n"
            "       Sleep, my child, and hushaby."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "soon.you" not in full_text

    def test_wrap_008_hour_mothers(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: hour.mothers
        passage = (
            "Sleep, my daughter, sleep an hour;\n"
            "    Mother's darling gilliflower.\n"
            "    Mother rocks thee, standing near,\n"
            "    She will wash thee in the clear\n"
            "    Waters that from fountains run,\n"
            "    To protect thee from the sun."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hour.mothers" not in full_text

    def test_wrap_009_hour_grow(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: hour.grow
        passage = (
            "Sleep, my darling, sleep an hour,\n"
            "    Grow thou as the gilliflower.\n"
            "    As a tear-drop be thou white,\n"
            "    As a willow tall and slight;\n"
            "    Gentle as the ring-doves are,\n"
            "    And be lovely as a star!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hour.grow" not in full_text

    def test_wrap_010_first_were(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: first.were
        passage = (
            "They disputed all day over the conditions I had made.  The two first\n"
            "    were granted me, but all that could be obtained with respect to the\n"
            "    third was, that the Empress would use quite a small armchair, whilst\n"
            "    she gave me a chair."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "first.were" not in full_text

    def test_wrap_011_somerville_acquaintan(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: somervilles.acquaintance
        passage = (
            "A very amusing circumstance in connection with Mrs. Somerville's\n"
            "    acquaintance with Sir Walter arose out of the childish\n"
            "    inquisitiveness of Woronzow Greig, Mrs. Somerville's little boy."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "somervilles.acquaintance" not in full_text

    def test_wrap_012_that_this(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: that.this
        passage = (
            "The history of Joseph: they all found a difficulty in realizing that\n"
            "    this had actually occurred.  One asked if Egypt existed now, and if\n"
            "    people lived in it.  When I told them that buildings now stood which\n"
            "    had been erected about the time of Joseph, one said that it was\n"
            "    impossible, as they must have fallen down ere this.  I showed them\n"
            "    the form of a pyramid, and they were satisfied.  One asked if all\n"
            "    books were true."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.this" not in full_text

    def test_wrap_013_dear_beauty(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: dear.beauty
        passage = (
            "'Art should aspire, yet ugliness be dear;\n"
            "    Beauty, the shaft, should speed with wit for feather;\n"
            "    And love, sweet love, should never fall to sere,\n"
            "             If I were king.'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dear.beauty" not in full_text

    def test_wrap_014_glistening_dripped(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: glistening.dripped
        passage = (
            "As with varnish red and glistening\n"
            "       Dripped his hair; his feet were rigid;\n"
            "       Raised, he settled stiffly sideways:\n"
            "       You could see the hurts were spinal."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "glistening.dripped" not in full_text

    def test_wrap_015_engine_and(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: engine.and
        passage = (
            "He had fallen from an engine,\n"
            "       And been dragged along the metals.\n"
            "       It was hopeless, and they knew it;\n"
            "       So they covered him, and left him."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "engine.and" not in full_text

    def test_wrap_016_sentient_inarticula(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: sentient.inarticulately
        passage = (
            "As he lay, by fits half sentient,\n"
            "       Inarticulately moaning,\n"
            "       With his stockinged feet protruded\n"
            "       Sharp and awkward from the blankets,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sentient.inarticulately" not in full_text

    def test_wrap_017_woman_stood(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: woman.stood
        passage = (
            "To his bed there came a woman,\n"
            "       Stood and looked and sighed a little,\n"
            "       And departed without speaking,\n"
            "       As himself a few hours after."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "woman.stood" not in full_text

    def test_wrap_018_sweetheart_they(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: sweetheart.they
        passage = (
            "I was told she was his sweetheart.\n"
            "       They were on the eve of marriage.\n"
            "       She was quiet as a statue,\n"
            "       But her lip was gray and writhen."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sweetheart.they" not in full_text

    def test_wrap_019_see_case(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: see.case
        passage = (
            "Now one can see.\n"
            "    Case Number One\n"
            "    Sits (rather pale) with his bedclothes\n"
            "    Stripped up, and showing his foot\n"
            "    (Alas, for God's image!)\n"
            "    Swaddled in wet white lint\n"
            "    Brilliantly hideous with red."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "see.case" not in full_text

    def test_wrap_020_renowned_twosworded(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: renowned.twosworded
        passage = (
            "Was I a Samurai renowned,\n"
            "    Two-sworded, fierce, immense of bow?\n"
            "    A histrion angular and profound?\n"
            "    A priest? a porter?--Child, although\n"
            "    I have forgotten clean, I know\n"
            "    That in the shade of Fujisan,\n"
            "    What time the cherry-orchards blow,\n"
            "    I loved you once in old Japan."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "renowned.twosworded" not in full_text

    def test_wrap_021_flowinggow_and(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: flowinggowned.and
        passage = (
            "As here you loiter, flowing-gowned\n"
            "    And hugely sashed, with pins a-row\n"
            "    Your quaint head as with flamelets crowned,\n"
            "    Demure, inviting--even so,\n"
            "    When merry maids in Miyako\n"
            "    To feel the sweet o' the year began,\n"
            "    And green gardens to overflow,\n"
            "    I loved you once in old Japan."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "flowinggowned.and" not in full_text

    def test_wrap_022_round_two(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: round.two
        passage = (
            "Clear shine the hills; the rice-fields round\n"
            "    Two cranes are circling; sleepy and slow,\n"
            "    A blue canal the lake's blue bound\n"
            "    Breaks at the bamboo bridge; and lo!\n"
            "    Touched with the sundown's spirit and glow,\n"
            "    I see you turn, with flirted fan,\n"
            "    Against the plum-tree's bloomy snow . . .\n"
            "    I loved you once in old Japan!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "round.two" not in full_text

    def test_wrap_023_may_fresh(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: may.fresh
        passage = (
            "We'll to the woods and gather may\n"
            "    Fresh from the footprints of the rain.\n"
            "    We'll to the woods, at every vein\n"
            "    To drink the spirit of the day."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "may.fresh" not in full_text

    def test_wrap_024_play_the(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: play.the
        passage = (
            "The winds of spring are out at play,\n"
            "    The needs of spring in heart and brain.\n"
            "    We'll to the woods and gather may\n"
            "    Fresh from the footprints of the rain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "play.the" not in full_text

    def test_wrap_025_say_hark(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: say.hark
        passage = (
            "The world's too near her end, you say?\n"
            "    Hark to the blackbird's mad refrain!\n"
            "    It waits for her, the vast Inane?\n"
            "    Then, girls, to help her on the way\n"
            "    We'll to the woods and gather may."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "say.hark" not in full_text

    def test_wrap_026_gate_how(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: gate.how
        passage = (
            "It matters not how strait the gate,\n"
            "       How charged with punishments the scroll,\n"
            "    I am the master of my fate:\n"
            "       I am the captain of my soul."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gate.how" not in full_text

    def test_wrap_027_against_their(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: against.their
        passage = (
            "You are for pressing and urging the people to their profit against\n"
            "    their inclination: so am I.  You set little value upon all merely\n"
            "    technical instruction, upon all that fails to touch the inner nature\n"
            "    of man: so do I.  And here I find ground of union broad and\n"
            "    deep-laid. . . ."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "against.their" not in full_text

    def test_wrap_028_private_circumstan(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: private.circumstances
        passage = (
            "But indeed I am most unfit to pursue the subject; private\n"
            "    circumstances of no common interest are upon me, as I have become\n"
            "    very recently engaged to Miss Glynne, and I hope your recollections\n"
            "    will enable you in some degree to excuse me."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "private.circumstances" not in full_text

    def test_wrap_029_among_thorns(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: among.thorns
        passage = (
            "'St. Anselm was grown old and infirm, and lay on the ground among\n"
            "    thorns and thistles.  Der liebe Gott said to him, \"You are very\n"
            "    badly lodged there; why don't you build yourself a house?\"  \"Before I\n"
            "    take the trouble,\" said Anselm, \"I should like to know how long I\n"
            "    have to live.\"  \"About thirty years,\" said Der liebe Gott.  \"Oh,\n"
            "    for so short a time,\" replied he, \"it's not worth while,\" and turned\n"
            "    himself round among the thistles.'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "among.thorns" not in full_text

    def test_wrap_030_before_voltaire(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: before.voltaire
        passage = (
            "Dr. Franck told me a story of which I had never heard before.\n"
            "    Voltaire had for some reason or other taken a grudge against the\n"
            "    prophet Habakkuk, and affected to find in him things he never wrote.\n"
            "    Somebody took the Bible and began to demonstrate to him that he was\n"
            "    mistaken.  'C'est egal,' he said impatiently, '_Habakkuk etait\n"
            "    capable de tout_!'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "before.voltaire" not in full_text

    def test_wrap_031_tears_touched(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: tears.touched
        passage = (
            "God knows it.  And He knows how the world's tears\n"
            "       Touched me.  And He is witness of my wrath,\n"
            "    How it was kindled against murderers\n"
            "       Who slew for gold, and how upon their path\n"
            "    I met them.  Since which day the World in arms\n"
            "    Strikes at my life with angers and alarms."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tears.touched" not in full_text

    def test_wrap_032_pleasure_and(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: pleasure.and
        passage = (
            "Naked I came into the world of pleasure,\n"
            "       And naked come I to this house of pain.\n"
            "    Here at the gate I lay down my life's treasure,\n"
            "       My pride, my garments and my name with men.\n"
            "       The world and I henceforth shall be as twain,\n"
            "    No sound of me shall pierce for good or ill\n"
            "       These walls of grief.  Nor shall I hear the vain\n"
            "    Laughter and tears of those who love me still."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pleasure.and" not in full_text

    def test_wrap_033_ease_cold(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: ease.cold
        passage = (
            "Within, what new life waits me!  Little ease,\n"
            "       Cold lying, hunger, nights of wakefulness,\n"
            "    Harsh orders given, no voice to soothe or please,\n"
            "       Poor thieves for friends, for books rules meaningless;\n"
            "    This is the grave--nay, hell.  Yet, Lord of Might,\n"
            "    Still in Thy light my spirit shall see light."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ease.cold" not in full_text

    def test_wrap_034_consistent_with(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: consistently.with
        passage = (
            "I round and finish little, if anything; and could not, consistently\n"
            "    with my scheme.  The reader will have his or her part to do, just as\n"
            "    much as I have had mine.  I seek less to state or display any theme\n"
            "    or thought, and more to bring you, reader, into the atmosphere of the\n"
            "    theme or thought--there to pursue your own flight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "consistently.with" not in full_text

    def test_wrap_035_mountain_down(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: mountain.down
        passage = (
            "Up the airy mountain,\n"
            "       Down the rushy glen,\n"
            "    We daren't go a-hunting\n"
            "       For fear of little men;\n"
            "    Wee folk, good folk,\n"
            "       Trooping all together;\n"
            "    Green jacket, red cap,\n"
            "       And white owl's feather!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mountain.down" not in full_text

    def test_wrap_036_shore_some(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: shore.some
        passage = (
            "Down along the rocky shore\n"
            "       Some make their home,\n"
            "    They live on crispy pancakes\n"
            "       Of yellow tide-foam;\n"
            "    Some in the reeds\n"
            "       Of the black mountain lake,\n"
            "    With frogs for their watch-dogs\n"
            "       All night awake."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shore.some" not in full_text

    def test_wrap_037_hilltop_the(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: hilltop.the
        passage = (
            "High on the hill-top\n"
            "       The old King sits;\n"
            "    He is now so old and gray\n"
            "       He's nigh lost his wits.\n"
            "    With a bridge of white mist\n"
            "       Columbkill he crosses,\n"
            "    On his stately journeys\n"
            "       From Slieveleague to Rosses;\n"
            "    Or going up with music,\n"
            "       On cold starry nights,\n"
            "    To sup with the Queen\n"
            "       Of the gay Northern Lights."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hilltop.the" not in full_text

    def test_wrap_038_light_for(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: light.for
        passage = (
            "And the ears of the horse went sinking away in the hollow light,\n"
            "       For, as drift from a sailor slow drowning the gleams of the world\n"
            "    and the sun,\n"
            "    Ceased on our hands and faces, on hazel and oak leaf, the light,\n"
            "       And the stars were blotted above us, and the whole of the world\n"
            "    was one;"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "light.for" not in full_text

    def test_wrap_039_hazel_and(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: hazel.and
        passage = (
            "Till the horse gave a whinny; for cumbrous with stems of the hazel\n"
            "    and oak,\n"
            "       Of hollies, and hazels, and oak-trees, a valley was sloping away\n"
            "    From his hoofs in the heavy grasses, with monstrous slumbering folk,\n"
            "       Their mighty and naked and gleaming bodies heaped loose where they\n"
            "    lay."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hazel.and" not in full_text

    def test_wrap_040_gold_were(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: gold.were
        passage = (
            "More comely than man may make them, inlaid with silver and gold,\n"
            "       Were arrow and shield and war-axe, arrow and spear and blade,\n"
            "    And dew-blanched horns, in whose hollows a child of three years old\n"
            "       Could sleep on a couch of rushes, round and about them laid."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gold.were" not in full_text

    def test_wrap_041_worlds_sat(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: worlds.sat
        passage = (
            "The maker of the stars and worlds\n"
            "       Sat underneath the market cross,\n"
            "    And the old men were walking, walking,\n"
            "       And little boys played pitch-and-toss."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "worlds.sat" not in full_text

    def test_wrap_042_worlds_are(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: worlds.are
        passage = (
            "'The props,' said He, 'of stars and worlds\n"
            "       Are prayers of patient men and good.\n"
            "    The boys, the women, and old men,\n"
            "       Listening, upon their shadows stood."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "worlds.are" not in full_text

    def test_wrap_043_cried_how(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: cried.how
        passage = (
            "A grey professor passing cried,\n"
            "       'How few the mind's intemperance rule!\n"
            "    What shallow thoughts about deep things!\n"
            "       The world grows old and plays the fool.'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "cried.how" not in full_text

    def test_wrap_044_ear_there(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: ear.there
        passage = (
            "The mayor came, leaning his left ear--\n"
            "       There were some talking of the poor--\n"
            "    And to himself cried, 'Communist!'\n"
            "       And hurried to the guardhouse door."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ear.there" not in full_text

    def test_wrap_045_book_whispering(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: book.whispering
        passage = (
            "The bishop came with open book,\n"
            "       Whispering along the sunny path;\n"
            "    There was some talking of man's God,\n"
            "       His God of stupor and of wrath."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "book.whispering" not in full_text

    def test_wrap_046_and_grey(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: and.grey
        passage = (
            "And I rode by the plains of the sea's edge, where all is barren and\n"
            "    grey,\n"
            "       Grey sands on the green of the grasses and over the dripping\n"
            "    trees,\n"
            "    Dripping and doubling landward, as though they would hasten away\n"
            "       Like an army of old men longing for rest from the moan of the\n"
            "    seas."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.grey" not in full_text

    def test_wrap_047_vast_snatching(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: vast.snatching
        passage = (
            "Long fled the foam-flakes around me, the winds fled out of the vast,\n"
            "       Snatching the bird in secret, nor knew I, embosomed apart,\n"
            "    When they froze the cloth on my body like armour riveted fast,\n"
            "       For Remembrance, lifting her leanness, keened in the gates of my\n"
            "    heart."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "vast.snatching" not in full_text

    def test_wrap_048_hay_came(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: hay.came
        passage = (
            "Till fattening the winds of the morning, an odour of new-mown hay\n"
            "       Came, and my forehead fell low, and my tears like berries fell\n"
            "    down;\n"
            "    Later a sound came, half lost in the sound of a shore far away,\n"
            "       From the great grass-barnacle calling, and later the shore-winds\n"
            "    brown."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hay.came" not in full_text

    def test_wrap_049_the_shells(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: the.shells
        passage = (
            "If I were as I once was, the gold hooves crushing the sand and the\n"
            "    shells,\n"
            "       Coming forth from the sea like the morning with red lips murmuring\n"
            "    a song,\n"
            "    Not coughing, my head on my knees, and praying, and wroth with the\n"
            "    bells,\n"
            "       I would leave no Saint's head on his body, though spacious his\n"
            "    lands were and strong."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.shells" not in full_text

    def test_wrap_050_bridlepath_much(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: bridlepath.much
        passage = (
            "Making way from the kindling surges, I rode on a bridle-path,\n"
            "       Much wondering to see upon all hands, of wattle and woodwork made,\n"
            "    Thy bell-mounted churches, and guardless the sacred cairn and the\n"
            "    earth,\n"
            "       And a small and feeble populace stooping with mattock and spade."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bridlepath.much" not in full_text

    def test_wrap_051_their_return(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: their.return
        passage = (
            "There then they fell to feasting, hallowing in the high-tide of their\n"
            "    return with victory in their hands: and the dead corpses of Thiodolf\n"
            "    and Otter, clad in precious glittering raiment, looked down on them\n"
            "    from the High-seat, and the kindreds worshipped them and were glad;\n"
            "    and they drank the Cup to them before any others, were they Gods or\n"
            "    men."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "their.return" not in full_text

    def test_wrap_052_looks_and(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: looks.and
        passage = (
            "And who is he with modest looks,\n"
            "       And clad in sober russet gown?\n"
            "    He murmurs by the running brooks,\n"
            "       A music sweeter than their own;\n"
            "    He is retired as noontide dew,\n"
            "    Or fountain in a noonday grove."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "looks.and" not in full_text

    def test_wrap_053_about_proud(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: about.proud
        passage = (
            "wheeled about,\n"
            "    Proud and exulting like an untired horse\n"
            "    That cares not for his home, and, shod with steel,\n"
            "    Had hissed along the polished ice,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "about.proud" not in full_text

    def test_wrap_054_retired_into(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: retired.into
        passage = (
            "Not seldom from the uproar he retired,\n"
            "    Into a silent bay, or sportively\n"
            "    Glanced sideways, leaving the tumultuous throng\n"
            "    To cut across the reflex of a star,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "retired.into" not in full_text

    def test_wrap_055_seine_and(self):
        # Source: A Critic in Pall Mall Being Extracts From Reviews and Miscellanies, wrap corruption: seine.and
        passage = (
            "O lordly flow the Loire and Seine,\n"
            "       And loud the dark Durance:\n"
            "    But bonnier shine the braes of Tyne\n"
            "       Than a' the fields of France;\n"
            "    And the waves of Till that speak sae still\n"
            "       Gleam goodlier where they glance:"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "seine.and" not in full_text

