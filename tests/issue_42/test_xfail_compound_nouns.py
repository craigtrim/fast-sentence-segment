# -*- coding: UTF-8 -*-
"""Xfail tests for compound-noun wrap corruption (issue #42).

These target the most common compound nouns that appear in Project Gutenberg
plain-text files and get corrupted by the 4-space-indent hard-wrap bug.

Related: https://github.com/craigtrim/fast-sentence-segment/issues/42
"""

import pytest
from fast_sentence_segment.dmo.newlines_to_periods import NewlinesToPeriods


class TestXfailCompoundNouns:
    """4-space wrap at common compound-noun boundaries — all currently corrupted."""

    # ---------------------------------------------------------------- rooms

    @pytest.mark.xfail(reason="4-space wrap: 'sitting.room' (issue #42)")
    def test_room_001(self):
        assert NewlinesToPeriods.process("She sat in the sitting\n    room until dark.") == "She sat in the sitting room until dark."

    @pytest.mark.xfail(reason="4-space wrap: 'dining.room' (issue #42)")
    def test_room_002(self):
        assert NewlinesToPeriods.process("They ate in the dining\n    room as usual.") == "They ate in the dining room as usual."

    @pytest.mark.xfail(reason="4-space wrap: 'drawing.room' (issue #42)")
    def test_room_003(self):
        assert NewlinesToPeriods.process("Ladies retired to the drawing\n    room after dinner.") == "Ladies retired to the drawing room after dinner."

    @pytest.mark.xfail(reason="4-space wrap: 'bed.room' (issue #42)")
    def test_room_004(self):
        assert NewlinesToPeriods.process("She locked herself in her bed\n    room.") == "She locked herself in her bed room."

    @pytest.mark.xfail(reason="4-space wrap: 'store.room' (issue #42)")
    def test_room_005(self):
        assert NewlinesToPeriods.process("Old trunks were kept in the store\n    room.") == "Old trunks were kept in the store room."

    @pytest.mark.xfail(reason="4-space wrap: 'work.room' (issue #42)")
    def test_room_006(self):
        assert NewlinesToPeriods.process("She sewed all day in the work\n    room.") == "She sewed all day in the work room."

    @pytest.mark.xfail(reason="4-space wrap: 'show.room' (issue #42)")
    def test_room_007(self):
        assert NewlinesToPeriods.process("New models were displayed in the show\n    room.") == "New models were displayed in the show room."

    @pytest.mark.xfail(reason="4-space wrap: 'board.room' (issue #42)")
    def test_room_008(self):
        assert NewlinesToPeriods.process("Directors met in the board\n    room at noon.") == "Directors met in the board room at noon."

    @pytest.mark.xfail(reason="4-space wrap: 'court.room' (issue #42)")
    def test_room_009(self):
        assert NewlinesToPeriods.process("The jury filed into the court\n    room.") == "The jury filed into the court room."

    @pytest.mark.xfail(reason="4-space wrap: 'gun.room' (issue #42)")
    def test_room_010(self):
        assert NewlinesToPeriods.process("Rifles were stored in the gun\n    room.") == "Rifles were stored in the gun room."

    # ---------------------------------------------------------------- houses / buildings

    @pytest.mark.xfail(reason="4-space wrap: 'farm.house' (issue #42)")
    def test_house_001(self):
        assert NewlinesToPeriods.process("Light burned in the farm\n    house window.") == "Light burned in the farm house window."

    @pytest.mark.xfail(reason="4-space wrap: 'court.house' (issue #42)")
    def test_house_002(self):
        assert NewlinesToPeriods.process("He climbed the steps of the court\n    house.") == "He climbed the steps of the court house."

    @pytest.mark.xfail(reason="4-space wrap: 'work.house' (issue #42)")
    def test_house_003(self):
        assert NewlinesToPeriods.process("The family feared the work\n    house.") == "The family feared the work house."

    @pytest.mark.xfail(reason="4-space wrap: 'club.house' (issue #42)")
    def test_house_004(self):
        assert NewlinesToPeriods.process("Members gathered at the club\n    house.") == "Members gathered at the club house."

    @pytest.mark.xfail(reason="4-space wrap: 'coffee.house' (issue #42)")
    def test_house_005(self):
        assert NewlinesToPeriods.process("Merchants met at the coffee\n    house.") == "Merchants met at the coffee house."

    # ---------------------------------------------------------------- shops / offices

    @pytest.mark.xfail(reason="4-space wrap: 'book.shop' (issue #42)")
    def test_shop_001(self):
        assert NewlinesToPeriods.process("She browsed the book\n    shop all afternoon.") == "She browsed the book shop all afternoon."

    @pytest.mark.xfail(reason="4-space wrap: 'tea.shop' (issue #42)")
    def test_shop_002(self):
        assert NewlinesToPeriods.process("They met at the tea\n    shop near the station.") == "They met at the tea shop near the station."

    @pytest.mark.xfail(reason="4-space wrap: 'barber.shop' (issue #42)")
    def test_shop_003(self):
        assert NewlinesToPeriods.process("He stopped at the barber\n    shop for a trim.") == "He stopped at the barber shop for a trim."

    @pytest.mark.xfail(reason="4-space wrap: 'post.office' (issue #42)")
    def test_shop_004(self):
        assert NewlinesToPeriods.process("She went to the post\n    office at noon.") == "She went to the post office at noon."

    @pytest.mark.xfail(reason="4-space wrap: 'law.office' (issue #42)")
    def test_shop_005(self):
        assert NewlinesToPeriods.process("He called at the law\n    office on the high street.") == "He called at the law office on the high street."

    # ---------------------------------------------------------------- land / outdoor

    @pytest.mark.xfail(reason="4-space wrap: 'farm.land' (issue #42)")
    def test_land_001(self):
        assert NewlinesToPeriods.process("He owned fifty acres of farm\n    land.") == "He owned fifty acres of farm land."

    @pytest.mark.xfail(reason="4-space wrap: 'wood.land' (issue #42)")
    def test_land_002(self):
        assert NewlinesToPeriods.process("The path led through ancient wood\n    land.") == "The path led through ancient wood land."

    @pytest.mark.xfail(reason="4-space wrap: 'moor.land' (issue #42)")
    def test_land_003(self):
        assert NewlinesToPeriods.process("She crossed miles of bleak moor\n    land.") == "She crossed miles of bleak moor land."

    @pytest.mark.xfail(reason="4-space wrap: 'meadow.land' (issue #42)")
    def test_land_004(self):
        assert NewlinesToPeriods.process("Cattle grazed on the flat meadow\n    land.") == "Cattle grazed on the flat meadow land."

    @pytest.mark.xfail(reason="4-space wrap: 'hill.side' (issue #42)")
    def test_land_005(self):
        assert NewlinesToPeriods.process("The flock grazed on the open hill\n    side.") == "The flock grazed on the open hill side."

    # ---------------------------------------------------------------- people / titles

    @pytest.mark.xfail(reason="4-space wrap: 'house.keeper' (issue #42)")
    def test_person_001(self):
        assert NewlinesToPeriods.process("The house\n    keeper ran the establishment.") == "The house keeper ran the establishment."

    @pytest.mark.xfail(reason="4-space wrap: 'book.keeper' (issue #42)")
    def test_person_002(self):
        assert NewlinesToPeriods.process("The firm's trusted book\n    keeper retired at sixty.") == "The firm's trusted book keeper retired at sixty."

    @pytest.mark.xfail(reason="4-space wrap: 'school.master' (issue #42)")
    def test_person_003(self):
        assert NewlinesToPeriods.process("The old school\n    master rang the bell.") == "The old school master rang the bell."

    @pytest.mark.xfail(reason="4-space wrap: 'inn.keeper' (issue #42)")
    def test_person_004(self):
        assert NewlinesToPeriods.process("The inn\n    keeper showed them to their room.") == "The inn keeper showed them to their room."

    @pytest.mark.xfail(reason="4-space wrap: 'gate.keeper' (issue #42)")
    def test_person_005(self):
        assert NewlinesToPeriods.process("The gate\n    keeper waved them through.") == "The gate keeper waved them through."

    # ---------------------------------------------------------------- stations / places

    @pytest.mark.xfail(reason="4-space wrap: 'fire.station' (issue #42)")
    def test_station_001(self):
        assert NewlinesToPeriods.process("The alarm rang at the fire\n    station.") == "The alarm rang at the fire station."

    @pytest.mark.xfail(reason="4-space wrap: 'police.station' (issue #42)")
    def test_station_002(self):
        assert NewlinesToPeriods.process("He was taken to the police\n    station.") == "He was taken to the police station."

    @pytest.mark.xfail(reason="4-space wrap: 'railway.station' (issue #42)")
    def test_station_003(self):
        assert NewlinesToPeriods.process("They drove to the railway\n    station.") == "They drove to the railway station."

    @pytest.mark.xfail(reason="4-space wrap: 'naval.station' (issue #42)")
    def test_station_004(self):
        assert NewlinesToPeriods.process("She reported to the naval\n    station.") == "She reported to the naval station."

    @pytest.mark.xfail(reason="4-space wrap: 'pumping.station' (issue #42)")
    def test_station_005(self):
        assert NewlinesToPeriods.process("Engineers inspected the pumping\n    station.") == "Engineers inspected the pumping station."

    # ---------------------------------------------------------------- departments

    @pytest.mark.xfail(reason="4-space wrap: 'business.department' (issue #42)")
    def test_dept_001(self):
        assert NewlinesToPeriods.process("Young men to assist in the business\n    department.") == "Young men to assist in the business department."

    @pytest.mark.xfail(reason="4-space wrap: 'advertising.department' (issue #42)")
    def test_dept_002(self):
        assert NewlinesToPeriods.process("She ran the advertising\n    department with skill.") == "She ran the advertising department with skill."

    @pytest.mark.xfail(reason="4-space wrap: 'health.department' (issue #42)")
    def test_dept_003(self):
        assert NewlinesToPeriods.process("The health\n    department issued a statement.") == "The health department issued a statement."

    @pytest.mark.xfail(reason="4-space wrap: 'finance.department' (issue #42)")
    def test_dept_004(self):
        assert NewlinesToPeriods.process("He worked in the finance\n    department.") == "He worked in the finance department."

    @pytest.mark.xfail(reason="4-space wrap: 'legal.department' (issue #42)")
    def test_dept_005(self):
        assert NewlinesToPeriods.process("She consulted the legal\n    department.") == "She consulted the legal department."

    @pytest.mark.xfail(reason="4-space wrap: 'research.department' (issue #42)")
    def test_dept_006(self):
        assert NewlinesToPeriods.process("He led the research\n    department for two decades.") == "He led the research department for two decades."

    @pytest.mark.xfail(reason="4-space wrap: 'sales.department' (issue #42)")
    def test_dept_007(self):
        assert NewlinesToPeriods.process("She transferred to the sales\n    department.") == "She transferred to the sales department."

    @pytest.mark.xfail(reason="4-space wrap: 'editorial.department' (issue #42)")
    def test_dept_008(self):
        assert NewlinesToPeriods.process("He joined the editorial\n    department of the newspaper.") == "He joined the editorial department of the newspaper."

    @pytest.mark.xfail(reason="4-space wrap: 'personnel.department' (issue #42)")
    def test_dept_009(self):
        assert NewlinesToPeriods.process("She applied through the personnel\n    department.") == "She applied through the personnel department."

    @pytest.mark.xfail(reason="4-space wrap: 'accounts.department' (issue #42)")
    def test_dept_010(self):
        assert NewlinesToPeriods.process("He spent thirty years in the accounts\n    department.") == "He spent thirty years in the accounts department."

    # ---------------------------------------------------------------- miscellaneous

    @pytest.mark.xfail(reason="4-space wrap: 'night.watchman' (issue #42)")
    def test_misc_001(self):
        assert NewlinesToPeriods.process("The night\n    watchman made his rounds at midnight.") == "The night watchman made his rounds at midnight."

    @pytest.mark.xfail(reason="4-space wrap: 'town.council' (issue #42)")
    def test_misc_002(self):
        assert NewlinesToPeriods.process("He stood for the town\n    council.") == "He stood for the town council."

    @pytest.mark.xfail(reason="4-space wrap: 'foreign.office' (issue #42)")
    def test_misc_003(self):
        assert NewlinesToPeriods.process("The foreign\n    office replied at once.") == "The foreign office replied at once."

    @pytest.mark.xfail(reason="4-space wrap: 'finance.committee' (issue #42)")
    def test_misc_004(self):
        assert NewlinesToPeriods.process("The finance\n    committee approved the budget.") == "The finance committee approved the budget."

    @pytest.mark.xfail(reason="4-space wrap: 'lamp.post' (issue #42)")
    def test_misc_005(self):
        assert NewlinesToPeriods.process("He leaned against the lamp\n    post.") == "He leaned against the lamp post."

    @pytest.mark.xfail(reason="4-space wrap: 'letter.box' (issue #42)")
    def test_misc_006(self):
        assert NewlinesToPeriods.process("Letters came through the letter\n    box at seven.") == "Letters came through the letter box at seven."

    @pytest.mark.xfail(reason="4-space wrap: 'river.bank' (issue #42)")
    def test_misc_007(self):
        assert NewlinesToPeriods.process("They picnicked on the river\n    bank in summer.") == "They picnicked on the river bank in summer."

    @pytest.mark.xfail(reason="4-space wrap: 'corn.field' (issue #42)")
    def test_misc_008(self):
        assert NewlinesToPeriods.process("Poppies grew at the edge of the corn\n    field.") == "Poppies grew at the edge of the corn field."

    @pytest.mark.xfail(reason="4-space wrap: 'market.square' (issue #42)")
    def test_misc_009(self):
        assert NewlinesToPeriods.process("He crossed the market\n    square at noon.") == "He crossed the market square at noon."

    @pytest.mark.xfail(reason="4-space wrap: 'stage.coach' (issue #42)")
    def test_misc_010(self):
        assert NewlinesToPeriods.process("They boarded the stage\n    coach at dawn.") == "They boarded the stage coach at dawn."

    @pytest.mark.xfail(reason="4-space wrap: 'toll.gate' (issue #42)")
    def test_misc_011(self):
        assert NewlinesToPeriods.process("The coachman stopped at the toll\n    gate.") == "The coachman stopped at the toll gate."

    @pytest.mark.xfail(reason="4-space wrap: 'cross.roads' (issue #42)")
    def test_misc_012(self):
        assert NewlinesToPeriods.process("They halted at the cross\n    roads to check the map.") == "They halted at the cross roads to check the map."
