import pytest
from fast_sentence_segment import segment_text


class TestEbooksEdgeworth:
    """Integration tests mined from Maria Edgeworth ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1800s
    """

    def test_wrap_001_many_references(self):
        # Source: Castle Rackrent, wrap corruption: many.references
        passage = (
            "[Note: The body of this novel contains a lot of footnotes and many\n"
            "    references to the Glossary at the end. The references to the\n"
            "    Glossary have been numbered in square brackets. They are linked to\n"
            "    the Glossary at the end of the eBook. The footnotes (which are\n"
            "    sometimes quite long) have been numbered in curly brackets. They\n"
            "    are linked to the note at the end of the paragraph."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "many.references" not in full_text

    def test_wrap_002_sober_falls(self):
        # Source: Castle Rackrent, wrap corruption: sober.falls
        passage = (
            "He that goes to bed, and goes to bed sober,\n"
            "    Falls as the leaves do, falls as the leaves do, and dies in October;\n"
            "    But he that goes to bed, and goes to bed mellow,\n"
            "    Lives as he ought to do, lives as he ought to do, and dies an honest fellow."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sober.falls" not in full_text

    def test_wrap_003_the_shape(self):
        # Source: Castle Rackrent, wrap corruption: the.shape
        passage = (
            "{5} The Banshee is a species of aristocratic fairy, who, in the\n"
            "   shape of a little hideous old woman, has been known to appear, and\n"
            "   heard to sing in a mournful supernatural voice under the windows of\n"
            "   great houses, to warn the family that some of them are soon to die.\n"
            "   In the last century every great family in Ireland had a Banshee, who\n"
            "   attended regularly; but latterly their visits and songs have been\n"
            "   discontinued."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.shape" not in full_text

    def test_wrap_004_not_write(self):
        # Source: Castle Rackrent, wrap corruption: not.write
        passage = (
            "{11} HER MARK.--It was the custom in Ireland for those who could not\n"
            "   write to make a cross to stand for their signature, as was formerly\n"
            "   the practice of our English monarchs. The Editor inserts the\n"
            "   facsimile of an Irish mark, which may hereafter be valuable to a\n"
            "   judicious antiquary--"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "not.write" not in full_text

    def test_wrap_005_most_irish(self):
        # Source: Castle Rackrent, wrap corruption: most.irish
        passage = (
            "{13} GOSSOON: a little boy--from the French word garçon. In most\n"
            "   Irish families there used to be a barefooted gossoon, who was slave\n"
            "   to the cook and the butler, and who, in fact, without wages, did all\n"
            "   the hard work of the house. Gossoons were always employed as\n"
            "   messengers. The Editor has known a gossoon to go on foot, without\n"
            "   shoes or stockings, fifty-one English miles between sunrise and\n"
            "   sunset."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "most.irish" not in full_text

    def test_wrap_006_expression_that(self):
        # Source: Castle Rackrent, wrap corruption: expression.that
        passage = (
            "{17} MY LITTLE POTATOES.--Thady does not mean by this expression\n"
            "   that his potatoes were less than other people’s, or less than the\n"
            "   usual size. LITTLE is here used only as an Italian diminutive,\n"
            "   expressive of fondness."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "expression.that" not in full_text

    def test_wrap_007_for_sweeping(self):
        # Source: Castle Rackrent, wrap corruption: for.sweeping
        passage = (
            "{19} Wigs were formerly used instead of brooms in Ireland for\n"
            "   sweeping or dusting tables, stairs, etc. The Editor doubted the fact\n"
            "   till he saw a labourer of the old school sweep down a flight of\n"
            "   stairs with his wig; he afterwards put it on his head again with the\n"
            "   utmost composure, and said, ‘Oh, please your honour, it’s never a\n"
            "   bit the worse."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "for.sweeping" not in full_text

    def test_wrap_008_all_deal(self):
        # Source: Castle Rackrent, wrap corruption: all.deal
        passage = (
            "Deal on, deal on, my merry men all,\n"
            "       Deal on your cakes and your wine,\n"
            "     For whatever is dealt at her funeral to-day\n"
            "       Shall be dealt to-morrow at mine."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.deal" not in full_text

    def test_wrap_009_ill_shame(self):
        # Source: Leonora, wrap corruption: ill.shame
        passage = (
            "\"He taught them shame, the sudden sense of ill--\n"
            "   Shame, Nature's hasty conscience, which forbids\n"
            "   Weak inclination ere it grows to will,\n"
            "   Or stays rash will before it grows to deeds.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ill.shame" not in full_text

    def test_wrap_010_you_for(self):
        # Source: Leonora, wrap corruption: you.for
        passage = (
            "\"I mourn, but, ye woodlands, I mourn not for you,\n"
            "   For morn is approaching your charms to restore,\n"
            "   Perfum'd with fresh fragrance, and glitt'ring with dew.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.for" not in full_text

    def test_wrap_011_dame_august(self):
        # Source: Leonora, wrap corruption: dame.august
        passage = (
            "\"Let wealth, let honour wait the wedded dame,\n"
            "   August her deed, and sacred be her fame;\n"
            "   Before true passion all those views remove,\n"
            "   Fame, wealth, and honour, what are you to love?\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dame.august" not in full_text

    def test_wrap_012_this_letter(self):
        # Source: Leonora, wrap corruption: this.letter
        passage = (
            "It is with extreme concern I am forced to add, that since I wrote this\n"
            "  Letter the child has been so ill that I have fears for his life.--His\n"
            "poor mother!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "this.letter" not in full_text

    def test_wrap_013_notes_hyphenatio(self):
        # Source: Leonora, wrap corruption: notes.hyphenation
        passage = (
            "=Transcriber's Notes:=\n"
            "  hyphenation, spelling and grammar have been preserved as in the original\n"
            "  Page 61, out of doubt, Admire ==> out of doubt. Admire\n"
            "  Page 88, the eclat of public ==> the eclat of public\n"
            "  Page 124, grave and inpenetrable ==> grave and impenetrable"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "notes.hyphenation" not in full_text

    def test_wrap_014_woe_the(self):
        # Source: Murad the Unlucky and Other Tales, wrap corruption: woe.the
        passage = (
            "\"There oft are heard the notes of infant woe,\n"
            "  The short thick sob, loud scream, and shriller squall--\n"
            "  How can you, mothers, vex your infants so?\"--POPE"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "woe.the" not in full_text

    def test_wrap_015_bower_amusement(self):
        # Source: Murad the Unlucky and Other Tales, wrap corruption: bower.amusement
        passage = (
            "\"Come often, then; for haply in my bower\n"
            "  Amusement, knowledge, wisdom, thou may'st gain:\n"
            "  If I one soul improve, I have not lived in vain.\"--BEATTIE."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bower.amusement" not in full_text

    def test_wrap_016_face_each(self):
        # Source: Murad the Unlucky and Other Tales, wrap corruption: face.each
        passage = (
            "\"Her life, as lovely as her face,\n"
            "  Each duty mark'd with every grace;\n"
            "  Her native sense improved by reading,\n"
            "  Her native sweetness by good breeding.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "face.each" not in full_text

    def test_wrap_017_car_the(self):
        # Source: Murad the Unlucky and Other Tales, wrap corruption: car.the
        passage = (
            "\"Alas! full oft on Guilt's victorious car\n"
            "  The spoils of Virtue are in triumph borne,\n"
            "  While the fair captive, marked with many a scar,\n"
            "  In lone obscurity, oppressed, forlorn,\n"
            "  Resigns to tears her angel form.\"--BEATTIE."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "car.the" not in full_text

    def test_wrap_018_good_whilst(self):
        # Source: Murad the Unlucky and Other Tales, wrap corruption: good.whilst
        passage = (
            "\"I love you--I wish you were here again--I will be very very good\n"
            "  whilst you are away. If you stay away ever so long, I shall never\n"
            "  forget you, nor your goodness; but I hope you will soon be able to\n"
            "  come back, and this is what I pray for every night. Sister Frances\n"
            "  says I may tell you that I am very good, and Victoire thinks so too.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "good.whilst" not in full_text

    def test_wrap_019_rest_thy(self):
        # Source: Murad the Unlucky and Other Tales, wrap corruption: rest.thy
        passage = (
            "\"When thy last breath, ere Nature sank to rest\n"
            "  Thy meek submission to thy God expressed;\n"
            "  When thy last look, ere thought and feeling fled,\n"
            "  A mingled gleam of hope and triumph shed;\n"
            "  What to thy soul its glad assurance gave--\n"
            "  Its hope in death, its triumph o'er the grave?\n"
            "  The sweet remembrance of unblemished youth,\n"
            "  Th' inspiring voice of innocence and truth!\"--ROGERS."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rest.thy" not in full_text

    def test_wrap_020_lost_her(self):
        # Source: Murad the Unlucky and Other Tales, wrap corruption: lost.her
        passage = (
            "\"The character is lost!\n"
            "  Her head adorned with lappets, pinned aloft,\n"
            "  And ribands streaming gay, superbly raised,\n"
            "  Indebted to some smart wig-weaver's hand\n"
            "  For more than half the tresses it sustains.\"--COWPER."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lost.her" not in full_text

    def test_wrap_021_tree_laden(self):
        # Source: Murad the Unlucky and Other Tales, wrap corruption: tree.laden
        passage = (
            "\"But beauty, like the fair Hesperian tree,\n"
            "  Laden with blooming gold, had need the guard\n"
            "  Of dragon watch with unenchanted eye\n"
            "  To save her blossoms, or defend her fruit.\"--MILTON."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tree.laden" not in full_text

    def test_wrap_022_earth_virtue(self):
        # Source: Practical Education Volume I, wrap corruption: earth.virtue
        passage = (
            "\"When first thy sire to send on earth\n"
            "    Virtue, his darling child, design'd,\n"
            "    To thee he gave the heavenly birth,\n"
            "    And bade to form her infant mind.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "earth.virtue" not in full_text

    def test_wrap_023_fly_self(self):
        # Source: Practical Education Volume I, wrap corruption: fly.self
        passage = (
            "\"Scared at thy frown, terrific fly\n"
            "    Self pleasing follies, idle brood,\n"
            "    Wild laughter, noise, and thoughtless joy,\n"
            "    And leave us leisure to be good.\n"
            "    Light they disperse, and with them go\n"
            "    The summer friend, the flattering foe;\n"
            "    By vain prosperity receiv'd,\n"
            "    To her they vow their truth, and are again believ'd.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fly.self" not in full_text

    def test_wrap_024_grove_their(self):
        # Source: Practical Education Volume I, wrap corruption: grove.their
        passage = (
            "\"Then vanished many a sea-girt isle and grove,\n"
            "    Their forests floating on the wat'ry plain;\n"
            "    Then famed for arts, and laws deriv'd from Jove,\n"
            "    My Atalantis sunk beneath the main.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "grove.their" not in full_text

    def test_wrap_025_pride_pours(self):
        # Source: Practical Education Volume I, wrap corruption: pride.pours
        passage = (
            "\"To her no more Augusta's wealthy pride,\n"
            "    Pours the full tribute from Potosi's mine;\n"
            "    Nor fresh blown garlands village maids provide,\n"
            "    A purer offering at her rustic shrine.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pride.pours" not in full_text

    def test_wrap_026_born_the(self):
        # Source: Practical Education Volume I, wrap corruption: born.the
        passage = (
            "\"Ah! once to fame and bright dominion born,\n"
            "      The earth and smiling ocean saw me rise,\n"
            "    With time coeval, and the star of morn,\n"
            "      The first, the fairest daughter of the skies."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "born.the" not in full_text

    def test_wrap_027_sprung_the(self):
        # Source: Practical Education Volume I, wrap corruption: sprung.the
        passage = (
            "\"Then, when at heaven's prolific mandate sprung\n"
            "      The radiant beam of new-created day,\n"
            "    Celestial harps, to airs of triumph strung,\n"
            "      Hail'd the glad dawn, and angel's call'd me May."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sprung.the" not in full_text

    def test_wrap_028_sound_and(self):
        # Source: Practical Education Volume I, wrap corruption: sound.and
        passage = (
            "\"Space in her empty regions heard the sound,\n"
            "      And hills and dales, and rocks and valleys rung;\n"
            "    The sun exulted in his glorious round,\n"
            "      And shouting planets in their courses sung.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sound.and" not in full_text

    def test_wrap_029_extreme_the(self):
        # Source: Practical Education Volume Ii, wrap corruption: extreme.the
        passage = (
            "\"What modes of sight between each vast extreme,\n"
            "    The mole's dim curtain, and the lynx's beam;\n"
            "    Of smell the headlong lioness between,\n"
            "    And hound sagacious on the tainted green.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "extreme.the" not in full_text

    def test_wrap_030_repair_the(self):
        # Source: Practical Education Volume Ii, wrap corruption: repair.the
        passage = (
            "\"Haste, then, ye spirits; to your charge repair,\n"
            "    The fluttering fan be Zephyretta's care;\n"
            "    The drops to thee, Brillante, we consign,\n"
            "    And, Momentilla, let the watch be thine;\n"
            "    Do thou, Crispissa, tend her favourite lock,\n"
            "    Ariel himself shall be the guard of Shock.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "repair.the" not in full_text

    def test_wrap_031_pursue_but(self):
        # Source: Practical Education Volume Ii, wrap corruption: pursue.but
        passage = (
            "\"Envy will merit, as its shade, pursue;\n"
            "    But, like a shadow, proves the substance true:\n"
            "    For envy'd wit, like Sol eclips'd, makes known\n"
            "    Th' opposing body's grossness, not its own.\n"
            "    When first that sun too pow'rful beams displays,\n"
            "    It draws up vapour, which obscures its rays;\n"
            "    But ev'n those clouds at last adorn its way,\n"
            "    Reflect new glories, and augment the day.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pursue.but" not in full_text

    def test_wrap_032_name_swear(self):
        # Source: Practical Education Volume Ii, wrap corruption: name.swear
        passage = (
            "\"Approach, contemplate this immortal name,\n"
            "    Swear on this shrine to emulate his fame;\n"
            "    To dare, like him, e'en to thy latest breath,\n"
            "    Contemning chains, and poverty, and death.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "name.swear" not in full_text

    def test_wrap_033_sat_revolving(self):
        # Source: Practical Education Volume Ii, wrap corruption: sat.revolving
        passage = (
            "\"With downcast looks the joyless victor sat,\n"
            "    Revolving in his altered soul\n"
            "    The various turns of chance below;\n"
            "    And now and then a sigh he stole,\n"
            "    And tears began to flow.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sat.revolving" not in full_text

    def test_wrap_034_come_one(self):
        # Source: Practical Education Volume Ii, wrap corruption: come.one
        passage = (
            "\"Both of a name, lo! two contractors come;\n"
            "    One cheats in corn, and t'other cheats in rum.\n"
            "    Which is the greater, if you can, explain,\n"
            "    A rogue in spirit, or a rogue in grain?\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "come.one" not in full_text

    def test_wrap_035_invites_and(self):
        # Source: Practical Education Volume Ii, wrap corruption: invites.and
        passage = (
            "\"And with soft murmurs faithless sleep invites,\n"
            "    And there the flying past again delights;\n"
            "    And near the door the noxious poppy grows,\n"
            "    And spreads his sleepy milk at daylight's close.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "invites.and" not in full_text

    def test_wrap_036_dance_what(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: dance.what
        passage = (
            "“O Lord, methought what pain it was to dance!\n"
            "    What dreadful noise of fiddles in my ears!\n"
            "    What sights of ugly belles within my eyes!\n"
            "    ----Then came wandering by,\n"
            "    A shadow like a devil, with red hair,\n"
            "    ‘Dizen’d with flowers; and she bawl’d out aloud,\n"
            "    Clarence is come; false, fleeting, perjured Clarence!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dance.what" not in full_text

    def test_wrap_037_more_cried(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: more.cried
        passage = (
            "“When things are settled, one can’t bear to have them unsettled--but\n"
            "your ladyship must have your own way, to be sure--I’ll say no more,”\n"
            " cried she, throwing down the dresses."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "more.cried" not in full_text

    def test_wrap_038_dear_said(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: dear.said
        passage = (
            "“Clarence Hervey!” interrupted Belinda. “Clarence Hervey, my dear,”\n"
            " said Lady Delacour, coolly: “he can do every thing, you know, even drive\n"
            "pigs, better than any body else!--but let me go on."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dear.said" not in full_text

    def test_wrap_039_ballinacra_who(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: ballinacrasy.who
        passage = (
            "“There was a young man in Ballinacrasy,\n"
            "    Who wanted a wife to make him un_asy_,\n"
            "    And thus in gentle strains he spoke her,\n"
            "    Arrah, will you marry me, my dear Ally Croker?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ballinacrasy.who" not in full_text

    def test_wrap_040_honour_replied(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: honour.replied
        passage = (
            "“The foremost is Percival, of Oakly-park, I think, ‘pon my honour,”\n"
            " replied Mr. St. George, and he then began to settle how many thousands\n"
            "a year Mr. Percival was worth. This point was not decided when the\n"
            "gentlemen came up to the spot where Sir Philip was standing."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "honour.replied" not in full_text

    def test_wrap_041_nonono_answered(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: nonono.answered
        passage = (
            "Lord Delacour stopped short. “Tell me, then,” cried Lord Delacour,\n"
            "“is not a lover of Lady Delacour’s concealed there?” “No!--No!--No!”\n"
            " answered Belinda. “Then a lover of Miss Portman?” said Lord Delacour.\n"
            "“Gad! we have hit it now, I believe.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "nonono.answered" not in full_text

    def test_wrap_042_girl_said(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: girl.said
        passage = (
            "“Yes--are you much hurt?” said Belinda. “Oh, you are a charming girl!”\n"
            " said Lady Delacour. “Who would have thought you had so much presence of\n"
            "mind and courage--have you the key safe?” “Here it is,” said Belinda,\n"
            "producing it; and she repeated her question, “Are you much hurt?” “I am\n"
            "not in pain now,” said Lady Delacour, “but I have suffered terribly.\n"
            "If I could get rid of all this finery, if you could put me to bed, I\n"
            "could sleep perhaps.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "girl.said" not in full_text

    def test_wrap_043_marriott_said(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: marriott.said
        passage = (
            "And here Marriott actually burst into tears. “But, my dear Marriott,”\n"
            " said Lady Delacour, “I only object to your macaw--may not I dislike your\n"
            "macaw without disliking you?--I have heard of ‘love me, love my dog;’\n"
            "but I never heard of ‘love me, love my bird’--did you, Miss Portman?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "marriott.said" not in full_text

    def test_wrap_044_longer_and(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: longer.and
        passage = (
            "“Oh, that odious macaw!” cried her ladyship, “I can endure it no longer”\n"
            " (and she rang her bell violently): “it kept me from sleeping all last\n"
            "night--Marriott must give up this bird. Marriott, I cannot endure that\n"
            "macaw--you must part with it for my sake, Marriott. It cost you four\n"
            "guineas: I am sure I would give five with the greatest pleasure to get\n"
            "rid of it, for it is the torment of my life.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "longer.and" not in full_text

    def test_wrap_045_body_her(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: body.her
        passage = (
            "“Then I must go, my lady,” said Marriott, angrily, “that is certain;\n"
            "for to part with my macaw is a thing I cannot do to please any body.”\n"
            " Her eyes turned with indignation upon Belinda, from association merely;\n"
            "because the last time that she had been angry about her macaw, she had\n"
            "also been angry with Miss Portman, whom she imagined to be the secret\n"
            "enemy of her favourite."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "body.her" not in full_text

    def test_wrap_046_trifles_said(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: trifles.said
        passage = (
            "“But it is so difficult to get at facts, even about the merest trifles,”\n"
            " said Lady Delacour. “Actions we see, but their causes we seldom see--an\n"
            "aphorism worthy of Confucius himself: now to apply. Pray, my dear\n"
            "Helena, how came you by the pretty gold fishes that you were so good as\n"
            "to send to me yesterday?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "trifles.said" not in full_text

    def test_wrap_047_see_continued(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: see.continued
        passage = (
            "“Whose mark is this? Yours, Belinda, I am sure, by its elegance,” said\n"
            "Lady Delacour. “So! this is a concerted plan between you two, I see,”\n"
            " continued her ladyship, with an air of pique: “you have contrived\n"
            "prettily de me dire des vérités! One says, ‘Let us try our fate by the\n"
            "Sortes Virgilianae;’ the other has dexterously put a mark in the book,\n"
            "to make it open upon a lesson for the naughty child.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "see.continued" not in full_text

    def test_wrap_048_people_said(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: people.said
        passage = (
            "“The daughter will eclipse, totally eclipse, the mother,” said Lady\n"
            "Delacour. “That total eclipse has been foretold by many knowing people,”\n"
            " said Clarence Hervey; “but how can there be an eclipse between two\n"
            "bodies which never cross one another and that I understand to be the\n"
            "case between the duchess and her daughter.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "people.said" not in full_text

    def test_wrap_049_picture_said(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: picture.said
        passage = (
            "“Oh, damme! no--‘tis a cursed bore; and yet there are some fine\n"
            "pictures: one in particular--hey, Rochfort?--one damned fine picture!”\n"
            " said Sir Philip. And the two gentlemen laughing significantly, followed\n"
            "Lady Delacour and Belinda into the rooms."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "picture.said" not in full_text

    def test_wrap_050_honour_repeated(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: honour.repeated
        passage = (
            "“Ay, there’s one picture that’s worth all the rest, ‘pon honour!”\n"
            " repeated Rochfort; “and we’ll leave it to your ladyship’s and Miss\n"
            "Portman’s taste and judgment to find it out, mayn’t we, Sir Philip?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "honour.repeated" not in full_text

    def test_wrap_051_likeness_added(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: likeness.added
        passage = (
            "“I’ll take my oath as to the portrait’s being a devilish good likeness,”\n"
            " added Sir Philip; and as he spoke, he turned to Miss Portman: “Miss\n"
            "Portman has it! damme, Miss Portman has him!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "likeness.added" not in full_text

    def test_wrap_052_clary_added(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: clary.added
        passage = (
            "“Here’s the catalogue; here’s the picture your ladyship wants. St.\n"
            "Pierre’s Virginia: damme! I never heard of that fellow before--he is\n"
            "some new painter, damme! that is the reason I did not know the hand. Not\n"
            "a word of what I told you, Lady Delacour--you won’t blow us to Clary,”\n"
            " added he aside to her ladyship. “Rochfort keeps aloof; and so will I,\n"
            "damme!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "clary.added" not in full_text

    def test_wrap_053_sensible_said(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: sensible.said
        passage = (
            "Mr. Vincent laughed, and protested that he should be very unwilling to\n"
            "give up his title to civilized society; and that, instead of wishing to\n"
            "have less knowledge, he regretted that he had not more. “I am sensible,”\n"
            " said he, “that I have many prejudices;--Miss Portman has made me ashamed\n"
            "of some of them.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sensible.said" not in full_text

    def test_wrap_054_passion_cried(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: passion.cried
        passage = (
            "“Then you do not know my character--you do not know my heart: it is in\n"
            "your power to make me exquisitely miserable. Mine is not the cold,\n"
            "hackneyed phrase of gallantry, but the fervid language of passion,”\n"
            " cried he, seizing her hand."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "passion.cried" not in full_text

    def test_wrap_055_unaffected_said(self):
        # Source: Tales and Novels Volume 03 Belinda, wrap corruption: unaffected.said
        passage = (
            "“He is very handsome, he is well bred, and his manners are unaffected,”\n"
            " said Belinda; “but--do not accuse me of caprice--altogether he does not\n"
            "suit my taste; and I cannot think it sufficient not to feel disgust for\n"
            "a husband--though I believe this is the fashionable doctrine.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "unaffected.said" not in full_text

