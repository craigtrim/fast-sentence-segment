import pytest
from fast_sentence_segment import segment_text


class TestEbooksRinehart:
    """Integration tests mined from Mary Roberts Rinehart ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1910s
    """

    def test_wrap_001_myself_she(self):
        # Source: A Poor Wise Man, wrap corruption: myself.she
        passage = (
            "“It wasn't him. He doesn't matter. It's just--I got to hating myself.”\n"
            " She stood up and carefully dabbed her eyes. “Heavens, I must be a sight.\n"
            "Now don't you get to thinking things, Mr. Cameron. Girls can't go out\n"
            "and fight off a temper, or get full and sleep it off. So they cry.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "myself.she" not in full_text

    def test_wrap_002_kings_she(self):
        # Source: A Poor Wise Man, wrap corruption: kings.she
        passage = (
            "“I think he'd love it. He'd probably think some king gave it to you. I'm\n"
            "sure he believes that you and grandfather habitually hobnob with kings.”\n"
            " She turned to go out. “He doesn't approve of kings.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "kings.she" not in full_text

    def test_wrap_003_descriptio_said(self):
        # Source: A Poor Wise Man, wrap corruption: description.said
        passage = (
            "“You'll have to excuse me. I didn't recognize you by the description,”\n"
            " said Mrs. Boyd, unconsciously. “Well, I don't know. I'd like to have\n"
            "this dog around.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "description.said" not in full_text

    def test_wrap_004_course_she(self):
        # Source: A Poor Wise Man, wrap corruption: course.she
        passage = (
            "“Not always, Howard. He doesn't drink now, so that is over. And I think\n"
            "there are no other women. But when things go wrong I suffer, of course.”\n"
            " She stared past him toward the open window."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "course.she" not in full_text

    def test_wrap_005_death_suddenly(self):
        # Source: A Poor Wise Man, wrap corruption: death.suddenly
        passage = (
            "“Yes, I know,” she said, hysterically, “but I won't tell you. And I\n"
            "won't marry him. I hate him. If you go to him he'll beat you to death.”\n"
            " Suddenly the horrible picture of Dan in Akers' brutal hands overwhelmed\n"
            "her. “Dan, you won't go?” she begged. “He'll kill you.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "death.suddenly" not in full_text

    def test_wrap_006_him_elinor(self):
        # Source: A Poor Wise Man, wrap corruption: him.elinor
        passage = (
            "“Because, at the end of two months, nothing would make you marry him,”\n"
            " Elinor said, almost violently. “I have sat by and waited, because I\n"
            "thought you would surely see your mistake. But now--Lily, do you envy me\n"
            "my life?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "him.elinor" not in full_text

    def test_wrap_007_howard_his(self):
        # Source: A Poor Wise Man, wrap corruption: howard.his
        passage = (
            "“You're a good woman, Grace,” he said, still heavily. “We Cardews all\n"
            "marry good women, but we don't know how to treat them. Even Howard--”\n"
            " His voice trailed off. “No, she can't stay there,” he said, after a\n"
            "pause."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "howard.his" not in full_text

    def test_wrap_008_dreadful_grace(self):
        # Source: A Poor Wise Man, wrap corruption: dreadful.grace
        passage = (
            "“I don't know. She wanted to come home. She begged--it was dreadful.”\n"
            " Grace hesitated. “Even that couldn't be as bad as this, father,” she\n"
            "said. “We have all lived our own lives, you and Howard and myself, and\n"
            "now we won't let her do it.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dreadful.grace" not in full_text

    def test_wrap_009_willy_she(self):
        # Source: A Poor Wise Man, wrap corruption: willy.she
        passage = (
            "“Do you remember how you used to whistle 'The Long, Long Trail,' Willy?”\n"
            " she said at last. “All evening I have been sitting here thinking what a\n"
            "long trail we have both traveled since then.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "willy.she" not in full_text

    def test_wrap_010_the_love(self):
        # Source: Affinities and Other Stories, wrap corruption: the.love
        passage = (
            "\"DEAR BOY: We have decided on the eleven-o'clock train. For the\n"
            "     love of Mike don't miss meeting it! And after thinking it over\n"
            "     carefully, you're right. When I go to see after the luggage will be\n"
            "     the best time."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.love" not in full_text

    def test_wrap_011_mail_which(self):
        # Source: Affinities and Other Stories, wrap corruption: mail.which
        passage = (
            "\"Dear Old Man: Inclosed is the letter Clara gave Delaney to mail,\n"
            "     which I read to you last night over the long-distance phone. I'm\n"
            "     called away or I'd bring it round."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mail.which" not in full_text

    def test_wrap_012_but_you(self):
        # Source: Affinities and Other Stories, wrap corruption: but.you
        passage = (
            "\"I hope Clara didn't take cold. She must have been pretty wet. But\n"
            "     you were quite right. It wasn't only that she'd have had the laugh\n"
            "     on all of us if she got away with it. As you said, it would be a\n"
            "     bad precedent."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "but.you" not in full_text

    def test_wrap_013_and_keep(self):
        # Source: Affinities and Other Stories, wrap corruption: and.keep
        passage = (
            "\"Dear Viv: She knows and the worst is over. Breakfast early and\n"
            "     keep out of the way until noon. She is going to work, and anyhow,\n"
            "     it will make her curious. If you have a good retort to the T. C.\n"
            "     business, don't give it at once. It would humiliate her. Then, when\n"
            "     you've given it to her, if she's pleased, you can ask her _the\n"
            "     other_. She's silly about you, Viv, but she won't acknowledge it to\n"
            "     herself."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.keep" not in full_text

    def test_wrap_014_her_promise(self):
        # Source: Affinities and Other Stories, wrap corruption: her.promise
        passage = (
            "\"P. S. Don't make any stipulation about Suffrage, but make her\n"
            "     promise to let you do and think as you like. Be sure. Get her to\n"
            "     write it, if you can. I happen to know that if she marries you, she\n"
            "     hopes you'll take alternate Sundays with her at the Monument, so\n"
            "     she can speak at Camberwell."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "her.promise" not in full_text

    def test_wrap_015_soul_utterly(self):
        # Source: Dangerous Days, wrap corruption: soul.utterly
        passage = (
            "“When first I loved I gave my very soul\n"
            "    Utterly unreserved to Love's control,\n"
            "    But Love deceived me, wrenched my youth away,\n"
            "    And made the gold of life forever gray.\n"
            "    Long I lived lonely, yet I tried in vain\n"
            "    With any other joy to stifle pain;\n"
            "    There is no other joy, I learned to know,\n"
            "    And so returned to love, as long ago,\n"
            "    Yet I, this little while ere I go hence,\n"
            "    Love very lightly now, in self defense.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "soul.utterly" not in full_text

    def test_wrap_016_ours_heard(self):
        # Source: Dangerous Days, wrap corruption: ours.heard
        passage = (
            "His irritation passed as quickly as it came. He felt calm and very sure\n"
            "of himself, and rather light-hearted. Joey, who was by now installed\n"
            "as an office adjunct, and who commonly referred to the mill as “ours,”\n"
            " heard him whistling blithely and cocked an ear in the direction of the\n"
            "inner room."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ours.heard" not in full_text

    def test_wrap_017_you_she(self):
        # Source: Dangerous Days, wrap corruption: you.she
        passage = (
            "“It's hardly worth while struggling to have things attractive for you,”\n"
            " she observed petulantly. “You never notice, anyhow. Clay, do you know\n"
            "that you sit hours and hours, and never talk to me?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.she" not in full_text

    def test_wrap_018_here_what(self):
        # Source: Dangerous Days, wrap corruption: here.what
        passage = (
            "“Hail, hail, the gang's all here,\n"
            "      What the hell do we care?\n"
            "      What the hell do we care?\n"
            "      Hail, hail, the gang's all here,\n"
            "      What the hell do we care now?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "here.what" not in full_text

    def test_wrap_019_you_when(self):
        # Source: K, wrap corruption: you.when
        passage = (
            "“And does it not seem hard to you,\n"
            "      When all the sky is clear and blue,\n"
            "      And I should like so much to play,\n"
            "      To have to go to bed by day?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "you.when" not in full_text

    def test_wrap_020_policeman_reported(self):
        # Source: K, wrap corruption: policeman.reported
        passage = (
            "“An awning from the house door to the curbstone, and a policeman!”\n"
            " reported Mrs. Rosenfeld, who was finding steady employment at the Lorenz\n"
            "house. “And another awning at the church, with a red carpet!”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "policeman.reported" not in full_text

    def test_wrap_021_rose_two(self):
        # Source: K, wrap corruption: rose.two
        passage = (
            "Tillie never learned of that midnight excursion to the “Climbing Rose,”\n"
            " two miles away. Lights blazed in every window; a dozen automobiles were\n"
            "parked before the barn. Somebody was playing a piano. From the bar came\n"
            "the jingle of glasses and loud, cheerful conversation."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rose.two" not in full_text

    def test_wrap_022_not_she(self):
        # Source: K, wrap corruption: not.she
        passage = (
            "“But what shall I say to her? I'd really rather not go, K. Not,”\n"
            " she hastened to set herself right in his eyes--“not that I feel any\n"
            "unwillingness to see her. I know you understand that. But--what in the\n"
            "world shall I say to her?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "not.she" not in full_text

    def test_wrap_023_greatgrand_said(self):
        # Source: K, wrap corruption: greatgrandfather.said
        passage = (
            "There was a strained note in her voice. K., whose ear was attuned to\n"
            "every note in her voice, looked at her quickly. “My great-grandfather,”\n"
            " said Sidney in the same tone, “sold chickens at market. He didn't do it\n"
            "himself; but the fact's there, isn't it?”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "greatgrandfather.said" not in full_text

    def test_wrap_024_passe_regardez(self):
        # Source: Kings Queens and Pawns an American Woman at the Front, wrap corruption: passe.regardez
        passage = (
            "\"_L'Colo du 12me passe\n"
            "         Regardez ce vaillant\n"
            "         Quand il crie dans l'espace\n"
            "         Joyeus'ment 'En avant!'\n"
            "         Ses hommes, la mine heureuse\n"
            "         Gaîment suivent sa trace\n"
            "         Sur la route glorieuse.\n"
            "         Saluez-le, l'Colo du 12me passe_."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "passe.regardez" not in full_text

    def test_wrap_025_your_energies(self):
        # Source: Kings Queens and Pawns an American Woman at the Front, wrap corruption: your.energies
        passage = (
            "\"It is my Royal and Imperial Command that you concentrate your\n"
            "    energies, for the immediate present, upon one single purpose, and\n"
            "    that is that you address all your skill and all the valour of my\n"
            "    soldiers to exterminate first the treacherous English and walk over\n"
            "    General French's contemptible little army."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "your.energies" not in full_text

    def test_wrap_026_part_take(self):
        # Source: Kings Queens and Pawns an American Woman at the Front, wrap corruption: part.take
        passage = (
            "\"The operations in which you are engaged will, for the most part,\n"
            "    take place in a friendly country, and you can do your own country no\n"
            "    better service than in showing yourselves in France and Belgium in\n"
            "    the true character of a British soldier."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "part.take" not in full_text

    def test_wrap_027_together_almost(self):
        # Source: Kings Queens and Pawns an American Woman at the Front, wrap corruption: together.almost
        passage = (
            "\"The men have been called upon to stand for many hours together\n"
            "    almost up to their waists in bitterly cold water, separated by only\n"
            "    one or two hundred yards from a most vigilant enemy.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "together.almost" not in full_text

    def test_wrap_028_could_suggest(self):
        # Source: Kings Queens and Pawns an American Woman at the Front, wrap corruption: could.suggest
        passage = (
            "\"Although every measure which science and medical knowledge could\n"
            "    suggest to mitigate these hardships was employed, the sufferings of\n"
            "    the men have been very great.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "could.suggest" not in full_text

    def test_wrap_029_splendid_though(self):
        # Source: Kings Queens and Pawns an American Woman at the Front, wrap corruption: splendid.though
        passage = (
            "\"In spite of all this they present a most soldier like, splendid,\n"
            "    though somewhat war-worn appearance. Their spirit remains high and\n"
            "    confident; their general health is excellent, and their condition\n"
            "    most satisfactory.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "splendid.though" not in full_text

    def test_wrap_030_prevented_any(self):
        # Source: Kings Queens and Pawns an American Woman at the Front, wrap corruption: prevented.any
        passage = (
            "\"I regard it as most unfortunate that circumstances have prevented\n"
            "    any account of many splendid instances of courage and endurance, in\n"
            "    the face of almost unparalleled hardship and fatigue in war, coming\n"
            "    regularly to the knowledge of the public.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "prevented.any" not in full_text

    def test_wrap_031_evening_post(self):
        # Source: Kings Queens and Pawns an American Woman at the Front, wrap corruption: evening.post
        passage = (
            "\"'I nibble them'--Joffre. See your article in the _Saturday Evening\n"
            "    Post_ of May 29th, 1915. Really, Joffre has had time! It is\n"
            "    September now, and we are not nibbled yet. Still we stand deep in\n"
            "    France. Au revoir à Paris, Madame.\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "evening.post" not in full_text

    def test_wrap_032_thats_the(self):
        # Source: Locked Doors, wrap corruption: thats.the
        passage = (
            "I do not know just why I came here. But I know I’m frightened. That’s\n"
            "  the fact. I think there is something terribly wrong in the house of\n"
            "  Francis M. Reed, 71 Beauregard Square. I think a crime of some sort\n"
            "  has been committed. There are four people in the family, Mr. and Mrs.\n"
            "  Reed and two children. I was to look after the children."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thats.the" not in full_text

    def test_wrap_033_the_room(self):
        # Source: Locked Doors, wrap corruption: the.room
        passage = (
            "I was there four days and the children were never allowed out of the\n"
            "  room. At night we were locked in. I kept wondering what I would do if\n"
            "  there was a fire. The telephone wires are cut so no one can call the\n"
            "  house, and I believe the doorbell is disconnected too. But that’s\n"
            "  fixed now. Mrs. Reed went round all the time with a face like chalk\n"
            "  and her eyes staring. At all hours of the night she’d unlock the\n"
            "  bedroom door and come in and look at the children."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.room" not in full_text

    def test_wrap_034_the_olympic(self):
        # Source: Locked Doors, wrap corruption: the.olympic
        passage = (
            "Francis M. Reed is thirty-six years of age, married, a chemist at the\n"
            "  Olympic Paint Works. He has two children, both boys. Has a small\n"
            "  independent income and owns the house on Beauregard Square, which was\n"
            "  built by his grandfather, General F. R. Reed. Is supposed to be living\n"
            "  beyond his means. House is usually full of servants, and grocer in the\n"
            "  neighborhood has had to wait for money several times."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.olympic" not in full_text

    def test_wrap_035_for_two(self):
        # Source: Locked Doors, wrap corruption: for.two
        passage = (
            "On March thirtieth he applied to the owners of the paint factory for\n"
            "  two weeks’ vacation. Gave as his reason nervousness and insomnia. He\n"
            "  said he was “going to lay off and get some sleep.” Has not been back\n"
            "  at the works since. House under surveillance this afternoon. No\n"
            "  visitors."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "for.two" not in full_text

    def test_wrap_036_poor_the(self):
        # Source: Long Live the King, wrap corruption: poor.the
        passage = (
            "Except for the most ordinary civilities, she had refused to look in his\n"
            "direction. She was correcting an essay in English on Mr. Gladstone,\n"
            "with a blue pencil, and putting in blue commas every here and there. The\n"
            "Crown Prince was amazingly weak in commas. When she was all through, she\n"
            "piled the sheets together and wrote a word on the first page. It might\n"
            "have been “good.” On the other hand, it could easily have been “poor.”\n"
            " The motions of the hand are similar."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "poor.the" not in full_text

    def test_wrap_037_highness_she(self):
        # Source: Long Live the King, wrap corruption: highness.she
        passage = (
            "Her first words to Hedwig were those of Peter Niburg as he linked arms\n"
            "with his enemy and started down the street. “A fine night, Highness,”\n"
            " she said."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "highness.she" not in full_text

    def test_wrap_038_him_she(self):
        # Source: Long Live the King, wrap corruption: him.she
        passage = (
            "Miss Braithwaite looked troubled. “No doubt something has detained him,”\n"
            " she said, with unusual gentleness. “You might work at the frame for your\n"
            "Cousin Hedwig. Then, if Captain Larisch comes, you can still have a part\n"
            "of your lesson.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "him.she" not in full_text

    def test_wrap_039_race_she(self):
        # Source: Long Live the King, wrap corruption: race.she
        passage = (
            "Olga, the wardrobe woman, was also on her way to the Opera, which faced\n"
            "the park. She also saw the carriage, and at first her eyes twinkled. It\n"
            "was he, of course. The daring of him! But, as the carriage drew nearer,\n"
            "she bent forward. He looked pale, and there was a wistful droop to his\n"
            "mouth. “They have punished him for the little prank,” she muttered.\n"
            "“That tight-faced Englishwoman, of course. The English are a hard race.”\n"
            " She, too, went on."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "race.she" not in full_text

    def test_wrap_040_await_you(self):
        # Source: Long Live the King, wrap corruption: await.you
        passage = (
            "MADAME,--To-night at one o’clock a closed fiacre will await\n"
            "  you in the Street of the Wise Virgins, near the church.  You\n"
            "  will go in it, without fail, to wherever it takes you.\n"
            "                                 (Signed)THE COMMITTEE OF TEN"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "await.you" not in full_text

    def test_wrap_041_highness_standing(self):
        # Source: Long Live the King, wrap corruption: highness.standing
        passage = (
            "Nikky went out into the corridor, and became the Chamberlain. He stepped\n"
            "inside, bowed, and announced: “The delegation from the city, Highness,”\n"
            " standing very stiff, and a trifle bowlegged, as the Chamberlain was.\n"
            "Then he bowed again, and waddled out--the Chamberlain was fat--and\n"
            "became the delegation."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "highness.standing" not in full_text

    def test_wrap_042_book_because(self):
        # Source: Long Live the King, wrap corruption: book.because
        passage = (
            "“It is midnight,” she would say firmly--or one o’clock, or even later,\n"
            "for the Chancellor was old, and needed little sleep. “Give me the book.”\n"
            " Because, if she did not take it, he would carry it off to bed, and\n"
            "reading in bed is bad for the eyes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "book.because" not in full_text

    def test_wrap_043_another_his(self):
        # Source: Long Live the King, wrap corruption: another.his
        passage = (
            "“Adelbert, Excellency. As to occupation, for years I was connected with\n"
            "the Opera. Twenty years, Excellency. Then I grew old, and another--”\n"
            " His voice broke. What with excitement and terror, he was close to tears.\n"
            "“Now I am reduced to selling tickets for an American contrivance, a\n"
            "foolish thing, but I earn my bread by it.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "another.his" not in full_text

    def test_wrap_044_fancy_she(self):
        # Source: Long Live the King, wrap corruption: fancy.she
        passage = (
            "“Not to a young couple, come to him, perhaps, in peasant costume. They\n"
            "are glad to marry, these fathers. There is much irregularity. I fancy,”\n"
            " she added, still with her carefully detached manner, “that a marriage\n"
            "could be easily arranged.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fancy.she" not in full_text

    def test_wrap_045_night_his(self):
        # Source: Long Live the King, wrap corruption: night.his
        passage = (
            "“Worse than that. The old King gone and no Crown Prince! It may mean\n"
            "almost any sort of trouble! I’ve closed up at the Park for the night.”\n"
            " His arm around his wife, he looked through the doorway to where Bobby\n"
            "and Ferdinand were counting the candles. “It’s made me think pretty\n"
            "hard,” he said. “Bobby mustn’t go around alone the way he’s been doing.\n"
            "All Americans here are considered millionaires. If the Crown Prince\n"
            "could go, think how easy--”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "night.his" not in full_text

    def test_wrap_046_box_said(self):
        # Source: Long Live the King, wrap corruption: box.said
        passage = (
            "“The one in which Your Majesty’s seal ring came is here. Also there is\n"
            "one in the study which contained crayons.”--“I’ll have the ring box,”\n"
            " said His Majesty."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "box.said" not in full_text

    def test_wrap_047_bold_and(self):
        # Source: Love Stories, wrap corruption: bold.and
        passage = (
            "_Oh, I am the cook and the captain bold,\n"
            "             And the mate of the Nancy brig,\n"
            "           And the bosun tight and the midshipmite,\n"
            "             And the crew of the captain's gig._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bold.and" not in full_text

    def test_wrap_048_fresh_meats(self):
        # Source: Love Stories, wrap corruption: fresh.meats
        passage = (
            "I will not supply the Valley Hospital with any fresh\n"
            "      meats, canned oysters and sausages, or do any plumbing\n"
            "      for the hospital until the reinstatement of Dr. Sheets.\n"
            "                                T. CASHDOLLAR, Butcher."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fresh.meats" not in full_text

    def test_wrap_049_ribber_far(self):
        # Source: Love Stories, wrap corruption: ribber.far
        passage = (
            "_'Way down upon de S'wanee Ribber,\n"
            "             Far, far away,\n"
            "           Dere's wha my heart is turnin' ebber--\n"
            "             Dere's wha de old folks stay._"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ribber.far" not in full_text

    def test_wrap_050_preparatio_where(self):
        # Source: Love Stories, wrap corruption: preparation.where
        passage = (
            "\"_Are strewn this day in festal preparation,\n"
            "         Where Jesus comes to wipe our tears away--\n"
            "         E'en now the throng to welcome Him prepare._\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "preparation.where" not in full_text

    def test_wrap_051_just_going(self):
        # Source: Love Stories, wrap corruption: just.going
        passage = (
            "Dear Edith: I have put in a rotten evening and am just\n"
            "      going to bed. I am rather worried because you looked so\n"
            "      tired to-day. Please don't work too hard."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "just.going" not in full_text

    def test_wrap_052_tight_said(self):
        # Source: Sight Unseen, wrap corruption: tight.said
        passage = (
            "“Please be sure you are holding my hands tight. Hold them very tight,”\n"
            " said Miss Jeremy. Her voice sounded faint and far away. Her head was\n"
            "dropped forward on her chest, and she suddenly sagged in her chair.\n"
            "Sperry broke the circle and coming to her, took her pulse. It was, he\n"
            "reported, very rapid."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tight.said" not in full_text

    def test_wrap_053_controls_can(self):
        # Source: Sight Unseen, wrap corruption: controls.can
        passage = (
            "We went back, I remember, to speaking of the seance itself, and to the\n"
            "safer subject of the physical phenomena. As I have said, we did not\n"
            "then know of those experimenters who claim that the medium can evoke\n"
            "so-called rods of energy, and that by its means the invisible “controls”\n"
            " can perform their strange feats of levitation and the movement of solid\n"
            "bodies. Sperry touched very lightly on the spirit side."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "controls.can" not in full_text

    def test_wrap_054_that_she(self):
        # Source: Sight Unseen, wrap corruption: that.she
        passage = (
            "When, at noon and luncheon, I tried to tell her the truth, she listened\n"
            "to the end: Then: “I should think you could have done better than that,”\n"
            " she said. “You have had all morning to think it out.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.she" not in full_text

    def test_wrap_055_happened_clara(self):
        # Source: Sight Unseen, wrap corruption: happened.clara
        passage = (
            "“It doesn’t explain how that medium knew everything that happened,”\n"
            " Clara put in, excitedly. “She knew it all, even the library paste! I can\n"
            "tell you, Mr. Johnson, I was close to fainting a dozen times before I\n"
            "finally did it.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "happened.clara" not in full_text

