# -*- coding: UTF-8 -*-
"""Xfail tests for hard-wrap corruption in ebook-style passages (issue #42).

These tests document the desired behaviour of segment_text() when processing
Project Gutenberg plain-text files with 4-space-indented continuation lines.
Every test is marked xfail because the current implementation is buggy:
the word boundary between the two wrapped halves gets corrupted to a period.

After the fix (strip-per-line in NewlinesToPeriods), these should all xpass.

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

import pytest
from fast_sentence_segment import segment_text


class TestXfailEbookWrapping:
    """Full-pipeline xfail tests for Gutenberg-style 4-space hard-wrap passages.

    All tests use segment_text() and assert that word-boundary corruption
    (wordA.wordB) does not appear in the joined output.
    """

    # ================================================================ Bennett (1900s)

    @pytest.mark.xfail(reason="4-space wrap: 'business.department' corruption (issue #42)")
    def test_bennett_001(self):
        result = segment_text(
            "He had worked in the business\n    department for thirty years.",
            flatten=True,
        )
        assert "business.department" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'advertising.department' corruption (issue #42)")
    def test_bennett_002(self):
        result = segment_text(
            "She was transferred to the advertising\n    department after the merger.",
            flatten=True,
        )
        assert "advertising.department" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'five.towns' corruption (issue #42)")
    def test_bennett_003(self):
        result = segment_text(
            "He had grown up among the five\n    towns of the Potteries.",
            flatten=True,
        )
        assert "five.towns" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'pottery.district' corruption (issue #42)")
    def test_bennett_004(self):
        result = segment_text(
            "The whole economy depended on the pottery\n    district and its kilns.",
            flatten=True,
        )
        assert "pottery.district" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'old.wives' corruption (issue #42)")
    def test_bennett_005(self):
        result = segment_text(
            "The novel told of two old\n    wives and their long friendship.",
            flatten=True,
        )
        assert "old.wives" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'hotel.keeper' corruption (issue #42)")
    def test_bennett_006(self):
        result = segment_text(
            "The ambitious hotel\n    keeper expanded the establishment.",
            flatten=True,
        )
        assert "hotel.keeper" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'front.door' corruption (issue #42)")
    def test_bennett_007(self):
        result = segment_text(
            "She answered the front\n    door and found a stranger there.",
            flatten=True,
        )
        assert "front.door" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'market.square' corruption (issue #42)")
    def test_bennett_008(self):
        result = segment_text(
            "He crossed the crowded market\n    square in the afternoon sun.",
            flatten=True,
        )
        assert "market.square" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'town.hall' corruption (issue #42)")
    def test_bennett_009(self):
        result = segment_text(
            "The meeting was held in the town\n    hall on Wednesday evening.",
            flatten=True,
        )
        assert "town.hall" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'dining.room' corruption (issue #42)")
    def test_bennett_010(self):
        result = segment_text(
            "They gathered in the dining\n    room for the evening meal.",
            flatten=True,
        )
        assert "dining.room" not in " ".join(result)

    # ================================================================ Hardy (1890s)

    @pytest.mark.xfail(reason="4-space wrap: 'dairy.maid' corruption (issue #42)")
    def test_hardy_001(self):
        result = segment_text(
            "She had worked as a dairy\n    maid since she was fourteen.",
            flatten=True,
        )
        assert "dairy.maid" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'tess.of' corruption (issue #42)")
    def test_hardy_002(self):
        result = segment_text(
            "The story centres on Tess\n    of the d'Urbervilles.",
            flatten=True,
        )
        assert "tess.of" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'corn.field' corruption (issue #42)")
    def test_hardy_003(self):
        result = segment_text(
            "They met in the broad corn\n    field at the edge of the farm.",
            flatten=True,
        )
        assert "corn.field" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'vale.of' corruption (issue #42)")
    def test_hardy_004(self):
        result = segment_text(
            "She walked through the wide vale\n    of Blackmore in the early dusk.",
            flatten=True,
        )
        assert "vale.of" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'parish.church' corruption (issue #42)")
    def test_hardy_005(self):
        result = segment_text(
            "The family had worshipped at the old parish\n    church for generations.",
            flatten=True,
        )
        assert "parish.church" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'stone.wall' corruption (issue #42)")
    def test_hardy_006(self):
        result = segment_text(
            "He leaned against the old stone\n    wall and looked across the fields.",
            flatten=True,
        )
        assert "stone.wall" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'harvest.time' corruption (issue #42)")
    def test_hardy_007(self):
        result = segment_text(
            "All hands were needed at harvest\n    time to bring in the crop.",
            flatten=True,
        )
        assert "harvest.time" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'farm.house' corruption (issue #42)")
    def test_hardy_008(self):
        result = segment_text(
            "The light burned in the farm\n    house window until midnight.",
            flatten=True,
        )
        assert "farm.house" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'village.green' corruption (issue #42)")
    def test_hardy_009(self):
        result = segment_text(
            "The men gathered on the village\n    green on Sunday afternoons.",
            flatten=True,
        )
        assert "village.green" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'haymaking.season' corruption (issue #42)")
    def test_hardy_010(self):
        result = segment_text(
            "She had met him during the haymaking\n    season at Talbothays.",
            flatten=True,
        )
        assert "haymaking.season" not in " ".join(result)

    # ================================================================ Trollope (1870s)

    @pytest.mark.xfail(reason="4-space wrap: 'barchester.towers' corruption (issue #42)")
    def test_trollope_001(self):
        result = segment_text(
            "The dispute involved the deanery of Barchester\n    Towers and its revenues.",
            flatten=True,
        )
        assert "barchester.towers" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'church.living' corruption (issue #42)")
    def test_trollope_002(self):
        result = segment_text(
            "The bishop had the power to award a valuable church\n    living to a clergyman.",
            flatten=True,
        )
        assert "church.living" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'cathedral.close' corruption (issue #42)")
    def test_trollope_003(self):
        result = segment_text(
            "They lived in a comfortable house in the cathedral\n    close.",
            flatten=True,
        )
        assert "cathedral.close" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'county.family' corruption (issue #42)")
    def test_trollope_004(self):
        result = segment_text(
            "She married into a respectable county\n    family with ancient connections.",
            flatten=True,
        )
        assert "county.family" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'political.career' corruption (issue #42)")
    def test_trollope_005(self):
        result = segment_text(
            "His father had hoped for a distinguished political\n    career in Parliament.",
            flatten=True,
        )
        assert "political.career" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'estate.agent' corruption (issue #42)")
    def test_trollope_006(self):
        result = segment_text(
            "He consulted the estate\n    agent about managing the property.",
            flatten=True,
        )
        assert "estate.agent" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'hunting.field' corruption (issue #42)")
    def test_trollope_007(self):
        result = segment_text(
            "He had distinguished himself in the hunting\n    field every season.",
            flatten=True,
        )
        assert "hunting.field" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'evening.party' corruption (issue #42)")
    def test_trollope_008(self):
        result = segment_text(
            "She arranged an elaborate evening\n    party for the county gentry.",
            flatten=True,
        )
        assert "evening.party" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'dining.table' corruption (issue #42)")
    def test_trollope_009(self):
        result = segment_text(
            "The silver gleamed on the long dining\n    table set for twenty guests.",
            flatten=True,
        )
        assert "dining.table" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'morning.call' corruption (issue #42)")
    def test_trollope_010(self):
        result = segment_text(
            "She made a formal morning\n    call on the new arrivals.",
            flatten=True,
        )
        assert "morning.call" not in " ".join(result)

    # ================================================================ Dickens-era / general Victorian

    @pytest.mark.xfail(reason="4-space wrap: 'counting.house' corruption (issue #42)")
    def test_victorian_001(self):
        result = segment_text(
            "He had laboured in the counting\n    house since boyhood.",
            flatten=True,
        )
        assert "counting.house" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'work.house' corruption (issue #42)")
    def test_victorian_002(self):
        result = segment_text(
            "The destitute family feared being sent to the work\n    house.",
            flatten=True,
        )
        assert "work.house" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'gin.shop' corruption (issue #42)")
    def test_victorian_003(self):
        result = segment_text(
            "He stumbled out of the gin\n    shop just before closing time.",
            flatten=True,
        )
        assert "gin.shop" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'coal.merchant' corruption (issue #42)")
    def test_victorian_004(self):
        result = segment_text(
            "The coal\n    merchant delivered twice a week in winter.",
            flatten=True,
        )
        assert "coal.merchant" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'railway.station' corruption (issue #42)")
    def test_victorian_005(self):
        result = segment_text(
            "They drove to the railway\n    station in the family brougham.",
            flatten=True,
        )
        assert "railway.station" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'post.office' corruption (issue #42)")
    def test_victorian_006(self):
        result = segment_text(
            "She called in at the post\n    office to collect a registered letter.",
            flatten=True,
        )
        assert "post.office" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'fire.place' corruption (issue #42)")
    def test_victorian_007(self):
        result = segment_text(
            "The family gathered round the fire\n    place on cold evenings.",
            flatten=True,
        )
        assert "fire.place" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'drawing.room' corruption (issue #42)")
    def test_victorian_008(self):
        result = segment_text(
            "The ladies retired to the drawing\n    room after dinner.",
            flatten=True,
        )
        assert "drawing.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'smoking.room' corruption (issue #42)")
    def test_victorian_009(self):
        result = segment_text(
            "The gentlemen repaired to the smoking\n    room for cigars and port.",
            flatten=True,
        )
        assert "smoking.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'reading.room' corruption (issue #42)")
    def test_victorian_010(self):
        result = segment_text(
            "He spent the afternoon in the reading\n    room of the public library.",
            flatten=True,
        )
        assert "reading.room" not in " ".join(result)

    # ================================================================ Edwardian journalism / Dreiser-era

    @pytest.mark.xfail(reason="4-space wrap: 'news.paper' corruption (issue #42)")
    def test_edwardian_001(self):
        result = segment_text(
            "She picked up the morning news\n    paper from the doorstep.",
            flatten=True,
        )
        assert "news.paper" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'printing.press' corruption (issue #42)")
    def test_edwardian_002(self):
        result = segment_text(
            "The huge printing\n    press thundered through the night.",
            flatten=True,
        )
        assert "printing.press" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'city.editor' corruption (issue #42)")
    def test_edwardian_003(self):
        result = segment_text(
            "He applied for the post of city\n    editor of the Tribune.",
            flatten=True,
        )
        assert "city.editor" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'editorial.office' corruption (issue #42)")
    def test_edwardian_004(self):
        result = segment_text(
            "She worked late in the editorial\n    office to meet the deadline.",
            flatten=True,
        )
        assert "editorial.office" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'stock.market' corruption (issue #42)")
    def test_edwardian_005(self):
        result = segment_text(
            "Rumours on the stock\n    market caused widespread panic.",
            flatten=True,
        )
        assert "stock.market" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'trading.floor' corruption (issue #42)")
    def test_edwardian_006(self):
        result = segment_text(
            "He made his name on the trading\n    floor of the Chicago exchange.",
            flatten=True,
        )
        assert "trading.floor" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'board.room' corruption (issue #42)")
    def test_edwardian_007(self):
        result = segment_text(
            "The directors assembled in the board\n    room at nine o'clock sharp.",
            flatten=True,
        )
        assert "board.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'filing.clerk' corruption (issue #42)")
    def test_edwardian_008(self):
        result = segment_text(
            "A diligent filing\n    clerk kept the correspondence in order.",
            flatten=True,
        )
        assert "filing.clerk" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'book.keeper' corruption (issue #42)")
    def test_edwardian_009(self):
        result = segment_text(
            "The firm employed a trusted book\n    keeper for forty years.",
            flatten=True,
        )
        assert "book.keeper" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'type.writer' corruption (issue #42)")
    def test_edwardian_010(self):
        result = segment_text(
            "She typed the letters on a new type\n    writer with remarkable speed.",
            flatten=True,
        )
        assert "type.writer" not in " ".join(result)

    # ================================================================ Science / academic

    @pytest.mark.xfail(reason="4-space wrap: 'research.department' corruption (issue #42)")
    def test_science_001(self):
        result = segment_text(
            "He led the research\n    department for two decades.",
            flatten=True,
        )
        assert "research.department" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'laboratory.results' corruption (issue #42)")
    def test_science_002(self):
        result = segment_text(
            "The laboratory\n    results confirmed the hypothesis.",
            flatten=True,
        )
        assert "laboratory.results" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'field.work' corruption (issue #42)")
    def test_science_003(self):
        result = segment_text(
            "She conducted extensive field\n    work in the tropical forests.",
            flatten=True,
        )
        assert "field.work" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'control.group' corruption (issue #42)")
    def test_science_004(self):
        result = segment_text(
            "The control\n    group received no treatment whatsoever.",
            flatten=True,
        )
        assert "control.group" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'sample.size' corruption (issue #42)")
    def test_science_005(self):
        result = segment_text(
            "The small sample\n    size limited the statistical power.",
            flatten=True,
        )
        assert "sample.size" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'data.set' corruption (issue #42)")
    def test_science_006(self):
        result = segment_text(
            "She analysed the entire data\n    set using regression methods.",
            flatten=True,
        )
        assert "data.set" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'peer.review' corruption (issue #42)")
    def test_science_007(self):
        result = segment_text(
            "The paper passed peer\n    review after two rounds of revision.",
            flatten=True,
        )
        assert "peer.review" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'grant.funding' corruption (issue #42)")
    def test_science_008(self):
        result = segment_text(
            "They applied for grant\n    funding from the national council.",
            flatten=True,
        )
        assert "grant.funding" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'test.tube' corruption (issue #42)")
    def test_science_009(self):
        result = segment_text(
            "She heated the mixture in a glass test\n    tube over a Bunsen burner.",
            flatten=True,
        )
        assert "test.tube" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'lecture.theatre' corruption (issue #42)")
    def test_science_010(self):
        result = segment_text(
            "The professor filled the lecture\n    theatre every Monday morning.",
            flatten=True,
        )
        assert "lecture.theatre" not in " ".join(result)

    # ================================================================ Military / history

    @pytest.mark.xfail(reason="4-space wrap: 'battle.field' corruption (issue #42)")
    def test_military_001(self):
        result = segment_text(
            "Thousands fell on the battle\n    field before the armistice.",
            flatten=True,
        )
        assert "battle.field" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'command.post' corruption (issue #42)")
    def test_military_002(self):
        result = segment_text(
            "The general established his command\n    post on the ridge above the valley.",
            flatten=True,
        )
        assert "command.post" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'supply.line' corruption (issue #42)")
    def test_military_003(self):
        result = segment_text(
            "The enemy cut the main supply\n    line behind the advancing troops.",
            flatten=True,
        )
        assert "supply.line" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'trench.warfare' corruption (issue #42)")
    def test_military_004(self):
        result = segment_text(
            "Both sides settled into grim trench\n    warfare along the Somme.",
            flatten=True,
        )
        assert "trench.warfare" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'field.hospital' corruption (issue #42)")
    def test_military_005(self):
        result = segment_text(
            "The wounded were carried to the field\n    hospital three miles to the rear.",
            flatten=True,
        )
        assert "field.hospital" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'machine.gun' corruption (issue #42)")
    def test_military_006(self):
        result = segment_text(
            "The advance was halted by machine\n    gun fire from the embankment.",
            flatten=True,
        )
        assert "machine.gun" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'war.office' corruption (issue #42)")
    def test_military_007(self):
        result = segment_text(
            "The telegram arrived from the war\n    office at three in the morning.",
            flatten=True,
        )
        assert "war.office" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'army.corps' corruption (issue #42)")
    def test_military_008(self):
        result = segment_text(
            "The third army\n    corps was ordered to advance at dawn.",
            flatten=True,
        )
        assert "army.corps" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'naval.station' corruption (issue #42)")
    def test_military_009(self):
        result = segment_text(
            "She reported to the naval\n    station at Portsmouth.",
            flatten=True,
        )
        assert "naval.station" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'regimental.colours' corruption (issue #42)")
    def test_military_010(self):
        result = segment_text(
            "They carried the regimental\n    colours into the parade ground.",
            flatten=True,
        )
        assert "regimental.colours" not in " ".join(result)

    # ================================================================ Legal / formal

    @pytest.mark.xfail(reason="4-space wrap: 'legal.department' corruption (issue #42)")
    def test_legal_001(self):
        result = segment_text(
            "The matter was referred to the legal\n    department for an opinion.",
            flatten=True,
        )
        assert "legal.department" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'court.room' corruption (issue #42)")
    def test_legal_002(self):
        result = segment_text(
            "The jury filed back into the court\n    room after three hours.",
            flatten=True,
        )
        assert "court.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'court.house' corruption (issue #42)")
    def test_legal_003(self):
        result = segment_text(
            "He climbed the steps of the court\n    house and entered the building.",
            flatten=True,
        )
        assert "court.house" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'law.firm' corruption (issue #42)")
    def test_legal_004(self):
        result = segment_text(
            "She joined the distinguished law\n    firm as a junior partner.",
            flatten=True,
        )
        assert "law.firm" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'contract.law' corruption (issue #42)")
    def test_legal_005(self):
        result = segment_text(
            "He was an expert in contract\n    law and arbitration.",
            flatten=True,
        )
        assert "contract.law" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'jury.room' corruption (issue #42)")
    def test_legal_006(self):
        result = segment_text(
            "The jurors deliberated in the jury\n    room for two days.",
            flatten=True,
        )
        assert "jury.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'title.deed' corruption (issue #42)")
    def test_legal_007(self):
        result = segment_text(
            "The solicitor produced the original title\n    deed for the property.",
            flatten=True,
        )
        assert "title.deed" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'land.registry' corruption (issue #42)")
    def test_legal_008(self):
        result = segment_text(
            "The transfer was registered at the land\n    registry the following week.",
            flatten=True,
        )
        assert "land.registry" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'public.record' corruption (issue #42)")
    def test_legal_009(self):
        result = segment_text(
            "The document was filed as a public\n    record at the county office.",
            flatten=True,
        )
        assert "public.record" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'company.director' corruption (issue #42)")
    def test_legal_010(self):
        result = segment_text(
            "He resigned as company\n    director following the investigation.",
            flatten=True,
        )
        assert "company.director" not in " ".join(result)

    # ================================================================ Fiction — domestic/social

    @pytest.mark.xfail(reason="4-space wrap: 'sitting.room' corruption (issue #42)")
    def test_fiction_001(self):
        result = segment_text(
            "She sewed by the fire in the sitting\n    room every evening.",
            flatten=True,
        )
        assert "sitting.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'morning.room' corruption (issue #42)")
    def test_fiction_002(self):
        result = segment_text(
            "The correspondence was dealt with in the morning\n    room after breakfast.",
            flatten=True,
        )
        assert "morning.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'servant.girl' corruption (issue #42)")
    def test_fiction_003(self):
        result = segment_text(
            "The servant\n    girl opened the door without a word.",
            flatten=True,
        )
        assert "servant.girl" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'house.keeper' corruption (issue #42)")
    def test_fiction_004(self):
        result = segment_text(
            "The house\n    keeper had managed the establishment for years.",
            flatten=True,
        )
        assert "house.keeper" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'upper.class' corruption (issue #42)")
    def test_fiction_005(self):
        result = segment_text(
            "She aspired to move in upper\n    class society one day.",
            flatten=True,
        )
        assert "upper.class" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'church.going' corruption (issue #42)")
    def test_fiction_006(self):
        result = segment_text(
            "The family had a church\n    going habit that never varied.",
            flatten=True,
        )
        assert "church.going" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'school.master' corruption (issue #42)")
    def test_fiction_007(self):
        result = segment_text(
            "The old school\n    master taught the same pupils for thirty years.",
            flatten=True,
        )
        assert "school.master" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'club.house' corruption (issue #42)")
    def test_fiction_008(self):
        result = segment_text(
            "He met his friends at the club\n    house every Thursday.",
            flatten=True,
        )
        assert "club.house" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'ball.room' corruption (issue #42)")
    def test_fiction_009(self):
        result = segment_text(
            "The dancers filled the ball\n    room from eight until midnight.",
            flatten=True,
        )
        assert "ball.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'supper.table' corruption (issue #42)")
    def test_fiction_010(self):
        result = segment_text(
            "They gathered round the supper\n    table after the concert.",
            flatten=True,
        )
        assert "supper.table" not in " ".join(result)

    # ================================================================ Fiction — nature / outdoor

    @pytest.mark.xfail(reason="4-space wrap: 'hill.side' corruption (issue #42)")
    def test_nature_001(self):
        result = segment_text(
            "The flock grazed on the open hill\n    side all summer long.",
            flatten=True,
        )
        assert "hill.side" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'river.bank' corruption (issue #42)")
    def test_nature_002(self):
        result = segment_text(
            "They picnicked on the shaded river\n    bank in July.",
            flatten=True,
        )
        assert "river.bank" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'wood.land' corruption (issue #42)")
    def test_nature_003(self):
        result = segment_text(
            "The path wound through ancient wood\n    land for two miles.",
            flatten=True,
        )
        assert "wood.land" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'meadow.land' corruption (issue #42)")
    def test_nature_004(self):
        result = segment_text(
            "Cattle grazed on the flat meadow\n    land by the stream.",
            flatten=True,
        )
        assert "meadow.land" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'cliff.top' corruption (issue #42)")
    def test_nature_005(self):
        result = segment_text(
            "He stood alone on the windswept cliff\n    top looking out to sea.",
            flatten=True,
        )
        assert "cliff.top" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'moor.land' corruption (issue #42)")
    def test_nature_006(self):
        result = segment_text(
            "She crossed miles of bleak moor\n    land before reaching shelter.",
            flatten=True,
        )
        assert "moor.land" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'corn.field' corruption (issue #42)")
    def test_nature_007(self):
        result = segment_text(
            "Poppies grew at the edge of the corn\n    field in early summer.",
            flatten=True,
        )
        assert "corn.field" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'apple.orchard' corruption (issue #42)")
    def test_nature_008(self):
        result = segment_text(
            "They slept in the old apple\n    orchard on summer nights.",
            flatten=True,
        )
        assert "apple.orchard" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'kitchen.garden' corruption (issue #42)")
    def test_nature_009(self):
        result = segment_text(
            "She grew herbs in the kitchen\n    garden behind the house.",
            flatten=True,
        )
        assert "kitchen.garden" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'rose.garden' corruption (issue #42)")
    def test_nature_010(self):
        result = segment_text(
            "The scent drifted from the rose\n    garden on warm afternoons.",
            flatten=True,
        )
        assert "rose.garden" not in " ".join(result)

    # ================================================================ Travel / geography

    @pytest.mark.xfail(reason="4-space wrap: 'port.town' corruption (issue #42)")
    def test_travel_001(self):
        result = segment_text(
            "They arrived at the busy port\n    town in the early afternoon.",
            flatten=True,
        )
        assert "port.town" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'market.town' corruption (issue #42)")
    def test_travel_002(self):
        result = segment_text(
            "It was a quiet market\n    town with a weekly cattle fair.",
            flatten=True,
        )
        assert "market.town" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'county.town' corruption (issue #42)")
    def test_travel_003(self):
        result = segment_text(
            "The assizes were held in the county\n    town twice yearly.",
            flatten=True,
        )
        assert "county.town" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'sea.port' corruption (issue #42)")
    def test_travel_004(self):
        result = segment_text(
            "The trade route began at the prosperous sea\n    port of Bristol.",
            flatten=True,
        )
        assert "sea.port" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'cross.roads' corruption (issue #42)")
    def test_travel_005(self):
        result = segment_text(
            "They halted at the cross\n    roads to consult the map.",
            flatten=True,
        )
        assert "cross.roads" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'road.side' corruption (issue #42)")
    def test_travel_006(self):
        result = segment_text(
            "They rested at a road\n    side inn before continuing.",
            flatten=True,
        )
        assert "road.side" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'coach.road' corruption (issue #42)")
    def test_travel_007(self):
        result = segment_text(
            "The old coach\n    road ran straight across the heath.",
            flatten=True,
        )
        assert "coach.road" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'inn.keeper' corruption (issue #42)")
    def test_travel_008(self):
        result = segment_text(
            "The inn\n    keeper showed them to a comfortable room.",
            flatten=True,
        )
        assert "inn.keeper" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'stage.coach' corruption (issue #42)")
    def test_travel_009(self):
        result = segment_text(
            "They boarded the stage\n    coach at six in the morning.",
            flatten=True,
        )
        assert "stage.coach" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'toll.gate' corruption (issue #42)")
    def test_travel_010(self):
        result = segment_text(
            "The coachman slowed at the toll\n    gate and paid the keeper.",
            flatten=True,
        )
        assert "toll.gate" not in " ".join(result)

    # ================================================================ Dreiser / American naturalism

    @pytest.mark.xfail(reason="4-space wrap: 'sister.carrie' compound noun (issue #42)")
    def test_dreiser_001(self):
        result = segment_text(
            "The novel follows Sister\n    Carrie as she arrives in Chicago.",
            flatten=True,
        )
        assert "sister.carrie" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'garment.district' corruption (issue #42)")
    def test_dreiser_002(self):
        result = segment_text(
            "She found work in the garment\n    district on the west side.",
            flatten=True,
        )
        assert "garment.district" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'department.store' corruption (issue #42)")
    def test_dreiser_003(self):
        result = segment_text(
            "She applied for a position in the department\n    store on State Street.",
            flatten=True,
        )
        assert "department.store" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'factory.girl' corruption (issue #42)")
    def test_dreiser_004(self):
        result = segment_text(
            "She was just another factory\n    girl arriving in the big city.",
            flatten=True,
        )
        assert "factory.girl" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'boarding.house' corruption (issue #42)")
    def test_dreiser_005(self):
        result = segment_text(
            "She took a room at a respectable boarding\n    house near the station.",
            flatten=True,
        )
        assert "boarding.house" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'show.business' corruption (issue #42)")
    def test_dreiser_006(self):
        result = segment_text(
            "She dreamed of making it in show\n    business on the stage.",
            flatten=True,
        )
        assert "show.business" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'labour.union' corruption (issue #42)")
    def test_dreiser_007(self):
        result = segment_text(
            "The workers organised themselves into a labour\n    union.",
            flatten=True,
        )
        assert "labour.union" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'street.car' corruption (issue #42)")
    def test_dreiser_008(self):
        result = segment_text(
            "She rode the street\n    car down Michigan Avenue every morning.",
            flatten=True,
        )
        assert "street.car" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'sales.clerk' corruption (issue #42)")
    def test_dreiser_009(self):
        result = segment_text(
            "She was hired as a sales\n    clerk at the shoe counter.",
            flatten=True,
        )
        assert "sales.clerk" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'night.club' corruption (issue #42)")
    def test_dreiser_010(self):
        result = segment_text(
            "Hurstwood managed the finest night\n    club on the north side.",
            flatten=True,
        )
        assert "night.club" not in " ".join(result)

    # ================================================================ American West / adventure

    @pytest.mark.xfail(reason="4-space wrap: 'cattle.ranch' corruption (issue #42)")
    def test_western_001(self):
        result = segment_text(
            "He owned a thousand acres of cattle\n    ranch in Wyoming.",
            flatten=True,
        )
        assert "cattle.ranch" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'ranch.hand' corruption (issue #42)")
    def test_western_002(self):
        result = segment_text(
            "He hired on as a ranch\n    hand for the summer season.",
            flatten=True,
        )
        assert "ranch.hand" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'gold.mine' corruption (issue #42)")
    def test_western_003(self):
        result = segment_text(
            "He had invested everything in a worked-out gold\n    mine.",
            flatten=True,
        )
        assert "gold.mine" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'trail.boss' corruption (issue #42)")
    def test_western_004(self):
        result = segment_text(
            "The trail\n    boss gave the signal to move out at dawn.",
            flatten=True,
        )
        assert "trail.boss" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'water.hole' corruption (issue #42)")
    def test_western_005(self):
        result = segment_text(
            "They found the water\n    hole dry after three weeks without rain.",
            flatten=True,
        )
        assert "water.hole" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'camp.fire' corruption (issue #42)")
    def test_western_006(self):
        result = segment_text(
            "They gathered round the camp\n    fire and traded stories.",
            flatten=True,
        )
        assert "camp.fire" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'log.cabin' corruption (issue #42)")
    def test_western_007(self):
        result = segment_text(
            "He built a solid log\n    cabin on the ridge above the river.",
            flatten=True,
        )
        assert "log.cabin" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'saddle.bag' corruption (issue #42)")
    def test_western_008(self):
        result = segment_text(
            "He reached into the saddle\n    bag for the worn map.",
            flatten=True,
        )
        assert "saddle.bag" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'scout.report' corruption (issue #42)")
    def test_western_009(self):
        result = segment_text(
            "The scout\n    report indicated a large party ahead.",
            flatten=True,
        )
        assert "scout.report" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'frontier.town' corruption (issue #42)")
    def test_western_010(self):
        result = segment_text(
            "It was a rough frontier\n    town with a single muddy street.",
            flatten=True,
        )
        assert "frontier.town" not in " ".join(result)

    # ================================================================ Medicine / social reform

    @pytest.mark.xfail(reason="4-space wrap: 'fever.ward' corruption (issue #42)")
    def test_medical_001(self):
        result = segment_text(
            "She volunteered in the fever\n    ward during the epidemic.",
            flatten=True,
        )
        assert "fever.ward" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'nursing.staff' corruption (issue #42)")
    def test_medical_002(self):
        result = segment_text(
            "The nursing\n    staff worked without rest for three days.",
            flatten=True,
        )
        assert "nursing.staff" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'operating.theatre' corruption (issue #42)")
    def test_medical_003(self):
        result = segment_text(
            "The surgeon operated in the new operating\n    theatre all morning.",
            flatten=True,
        )
        assert "operating.theatre" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'dispensary.hours' corruption (issue #42)")
    def test_medical_004(self):
        result = segment_text(
            "The dispensary\n    hours were posted on the door.",
            flatten=True,
        )
        assert "dispensary.hours" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'health.board' corruption (issue #42)")
    def test_medical_005(self):
        result = segment_text(
            "The district health\n    board met to discuss the outbreak.",
            flatten=True,
        )
        assert "health.board" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'welfare.reform' corruption (issue #42)")
    def test_medical_006(self):
        result = segment_text(
            "She championed welfare\n    reform throughout her long career.",
            flatten=True,
        )
        assert "welfare.reform" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'charity.work' corruption (issue #42)")
    def test_medical_007(self):
        result = segment_text(
            "She devoted her retirement to charity\n    work in the East End.",
            flatten=True,
        )
        assert "charity.work" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'public.health' corruption (issue #42)")
    def test_medical_008(self):
        result = segment_text(
            "The new legislation improved public\n    health in the industrial towns.",
            flatten=True,
        )
        assert "public.health" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'soup.kitchen' corruption (issue #42)")
    def test_medical_009(self):
        result = segment_text(
            "Volunteers served meals at the soup\n    kitchen every evening.",
            flatten=True,
        )
        assert "soup.kitchen" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'reform.school' corruption (issue #42)")
    def test_medical_010(self):
        result = segment_text(
            "The boy was sent to a reform\n    school in the north.",
            flatten=True,
        )
        assert "reform.school" not in " ".join(result)

    # ================================================================ Collins / sensation fiction

    @pytest.mark.xfail(reason="4-space wrap: 'asylum.doctor' corruption (issue #42)")
    def test_collins_001(self):
        result = segment_text(
            "The asylum\n    doctor certified him as incapable.",
            flatten=True,
        )
        assert "asylum.doctor" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'private.detective' corruption (issue #42)")
    def test_collins_002(self):
        result = segment_text(
            "He engaged a private\n    detective to trace the missing woman.",
            flatten=True,
        )
        assert "private.detective" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'secret.passage' corruption (issue #42)")
    def test_collins_003(self):
        result = segment_text(
            "She discovered the hidden secret\n    passage behind the wardrobe.",
            flatten=True,
        )
        assert "secret.passage" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'family.secret' corruption (issue #42)")
    def test_collins_004(self):
        result = segment_text(
            "The lawyer revealed the family\n    secret that had been kept for decades.",
            flatten=True,
        )
        assert "family.secret" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'forged.will' corruption (issue #42)")
    def test_collins_005(self):
        result = segment_text(
            "The solicitor proved the document was a forged\n    will.",
            flatten=True,
        )
        assert "forged.will" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'locked.room' corruption (issue #42)")
    def test_collins_006(self):
        result = segment_text(
            "The body was found in the locked\n    room on the second floor.",
            flatten=True,
        )
        assert "locked.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'master.key' corruption (issue #42)")
    def test_collins_007(self):
        result = segment_text(
            "Only the butler held the master\n    key to the east wing.",
            flatten=True,
        )
        assert "master.key" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'witness.statement' corruption (issue #42)")
    def test_collins_008(self):
        result = segment_text(
            "The lawyer read the witness\n    statement aloud in court.",
            flatten=True,
        )
        assert "witness.statement" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'missing.heir' corruption (issue #42)")
    def test_collins_009(self):
        result = segment_text(
            "The mystery centred on a missing\n    heir and a disputed estate.",
            flatten=True,
        )
        assert "missing.heir" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'poison.ring' corruption (issue #42)")
    def test_collins_010(self):
        result = segment_text(
            "She wore a concealed poison\n    ring on her right hand.",
            flatten=True,
        )
        assert "poison.ring" not in " ".join(result)

    # ================================================================ Extra: assorted compound nouns

    @pytest.mark.xfail(reason="4-space wrap: 'fire.station' corruption (issue #42)")
    def test_compound_001(self):
        result = segment_text(
            "The alarm rang at the fire\n    station at half past two.",
            flatten=True,
        )
        assert "fire.station" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'police.station' corruption (issue #42)")
    def test_compound_002(self):
        result = segment_text(
            "He was taken to the police\n    station for questioning.",
            flatten=True,
        )
        assert "police.station" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'book.shop' corruption (issue #42)")
    def test_compound_003(self):
        result = segment_text(
            "She spent the afternoon in a second-hand book\n    shop on the high street.",
            flatten=True,
        )
        assert "book.shop" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'tea.shop' corruption (issue #42)")
    def test_compound_004(self):
        result = segment_text(
            "They met in the little tea\n    shop near the cathedral.",
            flatten=True,
        )
        assert "tea.shop" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'coffee.house' corruption (issue #42)")
    def test_compound_005(self):
        result = segment_text(
            "The merchants gathered at the coffee\n    house to discuss the rates.",
            flatten=True,
        )
        assert "coffee.house" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'barber.shop' corruption (issue #42)")
    def test_compound_006(self):
        result = segment_text(
            "He stopped in at the barber\n    shop for a trim and a shave.",
            flatten=True,
        )
        assert "barber.shop" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'hat.shop' corruption (issue #42)")
    def test_compound_007(self):
        result = segment_text(
            "She admired the window display of the hat\n    shop on Bond Street.",
            flatten=True,
        )
        assert "hat.shop" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'wine.merchant' corruption (issue #42)")
    def test_compound_008(self):
        result = segment_text(
            "He ordered two cases from the wine\n    merchant in the arcade.",
            flatten=True,
        )
        assert "wine.merchant" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'bread.basket' corruption (issue #42)")
    def test_compound_009(self):
        result = segment_text(
            "She carried the bread\n    basket in from the kitchen.",
            flatten=True,
        )
        assert "bread.basket" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'sugar.plum' corruption (issue #42)")
    def test_compound_010(self):
        result = segment_text(
            "The child reached for a sugar\n    plum from the bowl.",
            flatten=True,
        )
        assert "sugar.plum" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'lamp.post' corruption (issue #42)")
    def test_compound_011(self):
        result = segment_text(
            "He leaned against the lamp\n    post and watched the traffic.",
            flatten=True,
        )
        assert "lamp.post" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'letter.box' corruption (issue #42)")
    def test_compound_012(self):
        result = segment_text(
            "The postman pushed letters through the letter\n    box at seven each morning.",
            flatten=True,
        )
        assert "letter.box" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'stair.case' corruption (issue #42)")
    def test_compound_013(self):
        result = segment_text(
            "She heard footsteps on the stair\n    case and held her breath.",
            flatten=True,
        )
        assert "stair.case" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'bed.room' corruption (issue #42)")
    def test_compound_014(self):
        result = segment_text(
            "She retired to her bed\n    room early that evening.",
            flatten=True,
        )
        assert "bed.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'bath.room' corruption (issue #42)")
    def test_compound_015(self):
        result = segment_text(
            "He locked himself in the bath\n    room and refused to come out.",
            flatten=True,
        )
        assert "bath.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'store.room' corruption (issue #42)")
    def test_compound_016(self):
        result = segment_text(
            "The unused equipment was kept in the store\n    room at the back.",
            flatten=True,
        )
        assert "store.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'work.shop' corruption (issue #42)")
    def test_compound_017(self):
        result = segment_text(
            "He repaired clocks in the work\n    shop beneath the house.",
            flatten=True,
        )
        assert "work.shop" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'show.room' corruption (issue #42)")
    def test_compound_018(self):
        result = segment_text(
            "The new models were on display in the show\n    room on the ground floor.",
            flatten=True,
        )
        assert "show.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'gun.room' corruption (issue #42)")
    def test_compound_019(self):
        result = segment_text(
            "The sporting rifles were kept in the gun\n    room behind the library.",
            flatten=True,
        )
        assert "gun.room" not in " ".join(result)

    @pytest.mark.xfail(reason="4-space wrap: 'lumber.room' corruption (issue #42)")
    def test_compound_020(self):
        result = segment_text(
            "Old trunks were stored in the lumber\n    room on the top floor.",
            flatten=True,
        )
        assert "lumber.room" not in " ".join(result)
