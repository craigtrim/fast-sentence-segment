import pytest
from fast_sentence_segment import segment_text


class TestEbooksChesterton:
    """Integration tests mined from G K Chesterton ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1910s
    """

    def test_wrap_001_white_and(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: white.and
        passage = (
            "The world grows terrible and white,\n"
            "      And blinding white the breaking day,\n"
            "    We walk bewildered in the light,\n"
            "    For something is too large for sight,\n"
            "      And something much too plain to say."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "white.and" not in full_text

    def test_wrap_002_fed_the(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: fed.the
        passage = (
            "The house from which the heavens are fed,\n"
            "      The old strange house that is our own,\n"
            "    Where tricks of words are never said,\n"
            "    And Mercy is as plain as bread,\n"
            "      And Honour is as hard as stone."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fed.the" not in full_text

    def test_wrap_003_mystery_whatever(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: mystery.whatever
        passage = (
            "Mother of God's good witches, of all white mystery,\n"
            "  Whatever else I am seeking, I seek for thee.\n"
            "  For the old harp better fitted and swung on a stronger thong,\n"
            "  We, that shall sing for ever; O hear our song!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mystery.whatever" not in full_text

    def test_wrap_004_grew_like(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: grew.like
        passage = (
            "Fearfully plain the flowers grew,\n"
            "        Like a child's book to read,\n"
            "      Or like a friend's face seen in a glass.\n"
            "    He looked, and there Our Lady was;\n"
            "    She stood and stroked the tall live grass\n"
            "      As a man strokes his steed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "grew.like" not in full_text

    def test_wrap_005_state_straight(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: state.straight
        passage = (
            "I see you how you smile in state\n"
            "      Straight from the Peak to Plymouth Bar;\n"
            "    You need not tell me you are great,\n"
            "      I know how more than great you are.\n"
            "    I know what spirit Chaucer was;\n"
            "    I have seen Gainsborough and the grass."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "state.straight" not in full_text

    def test_wrap_006_first_our(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: first.our
        passage = (
            "It may be we shall rise the last as Frenchmen rose the first;\n"
            "  Our wrath come after Russia's, and our wrath be the worst.\n"
            "  It may be we are set to mark by our riot and our rest\n"
            "  God's scorn of all man's governance: it may be beer is best.\n"
            "  But we are the people of England, and we never have spoken yet.\n"
            "  Mock at us, pay us, pass us; but do not quite forget."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "first.our" not in full_text

    def test_wrap_007_wise_who(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: wise.who
        passage = (
            "Happy is he and more than wise\n"
            "      Who sees with wondering eyes and clean\n"
            "    This world through all the grey disguise\n"
            "      Of sleep and custom in between.\n"
            "    Yes; we may pass the heavenly screen,\n"
            "      But shall we know when we are there?\n"
            "    Who know not what these dead stones mean,\n"
            "      The lovely city of Lierre."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "wise.who" not in full_text

    def test_wrap_008_death_god(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: death.god
        passage = (
            "Lift up your heads: in life, in death,\n"
            "      God knoweth his head was high;\n"
            "    Quit we the coward's broken breath\n"
            "      Who watched a strong man die."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "death.god" not in full_text

    def test_wrap_009_grey_that(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: grey.that
        passage = (
            "My Lady clad herself in grey,\n"
            "      That caught and clung about her throat;\n"
            "    Then all the long grey winter-day\n"
            "      On me a living splendour smote;\n"
            "    And why grey palmers holy are,\n"
            "      And why grey minsters great in story,\n"
            "    And grey skies ring the morning star,\n"
            "      And grey hairs are a crown of glory."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "grey.that" not in full_text

    def test_wrap_010_green_like(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: green.like
        passage = (
            "My Lady clad herself in green,\n"
            "      Like meadows where the wind-waves pass;\n"
            "    Then round my spirit spread, I ween,\n"
            "      A splendour of forgotten grass.\n"
            "    Then all that dropped of stem or sod,\n"
            "      Hoarded as emeralds might be,\n"
            "    I bowed to every bush, and trod\n"
            "      Amid the live grass fearfully."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "green.like" not in full_text

    def test_wrap_011_blue_then(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: blue.then
        passage = (
            "My Lady clad herself in blue,\n"
            "      Then on me, like the seer long gone,\n"
            "    The likeness of a sapphire grew,\n"
            "      The throne of him that sat thereon.\n"
            "    Then knew I why the Fashioner\n"
            "      Splashed reckless blue on sky and sea;\n"
            "    And ere 'twas good enough for her,\n"
            "      He tried it on Eternity."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "blue.then" not in full_text

    def test_wrap_012_knowledget_sat(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: knowledgetree.sat
        passage = (
            "Beneath the gnarled old Knowledge-tree\n"
            "      Sat, like an owl, the evil sage:\n"
            "    'The world's a bubble,' solemnly\n"
            "      He read, and turned a second page.\n"
            "    'A bubble, then, old crow,' I cried,\n"
            "      'God keep you in your weary wit!\n"
            "    A bubble--have you ever spied\n"
            "      The colours I have seen on it?'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "knowledgetree.sat" not in full_text

    def test_wrap_013_waterfly_are(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: waterfly.are
        passage = (
            "Chattering finch and water-fly\n"
            "    Are not merrier than I;\n"
            "    Here among the flowers I lie\n"
            "    Laughing everlastingly.\n"
            "    No: I may not tell the best;\n"
            "    Surely, friends, I might have guessed\n"
            "    Death was but the good King's jest,\n"
            "    It was hid so carefully."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "waterfly.are" not in full_text

    def test_wrap_014_gonfalon_the(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: gonfalon.the
        passage = (
            "Gored on the Norman gonfalon\n"
            "    The Golden Dragon died,\n"
            "      We shall not wake with ballad strings\n"
            "    The good time of the smaller things,\n"
            "    We shall not see the holy kings\n"
            "      Ride down the Severn side."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gonfalon.the" not in full_text

    def test_wrap_015_afar_these(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: afar.these
        passage = (
            "Likelier across these flats afar,\n"
            "      These sulky levels smooth and free,\n"
            "    The drums shall crash a waltz of war\n"
            "      And Death shall dance with Liberty;\n"
            "    Likelier the barricades shall blare\n"
            "      Slaughter below and smoke above,\n"
            "    And death and hate and hell declare\n"
            "      That men have found a thing to love."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "afar.these" not in full_text

    def test_wrap_016_forth_out(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: forth.out
        passage = (
            "There fared a mother driven forth\n"
            "    Out of an inn to roam;\n"
            "    In the place where she was homeless\n"
            "    All men are at home.\n"
            "    The crazy stable close at hand,\n"
            "    With shaking timber and shifting sand,\n"
            "    Grew a stronger thing to abide and stand\n"
            "    Than the square stones of Rome."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "forth.out" not in full_text

    def test_wrap_017_homes_and(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: homes.and
        passage = (
            "For men are homesick in their homes,\n"
            "    And strangers under the sun,\n"
            "    And they lay their heads in a foreign land\n"
            "    Whenever the day is done.\n"
            "    Here we have battle and blazing eyes,\n"
            "    And chance and honour and high surprise,\n"
            "    But our homes are under miraculous skies\n"
            "    Where the Yule tale was begun."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "homes.and" not in full_text

    def test_wrap_018_stable_where(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: stable.where
        passage = (
            "A Child in a foul stable,\n"
            "    Where the beasts feed and foam,\n"
            "    Only where He was homeless\n"
            "    Are you and I at home:\n"
            "    We have hands that fashion and heads that know,\n"
            "    But our hearts we lost--how long ago!\n"
            "    In a place no chart nor ship can show\n"
            "    Under the sky's dome."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "stable.where" not in full_text

    def test_wrap_019_tale_and(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: tale.and
        passage = (
            "This world is wild as an old wives' tale,\n"
            "    And strange the plain things are,\n"
            "    The earth is enough and the air is enough\n"
            "    For our wonder and our war;\n"
            "    But our rest is as far as the fire-drake swings\n"
            "    And our peace is put in impossible things\n"
            "    Where clashed and thundered unthinkable wings\n"
            "    Round an incredible star."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tale.and" not in full_text

    def test_wrap_020_evening_home(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: evening.home
        passage = (
            "To an open house in the evening\n"
            "    Home shall all men come,\n"
            "    To an older place than Eden\n"
            "    And a taller town than Rome.\n"
            "    To the end of the way of the wandering star,\n"
            "    To the things that cannot be and that are,\n"
            "    To the place where God was homeless\n"
            "    And all men are at home."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "evening.home" not in full_text

    def test_wrap_021_prayers_say(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: prayers.say
        passage = (
            "People, if you have any prayers,\n"
            "  Say prayers for me;\n"
            "  And lay me under a Christian stone\n"
            "  In this lost land I thought my own,\n"
            "  To wait till the holy horn be blown\n"
            "  And all poor men are free."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "prayers.say" not in full_text

    def test_wrap_022_ages_because(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: ages.because
        passage = (
            "Why should I care for the Ages\n"
            "      Because they are old and grey?\n"
            "    To me like sudden laughter\n"
            "      The stars are fresh and gay;\n"
            "    The world is a daring fancy\n"
            "      And finished yesterday."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ages.because" not in full_text

    def test_wrap_023_systems_solid(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: systems.solid
        passage = (
            "The eternal suns and systems,\n"
            "      Solid and silent all,\n"
            "    To me are stars of an instant,\n"
            "      Only the fires that fall\n"
            "    From God's good rocket rising\n"
            "      On this night of carnival."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "systems.solid" not in full_text

    def test_wrap_024_golgotha_slain(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: golgotha.slain
        passage = (
            "Wherefore was God in Golgotha\n"
            "    Slain as a serf is slain;\n"
            "    And hate He had of prince and peer,\n"
            "    And love He had and made good cheer,\n"
            "    Of them that, like this woman here,\n"
            "    Go powerfully in pain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "golgotha.slain" not in full_text

    def test_wrap_025_gone_behind(self):
        # Source: A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro, wrap corruption: gone.behind
        passage = (
            "The meanest man in grey fields gone\n"
            "    Behind the set of sun,\n"
            "    Heareth between star and other star,\n"
            "    Through the door of the darkness fallen ajar,\n"
            "    The Council eldest of things that are,\n"
            "    The talk of the Three in One."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gone.behind" not in full_text

    def test_wrap_026_hour_and(self):
        # Source: A Miscellany of Men, wrap corruption: hour.and
        passage = (
            "Stilton, thou shouldst be living at this hour\n"
            "     And so thou art.  Nor losest grace thereby;\n"
            "     England has need of thee, and so have I--\n"
            "     She is a Fen.  Far as the eye can scour,\n"
            "     League after grassy league from Lincoln tower\n"
            "     To Stilton in the fields, she is a Fen.\n"
            "     Yet this high cheese, by choice of fenland men,\n"
            "     Like a tall green volcano rose in power."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hour.and" not in full_text

    def test_wrap_027_more_and(self):
        # Source: A Miscellany of Men, wrap corruption: more.and
        passage = (
            "Plain living and long drinking are no more,\n"
            "     And pure religion reading 'Household Words',\n"
            "     And sturdy manhood sitting still all day\n"
            "     Shrink, like this cheese that crumbles to its core;\n"
            "     While my digestion, like the House of Lords,\n"
            "     The heaviest burdens on herself doth lay."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "more.and" not in full_text

    def test_wrap_028_stoves_forbode(self):
        # Source: Alarms and Discursions, wrap corruption: stoves.forbode
        passage = (
            "“'Therefore, ye gas-pipes, ye asbestos? stoves,\n"
            "  Forbode not any severing of our loves.\n"
            "  I have relinquished but your earthly sight,\n"
            "  To hold you dear in a more distant way.\n"
            "  I'll love the 'buses lumbering through the wet,\n"
            "  Even more than when I lightly tripped as they.\n"
            "  The grimy colour of the London clay\n"
            "  Is lovely yet,'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "stoves.forbode" not in full_text

    def test_wrap_029_plagued_the(self):
        # Source: Alarms and Discursions, wrap corruption: plagued.the
        passage = (
            "“Or didst thou love the God of Flies who plagued\n"
            "  the Hebrews and was splashed\n"
            "  With wine unto the waist, or Pasht who had green\n"
            "  beryls for her eyes?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "plagued.the" not in full_text

    def test_wrap_030_bright_that(self):
        # Source: Alarms and Discursions, wrap corruption: bright.that
        passage = (
            "A notion came into my head as new as it was bright\n"
            "  That poems might be written on the subject of a fight;\n"
            "  No praise was given to Lancelot, Achilles, Nap or Corbett,\n"
            "  But we will sing the praises of man holding the flywheel of which the ideal\n"
            "steering-post traverses the earth impelled itself around the circuit of\n"
            "its own orbit."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bright.that" not in full_text

    def test_wrap_031_far_but(self):
        # Source: Alarms and Discursions, wrap corruption: far.but
        passage = (
            "My fathers scaled the mountains in their pilgrimages far,\n"
            "  But I feel full of energy while sitting in a car;\n"
            "  And petrol is the perfect wine, I lick it and absorb it,\n"
            "  So we will sing the praises of man holding the flywheel of which the ideal\n"
            "steering-post traverses the earth impelled itself around the circuit of\n"
            "its own orbit."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "far.but" not in full_text

    def test_wrap_032_altogether_keep(self):
        # Source: Appreciations and Criticisms of the Works of Charles Dickens, wrap corruption: altogether.keep
        passage = (
            "\"'Susan,' I says, 'you've been a wery good vife to me altogether:\n"
            "     keep a good heart, my dear, and you'll live to see me punch that\n"
            "     'ere Stiggins's 'ead yet.' She smiled at this, Samivel ... but she\n"
            "     died arter all.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "altogether.keep" not in full_text

    def test_wrap_033_waterworks_for(self):
        # Source: Eugenics and Other Evils, wrap corruption: waterworks.for
        passage = (
            "\"Father's got the sack from the water-works\n"
            "      For smoking of his old cherry-briar;\n"
            "    Father's got the sack from the water-works\n"
            "      'Cos he might set the water-works on fire.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "waterworks.for" not in full_text

    def test_wrap_034_hollyer_permanent(self):
        # Source: G F Watts, wrap corruption: hollyer.permanent
        passage = (
            "_The Photogravures are from photographs by Fredk. Hollyer.\n"
            "     Permanent photographs of works of Watts, Rossetti, Burne-Jones,\n"
            "     Holbein, and of pictures in the Dublin and Hague Galleries can be\n"
            "     obtained of Fredk. Hollyer, 9 Pembroke Square, Kensington._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hollyer.permanent" not in full_text

    def test_wrap_035_noes_but(self):
        # Source: Heretics, wrap corruption: noes.but
        passage = (
            "“The ball no question makes of Ayes or Noes,\n"
            "   But Here or There as strikes the Player goes;\n"
            "   And He that tossed you down into the field,\n"
            "   He knows about it all—he knows—he knows.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "noes.but" not in full_text

    def test_wrap_036_rainy_twilight(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: rainy.twilight
        passage = (
            "SCENE: _A plantation of thin young trees, in a misty and rainy\n"
            "     twilight; some woodland blossom showing the patches on the earth\n"
            "     between the stems._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rainy.twilight" not in full_text

    def test_wrap_037_hood_his(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: hood.his
        passage = (
            "THE STRANGER _is discovered, a cloaked figure with a pointed hood.\n"
            "     His costume might belong to modern or any other time, and the\n"
            "     conical hood is so drawn over the head that little can be seen of\n"
            "     the face._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hood.his" not in full_text

    def test_wrap_038_morris_carleon(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: morris.carleon
        passage = (
            "[MR. HASTINGS goes out into the garden. He returns with MORRIS\n"
            "     CARLEON, _a very young man: hardly more than a boy, but with very\n"
            "     grown-up American dress and manners. He is dark, smallish, and\n"
            "     active; and the racial type under his Americanism is Irish._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "morris.carleon" not in full_text

    def test_wrap_039_and_unintellig(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: and.unintelligible
        passage = (
            "[_She goes out into the garden and calls out some half-chanted and\n"
            "     unintelligible words, somewhat like the song preceding her\n"
            "     entrance. The red light reappears; and there is a slight sound as\n"
            "     of fallen leaves shuffled by approaching feet. The cloaked_\n"
            "     STRANGER _with the pointed hood is seen standing outside the garden\n"
            "     doors._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.unintelligible" not in full_text

    def test_wrap_040_the_evening(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: the.evening
        passage = (
            "_The same room lighted more brilliantly an hour later in the\n"
            "     evening. On one side a table covered with packs of cards, pyramids,\n"
            "     etc., at which the_ CONJURER _in evening dress is standing quietly\n"
            "     setting out his tricks. A little more in the foreground the_ DUKE;\n"
            "     and HASTINGS with a number of papers."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.evening" not in full_text

    def test_wrap_041_conjurer_who(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: conjurer.who
        passage = (
            "[She puts her hand on the handle of the door, but the CONJURER,\n"
            "     _who is sitting on the table and staring at his boots, does not\n"
            "     notice the action, and goes on as in a sincere soliloquy._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "conjurer.who" not in full_text

    def test_wrap_042_the_conjuringt(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: the.conjuringtable
        passage = (
            "[Enter MORRIS, _in evening-dress. He walks straight up to the\n"
            "     conjuring-table; and picks up one article after another, putting\n"
            "     each down with a comment._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.conjuringtable" not in full_text

    def test_wrap_043_empty_chair(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: empty.chair
        passage = (
            "_Room partly darkened, a table with a lamp on it, and an empty\n"
            "     chair. From room next door faint and occasional sounds of the\n"
            "     tossing or talking of the invalid._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "empty.chair" not in full_text

    def test_wrap_044_rev_smith(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: rev.smith
        passage = (
            "[The DUKE and DOCTOR stare at him motionless; but the REV.\n"
            "     SMITH starts and takes a step nearer the table. The CONJURER\n"
            "     _pulls his cloak round his shoulders. This gesture, as of\n"
            "     departure, brings the_ DOCTOR to his feet."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rev.smith" not in full_text

    def test_wrap_045_has_done(self):
        # Source: Magic a Fantastic Comedy, wrap corruption: has.done
        passage = (
            "[Exit into garden. He paces up and down exactly as MORRIS _has\n"
            "     done. As he does so_, PATRICIA _slowly goes out; and a long silence\n"
            "     follows, during which the remaining men stir and stamp very\n"
            "     restlessly. The darkness increases. It is long before anyone\n"
            "     speaks._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "has.done" not in full_text

    def test_wrap_046_glitters_tree(self):
        # Source: Manalive, wrap corruption: glitters.tree
        passage = (
            "“All is gold that glitters—\n"
            "    Tree and tower of brass;\n"
            "Rolls the golden evening air\n"
            "    Down the golden grass.\n"
            "Kick the cry to Jericho,\n"
            "    How yellow mud is sold;\n"
            "All is gold that glitters,\n"
            "    For the glitter is the gold.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "glitters.tree" not in full_text

    def test_wrap_047_life_with(self):
        # Source: Orthodoxy, wrap corruption: life.with
        passage = (
            "\"Enough we live:--and if a life,\n"
            "    With large results so little rife,\n"
            "    Though bearable, seem hardly worth\n"
            "    This pomp of worlds, this pain of birth.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "life.with" not in full_text

    def test_wrap_048_now_looking(self):
        # Source: Orthodoxy, wrap corruption: now.looking
        passage = (
            "\"What doest thou now\n"
            "    Looking Godward to cry\n"
            "    I am I, thou art thou,\n"
            "    I am low, thou art high,\n"
            "    I am thou that thou seekest to find him, find thou\n"
            "        but thyself, thou art I.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "now.looking" not in full_text

    def test_wrap_049_place_god(self):
        # Source: Poems, wrap corruption: place.god
        passage = (
            "For every tiny town or place\n"
            "       God made the stars especially;\n"
            "     Babies look up with owlish face\n"
            "       And see them tangled in a tree:\n"
            "     You saw a moon from Sussex Downs,\n"
            "       A Sussex moon, untravelled still,\n"
            "     I saw a moon that was the town's,\n"
            "       The largest lamp on Campden Hill."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "place.god" not in full_text

    def test_wrap_050_home_the(self):
        # Source: Poems, wrap corruption: home.the
        passage = (
            "Yea, Heaven is everywhere at home.\n"
            "       The big blue cap that always fits,\n"
            "     And so it is (be calm; they come\n"
            "       To goal at last, my wandering wits),\n"
            "     So it is with the heroic thing;\n"
            "       This shall not end for the world's end,\n"
            "     And though the sullen engines swing,\n"
            "       Be you not much afraid, my friend."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "home.the" not in full_text

    def test_wrap_051_urn_where(self):
        # Source: Poems, wrap corruption: urn.where
        passage = (
            "This did not end by Nelson's urn\n"
            "       Where an immortal England sits--\n"
            "     Nor where your tall young men in turn\n"
            "       Drank death like wine at Austerlitz.\n"
            "     And when the pedants bade us mark\n"
            "       What cold mechanic happenings\n"
            "     Must come; our souls said in the dark,\n"
            "       \"Belike; but there are likelier things.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "urn.where" not in full_text

    def test_wrap_052_rhyme_rubbed(self):
        # Source: Poems, wrap corruption: rhyme.rubbed
        passage = (
            "Words, for alas my trade is words, a barren burst of rhyme,\n"
            "       Rubbed by a hundred rhymesters, battered a thousand times,\n"
            "     Take them, you, that smile on strings, those nobler sounds than mine,\n"
            "       The words that never lie, or brag, or flatter, or malign."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rhyme.rubbed" not in full_text

    def test_wrap_053_ours_old(self):
        # Source: Poems, wrap corruption: ours.old
        passage = (
            "In the calm of the last white winter, when all the past is ours,\n"
            "       Old tears are frozen as jewels, old storms frosted as flowers.\n"
            "     Dear Lady, may we meet again, stand up again, we four,\n"
            "       Beneath the burden of the years, and praise the earth once more."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ours.old" not in full_text

    def test_wrap_054_heard_where(self):
        # Source: Poems, wrap corruption: heard.where
        passage = (
            "Dim drums throbbing, in the hills half heard,\n"
            "     Where only on a nameless throne a crownless prince has stirred,\n"
            "     Where, risen from a doubtful seat and half attainted stall,\n"
            "     The last knight of Europe takes weapons from the wall,\n"
            "     The last and lingering troubadour to whom the bird has sung,\n"
            "     That once went singing southward when all the world was young.\n"
            "     In that enormous silence, tiny and unafraid,\n"
            "     Comes up along a winding road the noise of the Crusade."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "heard.where" not in full_text

    def test_wrap_055_sheath_don(self):
        # Source: Poems, wrap corruption: sheath.don
        passage = (
            "Cervantes on his galley sets the sword back in the sheath\n"
            "     (Don John of Austria rides homeward with a wreath.)\n"
            "     And he sees across a weary land a straggling road in Spain,\n"
            "     Up which a lean and foolish knight for ever rides in vain,\n"
            "     And he smiles, but not as Sultans smile, and settles back the blade....\n"
            "     (But Don John of Austria rides home from the Crusade.)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sheath.don" not in full_text

