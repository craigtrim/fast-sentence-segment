import pytest
from fast_sentence_segment import segment_text


class TestEbooksLovecraft:
    """Integration tests mined from H. P. Lovecraft ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1920s
    """

    def test_wrap_001_roll_their(self):
        # Source: At the Mountains of Madness, wrap corruption: roll.their
        passage = (
            "\"--the lavas that restlessly roll\n"
            "    Their sulphurous currents down Yaanek\n"
            "      In the ultimate climes of the pole--\n"
            "    That groan as they roll down Mount Yaanek\n"
            "      In the realms of the boreal pole.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "roll.their" not in full_text

    def test_wrap_002_range_ahead(self):
        # Source: At the Mountains of Madness, wrap corruption: range.ahead
        passage = (
            "\"10:05 p.m. On the wing. After snowstorm, have spied mountain range\n"
            "    ahead higher than any hitherto seen. May equal Himalayas, allowing\n"
            "    for height of plateau. Probable Latitude 76° 15´, Longitude 113° 10´\n"
            "    E. Reaches far as can see to right and left. Suspicion of two\n"
            "    smoking cones. All peaks black and bare of snow. Gale blowing off\n"
            "    them impedes navigation.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "range.ahead" not in full_text

    def test_wrap_003_nobody_hurt(self):
        # Source: At the Mountains of Madness, wrap corruption: nobody.hurt
        passage = (
            "\"Moulton's plane forced down on plateau in foothills, but nobody\n"
            "    hurt and perhaps can repair. Shall transfer essentials to other\n"
            "    three for return or further moves if necessary, but no more heavy\n"
            "    plane travel needed just now. Mountains surpass anything in\n"
            "    imagination. Am going up scouting in Carroll's plane, with all\n"
            "    weight out."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "nobody.hurt" not in full_text

    def test_wrap_004_appendages_have(self):
        # Source: At the Mountains of Madness, wrap corruption: appendages.have
        passage = (
            "Of organic specimens, eight apparently perfect, with all appendages.\n"
            "    Have brought all to surface, leading off dogs to distance. They\n"
            "    cannot stand the things. Give close attention to description and\n"
            "    repeat back for accuracy. Papers must get this right."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "appendages.have" not in full_text

    def test_wrap_005_gilllike_suggestion(self):
        # Source: At the Mountains of Madness, wrap corruption: gilllike.suggestions
        passage = (
            "At top of torso blunt, bulbous neck of lighter gray, with gill-like\n"
            "    suggestions, holds yellowish five-pointed starfish-shaped apparent\n"
            "    head covered with three-inch wiry cilia of various prismatic colors."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gilllike.suggestions" not in full_text

    def test_wrap_006_threeinch_flexible(self):
        # Source: At the Mountains of Madness, wrap corruption: threeinch.flexible
        passage = (
            "Head thick and puffy, about two feet point to point, with three-inch\n"
            "    flexible yellowish tubes projecting from each point. Slit in exact\n"
            "    center of top probably breathing aperture. At end of each tube is\n"
            "    spherical expansion where yellowish membrane rolls back on handling\n"
            "    to reveal glassy, red-irised globe, evidently an eye."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "threeinch.flexible" not in full_text

    def test_wrap_007_inches_diameter(self):
        # Source: At the Mountains of Madness, wrap corruption: inches.diameter
        passage = (
            "Tough, muscular arms four feet long and tapering from seven inches\n"
            "    diameter at base to about two and five tenths at point. To each\n"
            "    point is attached small end of a greenish five-veined membranous\n"
            "    triangle eight inches long and six wide at farther end. This is the\n"
            "    paddle, fin, or pseudofoot which had made prints in rocks from a\n"
            "    thousand million to fifty or sixty million years old."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "inches.diameter" not in full_text

    def test_wrap_008_but_odds(self):
        # Source: At the Mountains of Madness, wrap corruption: but.odds
        passage = (
            "Cannot yet assign positively to animal or vegetable kingdom, but\n"
            "    odds now favor animal. Probably represents incredibly advanced\n"
            "    evolution of radiata without loss of certain primitive features.\n"
            "    Echinoderm resemblances unmistakable despite local contradictory\n"
            "    evidences."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "but.odds" not in full_text

    def test_wrap_009_may_have(self):
        # Source: At the Mountains of Madness, wrap corruption: may.have
        passage = (
            "Wing structure puzzles in view of probable marine habitat, but may\n"
            "    have use in water navigation. Symmetry is curiously vegetablelike,\n"
            "    suggesting vegetable's essential up-and-down structure rather than\n"
            "    animal's fore-and-aft structure. Fabulously early date of evolution,\n"
            "    preceding even simplest archæan Protozoa hitherto known, baffles all\n"
            "    conjecture as to origin."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "may.have" not in full_text

    def test_wrap_010_ghastly_mystery(self):
        # Source: Cool Air, wrap corruption: ghastly.mystery
        passage = (
            "_A tale of dark science, and the ghastly\n"
            "              mystery that enveloped the Spanish doctor's\n"
            "                attempts at artificial refrigeration._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ghastly.mystery" not in full_text

    def test_wrap_011_brooding_horror(self):
        # Source: Medusas Coil, wrap corruption: brooding.horror
        passage = (
            "_A powerful and compelling tale of brooding\n"
            "             horror that deepens and broadens to the final\n"
            "           catastrophe--an unusual and engrossing novelette\n"
            "                 by the author of \"The Curse of Yig.\"_"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "brooding.horror" not in full_text

    def test_wrap_012_tow_one(self):
        # Source: The Call of Cthulhu, wrap corruption: tow.one
        passage = (
            "Vigilant Arrives With Helpless Armed New Zealand Yacht in Tow.\n"
            "    One Survivor and Dead Man Found Aboard. Tale of Desperate Battle\n"
            "    and Deaths at Sea. Rescued Seaman Refuses Particulars of Strange\n"
            "    Experience. Odd Idol Found in His Possession. Inquiry to Follow."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tow.one" not in full_text

    def test_wrap_013_valparaiso_arrived(self):
        # Source: The Call of Cthulhu, wrap corruption: valparaiso.arrived
        passage = (
            "The Morrison Co.'s freighter Vigilant, bound from Valparaiso,\n"
            "    arrived this morning at its wharf in Darling Harbour, having in tow\n"
            "    the battled and disabled but heavily armed steam yacht Alert of\n"
            "    Dunedin, N. Z., which was sighted April 12th in S. Latitude 34° 21',\n"
            "    W. Longitude 152° 17', with one living and one dead man aboard."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "valparaiso.arrived" not in full_text

    def test_wrap_014_was_driven(self):
        # Source: The Call of Cthulhu, wrap corruption: was.driven
        passage = (
            "The Vigilant left Valparaiso March 25th, and on April 2d was\n"
            "    driven considerably south of her course by exceptionally heavy\n"
            "    storms and monster waves. On April 12th the derelict was sighted;\n"
            "    and though apparently deserted, was found upon boarding to contain\n"
            "    one survivor in a half-delirious condition and one man who had\n"
            "    evidently been dead for more than a week."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "was.driven" not in full_text

    def test_wrap_015_unknown_origin(self):
        # Source: The Call of Cthulhu, wrap corruption: unknown.origin
        passage = (
            "The living man was clutching a horrible stone idol of unknown\n"
            "    origin, about a foot in height, regarding whose nature authorities\n"
            "    at Sydney University, the Royal Society, and the Museum in College\n"
            "    Street all profess complete bafflement, and which the survivor says\n"
            "    he found in the cabin of the yacht, in a small carved shrine of\n"
            "    common pattern."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "unknown.origin" not in full_text

    def test_wrap_016_strange_story(self):
        # Source: The Call of Cthulhu, wrap corruption: strange.story
        passage = (
            "This man, after recovering his senses, told an exceedingly strange\n"
            "    story of piracy and slaughter. He is Gustaf Johansen, a Norwegian\n"
            "    of some intelligence, and had been second mate of the two-masted\n"
            "    schooner Emma of Auckland, which sailed for Callao February 20th,\n"
            "    with a complement of eleven men."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "strange.story" not in full_text

    def test_wrap_017_the_schooner(self):
        # Source: The Call of Cthulhu, wrap corruption: the.schooner
        passage = (
            "The Emma's men showed fight, says the survivor, and though the\n"
            "    schooner began to sink from shots beneath the waterline they managed\n"
            "    to heave alongside their enemy and board her, grappling with the\n"
            "    savage crew on the yacht's deck, and being forced to kill them all,\n"
            "    the number being slightly superior, because of their particularly\n"
            "    abhorrent and desperate though rather clumsy mode of fighting."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.schooner" not in full_text

    def test_wrap_018_mate_green(self):
        # Source: The Call of Cthulhu, wrap corruption: mate.green
        passage = (
            "Three of the Emma's men, including Capt. Collins and First Mate\n"
            "    Green, were killed; and the remaining eight under Second Mate\n"
            "    Johansen proceeded to navigate the captured yacht, going ahead in\n"
            "    their original direction to see if any reason for their ordering\n"
            "    back had existed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mate.green" not in full_text

    def test_wrap_019_island_although(self):
        # Source: The Call of Cthulhu, wrap corruption: island.although
        passage = (
            "The next day, it appears, they raised and landed on a small island,\n"
            "    although none is known to exist in that part of the ocean; and six\n"
            "    of the men somehow died ashore, though Johansen is queerly reticent\n"
            "    about this part of his story and speaks only of their falling into\n"
            "    a rock chasm."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "island.although" not in full_text

    def test_wrap_020_remembers_little(self):
        # Source: The Call of Cthulhu, wrap corruption: remembers.little
        passage = (
            "From that time till his rescue on the 12th, the man remembers\n"
            "    little, and he does not even recall when William Briden, his\n"
            "    companion, died. Briden's death reveals no apparent cause, and was\n"
            "    probably due to excitement or exposure."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "remembers.little" not in full_text

    def test_wrap_021_known_there(self):
        # Source: The Call of Cthulhu, wrap corruption: known.there
        passage = (
            "Cable advices from Dunedin report that the Alert was well known\n"
            "    there as an island trader, and bore an evil reputation along the\n"
            "    waterfront. It was owned by a curious group of half-castes whose\n"
            "    frequent meetings and night trips to the woods attracted no little\n"
            "    curiosity; and it had set sail in great haste just after the storm\n"
            "    and earth tremors of March 1st."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "known.there" not in full_text

    def test_wrap_022_matter_beginning(self):
        # Source: The Call of Cthulhu, wrap corruption: matter.beginning
        passage = (
            "The admiralty will institute an inquiry on the whole matter\n"
            "    beginning tomorrow, at which every effort will be made to induce\n"
            "    Johansen to speak more freely than he has done hitherto."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "matter.beginning" not in full_text

    def test_wrap_023_preserved_that(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: preserved.that
        passage = (
            "The essential Saltes of Animals may be so prepared and preserved,\n"
            "    that an ingenious Man may have the whole Ark of Noah in his owne\n"
            "    Studie and raise the fine shape of an Animal out of its Ashes at\n"
            "    his Pleasure; and by the lyke method from the essential Saltes of\n"
            "    humane Dust, a Philosopher may, without any criminal Necromancy,\n"
            "    call up the Shape of any dead Ancestour from the Dust whereinto his\n"
            "    Bodie has been incinerated."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "preserved.that" not in full_text

    def test_wrap_024_merchant_was(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: merchant.was
        passage = (
            "Monday evening last, Mr. Joseph Curwen, of this Town, Merchant,\n"
            "    was married to Miss Eliza Tillinghast, Daughter of Captain Dutie\n"
            "    Tillinghast, a young Lady who has real Merit, added to a beautiful\n"
            "    Person, to grace the connubial State and perpetuate its Felicity."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "merchant.was" not in full_text

    def test_wrap_025_this_morning(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: this.morning
        passage = (
            "Robert Hart, night watchman at the North Burial Ground, this\n"
            "    morning discovered a party of several men with a motor truck in\n"
            "    the oldest part of the cemetery, but apparently frightened them off\n"
            "    before they had accomplished whatever their object may have been."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "this.morning" not in full_text

    def test_wrap_026_before_detection(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: before.detection
        passage = (
            "The diggers must have been at work for a long while before\n"
            "    detection, for Hart found an enormous hole dug at a considerable\n"
            "    distance back from the roadway in the lot of Amosa Field, where\n"
            "    most of the old stones have long ago disappeared. The hole, a place\n"
            "    as large and deep as a grave, was empty; and did not coincide with\n"
            "    any interment mentioned in the cemetery records."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "before.detection" not in full_text

    def test_wrap_027_the_opinion(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: the.opinion
        passage = (
            "Sergeant Riley of the Second Station viewed the spot and gave the\n"
            "    opinion that the hole was dug by bootleggers rather gruesomely and\n"
            "    ingeniously seeking a safe cache for liquor in a place not likely\n"
            "    to be disturbed. In reply to questions Hart said he thought the\n"
            "    escaping truck had headed up Rochambeau Avenue, though he could not\n"
            "    be sure."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.opinion" not in full_text

    def test_wrap_028_the_north(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: the.north
        passage = (
            "It was this morning discovered by Robert Hart, night watchman at the\n"
            " North Burial ground, that ghouls were again at work in the ancient\n"
            " portion of the cemetery. The grave of Ezra Weeden, who was born\n"
            " in 1740 and died in 1824 according to his uprooted and savagely\n"
            " splintered slate headstone, was found excavated and rifled, the work\n"
            " being evidently done with a spade stolen from an adjacent tool shed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.north" not in full_text

    def test_wrap_029_the_disclosure(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: the.disclosures
        passage = (
            "I feel that at last the time has come for me to make the\n"
            "    disclosures which I have so long promised you, and for which you\n"
            "    have pressed me so often. The patience you have shewn in waiting,\n"
            "    and the confidence you have shewn in my mind and integrity, are\n"
            "    things I shall never cease to appreciate."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.disclosures" not in full_text

    def test_wrap_030_thing_but(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: thing.but
        passage = (
            "I dare not tell my father, for he could not grasp the whole thing.\n"
            "    But I have told him of my danger, and he has four men from a\n"
            "    detective agency watching the house. I don't know how much good\n"
            "    they can do, for they have against them forces which even you could\n"
            "    scarcely envisage or acknowledge. So come quickly if you wish to\n"
            "    see me alive and hear how you may help to save the cosmos from\n"
            "    stark hell."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thing.but" not in full_text

    def test_wrap_031_telephone_ahead(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: telephone.ahead
        passage = (
            "Any time will do--I shall not be out of the house. Don't telephone\n"
            "    ahead, for there is no telling who or what may try to intercept\n"
            "    you. And let us pray to whatever gods there be that nothing may\n"
            "    prevent this meeting."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "telephone.ahead" not in full_text

    def test_wrap_032_this_intruder(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: this.intruder
        passage = (
            "Like the first of the ghouls active during the past year, this\n"
            "    intruder had done no real damage before detection. A vacant part\n"
            "    of the Ward lot shewed signs of a little superficial digging, but\n"
            "    nothing even nearly the size of a grave had been attempted, and no\n"
            "    previous grave had been disturbed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "this.intruder" not in full_text

    def test_wrap_033_man_probably(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: man.probably
        passage = (
            "Hart, who cannot describe the prowler except as a small man\n"
            "    probably having a full beard, inclines to the view that all three\n"
            "    of the digging incidents have a common source; but police from the\n"
            "    Second Station think otherwise on account of the savage nature of\n"
            "    the second incident, where an ancient coffin was removed and its\n"
            "    headstone violently shattered."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "man.probably" not in full_text

    def test_wrap_034_you_will(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: you.will
        passage = (
            "You have known me ever since you were a small boy, so I think you\n"
            "    will not distrust me when I hint that some matters are best left\n"
            "    undecided and unexplored. It is better that you attempt no further\n"
            "    speculation as to Charles's case, and almost imperative that you\n"
            "    tell his mother nothing more than she already suspects. When I call\n"
            "    on you tomorrow Charles will have escaped. That is all which need\n"
            "    remain in anyone's mind. He was mad, and he escaped."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.will" not in full_text

    def test_wrap_035_can_put(self):
        # Source: The Case of Charles Dexter Ward, wrap corruption: can.put
        passage = (
            "That is all. Charles will have escaped, and a year from now you can\n"
            "    put up his stone. Do not question me tomorrow. And believe that the\n"
            "    honour of your ancient family remains untainted now, as it has been\n"
            "    at all times in the past."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "can.put" not in full_text

    def test_wrap_036_can_highly(self):
        # Source: The Colour Out of Space, wrap corruption: can.highly
        passage = (
            "_Here is a totally different story that we can\n"
            "           highly recommend to you. We could wax rhapsodical\n"
            "           in our praise, as the story is one of the finest\n"
            "         pieces of literature it has been our good fortune to\n"
            "            read. The theme is original, and yet fantastic\n"
            "            enough to make it rise head and shoulders above\n"
            "          many contemporary scientifiction stories. You will\n"
            "             not regret having read this marvellous tale._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "can.highly" not in full_text

    def test_wrap_037_yawning_where(self):
        # Source: The Haunter of the Dark, wrap corruption: yawning.where
        passage = (
            "I have seen the dark universe yawning\n"
            "      Where the black planets roll without aim--\n"
            "    Where they roll in their horror unheeded,\n"
            "      Without knowledge or luster or name."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "yawning.where" not in full_text

    def test_wrap_038_great_egyptian(self):
        # Source: The Haunter of the Dark, wrap corruption: great.egyptian
        passage = (
            "\"Fr. O'Malley tells of devil-worship with box found in great\n"
            "    Egyptian ruins--says they call up something that can't exist in\n"
            "    light. Flees a little light, and banished by strong light. Then has\n"
            "    to be summoned again. Probably got this from deathbed confession\n"
            "    of Francis X. Feeney, who had joined Starry Wisdom in '49. These\n"
            "    people say the Shining Trapezohedron shows them heaven & other\n"
            "    worlds, & that the Haunter of the Dark tells them secrets in some\n"
            "    way.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "great.egyptian" not in full_text

    def test_wrap_039_gruesome_happening(self):
        # Source: The Horror in the Burying Ground, wrap corruption: gruesome.happening
        passage = (
            "_A bizarre and outré story of a gruesome\n"
            "              happening in the old town of Stillwater--a\n"
            "               blood-chilling tale of a double burial._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gruesome.happening" not in full_text

    def test_wrap_040_overhung_the(self):
        # Source: The Shadow Over Innsmouth, wrap corruption: overhung.the
        passage = (
            "_Unspeakable monstrousness over-hung\n"
            "                 the crumbling, stench-cursed town of\n"
            "               Innsmouth ... and folks there had somehow\n"
            "                   got out of the idea of dying...._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "overhung.the" not in full_text

    def test_wrap_041_weird_fictiona(self):
        # Source: The Shunned House, wrap corruption: weird.fictiona
        passage = (
            "_A posthumous story of immense power, written by a master of weird\n"
            "   fiction--a tale of a revolting horror in the cellar of an old\n"
            "                       house in New England_"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "weird.fictiona" not in full_text

    def test_wrap_042_supreme_masters(self):
        # Source: The Thing on the Door Step, wrap corruption: supreme.masters
        passage = (
            "_A powerful tale by one of the supreme\n"
            "             masters of weird fiction--a tale in which the\n"
            "              horror creeps and grows, to spring at last\n"
            "             upon the reader in all its hideous totality._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "supreme.masters" not in full_text

    def test_wrap_043_isnt_edward(self):
        # Source: The Thing on the Door Step, wrap corruption: isnt.edward
        passage = (
            "\"Dan--go to the sanitarium and kill it. Exterminate it. It isn't\n"
            "    Edward Derby any more. She got me--it's Asenath--_and she has been\n"
            "    dead three months and a half_. I lied when I said she had gone\n"
            "    away. I killed her. I had to. It was sudden, but we were alone and\n"
            "    I was in my right body. I saw a candlestick and smashed her head\n"
            "    in. She would have got me for good at Hallowmass."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "isnt.edward" not in full_text

    def test_wrap_044_old_boxes(self):
        # Source: The Thing on the Door Step, wrap corruption: old.boxes
        passage = (
            "\"I buried her in the farther cellar storeroom under some old\n"
            "    boxes and cleaned up all the traces. The servants suspected next\n"
            "    morning, but they have such secrets that they dare not tell the\n"
            "    police. I sent them off, but God knows what they--and others of the\n"
            "    cult--will do."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "old.boxes" not in full_text

    def test_wrap_045_text_appears(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: text.appears
        passage = (
            "Italic text has been marked by underscores, whilst bold text\n"
            "    appears as =bold=. The following table of contents has been added\n"
            "    for convenience:"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "text.appears" not in full_text

    def test_wrap_046_rains_and(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: rains.and
        passage = (
            "The summer rains\n"
            "          And autumn winds\n"
            "    The snowdrop find yet standing;\n"
            "          A petal gone,\n"
            "          And all alone,\n"
            "    Her tender roots expanding."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rains.and" not in full_text

    def test_wrap_047_unda_terra(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: unda.terra
        passage = (
            "\"Omnis erat vulnus unda\n"
            "    Terra rubefacta calido\n"
            "    Frendebat gladius in loricas\n"
            "    Gladius findebat clypeos--\n"
            "    Non retrocedat vir a viro\n"
            "    Hoc fuit viri fortis nobilitas diu--\n"
            "    Laetus cerevisiam cum Asis\n"
            "    In summa sede bibam\n"
            "    Vitae elapsae sunt horae\n"
            "    Ridens moriar.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "unda.terra" not in full_text

    def test_wrap_048_rhyme_thou(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: rhyme.thou
        passage = (
            "\"O Love, how thou art tired out with rhyme!\n"
            "    Thou art a tree whereon all poets climb;\n"
            "    And from thy branches every one takes some\n"
            "    Of the sweet fruit, which Fancy feeds upon.\n"
            "    But now thy tree is left so bare and poor,\n"
            "    That they can hardly gather one plum more!\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rhyme.thou" not in full_text

    def test_wrap_049_boy_and(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: boy.and
        passage = (
            "\"Once upon a time, there was a little boy,\n"
            "      And, if you please, he went to school;\n"
            "    That little boy, he always would annoy,\n"
            "      And found at school a very nasty rule.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "boy.and" not in full_text

    def test_wrap_050_air_behold(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: air.behold
        passage = (
            "Oh! could I breathe again dear Scotland's air;\n"
            "      Behold once more her stately mountains high,\n"
            "      Thence view the wide expanse of azure sky,\n"
            "    Instead of these perpetual walls so bare!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "air.behold" not in full_text

    def test_wrap_051_distress_and(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: distress.and
        passage = (
            "My Scotland! know'st thou thy poor Queen's distress,\n"
            "      And canst thou hear my wailing and my woe?\n"
            "      May the soft wind that o'er thy hills doth blow\n"
            "    Waft thee these thoughts, that I cannot suppress!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "distress.and" not in full_text

    def test_wrap_052_killarney_early(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: killarney.early
        passage = (
            "\"Oh, it's April in Killarney,\n"
            "    Early April in Killarney,\n"
            "      Where the Irish lanes are merry\n"
            "        And the lyric breezes blow;\n"
            "      And the scented snows of cherry\n"
            "      Drift across the fields of Kerry--\n"
            "    Oh, it's April in Killarney\n"
            "        And she loves the April so.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "killarney.early" not in full_text

    def test_wrap_053_arrayd_once(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: arrayd.once
        passage = (
            "As Columbia's brave scions, in anger array'd,\n"
            "      Once defy'd a proud monarch and built a new nation;\n"
            "    'Gainst their brothers of Britain unsheath'd the sharp blade\n"
            "      That hath ne'er met defeat nor endur'd desecration;\n"
            "          So must we in this hour\n"
            "          Show our valour and pow'r,\n"
            "    And dispel the black perils that over us low'r:\n"
            "      Whilst the sons of Britannia, no longer our foes,\n"
            "      Will rejoice in our triumphs and strengthen our blows!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "arrayd.once" not in full_text

    def test_wrap_054_breeze_that(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: breeze.that
        passage = (
            "See the banners of Liberty float in the breeze\n"
            "      That plays light o'er the regions our fathers defended;\n"
            "    Hear the voice of the million resound o'er the leas,\n"
            "      As the deeds of the past are proclaim'd and commended;\n"
            "          And in splendour on high\n"
            "          Where our flags proudly fly,\n"
            "    See the folds we tore down flung again to the sky:\n"
            "      For the Emblem of England, in kinship unfurl'd,\n"
            "      Shall divide with Old Glory the praise of the world!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "breeze.that" not in full_text

    def test_wrap_055_king_and(self):
        # Source: Writings in the United Amateur 1915 1922, wrap corruption: king.and
        passage = (
            "Bury'd now are the hatreds of subject and King,\n"
            "      And the strife that once sunder'd an Empire hath vanish'd.\n"
            "    With the fame of the Saxon the heavens shall ring\n"
            "      As the vultures of darkness are baffled and banish'd:\n"
            "          And the broad British sea,\n"
            "          Of her enemies free,\n"
            "    Shall in tribute bow gladly, Columbia, to thee:\n"
            "      For the friends of the Right, in the field side by side,\n"
            "      Form a fabric of Freedom no hand can divide!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "king.and" not in full_text

