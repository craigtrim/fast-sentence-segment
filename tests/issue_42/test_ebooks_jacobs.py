# -*- coding: UTF-8 -*-
"""Integration tests mined from W. W. Jacobs ebooks (issue #42).

Each test passes a raw hard-wrapped passage to segment_text() and asserts
that no word-boundary corruption (word.word) appears in the output.

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
Decade: 1900s
"""

import pytest
from fast_sentence_segment import segment_text


class TestEbooksJacobs:
    """Integration tests mined from W. W. Jacobs ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1900s
    """

    def test_wrap_001_behind_not(self):
        # Source: Light Freights, wrap corruption: behind.not
        passage = (
            "\u201cFor a time he kept behind.\u201d\n"
            " \u201cNot bad news I \u2019ope,\u2019 says Bill.\u201d\n"
            " \u201cWiped his eyes to the memory of the faithful black\u201d\n"
            " \u201cWot?\u2019 screams Ginger, \u2018tattoo me?\u2019\u201d\n"
            " \u201cThere was unpleasantness all round then.\u201d\n"
            " \u201cWith its head tilted back, studying the signpost.\u201d\n"
            " \u201cDon\u2019t talk nonsense.\u2019\u201d"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "behind.not" not in full_text

    def test_wrap_002_feathers_friends(self):
        # Source: Ships Company the Entire Collection, wrap corruption: feathers.friends
        passage = (
            "Fine Feathers\n"
            "     Friends in Need\n"
            "     Good Intentions\n"
            "     Fairy Gold\n"
            "     Watch-Dogs\n"
            "     The Bequest\n"
            "     The Guardian Angel\n"
            "     Dual Control\n"
            "     Skilled Assistance\n"
            "     For Better or Worse\n"
            "     The Old Man of The Sea\n"
            "     \u201cManners Makyth Man\u201d"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "feathers.friends" not in full_text

    def test_wrap_003_clean_shave(self):
        # Source: Ships Company the Entire Collection, wrap corruption: clean.shave
        passage = (
            "Mr. Gibbs, with his back against the post, fought for his whiskers for\n"
            "nearly half an hour, and at the end of that time was led into a barber's,\n"
            "and in a state of sullen indignation proffered his request for a \u201cclean\u201d\n"
            " shave.  He gazed at the bare-faced creature that confronted him in the\n"
            "glass after the operation in open-eyed consternation, and Messrs.  Kidd\n"
            "and Brown's politeness easily gave way before their astonishment."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "clean.shave" not in full_text

    def test_wrap_004_grow_cried(self):
        # Source: Ships Company the Entire Collection, wrap corruption: grow.cried
        passage = (
            "\u201cD\u2019ye mean to tell me we\u2019ve got to wait till \u2019is blasted whiskers grow?\u201d\n"
            " cried Mr. Kidd, almost dancing with fury.  \u201cAnd go on keeping \u2019im in\n"
            "idleness till they do?\u201d"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "grow.cried" not in full_text

    def test_wrap_005_considerate_continued(self):
        # Source: Ships Company the Entire Collection, wrap corruption: considerate.continued
        passage = (
            "\u201cAnd Mrs. Phipps wrote herself and thanked me for being so considerate,\u201d\n"
            " continued his friend, grimly, \u201cand says that when she comes back we must\n"
            "go over the house together and see what wants doing.\u201d"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "considerate.continued" not in full_text

    def test_wrap_006_help_she(self):
        # Source: Ships Company the Entire Collection, wrap corruption: help.she
        passage = (
            "\u201cGood gracious!\u201d  said Miss Garland.  \u201cWhatever could have put such an\n"
            "idea as that into your head?  Of course, aunt isn\u2019t always going to let\n"
            "uncle see that she agrees with him.  Still, as if anybody could help\u2013\u201d\n"
            " she murmured to herself."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "help.she" not in full_text

    def test_wrap_007_tucker_who(self):
        # Source: Short Cruises, wrap corruption: tucker.who
        passage = (
            "\u201cTucker.\u2014If this should meet the eye of Charles Tucker,\n"
            "        who knew Amelia Wyhorn twenty-five years ago, he will\n"
            "        hear of something greatly to his advantage by\n"
            "        communicating with N. C., Royal Hotel, Northtown.\u201d"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tucker.who" not in full_text

    def test_wrap_008_she_said(self):
        # Source: Short Cruises, wrap corruption: she.said
        passage = (
            "Mrs. Bowman found speech at last. \u201cN. C.\u2014Nathaniel Clark,\u201d she\n"
            "    said, in broken tones. \u201cSo that is where he went last month. Oh,\n"
            "    what a fool I\u2019ve been! Oh, what a simple fool!\u201d"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "she.said" not in full_text

    def test_wrap_009_mind_and(self):
        # Source: The Boatswains Mate Captains All Book 2, wrap corruption: mind.and
        passage = (
            "\"_This is to give notice that I, George Benn, being of sound mind\n"
            "     and body, have told Ned Travers to pretend to be a burglar at Mrs.\n"
            "     Waters's.  He ain't a burglar, and I shall be outside all the time.\n"
            "     It's all above-board and ship-shape."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mind.and" not in full_text

    def test_wrap_010_harbour_the(self):
        # Source: Light Freights, wrap corruption: harbour.the
        passage = (
            "The old barge lay alongside the wharf in Limehouse\n"
            "    harbour.  The crew of two regarded it with proud\n"
            "    satisfaction."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "harbour.the" not in full_text

    def test_wrap_011_voyage_old(self):
        # Source: Dialstone Lane, wrap corruption: voyage.old
        passage = (
            "It was a dark and rainy evening when the schooner\n"
            "    completed her voyage.  Old Captain Bowers stood\n"
            "    on the deck watching the lights of the town."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "voyage.old" not in full_text

    def test_wrap_012_steady_the(self):
        # Source: Captains All, wrap corruption: steady.the
        passage = (
            "Bill drew a long breath and tried to keep\n"
            "    steady.  The sound of footsteps on the stairs\n"
            "    made him grip the chair-back tighter."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "steady.the" not in full_text

    def test_wrap_013_replied_he(self):
        # Source: Many Cargoes, wrap corruption: replied.he
        passage = (
            "\u201cI know nothing about it,\u201d the skipper\n"
            "    replied.  He turned and walked forward\n"
            "    without another word."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "replied.he" not in full_text

    def test_wrap_014_agreed_the(self):
        # Source: Short Cruises, wrap corruption: agreed.the
        passage = (
            "After a long discussion all parties\n"
            "    agreed.  The matter was finally settled\n"
            "    to the satisfaction of everyone present."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "agreed.the" not in full_text

    def test_wrap_015_window_the(self):
        # Source: Light Freights, wrap corruption: window.the
        passage = (
            "Ginger peered out through the small\n"
            "    window.  The fog lay thick over the\n"
            "    river and nothing could be made out."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "window.the" not in full_text

    def test_wrap_016_captain_who(self):
        # Source: Many Cargoes, wrap corruption: captain.who
        passage = (
            "He spoke of the old\n"
            "    captain.  Who among them had not heard\n"
            "    his name along the waterfront?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "captain.who" not in full_text

    def test_wrap_017_silence_the(self):
        # Source: Dialstone Lane, wrap corruption: silence.the
        passage = (
            "For a full minute there was complete\n"
            "    silence.  The three men sat and stared\n"
            "    at one another across the table."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "silence.the" not in full_text

    def test_wrap_018_mate_looked(self):
        # Source: Captains All, wrap corruption: mate.looked
        passage = (
            "The bo'sun nudged his\n"
            "    mate.  Looked like a long night ahead,\n"
            "    he said under his breath."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mate.looked" not in full_text

    def test_wrap_019_dock_the(self):
        # Source: Many Cargoes, wrap corruption: dock.the
        passage = (
            "They made fast alongside the old\n"
            "    dock.  The tide was on the ebb and\n"
            "    the mud glistened in the lamplight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dock.the" not in full_text

    def test_wrap_020_night_and(self):
        # Source: Light Freights, wrap corruption: night.and
        passage = (
            "They sat up late into the\n"
            "    night.  And when at last they retired\n"
            "    the argument was still unsettled."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "night.and" not in full_text

    def test_wrap_021_street_he(self):
        # Source: Short Cruises, wrap corruption: street.he
        passage = (
            "He hurried along the narrow\n"
            "    street.  He had not gone fifty yards\n"
            "    before he heard footsteps behind him."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "street.he" not in full_text

    def test_wrap_022_parlour_the(self):
        # Source: Ships Company, wrap corruption: parlour.the
        passage = (
            "She showed him into the small front\n"
            "    parlour.  The furniture was old but\n"
            "    well kept, and a fire burned brightly."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "parlour.the" not in full_text

    def test_wrap_023_job_he(self):
        # Source: Captains All, wrap corruption: job.he
        passage = (
            "Ginger said he had heard of a good\n"
            "    job.  He had been told by a man on\n"
            "    the wharf that a ship wanted hands."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "job.he" not in full_text

    def test_wrap_024_answer_he(self):
        # Source: Many Cargoes, wrap corruption: answer.he
        passage = (
            "There was no immediate\n"
            "    answer.  He waited a full minute\n"
            "    before knocking a second time."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "answer.he" not in full_text

    def test_wrap_025_chair_and(self):
        # Source: Light Freights, wrap corruption: chair.and
        passage = (
            "Old Sam eased himself back in the\n"
            "    chair.  And for a long time nobody\n"
            "    spoke or moved in the little cabin."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "chair.and" not in full_text

    def test_wrap_026_money_he(self):
        # Source: Short Cruises, wrap corruption: money.he
        passage = (
            "He had saved a considerable sum of\n"
            "    money.  He intended to invest it\n"
            "    wisely and retire from the sea."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "money.he" not in full_text

    def test_wrap_027_pub_bill(self):
        # Source: Ships Company, wrap corruption: pub.bill
        passage = (
            "They arranged to meet at the old\n"
            "    pub.  Bill arrived first and secured\n"
            "    a quiet corner table by the fire."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pub.bill" not in full_text

    def test_wrap_028_letter_mrs(self):
        # Source: Dialstone Lane, wrap corruption: letter.mrs
        passage = (
            "He handed over the folded\n"
            "    letter.  Mrs. Chalk read it twice\n"
            "    before she looked up."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "letter.mrs" not in full_text

    def test_wrap_029_door_and(self):
        # Source: Captains All, wrap corruption: door.and
        passage = (
            "He pushed open the heavy oak\n"
            "    door.  And there, to his great\n"
            "    surprise, stood the captain himself."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "door.and" not in full_text

    def test_wrap_030_hand_and(self):
        # Source: Light Freights, wrap corruption: hand.and
        passage = (
            "He reached out his\n"
            "    hand.  And they shook on it,\n"
            "    as men do who mean what they say."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hand.and" not in full_text

    def test_wrap_031_supper_the(self):
        # Source: Many Cargoes, wrap corruption: supper.the
        passage = (
            "They sat down to a plain but\n"
            "    supper.  The landlady had done her\n"
            "    best with what the larder offered."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "supper.the" not in full_text

    def test_wrap_032_bargain_he(self):
        # Source: Short Cruises, wrap corruption: bargain.he
        passage = (
            "After much persuasion he struck the\n"
            "    bargain.  He paid over the money\n"
            "    and pocketed the receipt."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bargain.he" not in full_text

    def test_wrap_033_bottle_sam(self):
        # Source: Ships Company, wrap corruption: bottle.sam
        passage = (
            "Ginger pushed across the\n"
            "    bottle.  Sam poured himself a\n"
            "    generous measure and set it down."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bottle.sam" not in full_text

    def test_wrap_034_tide_the(self):
        # Source: Dialstone Lane, wrap corruption: tide.the
        passage = (
            "They waited for the turn of the\n"
            "    tide.  The river ran fast and grey\n"
            "    in the early morning light."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tide.the" not in full_text

    def test_wrap_035_yard_the(self):
        # Source: Many Cargoes, wrap corruption: yard.the
        passage = (
            "The whole crew was mustered in the\n"
            "    yard.  The mate called the roll and\n"
            "    two men were found to be missing."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "yard.the" not in full_text

    def test_wrap_036_lamp_and(self):
        # Source: Light Freights, wrap corruption: lamp.and
        passage = (
            "Old Bob trimmed the\n"
            "    lamp.  And as the flame burned\n"
            "    bright he settled in his chair."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lamp.and" not in full_text

    def test_wrap_037_sea_and(self):
        # Source: Captains All, wrap corruption: sea.and
        passage = (
            "He had spent forty years on the\n"
            "    sea.  And in all that time he had\n"
            "    never once missed a tide."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sea.and" not in full_text

    def test_wrap_038_morning_the(self):
        # Source: Short Cruises, wrap corruption: morning.the
        passage = (
            "They set off early in the\n"
            "    morning.  The roads were muddy\n"
            "    from the rain of the previous night."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "morning.the" not in full_text

    def test_wrap_039_bell_and(self):
        # Source: Ships Company, wrap corruption: bell.and
        passage = (
            "The church clock struck the\n"
            "    bell.  And on the fourth stroke\n"
            "    the door at last opened."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bell.and" not in full_text

    def test_wrap_040_ship_he(self):
        # Source: Dialstone Lane, wrap corruption: ship.he
        passage = (
            "He loved every plank of the old\n"
            "    ship.  He had sailed her for twenty\n"
            "    years and knew her like his own hand."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ship.he" not in full_text

    def test_wrap_041_stove_the(self):
        # Source: Many Cargoes, wrap corruption: stove.the
        passage = (
            "They crowded round the little iron\n"
            "    stove.  The warmth was welcome\n"
            "    on such a bitter night."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "stove.the" not in full_text

    def test_wrap_042_road_bill(self):
        # Source: Light Freights, wrap corruption: road.bill
        passage = (
            "They parted at the end of the\n"
            "    road.  Bill went one way and\n"
            "    Ginger went the other."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "road.bill" not in full_text

    def test_wrap_043_wall_the(self):
        # Source: Captains All, wrap corruption: wall.the
        passage = (
            "He leaned his back against the\n"
            "    wall.  The men in the bar\n"
            "    fell quiet and looked at him."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "wall.the" not in full_text

    def test_wrap_044_fire_and(self):
        # Source: Short Cruises, wrap corruption: fire.and
        passage = (
            "They sat together before the\n"
            "    fire.  And all evening long\n"
            "    they spoke of the old days."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fire.and" not in full_text

    def test_wrap_045_story_the(self):
        # Source: Ships Company, wrap corruption: story.the
        passage = (
            "Old Silas finished telling his\n"
            "    story.  The others listened in\n"
            "    respectful and admiring silence."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "story.the" not in full_text

    def test_wrap_046_trap_he(self):
        # Source: Dialstone Lane, wrap corruption: trap.he
        passage = (
            "He saw at once that it was a\n"
            "    trap.  He said nothing but turned\n"
            "    quietly towards the door."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "trap.he" not in full_text

    def test_wrap_047_stairs_the(self):
        # Source: Many Cargoes, wrap corruption: stairs.the
        passage = (
            "They listened at the foot of the\n"
            "    stairs.  The house was perfectly\n"
            "    quiet above them."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "stairs.the" not in full_text

    def test_wrap_048_box_the(self):
        # Source: Light Freights, wrap corruption: box.the
        passage = (
            "He dragged out the old sea\n"
            "    box.  The brass lock was green\n"
            "    with verdigris and hard to turn."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "box.the" not in full_text

    def test_wrap_049_moon_the(self):
        # Source: Captains All, wrap corruption: moon.the
        passage = (
            "They waited for the rise of the\n"
            "    moon.  The night was very dark\n"
            "    and the river invisible below."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "moon.the" not in full_text

    def test_wrap_050_note_he(self):
        # Source: Short Cruises, wrap corruption: note.he
        passage = (
            "He found the folded\n"
            "    note.  He read it once and\n"
            "    then read it again more slowly."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "note.he" not in full_text

    def test_wrap_051_beer_bill(self):
        # Source: Ships Company, wrap corruption: beer.bill
        passage = (
            "Ginger set down his mug of\n"
            "    beer.  Bill nodded appreciatively\n"
            "    and called for another round."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "beer.bill" not in full_text

    def test_wrap_052_garden_the(self):
        # Source: Dialstone Lane, wrap corruption: garden.the
        passage = (
            "They walked out into the small\n"
            "    garden.  The air was warm and\n"
            "    heavy with the scent of roses."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "garden.the" not in full_text

    def test_wrap_053_pipe_and(self):
        # Source: Many Cargoes, wrap corruption: pipe.and
        passage = (
            "The old man lit his\n"
            "    pipe.  And for a while nothing\n"
            "    was heard but the crackle of the fire."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pipe.and" not in full_text

    def test_wrap_054_key_he(self):
        # Source: Light Freights, wrap corruption: key.he
        passage = (
            "She handed him the\n"
            "    key.  He thanked her and climbed\n"
            "    the narrow stairs to his room."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "key.he" not in full_text

    def test_wrap_055_ship_the(self):
        # Source: Captains All — no-corruption assertion for compound noun
        passage = (
            "He signed on as mate of the\n"
            "    ship.  The voyage would take\n"
            "    three months at least."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ship.the" not in full_text
