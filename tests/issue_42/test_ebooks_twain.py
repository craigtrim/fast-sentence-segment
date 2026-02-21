import pytest
from fast_sentence_segment import segment_text


class TestEbooksTwain:
    """Integration tests mined from Mark Twain ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1890s
    """

    def test_wrap_001_excitement_relates(self):
        # Source: 1601 Conversation As It Was by the Social Fireside in the Time of the Tudors, wrap corruption: excitement.relates
        passage = (
            "In San Francisco in the sizzling sixties we catch a glimpse of Mark\n"
            "Twain and his buddy, Steve Gillis, pausing in doorways to sing “The\n"
            "Doleful Ballad of the Neglected Lover,” an old piece of uncollected\n"
            "erotica. One morning, when a dog began to howl, Steve awoke “to find\n"
            "his room-mate standing in the door that opened out into a back garden,\n"
            "holding a big revolver, his hand shaking with cold and excitement,”\n"
            " relates Paine in his Biography."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "excitement.relates" not in full_text

    def test_wrap_002_king_agrivance(self):
        # Source: A Connecticut Yankee in King Arthurs Court Part 5, wrap corruption: king.agrivance
        passage = (
            "Sir Launcelot met up with old King\n"
            "   Agrivance of Ireland unexpectedly last\n"
            "   weok over on the moor south of Sir\n"
            "   Balmoral le Merveilleuse's hog dasture.\n"
            "   The widow has been notified."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "king.agrivance" not in full_text

    def test_wrap_003_the_first(self):
        # Source: A Connecticut Yankee in King Arthurs Court Part 5, wrap corruption: the.first
        passage = (
            "Expedition No. 3 will start adout the\n"
            "   first of mext month on a search f8r Sir\n"
            "   Sagramour le Desirous. It is in com-\n"
            "   and of the renowned Knight of the Red\n"
            "   Lawns, assissted by Sir Persant of Inde,\n"
            "   who is compete9t. intelligent, courte-\n"
            "   ous, and in every way a brick, and fur-\n"
            "   tHer assisted by Sir Palamides the Sara-\n"
            "   cen, who is no huckleberry hinself.\n"
            "   This is no pic-nic, these boys mean\n"
            "   busine&s."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.first" not in full_text

    def test_wrap_004_hosannah_office(self):
        # Source: A Connecticut Yankee in King Arthurs Court Part 5, wrap corruption: hosannah.office
        passage = (
            "The cordial thanks of the Hosannah\n"
            "   office are due, from editor down to\n"
            "   devil, to the ever courteous and thought-\n"
            "   ful Lord High Stew d of the Palace's\n"
            "   Third Assistant V  t for several sau-\n"
            "   ceTs of ice crEam a quality calculated\n"
            "   to make the ey of the recipients hu-\n"
            "   mid with grt  ude; and it done it.\n"
            "   When this  administration wants to\n"
            "   chalk up a desirable name for early\n"
            "   promotion, the Hosannah would like a\n"
            "   chance to sudgest."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hosannah.office" not in full_text

    def test_wrap_005_illus_trious(self):
        # Source: A Connecticut Yankee in King Arthurs Court Part 8, wrap corruption: illus.trious
        passage = (
            "Know that the great lord and illus-\n"
            "   trious Kni8ht, SIR SAGRAMOR LE\n"
            "   DESIROUS having condescended to\n"
            "   meet the King's Minister, Hank Mor-\n"
            "    gan, the which is surnamed The Boss,\n"
            "   for satisfgction of offence anciently given,\n"
            "   these wilL engage in the lists by\n"
            "   Camelot about the fourth hour of the\n"
            "   morning of the sixteenth day of this\n"
            "   next succeeding month. The battle\n"
            "   will be a l outrance, sith the said offence\n"
            "   was of a deadly sort, admitting of no\n"
            "   comPosition."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "illus.trious" not in full_text

    def test_wrap_006_his_strength(self):
        # Source: A Connecticut Yankee in King Arthurs Court Part 9, wrap corruption: his.strength
        passage = (
            "Your General congratulates you!  In the pride of his\n"
            "   strength and the vanity of his renown, an arrogant\n"
            "   enemy came against you.  You were ready.  The conflict\n"
            "   was brief; on your side, glorious.  This mighty\n"
            "   victory, having been achieved utterly without loss,\n"
            "   stands without example in history.  So long as the\n"
            "   planets shall continue to move in their orbits, the\n"
            "   BATTLE OF THE SAND-BELT will not perish out of the\n"
            "   memories of men."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "his.strength" not in full_text

    def test_wrap_007_that_air(self):
        # Source: A Connecticut Yankee in King Arthurs Court, wrap corruption: that.air
        passage = (
            "Everybody was full of awe and interest again right away, the\n"
            "incorrigible idiots.  They watched the incantations absorbingly,\n"
            "and looked at me with a “There, now, what can you say to that?”\n"
            " air, when the announcement came:"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.air" not in full_text

    def test_wrap_008_year_added(self):
        # Source: A Connecticut Yankee in King Arthurs Court, wrap corruption: year.added
        passage = (
            "“On my table appeareth white bread every Sunday in the year,”\n"
            " added the master smith, with solemnity.  “I leave it to your own\n"
            "consciences, friends, if this is not also true?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "year.added" not in full_text

    def test_wrap_009_way_her(self):
        # Source: A Double Barrelled Detective Story, wrap corruption: way.her
        passage = (
            "The young woman turned white, and said to herself, “It's a birthmark!\n"
            "The gift of the bloodhound is in him.” She snatched the boy to her\n"
            "breast and hugged him passionately, saying, “God has appointed the way!”\n"
            " Her eyes were burning with a fierce light, and her breath came short and\n"
            "quick with excitement. She said to herself: “The puzzle is solved now;\n"
            "many a time it has been a mystery to me, the impossible things the child\n"
            "has done in the dark, but it is all clear to me now.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "way.her" not in full_text

    def test_wrap_010_analyzed_bhiedelber(self):
        # Source: A Tramp Abroad Volume 07, wrap corruption: analyzed.bhiedelberg
        passage = (
            "A--The Portier analyzed\n"
            "    B--Hiedelberg Castle Described\n"
            "    C--The College Prison and Inmates\n"
            "    D--The Awful German Language\n"
            "    E--Legends of the Castle\n"
            "    F--The Journals of Germany"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "analyzed.bhiedelberg" not in full_text

    def test_wrap_011_lear_played(self):
        # Source: A Tramp Abroad, wrap corruption: lear.played
        passage = (
            "One day we took the train and went down to Mannheim to see “King Lear”\n"
            " played in German. It was a mistake. We sat in our seats three whole\n"
            "hours and never understood anything but the thunder and lightning; and\n"
            "even that was reversed to suit German ideas, for the thunder came first\n"
            "and the lightning followed after."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lear.played" not in full_text

    def test_wrap_012_johnnys_benefit(self):
        # Source: A Tramp Abroad, wrap corruption: johnnys.benefit
        passage = (
            "At the end of this profane and cordial explosion he fetched a prodigious\n"
            "“WHOOSH!” to relieve his lungs and make recognition of the heat, and\n"
            "then he straightway dived into his narrative again for “Johnny's”\n"
            " benefit, beginning, “Well, ------it ain't any use talking, some of those\n"
            "old American words DO have a kind of a bully swing to them; a man\n"
            "can EXPRESS himself with 'em--a man can get at what he wants to SAY,\n"
            "dontchuknow.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "johnnys.benefit" not in full_text

    def test_wrap_013_frame_house(self):
        # Source: A Tramp Abroad, wrap corruption: frame.house
        passage = (
            "Beyond that end of our establishment which was furthest from the street,\n"
            "was a deserted garden, pathless, and thickly grown with the bloomy and\n"
            "villainous “jimpson” weed and its common friend the stately sunflower.\n"
            "In the midst of this mournful spot was a decayed and aged little “frame”\n"
            " house with but one room, one window, and no ceiling--it had been a\n"
            "smoke-house a generation before. Nicodemus was given this lonely and\n"
            "ghostly den as a bedchamber."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "frame.house" not in full_text

    def test_wrap_014_star_parts(self):
        # Source: A Tramp Abroad, wrap corruption: star.parts
        passage = (
            "In Nevada I used to see the children play at silver-mining. Of course,\n"
            "the great thing was an accident in a mine, and there were two “star”\n"
            " parts; that of the man who fell down the mimic shaft, and that of the\n"
            "daring hero who was lowered into the depths to bring him up. I knew one\n"
            "small chap who always insisted on playing BOTH of these parts--and he\n"
            "carried his point. He would tumble into the shaft and die, and then come\n"
            "to the surface and go back after his own remains."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "star.parts" not in full_text

    def test_wrap_015_moses_and(self):
        # Source: A Tramp Abroad, wrap corruption: moses.and
        passage = (
            "My sole purpose in going to Florence was to see this immortal “Moses,”\n"
            " and by good fortune I was just in time, for they were already preparing\n"
            "to remove it to a more private and better-protected place because a\n"
            "fashion of robbing the great galleries was prevailing in Europe at the\n"
            "time."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "moses.and" not in full_text

    def test_wrap_016_word_blessed(self):
        # Source: A Tramp Abroad, wrap corruption: word.blessed
        passage = (
            "“We are saved, father! I told you the Holy Virgin would keep her word!”\n"
            " “Blessed be her sacred name!” said the old scholar, with emotion. The\n"
            "crowd roared, “Huzza, huzza, huzza--at him again, Green-patch!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "word.blessed" not in full_text

    def test_wrap_017_notices_ten(self):
        # Source: A Tramp Abroad, wrap corruption: notices.ten
        passage = (
            "Exactly one-half of the second page is occupied with an opera criticism,\n"
            "fifty-three lines (three of them being headlines), and “Death Notices,”\n"
            " ten lines."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "notices.ten" not in full_text

    def test_wrap_018_fare_punch(self):
        # Source: Alonzo Fitz and Other Stories, wrap corruption: fare.punch
        passage = (
            "Conductor, when you receive a fare,\n"
            "               Punch in the presence of the passenjare!\n"
            "               A blue trip slip for an eight-cent fare,\n"
            "               A buff trip slip for a six-cent fare,\n"
            "               A pink trip slip for a three-cent fare,\n"
            "               Punch in the presence of the passenjare!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fare.punch" not in full_text

    def test_wrap_019_animal_whose(self):
        # Source: Alonzo Fitz and Other Stories, wrap corruption: animal.whose
        passage = (
            "In Hubert's fourteenth year a pregnant event will happen; the animal\n"
            "     whose singing shall sound sweetest in Hubert's ear shall save\n"
            "     Hubert's life.  So long as the king and the nation shall honor this\n"
            "     animal's race for this good deed, the ancient dynasty shall not fail\n"
            "     of an heir, nor the nation know war or pestilence or poverty.  But\n"
            "     beware an erring choice!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "animal.whose" not in full_text

    def test_wrap_020_platform_again(self):
        # Source: Chapters From My Autobiography, wrap corruption: platform.again
        passage = (
            "MY DEAR NAST: I did not think I should ever stand on a platform\n"
            "     again until the time was come for me to say I die innocent. But the\n"
            "     same old offers keep arriving that have arriven every year, and\n"
            "     been every year declined--$500 for Louisville, $500 for St. Louis,\n"
            "     $1,000 gold for two nights in Toronto, half gross proceeds for New\n"
            "     York, Boston, Brooklyn, &c. I have declined them all just as usual,\n"
            "     though sorely tempted as usual."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "platform.again" not in full_text

    def test_wrap_021_but_because(self):
        # Source: Chapters From My Autobiography, wrap corruption: but.because
        passage = (
            "Now, I do not decline because I mind talking to an audience, but\n"
            "     because (1) travelling alone is so heart-breakingly dreary, and (2)\n"
            "     shouldering the whole show is such cheer-killing responsibility."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "but.because" not in full_text

    def test_wrap_022_november_ten(self):
        # Source: Chapters From My Autobiography, wrap corruption: november.ten
        passage = (
            "Therefore I now propose to you what you proposed to me in November,\n"
            "     1867--ten years ago, (when I was unknown,) viz.; That you should\n"
            "     stand on the platform and make pictures, and I stand by you and\n"
            "     blackguard the audience. I should enormously enjoy meandering\n"
            "     around (to big towns--don't want to go to little ones) with you for\n"
            "     company."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "november.ten" not in full_text

    def test_wrap_023_fair_when(self):
        # Source: Chapters From My Autobiography, wrap corruption: fair.when
        passage = (
            "Love came at dawn, when all the world was fair,\n"
            "       When crimson glories' bloom and sun were rife;\n"
            "     Love came at dawn, when hope's wings fanned the air,\n"
            "       And murmured, \"I am life.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fair.when" not in full_text

    def test_wrap_024_done_when(self):
        # Source: Chapters From My Autobiography, wrap corruption: done.when
        passage = (
            "Love came at eve, and when the day was done,\n"
            "       When heart and brain were tired, and slumber pressed;\n"
            "     Love came at eve, shut out the sinking sun,\n"
            "       And whispered, \"I am rest.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "done.when" not in full_text

    def test_wrap_025_clara_and(self):
        # Source: Chapters From My Autobiography, wrap corruption: clara.and
        passage = (
            "We are a very happy family. We consist of Papa, Mamma, Jean, Clara\n"
            "     and me. It is papa I am writing about, and I shall have no trouble\n"
            "     in not knowing what to say about him, as he is a very striking\n"
            "     character."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "clara.and" not in full_text

    def test_wrap_026_see_whether(self):
        # Source: Chapters From My Autobiography, wrap corruption: see.whether
        passage = (
            "Mamma tried to explain to papa that when he wanted to go and see\n"
            "     whether the alarm would ring while the window was closed he\n"
            "     mustn't go and open the window--but in vain, papa couldn't\n"
            "     understand, and got very impatient with mamma for trying to make\n"
            "     him believe an impossible thing true."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "see.whether" not in full_text

    def test_wrap_027_but_most(self):
        # Source: Chapters From My Autobiography, wrap corruption: but.most
        passage = (
            "Papa has a peculiar gait we like, it seems just to sute him, but\n"
            "     most people do not; he always walks up and down the room while\n"
            "     thinking and between each coarse at meals."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "but.most" not in full_text

    def test_wrap_028_jane_lampton(self):
        # Source: Chapters From My Autobiography, wrap corruption: jane.lampton
        passage = (
            "Papa was born in Missouri. His mother is Grandma Clemens (Jane\n"
            "     Lampton Clemens) of Kentucky. Grandpa Clemens was of the F.F.V's of\n"
            "     Virginia."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "jane.lampton" not in full_text

    def test_wrap_029_about_the(self):
        # Source: Chapters From My Autobiography, wrap corruption: about.the
        passage = (
            "Clara and I are sure that papa played the trick on Grandma, about\n"
            "     the whipping, that is related in \"The Adventures of Tom Sayer\":\n"
            "     \"Hand me that switch.\" The switch hovered in the air, the peril was\n"
            "     desperate--\"My, look behind you Aunt!\" The old lady whirled around\n"
            "     and snatched her skirts out of danger. The lad fled on the instant,\n"
            "     scrambling up the high board fence and dissapeared over it."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "about.the" not in full_text

    def test_wrap_030_may_and(self):
        # Source: Chapters From My Autobiography, wrap corruption: may.and
        passage = (
            "Papa made arrangements to read at Vassar College the 1st of May,\n"
            "     and I went with him. We went by way of New York City. Mamma went\n"
            "     with us to New York and stayed two days to do some shopping. We\n"
            "     started Tuesday, at 1/2 past two o'clock in the afternoon, and\n"
            "     reached New York about 1/4 past six. Papa went right up to General\n"
            "     Grants from the station and mamma and I went to the Everett House.\n"
            "     Aunt Clara came to supper with us up in our room...."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "may.and" not in full_text

    def test_wrap_031_the_general(self):
        # Source: Chapters From My Autobiography, wrap corruption: the.general
        passage = (
            "I have not tried to give the General's language, but only the\n"
            "     general idea of what he said. The thing that mainly struck me was\n"
            "     his terse remark that the enemy originated the idea of the march to\n"
            "     the sea. It struck me because it was so suggestive of the General's\n"
            "     epigrammatic fashion--saying a great deal in a single crisp\n"
            "     sentence. (This is my account, and signed \"Mark Twain.\")"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.general" not in full_text

    def test_wrap_032_authors_that(self):
        # Source: Chapters From My Autobiography, wrap corruption: authors.that
        passage = (
            "Then papa went to read in public; there were a great many authors\n"
            "     that read, that Thursday afternoon, beside papa; I would have liked\n"
            "     to have gone and heard papa read, but papa said he was going to\n"
            "     read in Vassar just what he was planning to read in New York, so I\n"
            "     stayed at home with mamma."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "authors.that" not in full_text

    def test_wrap_033_our_tripp(self):
        # Source: Chapters From My Autobiography, wrap corruption: our.tripp
        passage = (
            "I stopped in the middle of mamma's early history to tell about our\n"
            "     tripp to Vassar because I was afraid I would forget about it, now I\n"
            "     will go on where I left off. Some time after Miss Emma Nigh died\n"
            "     papa took mamma and little Langdon to Elmira for the summer. When\n"
            "     in Elmira Langdon began to fail but I think mamma did not know just\n"
            "     what was the matter with him."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "our.tripp" not in full_text

    def test_wrap_034_power_sometimes(self):
        # Source: Chapters From My Autobiography, wrap corruption: power.sometimes
        passage = (
            "\"Sometimes by an assertion of the inter-State commerce power,\n"
            "     sometimes by an assertion of the taxing power, the national\n"
            "     government is taking up the performance of duties which under the\n"
            "     changed conditions the separate States are no longer capable of\n"
            "     adequately performing.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "power.sometimes" not in full_text

    def test_wrap_035_life_which(self):
        # Source: Chapters From My Autobiography, wrap corruption: life.which
        passage = (
            "\"We are urging forward in a development of business and social life\n"
            "     which tends more and more to the obliteration of State lines and\n"
            "     the decrease of State power as compared with national power.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "life.which" not in full_text

    def test_wrap_036_our_new(self):
        # Source: Chapters From My Autobiography, wrap corruption: our.new
        passage = (
            "Sept. 10, '85.--The other evening Clara and I brought down our\n"
            "     new soap bubble water and we all blew soap bubles. Papa blew his\n"
            "     soap bubles and filled them with tobacco smoke and as the light\n"
            "     shone on then they took very beautiful opaline colors. Papa would\n"
            "     hold them and then let us catch them in our hand and they felt\n"
            "     delightful to the touch the mixture of the smoke and water had a\n"
            "     singularly pleasant effect."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "our.new" not in full_text

    def test_wrap_037_say_much(self):
        # Source: Chapters From My Autobiography, wrap corruption: say.much
        passage = (
            "She was too much surprised, (and pleased privately, too) to say\n"
            "     much at first, but as we all expected publicly, (or rather when she\n"
            "     remembered that this article was to be read by every one that took\n"
            "     the Christian Union) she was rather shocked and a little\n"
            "     displeased."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "say.much" not in full_text

    def test_wrap_038_and_then(self):
        # Source: Chapters From My Autobiography, wrap corruption: and.then
        passage = (
            "Clara and I had great fun the night papa gave it to us to read and\n"
            "     then hide, so mamma couldn't see it, for just as we were in the\n"
            "     midst of reading it mamma appeared, papa following anxiously and\n"
            "     asked why we were not in bed? then a scuffle ensued for we told her\n"
            "     it was a secret and tried to hide it; but she chased us wherever we\n"
            "     went, till she thought it was time for us to go to bed, then she\n"
            "     surendered and left us to tuck it under Clara's matress."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.then" not in full_text

    def test_wrap_039_never_hear(self):
        # Source: Chapters From My Autobiography, wrap corruption: never.hear
        passage = (
            "After all this, papa and mamma both wished I think they might never\n"
            "     hear or be spoken to on the subject of the Christian Union article,\n"
            "     and whenever any has spoken to me and told me \"How much they did\n"
            "     enjoy my father's article in the Christian Union\" I almost laughed\n"
            "     in their faces when I remembered what a great variety of oppinions\n"
            "     had been expressed upon the subject of the Christian Union article\n"
            "     of papa's."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "never.hear" not in full_text

    def test_wrap_040_day_papa(self):
        # Source: Chapters From My Autobiography, wrap corruption: day.papa
        passage = (
            "The article was written in July or August and just the other day\n"
            "     papa received quite a bright letter from a gentleman who has read\n"
            "     the C. U. article and gave his opinion of it in these words."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "day.papa" not in full_text

    def test_wrap_041_hutton_were(self):
        # Source: Chapters From My Autobiography, wrap corruption: hutton.were
        passage = (
            "March 14th, '86.--Mr. Laurence Barrette and Mr. and Mrs. Hutton\n"
            "     were here a little while ago, and we had a very interesting visit\n"
            "     from them. Papa said Mr. Barette never had acted so well before\n"
            "     when he had seen him, as he did the first night he was staying with\n"
            "     us. And Mrs. ---- said she never had seen an actor on the stage,\n"
            "     whom she more wanted to speak with."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hutton.were" not in full_text

    def test_wrap_042_cure_theory(self):
        # Source: Chapters From My Autobiography, wrap corruption: cure.theory
        passage = (
            "Papa has been very much interested of late, in the \"Mind Cure\"\n"
            "     theory. And in fact so have we all. A young lady in town has worked\n"
            "     wonders by using the \"Mind Cure\" upon people; she is constantly\n"
            "     busy now curing peoples deseases in this way--and curing her own\n"
            "     even, which to me seems the most remarkable of all."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "cure.theory" not in full_text

    def test_wrap_043_mind_cure(self):
        # Source: Chapters From My Autobiography, wrap corruption: mind.cure
        passage = (
            "I shouldn't wonder if we finally became firm believers in Mind\n"
            "     Cure. The next time papa has a cold, I haven't a doubt, he will\n"
            "     send for Miss H---- the young lady who is doctoring in the \"Mind\n"
            "     Cure\" theory, to cure him of it."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mind.cure" not in full_text

    def test_wrap_044_and_miss(self):
        # Source: Chapters From My Autobiography, wrap corruption: and.miss
        passage = (
            "Mamma was over at Mrs. George Warners to lunch the other day, and\n"
            "     Miss H---- was there too. Mamma asked if anything as natural as\n"
            "     near sightedness could be cured she said oh yes just as well as\n"
            "     other deseases."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.miss" not in full_text

    def test_wrap_045_groups_and(self):
        # Source: Chapters From My Autobiography, wrap corruption: groups.and
        passage = (
            "We have just had our Prince and Pauper pictures taken; two groups\n"
            "     and some little single ones. The groups (the Interview and Lady\n"
            "     Jane Grey scene) were pretty good, the lady Jane scene was perfect,\n"
            "     just as pretty as it could be, the Interview was not so good; and\n"
            "     two of the little single pictures were very good indeed, but one\n"
            "     was very bad. Yet on the whole we think they were a success."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "groups.and" not in full_text

    def test_wrap_046_things_and(self):
        # Source: Chapters From My Autobiography, wrap corruption: things.and
        passage = (
            "Papa can make exceedingly bright jokes, and he enjoys funny things,\n"
            "     and when he is with people he jokes and laughs a great deal, but\n"
            "     still he is more interested in earnest books and earnest subjects\n"
            "     to talk upon, than in humorous ones."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "things.and" not in full_text

    def test_wrap_047_talks_about(self):
        # Source: Chapters From My Autobiography, wrap corruption: talks.about
        passage = (
            "When we are all alone at home, nine times out of ten, he talks\n"
            "     about some very earnest subjects, (with an ocasional joke thrown\n"
            "     in) and he a good deal more often talks upon such subjects than\n"
            "     upon the other kind."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "talks.about" not in full_text

    def test_wrap_048_three_days(self):
        # Source: Chapters From My Autobiography, wrap corruption: three.days
        passage = (
            "March 26.--Mamma and Papa have been in New York for two or three\n"
            "     days, and Miss Corey has been staying with us. They are coming home\n"
            "     to-day at two o'clock."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "three.days" not in full_text

    def test_wrap_049_any_one(self):
        # Source: Chapters From My Autobiography, wrap corruption: any.one
        passage = (
            "DEAR UNCLE,--That's one nice thing about me, I never bother any\n"
            "     one, to offer me a good thing twice. You dont ask me to stay over\n"
            "     Sunday, but then you dont ask me to leave Saturday night, and\n"
            "     knowing the nobility of your nature as I do--thank you, I'll stay\n"
            "     till Monday morning."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "any.one" not in full_text

    def test_wrap_050_when_jean(self):
        # Source: Chapters From My Autobiography, wrap corruption: when.jean
        passage = (
            "Jean and Papa were walking out past the barn the other day when\n"
            "     Jean saw some little newly born baby ducks, she exclaimed as she\n"
            "     perceived them \"I dont see why God gives us so much ducks when\n"
            "     Patrick kills them so.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "when.jean" not in full_text

    def test_wrap_051_boardingho_far(self):
        # Source: Chapters From My Autobiography, wrap corruption: boardinghouse.far
        passage = (
            "\"There is a boarding-house\n"
            "               Far, far away,\n"
            "     Where they have ham and eggs,\n"
            "               Three times a day.\n"
            "     Oh dont those boarders yell\n"
            "     When they hear the dinner-bell,\n"
            "     They give that land-lord rats\n"
            "               Three times a day.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "boardinghouse.far" not in full_text

    def test_wrap_052_decided_way(self):
        # Source: Chapters From My Autobiography, wrap corruption: decided.way
        passage = (
            "But she said the same words over again, and in the same decided\n"
            "     way. I suppose I ought to have been outraged; but I wasn't, I was\n"
            "     charmed. And I suppose I ought to have spanked her; but I didn't, I\n"
            "     fraternized with the enemy, and we went on and spent half an hour\n"
            "     with the cows."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "decided.way" not in full_text

    def test_wrap_053_but_was(self):
        # Source: Chapters From My Autobiography, wrap corruption: but.was
        passage = (
            "Mama was speaking of a servant who had been pretty unveracious, but\n"
            "     was now \"trying to tell the truth.\" Susy was a good deal surprised,\n"
            "     and said she shouldn't think anybody would have to try to tell\n"
            "     the truth."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "but.was" not in full_text

    def test_wrap_054_she_saw(self):
        # Source: Chapters From My Autobiography, wrap corruption: she.saw
        passage = (
            "Susy aged eleven, Jean three.--Susy said the other day when she\n"
            "     saw Jean bringing a cat to me of her own motion, \"Jean has found\n"
            "     out already that mamma loves morals and papa loves cats.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "she.saw" not in full_text

    def test_wrap_055_was_reminded(self):
        # Source: Chapters From My Autobiography, wrap corruption: was.reminded
        passage = (
            "One evening Susy had prayed, Clara was curled up for sleep; she was\n"
            "     reminded that it was her turn to pray now. She laid \"Oh! one's\n"
            "     enough,\" and dropped off to slumber."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "was.reminded" not in full_text

