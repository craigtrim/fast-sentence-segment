import pytest
from fast_sentence_segment import segment_text


class TestEbooksMacDonald:
    """Integration tests mined from George MacDonald ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1870s
    """

    def test_wrap_001_might_had(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: might.had
        passage = (
            "LORD, what I once had done with youthful might,\n"
            "     Had I been from the first true to the truth,\n"
            "     Grant me, now old, to do--with better sight,\n"
            "     And humbler heart, if not the brain of youth;\n"
            "     So wilt thou, in thy gentleness and ruth,\n"
            "     Lead back thy old soul, by the path of pain,\n"
            "     Round to his best--young eyes and heart and brain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "might.had" not in full_text

    def test_wrap_002_east_beyond(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: east.beyond
        passage = (
            "A dim aurora rises in my east,\n"
            "     Beyond the line of jagged questions hoar,\n"
            "     As if the head of our intombed High Priest\n"
            "     Began to glow behind the unopened door:\n"
            "     Sure the gold wings will soon rise from the gray!--\n"
            "     They rise not. Up I rise, press on the more,\n"
            "     To meet the slow coming of the Master's day."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "east.beyond" not in full_text

    def test_wrap_003_forgot_and(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: forgot.and
        passage = (
            "Sometimes I wake, and, lo! I have forgot,\n"
            "     And drifted out upon an ebbing sea!\n"
            "     My soul that was at rest now resteth not,\n"
            "     For I am with myself and not with thee;\n"
            "     Truth seems a blind moon in a glaring morn,\n"
            "     Where nothing is but sick-heart vanity:\n"
            "     Oh, thou who knowest! save thy child forlorn."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "forgot.and" not in full_text

    def test_wrap_004_all_when(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: all.when
        passage = (
            "Death, like high faith, levelling, lifteth all.\n"
            "     When I awake, my daughter and my son,\n"
            "     Grown sister and brother, in my arms shall fall,\n"
            "     Tenfold my girl and boy. Sure every one\n"
            "     Of all the brood to the old wings will run.\n"
            "     Whole-hearted is my worship of the man\n"
            "     From whom my earthly history began."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.when" not in full_text

    def test_wrap_005_roll_thy(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: roll.thy
        passage = (
            "Thy fishes breathe but where thy waters roll;\n"
            "     Thy birds fly but within thy airy sea;\n"
            "     My soul breathes only in thy infinite soul;\n"
            "     I breathe, I think, I love, I live but thee.\n"
            "     Oh breathe, oh think,--O Love, live into me;\n"
            "     Unworthy is my life till all divine,\n"
            "     Till thou see in me only what is thine."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "roll.thy" not in full_text

    def test_wrap_006_then_think(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: then.think
        passage = (
            "Then shall I breathe in sweetest sharing, then\n"
            "     Think in harmonious consort with my kin;\n"
            "     Then shall I love well all my father's men,\n"
            "     Feel one with theirs the life my heart within.\n"
            "     Oh brothers! sisters holy! hearts divine!\n"
            "     Then I shall be all yours, and nothing mine--\n"
            "     To every human heart a mother-twin."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "then.think" not in full_text

    def test_wrap_007_house_knocking(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: house.knocking
        passage = (
            "I see a child before an empty house,\n"
            "     Knocking and knocking at the closed door;\n"
            "     He wakes dull echoes--but nor man nor mouse,\n"
            "     If he stood knocking there for evermore.--\n"
            "     A mother angel, see! folding each wing,\n"
            "     Soft-walking, crosses straight the empty floor,\n"
            "     And opens to the obstinate praying thing."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "house.knocking" not in full_text

    def test_wrap_008_whereby_always(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: whereby.always
        passage = (
            "Were there but some deep, holy spell, whereby\n"
            "     Always I should remember thee--some mode\n"
            "     Of feeling the pure heat-throb momently\n"
            "     Of the spirit-fire still uttering this I!--\n"
            "     Lord, see thou to it, take thou remembrance' load:\n"
            "     Only when I bethink me can I cry;\n"
            "     Remember thou, and prick me with love's goad."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "whereby.always" not in full_text

    def test_wrap_009_move_and(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: move.and
        passage = (
            "When I no more can stir my soul to move,\n"
            "     And life is but the ashes of a fire;\n"
            "     When I can but remember that my heart\n"
            "     Once used to live and love, long and aspire,--\n"
            "     Oh, be thou then the first, the one thou art;\n"
            "     Be thou the calling, before all answering love,\n"
            "     And in me wake hope, fear, boundless desire."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "move.and" not in full_text

    def test_wrap_010_behold_thou(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: behold.thou
        passage = (
            "I thought that I had lost thee; but, behold!\n"
            "     Thou comest to me from the horizon low,\n"
            "     Across the fields outspread of green and gold--\n"
            "     Fair carpet for thy feet to come and go.\n"
            "     Whence I know not, or how to me thou art come!--\n"
            "     Not less my spirit with calm bliss doth glow,\n"
            "     Meeting thee only thus, in nature vague and dumb."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "behold.thou" not in full_text

    def test_wrap_011_doubt_faith(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: doubt.faith
        passage = (
            "The idle flapping of the sail is doubt;\n"
            "     Faith swells it full to breast the breasting seas.\n"
            "     Bold, conscience, fast, and rule the ruling helm;\n"
            "     Hell's freezing north no tempest can send out,\n"
            "     But it shall toss thee homeward to thy leas;\n"
            "     Boisterous wave-crest never shall o'erwhelm\n"
            "     Thy sea-float bark as safe as field-borne rooted elm."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "doubt.faith" not in full_text

    def test_wrap_012_pray_for(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: pray.for
        passage = (
            "Sometimes, hard-trying, it seems I cannot pray--\n"
            "     For doubt, and pain, and anger, and all strife.\n"
            "     Yet some poor half-fledged prayer-bird from the nest\n"
            "     May fall, flit, fly, perch--crouch in the bowery breast\n"
            "     Of the large, nation-healing tree of life;--\n"
            "     Moveless there sit through all the burning day,\n"
            "     And on my heart at night a fresh leaf cooling lay."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pray.for" not in full_text

    def test_wrap_013_live_all(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: live.all
        passage = (
            "My harvest withers. Health, my means to live--\n"
            "     All things seem rushing straight into the dark.\n"
            "     But the dark still is God. I would not give\n"
            "     The smallest silver-piece to turn the rush\n"
            "     Backward or sideways. Am I not a spark\n"
            "     Of him who is the light?--Fair hope doth flush\n"
            "     My east.--Divine success--Oh, hush and hark!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "live.all" not in full_text

    def test_wrap_014_everything_the(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: everything.the
        passage = (
            "Thy will be done. I yield up everything.\n"
            "     \"The life is more than meat\"--then more than health;\n"
            "     \"The body more than raiment\"--then than wealth;\n"
            "     The hairs I made not, thou art numbering.\n"
            "     Thou art my life--I the brook, thou the spring.\n"
            "     Because thine eyes are open, I can see;\n"
            "     Because thou art thyself, 'tis therefore I am me."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "everything.the" not in full_text

    def test_wrap_015_behind_care(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: behind.care
        passage = (
            "Care thou for mine whom I must leave behind;\n"
            "     Care that they know who 'tis for them takes care;\n"
            "     Thy present patience help them still to bear;\n"
            "     Lord, keep them clearing, growing, heart and mind;\n"
            "     In one thy oneness us together bind;\n"
            "     Last earthly prayer with which to thee I cling--\n"
            "     Grant that, save love, we owe not anything."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "behind.care" not in full_text

    def test_wrap_016_live_true(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: live.true
        passage = (
            "'Tis well, for unembodied thought a live,\n"
            "     True house to build--of stubble, wood, nor hay;\n"
            "     So, like bees round the flower by which they thrive,\n"
            "     My thoughts are busy with the informing truth,\n"
            "     And as I build, I feed, and grow in youth--\n"
            "     Hoping to stand fresh, clean, and strong, and gay,\n"
            "     When up the east comes dawning His great day."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "live.true" not in full_text

    def test_wrap_017_strong_would(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: strong.would
        passage = (
            "Thy will is truth--'tis therefore fate, the strong.\n"
            "     Would that my will did sweep full swing with thine!\n"
            "     Then harmony with every spheric song,\n"
            "     And conscious power, would give sureness divine.\n"
            "     Who thinks to thread thy great laws' onward throng,\n"
            "     Is as a fly that creeps his foolish way\n"
            "     Athwart an engine's wheels in smooth resistless play."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "strong.would" not in full_text

    def test_wrap_018_control_and(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: control.and
        passage = (
            "Do thou, my God, my spirit's weather control;\n"
            "     And as I do not gloom though the day be dun,\n"
            "     Let me not gloom when earth-born vapours roll\n"
            "     Across the infinite zenith of my soul.\n"
            "     Should sudden brain-frost through the heart's summer run,\n"
            "     Cold, weary, joyless, waste of air and sun,\n"
            "     Thou art my south, my summer-wind, my all, my one."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "control.and" not in full_text

    def test_wrap_019_eyes_therefore(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: eyes.therefore
        passage = (
            "I can no more than lift my weary eyes;\n"
            "     Therefore I lift my weary eyes--no more.\n"
            "     But my eyes pull my heart, and that, before\n"
            "     'Tis well awake, knocks where the conscience lies;\n"
            "     Conscience runs quick to the spirit's hidden door:\n"
            "     Straightway, from every sky-ward window, cries\n"
            "     Up to the Father's listening ears arise."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "eyes.therefore" not in full_text

    def test_wrap_020_thee_not(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: thee.not
        passage = (
            "Not in my fancy now I search to find thee;\n"
            "     Not in its loftiest forms would shape or bind thee;\n"
            "     I cry to one whom I can never know,\n"
            "     Filling me with an infinite overflow;\n"
            "     Not to a shape that dwells within my heart,\n"
            "     Clothed in perfections love and truth assigned thee,\n"
            "     But to the God thou knowest that thou art."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thee.not" not in full_text

    def test_wrap_021_ill_not(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: ill.not
        passage = (
            "Not, Lord, because I have done well or ill;\n"
            "     Not that my mind looks up to thee clear-eyed;\n"
            "     Not that it struggles in fast cerements tied;\n"
            "     Not that I need thee daily sorer still;\n"
            "     Not that I wretched, wander from thy will;\n"
            "     Not now for any cause to thee I cry,\n"
            "     But this, that thou art thou, and here am I."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ill.not" not in full_text

    def test_wrap_022_then_and(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: then.and
        passage = (
            "Till Death has done with him?--Ah, leave me then!\n"
            "     And Death has done with me, oh, nevermore!\n"
            "     He comes--and goes--to leave me in thy arms,\n"
            "     Nearer thy heart, oh, nearer than before!\n"
            "     To lay thy child, naked, new-born again\n"
            "     Of mother earth, crept free through many harms,\n"
            "     Upon thy bosom--still to the very core."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "then.and" not in full_text

    def test_wrap_023_how_nor(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: how.nor
        passage = (
            "Come to me, Lord: I will not speculate how,\n"
            "     Nor think at which door I would have thee appear,\n"
            "     Nor put off calling till my floors be swept,\n"
            "     But cry, \"Come, Lord, come any way, come now.\"\n"
            "     Doors, windows, I throw wide; my head I bow,\n"
            "     And sit like some one who so long has slept\n"
            "     That he knows nothing till his life draw near."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "how.nor" not in full_text

    def test_wrap_024_people_thoughts(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: people.thoughts
        passage = (
            "O Lord, I have been talking to the people;\n"
            "     Thought's wheels have round me whirled a fiery zone,\n"
            "     And the recoil of my words' airy ripple\n"
            "     My heart unheedful has puffed up and blown.\n"
            "     Therefore I cast myself before thee prone:\n"
            "     Lay cool hands on my burning brain, and press\n"
            "     From my weak heart the swelling emptiness."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "people.thoughts" not in full_text

    def test_wrap_025_worth_patience(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: worth.patience
        passage = (
            "I TO myself have neither power nor worth,\n"
            "     Patience nor love, nor anything right good;\n"
            "     My soul is a poor land, plenteous in dearth--\n"
            "     Here blades of grass, there a small herb for food--\n"
            "     A nothing that would be something if it could;\n"
            "     But if obedience, Lord, in me do grow,\n"
            "     I shall one day be better than I know."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "worth.patience" not in full_text

    def test_wrap_026_man_who(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: man.who
        passage = (
            "Back still it comes to this: there was a man\n"
            "     Who said, \"I am the truth, the life, the way:\"--\n"
            "     Shall I pass on, or shall I stop and hear?--\n"
            "     \"Come to the Father but by me none can:\"\n"
            "     What then is this?--am I not also one\n"
            "     Of those who live in fatherless dismay?\n"
            "     I stand, I look, I listen, I draw near."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "man.who" not in full_text

    def test_wrap_027_here_although(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: here.although
        passage = (
            "Thou art here--in heaven, I know, but not from here--\n"
            "     Although thy separate self do not appear;\n"
            "     If I could part the light from out the day,\n"
            "     There I should have thee! But thou art too near:\n"
            "     How find thee walking, when thou art the way?\n"
            "     Oh, present Christ! make my eyes keen as stings,\n"
            "     To see thee at their heart, the glory even of things."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "here.although" not in full_text

    def test_wrap_028_agree_wise(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: agree.wise
        passage = (
            "That thou art nowhere to be found, agree\n"
            "     Wise men, whose eyes are but for surfaces;\n"
            "     Men with eyes opened by the second birth,\n"
            "     To whom the seen, husk of the unseen is,\n"
            "     Descry thee soul of everything on earth.\n"
            "     Who know thy ends, thy means and motions see:\n"
            "     Eyes made for glory soon discover thee."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "agree.wise" not in full_text

    def test_wrap_029_feet_and(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: feet.and
        passage = (
            "Thou near then, I draw nearer--to thy feet,\n"
            "     And sitting in thy shadow, look out on the shine;\n"
            "     Ready at thy first word to leave my seat--\n"
            "     Not thee: thou goest too. From every clod\n"
            "     Into thy footprint flows the indwelling wine;\n"
            "     And in my daily bread, keen-eyed I greet\n"
            "     Its being's heart, the very body of God."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "feet.and" not in full_text

    def test_wrap_030_men_art(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: men.art
        passage = (
            "Thou wilt interpret life to me, and men,\n"
            "     Art, nature, yea, my own soul's mysteries--\n"
            "     Bringing, truth out, clear-joyous, to my ken,\n"
            "     Fair as the morn trampling the dull night. Then\n"
            "     The lone hill-side shall hear exultant cries;\n"
            "     The joyous see me joy, the weeping weep;\n"
            "     The watching smile, as Death breathes on me his cold sleep."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "men.art" not in full_text

    def test_wrap_031_faith_hidden(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: faith.hidden
        passage = (
            "I search my heart--I search, and find no faith.\n"
            "     Hidden He may be in its many folds--\n"
            "     I see him not revealed in all the world\n"
            "     Duty's firm shape thins to a misty wraith.\n"
            "     No good seems likely. To and fro I am hurled.\n"
            "     I have no stay. Only obedience holds:--\n"
            "     I haste, I rise, I do the thing he saith."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "faith.hidden" not in full_text

    def test_wrap_032_king_but(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: king.but
        passage = (
            "I will not shift my ground like Moab's king,\n"
            "     But from this spot whereon I stand, I pray--\n"
            "     From this same barren rock to thee I say,\n"
            "     \"Lord, in my commonness, in this very thing\n"
            "     That haunts my soul with folly--through the clay\n"
            "     Of this my pitcher, see the lamp's dim flake;\n"
            "     And hear the blow that would the pitcher break.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "king.but" not in full_text

    def test_wrap_033_think_when(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: think.when
        passage = (
            "Two things at once, thou know'st I cannot think.\n"
            "     When busy with the work thou givest me,\n"
            "     I cannot consciously think then of thee.\n"
            "     Then why, when next thou lookest o'er the brink\n"
            "     Of my horizon, should my spirit shrink,\n"
            "     Reproached and fearful, nor to greet thee run?\n"
            "     Can I be two when I am only one."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "think.when" not in full_text

    def test_wrap_034_awry_some(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: awry.some
        passage = (
            "My soul must unawares have sunk awry.\n"
            "     Some care, poor eagerness, ambition of work,\n"
            "     Some old offence that unforgiving did lurk,\n"
            "     Or some self-gratulation, soft and sly--\n"
            "     Something not thy sweet will, not the good part,\n"
            "     While the home-guard looked out, stirred up the old murk,\n"
            "     And so I gloomed away from thee, my Heart."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "awry.some" not in full_text

    def test_wrap_035_stray_into(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: stray.into
        passage = (
            "If I should slow diverge, and listless stray\n"
            "     Into some thought, feeling, or dream unright,\n"
            "     O Watcher, my backsliding soul affray;\n"
            "     Let me not perish of the ghastly blight.\n"
            "     Be thou, O Life eternal, in me light;\n"
            "     Then merest approach of selfish or impure\n"
            "     Shall start me up alive, awake, secure."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "stray.into" not in full_text

    def test_wrap_036_clod_selfish(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: clod.selfish
        passage = (
            "Lord, I have fallen again--a human clod!\n"
            "     Selfish I was, and heedless to offend;\n"
            "     Stood on my rights. Thy own child would not send\n"
            "     Away his shreds of nothing for the whole God!\n"
            "     Wretched, to thee who savest, low I bend:\n"
            "     Give me the power to let my rag-rights go\n"
            "     In the great wind that from thy gulf doth blow."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "clod.selfish" not in full_text

    def test_wrap_037_pray_strip(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: pray.strip
        passage = (
            "Lord, in thy spirit's hurricane, I pray,\n"
            "     Strip my soul naked--dress it then thy way.\n"
            "     Change for me all my rags to cloth of gold.\n"
            "     Who would not poverty for riches yield?\n"
            "     A hovel sell to buy a treasure-field?\n"
            "     Who would a mess of porridge careful hold\n"
            "     Against the universe's birthright old?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pray.strip" not in full_text

    def test_wrap_038_even_nor(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: even.nor
        passage = (
            "Help me to yield my will, in labour even,\n"
            "     Nor toil on toil, greedy of doing, heap--\n"
            "     Fretting I cannot more than me is given;\n"
            "     That with the finest clay my wheel runs slow,\n"
            "     Nor lets the lovely thing the shapely grow;\n"
            "     That memory what thought gives it cannot keep,\n"
            "     And nightly rimes ere morn like cistus-petals go."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "even.nor" not in full_text

    def test_wrap_039_mine_and(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: mine.and
        passage = (
            "'Tis--shall thy will be done for me?--or mine,\n"
            "     And I be made a thing not after thine--\n"
            "     My own, and dear in paltriest details?\n"
            "     Shall I be born of God, or of mere man?\n"
            "     Be made like Christ, or on some other plan?--\n"
            "     I let all run:--set thou and trim my sails;\n"
            "     Home then my course, let blow whatever gales."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mine.and" not in full_text

    def test_wrap_040_king_nor(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: king.nor
        passage = (
            "With thee on board, each sailor is a king\n"
            "     Nor I mere captain of my vessel then,\n"
            "     But heir of earth and heaven, eternal child;\n"
            "     Daring all truth, nor fearing anything;\n"
            "     Mighty in love, the servant of all men;\n"
            "     Resenting nothing, taking rage and blare\n"
            "     Into the Godlike silence of a loving care."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "king.nor" not in full_text

    def test_wrap_041_why_from(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: why.from
        passage = (
            "I cannot see, my God, a reason why\n"
            "     From morn to night I go not gladsome free;\n"
            "     For, if thou art what my soul thinketh thee,\n"
            "     There is no burden but should lightly lie,\n"
            "     No duty but a joy at heart must be:\n"
            "     Love's perfect will can be nor sore nor small,\n"
            "     For God is light--in him no darkness is at all."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "why.from" not in full_text

    def test_wrap_042_trust_but(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: trust.but
        passage = (
            "'Tis something thus to think, and half to trust--\n"
            "     But, ah! my very heart, God-born, should lie\n"
            "     Spread to the light, clean, clear of mire and rust,\n"
            "     And like a sponge drink the divine sunbeams.\n"
            "     What resolution then, strong, swift, and high!\n"
            "     What pure devotion, or to live or die!\n"
            "     And in my sleep, what true, what perfect dreams!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "trust.but" not in full_text

    def test_wrap_043_worn_why(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: worn.why
        passage = (
            "I would not have it so. Weary and worn,\n"
            "     Why not to thee run straight, and be at rest?\n"
            "     Motherward, with toy new, or garment torn,\n"
            "     The child that late forsook her changeless breast,\n"
            "     Runs to home's heart, the heaven that's heavenliest:\n"
            "     In joy or sorrow, feebleness or might,\n"
            "     Peace or commotion, be thou, Father, my delight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "worn.why" not in full_text

    def test_wrap_044_doubt_and(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: doubt.and
        passage = (
            "The thing I would say, still comes forth with doubt\n"
            "     And difference:--is it that thou shap'st my ends?\n"
            "     Or is it only the necessity\n"
            "     Of stubborn words, that shift sluggish about,\n"
            "     Warping my thought as it the sentence bends?--\n"
            "     Have thou a part in it, O Lord, and I\n"
            "     Shall say a truth, if not the thing I try."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "doubt.and" not in full_text

    def test_wrap_045_morn_fly(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: morn.fly
        passage = (
            "THE song birds that come to me night and morn,\n"
            "     Fly oft away and vanish if I sleep,\n"
            "     Nor to my fowling-net will one return:\n"
            "     Is the thing ever ours we cannot keep?--\n"
            "     But their souls go not out into the deep.\n"
            "     What matter if with changed song they come back?\n"
            "     Old strength nor yet fresh beauty shall they lack."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "morn.fly" not in full_text

    def test_wrap_046_thou_sunset(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: thou.sunset
        passage = (
            "Gloriously wasteful, O my Lord, art thou!\n"
            "     Sunset faints after sunset into the night,\n"
            "     Splendorously dying from thy window-sill--\n"
            "     For ever. Sad our poverty doth bow\n"
            "     Before the riches of thy making might:\n"
            "     Sweep from thy space thy systems at thy will--\n"
            "     In thee the sun sets every sunset still."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thou.sunset" not in full_text

    def test_wrap_047_god_when(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: god.when
        passage = (
            "And in the perfect time, O perfect God,\n"
            "     When we are in our home, our natal home,\n"
            "     When joy shall carry every sacred load,\n"
            "     And from its life and peace no heart shall roam,\n"
            "     What if thou make us able to make like thee--\n"
            "     To light with moons, to clothe with greenery,\n"
            "     To hang gold sunsets o'er a rose and purple sea!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "god.when" not in full_text

    def test_wrap_048_come_brother(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: come.brother
        passage = (
            "Then to his neighbour one may call out, \"Come!\n"
            "     Brother, come hither--I would show you a thing;\"\n"
            "     And lo, a vision of his imagining,\n"
            "     Informed of thought which else had rested dumb,\n"
            "     Before the neighbour's truth-delighted eyes,\n"
            "     In the great æther of existence rise,\n"
            "     And two hearts each to each the closer cling!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "come.brother" not in full_text

    def test_wrap_049_core_whatever(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: core.whatever
        passage = (
            "We make, but thou art the creating core.\n"
            "     Whatever thing I dream, invent, or feel,\n"
            "     Thou art the heart of it, the atmosphere.\n"
            "     Thou art inside all love man ever bore;\n"
            "     Yea, the love itself, whatever thing be dear.\n"
            "     Man calls his dog, he follows at his heel,\n"
            "     Because thou first art love, self-caused, essential, mere."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "core.whatever" not in full_text

    def test_wrap_050_leave_some(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: leave.some
        passage = (
            "What if, writing, I always seem to leave\n"
            "     Some better thing, or better way, behind,\n"
            "     Why should I therefore fret at all, or grieve!\n"
            "     The worse I drop, that I the better find;\n"
            "     The best is only in thy perfect mind.\n"
            "     Fallen threads I will not search for--I will weave.\n"
            "     Who makes the mill-wheel backward strike to grind!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "leave.some" not in full_text

    def test_wrap_051_prayers_for(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: prayers.for
        passage = (
            "Be with me, Lord. Keep me beyond all prayers:\n"
            "     For more than all my prayers my need of thee,\n"
            "     And thou beyond all need, all unknown cares;\n"
            "     What the heart's dear imagination dares,\n"
            "     Thou dost transcend in measureless majesty\n"
            "     All prayers in one--my God, be unto me\n"
            "     Thy own eternal self, absolutely."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "prayers.for" not in full_text

    def test_wrap_052_truth_lie(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: truth.lie
        passage = (
            "Where should the unknown treasures of the truth\n"
            "     Lie, but there whence the truth comes out the most--\n"
            "     In the Son of man, folded in love and ruth?\n"
            "     Fair shore we see, fair ocean; but behind\n"
            "     Lie infinite reaches bathing many a coast--\n"
            "     The human thought of the eternal mind,\n"
            "     Pulsed by a living tide, blown by a living wind."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "truth.lie" not in full_text

    def test_wrap_053_days_and(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: days.and
        passage = (
            "Thou, healthful Father, art the Ancient of Days,\n"
            "     And Jesus is the eternal youth of thee.\n"
            "     Our old age is the scorching of the bush\n"
            "     By life's indwelling, incorruptible blaze.\n"
            "     O Life, burn at this feeble shell of me,\n"
            "     Till I the sore singed garment off shall push,\n"
            "     Flap out my Psyche wings, and to thee rush."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "days.and" not in full_text

    def test_wrap_054_dear_however(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: dear.however
        passage = (
            "Therefore, my brothers, therefore, sisters dear,\n"
            "     However I, troubled or selfish, fail\n"
            "     In tenderness, or grace, or service clear,\n"
            "     I every moment draw to you more near;\n"
            "     God in us from our hearts veil after veil\n"
            "     Keeps lifting, till we see with his own sight,\n"
            "     And all together run in unity's delight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dear.however" not in full_text

    def test_wrap_055_love_not(self):
        # Source: A Book of Strife in the Form of the Diary of an Old Soul, wrap corruption: love.not
        passage = (
            "I love thee, Lord, for very greed of love--\n"
            "     Not of the precious streams that towards me move,\n"
            "     But of the indwelling, outgoing, fountain store.\n"
            "     Than mine, oh, many an ignorant heart loves more!\n"
            "     Therefore the more, with Mary at thy feet,\n"
            "     I must sit worshipping--that, in my core,\n"
            "     Thy words may fan to a flame the low primeval heat."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "love.not" not in full_text

