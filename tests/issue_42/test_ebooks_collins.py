import pytest
from fast_sentence_segment import segment_text


class TestEbooksCollins:
    """Integration tests mined from Wilkie Collins ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1860s
    """

    def test_wrap_001_edinburgh_giving(self):
        # Source: A Rogues Life, wrap corruption: edinburgh.giving
        passage = (
            "“A private room--something to eat, ready in an hour’s time--chaise\n"
            "afterward to the nearest place from which a coach runs to Edinburgh.”\n"
            " Giving these orders rapidly, I followed the girl with my traveling\n"
            "companions into a stuffy little room. As soon as our attendant had left\n"
            "us, I locked the door, put the key in my pocket, and took Alicia by the\n"
            "hand."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "edinburgh.giving" not in full_text

    def test_wrap_002_disgracefu_and(self):
        # Source: A Rogues Life, wrap corruption: disgraceful.and
        passage = (
            "Mrs. Baggs raised her eyes and hands to heaven, exclaimed “Disgraceful!”\n"
            " and flounced out of the room in a passion. Such was my Scotch\n"
            "marriage--as lawful a ceremony, remember, as the finest family wedding\n"
            "at the largest parish church in all England."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "disgraceful.and" not in full_text

    def test_wrap_003_monsieur_said(self):
        # Source: After Dark, wrap corruption: monsieur.said
        passage = (
            "“My young lady has just sent me to call you in to coffee, monsieur,”\n"
            " said Guillaume. “She has kept a cup hot for you, and another cup for\n"
            "Monsieur Lomaque.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "monsieur.said" not in full_text

    def test_wrap_004_anything_thought(self):
        # Source: After Dark, wrap corruption: anything.thought
        passage = (
            "Danville hurried to it, and looked out eagerly. “I have not hastened my\n"
            "return without reason. I wouldn’t have missed this arrest for anything!”\n"
            " thought he, peering into the night."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "anything.thought" not in full_text

    def test_wrap_005_him_these(self):
        # Source: After Dark, wrap corruption: him.these
        passage = (
            "“Silence him!” “Remove him out of court!” “Gag him!” “Guillotine him!”\n"
            " These cries rose from the audience the moment the president had done\n"
            "speaking. They were all directed at Trudaine, who had made a last\n"
            "desperate effort to persuade his sister to keep silence, and had been\n"
            "detected in the attempt by the spectators."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "him.these" not in full_text

    def test_wrap_006_falsehoods_answered(self):
        # Source: After Dark, wrap corruption: falsehoods.answered
        passage = (
            "“He has cleared himself by the most execrable of all falsehoods,”\n"
            " answered Trudaine. “If his mother could be traced and brought here, her\n"
            "testimony would prove it.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "falsehoods.answered" not in full_text

    def test_wrap_007_important_continued(self):
        # Source: After Dark, wrap corruption: important.continued
        passage = (
            "“You are not in your right senses,” said the chief agent, firmly;\n"
            "“anxiety and apprehension on your sister’s account have shaken your\n"
            "mind. Try to compose yourself, and listen to me. I have something\n"
            "important to say--” (Trudaine looked at him incredulously.) “Important,”\n"
            " continued Lomaque, “as affecting your sister’s interests at this\n"
            "terrible crisis.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "important.continued" not in full_text

    def test_wrap_008_kerby_said(self):
        # Source: After Dark, wrap corruption: kerby.said
        passage = (
            "“Fine anatomical preparations in my room, are there not, Mr. Kerby?”\n"
            " said the old gentleman. “Did you notice a very interesting and perfect\n"
            "arrangement of the intestinal ganglia? They form the subject of an\n"
            "important chapter in my great work.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "kerby.said" not in full_text

    def test_wrap_009_met_brigidas(self):
        # Source: After Dark, wrap corruption: met.brigidas
        passage = (
            "“Do you think I have not had my misfortunes, too, since we met?”\n"
            " (Brigida’s face brightened maliciously at those words.) “You have had\n"
            "your revenge,” continued Mademoiselle Virginie, coldly, turning away to\n"
            "the table and taking up the scissors again."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "met.brigidas" not in full_text

    def test_wrap_010_yet_with(self):
        # Source: After Dark, wrap corruption: yet.with
        passage = (
            "“My nurse was,” returned the young man, reddening, and laughing rather\n"
            "uneasily. “She taught me some bad habits that I have not got over yet.”\n"
            " With those words he nodded and hastily went out."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "yet.with" not in full_text

    def test_wrap_011_attention_pursued(self):
        # Source: After Dark, wrap corruption: attention.pursued
        passage = (
            "“Then you can listen to me, brother, with the greater attention,”\n"
            " pursued the priest. “I objected to the coarseness of your tone in\n"
            "talking of our young pupil and your daughter; I object still more\n"
            "strongly to your insinuation that my desire to see them married\n"
            "(provided always that they are sincerely attached to each other) springs\n"
            "from a mercenary motive.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "attention.pursued" not in full_text

    def test_wrap_012_rocco_answered(self):
        # Source: After Dark, wrap corruption: rocco.answered
        passage = (
            "“Her father, sir, Signor Luca Lomi; and her uncle, Father Rocco,”\n"
            " answered the man. “They were here all through the day, until my mistress\n"
            "fell asleep.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rocco.answered" not in full_text

    def test_wrap_013_interview_said(self):
        # Source: After Dark, wrap corruption: interview.said
        passage = (
            "“You suggested just now that we had better not prolong this interview,”\n"
            " said Father Rocco, still smiling. “I think you were right; if we part at\n"
            "once, we may still part friends. You have had my advice not to go to\n"
            "the ball, and you decline following it. I have nothing more to say.\n"
            "Good-night.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "interview.said" not in full_text

    def test_wrap_014_birth_heard(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: birth.heard
        passage = (
            "Angels, who had watched my birth,\n"
            "    Heard me sigh to sing to earth;\n"
            "    'Twas transgression ne'er forgiv'n\n"
            "    To forget my native Heav'n;\n"
            "    So they sternly bade me go--\n"
            "    Banish'd to the world below."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "birth.heard" not in full_text

    def test_wrap_015_breeze_came(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: breeze.came
        passage = (
            "Young spirits of the Spring sweet breeze\n"
            "    Came thronging round me, soft and coy,\n"
            "    Light wood-nymphs sported in the trees,\n"
            "    And laughing Echo leapt for joy!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "breeze.came" not in full_text

    def test_wrap_016_pain_softend(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: pain.softend
        passage = (
            "Brooding Woe and writhing Pain\n"
            "    Soften'd at my gentle strain;\n"
            "    Bounding Joy, with footstep fleet,\n"
            "    Ran to nestle at my feet;\n"
            "    While, aroused, delighted Love\n"
            "    Softly kiss'd me from above!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pain.softend" not in full_text

    def test_wrap_017_impart_where(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: impart.where
        passage = (
            "Still pleas'd, my solace I impart\n"
            "    Where brightest hopes are scattered dead;\n"
            "    'Tis mine--sweet gift!--to charm the heart,\n"
            "    Though all its other joys have fled!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "impart.where" not in full_text

    def test_wrap_018_beside_harmless(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: beside.harmless
        passage = (
            "Time, that withers all beside,\n"
            "    Harmless past me loves to glide;\n"
            "    Change, that mortals must obey,\n"
            "    Ne'er shall shake my gentle sway;\n"
            "    Still 'tis mine all hearts to move\n"
            "    In eternity of love."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "beside.harmless" not in full_text

    def test_wrap_019_birth_ere(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: birth.ere
        passage = (
            "No angel-bright guardians watch'd over its birth,\n"
            "    Ere yet it was suffer'd to roam upon earth;\n"
            "    No spirits of gladness its soft form caress'd;\n"
            "    SIGHS mourned round its cradle, and hush'd it to rest."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "birth.ere" not in full_text

    def test_wrap_020_career_the(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: career.the
        passage = (
            "When it came upon earth, 'twas to choose a career,\n"
            "    The brightest and best that is left to a TEAR;\n"
            "    To hallow delight, and bestow the relief\n"
            "    Denied by despair to the fulness of grief."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "career.the" not in full_text

    def test_wrap_021_came_whether(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: came.whether
        passage = (
            "Few repell'd it--some bless'd it--wherever it came;\n"
            "    Whether soft'ning their sorrow, or soothing their shame;\n"
            "    And the joyful themselves, though its name they might fear,\n"
            "    Oft welcom'd the calming approach of the TEAR!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "came.whether" not in full_text

    def test_wrap_022_above_speeds(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: above.speeds
        passage = (
            "Years on years have worn onward, as--watch'd from above--\n"
            "    Speeds that meek spirit yet on its labour of love;\n"
            "    Still the exile of Heav'n, it ne'er shall away,\n"
            "    Every heart has a home for it, roam where it may!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "above.speeds" not in full_text

    def test_wrap_023_sky_the(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: sky.the
        passage = (
            "'The tempest-god's pinions o'ershadow the sky,\n"
            "    The waves leap to welcome the storm that is nigh,\n"
            "    Through the hall of old Odin re-echo the shocks\n"
            "    That the fierce ocean hurls at his rampart of rocks,\n"
            "    As, alone on the crags that soar up from the sands,\n"
            "    With his virgin SIONA the young AGNAR stands;\n"
            "    Tears sprinkle their dew on the sad maiden's cheeks,\n"
            "    And the voice of the chieftain sinks low while he speaks:"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sky.the" not in full_text

    def test_wrap_024_ever_numberd(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: ever.numberd
        passage = (
            "\"Crippled in the fight for ever,\n"
            "    Number'd with the worse than slain;\n"
            "    Weak, deform'd, disabled!--never\n"
            "    Can I join the hosts again!\n"
            "    With the battle that is won\n"
            "    AGNAR'S earthly course is run!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ever.numberd" not in full_text

    def test_wrap_025_light_float(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: light.float
        passage = (
            "\"See, athwart the face of light\n"
            "    Float the clouds of sullen Night!\n"
            "    Odin's warriors watch for me\n"
            "    By the earth-encircling sea!\n"
            "    The water's dirges howl my knell;\n"
            "    'Tis time I die--Farewell-Farewell!\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "light.float" not in full_text

    def test_wrap_026_arrayd_those(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: arrayd.those
        passage = (
            "Ah, Glyco! why in flow'rs array'd?\n"
            "    Those festive wreaths less quickly fade\n"
            "    Than briefly-blooming joy!\n"
            "    Those high-prized friends who share your mirth\n"
            "    Are counterfeits of brittle earth,\n"
            "    False coin'd in Death's alloy!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "arrayd.those" not in full_text

    def test_wrap_027_inspire_when(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: inspire.when
        passage = (
            "The bliss your notes could once inspire,\n"
            "    When lightly o'er the god-like lyre\n"
            "    Your nimble fingers pass'd,\n"
            "    Shall spring the same from others' skill--\n"
            "    When you're forgot, the music still\n"
            "    The player shall outlast!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "inspire.when" not in full_text

    def test_wrap_028_sky_that(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: sky.that
        passage = (
            "The sun-touch'd cloud that mounts the sky,\n"
            "    That brightly glows to warm the eye,\n"
            "    Then fades we know not where,\n"
            "    Is image of the little breath\n"
            "    Of life--and then, the doom of Death\n"
            "    That you and I must share!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sky.that" not in full_text

    def test_wrap_029_wait_the(self):
        # Source: Antonina or the Fall of Rome, wrap corruption: wait.the
        passage = (
            "Who, timely wise, would meanly wait\n"
            "    The dull delay of tardy Fate,\n"
            "    When Life's delights are shorn?\n"
            "    No!  When its outer gloss has flown,\n"
            "    Let's fling the tarnish'd bauble down\n"
            "    As lightly as 'twas worn."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "wait.the" not in full_text

    def test_wrap_030_armadale_oversteps(self):
        # Source: Armadale, wrap corruption: armadale.oversteps
        passage = (
            "Readers in particular will, I have some reason to suppose, be here\n"
            "and there disturbed, perhaps even offended, by finding that “Armadale”\n"
            " oversteps, in more than one direction, the narrow limits within which\n"
            "they are disposed to restrict the development of modern fiction--if they\n"
            "can."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "armadale.oversteps" not in full_text

    def test_wrap_031_facts_persisted(self):
        # Source: Armadale, wrap corruption: facts.persisted
        passage = (
            "“Will you oblige me, once for all, by confining yourself to the facts,”\n"
            " persisted Mr. Neal, frowning impatiently. “May I inquire, for my own\n"
            "information, whether Mrs. Armadale could tell you what it is her husband\n"
            "wishes me to write, and why it is that he refuses to let her write for\n"
            "him?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "facts.persisted" not in full_text

    def test_wrap_032_london_having(self):
        # Source: Armadale, wrap corruption: london.having
        passage = (
            "Mr. Neal folded the manuscript, inclosed it in a sheet of paper, and\n"
            "sealed it with Mr. Armadale’s own seal. “The address?” he said, with his\n"
            "merciless business formality. “To Allan Armadale, junior,” he wrote, as\n"
            "the words were dictated from the bed. “Care of Godfrey Hammick, Esq.,\n"
            "Offices of Messrs. Hammick and Ridge, Lincoln’s Inn Fields, London.”\n"
            " Having written the address, he waited, and considered for a moment. “Is\n"
            "your executor to open this?” he asked."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "london.having" not in full_text

    def test_wrap_033_steamer_asked(self):
        # Source: Armadale, wrap corruption: steamer.asked
        passage = (
            "“Do you remember the woman who threw herself from the river steamer?”\n"
            " asked the other--“the woman who caused that succession of deaths which\n"
            "opened Allan Armadale’s way to the Thorpe Ambrose estate?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "steamer.asked" not in full_text

    def test_wrap_034_writingwhi_concluded(self):
        # Source: Armadale, wrap corruption: writingwhich.concluded
        passage = (
            "“Read that, doctor,” said Allan, as Mr. Hawbury opened the written\n"
            "paper. “It’s not told in my roundabout way; but there’s nothing added\n"
            "to it, and nothing taken away. It’s exactly what I dreamed, and exactly\n"
            "what I should have written myself, if I had thought the thing worth\n"
            "putting down on paper, and if I had had the knack of writing--which,”\n"
            " concluded Allan, composedly stirring his coffee, “I haven’t, except it’s\n"
            "letters; and I rattle them off in no time.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "writingwhich.concluded" not in full_text

    def test_wrap_035_now_answered(self):
        # Source: Armadale, wrap corruption: now.answered
        passage = (
            "“I think it’s a very good thing your papa’s friend is not here now,”\n"
            " answered the outspoken Allan; “I should quarrel with him to a dead\n"
            "certainty. As for society, Miss Milroy, nobody knows less about it than\n"
            "I do; but if we had an old lady here, I must say myself I think she\n"
            "would be uncommonly in the way. Won’t you?” concluded Allan, imploringly\n"
            "offering his arm for the second time. “Do!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "now.answered" not in full_text

    def test_wrap_036_way_replied(self):
        # Source: Armadale, wrap corruption: way.replied
        passage = (
            "“With the greatest pleasure, Major Milroy, if I am not in the way,”\n"
            " replied Allan, delighted at his reception. “I was sorry to hear from\n"
            "Miss Milroy that Mrs. Milroy is an invalid. Perhaps my being here\n"
            "unexpectedly; perhaps the sight of a strange face--”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "way.replied" not in full_text

    def test_wrap_037_armadale_she(self):
        # Source: Armadale, wrap corruption: armadale.she
        passage = (
            "She gave him her hand. “No more apologies, if you please, Mr. Armadale,”\n"
            " she said, saucily. Once more their eyes met, and once more the plump,\n"
            "dimpled little hand found its way to Allan’s lips. “It isn’t an apology\n"
            "this time!” cried Allan, precipitately defending himself. “It’s--it’s a\n"
            "mark of respect.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "armadale.she" not in full_text

    def test_wrap_038_family_said(self):
        # Source: Armadale, wrap corruption: family.said
        passage = (
            "“There’s a screw loose somewhere, sir, in Major Milroy’s family,”\n"
            " said the voice of young Pedgift. “Did you notice how the major and his\n"
            "daughter looked when Miss Gwilt made her excuses for being late at the\n"
            "Mere? You don’t remember? Do you remember what Miss Gwilt said?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "family.said" not in full_text

    def test_wrap_039_armadale_more(self):
        # Source: Armadale, wrap corruption: armadale.more
        passage = (
            "Allan looked at the address. It was in a strange handwriting. He opened\n"
            "the letter, and a little note inclosed in it dropped to the ground.\n"
            "The note was directed, still in the strange handwriting, to “Mrs.\n"
            "Mandeville, 18 Kingsdown Crescent, Bayswater. Favored by Mr. Armadale.”\n"
            " More and more surprised, Allan turned for information to the signature\n"
            "at the end of the letter. It was “Anne Milroy.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "armadale.more" not in full_text

    def test_wrap_040_letter_said(self):
        # Source: Armadale, wrap corruption: letter.said
        passage = (
            "If Mr. Bashwood had been caught in the act of committing murder, he\n"
            "could hardly have shown greater alarm than he now testified at Allan’s\n"
            "sudden discovery of him. Snatching off his dingy old hat, he bowed\n"
            "bare-headed, in a palsy of nervous trembling from head to foot. “No,\n"
            "sir--no, sir; only a little letter, a little letter, a little letter,”\n"
            " said the deputy-steward, taking refuge in reiteration, and bowing\n"
            "himself swiftly backward out of his employer’s sight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "letter.said" not in full_text

    def test_wrap_041_women_thought(self):
        # Source: Armadale, wrap corruption: women.thought
        passage = (
            "“Certainly!” assented young Pedgift. “Sketch it in outline, sir. The\n"
            "merest hint will do; I wasn’t born yesterday.” (“Oh, these women!”\n"
            " thought the youthful philosopher, in parenthesis.)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "women.thought" not in full_text

    def test_wrap_042_neighborho_said(self):
        # Source: Armadale, wrap corruption: neighborhood.said
        passage = (
            "“You can horsewhip a man, sir; but you can’t horsewhip a neighborhood,”\n"
            " said the lawyer, in his politely epigrammatic manner. “We will fight our\n"
            "battle, if you please, without borrowing our weapons of the coachman yet\n"
            "a while, at any rate.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "neighborhood.said" not in full_text

    def test_wrap_043_now_pursued(self):
        # Source: Armadale, wrap corruption: now.pursued
        passage = (
            "“Give me your hand, Mr. Armadale!” cried Pedgift Senior, warmly; “I\n"
            "honor you for being so angry with me. The neighborhood may say what it\n"
            "pleases; you’re a gentleman, sir, in the best sense of the word. Now,”\n"
            " pursued the lawyer, dropping Allan’s hand, and lapsing back instantly\n"
            "from sentiment to business, “just hear what I have got to say in my own\n"
            "defense. Suppose Miss Gwilt’s real position happens to be nothing like\n"
            "what you are generously determined to believe it to be?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "now.pursued" not in full_text

    def test_wrap_044_kind_exclaimed(self):
        # Source: Armadale, wrap corruption: kind.exclaimed
        passage = (
            "“You ought to have told her at once that I thought nothing of the kind!”\n"
            " exclaimed Allan, indignantly. “Why did you leave her a moment in doubt\n"
            "about it?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "kind.exclaimed" not in full_text

    def test_wrap_045_comes_once(self):
        # Source: Armadale, wrap corruption: comes.once
        passage = (
            "“Please to have a fly at the door at half-past ten,” said Miss Gwilt,\n"
            "as the amazed landlady followed her upstairs. “And excuse me, you good\n"
            "creature, if I beg and pray not to be disturbed till the fly comes.”\n"
            " Once inside the room, she locked the door, and then opened her\n"
            "writing-desk. “Now for my letter to the major!” she said. “How shall I\n"
            "word it?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "comes.once" not in full_text

    def test_wrap_046_there_said(self):
        # Source: Armadale, wrap corruption: there.said
        passage = (
            "The porter took him by the arm, and led him out. “You’ll get it there,”\n"
            " said the man, pointing confidentially to a public-house; “and you’ll get\n"
            "it good.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "there.said" not in full_text

    def test_wrap_047_address_with(self):
        # Source: Armadale, wrap corruption: address.with
        passage = (
            "The spy laid a card on the table. “I’ll come back for him or send for\n"
            "him,” he said. “I suppose I can go now, if I leave my name and address?”\n"
            " With those words, he put on his hat, and walked out."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "address.with" not in full_text

    def test_wrap_048_use_suggested(self):
        # Source: Armadale, wrap corruption: use.suggested
        passage = (
            "“I’m sorry, sir--I’m sure I’m very sorry. If I could be of any use--”\n"
            " suggested Mr. Bashwood, speaking under the influence in some degree of\n"
            "his nervous politeness, and in some degree of his remembrance of what\n"
            "Midwinter had done for him at Thorpe Ambrose in the by-gone time."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "use.suggested" not in full_text

    def test_wrap_049_life_she(self):
        # Source: Armadale, wrap corruption: life.she
        passage = (
            "“Offer me the strongest sleeping draught you ever made in your life,”\n"
            " she replied. “And leave me alone till the time comes to take it. I\n"
            "shall be your patient in earnest!” she added, fiercely, as the doctor\n"
            "attempted to remonstrate. “I shall be the maddest of the mad if you\n"
            "irritate me to-night!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "life.she" not in full_text

    def test_wrap_050_sir_she(self):
        # Source: Armadale, wrap corruption: sir.she
        passage = (
            "“The lady has ordered me to call her to-morrow at seven o’clock, sir,”\n"
            " she said. “She means to fetch her luggage herself, and she wants to have\n"
            "a cab at the door as soon as she is dressed. What am I to do?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sir.she" not in full_text

    def test_wrap_051_treat_they(self):
        # Source: Armadale, wrap corruption: treat.they
        passage = (
            "In another quarter of an hour the doctor had expounded his views on\n"
            "cookery and diet, and the visitors (duly furnished with prospectuses)\n"
            "were taking leave of him at the door. “Quite an intellectual treat!”\n"
            " they said to each other, as they streamed out again in neatly dressed\n"
            "procession through the iron gates. “And what a very superior man!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "treat.they" not in full_text

    def test_wrap_052_all_asked(self):
        # Source: Armadale, wrap corruption: all.asked
        passage = (
            "“Pardon me,” he resumed, “I thought I heard something downstairs. With\n"
            "regard to the little hitch that I adverted to just now, permit me to\n"
            "inform you that Mr. Armadale has brought a friend here with him, who\n"
            "bears the strange name of Midwinter. Do you know the gentleman at all?”\n"
            " asked the doctor, with a suspicious anxiety in his eyes, which strangely\n"
            "belied the elaborate indifference of his tone."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.asked" not in full_text

    def test_wrap_053_temper_rejoined(self):
        # Source: Armadale, wrap corruption: temper.rejoined
        passage = (
            "“Mr. Midwinter is a person of coarse manners and suspicious temper,”\n"
            " rejoined the doctor, steadily watching her. “He was rude enough\n"
            "to insist on staying here as soon as Mr. Armadale had accepted my\n"
            "invitation.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "temper.rejoined" not in full_text

    def test_wrap_054_livings_and(self):
        # Source: Basil, wrap corruption: livings.and
        passage = (
            "When I returned home, it was thought necessary, as I was a younger son,\n"
            "and could inherit none of the landed property of the family, except in\n"
            "the case of my brother’s dying without children, that I should belong\n"
            "to a profession. My father had the patronage of some valuable “livings,”\n"
            " and good interest with more than one member of the government. The\n"
            "church, the army, the navy, and, in the last instance, the bar, were\n"
            "offered me to choose from. I selected the last."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "livings.and" not in full_text

    def test_wrap_055_sherwin_over(self):
        # Source: Basil, wrap corruption: sherwin.over
        passage = (
            "I reached the place: there was the shop, and there the name “Sherwin”\n"
            " over the door. One chance still remained. This Sherwin and the Sherwin\n"
            "of Hollyoake Square might not be the same."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sherwin.over" not in full_text

