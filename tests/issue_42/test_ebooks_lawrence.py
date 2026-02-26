import pytest
from fast_sentence_segment import segment_text


class TestEbooksLawrence:
    """Integration tests mined from D H Lawrence ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1920s
    """

    def test_wrap_001_not_asked(self):
        # Source: Aarons Rod, wrap corruption: not.asked
        passage = (
            "“But look here, Mrs. Houseley, do you really think it makes much\n"
            "difference to a man, whether he can hold a serious conversation or not?”\n"
            " asked the doctor."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "not.asked" not in full_text

    def test_wrap_002_people_made(self):
        # Source: Aarons Rod, wrap corruption: people.made
        passage = (
            "“But what difference does it make,” said Aaron Sisson, “whether they\n"
            "govern themselves or not? They only live till they die, either way.” And\n"
            "he smiled faintly. He had not really listened to the doctor. The terms\n"
            "“British Government,” and “bad for the people--good for the people,”\n"
            " made him malevolently angry."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "people.made" not in full_text

    def test_wrap_003_oak_public(self):
        # Source: Aarons Rod, wrap corruption: oak.public
        passage = (
            "At one end of the dark tree-covered Shottle Lane stood the “Royal Oak”\n"
            " public house; and Mrs. Houseley was certainly an odd woman. At the\n"
            "other end of the lane was Shottle House, where the Bricknells lived; the\n"
            "Bricknells were odd, also. Alfred Bricknell, the old man, was one of the\n"
            "partners in the Colliery firm. His English was incorrect, his accent,\n"
            "broad Derbyshire, and he was not a gentleman in the snobbish sense of\n"
            "the word. Yet he was well-to-do, and very stuck-up. His wife was dead."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "oak.public" not in full_text

    def test_wrap_004_yes_she(self):
        # Source: Aarons Rod, wrap corruption: yes.she
        passage = (
            "“They are, aren't they, Tanny,” repeated Julia softly. “They're\n"
            "old--older than the Old Man of the Seas, sometimes, aren't they?\n"
            "Incredibly old, like little boys who know too much--aren't they? Yes!”\n"
            " She spoke quietly, seriously, as if it had struck her."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "yes.she" not in full_text

    def test_wrap_005_meet_she(self):
        # Source: Aarons Rod, wrap corruption: meet.she
        passage = (
            "“Alas, no, there we aren't,” cried Clariss. She was beautiful too, with\n"
            "her lifted upper-lip. “We both want to be loved, and so we miss each\n"
            "other entirely. We run on in two parallel lines, that can never meet.”\n"
            " She laughed low and half sad."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "meet.she" not in full_text

    def test_wrap_006_goes_and(self):
        # Source: Aarons Rod, wrap corruption: goes.and
        passage = (
            "“And it goes just here--the level of the heart. This is where it goes.”\n"
            " And carefully he pinned the large, radiating ornament on the black\n"
            "velvet dinner-jacket of the old man."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "goes.and" not in full_text

    def test_wrap_007_english_said(self):
        # Source: Aarons Rod, wrap corruption: english.said
        passage = (
            "Angus put in his monocle, and stared at the oblivious shoulders of\n"
            "Aaron, without apparently seeing anything. “Yes. Obviously English,”\n"
            " said Angus, pursing like a bird."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "english.said" not in full_text

    def test_wrap_008_but_said(self):
        # Source: Aarons Rod, wrap corruption: but.said
        passage = (
            "“But,” said Francis in English--none of them had any Italian yet. “But,”\n"
            " said Francis, turning round to Aaron, “that was YOUR SEAT?” and he flung\n"
            "his long fore-finger in the direction of the fat man's thighs."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "but.said" not in full_text

    def test_wrap_009_extra_said(self):
        # Source: Aarons Rod, wrap corruption: extra.said
        passage = (
            "“Oh, never mind. Come along to the first class. I'll pay the difference.\n"
            "We shall be much better all together. Get the luggage down, Francis.\n"
            "It wouldn't be possible to travel with this lot, even if he gave up the\n"
            "seat. There's plenty of room in our carriage--and I'll pay the extra,”\n"
            " said Angus."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "extra.said" not in full_text

    def test_wrap_010_somebody_and(self):
        # Source: Aarons Rod, wrap corruption: somebody.and
        passage = (
            "“Don't you do any such thing, my boy. Make them entertain YOU, for\n"
            "once.--They're always squeezing an entertainment out of somebody--”\n"
            " and Argyle desperately emptied the remains of Algy's wine into his\n"
            "own glass: whilst Algy stood as if listening to something far off, and\n"
            "blinking terribly."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "somebody.and" not in full_text

    def test_wrap_011_morning_said(self):
        # Source: Aarons Rod, wrap corruption: morning.said
        passage = (
            "“I am so anxious that you should come to play one Saturday morning,”\n"
            " said Manfredi. “With an accompaniment, you know. I should like so much\n"
            "to hear you with piano accompaniment.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "morning.said" not in full_text

    def test_wrap_012_pere_vole(self):
        # Source: Aarons Rod, wrap corruption: pere.vole
        passage = (
            "“Derriere chez mon pere\n"
            "                      Vole vole mon coeur, vole!\n"
            "                     Derriere chez mon pere\n"
            "                     Il y a un pommier doux.\n"
            "                       _Tout doux, et iou\n"
            "                        Et iou, tout doux.\n"
            "                        Il y a unpommier doux_."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pere.vole" not in full_text

    def test_wrap_013_princesses_vole(self):
        # Source: Aarons Rod, wrap corruption: princesses.vole
        passage = (
            "Trois belles princesses\n"
            "                      Vole vole mon coeur, vole!\n"
            "                     Trois belles princesses\n"
            "                     Sont assis dessous.\n"
            "                      _Tout doux, et iou\n"
            "                       Et iou, tout doux.\n"
            "                       Sont asses dessous._”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "princesses.vole" not in full_text

    def test_wrap_014_signore_padovano(self):
        # Source: Aarons Rod, wrap corruption: signore.padovano
        passage = (
            "“'Veneziano gran' Signore\n"
            "                     Padovano buon' dotore.\n"
            "                     Vicenzese mangia il gatto\n"
            "                     Veronese tutto matto---'”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "signore.padovano" not in full_text

    def test_wrap_015_sadness_their(self):
        # Source: Amores Poems, wrap corruption: sadness.their
        passage = (
            "THE quick sparks on the gorse bushes are leaping,\n"
            "Little jets of sunlight-texture imitating flame;\n"
            "Above them, exultant, the pee-wits are sweeping:\n"
            "They are lords of the desolate wastes of sadness\n"
            "    their screamings proclaim."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sadness.their" not in full_text

    def test_wrap_016_bitten_down(self):
        # Source: Amores Poems, wrap corruption: bitten.down
        passage = (
            "Rabbits, handfuls of brown earth, lie\n"
            "Low-rounded on the mournful grass they have bitten\n"
            "    down to the quick.\n"
            "Are they asleep?--Are they alive?--Now see,\n"
            "    when I\n"
            "Move my arms the hill bursts and heaves under their\n"
            "    spurting kick."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bitten.down" not in full_text

    def test_wrap_017_the_rushes(self):
        # Source: Amores Poems, wrap corruption: the.rushes
        passage = (
            "The common flaunts bravely; but below, from the\n"
            "    rushes\n"
            "Crowds of glittering king-cups surge to challenge the\n"
            "    blossoming bushes;\n"
            "There the lazy streamlet pushes\n"
            "Its curious course mildly; here it wakes again, leaps,\n"
            "    laughs, and gushes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.rushes" not in full_text

    def test_wrap_018_brook_ebbing(self):
        # Source: Amores Poems, wrap corruption: brook.ebbing
        passage = (
            "Into a deep pond, an old sheep-dip,\n"
            "Dark, overgrown with willows, cool, with the brook\n"
            "    ebbing through so slow,\n"
            "Naked on the steep, soft lip\n"
            "Of the bank I stand watching my own white shadow\n"
            "    quivering to and fro."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "brook.ebbing" not in full_text

    def test_wrap_019_were_lost(self):
        # Source: Amores Poems, wrap corruption: were.lost
        passage = (
            "What if the gorse flowers shrivelled and kissing were\n"
            "    lost?\n"
            "Without the pulsing waters, where were the marigolds\n"
            "    and the songs of the brook?\n"
            "If my veins and my breasts with love embossed\n"
            "Withered, my insolent soul would be gone like flowers\n"
            "    that the hot wind took."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "were.lost" not in full_text

    def test_wrap_020_scorned_and(self):
        # Source: Amores Poems, wrap corruption: scorned.and
        passage = (
            "So my soul like a passionate woman turns,\n"
            "Filled with remorseful terror to the man she scorned,\n"
            "    and her love\n"
            "For myself in my own eyes' laughter burns,\n"
            "Runs ecstatic over the pliant folds rippling down to\n"
            "    my belly from the breast-lights above."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "scorned.and" not in full_text

    def test_wrap_021_once_goes(self):
        # Source: Amores Poems, wrap corruption: once.goes
        passage = (
            "Over my sunlit skin the warm, clinging air,\n"
            "Rich with the songs of seven larks singing at once,\n"
            "    goes kissing me glad.\n"
            "And the soul of the wind and my blood compare\n"
            "Their wandering happiness, and the wind, wasted in\n"
            "    liberty, drifts on and is sad."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "once.goes" not in full_text

    def test_wrap_022_violet_hush(self):
        # Source: Amores Poems, wrap corruption: violet.hush
        passage = (
            "SOMEWHERE the long mellow note of the blackbird\n"
            "Quickens the unclasping hands of hazel,\n"
            "Somewhere the wind-flowers fling their heads back,\n"
            "Stirred by an impetuous wind. Some ways'll\n"
            "All be sweet with white and blue violet.\n"
            "    (Hush now, hush. Where am I?--Biuret--)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "violet.hush" not in full_text

    def test_wrap_023_pool_work(self):
        # Source: Amores Poems, wrap corruption: pool.work
        passage = (
            "On the green wood's edge a shy girl hovers\n"
            "From out of the hazel-screen on to the grass,\n"
            "Where wheeling and screaming the petulant plovers\n"
            "Wave frighted. Who comes? A labourer, alas!\n"
            "Oh the sunset swims in her eyes' swift pool.\n"
            "    (Work, work, you fool--!)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pool.work" not in full_text

    def test_wrap_024_bust_all(self):
        # Source: Amores Poems, wrap corruption: bust.all
        passage = (
            "(_Tears and dreams for them; for me\n"
            "Bitter science--the exams. are near.\n"
            "I wish I bore it more patiently.\n"
            "I wish you did not wait, my dear,\n"
            "For me to come: since work I must:\n"
            "Though it's all the same when we are dead.--\n"
            "I wish I was only a bust,\n"
            "      All head._)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bust.all" not in full_text

    def test_wrap_025_terrible_whips(self):
        # Source: Amores Poems, wrap corruption: terrible.whips
        passage = (
            "OUTSIDE the house an ash-tree hung its terrible\n"
            "    whips,\n"
            "And at night when the wind arose, the lash of the tree\n"
            "Shrieked and slashed the wind, as a ship's\n"
            "Weird rigging in a storm shrieks hideously."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "terrible.whips" not in full_text

    def test_wrap_026_slender_lash(self):
        # Source: Amores Poems, wrap corruption: slender.lash
        passage = (
            "Within the house two voices arose in anger, a slender\n"
            "    lash\n"
            "Whistling delirious rage, and the dreadful sound\n"
            "Of a thick lash booming and bruising, until it\n"
            "    drowned\n"
            "The other voice in a silence of blood, 'neath the noise\n"
            "    of the ash."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "slender.lash" not in full_text

    def test_wrap_027_like_heavy(self):
        # Source: Amores Poems, wrap corruption: like.heavy
        passage = (
            "THIS is the last of all, this is the last!\n"
            "I must hold my hands, and turn my face to the fire,\n"
            "I must watch my dead days fusing together in dross,\n"
            "Shape after shape, and scene after scene from my past\n"
            "Fusing to one dead mass in the sinking fire\n"
            "Where the ash on the dying coals grows swiftly, like\n"
            "    heavy moss."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "like.heavy" not in full_text

    def test_wrap_028_frozen_seas(self):
        # Source: Amores Poems, wrap corruption: frozen.seas
        passage = (
            "Like a strange white bird blown out of the frozen\n"
            "    seas,\n"
            "Like a bird from the far north blown with a broken\n"
            "    wing\n"
            "Into our sooty garden, he drags and beats\n"
            "From place to place perpetually, seeking release\n"
            "From me, from the hand of my love which creeps up,\n"
            "    needing\n"
            "His happiness, whilst he in displeasure retreats."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "frozen.seas" not in full_text

    def test_wrap_029_since_long(self):
        # Source: Amores Poems, wrap corruption: since.long
        passage = (
            "Three times have I offered myself, three times rejected.\n"
            "It will not be any more. No more, my son, my son!\n"
            "Never to know the glad freedom of obedience, since\n"
            "    long ago\n"
            "The angel of childhood kissed me and went. I expected\n"
            "Another would take me,--and now, my son, O my son,\n"
            "I must sit awhile and wait, and never know\n"
            "The loss of myself, till death comes, who cannot fail."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "since.long" not in full_text

    def test_wrap_030_skyrocket_dropping(self):
        # Source: Amores Poems, wrap corruption: skyrocket.dropping
        passage = (
            "THE five old bells\n"
            "Are hurrying and eagerly calling,\n"
            "Imploring, protesting\n"
            "They know, but clamorously falling\n"
            "Into gabbling incoherence, never resting,\n"
            "Like spattering showers from a bursten sky-rocket\n"
            "    dropping\n"
            "In splashes of sound, endlessly, never stopping."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "skyrocket.dropping" not in full_text

    def test_wrap_031_her_face(self):
        # Source: Amores Poems, wrap corruption: her.face
        passage = (
            "The patient Night\n"
            "Sits indifferent, hugged in her rags,\n"
            "She neither knows nor cares\n"
            "Why the old church sobs and brags;\n"
            "The light distresses her eyes, and tears\n"
            "Her old blue cloak, as she crouches and covers her\n"
            "    face,\n"
            "Smiling, perhaps, if we knew it, at the bells' loud\n"
            "    clattering disgrace."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "her.face" not in full_text

    def test_wrap_032_loves_through(self):
        # Source: Amores Poems, wrap corruption: loves.through
        passage = (
            "A come and go of March-day loves\n"
            "    Through the flower-vine, trailing screen;\n"
            "       A fluttering in of doves.\n"
            "    Then a launch abroad of shrinking doves\n"
            "    Over the waste where no hope is seen\n"
            "    Of open hands:\n"
            "               Dance in and out\n"
            "    Small-bosomed girls of the spring of love,\n"
            "    With a bubble of laughter, and shrilly shout\n"
            "    Of mirth; then the dripping of tears on your\n"
            "        glove."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "loves.through" not in full_text

    def test_wrap_033_the_sill(self):
        # Source: Amores Poems, wrap corruption: the.sill
        passage = (
            "I HAVE opened the window to warm my hands on the\n"
            "    sill\n"
            "Where the sunlight soaks in the stone: the afternoon\n"
            "Is full of dreams, my love, the boys are all still\n"
            "In a wistful dream of Lorna Doone."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.sill" not in full_text

    def test_wrap_034_and_shine(self):
        # Source: Amores Poems, wrap corruption: and.shine
        passage = (
            "The clink of the shunting engines is sharp and fine,\n"
            "Like savage music striking far off, and there\n"
            "On the great, uplifted blue palace, lights stir and\n"
            "   shine\n"
            "Where the glass is domed in the blue, soft air."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.shine" not in full_text

    def test_wrap_035_and_wistfulnes(self):
        # Source: Amores Poems, wrap corruption: and.wistfulness
        passage = (
            "There lies the world, my darling, full of wonder and\n"
            "    wistfulness and strange\n"
            "Recognition and greetings of half-acquaint things, as\n"
            "    I greet the cloud\n"
            "Of blue palace aloft there, among misty indefinite\n"
            "    dreams that range\n"
            "At the back of my life's horizon, where the dreamings\n"
            "    of past lives crowd."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.wistfulness" not in full_text

    def test_wrap_036_the_mellow(self):
        # Source: Amores Poems, wrap corruption: the.mellow
        passage = (
            "Over the nearness of Norwood Hill, through the\n"
            "    mellow veil\n"
            "Of the afternoon glows to me the old romance of\n"
            "    David and Dora,\n"
            "With the old, sweet, soothing tears, and laughter\n"
            "    that shakes the sail\n"
            "Of the ship of the soul over seas where dreamed\n"
            "    dreams lure the unoceaned explorer."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.mellow" not in full_text

    def test_wrap_037_where_the(self):
        # Source: Amores Poems, wrap corruption: where.the
        passage = (
            "All the bygone, hushèd years\n"
            "Streaming back where the mist distils\n"
            "Into forgetfulness: soft-sailing waters where fears\n"
            "No longer shake, where the silk sail fills\n"
            "With an unfelt breeze that ebbs over the seas, where\n"
            "    the storm\n"
            "Of living has passed, on and on\n"
            "Through the coloured iridescence that swims in the\n"
            "    warm\n"
            "Wake of the tumult now spent and gone,\n"
            "Drifts my boat, wistfully lapsing after\n"
            "The mists of vanishing tears and the echo of laughter."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "where.the" not in full_text

    def test_wrap_038_railway_and(self):
        # Source: Amores Poems, wrap corruption: railway.and
        passage = (
            "The surface of dreams is broken,\n"
            "The picture of the past is shaken and scattered.\n"
            "Fluent, active figures of men pass along the railway,\n"
            "    and I am woken\n"
            "From the dreams that the distance flattered."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "railway.and" not in full_text

    def test_wrap_039_they_move(self):
        # Source: Amores Poems, wrap corruption: they.move
        passage = (
            "Along the railway, active figures of men.\n"
            "They have a secret that stirs in their limbs as they\n"
            "    move\n"
            "Out of the distance, nearer, commanding my dreamy\n"
            "    world."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "they.move" not in full_text

    def test_wrap_040_moving_through(self):
        # Source: Amores Poems, wrap corruption: moving.through
        passage = (
            "Here in the subtle, rounded flesh\n"
            "Beats the active ecstasy.\n"
            "In the sudden lifting my eyes, it is clearer,\n"
            "The fascination of the quick, restless Creator moving\n"
            "    through the mesh\n"
            "Of men, vibrating in ecstasy through the rounded\n"
            "    flesh."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "moving.through" not in full_text

    def test_wrap_041_softtoned_and(self):
        # Source: Amores Poems, wrap corruption: softtoned.and
        passage = (
            "The old dreams are beautiful, beloved, soft-toned,\n"
            "    and sure,\n"
            "But the dream-stuff is molten and moving mysteriously,\n"
            "Alluring my eyes; for I, am I not also dream-stuff,\n"
            "Am I not quickening, diffusing myself in the pattern,\n"
            "    shaping and shapen?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "softtoned.and" not in full_text

    def test_wrap_042_dreams_reflected(self):
        # Source: Amores Poems, wrap corruption: dreams.reflected
        passage = (
            "Here in my class is the answer for the great yearning:\n"
            "Eyes where I can watch the swim of old dreams\n"
            "    reflected on the molten metal of dreams,\n"
            "Watch the stir which is rhythmic and moves them\n"
            "    all as a heart-beat moves the blood,\n"
            "Here in the swelling flesh the great activity working,\n"
            "Visible there in the change of eyes and the mobile\n"
            "    features."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dreams.reflected" not in full_text

    def test_wrap_043_unseen_shaper(self):
        # Source: Amores Poems, wrap corruption: unseen.shaper
        passage = (
            "Oh the great mystery and fascination of the unseen\n"
            "    Shaper,\n"
            "The power of the melting, fusing Force--heat,\n"
            "    light, all in one,\n"
            "Everything great and mysterious in one, swelling and\n"
            "    shaping the dream in the flesh,\n"
            "As it swells and shapes a bud into blossom."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "unseen.shaper" not in full_text

    def test_wrap_044_scattered_snow(self):
        # Source: Amores Poems, wrap corruption: scattered.snow
        passage = (
            "YESTERDAY the fields were only grey with scattered\n"
            "   snow,\n"
            "And now the longest grass-leaves hardly emerge;\n"
            "Yet her deep footsteps mark the snow, and go\n"
            "On towards the pines at the hills' white verge."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "scattered.snow" not in full_text

    def test_wrap_045_must_know(self):
        # Source: Amores Poems, wrap corruption: must.know
        passage = (
            "Why does she come so promptly, when she must\n"
            "   know\n"
            "That she's only the nearer to the inevitable farewell;\n"
            "The hill is steep, on the snow my steps are slow--\n"
            "Why does she come, when she knows what I have to\n"
            "   tell?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "must.know" not in full_text

    def test_wrap_046_the_wind(self):
        # Source: Amores Poems, wrap corruption: the.wind
        passage = (
            "WHEN the bare feet of the baby beat across the grass\n"
            "The little white feet nod like white flowers in the\n"
            "    wind,\n"
            "They poise and run like ripples lapping across the\n"
            "    water;\n"
            "And the sight of their white play among the grass\n"
            "Is like a little robin's song, winsome,\n"
            "Or as two white butterflies settle in the cup of one\n"
            "    flower\n"
            "For a moment, then away with a flutter of wings."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.wind" not in full_text

    def test_wrap_047_roots_are(self):
        # Source: Amores Poems, wrap corruption: roots.are
        passage = (
            "And there is the dark, my darling, where the roots\n"
            "     are entangled and fight\n"
            "Each one for its hold on the oblivious darkness, I\n"
            "     know that there\n"
            "In the night where we first have being, before we rise\n"
            "     on the light,\n"
            "We are not brothers, my darling, we fight and we\n"
            "     do not spare."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "roots.are" not in full_text

    def test_wrap_048_keep_cannot(self):
        # Source: Amores Poems, wrap corruption: keep.cannot
        passage = (
            "And in the original dark the roots cannot keep,\n"
            "     cannot know\n"
            "Any communion whatever, but they bind themselves\n"
            "     on to the dark,\n"
            "And drawing the darkness together, crush from it a\n"
            "     twilight, a slow\n"
            "Burning that breaks at last into leaves and a flower's\n"
            "     bright spark."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "keep.cannot" not in full_text

    def test_wrap_049_they_turned(self):
        # Source: Amores Poems, wrap corruption: they.turned
        passage = (
            "I came to the boys with love, my dear, but they\n"
            "     turned on me;\n"
            "I came with gentleness, with my heart 'twixt my\n"
            "     hands like a bowl,\n"
            "Like a loving-cup, like a grail, but they spilt it\n"
            "     triumphantly\n"
            "And tried to break the vessel, and to violate my\n"
            "     soul."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "they.turned" not in full_text

    def test_wrap_050_shall_burn(self):
        # Source: Amores Poems, wrap corruption: shall.burn
        passage = (
            "But whosoever would pluck apart my flowering shall\n"
            "     burn their hands,\n"
            "So flowers are tender folk, and roots can only hide,\n"
            "Yet my flowerings of love are a fire, and the scarlet\n"
            "     brands\n"
            "Of my love are roses to look at, but flames to chide."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shall.burn" not in full_text

    def test_wrap_051_destroyed_and(self):
        # Source: Amores Poems, wrap corruption: destroyed.and
        passage = (
            "But comfort me, my love, now the fires are low,\n"
            "Now I am broken to earth like a winter destroyed,\n"
            "     and all\n"
            "Myself but a knowledge of roots, of roots in the dark\n"
            "     that throw\n"
            "A net on the undersoil, which lies passive beneath\n"
            "     their thrall."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "destroyed.and" not in full_text

    def test_wrap_052_yours_alone(self):
        # Source: Amores Poems, wrap corruption: yours.alone
        passage = (
            "But comfort me, for henceforth my love is yours\n"
            "     alone,\n"
            "To you alone will I offer the bowl, to you will I give\n"
            "My essence only, but love me, and I will atone\n"
            "To you for my general loving, atone as long as I live."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "yours.alone" not in full_text

    def test_wrap_053_and_sable(self):
        # Source: Amores Poems, wrap corruption: and.sable
        passage = (
            "A FAINT, sickening scent of irises\n"
            "Persists all morning. Here in a jar on the table\n"
            "A fine proud spike of purple irises\n"
            "Rising above the class-room litter, makes me unable\n"
            "To see the class's lifted and bended faces\n"
            "Save in a broken pattern, amid purple and gold and\n"
            "    sable."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.sable" not in full_text

    def test_wrap_054_overcast_you(self):
        # Source: Amores Poems, wrap corruption: overcast.you
        passage = (
            "I can smell the gorgeous bog-end, in its breathless\n"
            "Dazzle of may-blobs, when the marigold glare overcast\n"
            "     you\n"
            "With fire on your cheeks and your brow and your\n"
            "    chin as you dipped\n"
            "Your face in the marigold bunch, to touch and contrast\n"
            "    you,\n"
            "Your own dark mouth with the bridal faint lady-smocks,\n"
            "Dissolved on the golden sorcery you should not\n"
            "    outlast."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "overcast.you" not in full_text

    def test_wrap_055_shall_loom(self):
        # Source: Amores Poems, wrap corruption: shall.loom
        passage = (
            "AH, my darling, when over the purple horizon shall\n"
            "    loom\n"
            "The shrouded mother of a new idea, men hide their\n"
            "    faces,\n"
            "Cry out and fend her off, as she seeks her procreant\n"
            "    groom,\n"
            "Wounding themselves against her, denying her\n"
            "    fecund embraces."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shall.loom" not in full_text

