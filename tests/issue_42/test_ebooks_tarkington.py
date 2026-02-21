import pytest
from fast_sentence_segment import segment_text


class TestEbooksTarkington:
    """Integration tests mined from Booth Tarkington ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1910s
    """

    def test_wrap_001_chance_she(self):
        # Source: Alice Adams, wrap corruption: chance.she
        passage = (
            "For the second time that morning--it was now a little after seven\n"
            "o'clock--tears seemed about to offer their solace to Mrs. Adams. “I\n"
            "might have expected you to say that, Alice; you never do miss a chance,”\n"
            " she said, gently. “It seems queer you don't some time miss just ONE\n"
            "chance!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "chance.she" not in full_text

    def test_wrap_002_there_she(self):
        # Source: Alice Adams, wrap corruption: there.she
        passage = (
            "“Please don't talk like that,” Alice said, quickly. “I'm old enough to\n"
            "realize that papa may need pressure of all sorts; I only think it makes\n"
            "him more obstinate to get him cross. You probably do understand him\n"
            "better, but that's one thing I've found out and you haven't. There!”\n"
            " She gave her mother a friendly tap on the shoulder and went to the door.\n"
            "“I'll hop in and say hello to him now.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "there.she" not in full_text

    def test_wrap_003_papa_she(self):
        # Source: Alice Adams, wrap corruption: papa.she
        passage = (
            "His voice had become tremulous in spite of him; and this sign of\n"
            "weakness and emotion had sufficient effect upon Alice. She bent over him\n"
            "suddenly, with her arm about him and her cheek against his. “Poor papa!”\n"
            " she murmured. “Poor papa!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "papa.she" not in full_text

    def test_wrap_004_you_she(self):
        # Source: Alice Adams, wrap corruption: you.she
        passage = (
            "“I'm sure Mildred will be needing you,” Alice said, and as she took his\n"
            "arm and they walked toward Mrs. Dresser, she thought it might be just\n"
            "possible to make a further use of the loan. “Oh, I wonder if you----”\n"
            " she began."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.she" not in full_text

    def test_wrap_005_something_but(self):
        # Source: Alice Adams, wrap corruption: something.but
        passage = (
            "“I want to go on the stage: I know I could act.” At this, her father\n"
            "abruptly gave utterance to a feeble cackling of laughter; and when\n"
            "Alice, surprised and a little offended, pressed him for his reason, he\n"
            "tried to evade, saying, “Nothing, dearie. I just thought of something.”\n"
            " But she persisted until he had to explain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "something.but" not in full_text

    def test_wrap_006_mama_she(self):
        # Source: Alice Adams, wrap corruption: mama.she
        passage = (
            "During the long illness the “glue factory” was completely forgotten, by\n"
            "Alice at least; and her laugh was rueful as well as derisive now, in the\n"
            "kitchen, when she realized that her mother's mind again dwelt upon this\n"
            "abandoned nuisance. “I thought you'd got over all that nonsense, mama,”\n"
            " she said."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mama.she" not in full_text

    def test_wrap_007_thing_shes(self):
        # Source: Alice Adams, wrap corruption: thing.shes
        passage = (
            "“I was walkin' out on Monday with my sweet thing.\n"
            "     She's my neat thing,\n"
            "     My sweet thing:\n"
            "     I'll go round on Tuesday night to see her.\n"
            "     Oh, how we'll spoon----”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thing.shes" not in full_text

    def test_wrap_008_business_she(self):
        # Source: Alice Adams, wrap corruption: business.she
        passage = (
            "“I suppose most quarrels between families are on account of business,”\n"
            " she said. “That's why they're so sordid. Certainly the Lambs seem a\n"
            "sordid lot to me, though of course I'm biased.” And with that she began\n"
            "to sketch a history of the commercial antagonism that had risen between\n"
            "the Adamses and the Lambs."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "business.she" not in full_text

    def test_wrap_009_mimi_she(self):
        # Source: Alice Adams, wrap corruption: mimi.she
        passage = (
            "As he spoke, a song came to them from a lighted window over their heads.\n"
            "Then the window darkened abruptly, but the song continued as Alice went\n"
            "down through the house to wait on the little veranda. “Mi chiamo Mimi,”\n"
            " she sang, and in her voice throbbed something almost startling in its\n"
            "sweetness. Her father and mother listened, not speaking until the song\n"
            "stopped with the click of the wire screen at the front door as Alice\n"
            "came out."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mimi.she" not in full_text

    def test_wrap_010_reason_mildred(self):
        # Source: Alice Adams, wrap corruption: reason.mildred
        passage = (
            "“I think his colour and his not listening came from the same reason,”\n"
            " Mildred said, and although she had come to sit near her mother, she\n"
            "did not look at her. “I think it happened because you and papa----” She\n"
            "stopped."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "reason.mildred" not in full_text

    def test_wrap_011_anyhow_she(self):
        # Source: Alice Adams, wrap corruption: anyhow.she
        passage = (
            "“How foolish! I think it's fun, getting ready to entertain a little\n"
            "again, like this. I only wish it hadn't turned so hot: I'm afraid your\n"
            "poor father'll suffer--his things are pretty heavy, I noticed. Well,\n"
            "it'll do him good to bear something for style's sake this once, anyhow!”\n"
            " She laughed, and coming to Alice, bent down and kissed her. “Dearie,”\n"
            " she said, tenderly, “wouldn't you please slip upstairs now and take just\n"
            "a little teeny nap to please your mother?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "anyhow.she" not in full_text

    def test_wrap_012_world_but(self):
        # Source: Alice Adams, wrap corruption: world.but
        passage = (
            "“I tell you, you're crazy!” Lamb said again. “I never in the world----”\n"
            " But he checked himself, staring in sudden perplexity at his accuser.\n"
            "“Look here!” he said. “What's the matter of you? Have you got another of\n"
            "those----?” He put his hand upon Adams's shoulder, which jerked feebly\n"
            "under the touch."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "world.but" not in full_text

    def test_wrap_013_amawnin_she(self):
        # Source: Beasleys Christmas Party, wrap corruption: amawnin.she
        passage = (
            "“Ah met mah sistuh in a-mawnin',\n"
            "     She 'uz a-waggin' up de hill SO slow!\n"
            "     'Sistuh, you mus' git a rastle in doo time,\n"
            "     B'fo de hevumly do's cloze--iz!'”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "amawnin.she" not in full_text

    def test_wrap_014_despatch_office(self):
        # Source: Beasleys Christmas Party, wrap corruption: despatch.office
        passage = (
            "It happened that I thus met him, as we were both starting down-town, and\n"
            "walked on with him, several days in succession; in a word, it became a\n"
            "habit. Then, one afternoon, as I turned to leave him at the “Despatch”\n"
            " office, he asked me if I wouldn't drop in at his house the next day for\n"
            "a cigar before we started. I did; and he asked me if I wouldn't come\n"
            "again the day after that. So this became a habit, too."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "despatch.office" not in full_text

    def test_wrap_015_with_working(self):
        # Source: Bimbo the Pirate a Comedy, wrap corruption: with.working
        passage = (
            "“On the Sabbath Day only such tasks were permitted as had to do with\n"
            "  working of the Ship and there was no Diversion ... but to read books\n"
            "  of a religious nature.”--_Narrative of a Seaman Captured and Forced\n"
            "  by Pirates._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "with.working" not in full_text

    def test_wrap_016_the_subject(self):
        # Source: Bimbo the Pirate a Comedy, wrap corruption: the.subject
        passage = (
            "=THE ART OF MAKE-UP= By HELENA CHALMERS. A complete book on the\n"
            "  subject of make-up, treating make-up for the stage, motion pictures,\n"
            "  minstrels, fancy dress balls, and for the street. Illustrated. $2.00."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.subject" not in full_text

    def test_wrap_017_practical_suggestion(self):
        # Source: Bimbo the Pirate a Comedy, wrap corruption: practical.suggestions
        passage = (
            "=A LIST OF MUSIC FOR PLAYS and PAGEANTS= By ROLAND HOLT. Practical\n"
            "  suggestions on organizing the musical program to accompany plays\n"
            "  and pageants; lists of music suitable for every sort of dramatic\n"
            "  situation. $1.00."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "practical.suggestions" not in full_text

    def test_wrap_018_steele_four(self):
        # Source: Bimbo the Pirate a Comedy, wrap corruption: steele.four
        passage = (
            "=THE TERRIBLE WOMAN and Other One-Act Plays= By WILBUR DANIEL STEELE.\n"
            "  Four vivid and actable plays. The Terrible Woman, a comedy of a\n"
            "  wise wife and mother. (2m. 2w.) The Giant’s Stair, an eerie drama\n"
            "  of horror and fear in a mountain cabin. (2m. 2w.) Not Smart, a\n"
            "  farcical satire on “parlor radicalism.” (2m. 3w.) Ropes, a gripping\n"
            "  drama set in a lonely lighthouse. (2m. 2w.) $1.75."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "steele.four" not in full_text

    def test_wrap_019_goodman_and(self):
        # Source: Bimbo the Pirate a Comedy, wrap corruption: goodman.and
        passage = (
            "=THE WONDER HAT and Other One-Act Plays= By KENNETH SAWYER GOODMAN\n"
            "  and BEN HECHT. A volume of five short plays. The Wonder Hat, a\n"
            "  fantastic Pierrot comedy. (3m. 2w.) The Two Lamps, a wartime spy\n"
            "  melodrama. (7m. 2w.) An Idyll of the Shops, a poignant drama of a\n"
            "  garment sweat shop. (3m. 3w.) The Hand of Siva, an absorbing drama\n"
            "  laid in an army post in India. (5m.) The Hero of Santa Maria, a\n"
            "  comedy based on the fictitious death of a man in the battle of Santa\n"
            "  Maria. (6m. 1w.) $1.75."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "goodman.and" not in full_text

    def test_wrap_020_love_lush(self):
        # Source: Gentle Julia, wrap corruption: love.lush
        passage = (
            "\"I--And Love!\n"
            "    Lush white lilies line the pool\n"
            "    Like laces limned on looking-glasses!\n"
            "    I tread the lilies underfoot,\n"
            "    Careless how they love me!\n"
            "      Still white maidens woo me,\n"
            "      Win me not!\n"
            "        But thou!\n"
            "        Thou art a cornflower\n"
            "    Sapphire-eyed!\n"
            "          I bend!\n"
            "        Cornflower, I ask a question.\n"
            "    O flower, speak----\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "love.lush" not in full_text

    def test_wrap_021_rasmile_the(self):
        # Source: Gentle Julia, wrap corruption: rasmile.the
        passage = (
            "\"Geev a-mee yewr ra-smile,\n"
            "      The luv va-ligh TIN yew rise,\n"
            "      Life cooed not hold a fairrerr paradise.\n"
            "    Geev a-mee the righ to luv va-yew all the wile,\n"
            "      My worrlda for AIV-vorr,\n"
            "    The sunshigh NUV vyewr-ra-smile!\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rasmile.the" not in full_text

    def test_wrap_022_backyrad_tis(self):
        # Source: Gentle Julia, wrap corruption: backyrad.tis
        passage = (
            "A new ditch is being dug accross the MR. Henry D. Vance backyrad.\n"
            "    ;Tis about dug but nobody is working there now. Patty Fairchild\n"
            "    received the highest mark in declamation of the 7A at Sumner School\n"
            "    last Friday."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "backyrad.tis" not in full_text

    def test_wrap_023_geo_the(self):
        # Source: Gentle Julia, wrap corruption: geo.the
        passage = (
            "Balf's grorcey wagon ran over a cat of the Mr. Rayfort family. Geo.\n"
            "    the driver of the wagom stated he had not but was willing to take\n"
            "    it away and burg it somewheres Geo. stated regret and claimed\n"
            "    nothing but an accident which could not be helped and not his team\n"
            "    that did the damage."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "geo.the" not in full_text

    def test_wrap_024_washes_their(self):
        # Source: Gentle Julia, wrap corruption: washes.their
        passage = (
            "Been Kriso the cHauffeur of the Mr. R. G. Atwater family washes\n"
            "    their car on Monday. In using the hose he turned water over the\n"
            "    fence accidently and hit Lonnie the washWOman in back of MRS.\n"
            "    Bruffs who called him some low names. Ben told her if he had have\n"
            "    been a man he wrould strike her but soon the distrubance was at an\n"
            "    end. There is a good deal more of other news which will be printed\n"
            "    in our next NO."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "washes.their" not in full_text

    def test_wrap_025_propietors_subscribe(self):
        # Source: Gentle Julia, wrap corruption: propietors.subscribe
        passage = (
            "Atwater & Co., Owners & Propietors\n"
            "    Subscribe NOW 25 cents Per. Year. Sub-\n"
            "    scriptions should be brought to the East\n"
            "    Main Entrance of Atwater & Co., News-\n"
            "       paper  Building  every afternoon\n"
            "          430  to  VI  25 Cents"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "propietors.subscribe" not in full_text

    def test_wrap_026_dreary_then(self):
        # Source: Gentle Julia, wrap corruption: dreary.then
        passage = (
            "When my heart is dreary\n"
            "        Then my soul is weary\n"
            "        As a bird with a broken wing\n"
            "    Who never again will sing\n"
            "    Like the sound of a vast amen\n"
            "    That comes from a church of men."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dreary.then" not in full_text

    def test_wrap_027_the_present(self):
        # Source: Gentle Julia, wrap corruption: the.present
        passage = (
            "The MR. Rayfort family of this City have been presentde with the\n"
            "    present of a new Cat by Geo. the man employeD by Balf & CO. This\n"
            "    cat is perfectly baeutiful and still quit young."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.present" not in full_text

    def test_wrap_028_soth_the(self):
        # Source: Gentle Julia, wrap corruption: soth.the
        passage = (
            "Miss Julia Atwater of this City is visiting friends in the Soth.\n"
            "    The family have had many letters from her that are read by each and\n"
            "    all of the famild."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "soth.the" not in full_text

    def test_wrap_029_family_stating(self):
        # Source: Gentle Julia, wrap corruption: family.stating
        passage = (
            "Miss Julia Atwater of this City wrote a letter to the family\n"
            "    stating while visiting in the SOuth she has made an engagement to\n"
            "    be married to MR. Crum of that City. The family do not know who\n"
            "    this MR. Crum is but It is said he is a widower though he has been\n"
            "    diVorced with a great many children."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "family.stating" not in full_text

    def test_wrap_030_hanscom_grew(self):
        # Source: Harlequin and Columbine, wrap corruption: hanscom.grew
        passage = (
            "For two hours, responding to the manipulation of the star and his\n"
            "thoroughly subjugated playwright, the character of “Roderick Hanscom”\n"
            " grew nobler and nobler, speech by speech and deed by deed, while the\n"
            "expression of the gentleman who was to impersonate it became, in precise\n"
            "parallel with this regeneration, sweeter and loftier and lovelier."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hanscom.grew" not in full_text

    def test_wrap_031_ingenue_both(self):
        # Source: Harlequin and Columbine, wrap corruption: ingenue.both
        passage = (
            "Miss Ellsling and a youth of the company took their places near the\n"
            "front of the stage and began the rehearsal of the second act with a\n"
            "dialogue that led up to the entrance of the star with the “ingenue,”\n"
            " both of whom still remained out of the playwright's range of vision."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ingenue.both" not in full_text

    def test_wrap_032_room_said(self):
        # Source: Harlequin and Columbine, wrap corruption: room.said
        passage = (
            "“We used to settle the universe in that little back restaurant room,”\n"
            " said Rieger. “Not one of use had ever got a thing into print--and me, I\n"
            "haven't yet, for that matter. Editors still hate my stuff. I've kept my\n"
            "oath, though; I've never compromised--never for a moment.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "room.said" not in full_text

    def test_wrap_033_films_slender(self):
        # Source: His Own People, wrap corruption: films.slender
        passage = (
            "While trails of scent, like cobweb's films\n"
            "         Slender and faint and rare,\n"
            "       Of roses, and rich, fair fabrics,\n"
            "         Cling on the stirless air,\n"
            "       The sibilance of voices,\n"
            "         At a wave of Milady's glove,\n"
            "       Is stilled--"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "films.slender" not in full_text

    def test_wrap_034_assembly_they(self):
        # Source: His Own People, wrap corruption: assembly.they
        passage = (
            "She sang to that great assembly,\n"
            "         They thought, as they praised her tone;\n"
            "       But she and my heart knew better:\n"
            "         Her song was for me alone."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "assembly.they" not in full_text

    def test_wrap_035_vaurigard_young(self):
        # Source: His Own People, wrap corruption: vaurigard.young
        passage = (
            "“Stop!” Mellin flung one arm up violently, striking the headboard with\n"
            "his knuckles. “I won't hear a syllable against Madame de Vaurigard!”\n"
            " Young Cooley regarded him steadily for a moment. “Have you remembered\n"
            "yet,” he said slowly, “how much you lost last night?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "vaurigard.young" not in full_text

    def test_wrap_036_you_and(self):
        # Source: In the Arena Stories of Political Life, wrap corruption: you.and
        passage = (
            "“Toby,” she said, “lieber Toby, I am so all-lofing by you--you are\n"
            "sitch a good maan--I am so--so--I am yoost all-lofing by you!”\n"
            " And she cried heartily upon his shoulder. “Toby, uf you ain'd here for\n"
            "me to-morrow by eckseckly dwelf o'glock, uf you are von minutes late,\n"
            "I'm goin' yoost fall down deat! Don' you led nothings happen mit you,\n"
            "Toby.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.and" not in full_text

    def test_wrap_037_long_which(self):
        # Source: In the Arena Stories of Political Life, wrap corruption: long.which
        passage = (
            "That was only the beginning. He had, indeed, “found his voice”; for he\n"
            "seldom went now to the boarding-house for his meals, but patronized\n"
            "the free-lunch counter and other allurements of the establishment\n"
            "across the way. Every day he rose in the House to speak, never failing\n"
            "to reach the assertion that he was “as honest as the day is long,”\n"
            " which was always greeted in the same way."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "long.which" not in full_text

    def test_wrap_038_bridge_and(self):
        # Source: In the Arena Stories of Political Life, wrap corruption: bridge.and
        passage = (
            "When he'd worked us through that, and perhaps “Horatius at the Bridge”\n"
            " and the quarrel scene between Brutus and Cassius and was pretty well\n"
            "emptied, he'd hang about and interrupt in a way that made me\n"
            "restless. Neither Mary nor I could get out two sentences before the\n"
            "boy would cut in with something like: “Don't tell cousin Ben about\n"
            "that day I recited in school; I'm tired of all that guff!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bridge.and" not in full_text

    def test_wrap_039_scored_and(self):
        # Source: In the Arena Stories of Political Life, wrap corruption: scored.and
        passage = (
            "The speech was about what I was looking for: bombastic platitudes\n"
            "delivered with such earnestness and velocity that “every point scored”\n"
            " and the cheering came whenever he wanted it."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "scored.and" not in full_text

    def test_wrap_040_laiglon_enthusiasm(self):
        # Source: In the Arena Stories of Political Life, wrap corruption: laiglon.enthusiasm
        passage = (
            "We talked of other things, then, until such time as we found ourselves\n"
            "seated by a small table at the club, old Tom somewhat uneasily\n"
            "regarding a twisted cigar he was smoking and plainly confounded by the\n"
            "“carbonated” syphon, for which, indeed, he had no use in the world.\n"
            "We had been joined by little Fiderson, the youngest member of the\n"
            "club, whose whole nervous person jerkily sparkled “L'Aiglon”\n"
            " enthusiasm."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "laiglon.enthusiasm" not in full_text

    def test_wrap_041_true_she(self):
        # Source: Monsieur Beaucaire, wrap corruption: true.she
        passage = (
            "Her eyes were not lifted. She went on: “We come, in time, to believe\n"
            "that true feeling comes faltering forth, not glibly; that smoothness\n"
            "betokens the adept in the art, sir, rather than your true--your true--”\n"
            " She was herself faltering; more, blushing deeply, and halting to a full\n"
            "stop in terror of a word. There was a silence."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "true.she" not in full_text

    def test_wrap_042_monseigneu_the(self):
        # Source: Monsieur Beaucaire, wrap corruption: monseigneur.the
        passage = (
            "There was borne on the breeze an answer--“Monseigneur! Monseigneur!”\n"
            " The cry grew louder suddenly. The clatter of hoofs urged to an anguish\n"
            "of speed sounded on the night. M. Beaucaire's servants had lagged sorely\n"
            "behind, but they made up for it now. Almost before the noise of their\n"
            "own steeds they came riding down the moonlit aisle between the mists.\n"
            "Chosen men, these servants of Beaucaire, and like a thunderbolt they\n"
            "fell upon the astounded cavaliers."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "monseigneur.the" not in full_text

    def test_wrap_043_hour_said(self):
        # Source: Monsieur Beaucaire, wrap corruption: hour.said
        passage = (
            "“The Duke of Orleans will receive a message from me within the hour!”\n"
            " said Winterset, as he made his way to the door. His face was black with\n"
            "rage and shame."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hour.said" not in full_text

    def test_wrap_044_bing_inflicted(self):
        # Source: Penrod and Sam, wrap corruption: bing.inflicted
        passage = (
            "He passed from the sidewalk into his own yard, with a subdued “Bing!”\n"
            " inflicted upon the stolid person of a gatepost, and, entering the house\n"
            "through the kitchen, ceased to bing for a time. However, driven back\n"
            "from the fore part of the house by a dismal sound of callers, he\n"
            "returned to the kitchen and sat down."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bing.inflicted" not in full_text

    def test_wrap_045_monday_penrod(self):
        # Source: Penrod and Sam, wrap corruption: monday.penrod
        passage = (
            "“Well, nobody with any sense cares if it rains Sunday and Monday,”\n"
            " Penrod said. “I wouldn't care if it rained every Sunday as long I lived;\n"
            "but I just like to know what's the reason it had to go and rain to-day.\n"
            "Got all the days o' the week to choose from and goes and picks on\n"
            "Saturday. That's a fine biz'nuss!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "monday.penrod" not in full_text

    def test_wrap_046_say_then(self):
        # Source: Penrod and Sam, wrap corruption: say.then
        passage = (
            "“Make 'em step back there!” he commanded his myrmidons savagely. “Fix\n"
            "it so's your horses'll step on their feet if they don't do what I say!”\n"
            " Then, from his shining saddle, he watched the throngs slinking away. “I\n"
            "guess they know who I am NOW!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "say.then" not in full_text

    def test_wrap_047_glad_and(self):
        # Source: Penrod and Sam, wrap corruption: glad.and
        passage = (
            "“Sammy's mad, and I am glad,\n"
            "     And I know what will please him:\n"
            "       A bottle o' wine to make him shine,\n"
            "     And Mabel Rorebeck to squeeze him!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "glad.and" not in full_text

    def test_wrap_048_were_said(self):
        # Source: Penrod and Sam, wrap corruption: were.said
        passage = (
            "“Your sister telephoned to our house to see if I knew where you were,”\n"
            " said Sam. “She told me if I saw you before you got home to tell you\n"
            "sumpthing; but not to say anything about it. She said Miss Spence had\n"
            "telephoned to her, but she said for me to tell you it was all right\n"
            "about that letter, and she wasn't goin' to tell your mother and father\n"
            "on you, so you needn't say anything about it to 'em.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "were.said" not in full_text

    def test_wrap_049_think_unfortunat(self):
        # Source: Penrod and Sam, wrap corruption: think.unfortunately
        passage = (
            "“Of course I didn't mean it, Penrod,” she said, at the first opportunity\n"
            "upon their homeward way. “I didn't notice--that is, I didn't think--”\n"
            " Unfortunately for the effect of sincerity she hoped to produce, her\n"
            "voice became tremulous and her shoulders moved suspiciously."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "think.unfortunately" not in full_text

    def test_wrap_050_chilly_neither(self):
        # Source: Penrod and Sam, wrap corruption: chilly.neither
        passage = (
            "“I was out in the sawdust-box,” he said, “but it got kind of chilly.”\n"
            " Neither of his auditors felt called upon to offer any comment, and\n"
            "presently he added, “I thought I better come in here where it's warmer.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "chilly.neither" not in full_text

    def test_wrap_051_about_his(self):
        # Source: Penrod and Sam, wrap corruption: about.his
        passage = (
            "“Where what?” Mr. Schofield asked testily. “What are you talking about?”\n"
            " His nerves were jarred, and he was rather hoarse after what he had been\n"
            "saying to Penrod. (That regretful necromancer was now upstairs doing\n"
            "unhelpful things to his nose over a washstand.) “What do you mean by,\n"
            "'Where, where, where?'” Mr. Schofield demanded. “I don't see any sense\n"
            "to it.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "about.his" not in full_text

    def test_wrap_052_ptawptaw_while(self):
        # Source: Penrod and Sam, wrap corruption: ptawptaw.while
        passage = (
            "Penrod was preoccupied at dinner and during the evening, now and then\n"
            "causing his father some irritation by croaking, “Taw, p'taw-p'taw!”\n"
            " while the latter was talking. And when bedtime came for the son of the\n"
            "house, he mounted the stairs in a rhythmic manner, and p'tawed himself\n"
            "through the upper hall as far as his own chamber."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ptawptaw.while" not in full_text

    def test_wrap_053_place_sam(self):
        # Source: Penrod and Sam, wrap corruption: place.sam
        passage = (
            "“Well, whyn't you say he was 'cross the street in the first place?”\n"
            " Sam returned plaintively. “Besides, he's so little you can't hardly\n"
            "see him.” This was, of course, a violent exaggeration, though Master\n"
            "Chitten, not yet eleven years old, was an inch or two short for his age.\n"
            "“He's all dressed up,” Sam added. “I guess he must be invited.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "place.sam" not in full_text

    def test_wrap_054_anyway_neither(self):
        # Source: Penrod and Sam, wrap corruption: anyway.neither
        passage = (
            "“Well,” said Sam darkly, “he's goin' to be sorry he stuck ME, anyway!”\n"
            " Neither Sam nor Maurice had even the vaguest plan for causing the\n"
            "desired regret in the breast of Master Chitten; but both derived a\n"
            "little consolation from these prophecies. And they, too, had aligned\n"
            "themselves with the insurgents. Their motives were personal--Carlie\n"
            "Chitten had wronged both of them, and Carlie was conspicuously in high\n"
            "favour with the Authorities. Naturally Sam and Maurice were against the\n"
            "Authorities."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "anyway.neither" not in full_text

    def test_wrap_055_child_gentulhear(self):
        # Source: Penrod, wrap corruption: child.gentulhearted
        passage = (
            "“'I hight Sir Lancelot du Lake, the Child,\n"
            "     Gentul-hearted, meek, and mild.\n"
            "     What though I'm BUT a littul child,\n"
            "     Gentul-hearted, meek, and----'  OOF!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "child.gentulhearted" not in full_text

