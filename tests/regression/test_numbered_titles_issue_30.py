# -*- coding: UTF-8 -*-
"""
Test cases for Issue #30: Incorrect sentence break on numbered titles.

Covers patterns like 'Part 2.', 'Module 3.', 'Chapter IV.' that should be kept
together as a single unit rather than split on the period after the number.

Reference: https://github.com/craigtrim/fast-sentence-segment/issues/30
"""

import pytest
from typing import Callable

SegmentationFunc = Callable[[str], list[str]]


class TestNumberedTitlesArabicNumerals:
    """Test numbered titles with Arabic numerals (1, 2, 3, etc.)"""

    @pytest.mark.parametrize("text,expected", [
        # Part + Arabic numerals
        ("Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]",
         ["Try crossing this street in India!!", "Part 2. (May 6, 2008) [Video File]"]),

        ("Bush Taxi Part 2. (Sept 29, 2015)",
         ["Bush Taxi Part 2. (Sept 29, 2015)"]),

        ("This is the introduction. Part 1. Welcome to the course.",
         ["This is the introduction.", "Part 1. Welcome to the course."]),

        ("See the previous video. Part 3. Advanced techniques are covered here.",
         ["See the previous video.", "Part 3. Advanced techniques are covered here."]),

        ("The story continues in Part 4. The hero faces new challenges.",
         ["The story continues in Part 4.", "The hero faces new challenges."]),

        ("Watch Part 5. It contains the final revelations.",
         ["Watch Part 5.", "It contains the final revelations."]),

        ("Complete Part 6. Then move to the next section.",
         ["Complete Part 6.", "Then move to the next section."]),

        ("Review Part 7. Understanding this is crucial.",
         ["Review Part 7.", "Understanding this is crucial."]),

        ("Part 8. The conclusion brings everything together.",
         ["Part 8. The conclusion brings everything together."]),

        ("Start with Part 9. You will learn the basics.",
         ["Start with Part 9.", "You will learn the basics."]),

        ("Finish Part 10. The assignment is due tomorrow.",
         ["Finish Part 10.", "The assignment is due tomorrow."]),

        ("Part 11. Introduction to the methodology.",
         ["Part 11. Introduction to the methodology."]),

        ("Skip ahead to Part 12. The summary is helpful.",
         ["Skip ahead to Part 12.", "The summary is helpful."]),

        ("Part 13. Key concepts are explained here.",
         ["Part 13. Key concepts are explained here."]),

        ("Read Part 14. Take notes as you go.",
         ["Read Part 14.", "Take notes as you go."]),

        ("Part 15. This section covers advanced topics.",
         ["Part 15. This section covers advanced topics."]),

        ("Refer to Part 16. Examples are provided.",
         ["Refer to Part 16.", "Examples are provided."]),

        ("Part 17. The exercises will test your knowledge.",
         ["Part 17. The exercises will test your knowledge."]),

        ("Study Part 18. Quiz next week.",
         ["Study Part 18.", "Quiz next week."]),

        ("Part 19. Final review session.",
         ["Part 19. Final review session."]),

        ("Check Part 20. Supplementary materials available.",
         ["Check Part 20.", "Supplementary materials available."]),

        ("Part 21. Guest lecture recording.",
         ["Part 21. Guest lecture recording."]),

        ("Part 22. Lab demonstration video.",
         ["Part 22. Lab demonstration video."]),

        ("Part 23. Case study analysis.",
         ["Part 23. Case study analysis."]),

        ("Part 24. Practical applications discussed.",
         ["Part 24. Practical applications discussed."]),

        ("Part 25. Closing remarks and Q&A.",
         ["Part 25. Closing remarks and Q&A."]),

        # Large numbers
        ("Part 100. Century milestone edition.",
         ["Part 100. Century milestone edition."]),

        ("Part 999. Near the end of the series.",
         ["Part 999. Near the end of the series."]),
    ])
    def test_part_arabic_numerals(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesModule:
    """Test Module + numbers"""

    @pytest.mark.parametrize("text,expected", [
        ("Welcome to the course. Module 1. Getting started with Python.",
         ["Welcome to the course.", "Module 1. Getting started with Python."]),

        ("Module 2. Data structures and algorithms.",
         ["Module 2. Data structures and algorithms."]),

        ("Please complete Module 3. Submit by Friday.",
         ["Please complete Module 3.", "Submit by Friday."]),

        ("Module 4. Object-oriented programming concepts.",
         ["Module 4. Object-oriented programming concepts."]),

        ("Review Module 5. Prepare for the midterm.",
         ["Review Module 5.", "Prepare for the midterm."]),

        ("Module 6. Web development fundamentals.",
         ["Module 6. Web development fundamentals."]),

        ("Start Module 7. Database design principles.",
         ["Start Module 7.", "Database design principles."]),

        ("Module 8. API development and testing.",
         ["Module 8. API development and testing."]),

        ("Complete Module 9. Final project requirements.",
         ["Complete Module 9.", "Final project requirements."]),

        ("Module 10. Security best practices.",
         ["Module 10. Security best practices."]),

        ("Module 11. Cloud computing overview.",
         ["Module 11. Cloud computing overview."]),

        ("Study Module 12. Machine learning basics.",
         ["Study Module 12.", "Machine learning basics."]),

        ("Module 13. DevOps and CI/CD pipelines.",
         ["Module 13. DevOps and CI/CD pipelines."]),

        ("Module 14. Microservices architecture.",
         ["Module 14. Microservices architecture."]),

        ("Module 15. Performance optimization.",
         ["Module 15. Performance optimization."]),

        ("Skip to Module 16. Advanced topics.",
         ["Skip to Module 16.", "Advanced topics."]),

        ("Module 17. Testing strategies.",
         ["Module 17. Testing strategies."]),

        ("Module 18. Code review practices.",
         ["Module 18. Code review practices."]),

        ("Module 19. Documentation standards.",
         ["Module 19. Documentation standards."]),

        ("Module 20. Deployment strategies.",
         ["Module 20. Deployment strategies."]),

        ("Module 21. Monitoring and logging.",
         ["Module 21. Monitoring and logging."]),

        ("Module 22. Scalability patterns.",
         ["Module 22. Scalability patterns."]),

        ("Module 23. Error handling.",
         ["Module 23. Error handling."]),

        ("Module 24. Design patterns.",
         ["Module 24. Design patterns."]),

        ("Module 25. Best practices summary.",
         ["Module 25. Best practices summary."]),

        ("Assignment for Module 26. Due next Monday.",
         ["Assignment for Module 26.", "Due next Monday."]),

        ("Module 27. Bonus content available.",
         ["Module 27. Bonus content available."]),
    ])
    def test_module_arabic_numerals(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesChapter:
    """Test Chapter + numbers"""

    @pytest.mark.parametrize("text,expected", [
        ("Chapter 1. The Beginning. It was a dark and stormy night.",
         ["Chapter 1.", "The Beginning.", "It was a dark and stormy night."]),

        ("I finished reading Chapter 2. The plot thickens.",
         ["I finished reading Chapter 2.", "The plot thickens."]),

        ("Chapter 3. New characters are introduced.",
         ["Chapter 3. New characters are introduced."]),

        ("Turn to Chapter 4. The mystery deepens.",
         ["Turn to Chapter 4.", "The mystery deepens."]),

        ("Chapter 5. A shocking revelation occurs.",
         ["Chapter 5. A shocking revelation occurs."]),

        ("Read Chapter 6. Take notes on the themes.",
         ["Read Chapter 6.", "Take notes on the themes."]),

        ("Chapter 7. The climax approaches.",
         ["Chapter 7. The climax approaches."]),

        ("Chapter 8. Everything changes here.",
         ["Chapter 8. Everything changes here."]),

        ("Study Chapter 9. Key concepts explained.",
         ["Study Chapter 9.", "Key concepts explained."]),

        ("Chapter 10. Midpoint of the story.",
         ["Chapter 10. Midpoint of the story."]),

        ("Chapter 11. Rising action continues.",
         ["Chapter 11. Rising action continues."]),

        ("Chapter 12. Major turning point.",
         ["Chapter 12. Major turning point."]),

        ("Chapter 13. Unlucky for the protagonist.",
         ["Chapter 13. Unlucky for the protagonist."]),

        ("Chapter 14. New setting introduced.",
         ["Chapter 14. New setting introduced."]),

        ("Chapter 15. Flashback sequence.",
         ["Chapter 15. Flashback sequence."]),

        ("Chapter 16. Multiple perspectives.",
         ["Chapter 16. Multiple perspectives."]),

        ("Chapter 17. Tension builds.",
         ["Chapter 17. Tension builds."]),

        ("Chapter 18. Confrontation scene.",
         ["Chapter 18. Confrontation scene."]),

        ("Chapter 19. Unexpected alliance.",
         ["Chapter 19. Unexpected alliance."]),

        ("Chapter 20. Halfway through the book.",
         ["Chapter 20. Halfway through the book."]),

        ("Chapter 21. The chase begins.",
         ["Chapter 21. The chase begins."]),

        ("Chapter 22. A narrow escape.",
         ["Chapter 22. A narrow escape."]),

        ("Chapter 23. Regrouping and planning.",
         ["Chapter 24. Regrouping and planning."]),

        ("Chapter 24. The final plan.",
         ["Chapter 24. The final plan."]),

        ("Chapter 25. Everything comes together.",
         ["Chapter 25. Everything comes together."]),

        ("Chapter 26. The climax.",
         ["Chapter 26. The climax."]),

        ("Chapter 27. Resolution begins.",
         ["Chapter 27. Resolution begins."]),
    ])
    def test_chapter_arabic_numerals(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesSection:
    """Test Section + numbers"""

    @pytest.mark.parametrize("text,expected", [
        ("Section 1. Introduction to the methodology.",
         ["Section 1. Introduction to the methodology."]),

        ("Refer to Section 2. Data collection methods.",
         ["Refer to Section 2.", "Data collection methods."]),

        ("Section 3. Analysis techniques.",
         ["Section 3. Analysis techniques."]),

        ("Section 4. Results and findings.",
         ["Section 4. Results and findings."]),

        ("See Section 5. Discussion of implications.",
         ["See Section 5.", "Discussion of implications."]),

        ("Section 6. Limitations of the study.",
         ["Section 6. Limitations of the study."]),

        ("Section 7. Future research directions.",
         ["Section 7. Future research directions."]),

        ("Section 8. Conclusions.",
         ["Section 8. Conclusions."]),

        ("Section 9. Acknowledgments.",
         ["Section 9. Acknowledgments."]),

        ("Section 10. References.",
         ["Section 10. References."]),

        ("Section 11. Appendix A.",
         ["Section 11. Appendix A."]),

        ("Section 12. Supplementary materials.",
         ["Section 12. Supplementary materials."]),

        ("Section 13. Ethical considerations.",
         ["Section 13. Ethical considerations."]),

        ("Section 14. Statistical methods.",
         ["Section 14. Statistical methods."]),

        ("Section 15. Participant demographics.",
         ["Section 15. Participant demographics."]),

        ("Section 16. Instruments used.",
         ["Section 16. Instruments used."]),

        ("Section 17. Procedures followed.",
         ["Section 17. Procedures followed."]),

        ("Section 18. Data validation.",
         ["Section 18. Data validation."]),

        ("Section 19. Quality control measures.",
         ["Section 19. Quality control measures."]),

        ("Section 20. Preliminary results.",
         ["Section 20. Preliminary results."]),

        ("Section 21. Detailed analysis.",
         ["Section 21. Detailed analysis."]),

        ("Section 22. Comparative findings.",
         ["Section 22. Comparative findings."]),

        ("Section 23. Cross-validation results.",
         ["Section 23. Cross-validation results."]),

        ("Section 24. Summary tables.",
         ["Section 24. Summary tables."]),

        ("Section 25. Final recommendations.",
         ["Section 25. Final recommendations."]),

        # Subsections with decimals
        ("Section 3.1. Methodology. We used a mixed-methods approach.",
         ["Section 3.1.", "Methodology.", "We used a mixed-methods approach."]),

        ("Section 3.2. Participants and setting.",
         ["Section 3.2. Participants and setting."]),
    ])
    def test_section_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesWeek:
    """Test Week + numbers

    Design Decision: Week N. patterns are ALWAYS separate sentences.
    This is an overfitted solution for common academic/course patterns.
    Related GitHub Issue:
        https://github.com/craigtrim/fast-sentence-segment/issues/30#issuecomment-3881265186
    """

    @pytest.mark.parametrize("text,expected", [
        ("Week 1. Course introduction and syllabus.",
         ["Week 1.", "Course introduction and syllabus."]),

        ("Week 2. Fundamentals of programming.",
         ["Week 2.", "Fundamentals of programming."]),

        ("Week 3. Variables and data types.",
         ["Week 3.", "Variables and data types."]),

        ("Week 4. Control flow and loops.",
         ["Week 4.", "Control flow and loops."]),

        ("Week 5. Functions and modules.",
         ["Week 5.", "Functions and modules."]),

        ("Week 6. Object-oriented programming.",
         ["Week 6.", "Object-oriented programming."]),

        ("Week 7. File I/O operations.",
         ["Week 7.", "File I/O operations."]),

        ("Week 8. Error handling.",
         ["Week 8.", "Error handling."]),

        ("Week 9. Midterm review.",
         ["Week 9.", "Midterm review."]),

        ("Week 10. Data structures.",
         ["Week 10.", "Data structures."]),

        ("Week 11. Algorithms.",
         ["Week 11.", "Algorithms."]),

        ("Week 12. Recursion.",
         ["Week 12.", "Recursion."]),

        ("Week 13. Sorting and searching.",
         ["Week 13.", "Sorting and searching."]),

        ("Week 14. Graph algorithms.",
         ["Week 14.", "Graph algorithms."]),

        ("Week 15. Dynamic programming.",
         ["Week 15.", "Dynamic programming."]),

        ("Week 16. Final project work.",
         ["Week 16.", "Final project work."]),

        ("Homework due Week 17. Submit online.",
         ["Homework due Week 17.", "Submit online."]),

        ("Week 18. Guest speaker session.",
         ["Week 18.", "Guest speaker session."]),

        ("Week 19. Lab practical.",
         ["Week 19.", "Lab practical."]),

        ("Week 20. Review session.",
         ["Week 20.", "Review session."]),

        ("Week 21. Final exam preparation.",
         ["Week 21.", "Final exam preparation."]),

        ("Week 22. Project presentations.",
         ["Week 22.", "Project presentations."]),

        ("Week 23. Course wrap-up.",
         ["Week 23.", "Course wrap-up."]),

        ("Week 24. Summer intensive begins.",
         ["Week 24.", "Summer intensive begins."]),

        ("Week 25. Advanced topics.",
         ["Week 25.", "Advanced topics."]),

        ("Assignment for Week 26. Group project.",
         ["Assignment for Week 26.", "Group project."]),

        ("Week 27. Final assessments.",
         ["Week 27.", "Final assessments."]),
    ])
    def test_week_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesStep:
    """Test Step + numbers"""

    @pytest.mark.parametrize("text,expected", [
        ("Step 1. Open the application.",
         ["Step 1. Open the application."]),

        ("Step 2. Click the login button.",
         ["Step 2. Click the login button."]),

        ("Step 3. Enter your credentials.",
         ["Step 3. Enter your credentials."]),

        ("Step 4. Click submit.",
         ["Step 4. Click submit."]),

        ("Step 5. Wait for verification.",
         ["Step 5. Wait for verification."]),

        ("Step 6. Navigate to settings.",
         ["Step 6. Navigate to settings."]),

        ("Step 7. Update your profile.",
         ["Step 7. Update your profile."]),

        ("Step 8. Save changes.",
         ["Step 8. Save changes."]),

        ("Step 9. Log out.",
         ["Step 9. Log out."]),

        ("Step 10. Restart the process.",
         ["Step 10. Restart the process."]),

        ("Complete Step 11. Verify installation.",
         ["Complete Step 11.", "Verify installation."]),

        ("Step 12. Run diagnostics.",
         ["Step 12. Run diagnostics."]),

        ("Step 13. Check for updates.",
         ["Step 13. Check for updates."]),

        ("Step 14. Install dependencies.",
         ["Step 14. Install dependencies."]),

        ("Step 15. Configure environment.",
         ["Step 15. Configure environment."]),

        ("Step 16. Test connection.",
         ["Step 16. Test connection."]),

        ("Step 17. Deploy to production.",
         ["Step 17. Deploy to production."]),

        ("Step 18. Monitor logs.",
         ["Step 18. Monitor logs."]),

        ("Step 19. Set up backups.",
         ["Step 19. Set up backups."]),

        ("Step 20. Document process.",
         ["Step 20. Document process."]),

        ("Step 21. Train team members.",
         ["Step 21. Train team members."]),

        ("Step 22. Schedule maintenance.",
         ["Step 22. Schedule maintenance."]),

        ("Step 23. Review security.",
         ["Step 23. Review security."]),

        ("Step 24. Optimize performance.",
         ["Step 24. Optimize performance."]),

        ("Step 25. Finalize deployment.",
         ["Step 25. Finalize deployment."]),

        ("Follow Step 26. Additional configuration.",
         ["Follow Step 26.", "Additional configuration."]),

        ("Step 27. Cleanup temporary files.",
         ["Step 27. Cleanup temporary files."]),
    ])
    def test_step_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesPhase:
    """Test Phase + numbers"""

    @pytest.mark.parametrize("text,expected", [
        ("Phase 1. Planning and requirements.",
         ["Phase 1. Planning and requirements."]),

        ("Phase 2. Design and architecture.",
         ["Phase 2. Design and architecture."]),

        ("Phase 3. Implementation begins.",
         ["Phase 3. Implementation begins."]),

        ("Phase 4. Testing and QA.",
         ["Phase 4. Testing and QA."]),

        ("Phase 5. Deployment preparation.",
         ["Phase 5. Deployment preparation."]),

        ("Phase 6. Go-live.",
         ["Phase 6. Go-live."]),

        ("Phase 7. Post-launch support.",
         ["Phase 7. Post-launch support."]),

        ("Phase 8. Optimization.",
         ["Phase 8. Optimization."]),

        ("Phase 9. Maintenance mode.",
         ["Phase 9. Maintenance mode."]),

        ("Phase 10. End of life planning.",
         ["Phase 10. End of life planning."]),

        ("We are in Phase 11. Expansion planning.",
         ["We are in Phase 11.", "Expansion planning."]),

        ("Phase 12. Market research.",
         ["Phase 12. Market research."]),

        ("Phase 13. Prototype development.",
         ["Phase 13. Prototype development."]),

        ("Phase 14. User testing.",
         ["Phase 14. User testing."]),

        ("Phase 15. Feedback integration.",
         ["Phase 15. Feedback integration."]),

        ("Phase 16. Beta release.",
         ["Phase 16. Beta release."]),

        ("Phase 17. Bug fixing.",
         ["Phase 17. Bug fixing."]),

        ("Phase 18. Performance tuning.",
         ["Phase 18. Performance tuning."]),

        ("Phase 19. Security hardening.",
         ["Phase 19. Security hardening."]),

        ("Phase 20. Documentation.",
         ["Phase 20. Documentation."]),

        ("Phase 21. Training materials.",
         ["Phase 21. Training materials."]),

        ("Phase 22. Marketing launch.",
         ["Phase 22. Marketing launch."]),

        ("Phase 23. Customer onboarding.",
         ["Phase 23. Customer onboarding."]),

        ("Phase 24. Feature enhancement.",
         ["Phase 24. Feature enhancement."]),

        ("Phase 25. Long-term support.",
         ["Phase 25. Long-term support."]),

        ("Entering Phase 26. Major upgrade.",
         ["Entering Phase 26.", "Major upgrade."]),

        ("Phase 27. Migration planning.",
         ["Phase 27. Migration planning."]),
    ])
    def test_phase_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesUnit:
    """Test Unit + numbers"""

    @pytest.mark.parametrize("text,expected", [
        ("Unit 1. Introduction to biology.",
         ["Unit 1. Introduction to biology."]),

        ("Unit 2. Cell structure.",
         ["Unit 2. Cell structure."]),

        ("Unit 3. Genetics.",
         ["Unit 3. Genetics."]),

        ("Unit 4. Evolution.",
         ["Unit 4. Evolution."]),

        ("Unit 5. Ecology.",
         ["Unit 5. Ecology."]),

        ("Study Unit 6. Human anatomy.",
         ["Study Unit 6.", "Human anatomy."]),

        ("Unit 7. Physiology.",
         ["Unit 7. Physiology."]),

        ("Unit 8. Biochemistry.",
         ["Unit 8. Biochemistry."]),

        ("Unit 9. Microbiology.",
         ["Unit 9. Microbiology."]),

        ("Unit 10. Plant biology.",
         ["Unit 10. Plant biology."]),

        ("Unit 11. Animal behavior.",
         ["Unit 11. Animal behavior."]),

        ("Unit 12. Conservation.",
         ["Unit 12. Conservation."]),

        ("Unit 13. Biodiversity.",
         ["Unit 13. Biodiversity."]),

        ("Unit 14. Molecular biology.",
         ["Unit 14. Molecular biology."]),

        ("Unit 15. Immunology.",
         ["Unit 15. Immunology."]),

        ("Unit 16. Neuroscience.",
         ["Unit 16. Neuroscience."]),

        ("Unit 17. Developmental biology.",
         ["Unit 17. Developmental biology."]),

        ("Unit 18. Marine biology.",
         ["Unit 18. Marine biology."]),

        ("Unit 19. Taxonomy.",
         ["Unit 19. Taxonomy."]),

        ("Unit 20. Scientific method.",
         ["Unit 20. Scientific method."]),

        ("Unit 21. Laboratory techniques.",
         ["Unit 21. Laboratory techniques."]),

        ("Unit 22. Data analysis.",
         ["Unit 22. Data analysis."]),

        ("Unit 23. Research design.",
         ["Unit 23. Research design."]),

        ("Unit 24. Ethics in science.",
         ["Unit 24. Ethics in science."]),

        ("Unit 25. Review and synthesis.",
         ["Unit 25. Review and synthesis."]),

        ("Complete Unit 26. Final project.",
         ["Complete Unit 26.", "Final project."]),

        ("Unit 27. Advanced topics.",
         ["Unit 27. Advanced topics."]),
    ])
    def test_unit_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesLevel:
    """Test Level + numbers"""

    @pytest.mark.parametrize("text,expected", [
        ("Level 1. Beginner basics.",
         ["Level 1. Beginner basics."]),

        ("Level 2. Elementary skills.",
         ["Level 2. Elementary skills."]),

        ("Level 3. Intermediate techniques.",
         ["Level 3. Intermediate techniques."]),

        ("Level 4. Advanced methods.",
         ["Level 4. Advanced methods."]),

        ("Level 5. Expert strategies.",
         ["Level 5. Expert strategies."]),

        ("Complete Level 6. Unlock new content.",
         ["Complete Level 6.", "Unlock new content."]),

        ("Level 7. Boss fight.",
         ["Level 7. Boss fight."]),

        ("Level 8. Hidden treasures.",
         ["Level 8. Hidden treasures."]),

        ("Level 9. Puzzle solving.",
         ["Level 9. Puzzle solving."]),

        ("Level 10. Checkpoint reached.",
         ["Level 10. Checkpoint reached."]),

        ("Level 11. New abilities.",
         ["Level 11. New abilities."]),

        ("Level 12. Team challenges.",
         ["Level 12. Team challenges."]),

        ("Level 13. Timed missions.",
         ["Level 13. Timed missions."]),

        ("Level 14. Stealth required.",
         ["Level 14. Stealth required."]),

        ("Level 15. Combat intensive.",
         ["Level 15. Combat intensive."]),

        ("Level 16. Exploration focus.",
         ["Level 16. Exploration focus."]),

        ("Level 17. Character development.",
         ["Level 17. Character development."]),

        ("Level 18. Story climax.",
         ["Level 18. Story climax."]),

        ("Level 19. Skill mastery.",
         ["Level 19. Skill mastery."]),

        ("Level 20. Endgame content.",
         ["Level 20. Endgame content."]),

        ("Level 21. Bonus stage.",
         ["Level 21. Bonus stage."]),

        ("Level 22. Secret area.",
         ["Level 22. Secret area."]),

        ("Level 23. Speedrun challenge.",
         ["Level 23. Speedrun challenge."]),

        ("Level 24. Hardcore mode.",
         ["Level 24. Hardcore mode."]),

        ("Level 25. Achievement unlocked.",
         ["Level 25. Achievement unlocked."]),

        ("Advance to Level 26. New game plus.",
         ["Advance to Level 26.", "New game plus."]),

        ("Level 27. Ultimate challenge.",
         ["Level 27. Ultimate challenge."]),
    ])
    def test_level_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesStage:
    """Test Stage + numbers"""

    @pytest.mark.parametrize("text,expected", [
        ("Stage 1. Foundation building.",
         ["Stage 1. Foundation building."]),

        ("Stage 2. Growth period.",
         ["Stage 2. Growth period."]),

        ("Stage 3. Maturity phase.",
         ["Stage 3. Maturity phase."]),

        ("Stage 4. Decline or renewal.",
         ["Stage 4. Decline or renewal."]),

        ("Stage 5. Transformation.",
         ["Stage 5. Transformation."]),

        ("We are at Stage 6. Critical juncture.",
         ["We are at Stage 6.", "Critical juncture."]),

        ("Stage 7. Consolidation.",
         ["Stage 7. Consolidation."]),

        ("Stage 8. Expansion.",
         ["Stage 8. Expansion."]),

        ("Stage 9. Diversification.",
         ["Stage 9. Diversification."]),

        ("Stage 10. Integration.",
         ["Stage 10. Integration."]),

        ("Stage 11. Optimization.",
         ["Stage 11. Optimization."]),

        ("Stage 12. Innovation.",
         ["Stage 12. Innovation."]),

        ("Stage 13. Disruption.",
         ["Stage 13. Disruption."]),

        ("Stage 14. Adaptation.",
         ["Stage 14. Adaptation."]),

        ("Stage 15. Stabilization.",
         ["Stage 15. Stabilization."]),

        ("Stage 16. Acceleration.",
         ["Stage 16. Acceleration."]),

        ("Stage 17. Pivot point.",
         ["Stage 17. Pivot point."]),

        ("Stage 18. Scaling up.",
         ["Stage 18. Scaling up."]),

        ("Stage 19. Market entry.",
         ["Stage 19. Market entry."]),

        ("Stage 20. Competitive positioning.",
         ["Stage 20. Competitive positioning."]),

        ("Stage 21. Brand establishment.",
         ["Stage 21. Brand establishment."]),

        ("Stage 22. Customer acquisition.",
         ["Stage 22. Customer acquisition."]),

        ("Stage 23. Retention focus.",
         ["Stage 23. Retention focus."]),

        ("Stage 24. Revenue optimization.",
         ["Stage 24. Revenue optimization."]),

        ("Stage 25. Sustainable growth.",
         ["Stage 25. Sustainable growth."]),

        ("Approaching Stage 26. Market leadership.",
         ["Approaching Stage 26.", "Market leadership."]),

        ("Stage 27. Global expansion.",
         ["Stage 27. Global expansion."]),
    ])
    def test_stage_numbers(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesRomanNumerals:
    """Test numbered titles with Roman numerals"""

    @pytest.mark.parametrize("text,expected", [
        # Part with Roman numerals
        ("Part I. The introduction begins here.",
         ["Part I. The introduction begins here."]),

        ("Part II. The story continues.",
         ["Part II. The story continues."]),

        ("Part III. Major developments.",
         ["Part III. Major developments."]),

        ("Part IV. The climax approaches.",
         ["Part IV. The climax approaches."]),

        ("Part V. Resolution.",
         ["Part V. Resolution."]),

        ("Part VI. Epilogue.",
         ["Part VI. Epilogue."]),

        ("Part VII. Bonus content.",
         ["Part VII. Bonus content."]),

        ("Part VIII. Extended edition.",
         ["Part VIII. Extended edition."]),

        ("Part IX. Penultimate chapter.",
         ["Part IX. Penultimate chapter."]),

        ("Part X. Final installment.",
         ["Part X. Final installment."]),

        ("Read Part XI. New characters introduced.",
         ["Read Part XI.", "New characters introduced."]),

        ("Part XII. The plot thickens.",
         ["Part XII. The plot thickens."]),

        ("Part XIII. Unlucky events.",
         ["Part XIII. Unlucky events."]),

        ("Part XIV. Turning point.",
         ["Part XIV. Turning point."]),

        ("Part XV. Midpoint.",
         ["Part XV. Midpoint."]),

        ("Part XVI. Rising action.",
         ["Part XVI. Rising action."]),

        ("Part XVII. Complications arise.",
         ["Part XVII. Complications arise."]),

        ("Part XVIII. Confrontation.",
         ["Part XVIII. Confrontation."]),

        ("Part XIX. Near the end.",
         ["Part XIX. Near the end."]),

        ("Part XX. Twentieth installment.",
         ["Part XX. Twentieth installment."]),

        ("Part XXI. Twenty-first chapter.",
         ["Part XXI. Twenty-first chapter."]),

        ("Part XXV. Quarter century mark.",
         ["Part XXV. Quarter century mark."]),

        ("Part XXX. Thirtieth edition.",
         ["Part XXX. Thirtieth edition."]),

        ("Part L. Fiftieth anniversary.",
         ["Part L. Fiftieth anniversary."]),

        ("Part C. Centennial edition.",
         ["Part C. Centennial edition."]),

        # Chapter with Roman numerals
        ("Chapter I. Opening scene.",
         ["Chapter I. Opening scene."]),

        ("Chapter II. Development.",
         ["Chapter II. Development."]),

        ("Chapter III. Complications.",
         ["Chapter III. Complications."]),

        ("Chapter IV. Crisis point.",
         ["Chapter IV. Crisis point."]),

        ("Chapter V. Resolution begins.",
         ["Chapter V. Resolution begins."]),

        ("Chapter X. Key turning point.",
         ["Chapter X. Key turning point."]),

        ("Chapter XV. Midway through.",
         ["Chapter XV. Midway through."]),

        ("Chapter XX. Major milestone.",
         ["Chapter XX. Major milestone."]),

        # Module with Roman numerals
        ("Module I. Foundations.",
         ["Module I. Foundations."]),

        ("Module II. Building blocks.",
         ["Module II. Building blocks."]),

        ("Module III. Advanced concepts.",
         ["Module III. Advanced concepts."]),

        ("Module IV. Practical applications.",
         ["Module IV. Practical applications."]),

        ("Module V. Synthesis.",
         ["Module V. Synthesis."]),

        # Section with Roman numerals
        ("Section I. Background.",
         ["Section I. Background."]),

        ("Section II. Methodology.",
         ["Section II. Methodology."]),

        ("Section III. Results.",
         ["Section III. Results."]),

        ("Section IV. Discussion.",
         ["Section IV. Discussion."]),

        ("Section V. Conclusion.",
         ["Section V. Conclusion."]),
    ])
    def test_roman_numerals(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesLetters:
    """Test numbered titles with letters"""

    @pytest.mark.parametrize("text,expected", [
        ("Part A. First section.",
         ["Part A. First section."]),

        ("Part B. Second section.",
         ["Part B. Second section."]),

        ("Part C. Third section.",
         ["Part C. Third section."]),

        ("Part D. Fourth section.",
         ["Part D. Fourth section."]),

        ("Part E. Fifth section.",
         ["Part E. Fifth section."]),

        ("Part F. Sixth section.",
         ["Part F. Sixth section."]),

        ("Part G. Seventh section.",
         ["Part G. Seventh section."]),

        ("Part H. Eighth section.",
         ["Part H. Eighth section."]),

        ("Part I. Ninth section.",
         ["Part I. Ninth section."]),

        ("Part J. Tenth section.",
         ["Part J. Tenth section."]),

        ("Part K. Eleventh section.",
         ["Part K. Eleventh section."]),

        ("Part L. Twelfth section.",
         ["Part L. Twelfth section."]),

        ("Part M. Thirteenth section.",
         ["Part M. Thirteenth section."]),

        ("Part N. Fourteenth section.",
         ["Part N. Fourteenth section."]),

        ("Part O. Fifteenth section.",
         ["Part O. Fifteenth section."]),

        ("Part P. Sixteenth section.",
         ["Part P. Sixteenth section."]),

        ("Part Q. Seventeenth section.",
         ["Part Q. Seventeenth section."]),

        ("Part R. Eighteenth section.",
         ["Part R. Eighteenth section."]),

        ("Part S. Nineteenth section.",
         ["Part S. Nineteenth section."]),

        ("Part T. Twentieth section.",
         ["Part T. Twentieth section."]),

        ("Part U. Twenty-first section.",
         ["Part U. Twenty-first section."]),

        ("Part V. Twenty-second section.",
         ["Part V. Twenty-second section."]),

        ("Part W. Twenty-third section.",
         ["Part W. Twenty-third section."]),

        ("Part X. Twenty-fourth section.",
         ["Part X. Twenty-fourth section."]),

        ("Part Y. Twenty-fifth section.",
         ["Part Y. Twenty-fifth section."]),

        ("Part Z. Final section.",
         ["Part Z. Final section."]),

        # Other keywords with letters
        ("Section A. Overview.",
         ["Section A. Overview."]),

        ("Section B. Details.",
         ["Section B. Details."]),

        ("Module A. Introduction.",
         ["Module A. Introduction."]),

        ("Module B. Practice.",
         ["Module B. Practice."]),

        ("Chapter A. Prologue.",
         ["Chapter A. Prologue."]),

        ("Chapter B. Beginning.",
         ["Chapter B. Beginning."]),

        ("Appendix A. Supplementary data.",
         ["Appendix A. Supplementary data."]),

        ("Appendix B. Additional resources.",
         ["Appendix B. Additional resources."]),
    ])
    def test_letter_designations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesAbbreviatedForms:
    """Test abbreviated forms (Ch., Sec., Pt., etc.)"""

    @pytest.mark.parametrize("text,expected", [
        # Ch. (Chapter abbreviated)
        ("Ch. 1. The beginning.",
         ["Ch. 1. The beginning."]),

        ("Ch. 2. Developments.",
         ["Ch. 2. Developments."]),

        ("Ch. 3. The plot thickens.",
         ["Ch. 3. The plot thickens."]),

        ("See Ch. 4. Important details there.",
         ["See Ch. 4.", "Important details there."]),

        ("Ch. 5. Major turning point.",
         ["Ch. 5. Major turning point."]),

        ("Ch. 10. Midway through.",
         ["Ch. 10. Midway through."]),

        ("Ch. 15. Climax approaches.",
         ["Ch. 15. Climax approaches."]),

        ("Ch. 20. Resolution.",
         ["Ch. 20. Resolution."]),

        ("Ch. 25. Epilogue.",
         ["Ch. 25. Epilogue."]),

        # Sec. (Section abbreviated)
        ("Sec. 1. Introduction.",
         ["Sec. 1. Introduction."]),

        ("Sec. 2. Methodology.",
         ["Sec. 2. Methodology."]),

        ("Sec. 3. Results.",
         ["Sec. 3. Results."]),

        ("Refer to Sec. 4. Discussion section.",
         ["Refer to Sec. 4.", "Discussion section."]),

        ("Sec. 5. Conclusions.",
         ["Sec. 5. Conclusions."]),

        ("Sec. 3.1. Subsection details.",
         ["Sec. 3.1. Subsection details."]),

        ("Sec. 3.2. Additional information.",
         ["Sec. 3.2. Additional information."]),

        # Mod. (Module abbreviated)
        ("Mod. 1. Getting started.",
         ["Mod. 1. Getting started."]),

        ("Mod. 2. Core concepts.",
         ["Mod. 2. Core concepts."]),

        ("Mod. 3. Advanced topics.",
         ["Mod. 3. Advanced topics."]),

        ("Complete Mod. 4. Final assignment.",
         ["Complete Mod. 4.", "Final assignment."]),

        # Vol. (Volume abbreviated)
        ("Vol. 1. First collection.",
         ["Vol. 1. First collection."]),

        ("Vol. 2. Second collection.",
         ["Vol. 2. Second collection."]),

        ("Vol. 3. Third collection.",
         ["Vol. 3. Third collection."]),

        ("Read Vol. 4. Conclusive volume.",
         ["Read Vol. 4.", "Conclusive volume."]),

        ("Vol. 10. Special anniversary edition.",
         ["Vol. 10. Special anniversary edition."]),

        # Pt. (Part abbreviated) - Note: already handled by existing code
        ("Pt. 1. Introduction.",
         ["Pt. 1. Introduction."]),

        ("Pt. 2. Development.",
         ["Pt. 2. Development."]),

        ("Pt. 3. Conclusion.",
         ["Pt. 3. Conclusion."]),

        ("See Pt. 4. Additional context.",
         ["See Pt. 4.", "Additional context."]),
    ])
    def test_abbreviated_forms(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesCaseVariations:
    """Test case variations (uppercase, lowercase, title case)"""

    @pytest.mark.parametrize("text,expected", [
        # Uppercase
        ("PART 1. ALL CAPS INTRODUCTION.",
         ["PART 1. ALL CAPS INTRODUCTION."]),

        ("CHAPTER 2. UPPERCASE TEXT.",
         ["CHAPTER 2. UPPERCASE TEXT."]),

        ("MODULE 3. SHOUTING MODE.",
         ["MODULE 3. SHOUTING MODE."]),

        ("SECTION 4. EMPHASIS.",
         ["SECTION 4. EMPHASIS."]),

        # Lowercase (less common but possible)
        ("part 1. lowercase beginning.",
         ["part 1. lowercase beginning."]),

        ("chapter 2. all lowercase.",
         ["chapter 2. all lowercase."]),

        ("module 3. no caps here.",
         ["module 3. no caps here."]),

        ("section 4. minimal emphasis.",
         ["section 4. minimal emphasis."]),

        # Title Case (most common)
        ("Part 1. Title Case Standard.",
         ["Part 1. Title Case Standard."]),

        ("Chapter 2. Proper Formatting.",
         ["Chapter 2. Proper Formatting."]),

        ("Module 3. Professional Style.",
         ["Module 3. Professional Style."]),

        ("Section 4. Conventional Format.",
         ["Section 4. Conventional Format."]),

        # Mixed case in same text
        ("Read PART 1. Then move to Part 2. Finally see part 3.",
         ["Read PART 1.", "Then move to Part 2.", "Finally see part 3."]),
    ])
    def test_case_variations(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesWithParentheticals:
    """Test numbered titles with parenthetical content"""

    @pytest.mark.parametrize("text,expected", [
        # With dates
        ("Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]",
         ["Try crossing this street in India!!", "Part 2. (May 6, 2008) [Video File]"]),

        ("Bush Taxi Part 2. (Sept 29, 2015)",
         ["Bush Taxi Part 2. (Sept 29, 2015)"]),

        ("Chapter 5. (Published 2020) Major updates included.",
         ["Chapter 5. (Published 2020) Major updates included."]),

        ("Module 3. (Updated March 2024) New content added.",
         ["Module 3. (Updated March 2024) New content added."]),

        ("Section 7. (Revised December 2023) See latest changes.",
         ["Section 7. (Revised December 2023) See latest changes."]),

        # With descriptors
        ("Part 2. (Revised) New edition available.",
         ["Part 2. (Revised) New edition available."]),

        ("Chapter 10. (Optional) Supplementary reading.",
         ["Chapter 10. (Optional) Supplementary reading."]),

        ("Module 5. (Advanced) For experienced users only.",
         ["Module 5. (Advanced) For experienced users only."]),

        ("Section 3. (Experimental) Approach with caution.",
         ["Section 3. (Experimental) Approach with caution."]),

        ("Week 4. (Intensive) Heavy workload expected.",
         ["Week 4.", "(Intensive) Heavy workload expected."]),

        # With notes
        ("Part 1. (See also Part 3) Related content.",
         ["Part 1. (See also Part 3) Related content."]),

        ("Chapter 8. (Contains spoilers) Read carefully.",
         ["Chapter 8. (Contains spoilers) Read carefully."]),

        ("Module 6. (Prerequisites required) Check your readiness.",
         ["Module 6. (Prerequisites required) Check your readiness."]),

        # With brackets
        ("Part 2. [Video File] Available online.",
         ["Part 2. [Video File] Available online."]),

        ("Chapter 3. [Audiobook] Now streaming.",
         ["Chapter 3. [Audiobook] Now streaming."]),

        ("Module 4. [PDF Download] Printable version.",
         ["Module 4. [PDF Download] Printable version."]),

        # Multiple parentheticals
        ("Part 2. (May 6, 2008) [Video File] Available now.",
         ["Part 2. (May 6, 2008) [Video File] Available now."]),

        ("Chapter 5. (Revised) (2024 Edition) [Digital] New format.",
         ["Chapter 5. (Revised) (2024 Edition) [Digital] New format."]),
    ])
    def test_with_parentheticals(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesEdgeCases:
    """Test edge cases and complex scenarios"""

    @pytest.mark.parametrize("text,expected", [
        # Multiple numbered titles in sequence
        ("Part 1. Introduction. Part 2. Development. Part 3. Conclusion.",
         ["Part 1. Introduction.", "Part 2. Development.", "Part 3. Conclusion."]),

        ("Chapter 1. Beginning. Chapter 2. Middle. Chapter 3. End.",
         ["Chapter 1. Beginning.", "Chapter 2. Middle.", "Chapter 3. End."]),

        # Mixed keywords
        ("Part 1. Overview. Chapter 2. Details. Section 3. Summary.",
         ["Part 1. Overview.", "Chapter 2. Details.", "Section 3. Summary."]),

        # At start of text
        ("Part 1. This starts immediately.",
         ["Part 1. This starts immediately."]),

        ("Module 1. No preamble here.",
         ["Module 1. No preamble here."]),

        # At end of text
        ("This concludes in Part 5.",
         ["This concludes in Part 5."]),

        ("Continue reading in Chapter 10.",
         ["Continue reading in Chapter 10."]),

        # With questions
        ("Have you read Part 3. What did you think?",
         ["Have you read Part 3.", "What did you think?"]),

        ("Did you complete Module 5. Submit your work now.",
         ["Did you complete Module 5.", "Submit your work now."]),

        # With exclamations
        ("Amazing content in Part 7. Don't miss it!",
         ["Amazing content in Part 7.", "Don't miss it!"]),

        ("Wow! Check out Chapter 12. It's incredible!",
         ["Wow!", "Check out Chapter 12.", "It's incredible!"]),

        # With quotations
        ('"Read Part 2." said the teacher.',
         ['"Read Part 2." said the teacher.']),

        ('The sign said "Chapter 5. Important information ahead."',
         ['The sign said "Chapter 5. Important information ahead."']),

        # With colons
        ("Assignment: Part 3. Complete by Friday.",
         ["Assignment: Part 3.", "Complete by Friday."]),

        ("Required reading: Chapter 7. Quiz on Monday.",
         ["Required reading: Chapter 7.", "Quiz on Monday."]),

        # With semicolons
        ("Study Part 4. Review the examples; practice the exercises.",
         ["Study Part 4.", "Review the examples; practice the exercises."]),

        # Numbers with leading zeros (unusual but possible)
        ("Part 01. First of many.",
         ["Part 01. First of many."]),

        ("Chapter 007. Special edition.",
         ["Chapter 007. Special edition."]),

        # Three-digit numbers
        ("Part 100. Centennial edition.",
         ["Part 100. Centennial edition."]),

        ("Chapter 365. Daily reading complete.",
         ["Chapter 365. Daily reading complete."]),

        # Decimal subsections
        ("Section 2.1. First subsection.",
         ["Section 2.1. First subsection."]),

        ("Section 2.1.1. Nested subsection.",
         ["Section 2.1.1. Nested subsection."]),

        ("Chapter 3.14. Mathematical references.",
         ["Chapter 3.14. Mathematical references."]),

        # With hyphens in numbers
        ("Part 2-A. Alternate version.",
         ["Part 2-A. Alternate version."]),

        ("Section 3-1. Alternative numbering.",
         ["Section 3-1. Alternative numbering."]),

        # Combined Roman and Arabic
        ("Part II.3. Mixed numbering system.",
         ["Part II.3. Mixed numbering system."]),
    ])
    def test_edge_cases(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesRealWorldExamples:
    """Real-world examples from the issue and corpus"""

    @pytest.mark.parametrize("text,expected", [
        # From issue #30
        ("Try crossing this street in India!! Part 2. (May 6, 2008) [Video File]",
         ["Try crossing this street in India!!", "Part 2. (May 6, 2008) [Video File]"]),

        ("Bush Taxi Part 2. (Sept 29, 2015)",
         ["Bush Taxi Part 2. (Sept 29, 2015)"]),

        # Educational materials
        ("Assignment Module 3. Overview",
         ["Assignment Module 3.", "Overview"]),

        ("Week 5. Introduction to Economics",
         ["Week 5.", "Introduction to Economics"]),

        # Video series
        ("Cooking Basics Part 1. Knife skills.",
         ["Cooking Basics Part 1.", "Knife skills."]),

        ("Guitar Lessons Part 12. Advanced techniques.",
         ["Guitar Lessons Part 12.", "Advanced techniques."]),

        # Tutorial content
        ("Python Tutorial Step 1. Installing Python.",
         ["Python Tutorial Step 1.", "Installing Python."]),

        ("Web Development Step 5. CSS styling basics.",
         ["Web Development Step 5.", "CSS styling basics."]),

        # Book series
        ("Fantasy Series Part III. The final battle.",
         ["Fantasy Series Part III.", "The final battle."]),

        ("Mystery Collection Vol. 2. Classic whodunits.",
         ["Mystery Collection Vol. 2.", "Classic whodunits."]),

        # Course materials
        ("Lecture notes Week 3. Covering thermodynamics.",
         ["Lecture notes Week 3.", "Covering thermodynamics."]),

        ("Lab exercise Module 7. Titration procedures.",
         ["Lab exercise Module 7.", "Titration procedures."]),

        # Documentation
        ("User guide Chapter 4. Troubleshooting common issues.",
         ["User guide Chapter 4.", "Troubleshooting common issues."]),

        ("API reference Section 2. Authentication methods.",
         ["API reference Section 2.", "Authentication methods."]),

        # Podcasts
        ("Tech Talk Episode Part 2. Cloud computing trends.",
         ["Tech Talk Episode Part 2.", "Cloud computing trends."]),

        # Newsletters
        ("Weekly Update Week 15. Company milestones.",
         ["Weekly Update Week 15.", "Company milestones."]),

        # Training materials
        ("Safety training Module 2. Fire procedures.",
         ["Safety training Module 2.", "Fire procedures."]),

        ("Onboarding Phase 1. Company culture overview.",
         ["Onboarding Phase 1.", "Company culture overview."]),

        # Game walkthrough
        ("Boss Strategy Level 8. Defeat the dragon.",
         ["Boss Strategy Level 8.", "Defeat the dragon."]),

        # Recipe series
        ("Baking 101 Part 4. Working with yeast.",
         ["Baking 101 Part 4.", "Working with yeast."]),

        # Fitness programs
        ("Workout Plan Week 2. Strength building.",
         ["Workout Plan Week 2.", "Strength building."]),

        # Language learning
        ("Spanish Lessons Unit 6. Past tense verbs.",
         ["Spanish Lessons Unit 6.", "Past tense verbs."]),

        # Project phases
        ("Construction Phase 3. Foundation work begins.",
         ["Construction Phase 3.", "Foundation work begins."]),

        # Conference sessions
        ("Conference Day 2. Keynote speaker at 9am.",
         ["Conference Day 2.", "Keynote speaker at 9am."]),
    ])
    def test_real_world_examples(self, segment: SegmentationFunc, text: str, expected: list[str]):
        assert segment(text) == expected


class TestNumberedTitlesNegativeCases:
    """Cases that should NOT be treated as numbered titles"""

    @pytest.mark.parametrize("text,expected", [
        # Cost/price patterns - "Cost 5." should split
        ("The total cost is $5. Next, we calculate tax.",
         ["The total cost is $5.", "Next, we calculate tax."]),

        ("Cost 5. New calculation begins.",
         ["Cost 5.", "New calculation begins."]),

        # Regular words that happen to be followed by numbers
        ("I bought 3. She bought 5.",
         ["I bought 3.", "She bought 5."]),

        ("Count to 10. Then start over.",
         ["Count to 10.", "Then start over."]),

        # Numbers at end of sentence (not titles)
        ("There were 5. I counted them.",
         ["There were 5.", "I counted them."]),

        ("The answer is 42. Don't panic.",
         ["The answer is 42.", "Don't panic."]),

        # Abbreviations that aren't titles (should already be handled)
        ("Call ext. 5. Ask for John.",
         ["Call ext. 5.", "Ask for John."]),

        ("See page 10. Then continue reading.",
         ["See page 10.", "Then continue reading."]),

        # Dates should not match
        ("On Jan. 5. we will meet.",
         ["On Jan. 5. we will meet."]),

        ("By Dec. 25. everything must be done.",
         ["By Dec. 25. everything must be done."]),
    ])
    def test_negative_cases(self, segment: SegmentationFunc, text: str, expected: list[str]):
        """These should NOT trigger numbered title handling"""
        assert segment(text) == expected
