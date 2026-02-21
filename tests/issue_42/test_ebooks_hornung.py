import pytest
from fast_sentence_segment import segment_text


class TestEbooksHornung:
    """Integration tests mined from E. W. Hornung ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1900s
    """

    def test_wrap_001_dove_far(self):
        # Source: A Bride From the Bush, wrap corruption: dove.far
        passage = (
            "O for the wings, for the wings of a dove!\n"
            "    Far away, far away would I rove:\n"
            "    In the wilderness build me a nest,\n"
            "    And remain there for ever at rest."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dove.far" not in full_text

    def test_wrap_002_been_committed(self):
        # Source: A Thief in the Night Further Adventures of a J Raffles Cricketer and Cracksman, wrap corruption: been.committed
        passage = (
            "An audacious burglary and dastardly assault have been\n"
            "     committed on the premises of the City and Suburban Bank in\n"
            "     Sloane Street, W. From the details so far to hand, the\n"
            "     robbery appears to have been deliberately planned and\n"
            "     adroitly executed in the early hours of this morning."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "been.committed" not in full_text

    def test_wrap_003_and_two(self):
        # Source: A Thief in the Night Further Adventures of a J Raffles Cricketer and Cracksman, wrap corruption: and.two
        passage = (
            "A night watchman named Fawcett states that between one and\n"
            "     two o'clock he heard a slight noise in the neighborhood of\n"
            "     the lower strong-room, used as a repository for the plate\n"
            "     and other possessions of various customers of the bank.\n"
            "     Going down to investigate, he was instantly attacked by a\n"
            "     powerful ruffian, who succeeded in felling him to the ground\n"
            "     before an alarm could be raised."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.two" not in full_text

    def test_wrap_004_philippi_was(self):
        # Source: A Thief in the Night Further Adventures of a J Raffles Cricketer and Cracksman, wrap corruption: philippi.was
        passage = (
            "\"'And I think that the field of Philippi\n"
            "       Was where Caesar came to an end;\n"
            "      But who gave old Brutus the tip, I\n"
            "           Can't comprehend!'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "philippi.was" not in full_text

    def test_wrap_005_quietly_because(self):
        # Source: A Thief in the Night Further Adventures of a J Raffles Cricketer and Cracksman, wrap corruption: quietly.because
        passage = (
            "\"'Because I was the other man,' he said quite quietly;\n"
            "    'because I led him blindfold into the whole business, and\n"
            "    would rather pay the shot than see poor Bunny suffer for it.'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "quietly.because" not in full_text

    def test_wrap_006_never_accurate(self):
        # Source: At Large, wrap corruption: never.accurate
        passage = (
            "\"Dear Biggs,--A false scent, I am afraid. Ladies are never\n"
            "    accurate; you have been misinformed about Miles. I knew him\n"
            "    in Australia! He cannot be the man you want.--Yours\n"
            "    sincerely,\n"
            "                                                \"R. Edmonstone.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "never.accurate" not in full_text

    def test_wrap_007_tree_lines(self):
        # Source: At Large, wrap corruption: tree.lines
        passage = (
            "Falling leaf and fading tree,\n"
            "        Lines of white in a sullen sea,\n"
            "        Shadows rising on you and me;\n"
            "        The swallows are making them ready to fly,\n"
            "        Wheeling out on a windy sky.\n"
            "        Good-bye, summer! good-bye, good-bye!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tree.lines" not in full_text

    def test_wrap_008_aquarum_jam(self):
        # Source: Dead Men Tell No Tales, wrap corruption: aquarum.jam
        passage = (
            "Me miserum, quanti montes volvuntur aquarum!\n"
            "   Jam jam tacturos sidera summa putes.\n"
            "   Quantae diducto subsidunt aequore valles!\n"
            "   Jam jam tacturas Tartara nigra putes.\n"
            "   Quocunque adspicio, nihil est nisi pontus et aether;\n"
            "   Fluctibus hic tumidis, nubibus ille minax...."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "aquarum.jam" not in full_text

    def test_wrap_009_this_said(self):
        # Source: Dead Men Tell No Tales, wrap corruption: this.said
        passage = (
            "“How on earth did you come to hear of a God-forsaken place like this?”\n"
            " said he, making use, I thought, of a somewhat stronger expression than\n"
            "quite became his cloth."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "this.said" not in full_text

    def test_wrap_010_yarn_which(self):
        # Source: Dead Men Tell No Tales, wrap corruption: yarn.which
        passage = (
            "“A good soul, Jane,” said he; “though she made an idiotic marriage, and\n"
            "leads a life which might spoil the temper of an archangel. She was my\n"
            "nurse when I was a youngster, Cole, and we never meet without a yarn.”\n"
            " Which seemed natural enough; still I failed to perceive why they need\n"
            "yarn in whispers."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "yarn.which" not in full_text

    def test_wrap_011_dead_remember(self):
        # Source: Dead Men Tell No Tales, wrap corruption: dead.remember
        passage = (
            "“But you acted it, and I've a jolly good mind to shoot you dead!”\n"
            " (Remember, I was so weak myself that I thought my arm would break from\n"
            "presenting my five chambers and my ten-inch barrel; otherwise I should\n"
            "be sorry to relate how I bullied that mouse of a man.) “I may let you\n"
            "off,” I continued, “if you answer questions. Where's your wife?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dead.remember" not in full_text

    def test_wrap_012_morning_concluded(self):
        # Source: Dead Men Tell No Tales, wrap corruption: morning.concluded
        passage = (
            "“Say nothing till it's found out; then lie for their lives; and it was\n"
            "their lives, poor creatures on the Zambesi!” She was silent a moment,\n"
            "her determined little face hard--set upon some unforgotten horror.\n"
            "“Once we get away, I shall be surprised if it's found out till morning,”\n"
            " concluded Eva, without a word as to what I was to do with her; neither,\n"
            "indeed, had I myself given that question a moment's consideration."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "morning.concluded" not in full_text

    def test_wrap_013_him_she(self):
        # Source: Dead Men Tell No Tales, wrap corruption: him.she
        passage = (
            "“Should I?” she asked half eagerly, as she looked quickly round at me;\n"
            "and suddenly I saw her eyes fill. “Oh, why will you speak about him?”\n"
            " she burst out. “Why must you defend him, unless it's to go against me,\n"
            "as you always did and always will! I never knew anybody like you--never!\n"
            "I want you to take me away from these wretches, and all you do is to\n"
            "defend them!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "him.she" not in full_text

    def test_wrap_014_life_and(self):
        # Source: Dead Men Tell No Tales, wrap corruption: life.and
        passage = (
            "“I wish it was,” said I; “but I can't complain; it's saved my life.”\n"
            " And I looked at Santos, standing dignified and alert, my still smoking\n"
            "pistol in his hand."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "life.and" not in full_text

    def test_wrap_015_the_upper(self):
        # Source: Fathers of Men, wrap corruption: the.upper
        passage = (
            "“When 'tis joy on one’s rug to be basking, and watching a match on the\n"
            "   Upper,\n"
            " When the works of J. Lillywhite, junior, rank higher than those of one\n"
            "    Tupper——”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.upper" not in full_text

    def test_wrap_016_coat_lardydah(self):
        # Source: Fathers of Men, wrap corruption: coat.lardydah
        passage = (
            "“He wears a penny flower in his coat—\n"
            "                Lardy-dah—\n"
            "               And a penny paper collar round his throat—\n"
            "                Lardy-dah—\n"
            "               In his hand a penny stick,\n"
            "               In his tooth a penny pick,\n"
            "               And a penny in his pocket—\n"
            "                Lardy-dah—lardy-dah—\n"
            "               And a penny in his pocket—\n"
            "                Lardy-dah!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "coat.lardydah" not in full_text

    def test_wrap_017_done_you(self):
        # Source: Fathers of Men, wrap corruption: done.you
        passage = (
            "“But 'tis no use lamenting. What is done\n"
            "                   You couldn’t undo if you tried....\n"
            "                 O, if only they’d set us some Wisden,\n"
            "                           Or Lillywhite’s Guide!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "done.you" not in full_text

    def test_wrap_018_dead_they(self):
        # Source: Fathers of Men, wrap corruption: dead.they
        passage = (
            "“They told me, Heraclitus, they told me you were dead,\n"
            "      They brought me bitter news to hear and bitter tears to shed.\n"
            "      I wept, as I remembered, how often you and I\n"
            "      Had tired the sun with talking and sent him down the sky.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dead.they" not in full_text

    def test_wrap_019_peers_and(self):
        # Source: Fathers of Men, wrap corruption: peers.and
        passage = (
            "“There courteous strivings with my peers,\n"
            "                  And duties not bound up in books,\n"
            "                And courage fanned by stormy cheers,\n"
            "                  And wisdom writ in pleasant looks,\n"
            "                And hardship buoyed with hope, and pain\n"
            "                  Encountered for the common weal,\n"
            "                And glories void of vulgar gain,\n"
            "                  Were mine to take, were mine to feel.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "peers.and" not in full_text

    def test_wrap_020_said_what(self):
        # Source: Fathers of Men, wrap corruption: said.what
        passage = (
            "“And to myself in games I said,\n"
            "                 'What mean the books? Can I win fame?\n"
            "               I would be like the faithful dead\n"
            "                 A fearless man, and pure of blame.\n"
            "               I may have failed, my School may fail;\n"
            "                 I tremble, but thus much I dare;\n"
            "               I love her. Let the critics rail,\n"
            "                 My brethren and my home are there.’”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "said.what" not in full_text

    def test_wrap_021_not_when(self):
        # Source: Fathers of Men, wrap corruption: not.when
        passage = (
            "“I go, and men who know me not,\n"
            "                 When I am reckoned man, will ask,\n"
            "               'What is it then that thou hast got\n"
            "                 By drudging through that five-year task?\n"
            "               What knowledge or what art is thine?\n"
            "                 Set out thy stock, thy craft declare.’\n"
            "               Then this child-answer shall be mine,\n"
            "                 'I only know they loved me there.’”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "not.when" not in full_text

    def test_wrap_022_you_from(self):
        # Source: My Lord Duke, wrap corruption: you.from
        passage = (
            "\"What garlands can I bring you\n"
            "      From Fancy's fairest dell?\n"
            "    Before the world grew old, dear,\n"
            "      The lute was lightlier strung;\n"
            "    Now all the tales are told, dear,\n"
            "      And all the songs are sung.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.from" not in full_text

    def test_wrap_023_please_right(self):
        # Source: No Hero, wrap corruption: please.right
        passage = (
            "\"If doughty deeds my lady please,\n"
            "    Right soon I'll mount my steed;\n"
            "  And strong his arm, and fast his seat,\n"
            "    That bears frae me the meed.\n"
            "  I'll wear thy colours in my cap,\n"
            "    Thy picture at my heart;\n"
            "  And he that bends not to thine eye\n"
            "    Shall rue it to his smart!\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "please.right" not in full_text

    def test_wrap_024_see_what(self):
        # Source: No Hero, wrap corruption: see.what
        passage = (
            "\"And I,--what I seem to my friend, you see:\n"
            "    What I soon shall seem to his love, you guess:\n"
            "  What I seem to myself, do you ask of me?\n"
            "    No hero, I confess.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "see.what" not in full_text

    def test_wrap_025_supply_the(self):
        # Source: Notes of a Camp Follower on the Western Front, wrap corruption: supply.the
        passage = (
            "'DEAR SIRS,--I will be much obliged if you will supply\n"
            "      the bearer with hot cocoa (sufficient for 90 men)\n"
            "      which I understand you are good enough to issue to\n"
            "      units in this line. The party are taking 2 hot-food\n"
            "      containers for the purpose."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "supply.the" not in full_text

    def test_wrap_026_duncan_morris(self):
        # Source: Notes of a Camp Follower on the Western Front, wrap corruption: duncan.morris
        passage = (
            "'P.S.--Lochie Rob, J. Small, Philip Clyne, Duncan\n"
            "      Morris, Headly, wee Mac, Ginger Wilson, Macrae and\n"
            "      Dean Swift are killed. There are just three of us left\n"
            "      in the section now, that is, Gordon, Black, and\n"
            "      Martin, the rest drafted."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "duncan.morris" not in full_text

    def test_wrap_027_loved_honoured(self):
        # Source: Notes of a Camp Follower on the Western Front, wrap corruption: loved.honoured
        passage = (
            "He was liked by his fellow-officers, but he was loved,\n"
            "      honoured and respected by his men, and you know, Sir,\n"
            "      that _I am not guilty of paying tributes to anyone\n"
            "      where they are not deserved_....'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "loved.honoured" not in full_text

    def test_wrap_028_each_others(self):
        # Source: Notes of a Camp Follower on the Western Front, wrap corruption: each.others
        passage = (
            "_A book may be kept as long as required: but in each\n"
            "      other's interests Readers are begged to return all\n"
            "      books as soon as they conveniently can, and in as good\n"
            "      order as possible._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "each.others" not in full_text

    def test_wrap_029_graces_but(self):
        # Source: Notes of a Camp Follower on the Western Front, wrap corruption: graces.but
        passage = (
            "Not for Prophecies or Powers, Visions, Gifts or Graces,\n"
            "    But the unrelenting hours that grind us in our places,\n"
            "    With the burden on our backs, the smile upon our faces."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "graces.but" not in full_text

    def test_wrap_030_fishes_but(self):
        # Source: Notes of a Camp Follower on the Western Front, wrap corruption: fishes.but
        passage = (
            "Not for any miracle of easy loaves and fishes,\n"
            "    But for work against our will and waiting 'gainst our wishes--\n"
            "    Such as gathering up the crumbs and cleaning dirty dishes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fishes.but" not in full_text

    def test_wrap_031_soul_let(self):
        # Source: Peccavi, wrap corruption: soul.let
        passage = (
            "\"Jesu, Lover of my soul,\n"
            "      Let me to Thy Bosom fly,\n"
            "    While the gathering waters roll,\n"
            "      While the tempest still is high:\n"
            "    Hide me, O my Saviour, hide,\n"
            "      Till the storm of life is past:\n"
            "    Safe into the haven guide,\n"
            "      O receive my soul at last . . .\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "soul.let" not in full_text

    def test_wrap_032_heaven_here(self):
        # Source: Peccavi, wrap corruption: heaven.here
        passage = (
            "\"My brethren, you need be no farther from heaven,\n"
            "      here in this place, unfinished as it is, than when the\n"
            "      roof is up, and the windows are in, and proper seats,\n"
            "      and when a new organ peals . . . and one whom you can\n"
            "      respect stands where I am standing now . . ."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "heaven.here" not in full_text

    def test_wrap_033_god_sits(self):
        # Source: Peccavi, wrap corruption: god.sits
        passage = (
            "\"And remember--never, never forget--that a just God\n"
            "      sits in yonder blue heaven above us--that He is not\n"
            "      hard--that I told you . . . He is merciful . . .\n"
            "      merciful . . . merciful . . ."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "god.sits" not in full_text

    def test_wrap_034_again_how(self):
        # Source: Peccavi, wrap corruption: again.how
        passage = (
            "\"O look above once more before we part, and see again\n"
            "      how '_The heavens declare the glory of God; and the\n"
            "      firmament sheweth his handywork_.'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "again.how" not in full_text

    def test_wrap_035_the_holy(self):
        # Source: Peccavi, wrap corruption: the.holy
        passage = (
            "\"And now to God the Father, God the Son, and God the\n"
            "      Holy Ghost, be ascribed all honour, power, dominion,\n"
            "      might, henceforth and for ever. Amen.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.holy" not in full_text

    def test_wrap_036_parete_era(self):
        # Source: Raffles Further Adventures of the Amateur Cracksman, wrap corruption: parete.era
        passage = (
            "“Margarita de Parete,\n"
            "    era a’ sarta d’ e’ signore;\n"
            "    se pugneva sempe e ddete\n"
            "    pe penzare a Salvatore!\n"
            "“Mar—ga—rì,\n"
            "    e perzo e Salvatore!\n"
            "Mar—ga—rì,\n"
            "    Ma l’ommo è cacciatore!\n"
            "Mar—ga—rì,\n"
            "    Nun ce aje corpa tu!\n"
            "Chello ch’ è fatto, è fatto, un ne parlammo cchieù!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "parete.era" not in full_text

    def test_wrap_037_swore_hops(self):
        # Source: Some Persons Unknown, wrap corruption: swore.hops
        passage = (
            "\"Who is this?\" King Willow he swore,\n"
            "  \"Hops like that to a gentleman's door?\n"
            "  Who's afraid of a Duke like him?\n"
            "  Fiddlededee!\" says the monarch slim.\n"
            "  \"What do you say, my courtiers three?\"\n"
            "  And the courtiers all said \"Fiddlededee!\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "swore.hops" not in full_text

    def test_wrap_038_say_will(self):
        # Source: The Boss of Taroomba, wrap corruption: say.will
        passage = (
            "Oh, walk up, Mr. Pompey, oh, walk up while I say,\n"
            "     Will you walk into the banjo and hear the parlor play?\n"
            "     Will you walk into the parlor and hear the banjo ring?\n"
            "     Oh, listen to de darkies how merrily dey sing!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "say.will" not in full_text

    def test_wrap_039_hear_let(self):
        # Source: The Boss of Taroomba, wrap corruption: hear.let
        passage = (
            "\"Let us go hence, my songs; she will not hear.\n"
            "     Let us go hence together without fear;\n"
            "     Keep silence now, for singing-time is over,\n"
            "     And over all old things and all things dear.\n"
            "     She loves not you nor me as all we love her.\n"
            "     Yea, though we sang as angels in her ear,\n"
            "                 She would not hear."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hear.let" not in full_text

    def test_wrap_040_know_let(self):
        # Source: The Boss of Taroomba, wrap corruption: know.let
        passage = (
            "\"Let us rise up and part; she will not know.\n"
            "     Let us go seaward as the great winds go,\n"
            "     Full of blown sand and foam; what help is there?\n"
            "     There is no help, for all these things are so,\n"
            "     And all the world is bitter as a tear.\n"
            "     And how these things are, though ye strove to show\n"
            "                 She would not know."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "know.let" not in full_text

    def test_wrap_041_maid_yoho(self):
        # Source: The Boss of Taroomba, wrap corruption: maid.yoho
        passage = (
            "Oh, where are you going to, my pretty maid?--\n"
            "       Yo-ho, blow the land down!\n"
            "     Oh, where are you going to, my pretty maid?--\n"
            "       And give us some time to blow the land down!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "maid.yoho" not in full_text

    def test_wrap_042_already_one(self):
        # Source: The Camera Fiend, wrap corruption: already.one
        passage = (
            "The time-table of that boy’s day must speak for itself. It was already\n"
            " one o’clock, and he was naturally hungry, especially after the way his\n"
            " breakfast had been spoilt by Coverley’s card. At 1.15 he was munching\n"
            " a sausage roll and sipping chocolate at a pastry-cook’s in Oxford\n"
            " Street. The sausage roll, like the cup of chocolate, was soon followed\n"
            " by another; and a big Bath bun completed a debauch of which Dr. Bompas\n"
            " would undoubtedly have disapproved."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "already.one" not in full_text

    def test_wrap_043_novel_that(self):
        # Source: The Shadow of a Man, wrap corruption: novel.that
        passage = (
            "\"'Peccavi' is at once the most serious and the strongest novel\n"
            "    that has issued from Mr. Hornung's engaging pen.... A striking\n"
            "    and admirable story.\"--The Spectator."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "novel.that" not in full_text

    def test_wrap_044_figure_standing(self):
        # Source: The Shadow of a Man, wrap corruption: figure.standing
        passage = (
            "\"It must be said that the erring parson is a fine figure,\n"
            "    standing aloof, yet never passive in his awful solitude. He\n"
            "    works out a grand and unselfish salvation in an heroic\n"
            "    way.\"--The Athenæum."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "figure.standing" not in full_text

    def test_wrap_045_novels_describes(self):
        # Source: The Shadow of a Man, wrap corruption: novels.describes
        passage = (
            "\"One of the strongest and most touching of recent novels.\n"
            "    Describes the moral fall of an English clergyman and his\n"
            "    strange, brave, victorious struggle to win back public respect\n"
            "    and confidence.\"--The Congregationalist."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "novels.describes" not in full_text

    def test_wrap_046_burglarian_exploits(self):
        # Source: The Shadow of a Man, wrap corruption: burglarian.exploits
        passage = (
            "\"For sheer excitement and inventive genius the burglarian\n"
            "    exploits of 'The Amateur Cracksman' carry off the palm. Raffles\n"
            "    is as distinct and convincing a creation as Sherlock\n"
            "    Holmes.\"--The Bookman."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "burglarian.exploits" not in full_text

    def test_wrap_047_pen_there(self):
        # Source: The Shadow of a Man, wrap corruption: pen.there
        passage = (
            "\"In this novel, as in the previous ones from Mr. Hornung's pen,\n"
            "    there is a wealth of well-handled incidents. It is story-telling\n"
            "    of the most direct kind and holds the attention from the first\n"
            "    page to the last. Mr. Hornung seems to us in each succeeding\n"
            "    book from his pen to gain in confidence and authority, and we do\n"
            "    not hesitate to place him among the first of the comparatively\n"
            "    new writers who must be reckoned with.\"--Literature."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pen.there" not in full_text

    def test_wrap_048_his_australian(self):
        # Source: The Shadow of a Man, wrap corruption: his.australian
        passage = (
            "\"Mr. Hornung has succeeded admirably in his object: his\n"
            "    Australian scenes are a veritable nightmare; they sear the\n"
            "    imagination, and it will be some time before we get Hookey\n"
            "    Simpson, the clank of the chains, and the hero's degradation off\n"
            "    our mind.\"--London Saturday Review."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "his.australian" not in full_text

    def test_wrap_049_storywrite_such(self):
        # Source: The Shadow of a Man, wrap corruption: storywriter.such
        passage = (
            "\"It is pleasant to turn to a real story by a real story-writer.\n"
            "    Such is 'My Lord Duke.' ... Its story is its own, both in plot\n"
            "    and in characterization. It is a capital little novel.\"--_The\n"
            "    Nation_."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "storywriter.such" not in full_text

    def test_wrap_050_much_matter(self):
        # Source: The Shadow of a Man, wrap corruption: much.matter
        passage = (
            "\"Whether Lowndes be entirely realized or not does not much\n"
            "    matter; the conception of him is already a distinction. He is an\n"
            "    adventurer of genius, but not built on the usual lines.... And\n"
            "    his vitality is inexhaustible. We leave him, not without a stain\n"
            "    upon his character, but with considerable regret in our\n"
            "    minds.\"--The Bookman."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "much.matter" not in full_text

    def test_wrap_051_and_the(self):
        # Source: The Shadow of a Man, wrap corruption: and.the
        passage = (
            "\"In about half-a-dozen cases the scene is laid in Australia, and\n"
            "    the dramatic and tragic aspects of Colonial life are treated by\n"
            "    Mr. Hornung with that happy union of vigor and sympathy which\n"
            "    has stood him in such good stead in his earlier\n"
            "    novels.\"--London Spectator."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.the" not in full_text

    def test_wrap_052_hotel_about(self):
        # Source: The Shadow of the Rope, wrap corruption: hotel.about
        passage = (
            "1.  Was in Sloane Street on the night of the murder, at an hotel\n"
            "    about a mile from the house in which the murder was committed.\n"
            "    This can be proved."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hotel.about" not in full_text

    def test_wrap_053_two_mornings(self):
        # Source: The Shadow of the Rope, wrap corruption: two.mornings
        passage = (
            "3.  Knew M. in Australia, but was in England unknown to M. till two\n"
            "    mornings before murder, when M. wrote letter on receipt of which\n"
            "    ---- ---- ---- came up to town (arriving near scene of murder as\n"
            "    above stated, about time of commission). All this morally certain\n"
            "    and probably capable of legal proof."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "two.mornings" not in full_text

    def test_wrap_054_pay_his(self):
        # Source: The Shadow of the Rope, wrap corruption: pay.his
        passage = (
            "4.  \"So then I asked why a man he hadn't seen for so long should pay\n"
            "    his debts; but M. only laughed and swore, and said he'd make him.\"\n"
            "    C. could be subpoenaed to confirm if not to amplify this statement\n"
            "    to me, with others to effect that it was for money M. admitted\n"
            "    having written to \"a millionaire.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pay.his" not in full_text

    def test_wrap_055_her_acquaintan(self):
        # Source: The Shadow of the Rope, wrap corruption: her.acquaintance
        passage = (
            "5.  Attended Mrs. M.'s trial throughout, thereafter making her\n"
            "    acquaintance and offering marriage without any previous private\n"
            "    knowledge whatsoever of her character or antecedents."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "her.acquaintance" not in full_text

