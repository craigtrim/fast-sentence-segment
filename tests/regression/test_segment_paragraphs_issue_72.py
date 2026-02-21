# -*- coding: utf-8 -*-
"""
Test Suite: Paragraph-Level Segmentation — Real Ebook Passages (Issue #72)

All inputs are the ACTUAL output of segment_text(text, flatten=False)
run against real Project Gutenberg ebook text.
Each test documents the source book and character range.
"""

import pytest
from fast_sentence_segment import segment_paragraphs

def test_shelley_frankenstein_or_the_modern_prometheus():
    # Source: Shelley - Frankenstein or the Modern Prometheus
    # Chars:  4337–5808
    sentences = [
            ['Six years have passed since I resolved on my present undertaking.',
             'I can, even now, remember the hour from which I dedicated myself to this great enterprise.',
             'I commenced by inuring my body to hardship.',
             'I accompanied the whale-fishers on several expeditions to the North Sea; I voluntarily endured cold, famine, thirst, and want of sleep; I often worked harder than the common sailors during the day and devoted my nights to the study of mathematics, the theory of medicine, and those branches of physical science from which a naval adventurer might derive the greatest practical advantage.',
             'Twice I actually hired myself as an under-mate in a Greenland whaler, and acquitted myself to admiration.',
             'I must own I felt a little proud when my captain offered me the second dignity in the vessel and entreated me to remain with the greatest earnestness, so valuable did he consider my services.'],
            ['And now, dear Margaret, do I not deserve to accomplish some great purpose?',
             'My life might have been passed in ease and luxury, but I preferred glory to every enticement that wealth placed in my path.',
             'Oh, that some encouraging voice would answer in the affirmative!',
             'My courage and my resolution is firm; but my hopes fluctuate, and my spirits are often depressed.',
             'I am about to proceed on a long and difficult voyage, the emergencies of which will demand all my fortitude: I am required not only to raise the spirits of others, but sometimes to sustain my own, when theirs are failing.']
        ]
    expected = [
            'Six years have passed since I resolved on my present undertaking. I can, even now, remember the hour from which I dedicated myself to this great enterprise. I commenced by inuring my body to hardship. I accompanied the whale-fishers on several expeditions to the North Sea; I voluntarily endured cold, famine, thirst, and want of sleep; I often worked harder than the common sailors during the day and devoted my nights to the study of mathematics, the theory of medicine, and those branches of physical science from which a naval adventurer might derive the greatest practical advantage. Twice I actually hired myself as an under-mate in a Greenland whaler, and acquitted myself to admiration. I must own I felt a little proud when my captain offered me the second dignity in the vessel and entreated me to remain with the greatest earnestness, so valuable did he consider my services.',
            'And now, dear Margaret, do I not deserve to accomplish some great purpose? My life might have been passed in ease and luxury, but I preferred glory to every enticement that wealth placed in my path. Oh, that some encouraging voice would answer in the affirmative! My courage and my resolution is firm; but my hopes fluctuate, and my spirits are often depressed. I am about to proceed on a long and difficult voyage, the emergencies of which will demand all my fortitude: I am required not only to raise the spirits of others, but sometimes to sustain my own, when theirs are failing.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_hardy_tess_of_the_durbervilles_a_pure_woman():
    # Source: Hardy - Tess of the Durbervilles a Pure Woman
    # Chars:  5143–6570
    sentences = [
            ['In the introductory words to the first edition I suggested the possible advent of the genteel person who would not be able to endure something or other in these pages.',
             'That person duly appeared among the aforesaid objectors. In one case he felt upset that it was not possible for him to read the book through three times, owing to my not having made that critical effort which "alone can prove the salvation of such an one."',
             'In another, he objected to such vulgar articles as the Devil\'s pitchfork, a lodging-house carving-knife, and a shame-bought parasol, appearing in a respectable story. In another place he was a gentleman who turned Christian for half-an-hour the better to express his grief that a disrespectful phrase about the Immortals should have been used; though the same innate gentility compelled him to excuse the author in words of pity that one cannot be too thankful for: "He does but give us of his best."',
             'I can assure this great critic that to exclaim illogically against the gods, singular or plural, is not such an original sin of mine as he seems to imagine.',
             'True, it may have some local originality; though if Shakespeare were an authority on history, which perhaps he is not, I could show that the sin was introduced into Wessex as early as the Heptarchy itself.',
             "Says Glo'ster in Lear, otherwise Ina, king of that country:"],
            ['As flies to wanton boys are we to the gods;.They kill us for their sport.']
        ]
    expected = [
            'In the introductory words to the first edition I suggested the possible advent of the genteel person who would not be able to endure something or other in these pages. That person duly appeared among the aforesaid objectors. In one case he felt upset that it was not possible for him to read the book through three times, owing to my not having made that critical effort which "alone can prove the salvation of such an one." In another, he objected to such vulgar articles as the Devil\'s pitchfork, a lodging-house carving-knife, and a shame-bought parasol, appearing in a respectable story. In another place he was a gentleman who turned Christian for half-an-hour the better to express his grief that a disrespectful phrase about the Immortals should have been used; though the same innate gentility compelled him to excuse the author in words of pity that one cannot be too thankful for: "He does but give us of his best." I can assure this great critic that to exclaim illogically against the gods, singular or plural, is not such an original sin of mine as he seems to imagine. True, it may have some local originality; though if Shakespeare were an authority on history, which perhaps he is not, I could show that the sin was introduced into Wessex as early as the Heptarchy itself. Says Glo\'ster in Lear, otherwise Ina, king of that country:',
            'As flies to wanton boys are we to the gods;.They kill us for their sport.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_hardy_the_mayor_of_casterbridge():
    # Source: Hardy - The Mayor of Casterbridge
    # Chars:  5602–6028
    sentences = [
            ['The pessimist still maintained a negative.',
             '"Pulling down is more the nater of Weydon.',
             'There were five houses cleared away last year, and three this; and the volk nowhere to go—no, not so much as a thatched hurdle; that\'s the way o\' Weydon-Priors."'],
            ['The hay-trusser, which he obviously was, nodded with some superciliousness.',
             'Looking towards the village, he continued, "There is something going on here, however, is there not?"']
        ]
    expected = [
            'The pessimist still maintained a negative. "Pulling down is more the nater of Weydon. There were five houses cleared away last year, and three this; and the volk nowhere to go—no, not so much as a thatched hurdle; that\'s the way o\' Weydon-Priors."',
            'The hay-trusser, which he obviously was, nodded with some superciliousness. Looking towards the village, he continued, "There is something going on here, however, is there not?"'
        ]
    assert segment_paragraphs(sentences) == expected

def test_hardy_the_return_of_the_native():
    # Source: Hardy - The Return of the Native
    # Chars:  4401–5738
    sentences = [
            ['The most thoroughgoing ascetic could feel that he had a natural right to wander on Egdon—he was keeping within the line of legitimate indulgence when he laid himself open to influences such as these.',
             'Colours and beauties so far subdued were, at least, the birthright of all.',
             'Only in summer days of highest feather did its mood touch the level of gaiety.',
             'Intensity was more usually reached by way of the solemn than by way of the brilliant, and such a sort of intensity was often arrived at during winter darkness, tempests, and mists.',
             'Then Egdon was aroused to reciprocity; for the storm was its lover, and the wind its friend.',
             'Then it became the home of strange phantoms; and it was found to be the hitherto unrecognized original of those wild regions of obscurity which are vaguely felt to be compassing us about in midnight dreams of flight and disaster, and are never thought of after the dream till revived by scenes like this.'],
            ["It was at present a place perfectly accordant with man's nature—neither ghastly, hateful, nor ugly; neither commonplace, unmeaning, nor tame; but, like man, slighted and enduring; and withal singularly colossal and mysterious in its swarthy monotony.",
             'As with some persons who have long lived apart, solitude seemed to look out of its countenance.',
             'It had a lonely face, suggesting tragical possibilities.']
        ]
    expected = [
            'The most thoroughgoing ascetic could feel that he had a natural right to wander on Egdon—he was keeping within the line of legitimate indulgence when he laid himself open to influences such as these. Colours and beauties so far subdued were, at least, the birthright of all. Only in summer days of highest feather did its mood touch the level of gaiety. Intensity was more usually reached by way of the solemn than by way of the brilliant, and such a sort of intensity was often arrived at during winter darkness, tempests, and mists. Then Egdon was aroused to reciprocity; for the storm was its lover, and the wind its friend. Then it became the home of strange phantoms; and it was found to be the hitherto unrecognized original of those wild regions of obscurity which are vaguely felt to be compassing us about in midnight dreams of flight and disaster, and are never thought of after the dream till revived by scenes like this.',
            "It was at present a place perfectly accordant with man's nature—neither ghastly, hateful, nor ugly; neither commonplace, unmeaning, nor tame; but, like man, slighted and enduring; and withal singularly colossal and mysterious in its swarthy monotony. As with some persons who have long lived apart, solitude seemed to look out of its countenance. It had a lonely face, suggesting tragical possibilities."
        ]
    assert segment_paragraphs(sentences) == expected

def test_stevenson_treasure_island():
    # Source: Stevenson - Treasure Island
    # Chars:  7781–9464
    sentences = [
            ['How that personage haunted my dreams, I need scarcely tell you.',
             'On stormy nights, when the wind shook the four corners of the house and the surf roared along the cove and up the cliffs, I would see him in a thousand forms, and with a thousand diabolical expressions.',
             'Now the leg would be cut off at the knee, now at the hip; now he was a monstrous kind of a creature who had never had but the one leg, and that in the middle of his body.',
             'To see him leap and run and pursue me over hedge and ditch was the worst of nightmares.',
             'And altogether I paid pretty dear for my monthly fourpenny piece, in the shape of these abominable fancies.'],
            ['But though I was so terrified by the idea of the seafaring man with one leg, I was far less afraid of the captain himself than anybody else who knew him.',
             'There were nights when he took a deal more rum and water than his head would carry; and then he would sometimes sit and sing his wicked, old, wild sea-songs, minding nobody; but sometimes he would call for glasses round and force all the trembling company to listen to his stories or bear a chorus to his singing.',
             'Often I have heard the house shaking with "Yo-ho-ho, and a bottle of rum," all the neighbours joining in for dear life, with the fear of death upon them, and each singing louder than the other to avoid remark.',
             'For in these fits he was the most overriding companion ever known; he would slap his hand on the table for silence all round; he would fly up in a passion of anger at a question, or sometimes because none was put, and so he judged the company was not following his story.',
             'Nor would he allow anyone to leave the inn till he had drunk himself sleepy and reeled off to bed.']
        ]
    expected = [
            'How that personage haunted my dreams, I need scarcely tell you. On stormy nights, when the wind shook the four corners of the house and the surf roared along the cove and up the cliffs, I would see him in a thousand forms, and with a thousand diabolical expressions. Now the leg would be cut off at the knee, now at the hip; now he was a monstrous kind of a creature who had never had but the one leg, and that in the middle of his body. To see him leap and run and pursue me over hedge and ditch was the worst of nightmares. And altogether I paid pretty dear for my monthly fourpenny piece, in the shape of these abominable fancies.',
            'But though I was so terrified by the idea of the seafaring man with one leg, I was far less afraid of the captain himself than anybody else who knew him. There were nights when he took a deal more rum and water than his head would carry; and then he would sometimes sit and sing his wicked, old, wild sea-songs, minding nobody; but sometimes he would call for glasses round and force all the trembling company to listen to his stories or bear a chorus to his singing. Often I have heard the house shaking with "Yo-ho-ho, and a bottle of rum," all the neighbours joining in for dear life, with the fear of death upon them, and each singing louder than the other to avoid remark. For in these fits he was the most overriding companion ever known; he would slap his hand on the table for silence all round; he would fly up in a passion of anger at a question, or sometimes because none was put, and so he judged the company was not following his story. Nor would he allow anyone to leave the inn till he had drunk himself sleepy and reeled off to bed.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_wilde_a_critic_in_pall_mall_being_extracts_from_reviews_and_():
    # Source: Wilde - A Critic in Pall Mall Being Extracts From Reviews and Miscellanies
    # Chars:  4244–4835
    sentences = [
            ['Yet though we cannot care much for the dead man who lies in lonely state beneath it, and who is only known to the world through his sepulchre, still this pyramid will be ever dear to the eyes of all English-speaking people, because at evening its shadows fall on the tomb of one who walks with Spenser, and Shakespeare, and Byron, and Shelley, and Elizabeth Barrett Browning in the great procession of the sweet singers of England.'],
            ['For at its foot there is a green sunny slope, known as the Old Protestant Cemetery, and on this a common-looking grave, which bears the following inscription:']
        ]
    expected = [
            'Yet though we cannot care much for the dead man who lies in lonely state beneath it, and who is only known to the world through his sepulchre, still this pyramid will be ever dear to the eyes of all English-speaking people, because at evening its shadows fall on the tomb of one who walks with Spenser, and Shakespeare, and Byron, and Shelley, and Elizabeth Barrett Browning in the great procession of the sweet singers of England.',
            'For at its foot there is a green sunny slope, known as the Old Protestant Cemetery, and on this a common-looking grave, which bears the following inscription:'
        ]
    assert segment_paragraphs(sentences) == expected

def test_gissing_a_lifes_morning():
    # Source: Gissing - A Lifes Morning
    # Chars:  11913–12461
    sentences = [
            ['Mr. Athel, having pronounced a grace, mentioned that he thought of running up to town; did anybody wish to give him a commission?',
             'Mrs. Rossall looked thoughtful, and said she would make a note of two or three things.'],
            ["'I haven't much faith in that porridge regimen, Wilf,' remarked the master of the house, as he helped himself to chicken and tongue.",
             "'We are not Highlanders.",
             "It's dangerous to make diet too much a matter of theory.",
             'Your example is infectious; first the twins; now Miss Hood.',
             "Edith, do you propose to become a pervert to porridge?'"]
        ]
    expected = [
            'Mr. Athel, having pronounced a grace, mentioned that he thought of running up to town; did anybody wish to give him a commission? Mrs. Rossall looked thoughtful, and said she would make a note of two or three things.',
            "'I haven't much faith in that porridge regimen, Wilf,' remarked the master of the house, as he helped himself to chicken and tongue. 'We are not Highlanders. It's dangerous to make diet too much a matter of theory. Your example is infectious; first the twins; now Miss Hood. Edith, do you propose to become a pervert to porridge?'"
        ]
    assert segment_paragraphs(sentences) == expected

def test_bierce_a_cynic_looks_at_life():
    # Source: Bierce - A Cynic Looks at Life
    # Chars:  4473–5861
    sentences = [
            ['The cant of civilization fatigues.',
             'Civilization, is a fine and beautiful structure.',
             'It is as picturesque as a Gothic cathedral, but it is built upon the bones and cemented with the blood of those whose part in all its pomp is that and nothing more.',
             'It cannot be reared in the ungenerous tropics, for there the people will not contribute their blood and bones.',
             'The proposition that the average American workingman or European peasant is "better off" than the South Sea islander, lolling under a palm and drunk with over-eating, will not bear a moment\'s examination.',
             'It is we scholars and gentlemen that are better off.'],
            ['It is admitted that the South Sea islander in a state of nature is overmuch addicted to the practice of eating human flesh; but concerning that I submit: first, that he likes it; second, that those who supply it are mostly dead.',
             'It is upon his enemies that he feeds, and these he would kill anyhow, as we do ours. In civilized, enlightened and Christian countries, where cannibalism has not yet established itself, wars are as frequent and destructive as among the maneaters.',
             'The untitled savage knows at least why he goes killing, whereas our private soldier is commonly in black ignorance of the apparent cause of quarrel--of the actual cause, always.',
             'Their shares in the fruits of victory are about equal, for the chief takes all the dead, the general all the glory.']
        ]
    expected = [
            'The cant of civilization fatigues. Civilization, is a fine and beautiful structure. It is as picturesque as a Gothic cathedral, but it is built upon the bones and cemented with the blood of those whose part in all its pomp is that and nothing more. It cannot be reared in the ungenerous tropics, for there the people will not contribute their blood and bones. The proposition that the average American workingman or European peasant is "better off" than the South Sea islander, lolling under a palm and drunk with over-eating, will not bear a moment\'s examination. It is we scholars and gentlemen that are better off.',
            'It is admitted that the South Sea islander in a state of nature is overmuch addicted to the practice of eating human flesh; but concerning that I submit: first, that he likes it; second, that those who supply it are mostly dead. It is upon his enemies that he feeds, and these he would kill anyhow, as we do ours. In civilized, enlightened and Christian countries, where cannibalism has not yet established itself, wars are as frequent and destructive as among the maneaters. The untitled savage knows at least why he goes killing, whereas our private soldier is commonly in black ignorance of the apparent cause of quarrel--of the actual cause, always. Their shares in the fruits of victory are about equal, for the chief takes all the dead, the general all the glory.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_hope_a_change_of_air():
    # Source: Hope - A Change of Air
    # Chars:  4139–4439
    sentences = [
            ["At first Arthur Angell said he would not go near a villa; he could not breath in a villa; or sleep quiet o' nights in a villa; but presently he relented."],
            ['"I can\'t stand it for long, though," he said.',
             '"Still, I\'m glad you\'re going to have Nellie there.',
             "She'd have missed you awfully.",
             'When do you go?"']
        ]
    expected = [
            "At first Arthur Angell said he would not go near a villa; he could not breath in a villa; or sleep quiet o' nights in a villa; but presently he relented.",
            '"I can\'t stand it for long, though," he said. "Still, I\'m glad you\'re going to have Nellie there. She\'d have missed you awfully. When do you go?"'
        ]
    assert segment_paragraphs(sentences) == expected

def test_bennett_a_great_man_a_frolic():
    # Source: Bennett - A Great Man a Frolic
    # Chars:  4072–4270
    sentences = [
            ["'No, sir.",
             "He was called away half an hour ago or hardly, and may be out till very late.'"],
            ["'Called away!' exclaimed Mr. Knight.",
             'He was astounded, shocked, pained.',
             "'But I warned him three months ago!'"]
        ]
    expected = [
            "'No, sir. He was called away half an hour ago or hardly, and may be out till very late.'",
            "'Called away!' exclaimed Mr. Knight. He was astounded, shocked, pained. 'But I warned him three months ago!'"
        ]
    assert segment_paragraphs(sentences) == expected

def test_baum_a_kidnapped_santa_claus():
    # Source: Baum - A Kidnapped Santa Claus
    # Chars:  4000–4345
    sentences = [
            ['So the very next day, while Santa Claus was busily at work, surrounded by his little band of assistants, the Daemon of Selfishness came to him and said:'],
            ['"These toys are wonderfully bright and pretty.',
             'Why do you not keep them for yourself?',
             'It\'s a pity to give them to those noisy boys and fretful girls, who break and destroy them so quickly."']
        ]
    expected = [
            'So the very next day, while Santa Claus was busily at work, surrounded by his little band of assistants, the Daemon of Selfishness came to him and said:',
            '"These toys are wonderfully bright and pretty. Why do you not keep them for yourself? It\'s a pity to give them to those noisy boys and fretful girls, who break and destroy them so quickly."'
        ]
    assert segment_paragraphs(sentences) == expected

def test_jacobs_a_golden_venture_the_lady_of_the_barge_and_others_par():
    # Source: Jacobs - A Golden Venture the Lady of the Barge and Others Part 11
    # Chars:  4036–4353
    sentences = [
            ['"Ten hundered pounds twice over," said the carpenter, mouthing it slowly; "twenty hundered pounds."'],
            ['He got up from the table, and instinctively realizing that he could not do full justice to his feelings with the baby in his arms, laid it on the teatray in a puddle of cold tea and stood looking hard at the heiress.']
        ]
    expected = [
            '"Ten hundered pounds twice over," said the carpenter, mouthing it slowly; "twenty hundered pounds."',
            'He got up from the table, and instinctively realizing that he could not do full justice to his feelings with the baby in his arms, laid it on the teatray in a puddle of cold tea and stood looking hard at the heiress.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_tarkington_alice_adams():
    # Source: Tarkington - Alice Adams
    # Chars:  4699–6163
    sentences = [
            ['Night sounds were becoming day sounds; the far-away hooting of freight-engines seemed brisker than an hour ago in the dark.',
             "A cheerful whistler passed the house, even more careless of sleepers than the milkman's horse had been; then a group of coloured workmen came by, and although it was impossible to be sure whether they were homeward bound from night-work or on their way to day-work, at least it was certain that they were jocose.",
             'Loose, aboriginal laughter preceded them afar, and beat on the air long after they had gone by.'],
            ['The sick-room night-light, shielded from his eyes by a newspaper propped against a water-pitcher, still showed a thin glimmering that had grown offensive to Adams. In his wandering and enfeebled thoughts, which were much more often imaginings than reasonings, the attempt of the night-light to resist the dawn reminded him of something unpleasant, though he could not discover just what the unpleasant thing was.',
             'Here was a puzzle that irritated him the more because he could not solve it, yet always seemed just on the point of a solution.',
             'However, he may have lost nothing cheerful by remaining in the dark upon the matter; for if he had been a little sharper in this introspection he might have concluded that the squalor of the night-light, in its seeming effort to show against the forerunning of the sun itself, had stimulated some half-buried perception within him to sketch the painful little synopsis of an autobiography.']
        ]
    expected = [
            "Night sounds were becoming day sounds; the far-away hooting of freight-engines seemed brisker than an hour ago in the dark. A cheerful whistler passed the house, even more careless of sleepers than the milkman's horse had been; then a group of coloured workmen came by, and although it was impossible to be sure whether they were homeward bound from night-work or on their way to day-work, at least it was certain that they were jocose. Loose, aboriginal laughter preceded them afar, and beat on the air long after they had gone by.",
            'The sick-room night-light, shielded from his eyes by a newspaper propped against a water-pitcher, still showed a thin glimmering that had grown offensive to Adams. In his wandering and enfeebled thoughts, which were much more often imaginings than reasonings, the attempt of the night-light to resist the dawn reminded him of something unpleasant, though he could not discover just what the unpleasant thing was. Here was a puzzle that irritated him the more because he could not solve it, yet always seemed just on the point of a solution. However, he may have lost nothing cheerful by remaining in the dark upon the matter; for if he had been a little sharper in this introspection he might have concluded that the squalor of the night-light, in its seeming effort to show against the forerunning of the sun itself, had stimulated some half-buried perception within him to sketch the painful little synopsis of an autobiography.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_dreiser_a_book_about_myself():
    # Source: Dreiser - A Book About Myself
    # Chars:  7369–7718
    sentences = [
            ['Imagine then my intense delight one day, when, scanning the "Help Wanted: Male" columns of the Chicago Herald, I encountered an advertisement which ran (in substance):'],
            ['Wanted: A number of bright young men to assist in the business.department during the Christmas holidays.',
             'Promotion possible.',
             'Apply to Business Manager between 9 and 10 a.m.']
        ]
    expected = [
            'Imagine then my intense delight one day, when, scanning the "Help Wanted: Male" columns of the Chicago Herald, I encountered an advertisement which ran (in substance):',
            'Wanted: A number of bright young men to assist in the business.department during the Christmas holidays. Promotion possible. Apply to Business Manager between 9 and 10 a.m.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_lawrence_aarons_rod():
    # Source: Lawrence - Aarons Rod
    # Chars:  4465–4850
    sentences = [
            ['The two children ran indoors, the man stood contemplative in the cold, shrugging his uncovered shoulders slightly.',
             'The open inner door showed a bright linoleum on the floor, and the end of a brown side-board on which stood an aspidistra.'],
            ['Again with a wrench Aaron Sisson lifted the box.',
             'The tree pricked and stung.',
             'His wife watched him as he entered staggering, with his face averted.']
        ]
    expected = [
            'The two children ran indoors, the man stood contemplative in the cold, shrugging his uncovered shoulders slightly. The open inner door showed a bright linoleum on the floor, and the end of a brown side-board on which stood an aspidistra.',
            'Again with a wrench Aaron Sisson lifted the box. The tree pricked and stung. His wife watched him as he entered staggering, with his face averted.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_huxley_antic_hay():
    # Source: Huxley - Antic Hay
    # Chars:  9788–10188
    sentences = [
            ['The moment had now come for the Hymn.',
             'This being the first Sunday of the Summer term, they sang that special hymn, written by the Headmaster, with music by Dr. Jolly, on purpose to be sung on the first Sundays of terms.',
             'The organ quietly sketched out the tune.',
             'Simple it was, uplifting and manly.'],
            ['One, two, three, four; one, two THREE—4. One, two-and three-and four-and; One, two THREE—4.']
        ]
    expected = [
            'The moment had now come for the Hymn. This being the first Sunday of the Summer term, they sang that special hymn, written by the Headmaster, with music by Dr. Jolly, on purpose to be sung on the first Sundays of terms. The organ quietly sketched out the tune. Simple it was, uplifting and manly.',
            'One, two, three, four; one, two THREE—4. One, two-and three-and four-and; One, two THREE—4.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_thackeray_a_history_of_pendennis_volume_1_his_fortunes_and_m():
    # Source: Thackeray - A History of Pendennis Volume 1 His Fortunes and Misfortunes His Friends and His
    # Chars:  4029–4838
    sentences = [
            ['These perused, the major took out his pocket-book to see on what days he was disengaged, and which of these many hospitable calls he could afford to accept or decline.'],
            ['He threw over Cutler, the East India Director, in Baker-street, in order to dine with Lord Steyne and the little French party at the Star and Garter--the bishop he accepted, because, though the dinner was slow he liked to dine with bishops--and so went through his list and disposed of them according to his fancy or interest.',
             "Then he took his breakfast and looked over the paper, the gazette, the births and deaths, and the fashionable intelligence, to see that his name was down among the guests at my Lord So-and-so's fete, and in the intervals of these occupations carried on cheerful conversation with his acquaintances about the room."]
        ]
    expected = [
            'These perused, the major took out his pocket-book to see on what days he was disengaged, and which of these many hospitable calls he could afford to accept or decline.',
            "He threw over Cutler, the East India Director, in Baker-street, in order to dine with Lord Steyne and the little French party at the Star and Garter--the bishop he accepted, because, though the dinner was slow he liked to dine with bishops--and so went through his list and disposed of them according to his fancy or interest. Then he took his breakfast and looked over the paper, the gazette, the births and deaths, and the fashionable intelligence, to see that his name was down among the guests at my Lord So-and-so's fete, and in the intervals of these occupations carried on cheerful conversation with his acquaintances about the room."
        ]
    assert segment_paragraphs(sentences) == expected

def test_trollope_a_ride_across_palestine():
    # Source: Trollope - A Ride Across Palestine
    # Chars:  20803–21818
    sentences = [
            ['Remounting our horses we rode slowly up the winding ascent of the Mount of Olives, turning round at the brow of the hill to look back over Jerusalem.',
             'Sometimes I think that of all spots in the world this one should be the spot most cherished in the memory of Christians.',
             'It was there that He stood when He wept over the city.',
             'So much we do know, though we are ignorant, and ever shall be so, of the site of His cross and of the tomb.',
             'And then we descended on the eastern side of the hill, passing through Bethany, the town of Lazarus and his sisters, and turned our faces steadily towards the mountains of Moab.'],
            ['Hitherto we had met no Bedouins, and I interrogated my dragoman about them more than once; but he always told me that it did not signify; we should meet them, he said, before any danger could arise.',
             '"As for danger," said I, "I think more of this than I do of the Arabs," and I put my hand on my revolver.',
             '"But as they agreed to be here, here they ought to be.',
             'Don\'t you carry a revolver, Smith?"']
        ]
    expected = [
            'Remounting our horses we rode slowly up the winding ascent of the Mount of Olives, turning round at the brow of the hill to look back over Jerusalem. Sometimes I think that of all spots in the world this one should be the spot most cherished in the memory of Christians. It was there that He stood when He wept over the city. So much we do know, though we are ignorant, and ever shall be so, of the site of His cross and of the tomb. And then we descended on the eastern side of the hill, passing through Bethany, the town of Lazarus and his sisters, and turned our faces steadily towards the mountains of Moab.',
            'Hitherto we had met no Bedouins, and I interrogated my dragoman about them more than once; but he always told me that it did not signify; we should meet them, he said, before any danger could arise. "As for danger," said I, "I think more of this than I do of the Arabs," and I put my hand on my revolver. "But as they agreed to be here, here they ought to be. Don\'t you carry a revolver, Smith?"'
        ]
    assert segment_paragraphs(sentences) == expected

def test_collins_a_fair_penitent():
    # Source: Collins - A Fair Penitent
    # Chars:  5780–6261
    sentences = [
            ['The mass over, I send home the footman and the orphan, remaining behind myself, plunged in inconceivable perplexity.',
             'At last I rouse myself on a sudden; I go to the sacristy; I demand a mass for my own proper advantage every day; I determine to attend it regularly; and, after three hours of agitation, I return home, resolved to enter on the path that leads to justification.'],
            ['Six months passed.',
             'Every morning I went to my mass: every evening I spent in my customary dissipations.']
        ]
    expected = [
            'The mass over, I send home the footman and the orphan, remaining behind myself, plunged in inconceivable perplexity. At last I rouse myself on a sudden; I go to the sacristy; I demand a mass for my own proper advantage every day; I determine to attend it regularly; and, after three hours of agitation, I return home, resolved to enter on the path that leads to justification.',
            'Six months passed. Every morning I went to my mass: every evening I spent in my customary dissipations.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_moore_esther_waters():
    # Source: Moore - Esther Waters
    # Chars:  5305–6618
    sentences = [
            ['On both sides of the straight road there were tall hedges, and the nursemaids lay in the wide shadows on the rich summer grass, their perambulators at a little distance.',
             'The hum of the town died out of the ear, and the girl continued to imagine the future she was about to enter on with increasing distinctness.',
             'Looking across the fields she could see two houses, one in grey stone, the other in red brick with a gable covered with ivy; and between them, lost in the north, the spire of a church.',
             'On questioning a passer-by she learnt that the first house was the Rectory, the second was Woodview Lodge.',
             'If that was the lodge, what must the house be?'],
            ['Two hundred yards further on the road branched, passing on either side of a triangular clump of trees, entering the sea road; and under the leaves the air was green and pleasant, and the lungs of the jaded town girl drew in a deep breath of health.',
             'Behind the plantation she found a large white-painted wooden gate.',
             'It opened into a handsome avenue, and the gatekeeper told her to keep straight on, and to turn to the left when she got to the top.',
             'She had never seen anything like it before, and stopped to admire the uncouth arms of elms, like rafters above the roadway; pink clouds showed through, and the monotonous dove seemed the very heart of the silence.']
        ]
    expected = [
            'On both sides of the straight road there were tall hedges, and the nursemaids lay in the wide shadows on the rich summer grass, their perambulators at a little distance. The hum of the town died out of the ear, and the girl continued to imagine the future she was about to enter on with increasing distinctness. Looking across the fields she could see two houses, one in grey stone, the other in red brick with a gable covered with ivy; and between them, lost in the north, the spire of a church. On questioning a passer-by she learnt that the first house was the Rectory, the second was Woodview Lodge. If that was the lodge, what must the house be?',
            'Two hundred yards further on the road branched, passing on either side of a triangular clump of trees, entering the sea road; and under the leaves the air was green and pleasant, and the lungs of the jaded town girl drew in a deep breath of health. Behind the plantation she found a large white-painted wooden gate. It opened into a handsome avenue, and the gatekeeper told her to keep straight on, and to turn to the left when she got to the top. She had never seen anything like it before, and stopped to admire the uncouth arms of elms, like rafters above the roadway; pink clouds showed through, and the monotonous dove seemed the very heart of the silence.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_moore_confessions_of_a_young_man():
    # Source: Moore - Confessions of a Young Man
    # Chars:  5204–5318
    sentences = [
            ['With sincere wishes for the future success of your most entertaining.',
             'pen.--Very sincerely yours,'],
            ['Walter Pater.']
        ]
    expected = [
            'With sincere wishes for the future success of your most entertaining. pen.--Very sincerely yours,',
            'Walter Pater.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_carroll_a_tangled_tale():
    # Source: Carroll - A Tangled Tale
    # Chars:  4282–4538
    sentences = [
            ['Problem.--"A Square has 20 doors on each side, which contains 21 equal parts.',
             'They are numbered all round, beginning at one corner.',
             'From which of the four, Nos. 9, 25, 52, 73, is the sum of the distances, to the other three, least?"'],
            ['Answer.--"From No. 9."']
        ]
    expected = [
            'Problem.--"A Square has 20 doors on each side, which contains 21 equal parts. They are numbered all round, beginning at one corner. From which of the four, Nos. 9, 25, 52, 73, is the sum of the distances, to the other three, least?"',
            'Answer.--"From No. 9."'
        ]
    assert segment_paragraphs(sentences) == expected

def test_henty_a_chapter_of_adventures():
    # Source: Henty - A Chapter of Adventures
    # Chars:  4434–4724
    sentences = [
            ['"All right, mother!',
             "It's been a fine night, with just enough wind, and not too much.",
             'I ought to have been in half an hour ago, but tide is late this morning."'],
            ['"Lily brought word, just as she was starting for school, that the boats were coming up the creek, so your breakfast is all ready."']
        ]
    expected = [
            '"All right, mother! It\'s been a fine night, with just enough wind, and not too much. I ought to have been in half an hour ago, but tide is late this morning."',
            '"Lily brought word, just as she was starting for school, that the boats were coming up the creek, so your breakfast is all ready."'
        ]
    assert segment_paragraphs(sentences) == expected

def test_harte_a_drift_from_redwood_camp():
    # Source: Harte - A Drift From Redwood Camp
    # Chars:  23472–24154
    sentences = [
            ['That these improvements and changes were due to the influence of one man was undoubtedly true, but that he was necessarily a superior man did not follow.',
             "Elijah's success was due partly to the fact that he had been enabled to impress certain negative virtues, which were part of his own nature, upon a community equally constituted to receive them.",
             'Each was strengthened by the recognition in each other of the unexpected value of those qualities; each acquired a confidence begotten of their success.',
             '"He-hides-his-face," as Elijah Martin was known to the tribe after the episode of the released captives, was really not so much of an autocrat as many constitutional rulers.'],
            ['*',
             '*',
             '*',
             '*',
             '*']
        ]
    expected = [
            'That these improvements and changes were due to the influence of one man was undoubtedly true, but that he was necessarily a superior man did not follow. Elijah\'s success was due partly to the fact that he had been enabled to impress certain negative virtues, which were part of his own nature, upon a community equally constituted to receive them. Each was strengthened by the recognition in each other of the unexpected value of those qualities; each acquired a confidence begotten of their success. "He-hides-his-face," as Elijah Martin was known to the tribe after the episode of the released captives, was really not so much of an autocrat as many constitutional rulers.',
            '* * * * *'
        ]
    assert segment_paragraphs(sentences) == expected

def test_hichens_a_spirit_in_prison():
    # Source: Hichens - A Spirit in Prison
    # Chars:  4997–5169
    sentences = [
            ['As her voice died away, the boy stopped singing, sprang into the sea, kicked up his feet and disappeared.'],
            ['Vere was conscious of a thrill that was like a thrill of triumph.']
        ]
    expected = [
            'As her voice died away, the boy stopped singing, sprang into the sea, kicked up his feet and disappeared.',
            'Vere was conscious of a thrill that was like a thrill of triumph.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_chesterton_a_chesterton_calendar_compiled_from_the_writings_():
    # Source: Chesterton - A Chesterton Calendar Compiled From the Writings of Gkc Both in Verse and in Pro
    # Chars:  4413–4752
    sentences = [
            ['Step softly, under snow or rain,',
             'To find the place where men can pray;.The way is all so very plain,',
             'That we may lose the way.'],
            ['Oh, we have learnt to peer and pore.',
             'On tortured puzzles from our youth.',
             'We know all labyrinthine lore,',
             'We are the three Wise Men of yore,',
             'And we know all things but the truth.']
        ]
    expected = [
            'Step softly, under snow or rain, To find the place where men can pray;.The way is all so very plain, That we may lose the way.',
            'Oh, we have learnt to peer and pore. On tortured puzzles from our youth. We know all labyrinthine lore, We are the three Wise Men of yore, And we know all things but the truth.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_rinehart_a_poor_wise_man():
    # Source: Rinehart - A Poor Wise Man
    # Chars:  5574–6457
    sentences = [
            ['The curious reserve that so often exists between mother and daughter held Grace Cardew dumb.',
             'She nodded, but her eyes had slightly hardened.',
             'So this was what war had done to her.',
             'She had had no son, and had thanked God for it during the war, although old Anthony had hated her all her married life for it.',
             'But she had given her daughter, her clear-eyed daughter, and they had shown her the dregs of life.'],
            ['Her thoughts went back over the years.',
             'To Lily as a child, with Mademoiselle always at her elbow, and life painted as a thing of beauty.',
             'Love, marriage and birth were divine accidents.',
             'Death was a quiet sleep, with heaven just beyond, a sleep which came only to age, which had wearied and would rest.',
             "Then she remembered the day when Elinor Cardew, poor unhappy Elinor, had fled back to Anthony's roof to have a baby, and after a few rapturous weeks for Lily the baby had died."]
        ]
    expected = [
            'The curious reserve that so often exists between mother and daughter held Grace Cardew dumb. She nodded, but her eyes had slightly hardened. So this was what war had done to her. She had had no son, and had thanked God for it during the war, although old Anthony had hated her all her married life for it. But she had given her daughter, her clear-eyed daughter, and they had shown her the dregs of life.',
            "Her thoughts went back over the years. To Lily as a child, with Mademoiselle always at her elbow, and life painted as a thing of beauty. Love, marriage and birth were divine accidents. Death was a quiet sleep, with heaven just beyond, a sleep which came only to age, which had wearied and would rest. Then she remembered the day when Elinor Cardew, poor unhappy Elinor, had fled back to Anthony's roof to have a baby, and after a few rapturous weeks for Lily the baby had died."
        ]
    assert segment_paragraphs(sentences) == expected

def test_wister_a_journey_in_search_of_christmas():
    # Source: Wister - A Journey in Search of Christmas
    # Chars:  4123–5056
    sentences = [
            ['His Excellency the jovial Governor opened his teeth in pleasure at this, for he was a bachelor, and there were fifteen upon his list, which he held up for the edification of the hasty McLean.',
             '"Not mine, I\'m happy to say.',
             "My friends keep marrying and settling, and their kids call me uncle, and climb around and bother, and I forget their names, and think it's a girl, and the mother gets mad.",
             "Why, if I didn't remember these little folks at Christmas they'd be wondering—not the kids, they just break your toys and don't notice; but the mother would wonder—'What's the matter with Dr. Barker?",
             'Has Governor Barker gone back on us?\'—that\'s where the strain comes!" he broke off, facing Mr. McLean with another spacious laugh.'],
            ["But the cow-puncher had ceased to smile, and now, while Barker ran on exuberantly McLean's wide-open eyes rested upon him, singular and intent, and in their hazel depths the last gleam of jocularity went out."]
        ]
    expected = [
            'His Excellency the jovial Governor opened his teeth in pleasure at this, for he was a bachelor, and there were fifteen upon his list, which he held up for the edification of the hasty McLean. "Not mine, I\'m happy to say. My friends keep marrying and settling, and their kids call me uncle, and climb around and bother, and I forget their names, and think it\'s a girl, and the mother gets mad. Why, if I didn\'t remember these little folks at Christmas they\'d be wondering—not the kids, they just break your toys and don\'t notice; but the mother would wonder—\'What\'s the matter with Dr. Barker? Has Governor Barker gone back on us?\'—that\'s where the strain comes!" he broke off, facing Mr. McLean with another spacious laugh.',
            "But the cow-puncher had ceased to smile, and now, while Barker ran on exuberantly McLean's wide-open eyes rested upon him, singular and intent, and in their hazel depths the last gleam of jocularity went out."
        ]
    assert segment_paragraphs(sentences) == expected

def test_defoe_a_journal_of_the_plague_year_being_observations_or_mem():
    # Source: Defoe - A Journal of the Plague Year Being Observations or Memorials of the Most Remarka
    # Chars:  5021–5504
    sentences = [
            ["The like increase of the bills was observed in the parishes of St.Bride's, adjoining on one side of Holborn parish, and in the.parish of St James, Clerkenwell, adjoining on the other side of.",
             'Holborn; in both which parishes the usual numbers that died.weekly were from four to six or eight, whereas at that time they.were increased as follows:—.'],
            ['From December 20 to December 27.',
             '{',
             'St Bride\'s.0."',
             ".  .  { St James's.8."]
        ]
    expected = [
            "The like increase of the bills was observed in the parishes of St.Bride's, adjoining on one side of Holborn parish, and in the.parish of St James, Clerkenwell, adjoining on the other side of. Holborn; in both which parishes the usual numbers that died.weekly were from four to six or eight, whereas at that time they.were increased as follows:—.",
            'From December 20 to December 27. { St Bride\'s.0." .  .  { St James\'s.8.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_edgeworth_castle_rackrent():
    # Source: Edgeworth - Castle Rackrent
    # Chars:  9966–10176
    sentences = [
            ["TRUTH WHICH PERVADE THE WORKS OF MY ACCOMPLISHED FRIEND,' Sir Walter wrote, I FELT THAT SOMETHING MIGHT BE ATTEMPTED FOR MY OWN COUNTRY OF"],
            ['The Same Kind As That Which Miss Edgeworth So Fortunately Achieved For']
        ]
    expected = [
            "TRUTH WHICH PERVADE THE WORKS OF MY ACCOMPLISHED FRIEND,' Sir Walter wrote, I FELT THAT SOMETHING MIGHT BE ATTEMPTED FOR MY OWN COUNTRY OF",
            'The Same Kind As That Which Miss Edgeworth So Fortunately Achieved For'
        ]
    assert segment_paragraphs(sentences) == expected

def test_alcott_a_garland_for_girls():
    # Source: Alcott - A Garland for Girls
    # Chars:  10655–11297
    sentences = [
            ['With these farewell words from their president the girls departed, with great plans and new ideas simmering in their young heads and hearts.'],
            ['It seemed a vast undertaking; but where there is a will there is always a way, and soon it was evident that each had found "a little chore" to do for sweet charity\'s sake.',
             'Not a word was said at the weekly meetings, but the artless faces betrayed all shades of hope, discouragement, pride, and doubt, as their various attempts seemed likely to succeed or fail.',
             'Much curiosity was felt, and a few accidental words, hints, or meetings in queer places, were very exciting, though nothing was discovered.']
        ]
    expected = [
            'With these farewell words from their president the girls departed, with great plans and new ideas simmering in their young heads and hearts.',
            'It seemed a vast undertaking; but where there is a will there is always a way, and soon it was evident that each had found "a little chore" to do for sweet charity\'s sake. Not a word was said at the weekly meetings, but the artless faces betrayed all shades of hope, discouragement, pride, and doubt, as their various attempts seemed likely to succeed or fail. Much curiosity was felt, and a few accidental words, hints, or meetings in queer places, were very exciting, though nothing was discovered.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_hardy_the_woodlanders():
    # Source: Hardy - The Woodlanders
    # Chars:  4235–4815
    sentences = [
            ['She assured him that she could—that as she went to Great Hintock her van passed near it—that it was only up the lane that branched out of the lane into which she was about to turn—just ahead.',
             '"Though," continued Mrs. Dollery, "\'tis such a little small place that, as a town gentleman, you\'d need have a candle and lantern to find it if ye don\'t know where \'tis.',
             'Bedad!',
             "I wouldn't live there if they'd pay me to.",
             'Now at Great Hintock you do see the world a bit."'],
            ["He mounted and sat beside her, with his feet outside, where they were ever and anon brushed over by the horse's tail."]
        ]
    expected = [
            'She assured him that she could—that as she went to Great Hintock her van passed near it—that it was only up the lane that branched out of the lane into which she was about to turn—just ahead. "Though," continued Mrs. Dollery, "\'tis such a little small place that, as a town gentleman, you\'d need have a candle and lantern to find it if ye don\'t know where \'tis. Bedad! I wouldn\'t live there if they\'d pay me to. Now at Great Hintock you do see the world a bit."',
            "He mounted and sat beside her, with his feet outside, where they were ever and anon brushed over by the horse's tail."
        ]
    assert segment_paragraphs(sentences) == expected

def test_hardy_a_pair_of_blue_eyes():
    # Source: Hardy - A Pair of Blue Eyes
    # Chars:  4460–4876
    sentences = [
            ['One point in her, however, you did notice: that was her eyes. In them was seen a sublimation of all of her; it was not necessary to look further: there she lived.'],
            ['These eyes were blue; blue as autumn distance—blue as the blue we see between the retreating mouldings of hills and woody slopes on a sunny September morning.',
             'A misty and shady blue, that had no beginning or surface, and was looked INTO rather than AT.']
        ]
    expected = [
            'One point in her, however, you did notice: that was her eyes. In them was seen a sublimation of all of her; it was not necessary to look further: there she lived.',
            'These eyes were blue; blue as autumn distance—blue as the blue we see between the retreating mouldings of hills and woody slopes on a sunny September morning. A misty and shady blue, that had no beginning or surface, and was looked INTO rather than AT.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_moore_a_mummers_wife():
    # Source: Moore - A Mummers Wife
    # Chars:  7746–8673
    sentences = [
            ['In default of a screen, a gown and a red petticoat had been thrown over a clothes-horse, and these shaded the glare of the lamp from the eyes of the sick man. In the pale obscurity of the room, his bearded cheeks could be seen buried in a heap of tossed pillows.',
             'By his bedside sat a young woman.',
             'As she dozed, her face drooped until her features were hidden, and the lamp-light made the curious curves of a beautiful ear look like a piece of illuminated porcelain.',
             'Her hands lay upon her lap, her needlework slipped from them; and as it fell to the ground she awoke.'],
            ['She pressed her hands against her forehead and made an effort to rouse herself.',
             'As she did so, her face contracted with an expression of disgust, and she remembered the ether.',
             'The soft, vaporous odour drifted towards her from a small table strewn with medicine bottles, and taking care to hold the cork tightly in her fingers she squeezed it into the bottle.']
        ]
    expected = [
            'In default of a screen, a gown and a red petticoat had been thrown over a clothes-horse, and these shaded the glare of the lamp from the eyes of the sick man. In the pale obscurity of the room, his bearded cheeks could be seen buried in a heap of tossed pillows. By his bedside sat a young woman. As she dozed, her face drooped until her features were hidden, and the lamp-light made the curious curves of a beautiful ear look like a piece of illuminated porcelain. Her hands lay upon her lap, her needlework slipped from them; and as it fell to the ground she awoke.',
            'She pressed her hands against her forehead and made an effort to rouse herself. As she did so, her face contracted with an expression of disgust, and she remembered the ether. The soft, vaporous odour drifted towards her from a small table strewn with medicine bottles, and taking care to hold the cork tightly in her fingers she squeezed it into the bottle.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_jerome_all_roads_lead_to_calvary():
    # Source: Jerome - All Roads Lead to Calvary
    # Chars:  4304–4584
    sentences = [
            ['Mary Stopperton was afraid he never had, in spite of its being so near.',
             '"And yet he was a dear good Christian--in his way," Mary Stopperton felt sure.'],
            ['"How do you mean \'in his way\'?" demanded Joan.',
             'It certainly, if Froude was to be trusted, could not have been the orthodox way.']
        ]
    expected = [
            'Mary Stopperton was afraid he never had, in spite of its being so near. "And yet he was a dear good Christian--in his way," Mary Stopperton felt sure.',
            '"How do you mean \'in his way\'?" demanded Joan. It certainly, if Froude was to be trusted, could not have been the orthodox way.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_howells_a_belated_guest_from_literary_friends_and_acquaintan():
    # Source: Howells - A Belated Guest From Literary Friends and Acquaintance
    # Chars:  4470–5401
    sentences = [
            ["Before they came in sight of the editor's humble roof he had mocked himself to his guest for his trepidations, and Harte with burlesque magnanimity had consented to be for that occasion only something less formidable than he had loomed afar.",
             'He accepted with joy the theory of passing a week in the home of virtuous poverty, and the week began as delightfully as it went on.',
             'From first to last Cambridge amused him as much as it charmed him by that air of academic distinction which was stranger to him even than the refined trees and grass.',
             'It has already been told how, after a list of the local celebrities had been recited to him, he said, "why, you couldn\'t stand on your front porch and fire off your revolver without bringing down a two volumer," and no doubt the pleasure he had in it was the effect of its contrast with the wild California he had known, and perhaps, when he had not altogether known it, had invented.'],
            ['Ii.']
        ]
    expected = [
            'Before they came in sight of the editor\'s humble roof he had mocked himself to his guest for his trepidations, and Harte with burlesque magnanimity had consented to be for that occasion only something less formidable than he had loomed afar. He accepted with joy the theory of passing a week in the home of virtuous poverty, and the week began as delightfully as it went on. From first to last Cambridge amused him as much as it charmed him by that air of academic distinction which was stranger to him even than the refined trees and grass. It has already been told how, after a list of the local celebrities had been recited to him, he said, "why, you couldn\'t stand on your front porch and fire off your revolver without bringing down a two volumer," and no doubt the pleasure he had in it was the effect of its contrast with the wild California he had known, and perhaps, when he had not altogether known it, had invented.',
            'Ii.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_ellis_affirmations():
    # Source: Ellis - Affirmations
    # Chars:  57836–59924
    sentences = [
            ["I have briefly stated Nietzsche's feeling as regards each of the three chief European peoples, because we are thus led up to the central points of his philosophy--his attitude towards modern religion and his attitude towards modern morals.",
             'We are often apt to regard these matters as of little practical importance; we think it the reasonable duty of practical social politics to attend to the immediate questions in hand, and leave these wider questions to settle themselves.',
             'Rightly or wrongly, that was not how Nietzsche looked at the matter.',
             'He was too much of a philosopher, he had too keen a sense of the vital relation of things, to be content with the policy of tinkering society, wherever it seems to need mending most badly, avoiding any reference to the whole.',
             'That is our English method, and no doubt it is a very sane and safe method, but, as we have seen, Nietzsche was not in sympathy with English methods.',
             'His whole significance lies in the thorough and passionate analysis with which he sought to dissect and to dissolve, first, "German culture," then Christianity, and lastly, modern morals, with all that these involve.'],
            ['It is scarcely necessary to point out, that though Nietzsche rejoiced in the title of freethinker, he can by no means be confounded with the ordinary secularist.',
             'He is not bent on destroying religion from any anæsthesia of the religious sense, or even in order to set up some religion of science which is practically no religion at all.',
             'He is thus on different ground from the great freethinkers of France, and to some extent of England.',
             'Nietzsche was himself of the stuff of which great religious teachers are made, of the race of apostles.',
             'So when he writes of the founder of Christianity and the great Christian types, it is often with a poignant sympathy which the secularist can never know; and if his knife seems keen and cruel, it is not the easy indifferent cruelty of the pachydermatous scoffer.',
             'When he analyses the souls of these men and the impulses which have moved them, he knows with what he is dealing: he is analysing his own soul.']
        ]
    expected = [
            'I have briefly stated Nietzsche\'s feeling as regards each of the three chief European peoples, because we are thus led up to the central points of his philosophy--his attitude towards modern religion and his attitude towards modern morals. We are often apt to regard these matters as of little practical importance; we think it the reasonable duty of practical social politics to attend to the immediate questions in hand, and leave these wider questions to settle themselves. Rightly or wrongly, that was not how Nietzsche looked at the matter. He was too much of a philosopher, he had too keen a sense of the vital relation of things, to be content with the policy of tinkering society, wherever it seems to need mending most badly, avoiding any reference to the whole. That is our English method, and no doubt it is a very sane and safe method, but, as we have seen, Nietzsche was not in sympathy with English methods. His whole significance lies in the thorough and passionate analysis with which he sought to dissect and to dissolve, first, "German culture," then Christianity, and lastly, modern morals, with all that these involve.',
            'It is scarcely necessary to point out, that though Nietzsche rejoiced in the title of freethinker, he can by no means be confounded with the ordinary secularist. He is not bent on destroying religion from any anæsthesia of the religious sense, or even in order to set up some religion of science which is practically no religion at all. He is thus on different ground from the great freethinkers of France, and to some extent of England. Nietzsche was himself of the stuff of which great religious teachers are made, of the race of apostles. So when he writes of the founder of Christianity and the great Christian types, it is often with a poignant sympathy which the secularist can never know; and if his knife seems keen and cruel, it is not the easy indifferent cruelty of the pachydermatous scoffer. When he analyses the souls of these men and the impulses which have moved them, he knows with what he is dealing: he is analysing his own soul.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_bower_cabin_fever():
    # Source: Bower - Cabin Fever
    # Chars:  6605–7633
    sentences = [
            ['There were the evenings he spent in the Basin, sitting beside Marie in the huge campfire circle, made wonderful by the shadowy giants, the redwoods; talking foolishness in undertones while the crowd sang snatches of songs which no one knew from beginning to end, and that went very lumpy in the verses and very much out of harmony in the choruses.',
             'Sometimes they would stroll down toward that sweeter music the creek made, and stand beside one of the enormous trees and watch the glow of the fire, and the silhouettes of the people gathered around it.'],
            ["In a week they were surreptitiously holding hands. In two weeks they could scarcely endure the partings when Bud must start back to San Jose, and were taxing their ingenuity to invent new reasons why Marie must go along. In three weeks they were married, and Marie's mother--a shrewd, shrewish widow--was trying to decide whether she should wash her hands of Marie, or whether it might be well to accept the situation and hope that Bud would prove himself a rising young man."]
        ]
    expected = [
            'There were the evenings he spent in the Basin, sitting beside Marie in the huge campfire circle, made wonderful by the shadowy giants, the redwoods; talking foolishness in undertones while the crowd sang snatches of songs which no one knew from beginning to end, and that went very lumpy in the verses and very much out of harmony in the choruses. Sometimes they would stroll down toward that sweeter music the creek made, and stand beside one of the enormous trees and watch the glow of the fire, and the silhouettes of the people gathered around it.',
            "In a week they were surreptitiously holding hands. In two weeks they could scarcely endure the partings when Bud must start back to San Jose, and were taxing their ingenuity to invent new reasons why Marie must go along. In three weeks they were married, and Marie's mother--a shrewd, shrewish widow--was trying to decide whether she should wash her hands of Marie, or whether it might be well to accept the situation and hope that Bud would prove himself a rising young man."
        ]
    assert segment_paragraphs(sentences) == expected

def test_gilman_concerning_children():
    # Source: Gilman - Concerning Children
    # Chars:  5264–5777
    sentences = [
            ['So far as environment is to really develope the race, that development must be made before the birth of the next generation.'],
            ['If a young man and woman are clean, healthy, vigorous, and virtuous before parenthood, they may become dirty, sickly, weak, and wicked afterward with far less ill effect to the race than if they were sick and vicious before their children were born, and thereafter became stalwart saints.',
             'The sowing of wild oats would be far less harmful if sowed in the autumn instead of in the spring.']
        ]
    expected = [
            'So far as environment is to really develope the race, that development must be made before the birth of the next generation.',
            'If a young man and woman are clean, healthy, vigorous, and virtuous before parenthood, they may become dirty, sickly, weak, and wicked afterward with far less ill effect to the race than if they were sick and vicious before their children were born, and thereafter became stalwart saints. The sowing of wild oats would be far less harmful if sowed in the autumn instead of in the spring.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_wallace_angel_esquire():
    # Source: Wallace - Angel Esquire
    # Chars:  4975–5350
    sentences = [
            ['So in rain and sunshine, by day and by night, the New Safe Deposit came into existence.'],
            ['Once--it was during a night shift, a brougham drove up the deserted city street, and a footman helped from the dark interior of the carriage a shivering old man with a white, drawn face.',
             'He showed a written order to the foreman, and was allowed inside the unpainted gate of the "works."']
        ]
    expected = [
            'So in rain and sunshine, by day and by night, the New Safe Deposit came into existence.',
            'Once--it was during a night shift, a brougham drove up the deserted city street, and a footman helped from the dark interior of the carriage a shivering old man with a white, drawn face. He showed a written order to the foreman, and was allowed inside the unpainted gate of the "works."'
        ]
    assert segment_paragraphs(sentences) == expected

def test_stowe_a_key_to_uncle_toms_cabin_presenting_the_original_fact():
    # Source: Stowe - A Key to Uncle Toms Cabin Presenting the Original Facts and Documents Upon Which
    # Chars:  4361–5019
    sentences = [
            ['The woman looked at the little boy who had been standing at her knee, with an expressive glance, and said, "She will be three years old this summer."'],
            ['On further inquiry into the history of the woman, it appeared that she had been set free by the will of her owners; that the child was legally entitled to freedom, but had been seized on by the heirs of the estate.',
             'She was poor and friendless, without money to maintain a suit, and the heirs, of course, threw the child into the hands of the trader.',
             'The necessary sum, it may be added, was all raised in the small neighborhood which then surrounded the Lane Theological Seminary, and the child was redeemed.']
        ]
    expected = [
            'The woman looked at the little boy who had been standing at her knee, with an expressive glance, and said, "She will be three years old this summer."',
            'On further inquiry into the history of the woman, it appeared that she had been set free by the will of her owners; that the child was legally entitled to freedom, but had been seized on by the heirs of the estate. She was poor and friendless, without money to maintain a suit, and the heirs, of course, threw the child into the hands of the trader. The necessary sum, it may be added, was all raised in the small neighborhood which then surrounded the Lane Theological Seminary, and the child was redeemed.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_hardy_wessex_tales():
    # Source: Hardy - Wessex Tales
    # Chars:  8817–9448
    sentences = [
            ['The servant did so; but the mistress of the house merely transmitted her former words.'],
            ['Barnet said nothing more, and presently sat down to his lonely meal, which was eaten abstractedly, the domestic scene he had lately witnessed still impressing him by its contrast with the situation here.',
             'His mind fell back into past years upon a certain pleasing and gentle being whose face would loom out of their shades at such times as these.',
             'Barnet turned in his chair, and looked with unfocused eyes in a direction southward from where he sat, as if he saw not the room but a long way beyond.',
             "'I wonder if she lives there still!' he said."]
        ]
    expected = [
            'The servant did so; but the mistress of the house merely transmitted her former words.',
            "Barnet said nothing more, and presently sat down to his lonely meal, which was eaten abstractedly, the domestic scene he had lately witnessed still impressing him by its contrast with the situation here. His mind fell back into past years upon a certain pleasing and gentle being whose face would loom out of their shades at such times as these. Barnet turned in his chair, and looked with unfocused eyes in a direction southward from where he sat, as if he saw not the room but a long way beyond. 'I wonder if she lives there still!' he said."
        ]
    assert segment_paragraphs(sentences) == expected

def test_moore_the_lake():
    # Source: Moore - The Lake
    # Chars:  4044–5522
    sentences = [
            ["The concern of this preface is with the mistake that was made when 'The Lake' was excluded from the volume entitled 'The Untilled Field,' reducing it to too slight dimensions, for bulk counts; and 'The Lake,' too, in being published in a separate volume lost a great deal in range and power, and criticism was baffled by the division of stories written at the same time and coming out of the same happy inspiration, one that could hardly fail to beget stories in the mind of anybody prone to narrative--the return of a man to his native land, to its people, to memories hidden for years, forgotten, but which rose suddenly out of the darkness, like water out of the earth when a spring is tapped."],
            ["Some chance words passing between John Eglinton and me as we returned home one evening from Professor Dowden's were enough.",
             "He spoke, or I spoke, of a volume of Irish stories; Tourguéniev's name was mentioned, and next morning--if not the next morning, certainly not later than a few mornings after--I was writing 'Homesickness,' while the story of 'The Exile' was taking shape in my mind.",
             "'The Exile' was followed by a series of four stories, a sort of village odyssey.",
             "'A Letter to Rome' is as good as these and as typical of my country.",
             "'So on He Fares' is the one that, perhaps, out of the whole volume I like the best, always excepting 'The Lake,' which, alas, was not included, but which belongs so strictly to the aforesaid stories that my memory includes it in the volume."]
        ]
    expected = [
            "The concern of this preface is with the mistake that was made when 'The Lake' was excluded from the volume entitled 'The Untilled Field,' reducing it to too slight dimensions, for bulk counts; and 'The Lake,' too, in being published in a separate volume lost a great deal in range and power, and criticism was baffled by the division of stories written at the same time and coming out of the same happy inspiration, one that could hardly fail to beget stories in the mind of anybody prone to narrative--the return of a man to his native land, to its people, to memories hidden for years, forgotten, but which rose suddenly out of the darkness, like water out of the earth when a spring is tapped.",
            "Some chance words passing between John Eglinton and me as we returned home one evening from Professor Dowden's were enough. He spoke, or I spoke, of a volume of Irish stories; Tourguéniev's name was mentioned, and next morning--if not the next morning, certainly not later than a few mornings after--I was writing 'Homesickness,' while the story of 'The Exile' was taking shape in my mind. 'The Exile' was followed by a series of four stories, a sort of village odyssey. 'A Letter to Rome' is as good as these and as typical of my country. 'So on He Fares' is the one that, perhaps, out of the whole volume I like the best, always excepting 'The Lake,' which, alas, was not included, but which belongs so strictly to the aforesaid stories that my memory includes it in the volume."
        ]
    assert segment_paragraphs(sentences) == expected

def test_moore_muslin():
    # Source: Moore - Muslin
    # Chars:  8168–11062
    sentences = [
            ['The public is without power of expression, and it felt that it was being fooled for some purpose not very apparent and perhaps anarchical.',
             "Nor is a sudden revelation very convincing in modern times. In the space of three minutes, Nora, who has been her husband's sensual toy, and has taken pleasure in being that, and only that, leaves her husband and her children, as has been said, for school-books.",
             'A more arbitrary piece of stage craft was never devised; but it was not the stage craft the critics were accustomed to, and the admirers of Ibsen did not dare to admit that he had devised Nora to cry aloud that a woman is more than a domestic animal.',
             "It would have been fatal for an apostle or even a disciple to admit the obvious fact that Ibsen was a dramatist of moral ideas rather than of sensuous emotions; and there was nobody in the 'eighties to explain the redemption of Ibsen by his dialogue, the strongest and most condensed ever written, yet coming off the reel like silk.",
             'A wonderful thread, that never tangles in his hands.',
             'Ibsen is a magical weaver, and so closely does he weave that we are drawn along in the net like fishes.'],
            ["But it is with the subject of the Doll's House rather than with the art with which it is woven that we are concerned here.",
             "The subject of _A Drama in Muslin_ is the same as that of A Doll's House, and for this choice of subject I take pride in my forerunner.",
             "It was a fine thing for a young man of thirty to choose the subject instinctively that Ibsen had chosen a few years before; it is a feather in his cap surely; and I remember with pleasure that he was half through his story when Dr. Aveling read him the first translation of A Doll's House, a poor thing, done by a woman, that withheld him from any appreciation of the play.",
             "The fact that he was writing the same subject from an entirely different point of view prejudiced him against Ibsen; and the making of a woman first in a sensual and afterward transferring her into an educational mould with a view to obtaining an instrument to thunder out a given theme could not be else than abhorrent to one whose art, however callow, was at least objective. In the Doll's House Ibsen had renounced all objectivity.",
             "It does not seem to me that further apologies are necessary for my predecessor's remark to Dr. Aveling after the reading that he was engaged in moulding a woman in one of Nature's moulds.",
             "'A puritan,' he said, 'I am writing of, but not a sexless puritan, and if women cannot win their freedom without leaving their sex behind they had better remain slaves, for a slave with his sex is better than a free eunuch;' and he discoursed on the book he was writing, convinced that Alice Barton represented her sex better than the archetypal hieratic and clouded figure of Nora which Ibsen had dreamed so piously, allowing, he said, memories of Egyptian sculpture to mingle with his dreams."]
        ]
    expected = [
            "The public is without power of expression, and it felt that it was being fooled for some purpose not very apparent and perhaps anarchical. Nor is a sudden revelation very convincing in modern times. In the space of three minutes, Nora, who has been her husband's sensual toy, and has taken pleasure in being that, and only that, leaves her husband and her children, as has been said, for school-books. A more arbitrary piece of stage craft was never devised; but it was not the stage craft the critics were accustomed to, and the admirers of Ibsen did not dare to admit that he had devised Nora to cry aloud that a woman is more than a domestic animal. It would have been fatal for an apostle or even a disciple to admit the obvious fact that Ibsen was a dramatist of moral ideas rather than of sensuous emotions; and there was nobody in the 'eighties to explain the redemption of Ibsen by his dialogue, the strongest and most condensed ever written, yet coming off the reel like silk. A wonderful thread, that never tangles in his hands. Ibsen is a magical weaver, and so closely does he weave that we are drawn along in the net like fishes.",
            "But it is with the subject of the Doll's House rather than with the art with which it is woven that we are concerned here. The subject of _A Drama in Muslin_ is the same as that of A Doll's House, and for this choice of subject I take pride in my forerunner. It was a fine thing for a young man of thirty to choose the subject instinctively that Ibsen had chosen a few years before; it is a feather in his cap surely; and I remember with pleasure that he was half through his story when Dr. Aveling read him the first translation of A Doll's House, a poor thing, done by a woman, that withheld him from any appreciation of the play. The fact that he was writing the same subject from an entirely different point of view prejudiced him against Ibsen; and the making of a woman first in a sensual and afterward transferring her into an educational mould with a view to obtaining an instrument to thunder out a given theme could not be else than abhorrent to one whose art, however callow, was at least objective. In the Doll's House Ibsen had renounced all objectivity. It does not seem to me that further apologies are necessary for my predecessor's remark to Dr. Aveling after the reading that he was engaged in moulding a woman in one of Nature's moulds. 'A puritan,' he said, 'I am writing of, but not a sexless puritan, and if women cannot win their freedom without leaving their sex behind they had better remain slaves, for a slave with his sex is better than a free eunuch;' and he discoursed on the book he was writing, convinced that Alice Barton represented her sex better than the archetypal hieratic and clouded figure of Nora which Ibsen had dreamed so piously, allowing, he said, memories of Egyptian sculpture to mingle with his dreams."
        ]
    assert segment_paragraphs(sentences) == expected

def test_hornung_a_bride_from_the_bush():
    # Source: Hornung - A Bride From the Bush
    # Chars:  4472–5709
    sentences = [
            ["The interpolation was not exactly ill-natured; but it was received in silence; and Granville's tones, as he resumed the reading, were even more studiously unsympathetic than before."],
            ['\'"Of my Bride I will say very little; for you will see her in a week at most.',
             'As for myself, I can only tell you, dear Mother, that I am the very luckiest and happiest man on earth!"\' (\'A brave statement,\' Granville murmured in parenthesis; \'but they all make it.\') \'"She is typically Australian, having indeed been born and bred in the Bush, and is the first to admit it, being properly proud of her native land; but, if you knew the Australians as I do, this would not frighten you.',
             'Far from it, for the typical Australian is one of the very highest if not the highest development of our species.',
             '"\' (Granville read that sentence with impressive gravity, and with such deference to the next as to suggest no kind of punctuation, since the writer had neglected it.) \'.',
             '"But as you, my dear Mother, are the very last person in the world to be prejudiced by mere mannerisms, I won\'t deny that she has one or two--though, mind you, I like them!',
             'And, at least, you may look forward to seeing the most beautiful woman you ever saw in your life--though I say it.']
        ]
    expected = [
            "The interpolation was not exactly ill-natured; but it was received in silence; and Granville's tones, as he resumed the reading, were even more studiously unsympathetic than before.",
            '\'"Of my Bride I will say very little; for you will see her in a week at most. As for myself, I can only tell you, dear Mother, that I am the very luckiest and happiest man on earth!"\' (\'A brave statement,\' Granville murmured in parenthesis; \'but they all make it.\') \'"She is typically Australian, having indeed been born and bred in the Bush, and is the first to admit it, being properly proud of her native land; but, if you knew the Australians as I do, this would not frighten you. Far from it, for the typical Australian is one of the very highest if not the highest development of our species. "\' (Granville read that sentence with impressive gravity, and with such deference to the next as to suggest no kind of punctuation, since the writer had neglected it.) \'. "But as you, my dear Mother, are the very last person in the world to be prejudiced by mere mannerisms, I won\'t deny that she has one or two--though, mind you, I like them! And, at least, you may look forward to seeing the most beautiful woman you ever saw in your life--though I say it.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_chambers_a_young_man_in_a_hurry_and_other_short_stories():
    # Source: Chambers - A Young Man in a Hurry and Other Short Stories
    # Chars:  4028–4317
    sentences = [
            ['The young lady was startled, but resolute.',
             '"You have made a dreadful mistake," she said; "you are in the wrong cab--".'],
            ['The match went out; there came a brief moment of darkness, then the cab turned a corner, and the ghostly light of electric lamps played over them in quivering succession.']
        ]
    expected = [
            'The young lady was startled, but resolute. "You have made a dreadful mistake," she said; "you are in the wrong cab--".',
            'The match went out; there came a brief moment of darkness, then the cab turned a corner, and the ghostly light of electric lamps played over them in quivering succession.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_marsh_a_duel():
    # Source: Marsh - A Duel
    # Chars:  5499–6664
    sentences = [
            ['When the young wife realised, or thought she realised, all that the curt epistle meant, she told herself that now indeed the worst had come.',
             'She had just had another bitter scene with her husband; had, in fact, driven him out into the night before the tempest of her scorn and opprobrium.',
             'The landlady had departed on an errand of her own.',
             'Isabel told herself that now, if ever, an opportunity presented itself to cut herself free from the bonds in which she had foolishly allowed herself to be entwined.',
             'She went upstairs, put on her hat and jacket, crammed a few of her scanty possessions into a leather handbag, and then--and only then--paused to think.'],
            ["It was nearly nine o'clock, late for that part of the world.",
             'The nearest railway station was at Carnoustie, more than seven miles away.',
             'She knew that there was an early train which would take her to Dundee, and thence to London; but, supposing she caught it, how about the fare?',
             'The fare to London was nearly two pounds; she had not a shilling.',
             'She did not doubt that, once in London, she could live, as she always had lived; but she had to get there first, across five hundred miles of intervening country.']
        ]
    expected = [
            'When the young wife realised, or thought she realised, all that the curt epistle meant, she told herself that now indeed the worst had come. She had just had another bitter scene with her husband; had, in fact, driven him out into the night before the tempest of her scorn and opprobrium. The landlady had departed on an errand of her own. Isabel told herself that now, if ever, an opportunity presented itself to cut herself free from the bonds in which she had foolishly allowed herself to be entwined. She went upstairs, put on her hat and jacket, crammed a few of her scanty possessions into a leather handbag, and then--and only then--paused to think.',
            "It was nearly nine o'clock, late for that part of the world. The nearest railway station was at Carnoustie, more than seven miles away. She knew that there was an early train which would take her to Dundee, and thence to London; but, supposing she caught it, how about the fare? The fare to London was nearly two pounds; she had not a shilling. She did not doubt that, once in London, she could live, as she always had lived; but she had to get there first, across five hundred miles of intervening country."
        ]
    assert segment_paragraphs(sentences) == expected

def test_marryat_diary_in_america_series_one():
    # Source: Marryat - Diary in America Series One
    # Chars:  4427–5623
    sentences = [
            ['It was impossible to have done more on either side; and the gentleman who gave me this information added, that McDonough told him that so nicely balanced were the chances, that he took out his watch just before the British colours were hauled down, and observed, "If they hold out ten minutes more, it will be more than, I am afraid, we can do."',
             'As soon as the victory was decided on the part of the Americans, the British general commenced his retreat, and was followed by this handful of militia. In a day or two afterwards, General McCoomb came up, and a large force was poured in from all quarters.'],
            ["There was something very similar and quite as ridiculous in the affair at Sackett's harbour.",
             'Our forces advancing would have cut off some hundreds of the American militia, who were really retreating, but by a road which led in such a direction as for a time to make the English commandant suppose that they were intending to take him in flank.',
             'This made him imagine that they must be advancing in large numbers, when, the fact was, they were running away from his superior force.',
             'He made a retreat; upon ascertaining which, the Americans turned back and followed him, harassing his rear.']
        ]
    expected = [
            'It was impossible to have done more on either side; and the gentleman who gave me this information added, that McDonough told him that so nicely balanced were the chances, that he took out his watch just before the British colours were hauled down, and observed, "If they hold out ten minutes more, it will be more than, I am afraid, we can do." As soon as the victory was decided on the part of the Americans, the British general commenced his retreat, and was followed by this handful of militia. In a day or two afterwards, General McCoomb came up, and a large force was poured in from all quarters.',
            "There was something very similar and quite as ridiculous in the affair at Sackett's harbour. Our forces advancing would have cut off some hundreds of the American militia, who were really retreating, but by a road which led in such a direction as for a time to make the English commandant suppose that they were intending to take him in flank. This made him imagine that they must be advancing in large numbers, when, the fact was, they were running away from his superior force. He made a retreat; upon ascertaining which, the Americans turned back and followed him, harassing his rear."
        ]
    assert segment_paragraphs(sentences) == expected

def test_bulwer_lytton_alice_or_the_mysteries_book_03():
    # Source: Bulwer-Lytton - Alice or the Mysteries Book 03
    # Chars:  11549–12852
    sentences = [
            ['In the House of Commons, too, and in the bureaucracy, he had no inconsiderable strength; for Lumley never contracted the habits of personal abruptness and discourtesy common to men in power who wish to keep applicants aloof.',
             'He was bland and conciliating to all men of ranks; his intellect and self-complacency raised him far above the petty jealousies that great men feel for rising men.',
             'Did any tyro earn the smallest distinction in parliament, no man sought his acquaintance so eagerly as Lord Vargrave; no man complimented, encouraged, "brought on" the new aspirants of his party with so hearty a good will.'],
            ['Such a minister could not fail of having devoted followers among the able, the ambitious, and the vain.',
             'It must also be confessed that Lord Vargrave neglected no baser and less justifiable means to cement his power by placing it on the sure rock of self-interest.',
             'No jobbing was too gross for him.',
             'He was shamefully corrupt in the disposition of his patronage; and no rebuffs, no taunts from his official brethren, could restrain him from urging the claims of any of his creatures upon the public purse.',
             'His followers regarded this charitable selfishness as the stanchness and zeal of friendship; and the ambition of hundreds was wound up in the ambition of the unprincipled minister.']
        ]
    expected = [
            'In the House of Commons, too, and in the bureaucracy, he had no inconsiderable strength; for Lumley never contracted the habits of personal abruptness and discourtesy common to men in power who wish to keep applicants aloof. He was bland and conciliating to all men of ranks; his intellect and self-complacency raised him far above the petty jealousies that great men feel for rising men. Did any tyro earn the smallest distinction in parliament, no man sought his acquaintance so eagerly as Lord Vargrave; no man complimented, encouraged, "brought on" the new aspirants of his party with so hearty a good will.',
            'Such a minister could not fail of having devoted followers among the able, the ambitious, and the vain. It must also be confessed that Lord Vargrave neglected no baser and less justifiable means to cement his power by placing it on the sure rock of self-interest. No jobbing was too gross for him. He was shamefully corrupt in the disposition of his patronage; and no rebuffs, no taunts from his official brethren, could restrain him from urging the claims of any of his creatures upon the public purse. His followers regarded this charitable selfishness as the stanchness and zeal of friendship; and the ambition of hundreds was wound up in the ambition of the unprincipled minister.'
        ]
    assert segment_paragraphs(sentences) == expected

def test_chesterton_the_man_who_was_thursday_a_nightmare():
    # Source: Chesterton - The Man Who Was Thursday a Nightmare
    # Chars:  9948–10342
    sentences = [
            ['The girl winced for a flash at the unpleasant word, but Syme was too hot to heed her.'],
            ['"It is things going right," he cried, "that is poetical!',
             'Our digestions, for instance, going sacredly and silently right, that is the foundation of all poetry.',
             'Yes, the most poetical thing, more poetical than the flowers, more poetical than the stars—the most poetical thing in the world is not being sick."']
        ]
    expected = [
            'The girl winced for a flash at the unpleasant word, but Syme was too hot to heed her.',
            '"It is things going right," he cried, "that is poetical! Our digestions, for instance, going sacredly and silently right, that is the foundation of all poetry. Yes, the most poetical thing, more poetical than the flowers, more poetical than the stars—the most poetical thing in the world is not being sick."'
        ]
    assert segment_paragraphs(sentences) == expected
