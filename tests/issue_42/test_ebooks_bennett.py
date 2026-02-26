import pytest
from fast_sentence_segment import segment_text


class TestEbooksBennett:
    """Integration tests mined from Arnold Bennett ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1900s
    """

    def test_wrap_001_mean_she(self):
        # Source: A Great Man a Frolic, wrap corruption: mean.she
        passage = (
            "'Upon this hint I spoke--spake, I mean;\n"
            "     She loved me for the dangers I had passed,\n"
            "     And I loved her that she did pity them.\n"
            "     This only is the witchcraft I have used.\n"
            "     Here comes the lady; let her witness it.'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mean.she" not in full_text

    def test_wrap_002_ear_her(self):
        # Source: Books and Persons Being Comments on a Past Epoch 1908 1911, wrap corruption: ear.her
        passage = (
            "To Love's low voice she lent a careless ear;\n"
            "    Her band within his rosy fingers lay,\n"
            "    A chilling weight. She would, not turn or hear;\n"
            "    But with averted, face went on her way.\n"
            "    But when pale Death, all featureless and grim,\n"
            "    Lifted his bony hand, and beckoning\n"
            "    Held out his cypress-wreath, she followed him,\n"
            "    And Love was left forlorn and wondering,\n"
            "    That she who for his bidding would not stay,\n"
            "    At Death's first whisper rose and went away."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ear.her" not in full_text

    def test_wrap_003_cry_thine(self):
        # Source: Books and Persons Being Comments on a Past Epoch 1908 1911, wrap corruption: cry.thine
        passage = (
            "Mother, O grey sea-mother, thine is the crowning cry!\n"
            "    Thine the glory for ever in the nation born of thy womb!\n"
            "    Thine is the Sword and the Shield and the shout that Salamis heard,\n"
            "    Surging in Æschylean splendour, earth-shaking acclaim!\n"
            "    Ocean-mother of England, thine is the throne of her fame!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "cry.thine" not in full_text

    def test_wrap_004_blood_drawn(self):
        # Source: Clayhanger, wrap corruption: blood.drawn
        passage = (
            "There is a fountain filled with blood\n"
            "  Drawn from Emmanuel's veins;\n"
            "  And sinners, plunged beneath that flood,\n"
            "  Lose all their guilty stains.\n"
            "  ...\n"
            "  Dear dying Lamb, Thy precious blood--"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "blood.drawn" not in full_text

    def test_wrap_005_drawn_attention(self):
        # Source: Denry the Audacious, wrap corruption: drawn.attention
        passage = (
            "\"The recent sensational burglary at Sneyd Hall has drawn\n"
            "    attention to the magnificent state apartments of that unique\n"
            "    mansion.  As very few but the personal friends of the family are\n"
            "    allowed a glimpse of these historic rooms, they being of course\n"
            "    quite closed to the public, we have thought that some account of\n"
            "    them might interest the readers of the Signal. On the occasion\n"
            "    of our last visit...\" etc."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "drawn.attention" not in full_text

    def test_wrap_006_trip_obstinacy(self):
        # Source: From the Log of the Velsa, wrap corruption: trip.obstinacy
        passage = (
            "“No,” I said, not a hero. “We ‘ll give up Manningtree this trip.”\n"
            " Obstinacy in adventure might have meant twelve hours in the mud. The\n"
            "crew breathed relief. We returned, with great care, to civilization.\n"
            "We knew now why the Stour is a desolate stream. Thus to this day I have\n"
            "never reached Manningtree except in an automobile."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "trip.obstinacy" not in full_text

    def test_wrap_007_thee_and(self):
        # Source: Hilda Lessways, wrap corruption: thee.and
        passage = (
            "All thy old woes shall now smile on thee,\n"
            "    And thy pains sit bright upon thee,\n"
            "    All thy sorrows here shall shine,\n"
            "    All thy sufferings be divine:\n"
            "    Tears shall take comfort, and turn gems,\n"
            "    And wrongs repent to diadems."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thee.and" not in full_text

    def test_wrap_008_him_keys(self):
        # Source: Hugo a Fantasia on Modern Themes, wrap corruption: him.keys
        passage = (
            "'Mr. Polycarp has just been here, and accidentally left behind him\n"
            "    keys of his vault, including safe of late Mr. Francis Tudor, etc.\n"
            "    In these peculiar circumstances I shall be glad to know what I am to\n"
            "    do."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "him.keys" not in full_text

    def test_wrap_009_some_extraordin(self):
        # Source: Hugo a Fantasia on Modern Themes, wrap corruption: some.extraordinary
        passage = (
            "'\"I have reason to think that you may be interested in some\n"
            "    extraordinary information which I have in my possession concerning\n"
            "    Camilla Tudor, who is supposed to have been buried at Brompton\n"
            "    Cemetery in July last year. If I am right, perhaps you will\n"
            "    accompany the bearer to my rooms. At present I will not disclose my\n"
            "    name."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "some.extraordinary" not in full_text

    def test_wrap_010_seen_flatter(self):
        # Source: Literary Taste How to Form It With Detailed Instructions for Collecting a Comple, wrap corruption: seen.flatter
        passage = (
            "Full many a glorious morning have I seen\n"
            "		Flatter the mountain-tops with sovereign eye,\n"
            "	Kissing with golden face the meadows green,\n"
            "		Gilding pale streams with heavenly alchemy."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "seen.flatter" not in full_text

    def test_wrap_011_soul_that(self):
        # Source: Literary Taste How to Form It With Detailed Instructions for Collecting a Comple, wrap corruption: soul.that
        passage = (
            "The Upholder of the tranquil soul\n"
            "	That tolerates the indignities of Time\n"
            "	And, from the centre of Eternity\n"
            "	All finite motions over-ruling, lives\n"
            "	In glory immutable."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "soul.that" not in full_text

    def test_wrap_012_see_there(self):
        # Source: Paris Nights and Other Impressions of Places and People, wrap corruption: see.there
        passage = (
            "Later in the day I asked him if he would come down early again to-morrow\n"
            "and have breakfast with me. He said: “I don’t know. I shall see.”\n"
            " There was no pose in this. Simply a perfect preoccupation with his\n"
            "own interests and welfare. I should say he is absolutely egotistic. He\n"
            "always employs natural, direct methods to get what he wants and to avoid\n"
            "what lie doesn’t want."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "see.there" not in full_text

    def test_wrap_013_selfmanage_married(self):
        # Source: Riceyman Steps a Novel, wrap corruption: selfmanagement.married
        passage = (
            "Self and Self-Management\n"
            "    Married Life\n"
            "    Friendship and Happiness\n"
            "    The Human Machine\n"
            "    How to Live on 24 Hours a Day\n"
            "    Literary Taste\n"
            "    Mental Efficiency\n"
            "    The Author's Craft\n"
            "    How to Make the Best of Life"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "selfmanagement.married" not in full_text

    def test_wrap_014_match_body(self):
        # Source: Riceyman Steps a Novel, wrap corruption: match.body
        passage = (
            "The Love Match\n"
            "    Body and Soul\n"
            "    Sacred and Profane Love\n"
            "    Judith\n"
            "    The Title\n"
            "    The Great Adventure\n"
            "    Cupid and Commonsense\n"
            "    What the Public Wants\n"
            "    Polite Farces\n"
            "    The Honeymoon"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "match.body" not in full_text

    def test_wrap_015_women_books(self):
        # Source: Riceyman Steps a Novel, wrap corruption: women.books
        passage = (
            "Our Women\n"
            "    Books and Persons\n"
            "    Paris Nights\n"
            "    The Truth About an Author\n"
            "    Liberty!\n"
            "    Over There: War Scenes\n"
            "    Things That Have Interested Me\n"
            "    Things That Have Interested Me (second series)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "women.books" not in full_text

    def test_wrap_016_north_anna(self):
        # Source: Self and Self Management B Essays About Existing, wrap corruption: north.anna
        passage = (
            "A Man from the North\n"
            "  Anna of the Five Towns\n"
            "  Leonora\n"
            "  A Great Man\n"
            "  Sacred and Profane Love\n"
            "  Whom God hath Joined\n"
            "  Buried Alive\n"
            "  The Old Wives’ Tale\n"
            "  The Glimpse\n"
            "  Helen with the High Hand\n"
            "  Clayhanger\n"
            "  The Card\n"
            "  Hilda Lessways\n"
            "  The Regent\n"
            "  The Price of Love\n"
            "  These Twain\n"
            "  The Lion’s Share\n"
            "  The Pretty Lady\n"
            "  The Roll-Call"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "north.anna" not in full_text

    def test_wrap_017_day_the(self):
        # Source: Self and Self Management B Essays About Existing, wrap corruption: day.the
        passage = (
            "How to Live on Twenty-Four Hours a Day\n"
            "  The Human Machine\n"
            "  Mental Efficiency\n"
            "  Literary Taste\n"
            "  Friendship and Happiness\n"
            "  Married Life\n"
            "  Those United States\n"
            "  Paris Nights\n"
            "  Books and Persons"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "day.the" not in full_text

    def test_wrap_018_for_benefit(self):
        # Source: Tales of the Five Towns, wrap corruption: for.benefit
        passage = (
            "'Each member shall, on the death of another member, pay 1s. for\n"
            "    benefit of widow or nominee of deceased, same to be paid within\n"
            "    one month after notice given.'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "for.benefit" not in full_text

    def test_wrap_019_the_card(self):
        # Source: Tales of the Five Towns, wrap corruption: the.card
        passage = (
            "'Or nominee--nominee,' he murmured reflectively, staring at the\n"
            "    card. He mechanically noticed, what he had noticed often before\n"
            "    with disdain, that the chairman had signed the rules without the\n"
            "    use of capitals."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.card" not in full_text

    def test_wrap_020_death_shall(self):
        # Source: Tales of the Five Towns, wrap corruption: death.shall
        passage = (
            "'I request that the money due to me from the Slate Club on my death\n"
            "    shall be paid to my nominee, Miss Susan Trimmer, now staying with\n"
            "    her aunt, Mrs. Penrose, at Bursley."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "death.shall" not in full_text

    def test_wrap_021_the_end(self):
        # Source: Tales of the Five Towns, wrap corruption: the.end
        passage = (
            "'P.S.--My annual salary of sixpence per member would be due at the\n"
            "     end of December. If so be the members would pay that, or part of\n"
            "     it, should they consider the same due, to Susan Trimmer as well, I\n"
            "     should be thankful.--Yours resp, W.F.'"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.end" not in full_text

    def test_wrap_022_done_for(self):
        # Source: Tales of the Five Towns, wrap corruption: done.for
        passage = (
            "'You will be surprised but not glad to get this letter. I'm done\n"
            "    for, and you will never see me again. I'm sorry for what I've done,\n"
            "    and how I've treated you, but it's no use saying anything now. If\n"
            "    Pater had only lived he might have kept me in order. But you were\n"
            "    too kind, you know. You've had a hard struggle these last six\n"
            "    years, and I hope Arthur and Dick will stand by you better than I\n"
            "    did, now they are growing up. Give them my love, and kiss little\n"
            "    Fannie for me."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "done.for" not in full_text

    def test_wrap_023_the_woman(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: the.woman
        passage = (
            "The individual who scoffs at New Year’s resolutions resembles the\n"
            "  woman who says she doesn’t look under the bed at nights; the truth is\n"
            "  not in him."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.woman" not in full_text

    def test_wrap_024_the_pleasure(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: the.pleasure
        passage = (
            "To give pleasure is the highest end of any work of art, because the\n"
            "  pleasure procured from any art is tonic, and transforms the life into\n"
            "  which it enters."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.pleasure" not in full_text

    def test_wrap_025_but_fatiguing(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: but.fatiguing
        passage = (
            "To enjoy a work of imagination is no pastime, rather a sweet but\n"
            "  fatiguing labour. After a play of Shakespeare or a Wagnerian opera\n"
            "  repose is needed. Only a madman like Louis of Bavaria could demand\n"
            "  Tristan twice in one night."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "but.fatiguing" not in full_text

    def test_wrap_026_great_men(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: great.men
        passage = (
            "Great books do not spring from something accidental in the great\n"
            "  men who wrote them. They are the effluence of their very core, the\n"
            "  expression of the life itself of the authors."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "great.men" not in full_text

    def test_wrap_027_our_instinctiv(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: our.instinctive
        passage = (
            "The brain is the diplomatist which arranges relations between our\n"
            "  instinctive self and the universe, and it fulfils its mission when it\n"
            "  provides for the maximum of freedom to the instincts with the minimum\n"
            "  of friction."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "our.instinctive" not in full_text

    def test_wrap_028_that_literature(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: that.literature
        passage = (
            "To utter a jeremiad upon the decadence of taste, to declare that\n"
            "  literature is going to the dogs because a fourth-rate novel has been\n"
            "  called a masterpiece and has made someone’s fortune, would be absurd.\n"
            "  I have a strong faith that taste is as good as ever it was, and that\n"
            "  literature will continue on its way undisturbed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.literature" not in full_text

    def test_wrap_029_kind_that(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: kind.that
        passage = (
            "There is a loveliness of so imperious, absolute, dazzling a kind\n"
            "  that it banishes from the hearts of men all moral conceptions, all\n"
            "  considerations of right and wrong, and leaves therein nothing but\n"
            "  worship and desire."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "kind.that" not in full_text

    def test_wrap_030_and_satisfying(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: and.satisfying
        passage = (
            "When homage is reiterated, when the pleasure of obeying a command and\n"
            "  satisfying a caprice is begged for, when roses are strewn, and even\n"
            "  necks put down in the path, one forgets to be humble; one forgets\n"
            "  that in meekness alone lies the sole good; one confuses deserts with\n"
            "  the hazards of heredity."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.satisfying" not in full_text

    def test_wrap_031_the_moment(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: the.moment
        passage = (
            "The uncultivated reader is content to live wholly in and for the\n"
            "  moment, sentence by sentence. Keep him amused and he will ask no\n"
            "  more. You may delude him, you may withhold from him every single\n"
            "  thing to which he is rightfully entitled, but he will not care. The\n"
            "  more crude you are, the better will he be pleased."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.moment" not in full_text

    def test_wrap_032_one_way(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: one.way
        passage = (
            "A merely literary crudity will affect the large public neither one\n"
            "  way nor the other, since the large public is entirely uninterested in\n"
            "  questions of style; but all other crudities appeal strongly to that\n"
            "  public."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "one.way" not in full_text

    def test_wrap_033_that_ensues(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: that.ensues
        passage = (
            "Everyone who has driven a motor-car knows the uncanny sensation that\n"
            "  ensues when for the first time in your life you engage the clutch,\n"
            "  and the Thing beneath you begins mysteriously and formidably to move.\n"
            "  It is at once an astonishment, a terror, and a delight. I felt like\n"
            "  that as I watched the progress of my first play."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "that.ensues" not in full_text

    def test_wrap_034_due_far(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: due.far
        passage = (
            "I knew that when love lasted, the credit of the survival was due\n"
            "  far more often to the woman than to the man. The woman must husband\n"
            "  herself, dole herself out, economise herself so that she might be\n"
            "  splendidly wasteful when need was. The woman must plan, scheme,\n"
            "  devise, invent, reconnoitre, take precautions; and do all this\n"
            "  sincerely and lovingly in the name and honour of love. A passion for\n"
            "  her is a campaign; and her deadliest enemy is satiety."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "due.far" not in full_text

    def test_wrap_035_last_ounce(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: last.ounce
        passage = (
            "Efficient living, living up to one’s best standard, getting the last\n"
            "  ounce of power out of the machine with the minimum of friction: these\n"
            "  things depend on the disciplined and vigorous condition of the brain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "last.ounce" not in full_text

    def test_wrap_036_not_know(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: not.know
        passage = (
            "In the world of books, as in every other world, one-half does not\n"
            "  know how the other half lives. In literary matters the literate\n"
            "  seldom suspect the extreme simplicity and naïveté of the\n"
            "  illiterate. They wilfully blind themselves to it; they are afraid to\n"
            "  face it."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "not.know" not in full_text

    def test_wrap_037_average_wellintent(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: average.wellintentioned
        passage = (
            "As regards facts and ideas, the great mistake made by the average\n"
            "  well-intentioned reader is that he is content with the names of\n"
            "  things instead of occupying himself with the causes of things."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "average.wellintentioned" not in full_text

    def test_wrap_038_and_definitely(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: and.definitely
        passage = (
            "If a man does not spend at least as much time in actively and\n"
            "  definitely thinking about what he has read as he spent in reading, he\n"
            "  is simply insulting his author."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.definitely" not in full_text

    def test_wrap_039_know_ambition(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: know.ambition
        passage = (
            "He was of that small and lonely minority of men who never know\n"
            "  ambition, ardour, zeal, yearning, tears; whose convenient desires are\n"
            "  capable of immediate satisfaction; of whom it may be said that they\n"
            "  purchase a second-rate happiness cheap at the price of an incapacity\n"
            "  for deep feeling."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "know.ambition" not in full_text

    def test_wrap_040_the_imaginatio(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: the.imagination
        passage = (
            "Size is the quality which most strongly and surely appeals to the\n"
            "  imagination of the multitude. Of all modern monuments the Eiffel\n"
            "  Tower and the Big Wheel have aroused the most genuine curiosity and\n"
            "  admiration: they are the biggest. As with this monstrous architecture\n"
            "  of metals, so with the fabric of ideas and emotions: the attention\n"
            "  of the whole crowd can only be caught by an audacious hugeness, an\n"
            "  eye-smiting enormity of dimensions so gross as to be nearly physical."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.imagination" not in full_text

    def test_wrap_041_and_the(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: and.the
        passage = (
            "I had fast in my heart’s keeping the new truth that in the body, and\n"
            "  the instincts of the body, there should be no shame but rather a\n"
            "  frank, joyous pride."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.the" not in full_text

    def test_wrap_042_all_costs(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: all.costs
        passage = (
            "Having once decided to achieve a certain task, achieve it at all\n"
            "  costs of tedium and distaste. The gain in self-confidence of having\n"
            "  accomplished a tiresome labour is immense."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.costs" not in full_text

    def test_wrap_043_literature_merely(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: literature.merely
        passage = (
            "Many writers, and many clever writers, use the art of literature\n"
            "  merely to gain an end which is connected with some different art, or\n"
            "  with no art. Such a writer, finding himself burdened with a message\n"
            "  prophetic, didactic, or reforming, discovers suddenly that he has\n"
            "  the imaginative gift, and makes his imagination the servant of his\n"
            "  intellect, or of emotions which are not artistic emotions."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "literature.merely" not in full_text

    def test_wrap_044_and_without(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: and.without
        passage = (
            "To take the common grey things which people know and despise, and,\n"
            "  without tampering, to disclose their epic significance, their\n"
            "  essential grandeur--that is realism as distinguished from idealism or\n"
            "  romanticism. It may scarcely be, it probably is not, the greatest art\n"
            "  of all; but it is art precious and indisputable."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.without" not in full_text

    def test_wrap_045_are_almost(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: are.almost
        passage = (
            "Some people have a gift of conjuring with conversations. They are\n"
            "  almost always frankly and openly interested in themselves. You may\n"
            "  seek to foil them; you may even violently wrench the conversation\n"
            "  into other directions. But every effort will be useless. They will\n"
            "  beat you. You had much better lean back in your chair and enjoy their\n"
            "  legerdemain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "are.almost" not in full_text

    def test_wrap_046_themselves_done(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: themselves.done
        passage = (
            "Diaries, save in experienced hands, are apt to get themselves\n"
            "  done with the very minimum of mental effort. They also tend to an\n"
            "  exaggeration of egotism, and if they are left lying about they tend\n"
            "  to strife."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "themselves.done" not in full_text

    def test_wrap_047_vocation_that(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: vocation.that
        passage = (
            "It is characteristic of the literary artist with a genuine vocation\n"
            "  that his large desire is, not to express in words any particular\n"
            "  thing, but to express himself, the sum of his sensations. He feels\n"
            "  the vague, disturbing impulse to write long before he has chosen\n"
            "  his first subject from the thousands of subjects which present\n"
            "  themselves, and which in the future he is destined to attack."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "vocation.that" not in full_text

    def test_wrap_048_social_reformers(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: social.reformers
        passage = (
            "In England, nearly all the most interesting people are social\n"
            "  reformers: and the only circles of society in which you are not\n"
            "  bored, in which there is real conversation, are the circles of social\n"
            "  reform."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "social.reformers" not in full_text

    def test_wrap_049_human_machine(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: human.machine
        passage = (
            "The art of life, the art of extracting all its power from the human\n"
            "  machine, does not lie chiefly in processes of bookish-culture, nor\n"
            "  in contemplations of the beauty and majesty of existence. It lies\n"
            "  chiefly in keeping the peace, the whole peace, and nothing but the\n"
            "  peace, with those with whom one is “thrown.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "human.machine" not in full_text

    def test_wrap_050_carefully_nurtured(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: carefully.nurtured
        passage = (
            "An accurate knowledge of any subject, coupled with a carefully\n"
            "  nurtured sense of the relativity of that subject to other subjects,\n"
            "  implies an enormous self-development."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "carefully.nurtured" not in full_text

    def test_wrap_051_something_rather(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: something.rather
        passage = (
            "The man who loses his temper often thinks he is doing something\n"
            "  rather fine and majestic. On the contrary, so far is this from being\n"
            "  the fact, he is merely making an ass of himself."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "something.rather" not in full_text

    def test_wrap_052_apparently_trivial(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: apparently.trivial
        passage = (
            "The female sex is prone to be inaccurate and careless of apparently\n"
            "  trivial detail, because this is the general tendency of mankind.\n"
            "  In men destined for a business or a profession, the proclivity is\n"
            "  harshly discouraged at an early stage. In women, who usually are not\n"
            "  destined for anything whatever, it enjoys a merry life, and often\n"
            "  refuses to be improved out of existence when the sudden need arises.\n"
            "  No one by taking thought can deracinate the mental habits of, say,\n"
            "  twenty years."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "apparently.trivial" not in full_text

    def test_wrap_053_qualitiesa_its(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: qualitiesand.its
        passage = (
            "Kindliness of heart is not the greatest of human qualities--and\n"
            "  its general effect on the progress of the world is not entirely\n"
            "  beneficent--but it is the greatest of human qualities in friendship."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "qualitiesand.its" not in full_text

    def test_wrap_054_mental_processes(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: mental.processes
        passage = (
            "The great public is no fool. It is huge and simple and slow in mental\n"
            "  processes, like a good-humoured giant, easy to please and grateful for\n"
            "  diversion. But it has a keen sense of its own dignity; it will not be\n"
            "  trifled with; it resents for ever the tongue in the cheek."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mental.processes" not in full_text

    def test_wrap_055_divided_into(self):
        # Source: The Arnold Bennett Calendar, wrap corruption: divided.into
        passage = (
            "The respectable portion of the male sex in England may be divided\n"
            "  into two classes, according to its method and manner of complete\n"
            "  immersion in water. One class, the more dashing, dashes into a cold\n"
            "  tub every morning. Another, the more cleanly, sedately takes a warm\n"
            "  bath every Saturday night. There can be no doubt that the former\n"
            "  class lends tone and distinction to the country, but the latter is\n"
            "  the nation’s backbone."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "divided.into" not in full_text

