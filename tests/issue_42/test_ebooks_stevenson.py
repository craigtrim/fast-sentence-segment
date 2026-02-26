import pytest
from fast_sentence_segment import segment_text


class TestEbooksStevenson:
    """Integration tests mined from Robert Louis Stevenson ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1880s
    """

    def test_wrap_001_awake_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: awake.and
        passage = (
            "For the long nights you lay awake\n"
            "    And watched for my unworthy sake:\n"
            "    For your most comfortable hand\n"
            "    That led me through the uneven land:\n"
            "    For all the story-books you read:\n"
            "    For all the pains you comforted:"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "awake.and" not in full_text

    def test_wrap_002_read_may(self):
        # Source: A Childs Garden of Verses, wrap corruption: read.may
        passage = (
            "And grant it, Heaven, that all who read\n"
            "    May find as dear a nurse at need,\n"
            "    And every child who lists my rhyme,\n"
            "    In the bright, fireside, nursery clime,\n"
            "    May hear it in as kind a voice\n"
            "    As made my childish days rejoice!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "read.may" not in full_text

    def test_wrap_003_swing_three(self):
        # Source: A Childs Garden of Verses, wrap corruption: swing.three
        passage = (
            "Three of us afloat in the meadow by the swing,\n"
            "      Three of us aboard in the basket on the lea.\n"
            "    Winds are in the air, they are blowing in the spring,\n"
            "      And waves are on the meadow like the waves there are at sea."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "swing.three" not in full_text

    def test_wrap_004_afloat_wary(self):
        # Source: A Childs Garden of Verses, wrap corruption: afloat.wary
        passage = (
            "Where shall we adventure, to-day that we're afloat,\n"
            "      Wary of the weather and steering by a star?\n"
            "    Shall it be to Africa, a-steering of the boat,\n"
            "      To Providence, or Babylon, or off to Malabar?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "afloat.wary" not in full_text

    def test_wrap_005_sea_cattle(self):
        # Source: A Childs Garden of Verses, wrap corruption: sea.cattle
        passage = (
            "Hi! but here's a squadron a-rowing on the sea--\n"
            "      Cattle on the meadow a-charging with a roar!\n"
            "    Quick, and we'll escape them, they're as mad as they can be,\n"
            "      The wicket is the harbour and the garden is the shore."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sea.cattle" not in full_text

    def test_wrap_006_set_whenever(self):
        # Source: A Childs Garden of Verses, wrap corruption: set.whenever
        passage = (
            "Whenever the moon and stars are set,\n"
            "      Whenever the wind is high,\n"
            "    All night long in the dark and wet,\n"
            "      A man goes riding by.\n"
            "    Late in the night when the fires are out,\n"
            "    Why does he gallop and gallop about?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "set.whenever" not in full_text

    def test_wrap_007_aloud_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: aloud.and
        passage = (
            "Whenever the trees are crying aloud,\n"
            "      And ships are tossed at sea,\n"
            "    By, on the highway, low and loud,\n"
            "      By at the gallop goes he.\n"
            "    By at the gallop he goes, and then\n"
            "    By he comes back at the gallop again."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "aloud.and" not in full_text

    def test_wrap_008_nails_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: nails.and
        passage = (
            "We took a saw and several nails,\n"
            "    And water in the nursery pails;\n"
            "    And Tom said, \"Let us also take\n"
            "    An apple and a slice of cake;\"--\n"
            "    Which was enough for Tom and me\n"
            "    To go a-sailing on, till tea."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "nails.and" not in full_text

    def test_wrap_009_grow_not(self):
        # Source: A Childs Garden of Verses, wrap corruption: grow.not
        passage = (
            "The funniest thing about him is the way he likes to grow--\n"
            "    Not at all like proper children, which is always very slow;\n"
            "    For he sometimes shoots up taller like an india-rubber ball,\n"
            "    And he sometimes gets so little that there's none of him at all."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "grow.not" not in full_text

    def test_wrap_010_play_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: play.and
        passage = (
            "He hasn't got a notion of how children ought to play,\n"
            "    And can only make a fool of me in every sort of way.\n"
            "    He stays so close beside me, he's a coward you can see;\n"
            "    I'd think shame to stick to nursie as that shadow sticks to me!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "play.and" not in full_text

    def test_wrap_011_neat_with(self):
        # Source: A Childs Garden of Verses, wrap corruption: neat.with
        passage = (
            "The child that is not clean and neat,\n"
            "    With lots of toys and things to eat,\n"
            "    He is a naughty child, I'm sure--\n"
            "    Or else his dear papa is poor."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "neat.with" not in full_text

    def test_wrap_012_out_through(self):
        # Source: A Childs Garden of Verses, wrap corruption: out.through
        passage = (
            "The lights from the parlour and kitchen shone out\n"
            "      Through the blinds and the windows and bars;\n"
            "    And high overhead and all moving about,\n"
            "      There were thousands of millions of stars.\n"
            "    There ne'er were such thousands of leaves on a tree,\n"
            "      Nor of people in church or the Park,\n"
            "    As the crowds of the stars that looked down upon me,\n"
            "      And that glittered and winked in the dark."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "out.through" not in full_text

    def test_wrap_013_all_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: all.and
        passage = (
            "The Dog, and the Plough, and the Hunter, and all,\n"
            "      And the star of the sailor, and Mars,\n"
            "    These shone in the sky, and the pail by the wall\n"
            "      Would be half full of water and stars."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "all.and" not in full_text

    def test_wrap_014_cries_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: cries.and
        passage = (
            "They saw me at last, and they chased me with cries,\n"
            "      And they soon had me packed into bed;\n"
            "    But the glory kept shining and bright in my eyes,\n"
            "      And the stars going round in my head."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "cries.and" not in full_text

    def test_wrap_015_high_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: high.and
        passage = (
            "I saw you toss the kites on high\n"
            "    And blow the birds about the sky;\n"
            "    And all around I heard you pass,\n"
            "    Like ladies' skirts across the grass--\n"
            "      O wind, a-blowing all day long,\n"
            "      O wind, that sings so loud a song!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "high.and" not in full_text

    def test_wrap_016_did_but(self):
        # Source: A Childs Garden of Verses, wrap corruption: did.but
        passage = (
            "I saw the different things you did,\n"
            "    But always you yourself you hid.\n"
            "    I felt you push, I heard you call,\n"
            "    I could not see yourself at all--\n"
            "      O wind, a-blowing all day long,\n"
            "      O wind, that sings so loud a song!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "did.but" not in full_text

    def test_wrap_017_pardon_breaking(self):
        # Source: A Childs Garden of Verses, wrap corruption: pardon.breaking
        passage = (
            "Over the borders, a sin without pardon,\n"
            "      Breaking the branches and crawling below,\n"
            "    Out through the breach in the wall of the garden,\n"
            "      Down by the banks of the river, we go."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pardon.breaking" not in full_text

    def test_wrap_018_thunder_here(self):
        # Source: A Childs Garden of Verses, wrap corruption: thunder.here
        passage = (
            "Here is the mill with the humming of thunder,\n"
            "      Here is the weir with the wonder of foam,\n"
            "    Here is the sluice with the race running under--\n"
            "      Marvellous places, though handy to home!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thunder.here" not in full_text

    def test_wrap_019_stiller_stiller(self):
        # Source: A Childs Garden of Verses, wrap corruption: stiller.stiller
        passage = (
            "Sounds of the village grow stiller and stiller,\n"
            "      Stiller the note of the birds on the hill;\n"
            "    Dusty and dim are the eyes of the miller,\n"
            "      Deaf are his ears with the moil of the mill."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "stiller.stiller" not in full_text

    def test_wrap_020_river_wheel(self):
        # Source: A Childs Garden of Verses, wrap corruption: river.wheel
        passage = (
            "Years may go by, and the wheel in the river\n"
            "      Wheel as it wheels for us, children, to-day,\n"
            "    Wheel and keep roaring and foaming for ever\n"
            "      Long after all of the boys are away."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "river.wheel" not in full_text

    def test_wrap_021_ocean_heroes(self):
        # Source: A Childs Garden of Verses, wrap corruption: ocean.heroes
        passage = (
            "Home from the Indies and home from the ocean,\n"
            "      Heroes and soldiers we all shall come home;\n"
            "    Still we shall find the old mill wheel in motion,\n"
            "      Turning and churning that river to foam."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ocean.heroes" not in full_text

    def test_wrap_022_sky_its(self):
        # Source: A Childs Garden of Verses, wrap corruption: sky.its
        passage = (
            "My tea is nearly ready and the sun has left the sky.\n"
            "    It's time to take the window to see Leerie going by;\n"
            "    For every night at teatime and before you take your seat,\n"
            "    With lantern and with ladder he comes posting up the street."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sky.its" not in full_text

    def test_wrap_023_sea_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: sea.and
        passage = (
            "Now Tom would be a driver and Maria go to sea,\n"
            "    And my papa's a banker and as rich as he can be;\n"
            "    But I, when I am stronger and can choose what I'm to do,\n"
            "    O Leerie, I'll go round at night and light the lamps with you!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sea.and" not in full_text

    def test_wrap_024_door_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: door.and
        passage = (
            "For we are very lucky, with a lamp before the door,\n"
            "    And Leerie stops to light it as he lights so many more;\n"
            "    And oh! before you hurry by with ladder and with light;\n"
            "    O Leerie, see a little child and nod to him tonight!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "door.and" not in full_text

    def test_wrap_025_hall_she(self):
        # Source: A Childs Garden of Verses, wrap corruption: hall.she
        passage = (
            "The moon has a face like the clock in the hall;\n"
            "    She shines on thieves on the garden wall,\n"
            "    On streets and field and harbour quays,\n"
            "    And birdies asleep in the forks of the trees."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "hall.she" not in full_text

    def test_wrap_026_mouse_the(self):
        # Source: A Childs Garden of Verses, wrap corruption: mouse.the
        passage = (
            "The squalling cat and the squeaking mouse,\n"
            "    The howling dog by the door of the house,\n"
            "    The bat that lies in bed at noon,\n"
            "    All love to be out by the light of the moon."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "mouse.the" not in full_text

    def test_wrap_027_day_cuddle(self):
        # Source: A Childs Garden of Verses, wrap corruption: day.cuddle
        passage = (
            "But all of the things that belong to the day\n"
            "    Cuddle to sleep to be out of her way;\n"
            "    And flowers and children close their eyes\n"
            "    Till up in the morning the sun shall arise."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "day.cuddle" not in full_text

    def test_wrap_028_feet_here(self):
        # Source: A Childs Garden of Verses, wrap corruption: feet.here
        passage = (
            "Come up here, O dusty feet!\n"
            "      Here is fairy bread to eat.\n"
            "    Here in my retiring room,\n"
            "      Children, you may dine\n"
            "    On the golden smell of broom\n"
            "      And the shade of pine;\n"
            "    And when you have eaten well,\n"
            "    Fairy stories hear and tell."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "feet.here" not in full_text

    def test_wrap_029_sod_thick(self):
        # Source: A Childs Garden of Verses, wrap corruption: sod.thick
        passage = (
            "Black are my steps on silver sod;\n"
            "    Thick blows my frosty breath abroad;\n"
            "    And tree and house, and hill and lake,\n"
            "    Are frosted like a wedding-cake."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sod.thick" not in full_text

    def test_wrap_030_lawn_the(self):
        # Source: A Childs Garden of Verses, wrap corruption: lawn.the
        passage = (
            "To house and garden, field and lawn,\n"
            "    The meadow-gates we swang upon,\n"
            "    To pump and stable, tree and swing,\n"
            "    Good-bye, good-bye, to everything!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lawn.the" not in full_text

    def test_wrap_031_drum_with(self):
        # Source: A Childs Garden of Verses, wrap corruption: drum.with
        passage = (
            "Now my little heart goes a-beating like a drum,\n"
            "    With the breath of the Bogie in my hair;\n"
            "    And all round the candle the crooked shadows come,\n"
            "    And go marching along up the stair."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "drum.with" not in full_text

    def test_wrap_032_lamp_the(self):
        # Source: A Childs Garden of Verses, wrap corruption: lamp.the
        passage = (
            "The shadow of the balusters, the shadow of the lamp,\n"
            "      The shadow of the child that goes to bed--\n"
            "    All the wicked shadows coming, tramp, tramp, tramp,\n"
            "      With the black night overhead."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lamp.the" not in full_text

    def test_wrap_033_saw_his(self):
        # Source: A Childs Garden of Verses, wrap corruption: saw.his
        passage = (
            "Nobody heard him and nobody saw,\n"
            "    His is a picture you never could draw,\n"
            "    But he's sure to be present, abroad or at home,\n"
            "    When children are happy and playing alone."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "saw.his" not in full_text

    def test_wrap_034_big_tis(self):
        # Source: A Childs Garden of Verses, wrap corruption: big.tis
        passage = (
            "He loves to be little, he hates to be big,\n"
            "    'Tis he that inhabits the caves that you dig;\n"
            "    'Tis he when you play with your soldiers of tin\n"
            "    That sides with the Frenchmen and never can win."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "big.tis" not in full_text

    def test_wrap_035_bed_bids(self):
        # Source: A Childs Garden of Verses, wrap corruption: bed.bids
        passage = (
            "'Tis he, when at night you go off to your bed,\n"
            "    Bids you go to your sleep and not trouble your head;\n"
            "    For wherever they're lying, in cupboard or shelf,\n"
            "    'Tis he will take care of your playthings himself!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bed.bids" not in full_text

    def test_wrap_036_helm_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: helm.and
        passage = (
            "For I mean to grow as little as the dolly at the helm,\n"
            "      And the dolly I intend to come alive;\n"
            "    And with him beside to help me, it's a-sailing I shall go,\n"
            "    It's a-sailing on the water, when the jolly breezes blow\n"
            "      And the vessel goes a divie-divie-dive."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "helm.and" not in full_text

    def test_wrap_037_reeds_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: reeds.and
        passage = (
            "O it's then you'll see me sailing through the rushes and the reeds,\n"
            "      And you'll hear the water singing at the prow;\n"
            "    For beside the dolly sailor, I'm to voyage and explore,\n"
            "    To land upon the island where no dolly was before,\n"
            "      And to fire the penny cannon in the bow."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "reeds.and" not in full_text

    def test_wrap_038_sea_the(self):
        # Source: A Childs Garden of Verses, wrap corruption: sea.the
        passage = (
            "I called the little pool a sea;\n"
            "    The little hills were big to me;\n"
            "      For I am very small.\n"
            "    I made a boat, I made a town,\n"
            "    I searched the caverns up and down,\n"
            "      And named them one and all."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sea.the" not in full_text

    def test_wrap_039_said_the(self):
        # Source: A Childs Garden of Verses, wrap corruption: said.the
        passage = (
            "And all about was mine, I said,\n"
            "    The little sparrows overhead,\n"
            "      The little minnows too.\n"
            "    This was the world and I was king;\n"
            "    For me the bees came by to sing,\n"
            "      For me the swallows flew."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "said.the" not in full_text

    def test_wrap_040_seas_nor(self):
        # Source: A Childs Garden of Verses, wrap corruption: seas.nor
        passage = (
            "I played there were no deeper seas,\n"
            "    Nor any wider plains than these,\n"
            "      Nor other kings than me.\n"
            "    At last I heard my mother call\n"
            "    Out from the house at evenfall,\n"
            "      To call me home to tea."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "seas.nor" not in full_text

    def test_wrap_041_dell_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: dell.and
        passage = (
            "And I must rise and leave my dell,\n"
            "    And leave my dimpled water well,\n"
            "      And leave my heather blooms.\n"
            "    Alas! and as my home I neared,\n"
            "    How very big my nurse appeared.\n"
            "      How great and cool the rooms!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dell.and" not in full_text

    def test_wrap_042_nest_where(self):
        # Source: A Childs Garden of Verses, wrap corruption: nest.where
        passage = (
            "These nuts, that I keep in the back of the nest\n"
            "    Where all my lead soldiers are lying at rest,\n"
            "    Were gathered in autumn by nursie and me\n"
            "    In a wood with a well by the side of the sea."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "nest.where" not in full_text

    def test_wrap_043_king_for(self):
        # Source: A Childs Garden of Verses, wrap corruption: king.for
        passage = (
            "But of all my treasures the last is the king,\n"
            "    For there's very few children possess such a thing;\n"
            "    And that is a chisel, both handle and blade,\n"
            "    Which a man who was really a carpenter made."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "king.for" not in full_text

    def test_wrap_044_blocks_castles(self):
        # Source: A Childs Garden of Verses, wrap corruption: blocks.castles
        passage = (
            "What are you able to build with your blocks?\n"
            "    Castles and palaces, temples and docks.\n"
            "    Rain may keep raining, and others go roam,\n"
            "    But I can be happy and building at home."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "blocks.castles" not in full_text

    def test_wrap_045_sea_there(self):
        # Source: A Childs Garden of Verses, wrap corruption: sea.there
        passage = (
            "Let the sofa be mountains, the carpet be sea,\n"
            "    There I'll establish a city for me:\n"
            "    A kirk and a mill and a palace beside,\n"
            "    And a harbour as well where my vessels may ride."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sea.there" not in full_text

    def test_wrap_046_moored_hark(self):
        # Source: A Childs Garden of Verses, wrap corruption: moored.hark
        passage = (
            "This one is sailing and that one is moored:\n"
            "    Hark to the song of the sailors on board!\n"
            "    And see, on the steps of my palace, the kings\n"
            "    Coming and going with presents and things!"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "moored.hark" not in full_text

    def test_wrap_047_again_the(self):
        # Source: A Childs Garden of Verses, wrap corruption: again.the
        passage = (
            "Yet as I saw it, I see it again,\n"
            "    The kirk and the palace, the ships and the men,\n"
            "    And as long as I live and where'er I may be,\n"
            "    I'll always remember my town by the sea."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "again.the" not in full_text

    def test_wrap_048_woods_these(self):
        # Source: A Childs Garden of Verses, wrap corruption: woods.these
        passage = (
            "These are the hills, these are the woods,\n"
            "    These are my starry solitudes;\n"
            "    And there the river by whose brink\n"
            "    The roaring lions come to drink."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "woods.these" not in full_text

    def test_wrap_049_sit_and(self):
        # Source: A Childs Garden of Verses, wrap corruption: sit.and
        passage = (
            "When at home alone I sit,\n"
            "    And am very tired of it,\n"
            "    I have just to shut my eyes\n"
            "    To go sailing through the skies--\n"
            "    To go sailing far away\n"
            "    To the pleasant Land of Play;\n"
            "    To the fairy land afar\n"
            "    Where the Little People are;\n"
            "    Where the clover-tops are trees,\n"
            "    And the rain-pools are the seas,\n"
            "    And the leaves, like little ships,\n"
            "    Sail about on tiny trips;\n"
            "    And above the daisy tree\n"
            "      Through the grasses,\n"
            "    High o'erhead the Bumble Bee\n"
            "      Hums and passes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sit.and" not in full_text

    def test_wrap_050_pass_till(self):
        # Source: A Childs Garden of Verses, wrap corruption: pass.till
        passage = (
            "Through that forest I can pass\n"
            "    Till, as in a looking-glass,\n"
            "    Humming fly and daisy tree\n"
            "    And my tiny self I see,\n"
            "    Painted very clear and neat\n"
            "    On the rain-pool at my feet.\n"
            "    Should a leaflet come to land\n"
            "    Drifting near to where I stand,\n"
            "    Straight I'll board that tiny boat\n"
            "    Round the rain-pool sea to float."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pass.till" not in full_text

    def test_wrap_051_again_open(self):
        # Source: A Childs Garden of Verses, wrap corruption: again.open
        passage = (
            "When my eyes I once again\n"
            "      Open, and see all things plain:\n"
            "    High bare walls, great bare floor;\n"
            "    Great big knobs on drawer and door;\n"
            "    Great big people perched on chairs,\n"
            "    Stitching tucks and mending tears,\n"
            "    Each a hill that I could climb,\n"
            "    And talking nonsense all the time--\n"
            "      O dear me,\n"
            "      That I could be\n"
            "    A sailor on the rain-pool sea,\n"
            "    A climber in the clover tree,\n"
            "    And just come back, a sleepy-head,\n"
            "    Late at night to go to bed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "again.open" not in full_text

    def test_wrap_052_goes_through(self):
        # Source: A Childs Garden of Verses, wrap corruption: goes.through
        passage = (
            "Great is the sun, and wide he goes\n"
            "    Through empty heaven without repose;\n"
            "    And in the blue and glowing days\n"
            "    More thick than rain he showers his rays."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "goes.through" not in full_text

    def test_wrap_053_blue_round(self):
        # Source: A Childs Garden of Verses, wrap corruption: blue.round
        passage = (
            "Above the hills, along the blue,\n"
            "    Round the bright air with footing true,\n"
            "    To please the child, to paint the rose,\n"
            "    The gardener of the World, he goes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "blue.round" not in full_text

    def test_wrap_054_blue_nor(self):
        # Source: A Childs Garden of Verses, wrap corruption: blue.nor
        passage = (
            "He digs the flowers, green, red, and blue,\n"
            "    Nor wishes to be spoken to.\n"
            "    He digs the flowers and cuts the hay,\n"
            "    And never seems to want to play."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "blue.nor" not in full_text

    def test_wrap_055_dear_far(self):
        # Source: A Childs Garden of Verses, wrap corruption: dear.far
        passage = (
            "Ah, far enough, my dear,\n"
            "    Far, far enough from here--\n"
            "    Yet you have farther gone!\n"
            "    \"Can I get there by candlelight?\"\n"
            "    So goes the old refrain.\n"
            "    I do not know--perchance you might--\n"
            "    But only, children, hear it right,\n"
            "    Ah, never to return again!\n"
            "    The eternal dawn, beyond a doubt,\n"
            "    Shall break on hill and plain,\n"
            "    And put all stars and candles out\n"
            "    Ere we be young again."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dear.far" not in full_text

