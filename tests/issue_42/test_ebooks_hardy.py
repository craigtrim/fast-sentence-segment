import pytest
from fast_sentence_segment import segment_text


class TestEbooksHardy:
    """Integration tests mined from Thomas Hardy ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1880s
    """

    def test_wrap_001_blest_for(self):
        # Source: A Changed Man and Other Tales, wrap corruption: blest.for
        passage = (
            "If hours be years the twain are blest,\n"
            "      For now they solace swift desire\n"
            "   By lifelong ties that tether zest\n"
            "      If hours be years.  The twain are blest\n"
            "   Do eastern suns slope never west,\n"
            "      Nor pallid ashes follow fire.\n"
            "   If hours be years the twain are blest\n"
            "      For now they solace swift desire."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "blest.for" not in full_text

    def test_wrap_002_have_resolved(self):
        # Source: A Changed Man and Other Tales, wrap corruption: have.resolved
        passage = (
            "DEAR JACK--I am unable to endure this life any longer, and I have\n"
            "   resolved to put an end to it.  I told you I should run away if you\n"
            "   persisted in being a clergyman, and now I am doing it.  One cannot\n"
            "   help one's nature.  I have resolved to throw in my lot with Mr.\n"
            "   Vannicock, and I hope rather than expect you will forgive me.--L."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "have.resolved" not in full_text

    def test_wrap_003_the_cause(self):
        # Source: A Changed Man and Other Tales, wrap corruption: the.cause
        passage = (
            "\"As one whose life has been devoted, and I may say sacrificed, to the\n"
            "   cause of Liberty, I cannot allow your judgment (probably a permanent\n"
            "   one) to be fettered beyond release by a feeling which may be transient\n"
            "   only."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.cause" not in full_text

    def test_wrap_004_announce_this(self):
        # Source: A Changed Man and Other Tales, wrap corruption: announce.this
        passage = (
            "\"It would be no less than excruciating to both that I should announce\n"
            "   this decision to you by word of mouth.  I have therefore taken the\n"
            "   less painful course of writing.  Before you receive this I shall have\n"
            "   left the town by the evening coach for London, on reaching which city\n"
            "   my movements will be revealed to none."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "announce.this" not in full_text

    def test_wrap_005_dinner_the(self):
        # Source: A Group of Noble Dames, wrap corruption: dinner.the
        passage = (
            "Preface\n"
            "Part I--Before Dinner\n"
            "   The First Countess of Wessex\n"
            "   Barbara of the House of Grebe\n"
            "   The Marchioness of Stonehenge\n"
            "   Lady Mottisfont\n"
            "Part II--After Dinner\n"
            "   The Lady Icenway\n"
            "   Squire Petrick's Lady\n"
            "   Anna, Lady Baxby\n"
            "   The Lady Penelope\n"
            "   The Duchess Of Hamptonshire\n"
            "   The Honourable Laura"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dinner.the" not in full_text

    def test_wrap_006_masquerade_but(self):
        # Source: A Laodicean a Story of to Day, wrap corruption: masquerade.but
        passage = (
            "‘“Doubtless it is a brilliant masquerade;\n"
            "       But when of the first sight you’ve had your fill,\n"
            "       It palls--at least it does so upon me,\n"
            "       This paradise of pleasure and ennui.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "masquerade.but" not in full_text

    def test_wrap_007_gaming_dressed(self):
        # Source: A Laodicean a Story of to Day, wrap corruption: gaming.dressed
        passage = (
            "“When we have made our love, and gamed our gaming,\n"
            "          Dressed, voted, shone, and maybe, something more;\n"
            "        With dandies dined, heard senators declaiming;\n"
            "          Seen beauties brought to market by the score,”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gaming.dressed" not in full_text

    def test_wrap_008_discontent_dear(self):
        # Source: A Laodicean a Story of to Day, wrap corruption: discontent.dear
        passage = (
            "“From one that dyeth in his discontent,\n"
            "      Dear Faire, receive this greeting to thee sent;\n"
            "      And still as oft as it is read by thee,\n"
            "      Then with some deep sad sigh remember mee!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "discontent.dear" not in full_text

    def test_wrap_009_camelionli_live(self):
        # Source: A Laodicean a Story of to Day, wrap corruption: camelionlike.live
        passage = (
            "How well could I with ayre, camelion-like,\n"
            "      Live happie, and still gazeing on thy cheeke,\n"
            "      In which, forsaken man, methink I see\n"
            "      How goodlie love doth threaten cares to mee."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "camelionlike.live" not in full_text

    def test_wrap_010_soule_whose(self):
        # Source: A Laodicean a Story of to Day, wrap corruption: soule.whose
        passage = (
            "Why dost thou frowne thus on a kneelinge soule,\n"
            "      Whose faults in love thou may’st as well controule?--\n"
            "      In love--but O, that word; that word I feare\n"
            "      Is hateful still both to thy hart and eare!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "soule.whose" not in full_text

    def test_wrap_011_intend_the(self):
        # Source: A Laodicean a Story of to Day, wrap corruption: intend.the
        passage = (
            "Ladie, in breefe, my fate doth now intend\n"
            "      The period of my daies to have an end:\n"
            "      Waste not on me thy pittie, pretious Faire:\n"
            "      Rest you in much content; I, in despaire!”’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "intend.the" not in full_text

    def test_wrap_012_hand_taking(self):
        # Source: A Laodicean a Story of to Day, wrap corruption: hand.taking
        passage = (
            "‘If I profane with my unworthy hand\n"
            "                                    (Taking her hand)\n"
            "      This holy shrine, the gentle fine is this--\n"
            "      My lips, two blushing pilgrims, ready stand\n"
            "      To smooth that rough touch with a tender kiss.’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hand.taking" not in full_text

    def test_wrap_013_steed_and(self):
        # Source: A Pair of Blue Eyes, wrap corruption: steed.and
        passage = (
            "‘I sat her on my pacing steed,\n"
            "    And nothing else saw all day long,\n"
            "For sidelong would she bend, and sing\n"
            "            A fairy’s song,\n"
            "She found me roots of relish sweet,\n"
            "And honey wild, and manna dew;’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "steed.and" not in full_text

    def test_wrap_014_and_smiled(self):
        # Source: Desperate Remedies, wrap corruption: and.smiled
        passage = (
            "During pleasant doubt, when her eyes brightened stealthily and\n"
            "  smiled (as eyes will smile) as distinctly as her lips, and in the\n"
            "  space of a single instant expressed clearly the whole round of\n"
            "  degrees of expectancy which lie over the wide expanse between Yea\n"
            "  and Nay."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.smiled" not in full_text

    def test_wrap_015_involuntar_accompanie(self):
        # Source: Desperate Remedies, wrap corruption: involuntarily.accompanied
        passage = (
            "During the telling of a secret, which was involuntarily\n"
            "  accompanied by a sudden minute start, and ecstatic pressure of\n"
            "  the listener’s arm, side, or neck, as the position and degree\n"
            "  of intimacy dictated."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "involuntarily.accompanied" not in full_text

    def test_wrap_016_had_been(self):
        # Source: Desperate Remedies, wrap corruption: had.been
        passage = (
            "First, that their father’s income from professional sources had\n"
            "  been very small, amounting to not more than half their expenditure;\n"
            "  and that his own and his wife’s property, upon which he had relied\n"
            "  for the balance, had been sunk and lost in unwise loans to\n"
            "  unscrupulous men, who had traded upon their father’s too\n"
            "  open-hearted trustfulness."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "had.been" not in full_text

    def test_wrap_017_had_awakened(self):
        # Source: Desperate Remedies, wrap corruption: had.awakened
        passage = (
            "Fourth, that the loss of his wife two years earlier had\n"
            "  awakened him to a keen sense of his blindness, and of his duty by\n"
            "  his children. He had then resolved to reinstate by unflagging zeal\n"
            "  in the pursuit of his profession, and by no speculation, at least a\n"
            "  portion of the little fortune he had let go."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "had.awakened" not in full_text

    def test_wrap_018_mine_father(self):
        # Source: Desperate Remedies, wrap corruption: mine.father
        passage = (
            "‘I remember what he said once,’ returned the brother, ‘when I sat up\n"
            "late with him. He said, “Owen, don’t love too blindly: blindly you\n"
            "will love if you love at all, but a little care is still possible to\n"
            "a well-disciplined heart. May that heart be yours as it was not mine,”\n"
            " father said. “Cultivate the art of renunciation.” And I am going to,\n"
            "Cytherea.’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mine.father" not in full_text

    def test_wrap_019_same_and(self):
        # Source: Desperate Remedies, wrap corruption: same.and
        passage = (
            "‘Yes, one will occur often enough--that is, two disconnected events will\n"
            "fall strangely together by chance, and people scarcely notice the fact\n"
            "beyond saying, “Oddly enough it happened that so and so were the same,”\n"
            " and so on. But when three such events coincide without any apparent\n"
            "reason for the coincidence, it seems as if there must be invisible means\n"
            "at work. You see, three things falling together in that manner are ten\n"
            "times as singular as two cases of coincidence which are distinct.’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "same.and" not in full_text

    def test_wrap_020_streams_with(self):
        # Source: Desperate Remedies, wrap corruption: streams.with
        passage = (
            "‘Like some fair tree which, fed by streams,\n"
            "       With timely fruit doth bend,\n"
            "     He still shall flourish, and success\n"
            "       All his designs attend.’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "streams.with" not in full_text

    def test_wrap_021_her_whose(self):
        # Source: Desperate Remedies, wrap corruption: her.whose
        passage = (
            "‘O, what hast thou of her, of her\n"
            "     Whose every look did love inspire;\n"
            "     Whose every breathing fanned my fire,\n"
            "     And stole me from myself away!’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "her.whose" not in full_text

    def test_wrap_022_round_some(self):
        # Source: Desperate Remedies, wrap corruption: round.some
        passage = (
            "‘He, like a captain who beleaguers round\n"
            "      Some strong-built castle on a rising ground,\n"
            "      Views all the approaches with observing eyes,\n"
            "      This and that other part again he tries,\n"
            "      And more on industry than force relies.’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "round.some" not in full_text

    def test_wrap_023_days_shall(self):
        # Source: Desperate Remedies, wrap corruption: days.shall
        passage = (
            "‘Whoso for hours or lengthy days\n"
            "           Shall catch her aspect’s changeful rays,\n"
            "           Then turn away, can none recall\n"
            "           Beyond a galaxy of all\n"
            "               In hazy portraiture;\n"
            "           Lit by the light of azure eyes\n"
            "           Like summer days by summer skies:\n"
            "           Her sweet transitions seem to be\n"
            "           A kind of pictured melody,\n"
            "               And not a set contour."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "days.shall" not in full_text

    def test_wrap_024_wall_said(self):
        # Source: Desperate Remedies, wrap corruption: wall.said
        passage = (
            "‘He flung his mallet against the wall,\n"
            "           Said, “The Lord make churches and chapels to fall,\n"
            "           And there’ll be work for tradesmen all!”\n"
            "                When Joan’s ale was new,\n"
            "                               My boys,\n"
            "               When Joan’s ale was new.’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "wall.said" not in full_text

    def test_wrap_025_love_iit(self):
        # Source: Far From the Madding Crowd, wrap corruption: love.iit
        passage = (
            "I sow′-ed th′-e.....\n"
            "I sow′-ed.....\n"
            "I sow′-ed th′-e seeds′ of′ love′,\n"
            "    I-it was′ all′ i′-in the′-e spring′,\n"
            "I-in A′-pril′, Ma′-ay, a′-nd sun′-ny′ June′,\n"
            "    When sma′-all bi′-irds they′ do′ sing."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "love.iit" not in full_text

    def test_wrap_026_board_with(self):
        # Source: Far From the Madding Crowd, wrap corruption: board.with
        passage = (
            "To-mor-row, to-mor-row!\n"
            "And while peace and plen-ty I find at my board,\n"
            "    With a heart free from sick-ness and sor-row,\n"
            "With my friends will I share what to-day may af-ford,\n"
            "    And let them spread the ta-ble to-mor-row.\n"
            "        To-mor-row, to-mor——"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "board.with" not in full_text

    def test_wrap_027_again_chapter(self):
        # Source: Jude the Obscure, wrap corruption: again.chapter
        passage = (
            "PART SIXTH—At Christminster Again\n"
            " Chapter I\n"
            " Chapter II\n"
            " Chapter III\n"
            " Chapter IV\n"
            " Chapter V\n"
            " Chapter VI\n"
            " Chapter VII\n"
            " Chapter VIII\n"
            " Chapter IX\n"
            " Chapter X\n"
            " Chapter XI"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "again.chapter" not in full_text

    def test_wrap_028_all_now(self):
        # Source: Jude the Obscure, wrap corruption: all.now
        passage = (
            "It is as I told you; and I am leaving to-morrow evening. Richard and I\n"
            "thought it could be done with less obtrusiveness after dark. I feel\n"
            "rather frightened, and therefore ask you to be sure you are on the\n"
            "Melchester platform to meet me. I arrive at a little to seven. I know\n"
            "you will, of course, dear Jude; but I feel so timid that I can’t help\n"
            "begging you to be punctual. He has been so very kind to me through it\n"
            "all!\n"
            "    Now to our meeting!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.now" not in full_text

    def test_wrap_029_likes_and(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: likes.and
        passage = (
            "THIS is the weather the cuckoo likes,\n"
            "      And so do I;\n"
            "   When showers betumble the chestnut spikes,\n"
            "      And nestlings fly:\n"
            "   And the little brown nightingale bills his best,\n"
            "   And they sit outside at “The Travellers’ Rest,”\n"
            "   And maids come forth sprig-muslin drest,\n"
            "   And citizens dream of the south and west,\n"
            "      And so do I."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "likes.and" not in full_text

    def test_wrap_030_shuns_and(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: shuns.and
        passage = (
            "This is the weather the shepherd shuns,\n"
            "      And so do I;\n"
            "   When beeches drip in browns and duns,\n"
            "      And thresh, and ply;\n"
            "   And hill-hid tides throb, throe on throe,\n"
            "   And meadow rivulets overflow,\n"
            "   And drops on gate-bars hang in a row,\n"
            "   And rooks in families homeward go,\n"
            "      And so do I."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shuns.and" not in full_text

    def test_wrap_031_gown_from(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: gown.from
        passage = (
            "Rose-necked, in sky-gray gown,\n"
            "   From a stage in Stower Town\n"
            "   Did she sing, and singing smile\n"
            "   As she blent that dexterous voice\n"
            "   With the ditty of her choice,\n"
            "   And banished our annoys\n"
            "      Thereawhile."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gown.from" not in full_text

    def test_wrap_032_now_timetrench(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: now.timetrenched
        passage = (
            "Ah, she’s a beldame now,\n"
            "   Time-trenched on cheek and brow,\n"
            "   Whom I once heard as a maid\n"
            "   From Keinton Mandeville\n"
            "   Of matchless scope and skill\n"
            "   Sing, with smile and swell and trill,\n"
            "      “Should he upbraid!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "now.timetrenched" not in full_text

    def test_wrap_033_again_calls(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: again.calls
        passage = (
            "WHEN friendly summer calls again,\n"
            "         Calls again\n"
            "   Her little fifers to these hills,\n"
            "   We’ll go—we two—to that arched fane\n"
            "   Of leafage where they prime their bills\n"
            "   Before they start to flood the plain\n"
            "   With quavers, minims, shakes, and trills.\n"
            "      “—We’ll go,” I sing; but who shall say\n"
            "      What may not chance before that day!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "again.calls" not in full_text

    def test_wrap_034_spring_waters(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: spring.waters
        passage = (
            "And we shall see the waters spring,\n"
            "         Waters spring\n"
            "   From chinks the scrubby copses crown;\n"
            "   And we shall trace their oncreeping\n"
            "   To where the cascade tumbles down\n"
            "   And sends the bobbing growths aswing,\n"
            "   And ferns not quite but almost drown.\n"
            "      “—We shall,” I say; but who may sing\n"
            "      Of what another moon will bring!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "spring.waters" not in full_text

    def test_wrap_035_peep_where(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: peep.where
        passage = (
            "PAST the hills that peep\n"
            "   Where the leaze is smiling,\n"
            "   On and on beguiling\n"
            "   Crisply-cropping sheep;\n"
            "   Under boughs of brushwood\n"
            "   Linking tree and tree\n"
            "   In a shade of lushwood,\n"
            "      There caressed we!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "peep.where" not in full_text

    def test_wrap_036_walls_that(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: walls.that
        passage = (
            "Hemmed by city walls\n"
            "   That outshut the sunlight,\n"
            "   In a foggy dun light,\n"
            "   Where the footstep falls\n"
            "   With a pit-pat wearisome\n"
            "   In its cadency\n"
            "   On the flagstones drearisome\n"
            "      There pressed we!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "walls.that" not in full_text

    def test_wrap_037_crowds_blown(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: crowds.blown
        passage = (
            "Where in wild-winged crowds\n"
            "   Blown birds show their whiteness\n"
            "   Up against the lightness\n"
            "   Of the clammy clouds;\n"
            "   By the random river\n"
            "   Pushing to the sea,\n"
            "   Under bents that quiver\n"
            "      There rest we."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "crowds.blown" not in full_text

    def test_wrap_038_know_your(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: know.your
        passage = (
            "How well I know\n"
            "      Your furtive feminine shape!\n"
            "   As if reluctantly you show\n"
            "      You nude of cloud, and but by favour throw\n"
            "         Aside its drape . . ."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "know.your" not in full_text

    def test_wrap_039_black_those(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: black.those
        passage = (
            "At night when reddest flowers are black\n"
            "   Those who once sat thereon come back;\n"
            "   Quite a row of them sitting there,\n"
            "   Quite a row of them sitting there."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "black.those" not in full_text

    def test_wrap_040_down_nor(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: down.nor
        passage = (
            "With them the seat does not break down,\n"
            "   Nor winter freeze them, nor floods drown,\n"
            "   For they are as light as upper air,\n"
            "   They are as light as upper air!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "down.nor" not in full_text

    def test_wrap_041_one_who(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: one.who
        passage = (
            "It lit his face—the weary face of one\n"
            "   Who in the adjacent gardens charged his string,\n"
            "   Nightly, with many a tuneful tender thing,\n"
            "   Till stars were weak, and dancing hours outrun."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "one.who" not in full_text

    def test_wrap_042_day_when(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: day.when
        passage = (
            "DID they catch as it were in a Vision at shut of the day—\n"
            "   When their cavalry smote through the ancient Esdraelon Plain,\n"
            "   And they crossed where the Tishbite stood forth in his enemy’s way—\n"
            "   His gaunt mournful Shade as he bade the King haste off amain?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "day.when" not in full_text

    def test_wrap_043_eyes_who(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: eyes.who
        passage = (
            "On war-men at this end of time—even on Englishmen’s eyes—\n"
            "   Who slay with their arms of new might in that long-ago place,\n"
            "   Flashed he who drove furiously? . . . Ah, did the phantom arise\n"
            "   Of that queen, of that proud Tyrian woman who painted her face?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "eyes.who" not in full_text

    def test_wrap_044_night_eerily(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: night.eerily
        passage = (
            "Faintly marked they the words “Throw her down!” rise from Night\n"
            "   eerily,\n"
            "   Spectre-spots of the blood of her body on some rotten wall?\n"
            "   And the thin note of pity that came: “A King’s daughter is she,”\n"
            "   As they passed where she trodden was once by the chargers’ footfall?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "night.eerily" not in full_text

    def test_wrap_045_style_had(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: style.had
        passage = (
            "Trite usages in tamest style\n"
            "         Had tended to their plighting.\n"
            "            “It’s just worth while,\n"
            "   Perhaps,” they had said.  “And saves much sad good-nighting.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "style.had" not in full_text

    def test_wrap_046_happenings_that(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: happenings.that
        passage = (
            "And petty seemed the happenings\n"
            "         That ministered to their joyance:\n"
            "            Simple things,\n"
            "   Onerous to satiate souls, increased their buoyance."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "happenings.that" not in full_text

    def test_wrap_047_drawn_and(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: drawn.and
        passage = (
            "THE curtains now are drawn,\n"
            "      And the spindrift strikes the glass,\n"
            "      Blown up the jagged pass\n"
            "      By the surly salt sou’-west,\n"
            "      And the sneering glare is gone\n"
            "      Behind the yonder crest,\n"
            "         While she sings to me:\n"
            "   “O the dream that thou art my Love, be it thine,\n"
            "   And the dream that I am thy Love, be it mine,\n"
            "   And death may come, but loving is divine.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "drawn.and" not in full_text

    def test_wrap_048_rain_with(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: rain.with
        passage = (
            "I stand here in the rain,\n"
            "      With its smite upon her stone,\n"
            "      And the grasses that have grown\n"
            "      Over women, children, men,\n"
            "      And their texts that “Life is vain”;\n"
            "      But I hear the notes as when\n"
            "         Once she sang to me:\n"
            "   “O the dream that thou art my Love, be it thine,\n"
            "   And the dream that I am thy Love, be it mine,\n"
            "   And death may come, but loving is divine.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rain.with" not in full_text

    def test_wrap_049_change_this(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: change.this
        passage = (
            "Peace, this hid riot, Change,\n"
            "      This revel of quick-cued mumming,\n"
            "      This never truly being,\n"
            "      This evermore becoming,\n"
            "      This spinner’s wheel onfleeing\n"
            "   Outside perception’s range."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "change.this" not in full_text

    def test_wrap_050_man_who(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: man.who
        passage = (
            "I WAS not he—the man\n"
            "   Who used to pilgrim to your gate,\n"
            "   At whose smart step you grew elate,\n"
            "      And rosed, as maidens can,\n"
            "         For a brief span."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "man.who" not in full_text

    def test_wrap_051_sang_beside(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: sang.beside
        passage = (
            "It was not I who sang\n"
            "   Beside the keys you touched so true\n"
            "   With note-bent eyes, as if with you\n"
            "      It counted not whence sprang\n"
            "         The voice that rang . . ."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sang.beside" not in full_text

    def test_wrap_052_girl_when(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: girl.when
        passage = (
            "Yet now my West-of-Wessex girl,\n"
            "      When midnight hammers slow\n"
            "      From Andrew’s, blow by blow,\n"
            "   As phantom draws me by the hand\n"
            "      To the place—Plymouth Hoe—\n"
            "   Where side by side in life, as planned,\n"
            "      We never were to go!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "girl.when" not in full_text

    def test_wrap_053_place_bent(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: place.bent
        passage = (
            "TO my native place\n"
            "      Bent upon returning,\n"
            "      Bosom all day burning\n"
            "      To be where my race\n"
            "   Well were known, ’twas much with me\n"
            "   There to dwell in amity."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "place.bent" not in full_text

    def test_wrap_054_beds_but(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: beds.but
        passage = (
            "Folk had sought their beds,\n"
            "      But I hailed: to view me\n"
            "      Under the moon, out to me\n"
            "      Several pushed their heads,\n"
            "   And to each I told my name,\n"
            "   Plans, and that therefrom I came."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "beds.but" not in full_text

    def test_wrap_055_spray_the(self):
        # Source: Late Lyrics and Earlier With Many Other Verses, wrap corruption: spray.the
        passage = (
            "THE moving sun-shapes on the spray,\n"
            "   The sparkles where the brook was flowing,\n"
            "   Pink faces, plightings, moonlit May,\n"
            "   These were the things we wished would stay;\n"
            "      But they were going."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "spray.the" not in full_text

