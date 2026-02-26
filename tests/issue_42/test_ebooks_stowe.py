import pytest
from fast_sentence_segment import segment_text


class TestEbooksStowe:
    """Integration tests mined from Harriet Beecher Stowe ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1860s
    """

    def test_wrap_001_which_hand(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: which.hand
        passage = (
            "Write to me about the crooked-fingered negro, and let me know which\n"
            "  hand and which finger, color, &c.; likewise any mark the fellow has\n"
            "  who says he got away from the negro-buyer, with his height and\n"
            "  color, or any other you think has run off."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "which.hand" not in full_text

    def test_wrap_002_person_but(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: person.but
        passage = (
            "Give my respects to your partner, and be sure you write to no person\n"
            "  but myself. If any person writes to you, you can inform me of it,\n"
            "  and I will try to buy from them. I think we can make money, if we\n"
            "  do business together; for I have plenty of money, if you can find\n"
            "  plenty of negroes. Let me know if Daniel is still where he was, and\n"
            "  if you have heard anything of Francis since I left you. Accept for\n"
            "  yourself my regard and esteem."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "person.but" not in full_text

    def test_wrap_003_justice_that(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: justice.that
        passage = (
            "I am not, however, altogether clear, to do John Caphart justice,\n"
            "  that he is entirely conscience-proof. There was something in his\n"
            "  anxious look which leaves one not without hope."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "justice.that" not in full_text

    def test_wrap_004_passed_merely(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: passed.merely
        passage = (
            "At the first trial we did not know of his pursuits, and he passed\n"
            "  merely as a police-man of Norfolk, Virginia. But, at the second\n"
            "  trial, some one in the room gave me a hint of the occupations many\n"
            "  of these police-men take to, which led to my cross-examination."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "passed.merely" not in full_text

    def test_wrap_005_niggers_you(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: niggers.you
        passage = (
            "A. [Looking calmly round the room.] I don’t know how many niggers\n"
            "  you have got here in Massachusetts, but I should think I had flogged\n"
            "  as many as you’ve got in the state."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "niggers.you" not in full_text

    def test_wrap_006_are_about(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: are.about
        passage = (
            "P. S.—It might have been stated above that on this estate there are\n"
            "  about one hundred and sixty blacks. With the exception of infants,\n"
            "  there has been, in eighteen months, but one death that I\n"
            "  remember,—that of a man fully sixty-five years of age. The bill for\n"
            "  medical attendance, from the second day of last November, comprising\n"
            "  upwards of a year, is less than forty dollars."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "are.about" not in full_text

    def test_wrap_007_small_about(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: small.about
        passage = (
            "Runaway about the 15th of August last, Joe, a yellow man; small,\n"
            "  about 5 feet 8 or 9 inches high, and about 20 years of age. _Has a\n"
            "  Roman nose_, was raised in New Orleans, and _speaks French and\n"
            "  English_. He was bought last winter of Mr. Digges, Banks Arcade, New\n"
            "  Orleans."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "small.about" not in full_text

    def test_wrap_008_six_months(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: six.months
        passage = (
            "The terms of sale are one-half cash, the balance on a credit of six\n"
            "  months, with interest, for notes payable at bank, with two or more\n"
            "  approved endorsers."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "six.months" not in full_text

    def test_wrap_009_good_pilot(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: good.pilot
        passage = (
            "Will be sold at private sale, a LIKELY MAN, boat hand, and good\n"
            "  pilot; is well acquainted with all the inlets between here and\n"
            "  Savannah and Georgetown."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "good.pilot" not in full_text

    def test_wrap_010_the_slaves(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: the.slaves
        passage = (
            "If there be one so lost to all feeling as even to say that the\n"
            "  slaves do not suffer when families are separated, let such a one\n"
            "  go to the ragged quilt which was my couch and pillow, and stand\n"
            "  there night after night, for long, weary hours, and see the bitter\n"
            "  tears streaming down the face of that more than orphan boy, while\n"
            "  with half-suppressed sighs and sobs he calls again and again upon\n"
            "  his absent mother."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.slaves" not in full_text

    def test_wrap_011_shed_hovered(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: shed.hovered
        passage = (
            "“Say, wast thou conscious of the tears I shed?\n"
            "            Hovered thy spirit o’er thy sorrowing son?\n"
            "            Wretch even then! life’s journey just begun.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shed.hovered" not in full_text

    def test_wrap_012_shrill_call(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: shrill.call
        passage = (
            "Such horror has seized me, lest I might not hear the first shrill\n"
            "  call, that I have often in dreams fancied I heard that unwelcome\n"
            "  voice, and have leaped from my couch and walked through the house\n"
            "  and out of it before I awoke. I have gone and called the other\n"
            "  slaves, in my sleep, and asked them if they did not hear master\n"
            "  call. Never, while I live, will the remembrance of those long,\n"
            "  bitter nights of fear pass from my mind."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shrill.call" not in full_text

    def test_wrap_013_these_ten(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: these.ten
        passage = (
            "But all my severe labor, and bitter and cruel punishments, for these\n"
            "  ten years of captivity with this worse than Arab family, all these\n"
            "  were as nothing to the sufferings I experienced by being separated\n"
            "  from my mother, brothers and sisters; the same things, with them\n"
            "  near to sympathize with me, to hear my story of sorrow, would have\n"
            "  been comparatively tolerable."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "these.ten" not in full_text

    def test_wrap_014_separate_room(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: separate.room
        passage = (
            "From this time I was most narrowly watched. If I was in a separate\n"
            "  room any considerable length of time, I was sure to be suspected of\n"
            "  having a book, and was at once called to give an account of myself.\n"
            "  All this, however, was too late. The first step had been taken.\n"
            "  Mistress, in teaching me the alphabet, had given me the inch, and\n"
            "  no precaution could prevent me from taking the ell."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "separate.room" not in full_text

    def test_wrap_015_safely_confine(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: safely.confine
        passage = (
            "“$100 will be paid to any person who may apprehend and safely\n"
            "  confine in any jail in this state a certain negro man, named ALFRED.\n"
            "  And the same reward will be paid, if satisfactory evidence is given\n"
            "  of his having been KILLED. He has one or more scars on one of his\n"
            "  hands, caused by his having been shot."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "safely.confine" not in full_text

    def test_wrap_016_his_apprehensi(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: his.apprehension
        passage = (
            "“RANAWAY, my negro man RICHARD. A reward of $25 will be paid for his\n"
            "  apprehension, DEAD or ALIVE. Satisfactory proof will only be\n"
            "  required of his being KILLED. He has with him, in all probability,\n"
            "  his wife, ELIZA, who ran away from Col. Thompson, now a resident of\n"
            "  Alabama, about the time he commenced his journey to that state."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "his.apprehension" not in full_text

    def test_wrap_017_without_the(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: without.the
        passage = (
            "“About the 1st of March last the negro man RANSOM left me without\n"
            "  the least provocation whatever; I will give a reward of twenty\n"
            "  dollars for said negro, if taken, DEAD OR ALIVE,—and if killed in\n"
            "  any attempt, an advance of five dollars will be paid."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "without.the" not in full_text

    def test_wrap_018_fifty_dollars(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: fifty.dollars
        passage = (
            "“RANAWAY from the subscriber, a negro man named SAMPSON. Fifty\n"
            "  dollars reward will be given for the delivery of him to me, or his\n"
            "  confinement in any jail, so that I get him; and should he resist in\n"
            "  being taken, so that violence is necessary to arrest him, I will not\n"
            "  hold any person liable for damages should the slave be KILLED."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fifty.dollars" not in full_text

    def test_wrap_019_for_many(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: for.many
        passage = (
            "“Billy is 25 years old, and is known as the patroon of my boat for\n"
            "  many years; in all probability he may resist; in that event 50\n"
            "  dollars will be paid for his HEAD.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "for.many" not in full_text

    def test_wrap_020_from_the(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: from.the
        passage = (
            "Very many such examples of fidelity and piety might be added from\n"
            "  the old Virginia families. These will suffice as specimens, and will\n"
            "  serve to show how interesting the relation between master and\n"
            "  servant often is."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "from.the" not in full_text

    def test_wrap_021_this_encouragem(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: this.encouragement
        passage = (
            "Many purposes of convenience and hospitality were subserved by this\n"
            "  encouragement of cultivation in some of the servants, on the part of\n"
            "  the owners."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "this.encouragement" not in full_text

    def test_wrap_022_the_impression(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: the.impression
        passage = (
            "Of course it is not to be supposed that we design to convey the\n"
            "  impression that such instances are numerous, the nature of the\n"
            "  relationship forbidding it; but we do mean emphatically to affirm\n"
            "  that there is far more of kindly and Christian intercourse than many\n"
            "  at a distance are apt to believe. That there is a great and sad want\n"
            "  of Christian instruction, notwithstanding the more recent efforts\n"
            "  put forth to impart it, we most sorrowfully acknowledge."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.impression" not in full_text

    def test_wrap_023_legitimate_tendency(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: legitimate.tendency
        passage = (
            "If I believed, or was of opinion, that it was the legitimate\n"
            "  tendency of the gospel to abolish slavery, how would I approach a\n"
            "  man, possessing as many slaves as Abraham had, and tell him I wished\n"
            "  to obtain his permission to preach to his slaves?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "legitimate.tendency" not in full_text

    def test_wrap_024_its_tendency(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: its.tendency
        passage = (
            "But suppose, when he put the last question to me, as to its\n"
            "  tendency, I could and would, without a twist or quibble, tell\n"
            "  him, plainly and candidly, that it was a slander on the gospel\n"
            "  to say that emancipation or abolition was its legitimate tendency. I\n"
            "  would tell him that the commandments of some men, and not the\n"
            "  commandments of God, made slavery a sin.—Smylie on Slavery, p. 71."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "its.tendency" not in full_text

    def test_wrap_025_the_environs(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: the.environs
        passage = (
            "“Also that, a few years since, he was at a brick-yard in the\n"
            "  environs of New Orleans, in which one hundred hands were employed;\n"
            "  among them were from twenty to thirty young women, in the prime of\n"
            "  life. He was told by the proprietor that there had _not been a child\n"
            "  born among them for the last two or three years, although they all\n"
            "  had husbands_.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.environs" not in full_text

    def test_wrap_026_resided_some(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: resided.some
        passage = (
            "The following testimony of Rev. Dr. Channing, of Boston, who resided\n"
            "  some time in Virginia, shows that the over-working of slaves, to\n"
            "  such an extent as to abridge life, and cause a decrease of\n"
            "  population, is not confined to the far South and South-west."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "resided.some" not in full_text

    def test_wrap_027_estate_decreased(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: estate.decreased
        passage = (
            "“I then found that the slaves on this well-managed estate\n"
            "  decreased in number. I asked the cause. He replied, with perfect\n"
            "  frankness and ease, ‘The gang is not large enough for the estate.’\n"
            "  In other words, they were not equal to the work of the plantation,\n"
            "  and yet were made to do it, though with the certainty of abridging\n"
            "  life."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "estate.decreased" not in full_text

    def test_wrap_028_the_system(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: the.system
        passage = (
            "And, indeed, once for all, I will here say that the wastes of the\n"
            "  system are so great, as well as the fluctuation in prices of the\n"
            "  staple articles for market, that it is difficult, nay, impossible,\n"
            "  to indulge in large expenditures on plantations, and make them\n"
            "  savingly profitable.—Religious Instruction, p. 116."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.system" not in full_text

    def test_wrap_029_fussin_with(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: fussin.with
        passage = (
            "“I used to, when I first begun, have considerable trouble fussin’\n"
            "  with ‘em, and trying to make ‘em hold out,—doctorin’ on ‘em up when\n"
            "  they’s sick, and givin’ on ‘em clothes, and blankets, and what not,\n"
            "  trying to keep ‘em all sort o’ decent and comfortable. Law, ‘twant\n"
            "  no sort o’ use; I lost money on ‘em, and ‘twas heaps o’ trouble.\n"
            "  Now, you see, I just put ‘em straight through, sick or well. When\n"
            "  one nigger’s dead, I buy another; and I find it comes cheaper and\n"
            "  easier every way.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fussin.with" not in full_text

    def test_wrap_030_labor_till(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: labor.till
        passage = (
            "When the grinding has once commenced, there is no cessation of labor\n"
            "  till it is completed. From beginning to end a busy and cheerful\n"
            "  scene continues. The negroes,"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "labor.till" not in full_text

    def test_wrap_031_holidays_when(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: holidays.when
        passage = (
            "After the grinding is finished, the negroes have several holidays,\n"
            "  when they are quite at liberty to dance and frolic as much as they\n"
            "  please; and the cane-song—which is improvised by one of the gang,\n"
            "  the rest all joining in a prolonged and unintelligible chorus—now\n"
            "  breaks, night and day, upon the ear, in notes “most musical, most\n"
            "  melancholy.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "holidays.when" not in full_text

    def test_wrap_032_months_they(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: months.they
        passage = (
            "“At the rolling of sugars, an interval of from two to three months,\n"
            "  they (the slaves in Louisiana) work both night and day. Abridged\n"
            "  of their sleep, they scarcely retire to rest during the whole\n"
            "  period.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "months.they" not in full_text

    def test_wrap_033_the_amount(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: the.amount
        passage = (
            "We find in many of our southern and western exchanges notices of the\n"
            "  amount of cotton picked by hands, and the quantity by each hand;\n"
            "  and, as we have received a similar account, which we have not seen\n"
            "  excelled, so far as regards the quantity picked by one hand, we with\n"
            "  pleasure furnish the statement, with the remark that it is from a\n"
            "  citizen of this district, overseeing for Maj. H. W. Parr."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.amount" not in full_text

    def test_wrap_034_the_lowest(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: the.lowest
        passage = (
            "“The highest, three hundred and fifty pounds, by several; the\n"
            "  lowest, one hundred and fifteen pounds. One of the number has picked\n"
            "  in the last seven and a half days (Sunday excepted), eleven hours\n"
            "  each day, nineteen hundred pounds clean cotton. When any of my\n"
            "  agricultural friends beat this, in the same time, and during\n"
            "  sunshine, I will try again."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.lowest" not in full_text

    def test_wrap_035_church_rochester(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: church.rochester
        passage = (
            "Mr. George A. Avery, elder of the 4th Presbyterian Church,\n"
            "  Rochester, N. Y., who lived four years in Virginia.—“Amongst all the\n"
            "  negro cabins which I saw in Virginia, I cannot call to mind one in\n"
            "  which there was any other floor than the earth; anything that a\n"
            "  Northern laborer, or mechanic, white or colored, would call a bed,\n"
            "  nor a solitary partition, to separate the sexes.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "church.rochester" not in full_text

    def test_wrap_036_cachexia_africana(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: cachexia.africana
        passage = (
            "The Western Medical Reformer, in an article on the Cachexia\n"
            "  Africana, by a Kentucky physician, thus speaks of the huts of the\n"
            "  slaves: “They are crowded together in a small hut, and sometimes\n"
            "  having an imperfect and sometimes no floor, and seldom raised from\n"
            "  the ground, ill ventilated, and surrounded with filth.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "cachexia.africana" not in full_text

    def test_wrap_037_maryland_formerly(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: maryland.formerly
        passage = (
            "Mr. Lemuel Sapington, of Lancaster, Pa., a native of Maryland,\n"
            "  formerly a slave-holder.—“The descriptions generally given of negro\n"
            "  quarters are correct; the quarters are _without floors, and not\n"
            "  sufficient to keep off the inclemency of the weather_; they are\n"
            "  uncomfortable both in summer and winter.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "maryland.formerly" not in full_text

    def test_wrap_038_their_miserable(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: their.miserable
        passage = (
            "Rev. John Rankin, a native of Tennessee.—“When they return to their\n"
            "  miserable huts at night, they find not there the means of\n"
            "  comfortable rest; but _on the cold ground they must lie without\n"
            "  covering, and shiver while they slumber_.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "their.miserable" not in full_text

    def test_wrap_039_negro_houses(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: negro.houses
        passage = (
            "Their general mode of living is coarse and vulgar. Many negro\n"
            "  houses are small, low to the ground, blackened with smoke, often\n"
            "  with dirt floors, and the furniture of the plainest kind. On some\n"
            "  estates the houses are framed, weather-boarded, neatly white-washed,\n"
            "  and made sufficiently large and comfortable in every respect. The\n"
            "  improvement in the size, material and finish, of negro houses, is\n"
            "  extending. Occasionally they may be found constructed of tabby or\n"
            "  brick."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "negro.houses" not in full_text

    def test_wrap_040_are_raised(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: are.raised
        passage = (
            "By confining the slaves to the Southern States, where crops are\n"
            "  raised for exportation, and bread and meat are purchased, you _doom\n"
            "  them to scarcity and hunger_. It is proposed to hem in the blacks\n"
            "  where they are ILL FED."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "are.raised" not in full_text

    def test_wrap_041_from_hunger(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: from.hunger
        passage = (
            "On almost every plantation, the hands suffer more or less from\n"
            "  hunger at some seasons of almost every year. There is always a _good\n"
            "  deal of suffering_ from hunger. On many plantations, and\n"
            "  particularly in Louisiana, the slaves are in a condition of _almost\n"
            "  utter famishment_, during a great portion of the year.—Ibid."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "from.hunger" not in full_text

    def test_wrap_042_when_they(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: when.they
        passage = (
            "The slaves down the Mississippi are half-starved. The boats, when\n"
            "  they stop at night, are constantly boarded by slaves, begging for\n"
            "  something to eat."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "when.they" not in full_text

    def test_wrap_043_gentlemanw_related(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: gentlemanwho.related
        passage = (
            "“What can you do with so much tobacco?” said a gentleman,—who\n"
            "  related the circumstance to me,—on hearing a planter, whom he was\n"
            "  visiting, give an order to his teamster to bring two hogsheads of\n"
            "  tobacco out to the estate from the “Landing.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gentlemanwho.related" not in full_text

    def test_wrap_044_highpost_bedsteads(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: highpost.bedsteads
        passage = (
            "“Why are you at the trouble and expense of having high-post\n"
            "  bedsteads for your negroes?” said a gentleman from the North, while\n"
            "  walking through the handsome “quarters,” or village, for the slaves,\n"
            "  then in progress on a plantation near Natchez—addressing the\n"
            "  proprietor."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "highpost.bedsteads" not in full_text

    def test_wrap_045_the_quarters(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: the.quarters
        passage = (
            "A few weeks after, I was at the plantation, and riding past the\n"
            "  quarters one Sabbath morning, beheld Peter, his wife and children,\n"
            "  with his old father, all sunning themselves in the new gallery."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.quarters" not in full_text

    def test_wrap_046_without_touching(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: without.touching
        passage = (
            "“It werry pretty, Missus,” said Jane, eying it at a distance without\n"
            "  touching it, “but me prefer muslin, if you please: muslin de fashion\n"
            "  dis Chrismus.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "without.touching" not in full_text

    def test_wrap_047_this_look(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: this.look
        passage = (
            "My friend, how can you, how dare you, carry on a trade like this?\n"
            "  Look at those poor creatures! Here I am, rejoicing in my heart that\n"
            "  I am going home to my wife and child; and the same bell which is the\n"
            "  signal to carry me onward towards them will part this poor man and\n"
            "  his wife forever. Depend upon it, God will bring you into judgment\n"
            "  for this."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "this.look" not in full_text

    def test_wrap_048_betrayal_there(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: betrayal.there
        passage = (
            "At times I thought it occasioned by the lurking fear of betrayal.\n"
            "  There was no Vigilance Committee at the time,—there were but\n"
            "  anti-slavery men. I came North with my counsels in my own cautious\n"
            "  breast. I married a wife, and did not tell her I was a fugitive.\n"
            "  None of my friends knew it. I knew not the means of safety, and\n"
            "  hence I was constantly in fear of meeting with some one who would\n"
            "  betray me."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "betrayal.there" not in full_text

    def test_wrap_049_still_that(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: still.that
        passage = (
            "It was fully two years before I could hold up my head; but still\n"
            "  that feeling was in my mind. In 1846, after opening my bosom as a\n"
            "  fugitive to John Hooker, Esq., I felt this much relief,—“Thank God\n"
            "  there is one brother-man in hard old Connecticut that knows my\n"
            "  troubles.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "still.that" not in full_text

    def test_wrap_050_nothing_but(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: nothing.but
        passage = (
            "But still there was this drawback. Somebody says, “This is nothing\n"
            "  but a nigger island.” Now, then, my old trouble came back again; “a\n"
            "  nigger among niggers is but a nigger still.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "nothing.but" not in full_text

    def test_wrap_051_and_merryheart(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: and.merryhearted
        passage = (
            "You say again you have never seen a slave how ever careless and\n"
            "  merry-hearted, who had not this sore place, and that did not shrink\n"
            "  or get angry if a finger was laid on it. I see that you have been a\n"
            "  close observer of negro nature."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.merryhearted" not in full_text

    def test_wrap_052_made_him(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: made.him
        passage = (
            "O, Mrs. Stowe, slavery is an awful system! It takes man as God made\n"
            "  him; it demolishes him, and then mis-creates him, or perhaps I\n"
            "  should say mal-creates him!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "made.him" not in full_text

    def test_wrap_053_many_instances(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: many.instances
        passage = (
            "You are right about Topsy: our ragged schools will afford you many\n"
            "  instances of poor children, hardened by kicks, insults and neglect,\n"
            "  moved to tears and docility by the first word of kindness. It opens\n"
            "  new feelings, develops, as it were, a new nature, and brings the\n"
            "  wretched outcast into the family of man."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "many.instances" not in full_text

    def test_wrap_054_from_charles(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: from.charles
        passage = (
            "HARRIET BEECHER STOWE: I have this day received a request from\n"
            "  Charles K. Whipple, of Boston, to furnish thee with a statement,\n"
            "  authentic and circumstantial, of the trouble and losses which have\n"
            "  been brought upon myself and others of my friends from the aid we\n"
            "  had rendered to fugitive slaves, in order, if thought of sufficient\n"
            "  importance, to be published in a work thee is now preparing for the\n"
            "  press."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "from.charles" not in full_text

    def test_wrap_055_and_myself(self):
        # Source: A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which, wrap corruption: and.myself
        passage = (
            "I will now endeavor to give thee a statement of what John Hunn and\n"
            "  myself suffered by aiding a family of slaves, a few years since. I\n"
            "  will give the facts as they occurred, and thee may condense and\n"
            "  publish so much as thee may think useful in thy work, and no more:"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.myself" not in full_text

