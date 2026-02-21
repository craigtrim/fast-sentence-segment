import pytest
from fast_sentence_segment import segment_text


class TestEbooksMeredith:
    """Integration tests mined from George Meredith ebooks.

    Each test passes a raw hard-wrapped passage to segment_text() and
    asserts that no word-boundary corruption (word.word) appears in the output.
    Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
    Decade: 1870s
    """

    def test_wrap_001_knees_homage(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: knees.homage
        passage = (
            "Youth must offer on bent knees\n"
            "   Homage unto one or other;\n"
            "   Earth, the mother,\n"
            "   This decrees;\n"
            "   And unto the pallid Scyther\n"
            "   Either points us shun we either\n"
            "   Shun or too devoutly follow."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "knees.homage" not in full_text

    def test_wrap_002_weaves_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: weaves.the
        passage = (
            "The rapture shed the torture weaves;\n"
            "   The direst blow on human heart she deals:\n"
            "   The pain to know the seen deceives;\n"
            "   Nought true but what insufferably feels.\n"
            "   And stabs of her delicious note,\n"
            "   That is as heavenly light to hearing, heard\n"
            "   Through shelter leaves, the laughter from her throat,\n"
            "   We answer as the midnight's morning's bird."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "weaves.the" not in full_text

    def test_wrap_003_ear_when(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: ear.when
        passage = (
            "Quickened of Nature's eye and ear,\n"
            "   When the wild sap at high tide smites\n"
            "   Within us; or benignly clear\n"
            "   To vision; or as the iris lights\n"
            "   On fluctuant waters; she is ours\n"
            "   Till set of man: the dreamed, the seen;\n"
            "   Flushing the world with odorous flowers:\n"
            "   A soft compulsion on terrene\n"
            "   By heavenly: and the world is hers\n"
            "   While hunger after Beauty spurs."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ear.when" not in full_text

    def test_wrap_004_sprang_ethereal(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: sprang.ethereal
        passage = (
            "That quiet dawn was Reverence; whereof sprang\n"
            "   Ethereal Beauty in full morningtide.\n"
            "   Another sun had risen to clasp his bride:\n"
            "   It was another earth unto him sang."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sprang.ethereal" not in full_text

    def test_wrap_005_heights_from(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: heights.from
        passage = (
            "Came Reverence from the Huntress on her heights?\n"
            "   From the Persuader came it, in those vales\n"
            "   Whereunto she melodiously invites,\n"
            "   Her troops of eager servitors regales?\n"
            "   Not far those two great Powers of Nature speed\n"
            "   Disciple steps on earth when sole they lead;\n"
            "   Nor either points for us the way of flame.\n"
            "   From him predestined mightier it came;\n"
            "   His task to hold them both in breast, and yield\n"
            "   Their dues to each, and of their war be field."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "heights.from" not in full_text

    def test_wrap_006_ceased_must(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: ceased.must
        passage = (
            "The foes that in repulsion never ceased,\n"
            "   Must he, who once has been the goodly beast\n"
            "   Of one or other, at whose beck he ran,\n"
            "   Constrain to make him serviceable man;\n"
            "   Offending neither, nor the natural claim\n"
            "   Each pressed, denying, for his true man's name."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "ceased.must" not in full_text

    def test_wrap_007_aid_might(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: aid.might
        passage = (
            "He drank of fictions, till celestial aid\n"
            "   Might seem accorded when he fawned and prayed;\n"
            "   Sagely the generous Giver circumspect,\n"
            "   To choose for grants the egregious, his elect;\n"
            "   And ever that imagined succour slew\n"
            "   The soul of brotherhood whence Reverence drew."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "aid.might" not in full_text

    def test_wrap_008_founts_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: founts.the
        passage = (
            "In fellowship religion has its founts:\n"
            "   The solitary his own God reveres:\n"
            "   Ascend no sacred Mounts\n"
            "   Our hungers or our fears.\n"
            "   As only for the numbers Nature's care\n"
            "   Is shown, and she the personal nothing heeds,\n"
            "   So to Divinity the spring of prayer\n"
            "   From brotherhood the one way upward leads.\n"
            "   Like the sustaining air\n"
            "   Are both for flowers and weeds.\n"
            "   But he who claims in spirit to be flower,\n"
            "   Will find them both an air that doth devour."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "founts.the" not in full_text

    def test_wrap_009_implored_external(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: implored.external
        passage = (
            "Whereby he smelt his treason, who implored\n"
            "   External gifts bestowed but on the sword;\n"
            "   Beheld himself, with less and less disguise,\n"
            "   Through those blood-cataracts which dimmed his eyes,\n"
            "   His army's foe, condemned to strive and fail;\n"
            "   See a black adversary's ghost prevail;\n"
            "   Never, though triumphs hailed him, hope to win\n"
            "   While still the conflict tore his breast within."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "implored.external" not in full_text

    def test_wrap_010_those_imprisoned(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: those.imprisoned
        passage = (
            "Out of that agony, misread for those\n"
            "   Imprisoned Powers warring unappeased,\n"
            "   The ghost of his black adversary rose,\n"
            "   To smother light, shut heaven, show earth diseased.\n"
            "   And long with him was wrestling ere emerged\n"
            "   A mind to read in him the reflex shade\n"
            "   Of its fierce torment; this way, that way urged;\n"
            "   By craven compromises hourly swayed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "those.imprisoned" not in full_text

    def test_wrap_011_untried_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: untried.the
        passage = (
            "Crouched as a nestling, still its wings untried,\n"
            "   The man's mind opened under weight of cloud.\n"
            "   To penetrate the dark was it endowed;\n"
            "   Stood day before a vision shooting wide.\n"
            "   Whereat the spectral enemy lost form;\n"
            "   The traversed wilderness exposed its track.\n"
            "   He felt the far advance in looking back;\n"
            "   Thence trust in his foot forward through the storm."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "untried.the" not in full_text

    def test_wrap_012_destroy_this(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: destroy.this
        passage = (
            "This man, this hero, works not to destroy;\n"
            "   This godlike--as the rock in ocean stands;--\n"
            "   He of the myriad eyes, the myriad hands\n"
            "   Creative; in his edifice has joy.\n"
            "   How strength may serve for purity is shown\n"
            "   When he himself can scourge to make it clean.\n"
            "   Withal his pitch of pride would not disown\n"
            "   A sober world that walks the balanced mean\n"
            "   Between its tempters, rarely overthrown:\n"
            "   And such at times his army's march has been."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "destroy.this" not in full_text

    def test_wrap_013_thought_each(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: thought.each
        passage = (
            "Near is he to great Nature in the thought\n"
            "   Each changing Season intimately saith,\n"
            "   That nought save apparition knows the death;\n"
            "   To the God-lighted mind of man 'tis nought.\n"
            "   She counts not loss a word of any weight;\n"
            "   It may befal his passions and his greeds\n"
            "   To lose their treasures, like the vein that bleeds,\n"
            "   But life gone breathless will she reinstate."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thought.each" not in full_text

    def test_wrap_014_beats_when(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: beats.when
        passage = (
            "Close on the heart of Earth his bosom beats,\n"
            "   When he the mandate lodged in it obeys,\n"
            "   Alive to breast a future wrapped in haze,\n"
            "   Strike camp, and onward, like the wind's cloud-fleets.\n"
            "   Unresting she, unresting he, from change\n"
            "   To change, as rain of cloud, as fruit of rain;\n"
            "   She feels her blood-tree throbbing in her grain,\n"
            "   Yet skyward branched, with loftier mark and range."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "beats.when" not in full_text

    def test_wrap_015_clod_she(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: clod.she
        passage = (
            "No miracle the sprout of wheat from clod,\n"
            "   She knows, nor growth of man in grisly brute;\n"
            "   But he, the flower at head and soil at root,\n"
            "   Is miracle, guides he the brute to God.\n"
            "   And that way seems he bound; that way the road,\n"
            "   With his dark-lantern mind, unled, alone,\n"
            "   Wearifully through forest-tracts unsown,\n"
            "   He travels, urged by some internal goad."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "clod.she" not in full_text

    def test_wrap_016_preserves_between(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: preserves.between
        passage = (
            "'Tis that in each recovery he preserves,\n"
            "   Between his upper and his nether wit,\n"
            "   Sense of his march ahead, more brightly lit;\n"
            "   He less the shaken thing of lusts and nerves;\n"
            "   With such a grasp upon his brute as tells\n"
            "   Of wisdom from that vile relapsing spun.\n"
            "   A Sun goes down in wasted fire, a Sun\n"
            "   Resplendent springs, to faith refreshed compels."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "preserves.between" not in full_text

    def test_wrap_017_shroud_all(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: shroud.all
        passage = (
            "AWAKES for me and leaps from shroud\n"
            "   All radiantly the moon's own night\n"
            "   Of folded showers in streamer cloud;\n"
            "   Our shadows down the highway white\n"
            "   Or deep in woodland woven-boughed,\n"
            "   With yon and yon a stem alight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "shroud.all" not in full_text

    def test_wrap_018_tale_was(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: tale.was
        passage = (
            "To either then an untold tale\n"
            "   Was Life, and author, hero, we.\n"
            "   The chapters holding peaks to scale,\n"
            "   Or depths to fathom, made our glee;\n"
            "   For we were armed of inner fires,\n"
            "   Unbled in us the ripe desires;\n"
            "   And passion rolled a quiet sea,\n"
            "   Whereon was Love the phantom sail."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "tale.was" not in full_text

    def test_wrap_019_attain_which(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: attain.which
        passage = (
            "UNTO that love must we through fire attain,\n"
            "      Which those two held as breath of common air;\n"
            "      The hands of whom were given in bond elsewhere;\n"
            "   Whom Honour was untroubled to restrain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "attain.which" not in full_text

    def test_wrap_020_met_and(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: met.and
        passage = (
            "Midway the road of our life's term they met,\n"
            "      And one another knew without surprise;\n"
            "      Nor cared that beauty stood in mutual eyes;\n"
            "   Nor at their tardy meeting nursed regret."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "met.and" not in full_text

    def test_wrap_021_found_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: found.the
        passage = (
            "To them it was revealed how they had found\n"
            "      The kindred nature and the needed mind;\n"
            "      The mate by long conspiracy designed;\n"
            "   The flower to plant in sanctuary ground."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "found.the" not in full_text

    def test_wrap_022_solicitude_for(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: solicitude.for
        passage = (
            "Avowed in vigilant solicitude\n"
            "      For either, what most lived within each breast\n"
            "      They let be seen: yet every human test\n"
            "   Demanding righteousness approved them good."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "solicitude.for" not in full_text

    def test_wrap_023_feared_abandonmen(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: feared.abandonment
        passage = (
            "She leaned on a strong arm, and little feared\n"
            "      Abandonment to help if heaved or sank\n"
            "      Her heart at intervals while Love looked blank,\n"
            "   Life rosier were she but less revered."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "feared.abandonment" not in full_text

    def test_wrap_024_obscure_her(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: obscure.her
        passage = (
            "An arm that never shook did not obscure\n"
            "      Her woman's intuition of the bliss--\n"
            "      Their tempter's moment o'er the black abyss,\n"
            "   Across the narrow plank--he could abjure."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "obscure.her" not in full_text

    def test_wrap_025_thread_and(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: thread.and
        passage = (
            "Then came a day that clipped for him the thread,\n"
            "      And their first touch of lips, as he lay cold,\n"
            "      Was all of earthly in their love untold,\n"
            "   Beyond all earthly known to them who wed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "thread.and" not in full_text

    def test_wrap_026_dry_and(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: dry.and
        passage = (
            "THEY have no song, the sedges dry,\n"
            "         And still they sing.\n"
            "   It is within my breast they sing,\n"
            "         As I pass by.\n"
            "   Within my breast they touch a string,\n"
            "         They wake a sigh.\n"
            "   There is but sound of sedges dry;\n"
            "   In me they sing."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "dry.and" not in full_text

    def test_wrap_027_sinks_lifes(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: sinks.lifes
        passage = (
            "Lustrous momently, near on earth she sinks;\n"
            "   Life's full throb over breathless and abased:\n"
            "   Yet stand they, though impalpable the links,\n"
            "   One, more one than the bridally embraced."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sinks.lifes" not in full_text

    def test_wrap_028_know_thy(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: know.thy
        passage = (
            "IF that thou hast the gift of strength, then know\n"
            "   Thy part is to uplift the trodden low;\n"
            "   Else in a giant's grasp until the end\n"
            "   A hopeless wrestler shall thy soul contend."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "know.thy" not in full_text

    def test_wrap_029_omission_frown(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: omission.frown
        passage = (
            "SEEN, too clear and historic within us, our sins of omission\n"
            "      Frown when the Autumn days strike us all ruthlessly bare.\n"
            "   They of our mortal diseases find never healing physician;\n"
            "      Errors they of the soul, past the one hope to repair."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "omission.frown" not in full_text

    def test_wrap_030_scattered_seed(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: scattered.seed
        passage = (
            "Sunshine might we have been unto seed under soil, or have scattered\n"
            "      Seed to ascendant suns brighter than any that shone.\n"
            "   Even the limp-legged beggar a sick desperado has flattered\n"
            "      Back to a half-sloughed life cheered by the mere human tone."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "scattered.seed" not in full_text

    def test_wrap_031_well_that(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: well.that
        passage = (
            "Beneath them throbs an urgent well,\n"
            "   That here is play, and there is war.\n"
            "   I know not which had most to tell\n"
            "   Of whence we spring and what we are."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "well.that" not in full_text

    def test_wrap_032_fear_while(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: fear.while
        passage = (
            "More intimate became the forest fear\n"
            "      While pillared darkness hatched malicious life\n"
            "      At either elbow, wolf or gnome or knife\n"
            "   And wary slid the glance from ear to ear."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "fear.while" not in full_text

    def test_wrap_033_lanternray_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: lanternray.the
        passage = (
            "In chillness, like a clouded lantern-ray,\n"
            "      The forest's heart of fog on mossed morass,\n"
            "      On purple pool and silky cotton-grass,\n"
            "   Revealed where lured the swallower byway."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lanternray.the" not in full_text

    def test_wrap_034_rebound_off(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: rebound.off
        passage = (
            "Dead outlook, flattened back with hard rebound\n"
            "      Off walls of distance, left each mounted height.\n"
            "      It seemed a giant hag-fiend, churning spite\n"
            "   Of humble human being, held the ground."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "rebound.off" not in full_text

    def test_wrap_035_slow_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: slow.the
        passage = (
            "Through friendless wastes, through treacherous woodland, slow\n"
            "      The feet sustained by track of feet pursued\n"
            "      Pained steps, and found the common brotherhood\n"
            "   By sign of Heaven indifferent, Nature foe."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "slow.the" not in full_text

    def test_wrap_036_sight_and(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: sight.and
        passage = (
            "Anon a mason's work amazed the sight,\n"
            "      And long-frocked men, called Brothers, there abode.\n"
            "      They pointed up, bowed head, and dug and sowed;\n"
            "   Whereof was shelter, loaf, and warm firelight."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "sight.and" not in full_text

    def test_wrap_037_head_benignant(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: head.benignant
        passage = (
            "What words they taught were nails to scratch the head.\n"
            "      Benignant works explained the chanting brood.\n"
            "      Their monastery lit black solitude,\n"
            "   As one might think a star that heavenward led."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "head.benignant" not in full_text

    def test_wrap_038_feet_like(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: feet.like
        passage = (
            "Uprose a fairer nest for weary feet,\n"
            "      Like some gold flower nightly inward curled,\n"
            "      Where gentle maidens fled a roaring world,\n"
            "   Or played with it, and had their white retreat."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "feet.like" not in full_text

    def test_wrap_039_pored_they(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: pored.they
        passage = (
            "Into big books of metal clasps they pored.\n"
            "      They governed, even as men; they welcomed lays.\n"
            "      The treasures women are whose aim is praise,\n"
            "   Was shown in them: the Garden half restored."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "pored.they" not in full_text

    def test_wrap_040_seas_with(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: seas.with
        passage = (
            "A deluge billow scoured the land off seas,\n"
            "      With widened jaws, and slaughter was its foam.\n"
            "      For food, for clothing, ambush, refuge, home,\n"
            "   The lesser savage offered bogs and trees."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "seas.with" not in full_text

    def test_wrap_041_grew_and(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: grew.and
        passage = (
            "Whence reverence round grey-haired story grew:\n"
            "      And inmost spots of ancient horror shone\n"
            "      As temples under beams of trials bygone;\n"
            "   For in them sang brave times with God in view."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "grew.and" not in full_text

    def test_wrap_042_green_like(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: green.like
        passage = (
            "Till now trim homesteads bordered spaces green,\n"
            "      Like night's first little stars through clearing showers.\n"
            "      Was rumoured how a castle's falcon towers\n"
            "   The wilderness commanded with fierce mien."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "green.like" not in full_text

    def test_wrap_043_lance_for(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: lance.for
        passage = (
            "Therein a serious Baron stuck his lance;\n"
            "      For minstrel songs a beauteous Dame would pout.\n"
            "      Gay knights and sombre, felon or devout,\n"
            "   Pricked onward, bound for their unsung romance."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "lance.for" not in full_text

    def test_wrap_044_across_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: across.the
        passage = (
            "It might be that two errant lords across\n"
            "      The block of each came edged, and at sharp cry\n"
            "      They charged forthwith, the better man to try.\n"
            "   One rode his way, one couched on quiet moss."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "across.the" not in full_text

    def test_wrap_045_slain_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: slain.the
        passage = (
            "Perchance a lady sweet, whose lord lay slain,\n"
            "      The robbers into gruesome durance drew.\n"
            "      Swift should her hero come, like lightning's blue!\n"
            "   She prayed for him, as crackling drought for rain."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "slain.the" not in full_text

    def test_wrap_046_read_itself(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: read.itself
        passage = (
            "By daylight now the forest fear could read\n"
            "      Itself, and at new wonders chuckling went.\n"
            "      Straight for the roebuck's neck the bowman spent\n"
            "   A dart that laughed at distance and at speed."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "read.itself" not in full_text

    def test_wrap_047_elate_rang(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: elate.rang
        passage = (
            "Right loud the bugle's hallali elate\n"
            "      Rang forth of merry dingles round the tors;\n"
            "      And deftest hand was he from foreign wars,\n"
            "   But soon he hailed the home-bred yeoman mate."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "elate.rang" not in full_text

    def test_wrap_048_time_some(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: time.some
        passage = (
            "Some shadow lurked aloof of ancient time;\n"
            "      Some warning haunted any sound prolonged,\n"
            "      As though the leagues of woodland held them wronged\n"
            "   To hear an axe and see a township climb."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "time.some" not in full_text

    def test_wrap_049_eve_had(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: eve.had
        passage = (
            "The forest's erewhile emperor at eve\n"
            "      Had voice when lowered heavens drummed for gales.\n"
            "      At midnight a small people danced the dales,\n"
            "   So thin that they might dwindle through a sieve"
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "eve.had" not in full_text

    def test_wrap_050_throats_old(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: throats.old
        passage = (
            "Ringed mushrooms told of them, and in their throats,\n"
            "      Old wives that gathered herbs and knew too much.\n"
            "      The pensioned forester beside his crutch,\n"
            "   Struck showers from embers at those bodeful notes."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "throats.old" not in full_text

    def test_wrap_051_heart_devourer(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: heart.devourer
        passage = (
            "Came then the one, all ear, all eye, all heart;\n"
            "      Devourer, and insensibly devoured;\n"
            "      In whom the city over forest flowered,\n"
            "   The forest wreathed the city's drama-mart."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "heart.devourer" not in full_text

    def test_wrap_052_old_from(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: old.from
        passage = (
            "There found he in new form that Dragon old,\n"
            "      From tangled solitudes expelled; and taught\n"
            "      How blindly each its antidote besought;\n"
            "   For either's breath the needs of either told."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "old.from" not in full_text

    def test_wrap_053_retain_the(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: retain.the
        passage = (
            "Our conquest these: if haply we retain\n"
            "      The reverence that ne'er will overrun\n"
            "      Due boundaries of realms from Nature won,\n"
            "   Nor let the poet's awe in rapture wane."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "retain.the" not in full_text

    def test_wrap_054_worked_her(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: worked.her
        passage = (
            "WITH sagest craft Arachne worked\n"
            "   Her web, and at a corner lurked,\n"
            "   Awaiting what should plump her soon,\n"
            "   To case it in the death-cocoon.\n"
            "   Sagaciously her home she chose\n"
            "   For visits that would never close;\n"
            "   Inside my chalet-porch her feast\n"
            "   Plucked all the winds but chill North-east."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "worked.her" not in full_text

    def test_wrap_055_size_aspired(self):
        # Source: A Reading of Life With Other Poems, wrap corruption: size.aspired
        passage = (
            "Arachne's dream of prey to size\n"
            "   Aspired; so she could nigh despise\n"
            "   The puny specks the breezes round\n"
            "   Supplied, and let them shake unwound;\n"
            "   Assured of her fat fly to come;\n"
            "   Perhaps a blue, the spider's plum;\n"
            "   Who takes the fatal odds in fight,\n"
            "   And gives repast an appetite,\n"
            "   By plunging, whizzing, till his wings\n"
            "   Are webbed, and in the lists he swings,\n"
            "   A shrouded lump, for her to see\n"
            "   Her banquet in her victory."
        )
        result = segment_text(passage, flatten=True)
        full_text = " ".join(result)
        assert "size.aspired" not in full_text

