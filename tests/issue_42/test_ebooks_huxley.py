import pytest
from fast_sentence_segment import segment_text


class TestEbooksHuxley:
    """Integration tests mined from Aldous Huxley ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1920s
    """

    def test_wrap_001_ecclesi_cithara(self):
        # Source: Antic Hay, wrap corruption: ecclesi.cithara
        passage = (
            "“Gazophylacium Ecclesiæ,\n"
            "             Cithara benesonans Dei,\n"
            "             Cymbalum jubilationis Christi,\n"
            "             Promptuarium mysteriorum fidei, ora pro nobis."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ecclesi.cithara" not in full_text

    def test_wrap_002_conquistad_there(self):
        # Source: Antic Hay, wrap corruption: conquistador.there
        passage = (
            "“Look down, Conquistador!\n"
            "            There on the valley’s broad green floor,\n"
            "            There lies the lake; the jewelled cities gleam;\n"
            "            Chalco and Tlacopan\n"
            "            Awaiting the coming Man.\n"
            "            Look down on Mexico, Conquistador,\n"
            "            Land of your golden dream.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "conquistador.there" not in full_text

    def test_wrap_003_behaviour_like(self):
        # Source: Antic Hay, wrap corruption: behaviour.like
        passage = (
            "“Christlike in my behaviour,\n"
            "                      Like every good believer,\n"
            "                      I imitate the Saviour,\n"
            "                      And cultivate a beaver."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "behaviour.like" not in full_text

    def test_wrap_004_dois_vous(self):
        # Source: Antic Hay, wrap corruption: dois.vous
        passage = (
            "“‘Puisque nous sommes là, je dois,\n"
            "                    Vous avertir, sans trop de honte,\n"
            "                  Que je n’égale pas le Comte\n"
            "                    Casanovesque de Sixfois.’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dois.vous" not in full_text

    def test_wrap_005_rose_goodness(self):
        # Source: Antic Hay, wrap corruption: rose.goodness
        passage = (
            "‘O beauty of the rose,\n"
            "             Goodness as well as perfume exhaling!\n"
            "             Who gazes on these flowers,\n"
            "             On this blue hill and ripening field—he knows\n"
            "             Where duty leads and that the nameless Powers\n"
            "             In a rose can speak their will.’"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rose.goodness" not in full_text

    def test_wrap_006_husband_kneels(self):
        # Source: Antic Hay, wrap corruption: husband.kneels
        passage = (
            "On a narrow bed—on a bier perhaps—the corpse of a woman. The husband\n"
            "  kneels beside it. At the foot stands the doctor, putting away his\n"
            "  instruments. In a beribboned pink cradle reposes a monstrous baby."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "husband.kneels" not in full_text

    def test_wrap_007_her_chilled(self):
        # Source: Antic Hay, wrap corruption: her.chilled
        passage = (
            "THE HUSBAND: Her milk—her milk is cold already. All the woman in her\n"
            "  chilled and curdled within her breasts. Ah, Jesus! what miraculous\n"
            "  galactagogue will make it flow again?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "her.chilled" not in full_text

    def test_wrap_008_feedingbot_heres(self):
        # Source: Antic Hay, wrap corruption: feedingbottle.heres
        passage = (
            "THE HUSBAND (pouring the milk into a long-tubed feeding-bottle):\n"
            "  Here’s for you, monster, to drink your own health in. (_He gives the\n"
            "  bottle to the child._)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "feedingbottle.heres" not in full_text

    def test_wrap_009_now_from(self):
        # Source: Antic Hay, wrap corruption: now.from
        passage = (
            "The curtain went up. In a bald room stood the Monster, grown now\n"
            "  from an infant into a frail and bent young man with bandy legs. At\n"
            "  the back of the stage a large window giving on to a street along\n"
            "  which people pass."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "now.from" not in full_text

    def test_wrap_010_the_street(self):
        # Source: Antic Hay, wrap corruption: the.street
        passage = (
            "(The YOUNG LADY _enters. She stands outside the window, in the\n"
            "    street, paying no attention to the_ MONSTER; _she seems to be\n"
            "    waiting for somebody._)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.street" not in full_text

    def test_wrap_011_though_there(self):
        # Source: Antic Hay, wrap corruption: though.there
        passage = (
            "She is like a pear tree in flower. When she smiles, it is as though\n"
            "  there were stars. Her hair is like the harvest in an eclogue, her\n"
            "  cheeks are all the fruits of summer. Her arms and thighs are as\n"
            "  beautiful as the soul of St. Catherine of Siena. And her eyes, her\n"
            "  eyes are plumbless with thought and limpidly pure like the water of\n"
            "  the mountains."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "though.there" not in full_text

    def test_wrap_012_chine_will(self):
        # Source: Antic Hay, wrap corruption: chine.will
        passage = (
            "THE YOUNG LADY: If I wait till the summer sale, the crêpe de Chine\n"
            "  will be reduced by at least two shillings a yard, and on six\n"
            "  camisoles that will mean a lot of money. But the question is: can I\n"
            "  go from May till the end of July with the underclothing I have now?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "chine.will" not in full_text

    def test_wrap_013_golden_harvest(self):
        # Source: Antic Hay, wrap corruption: golden.harvest
        passage = (
            "THE MONSTER: But I love you, flowering pear tree; I love you, golden\n"
            "  harvest; I love you, fruitage of summer; I love you, body and limbs,\n"
            "  with the shape of a saint’s thought."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "golden.harvest" not in full_text

    def test_wrap_014_seized_with(self):
        # Source: Antic Hay, wrap corruption: seized.with
        passage = (
            "THE MONSTER (taking her hand): You cannot be cruel! (_He is seized\n"
            "  with a violent paroxysm of coughing which doubles him up, which\n"
            "  shakes and torments him. The handkerchief he holds to his mouth is\n"
            "  spotted with blood._)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "seized.with" not in full_text

    def test_wrap_015_roger_she(self):
        # Source: Antic Hay, wrap corruption: roger.she
        passage = (
            "THE YOUNG LADY: Please go away. (In a different voice) Ah, Roger!\n"
            "  (_She advances to meet a snub-nosed lubber with curly hair and a\n"
            "  face like a groom’s, who passes along the street at this moment._)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "roger.she" not in full_text

    def test_wrap_016_through_the(self):
        # Source: Antic Hay, wrap corruption: through.the
        passage = (
            "(_She climbs through the window and they go off together through\n"
            "      the door on the left of the stage. The curtains descend for a\n"
            "      moment, then rise again. The_ MONSTER and the PROSTITUTE _are\n"
            "      seen issuing from the door at which they went out._)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "through.the" not in full_text

    def test_wrap_017_cheques_how(self):
        # Source: Antic Hay, wrap corruption: cheques.how
        passage = (
            "THE PROSTITUTE: Thank you. Not a cheque. I don’t want any cheques.\n"
            "    How do I know it isn’t a dud one that they’ll refuse payment for\n"
            "    at the bank? Ready money for me, thanks."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "cheques.how" not in full_text

    def test_wrap_018_young_rips(self):
        # Source: Antic Hay, wrap corruption: young.rips
        passage = (
            "THE PROSTITUTE: Nice state of things we’re coming to, when young\n"
            "    rips try and swindle us poor girls out of our money! Mean,\n"
            "    stinking skunks! I’d like to slit the throats of some of them."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "young.rips" not in full_text

    def test_wrap_019_music_love(self):
        # Source: Antic Hay, wrap corruption: music.love
        passage = (
            "THE MONSTER (solus): Somewhere there must be love like music.\n"
            "    Love harmonious and ordered: two spirits, two bodies moving\n"
            "    contrapuntally together. Somewhere, the stupid brutish act must be\n"
            "    made to make sense, must be enriched, must be made significant.\n"
            "    Lust, like Diabelli’s waltz, a stupid air, turned by a genius into\n"
            "    three-and-thirty fabulous variations. Somewhere...."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "music.love" not in full_text

    def test_wrap_020_black_patch(self):
        # Source: Antic Hay, wrap corruption: black.patch
        passage = (
            "When the curtain rose again it was on an aged Monster, with a black\n"
            "  patch over the left side of his nose, no hair, no teeth, and sitting\n"
            "  harmlessly behind the bars of an asylum."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "black.patch" not in full_text

    def test_wrap_021_pietate_porti(self):
        # Source: Antic Hay, wrap corruption: pietate.porti
        passage = (
            "Se dentro del tuo cor morte e pietate\n"
            "              Porti in un tempo, e ch’l mio basso ingegno\n"
            "              Non sappia ardendo trarne altro che morte."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pietate.porti" not in full_text

    def test_wrap_022_sir_deniss(self):
        # Source: Crome Yellow, wrap corruption: sir.deniss
        passage = (
            "“All in good time, sir,” said the guard soothingly. He was a large,\n"
            "stately man with a naval beard. One pictured him at home, drinking tea,\n"
            "surrounded by a numerous family. It was in that tone that he must have\n"
            "spoken to his children when they were tiresome. “All in good time, sir.”\n"
            " Denis’s man of action collapsed, punctured."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sir.deniss" not in full_text

    def test_wrap_023_incomes_she(self):
        # Source: Crome Yellow, wrap corruption: incomes.she
        passage = (
            "“‘What are thousand pound fur coats, what are quarter million incomes?’”\n"
            " She looked up from the page with a histrionic movement of the head; her\n"
            "orange coiffure nodded portentously. Denis looked at it, fascinated.\n"
            "Was it the Real Thing and henna, he wondered, or was it one of those\n"
            "Complete Transformations one sees in the advertisements?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "incomes.she" not in full_text

    def test_wrap_024_secondrate_implied(self):
        # Source: Crome Yellow, wrap corruption: secondrate.implied
        passage = (
            "“What are you reading?” She looked at the book. “Rather second-rate,\n"
            "isn’t it?” The tone in which Mary pronounced the word “second-rate”\n"
            " implied an almost infinite denigration. She was accustomed in London to\n"
            "associate only with first-rate people who liked first-rate things, and\n"
            "she knew that there were very, very few first-rate things in the world,\n"
            "and that those were mostly French."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "secondrate.implied" not in full_text

    def test_wrap_025_light_floats(self):
        # Source: Jonah Christmas 1917, wrap corruption: light.floats
        passage = (
            "A cream of phospherescent light\n"
            "    Floats on the wash that to and fro\n"
            "    Slides round his feet—enough to show\n"
            "    Many a pendulous stalactite\n"
            "    Of naked mucus, whorls and wreaths\n"
            "    And huge festoons of mottled tripes,\n"
            "    With smaller palpitating pipes\n"
            "    Through which some yeasty liquor seethes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "light.floats" not in full_text

    def test_wrap_026_stones_sunk(self):
        # Source: Jonah Christmas 1917, wrap corruption: stones.sunk
        passage = (
            "His eyes are little rutilant stones\n"
            "    Sunk in black basalt; scale by scale\n"
            "    Men count the wealth of silver mail\n"
            "    That laps his flesh and iron bones.\n"
            "    And from his navel, deep and wide\n"
            "    As an old Cyclops’ drinking-bowl,\n"
            "    Spring those stout nerves of twisted hide\n"
            "    That are his life and strength and soul."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "stones.sunk" not in full_text

    def test_wrap_027_jvoque_lesprit(self):
        # Source: Jonah Christmas 1917, wrap corruption: jvoque.lesprit
        passage = (
            "Péniblement de mes bouquins moisis j’évoque\n"
            "    L’esprit mystique et frais de la Sainte Alacocque;\n"
            "    Mais sans verve pour moi saigne le Sacré Coeur.\n"
            "    Tu parles, et ta voix de petite ingénue\n"
            "    Imite un Séraphin, cul nu sur une nue,\n"
            "    Louant Dieu de son psaume infiniment moqueur."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "jvoque.lesprit" not in full_text

    def test_wrap_028_rococo_rappelle(self):
        # Source: Jonah Christmas 1917, wrap corruption: rococo.rappelle
        passage = (
            "Temple d’Amours passés, ton style rococo\n"
            "    Rappelle tristement le rire d’un gai âge.\n"
            "    Sur ton autel discret les belles de Watteau\n"
            "    Vouaient leur vierge offrande, onzième pucelage."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rococo.rappelle" not in full_text

    def test_wrap_029_aprsmidis_elles(self):
        # Source: Jonah Christmas 1917, wrap corruption: aprsmidis.elles
        passage = (
            "Derrière tes volets, les beaux après-midis,\n"
            "    Elles out dénoué leur friponne ceinture,\n"
            "    Avec ménagement goûtant le paradis\n"
            "    Pour peur de violer leur chaste chevelure."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "aprsmidis.elles" not in full_text

    def test_wrap_030_nglig_car(self):
        # Source: Jonah Christmas 1917, wrap corruption: nglig.car
        passage = (
            "Mais, Temple, maintenant te voilà négligé;\n"
            "    Car aucun pied furtif ne sonne sur tes dalles,\n"
            "    Et dans l’Alcôve froid, restes de volupté,\n"
            "    Poussent lubriquement de gros amorphophalles."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "nglig.car" not in full_text

    def test_wrap_031_laforgue_frre(self):
        # Source: Jonah Christmas 1917, wrap corruption: laforgue.frre
        passage = (
            "Que je t’aime, mon cher Laforgue,\n"
            "    Frère qui connais les nostalgies\n"
            "    Qu’engendrent les sanglots des violons;\n"
            "    Et puis, dans la rue, les pâmoisons\n"
            "    Crépusculaires des orgues—des orgues\n"
            "    D’une par trop lointaine Barbarie.—\n"
            "    O ciel, tu les as senties\n"
            "    Percer ton coeur de Bon Breton!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "laforgue.frre" not in full_text

    def test_wrap_032_froufrous_malgr(self):
        # Source: Jonah Christmas 1917, wrap corruption: froufrous.malgr
        passage = (
            "Parmi les parfums et les frou-frous,\n"
            "    Malgré toi ta chair est restée pure,\n"
            "    Et tu en as devenu presque fou;\n"
            "    Tu pensais, tu étais un Hors-Nature."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "froufrous.malgr" not in full_text

    def test_wrap_033_vivote_selon(self):
        # Source: Jonah Christmas 1917, wrap corruption: vivote.selon
        passage = (
            "Hélas, il faut que l’on vivote\n"
            "    Selon la Nature et le père Aristote;\n"
            "    Mais c’était une bien autre loi\n"
            "    Que nous suivions, toi et moi.\n"
            "    Vois-tu, mon pauvre Jules,\n"
            "    Nous nous sommes faits assez ridicules."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "vivote.selon" not in full_text

    def test_wrap_034_issues_wise(self):
        # Source: Jonah Christmas 1917, wrap corruption: issues.wise
        passage = (
            "God’s in his Heaven:—He never issues\n"
            "        (Wise man!) to visit this world of ours.\n"
            "    Unchecked the cancer gnaws our tissues,\n"
            "        Stops to lick chops and then again devours."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "issues.wise" not in full_text

    def test_wrap_035_roam_mid(self):
        # Source: Jonah Christmas 1917, wrap corruption: roam.mid
        passage = (
            "They find who most delight to roam\n"
            "        ’Mid castles of remotest Spain\n"
            "    There’s luckily no place like home,\n"
            "        And so they start upon their travels again."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "roam.mid" not in full_text

    def test_wrap_036_escape_who(self):
        # Source: Jonah Christmas 1917, wrap corruption: escape.who
        passage = (
            "Beauty for some provides escape,\n"
            "        Who gain a happiness in eyeing\n"
            "    The gorgeous buttocks of the ape\n"
            "        Or autumn sunsets exquisitely dying."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "escape.who" not in full_text

    def test_wrap_037_this_mount(self):
        # Source: Jonah Christmas 1917, wrap corruption: this.mount
        passage = (
            "And some to better worlds than this\n"
            "        Mount up on wings as frail and misty\n"
            "    As passion’s all-too-transient kiss,\n"
            "        (Though afterwards—oh, omne animal triste!)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "this.mount" not in full_text

    def test_wrap_038_liquor_well(self):
        # Source: Jonah Christmas 1917, wrap corruption: liquor.well
        passage = (
            "Then brim the bowl with atrabilious liquor!\n"
            "        We’ll pledge our Empire vast across the flood;\n"
            "    For Blood, as all men know, than Water’s thicker,\n"
            "        But water’s wider, thank the Lord, than Blood."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "liquor.well" not in full_text

    def test_wrap_039_laureate_professor(self):
        # Source: Jonah Christmas 1917, wrap corruption: laureate.professor
        passage = (
            "Parson and Poet Laureate,\n"
            "        Professor, Grocer, Don—\n"
            "    This one as fat as Ehud, that (poor dear!) would grow the more he ate,\n"
            "        Yet more a skeleton."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "laureate.professor" not in full_text

    def test_wrap_040_goitres_most(self):
        # Source: Jonah Christmas 1917, wrap corruption: goitres.most
        passage = (
            "Some have piles and some have goitres,\n"
            "        Most of them have Bright’s disease,\n"
            "    Uric acid has made them flaccid and one gouty hero loiters,\n"
            "        Anchylosed in toes and knees."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "goitres.most" not in full_text

    def test_wrap_041_carrion_through(self):
        # Source: Jonah Christmas 1917, wrap corruption: carrion.through
        passage = (
            "’Tis Duty drags their aching carrion\n"
            "        Through the rain and through the mud.\n"
            "    England calls! From Windsor walls sounds the once Coburgian clarion,\n"
            "        Screaming: Empire, Home and Blood!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "carrion.through" not in full_text

    def test_wrap_042_trees_the(self):
        # Source: Jonah Christmas 1917, wrap corruption: trees.the
        passage = (
            "Dark water: the moonless side of the trees:\n"
            "    The Dog-Star sweating in the roses: Mind\n"
            "    Heat-curdled to sheer flesh. For ease\n"
            "    And the sake of coolness, having dined,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "trees.the" not in full_text

    def test_wrap_043_exhales_like(self):
        # Source: Jonah Christmas 1917, wrap corruption: exhales.like
        passage = (
            "‘How weedily the river exhales!’\n"
            "    ‘Like the smell of caterpillar’s dung.’\n"
            "    ‘You too collected?’ ‘When I was young,\n"
            "    But used no camphor; Moth prevails"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "exhales.like" not in full_text

    def test_wrap_044_close_but(self):
        # Source: Jonah Christmas 1917, wrap corruption: close.but
        passage = (
            "Over moths, you take me.’ Sounding close,\n"
            "    But God knows where, two landrails scrape\n"
            "    Nails on combs. Her hair is loose,\n"
            "    One tendril astray upon the nape"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "close.but" not in full_text

    def test_wrap_045_white_like(self):
        # Source: Jonah Christmas 1917, wrap corruption: white.like
        passage = (
            "Of a neck which star-revealed is white\n"
            "    Like an open-eyed tobacco-flower—\n"
            "    Frail thurible that fills the night\n"
            "    With the subtle intoxicating power"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "white.like" not in full_text

    def test_wrap_046_too_your(self):
        # Source: Jonah Christmas 1917, wrap corruption: too.your
        passage = (
            "Of summer perfume. And you too—\n"
            "    Your scent intoxicates; the smell\n"
            "    Of clothes, of hair, the essence of you.\n"
            "    But for the ferments of Moselle."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "too.your" not in full_text

    def test_wrap_047_aware_that(self):
        # Source: Jonah Christmas 1917, wrap corruption: aware.that
        passage = (
            "And I wake, distressingly aware\n"
            "    That there are uglier things in life\n"
            "    Than perfumed stars and women’s hair.—\n"
            "    Action, then, action! will you be my wife?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "aware.that" not in full_text

    def test_wrap_048_crookedly_for(self):
        # Source: Jonah Christmas 1917, wrap corruption: crookedly.for
        passage = (
            "My typewriter has been writing crookedly\n"
            "    For a very considerable time;\n"
            "    It is so hard to write in metre and rhyme\n"
            "    With a typewriter that writes crookedly.\n"
            "    Lines should look clean and decent to the eye,\n"
            "    And mine have ceased to do so; and so that is why\n"
            "    I am ceasing to be a poet....\n"
            "    Because my typewriter writes so exacerbatingly,\n"
            "    So distressingly crookedly."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "crookedly.for" not in full_text

    def test_wrap_049_john_and(self):
        # Source: Leda, wrap corruption: john.and
        passage = (
            "THE Open Sesame of “Master John,”\n"
            "  And then the broad silk bosom of Aunt Loo.\n"
            "  “Dear John, this is a pleasure. How are you?”\n"
            "  “Well, thanks. Where’s Uncle Will?” “Your uncle’s gone\n"
            "  To Bath for his lumbago. He gets on\n"
            "  As well as anyone can hope to do\n"
            "  At his age—for you know he’s seventy-two;\n"
            "  But still, he does his bit. He sits upon"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "john.and" not in full_text

    def test_wrap_050_takes_parties(self):
        # Source: Leda, wrap corruption: takes.parties
        passage = (
            "The local Tribunal at home, and takes\n"
            "  Parties of wounded soldiers out in brakes\n"
            "  To see the country. And three times a week\n"
            "  He still goes up to business in the City;\n"
            "  And then, sometimes, at night he has to speak\n"
            "  In Village Halls for the War Aims Committee.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "takes.parties" not in full_text

    def test_wrap_051_war_what(self):
        # Source: Leda, wrap corruption: war.what
        passage = (
            "“Well, have you any news about the war?\n"
            "  What do they say in France?” “I daren’t repeat\n"
            "  The things they say.” “You see we’ve got some meat\n"
            "  For you, dear John. Really, I think before\n"
            "  To-day I’ve had no lamb this year. We score\n"
            "  By getting decent vegetables to eat,\n"
            "  Sent up from home. This is a good receipt:\n"
            "  The touch of garlic makes it. Have some more."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "war.what" not in full_text

    def test_wrap_052_twentythir_did(self):
        # Source: Leda, wrap corruption: twentythird.did
        passage = (
            "Poor Tom was wounded on the twenty-third;\n"
            "  Did you know that? And just to-day I heard\n"
            "  News from your uncle that his nephew James\n"
            "  Is dead—Matilda’s eldest boy.” “I knew\n"
            "  One of those boys, but I’m so bad at names.\n"
            "  Mine had red hair.” “Oh, now, that must be Hugh.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "twentythird.did" not in full_text

    def test_wrap_053_dine_quietly(self):
        # Source: Leda, wrap corruption: dine.quietly
        passage = (
            "“Colonel McGillicuddy came to dine\n"
            "  Quietly here, a night or two ago.\n"
            "  He’s on the Staff and very much in the know\n"
            "  About all sorts of things. His special line\n"
            "  Is Tanks. He says we’ve got a new design\n"
            "  Of super-Tank, with big guns, that can go\n"
            "  (I think he said) at thirty miles or so\n"
            "  An hour. That ought to make them whine"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dine.quietly" not in full_text

    def test_wrap_054_remember_that(self):
        # Source: Leda, wrap corruption: remember.that
        passage = (
            "For peace. He also said, if I remember,\n"
            "  That the war couldn’t last beyond September,\n"
            "  Because the Germans’ trucks were wearing out\n"
            "  And couldn’t be replaced. I only hope\n"
            "  It’s true. You know your uncle has no doubt\n"
            "  That the whole thing was plotted by the Pope . . .”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "remember.that" not in full_text

    def test_wrap_055_melancholy_that(self):
        # Source: Leda, wrap corruption: melancholy.that
        passage = (
            "He tottered forth, full of the melancholy\n"
            "  That comes of surfeit, and began to walk\n"
            "  Slowly towards Oxford Street. The brazen sky\n"
            "  Burned overhead. Beneath his feet the stones\n"
            "  Were a grey incandescence, and his bones\n"
            "  Melted within him, and his bowels yearned."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "melancholy.that" not in full_text

