import pytest
from fast_sentence_segment import segment_text


class TestEbooksGalsworthy:
    """Integration tests mined from John Galsworthy ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1920s
    """

    def test_wrap_001_connie_trustaford(self):
        # Source: A Bit O Love, wrap corruption: connie.trustaford
        passage = (
            "As he speaks, GLADYS FREMAN, a dark gipsyish girl, and CONNIE\n"
            "     TRUSTAFORD, a fair, stolid, blue-eyed Saxon, both about sixteen,\n"
            "     come in through the front door, behind which they have evidently\n"
            "     been listening.  They too have prayer-books in their hands.\n"
            "     They sidle past Ivy, and also sit down under the window."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "connie.trustaford" not in full_text

    def test_wrap_002_and_taking(self):
        # Source: A Bit O Love, wrap corruption: and.taking
        passage = (
            "He turns to a book-case on a table against the far wall, and\n"
            "     taking out a book, finds his place in it.  While he stands thus\n"
            "     with his back to the girls, MERCY JARLAND comes in from the\n"
            "     green.  She also is about sixteen, with fair hair and china-blue\n"
            "     eyes.  She glides in quickly, hiding something behind her, and\n"
            "     sits down on the seat next the door.  And at once there is a\n"
            "     whispering."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.taking" not in full_text

    def test_wrap_003_over_her(self):
        # Source: A Bit O Love, wrap corruption: over.her
        passage = (
            "MERCY kicks afoot, sideways against her neighbour, frowns over\n"
            "     her china-blare eyes, is silent; then, as his question passes\n"
            "     on, makes a quick little face, wriggles, and looks behind her."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "over.her" not in full_text

    def test_wrap_004_tibby_comes(self):
        # Source: A Bit O Love, wrap corruption: tibby.comes
        passage = (
            "[Getting no reply from Tibby JARLAND, she passes out.  Tibby\n"
            "     comes in, looks round, takes a large sweet out of her mouth,\n"
            "     contemplates it, and puts it back again.  Then, in a perfunctory\n"
            "     and very stolid fashion, she looks about the floor, as if she\n"
            "     had been told to find something.  While she is finding nothing\n"
            "     and sucking her sweet, her sister MERCY comes in furtively,\n"
            "     still frowning and vindictive.]"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tibby.comes" not in full_text

    def test_wrap_005_turns_suddenly(self):
        # Source: A Bit O Love, wrap corruption: turns.suddenly
        passage = (
            "[Ivy looks at her as if she would speak again, then turns\n"
            "     suddenly, and goes out.  BEATRICE'S face darkens; she shivers.\n"
            "     Taking out a little cigarette case, she lights a cigarette, and\n"
            "     watches the puff's of smoke wreathe shout her and die away.  The\n"
            "     frightened MERCY peers out, spying for a chance, to escape.\n"
            "     Then from the house STRANGWAY comes in.  All his dreaminess is\n"
            "     gone.]"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "turns.suddenly" not in full_text

    def test_wrap_006_quickly_strangway(self):
        # Source: A Bit O Love, wrap corruption: quickly.strangway
        passage = (
            "[She passes him with her head down, and goes out quickly.\n"
            "     STRANGWAY stands unconsciously tearing at the little bird-cage.\n"
            "     And while he tears at it he utters a moaning sound.  The\n"
            "     terrified MERCY, peering from behind the curtain, and watching\n"
            "     her chance, slips to the still open door; but in her haste and\n"
            "     fright she knocks against it, and STRANGWAY sees her.  Before he\n"
            "     can stop her she has fled out on to the green and away.]"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "quickly.strangway" not in full_text

    def test_wrap_007_bar_with(self):
        # Source: A Bit O Love, wrap corruption: bar.with
        passage = (
            "About seven o'clock in the taproom of the village inn.  The bar,\n"
            "     with the appurtenances thereof, stretches across one end, and\n"
            "     opposite is the porch door on to the green.  The wall between is\n"
            "     nearly all window, with leaded panes, one wide-open casement\n"
            "     whereof lets in the last of the sunlight.  A narrow bench runs\n"
            "     under this broad window.  And this is all the furniture, save\n"
            "     three spittoons:"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "bar.with" not in full_text

    def test_wrap_008_dance_and(self):
        # Source: A Bit O Love, wrap corruption: dance.and
        passage = (
            "[TIBBY begins her drowsy beating, IVY hums the tune; they dance,\n"
            "     and their shadows dance again upon the walls.  When she has\n"
            "     beaten but a few moments on the tambourine, TIBBY is overcome\n"
            "     once more by sleep and falls back again into her nest of hay,\n"
            "     with her little shoed feet just visible over the edge of the\n"
            "     bench.  Ivy catches up the tambourine, and to her beating and\n"
            "     humming the dancers dance on.]"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dance.and" not in full_text

    def test_wrap_009_london_power(self):
        # Source: A Commentary, wrap corruption: london.power
        passage = (
            "“JUSTICE” APPEARED IN THE Albany Review (LONDON);\n"
            "           “POWER” IN THE New Age; ALL THE OTHER SKETCHES\n"
            "             IN THIS VOLUME HAVE APPEARED IN The Nation"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "london.power" not in full_text

    def test_wrap_010_day_scene(self):
        # Source: A Family Man in Three Acts, wrap corruption: day.scene
        passage = (
            "SCENE I. THE MAYOR'S Study.  10am the following day.\n"
            "        SCENE II.  BUILDER'S Study.  The same.  Noon.\n"
            "        SCENE III.  BUILDER'S Study.  The same.  Evening."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "day.scene" not in full_text

    def test_wrap_011_brokendown_cardboard(self):
        # Source: A Family Man in Three Acts, wrap corruption: brokendown.cardboard
        passage = (
            "As the curtain rises CAMILLE enters with a rather broken-down\n"
            "     cardboard box containing flowers.  She is a young woman with a good\n"
            "     figure, a pale face, the warm brown eyes and complete poise of a\n"
            "     Frenchwoman.  She takes the box to MRS BUILDER."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "brokendown.cardboard" not in full_text

    def test_wrap_012_camille_camille(self):
        # Source: A Family Man in Three Acts, wrap corruption: camille.camille
        passage = (
            "MRS BUILDER.  The blue vase, please, Camille.\n"
            "     CAMILLE fetches a vase.  MRS BUILDER puts the flowers into the vase.\n"
            "     CAMILLE gathers up the debris;  and with a glance at BUILDER goes\n"
            "     out."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "camille.camille" not in full_text

    def test_wrap_013_again_when(self):
        # Source: A Family Man in Three Acts, wrap corruption: again.when
        passage = (
            "BUILDER fills his second pipe.  He is just taking up the paper again\n"
            "     when the door from the hall is opened, and the manservant TOPPING,\n"
            "     dried, dark, sub-humorous, in a black cut-away, announces:"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "again.when" not in full_text

    def test_wrap_014_redfaced_lighteyed(self):
        # Source: A Family Man in Three Acts, wrap corruption: redfaced.lighteyed
        passage = (
            "THE MAYOR of Breconridge enters, He is clean-shaven, red-faced,\n"
            "     light-eyed, about sixty, shrewd, poll-parroty, naturally jovial,\n"
            "     dressed with the indefinable wrongness of a burgher; he is followed\n"
            "     by his Secretary HARRIS, a man all eyes and cleverness.  TOPPING\n"
            "     retires."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "redfaced.lighteyed" not in full_text

    def test_wrap_015_when_the(self):
        # Source: A Family Man in Three Acts, wrap corruption: when.the
        passage = (
            "He compresses his lips, and is settling back into his chair, when\n"
            "     the door from the hall is opened and his daughter MAUD comes in; a\n"
            "     pretty girl, rather pale, with fine eyes.  Though her face has a\n"
            "     determined cast her manner at this moment is by no means decisive.\n"
            "     She has a letter in her hand, and advances rather as if she were\n"
            "     stalking her father, who, after a \"Hallo, Maud!\" has begun to read\n"
            "     his paper."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "when.the" not in full_text

    def test_wrap_016_her_hands(self):
        # Source: A Family Man in Three Acts, wrap corruption: her.hands
        passage = (
            "He has disappeared, and she ends with an expressive movement of her\n"
            "     hands, a long sigh, and a closing of her eyes.  BUILDER'S peremptory\n"
            "     voice is heard: \"Julia!\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "her.hands" not in full_text

    def test_wrap_017_towards_the(self):
        # Source: A Family Man in Three Acts, wrap corruption: towards.the
        passage = (
            "MRS BUILDER has approached him, and they have both turned towards\n"
            "     the opening door.  GUY HERRINGHAME comes in.  They are a little out\n"
            "     of his line of sight, and he has shut the door before he sees them.\n"
            "     When he does, his mouth falls open, and his hand on to the knob of\n"
            "     the door.  He is a comely young man in Harris tweeds.  Moreover, he\n"
            "     is smoking.  He would speak if he could, but his surprise is too\n"
            "     excessive.  BUILDER.  Well, sir?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "towards.the" not in full_text

    def test_wrap_018_door_quickly(self):
        # Source: A Family Man in Three Acts, wrap corruption: door.quickly
        passage = (
            "MRS BUILDER, who has so far seemed to accompany him, shuts the door\n"
            "     quickly and remains in the studio.  She stands there with that faint\n"
            "     smile on her face, looking at the two young people."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "door.quickly" not in full_text

    def test_wrap_019_paper_into(self):
        # Source: A Family Man in Three Acts, wrap corruption: paper.into
        passage = (
            "BUILDER'S study.  At the table, MAUD has just put a sheet of paper\n"
            "     into a typewriter.  She sits facing the audience, with her hands\n"
            "     stretched over the keys."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "paper.into" not in full_text

    def test_wrap_020_sealingwax_and(self):
        # Source: A Family Man in Three Acts, wrap corruption: sealingwax.and
        passage = (
            "She opens an imaginary drawer, takes out some bits of sealing-wax,\n"
            "     and with every circumstance of stealth in face and hands, conceals\n"
            "     them in her bosom."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sealingwax.and" not in full_text

    def test_wrap_021_she_turns(self):
        # Source: A Family Man in Three Acts, wrap corruption: she.turns
        passage = (
            "As she turns he looks swiftly at her, sweeping her up and down.  She\n"
            "     turns her head and catches his glance, which is swiftly dropped.\n"
            "     Will Monsieur not 'ave anything to eat?"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "she.turns" not in full_text

    def test_wrap_022_following_towards(self):
        # Source: A Family Man in Three Acts, wrap corruption: following.towards
        passage = (
            "She goes through the doorway into the hall.  MRS BUILDER, following\n"
            "     towards the door, meets RALPH BUILDER, a man rather older than\n"
            "     BUILDER and of opposite build and manner.  He has a pleasant,\n"
            "     whimsical face and grizzled hair."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "following.towards" not in full_text

    def test_wrap_023_table_sits(self):
        # Source: A Family Man in Three Acts, wrap corruption: table.sits
        passage = (
            "He goes out, followed by BUILDER.  MAUD goes quickly to the table,\n"
            "     sits down and rests her elbows on it, her chin on her hands, looking\n"
            "     at the door."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "table.sits" not in full_text

    def test_wrap_024_sits_down(self):
        # Source: A Family Man in Three Acts, wrap corruption: sits.down
        passage = (
            "She pours it out, and he drinks it, hands her the glass and sits\n"
            "     down suddenly in an armchair.  CAMILLE puts the glass on a tray, and\n"
            "     looks for a box of matches from the mantelshelf."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sits.down" not in full_text

    def test_wrap_025_are_engaged(self):
        # Source: A Family Man in Three Acts, wrap corruption: are.engaged
        passage = (
            "She suddenly kisses him, and he returns the kiss.  While they are\n"
            "     engaged in this entrancing occupation, MRS BUILDER opens the door\n"
            "     from the hall, watches unseen for a few seconds, and quietly goes\n"
            "     out again."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "are.engaged" not in full_text

    def test_wrap_026_the_bureau(self):
        # Source: A Family Man in Three Acts, wrap corruption: the.bureau
        passage = (
            "HARRIS goes out Left.  The MAYOR takes the upper chair behind the\n"
            "     bureau, sitting rather higher because of the book than CHANTREY, who\n"
            "     takes the lower.  Now that they are in the seats of justice, a sort\n"
            "     of reticence falls on them, as if they were afraid of giving away\n"
            "     their attitudes of mind to some unseen presence."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.bureau" not in full_text

    def test_wrap_027_chairs_ralph(self):
        # Source: A Family Man in Three Acts, wrap corruption: chairs.ralph
        passage = (
            "HARRIS and HERRINGHAME succeed in placing the three women in chairs.\n"
            "     RALPH BUILDER also sits.  HERRINGHAME stands behind.  JOHN BUILDER\n"
            "     remains standing between the two POLICEMEN.  His face is unshaved\n"
            "     and menacing, but he stands erect staring straight at the MAYOR.\n"
            "     HARRIS goes to the side of the bureau, Back, to take down the\n"
            "     evidence."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "chairs.ralph" not in full_text

    def test_wrap_028_gone_swiftly(self):
        # Source: A Family Man in Three Acts, wrap corruption: gone.swiftly
        passage = (
            "While he is speaking the door has been opened, and HARRIS has gone\n"
            "     swiftly to it, spoken to someone and returned.  He leans forward to\n"
            "     the MAYOR."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "gone.swiftly" not in full_text

    def test_wrap_029_down_then(self):
        # Source: A Family Man in Three Acts, wrap corruption: down.then
        passage = (
            "The MAYOR nods and makes a gesture, so that MAUD and RALPH sit down;\n"
            "     then, leaning over, he confers in a low voice with CHANTREY.  The\n"
            "     rest all sit or stand exactly as if each was the only person in the\n"
            "     room, except the JOURNALIST, who is writing busily and rather\n"
            "     obviously making a sketch of BUILDER."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "down.then" not in full_text

    def test_wrap_030_are_exchanged(self):
        # Source: A Family Man in Three Acts, wrap corruption: are.exchanged
        passage = (
            "His uncontrollable laughter and the MAYOR'S rueful appreciation are\n"
            "     exchanged with lightning rapidity for a preternatural solemnity, as\n"
            "     the door opens, admitting SERGEANT MARTIN and the lugubrious object\n"
            "     of their next attentions."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "are.exchanged" not in full_text

    def test_wrap_031_builder_standing(self):
        # Source: A Family Man in Three Acts, wrap corruption: builder.standing
        passage = (
            "They have not seen the door opened from the hall, and BUILDER\n"
            "     standing there.  He is still unshaven, a little sunken in the face,\n"
            "     with a glum, glowering expression.  He has a document in his hand.\n"
            "     He advances a step or two and they see him."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "builder.standing" not in full_text

    def test_wrap_032_his_brothers(self):
        # Source: A Family Man in Three Acts, wrap corruption: his.brothers
        passage = (
            "RALPH BUILDER stands gazing with whimsical commiseration at his\n"
            "     brother's back.  As BUILDER finishes writing, he goes up and puts\n"
            "     his hand on his brother's shoulder."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "his.brothers" not in full_text

    def test_wrap_033_door_opens(self):
        # Source: A Family Man in Three Acts, wrap corruption: door.opens
        passage = (
            "BUILDER remains staring in front of him.  The dining-room door\n"
            "     opens, and CAMILLE's head is thrust in.  Seeing him, she draws back,\n"
            "     but he catches sight of her."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "door.opens" not in full_text

    def test_wrap_034_glum_laugh(self):
        # Source: A Family Man in Three Acts, wrap corruption: glum.laugh
        passage = (
            "She turns swiftly and goes out.  BUILDER again utters his glum\n"
            "     laugh.  And then, as he sits alone staring before him, perfect\n"
            "     silence reigns in the room.  Over the window-sill behind him a BOY'S\n"
            "     face is seen to rise; it hangs there a moment with a grin spreading\n"
            "     on it."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "glum.laugh" not in full_text

    def test_wrap_035_still_open(self):
        # Source: A Family Man in Three Acts, wrap corruption: still.open
        passage = (
            "BUILDER's study is dim and neglected-looking; the window is still\n"
            "     open, though it has become night.  A street lamp outside shines in,\n"
            "     and the end of its rays fall on BUILDER asleep.  He is sitting in a\n"
            "     high chair at the fireside end of the writing-table, with his elbows\n"
            "     on it, and his cheek resting on his hand.  He is still unshaven, and\n"
            "     his clothes unchanged.  A Boy's head appears above the level of the\n"
            "     window-sill, as if beheaded and fastened there."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "still.open" not in full_text

    def test_wrap_036_raising_his(self):
        # Source: A Family Man in Three Acts, wrap corruption: raising.his
        passage = (
            "BUILDER stirs uneasily.  The Boy's head vanishes.  BUILDER, raising\n"
            "     his other hand, makes a sweep before his face, as if to brush away a\n"
            "     mosquito.  He wakes.  Takes in remembrance, and sits a moment\n"
            "     staring gloomily before him.  The door from the hall is opened and\n"
            "     TOPPING comes in with a long envelope in his hand."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "raising.his" not in full_text

    def test_wrap_037_table_opens(self):
        # Source: A Family Man in Three Acts, wrap corruption: table.opens
        passage = (
            "TOPPING withdraws.  BUILDER turns up a standard lamp on the table,\n"
            "     opens the envelope, and begins reading the galley slip.  The signs\n"
            "     of uneasiness and discomfort grow on him."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "table.opens" not in full_text

    def test_wrap_038_the_windowsill(self):
        # Source: A Family Man in Three Acts, wrap corruption: the.windowsill
        passage = (
            "The Boy's head is again seen rising above the level of the\n"
            "     window-sill, and another and another follows, till the three,\n"
            "     as if decapitated, heads are seen in a row."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.windowsill" not in full_text

    def test_wrap_039_disappear_and(self):
        # Source: A Family Man in Three Acts, wrap corruption: disappear.and
        passage = (
            "BUILDER rises, turns and stares at them.  The THREE HEADS disappear,\n"
            "     and a Boy's voice cries shrilly:  \"Johnny Builder!\"  BUILDER moves\n"
            "     towards the window; voices are now crying in various pitches and\n"
            "     keys: \"Johnny Builder!\"  \"Beatey Builder!\"  \"Beat 'is wife-er!\"\n"
            "     \"Beatey Builder!\""
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "disappear.and" not in full_text

    def test_wrap_040_lamp_lighting(self):
        # Source: A Family Man in Three Acts, wrap corruption: lamp.lighting
        passage = (
            "BUILDER stands quite motionless, staring, with the street lamp\n"
            "     lighting up a queer, rather pitiful defiance on his face.  The\n"
            "     voices swell.  There comes a sudden swish and splash of water, and\n"
            "     broken yells of dismay."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lamp.lighting" not in full_text

    def test_wrap_041_and_applies(self):
        # Source: A Family Man in Three Acts, wrap corruption: and.applies
        passage = (
            "While TOPPING lights the fire BUILDER puts the pipe in his mouth and\n"
            "     applies a match to it.  TOPPING, having lighted the fire, turns to\n"
            "     go, gets as far as half way, then comes back level with the table\n"
            "     and regards the silent brooding figure in the chair."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "and.applies" not in full_text

    def test_wrap_042_the_firelight(self):
        # Source: A Family Man in Three Acts, wrap corruption: the.firelight
        passage = (
            "TOPPING has gone.  BUILDER sits drawing at his pipe between the\n"
            "     firelight and the light from the standard lamp.  He takes the pipe\n"
            "     out of his mouth and a quiver passes over his face.  With a half\n"
            "     angry gesture he rubs the back of his hand across his eyes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.firelight" not in full_text

    def test_wrap_043_good_intentions(self):
        # Source: A Sheaf, wrap corruption: good.intentions
        passage = (
            "Inspection of private slaughter-houses, in spite of all the good\n"
            "    intentions of local authorities and medical officers, admitted\n"
            "    to be very inefficient in so far as condition of meat and method\n"
            "    of slaughter are concerned."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "good.intentions" not in full_text

    def test_wrap_044_the_present(self):
        # Source: A Sheaf, wrap corruption: the.present
        passage = (
            "Supervision of public slaughter-houses much hampered by the\n"
            "    present widespread custom of allowing butchers to send in their\n"
            "    beasts with their own slaughtermen."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.present" not in full_text

    def test_wrap_045_slaughter_model(self):
        # Source: A Sheaf, wrap corruption: slaughter.model
        passage = (
            "No general statutory regulations as to method of slaughter.\n"
            "    Model by-laws have been drawn up by the Local Government Board\n"
            "    and recommended to local authorities—but they are not\n"
            "    compulsory and have been as yet but sparsely adopted."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "slaughter.model" not in full_text

    def test_wrap_046_slaughterh_directly(self):
        # Source: A Sheaf, wrap corruption: slaughterhouses.directly
        passage = (
            "Slaughtermen not licensed; nor—except in slaughterhouses\n"
            "    directly controlled by a Government Department (such as the\n"
            "    Admiralty)—required by law to be proficient before they\n"
            "    commence slaughtering."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "slaughterhouses.directly" not in full_text

    def test_wrap_047_humanekill_can(self):
        # Source: A Sheaf, wrap corruption: humanekiller.can
        passage = (
            "“At the present time the Board understand that a ‘humane-killer’\n"
            "    can be got which is adapted for stunning any kind of animal,\n"
            "    reasonable in cost, and effective and simple in operation. It\n"
            "    appears, too, that the use of the improved instruments can\n"
            "    readily be learnt, so that no prolonged training is needed for\n"
            "    their proper manipulation.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "humanekiller.can" not in full_text

    def test_wrap_048_ones_and(self):
        # Source: A Sheaf, wrap corruption: ones.and
        passage = (
            "“I, with another witness, saw five pigs killed—three small ones\n"
            "    and two large ones. The pigs were ‘knifed’ one at a time and\n"
            "    allowed to wander round the slaughter-house bleeding and in a\n"
            "    drunken, reeling, rolling state, and at the same time uttering\n"
            "    most plaintive cries.” (From a letter to a daily journal.)"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ones.and" not in full_text

    def test_wrap_049_chain_fastened(self):
        # Source: A Sheaf, wrap corruption: chain.fastened
        passage = (
            "“First the animals are hung up alive head downwards by a chain\n"
            "    fastened to a hind foot, and then they are stuck and bleed to\n"
            "    death. The work is done quickly in a collective sense—at the\n"
            "    rate possibly of 100 to 200 pigs an hour, but each individual\n"
            "    pig suffers from forty seconds to two or three minutes, and\n"
            "    several pigs struggle and shriek at the same time.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "chain.fastened" not in full_text

    def test_wrap_050_pigs_without(self):
        # Source: A Sheaf, wrap corruption: pigs.without
        passage = (
            "(a) All animals (cattle, calves, sheep, lambs, and pigs)\n"
            "    without exception must be stunned or otherwise rendered\n"
            "    unconscious before blood is drawn."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pigs.without" not in full_text

    def test_wrap_051_they_cannot(self):
        # Source: A Sheaf, wrap corruption: they.cannot
        passage = (
            "(b) Animals awaiting slaughter must be so placed that they\n"
            "    cannot see into the slaughter-house, and the doors of the latter\n"
            "    must be kept closed while slaughtering is going on."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "they.cannot" not in full_text

    def test_wrap_052_arranged_that(self):
        # Source: A Sheaf, wrap corruption: arranged.that
        passage = (
            "(c) The drainage of the slaughter-house must be so arranged\n"
            "    that no blood or other refuse can flow out within the sight or\n"
            "    smell of animals awaiting slaughter, and no such refuse shall\n"
            "    be deposited in proximity to the waiting pens."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "arranged.that" not in full_text

    def test_wrap_053_deform_and(self):
        # Source: A Sheaf, wrap corruption: deform.and
        passage = (
            "“From the influence of a vile and unbecoming custom you deform\n"
            "    and mutilate your horses. . . . You cut off their tails; and\n"
            "    when you enjoy them uninjured and perfect, you choose rather to\n"
            "    maim and blemish them, so as to make them odious and disgustful\n"
            "    objects to all who see them. . . . This you are admonished to\n"
            "    renounce.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "deform.and" not in full_text

    def test_wrap_054_the_opinion(self):
        # Source: A Sheaf, wrap corruption: the.opinion
        passage = (
            "“The evidence has been such as to show conclusively, in the\n"
            "    opinion of the Committee, that not only are birds of many\n"
            "    species slaughtered recklessly, but also that the methods\n"
            "    employed for slaughter are such as in many cases, and especially\n"
            "    in that of egrets, to involve the destruction of the young birds\n"
            "    and eggs."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.opinion" not in full_text

    def test_wrap_055_the_reference(self):
        # Source: A Sheaf, wrap corruption: the.reference
        passage = (
            "76. “In the consideration of several matters contained in the\n"
            "    reference we had to touch upon the practice of confining\n"
            "    convicts for nine months’” (now, 1909, three, six or nine)\n"
            "    “solitary imprisonment either in local or convict prisons. . . .\n"
            "    The history of it is interesting and suggestive. It was\n"
            "    originated in 1842 by Sir James Graham, then Home\n"
            "    Secretary. . . . We shall show how complete a change in the\n"
            "    apparent object of the practice has since occurred.”"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "the.reference" not in full_text

