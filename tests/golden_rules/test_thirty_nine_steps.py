# -*- coding: utf-8 -*-
"""
Test Suite: The Thirty-Nine Steps

Test cases using text from "The Thirty-Nine Steps" by John Buchan.

GitHub Issue: TBD
"""
import pytest
from fast_sentence_segment import segment_text


class TestThirtyNineSteps:
    """Test cases from The Thirty-Nine Steps."""

    def test_parapet_bridge(self):
        text = "I pulled myself up on the parapet of the bridge and filled my pipe. I began to detect an ally."
        expected = ["I pulled myself up on the parapet of the bridge and filled my pipe.", "I began to detect an ally."]
        assert segment_text(text, flatten=True) == expected

    def test_young_innkeeper(self):
        text = '"You\'re young to be an innkeeper," I said.'
        expected = ['"You\'re young to be an innkeeper," I said.']
        assert segment_text(text, flatten=True) == expected

    def test_father_died_business(self):
        text = '"My father died a year ago and left me the business. I live there with my grandmother. It\'s a slow job for a young man, and it wasn\'t my choice of profession."'
        expected = ['"My father died a year ago and left me the business. I live there with my grandmother. It\'s a slow job for a young man, and it wasn\'t my choice of profession."']
        assert segment_text(text, flatten=True) == expected

    def test_not_now_eagerly(self):
        text = '"Not now," he said eagerly. "Maybe in the old days when you had pilgrims and ballad-makers and highwaymen and mail-coaches on the road. But not now. Nothing comes here but motor-cars full of fat women, who stop for lunch, and a fisherman or two in the spring, and the shooting tenants in August. There is not much material to be got out of that. I want to see life, to travel the world, and write things like Kipling and Conrad. But the most I\'ve done yet is to get some verses printed in Chambers\'s Journal."'
        expected = [
            '"Not now," he said eagerly.',
            '"Maybe in the old days when you had pilgrims and ballad-makers and highwaymen and mail-coaches on the road. But not now. Nothing comes here but motor-cars full of fat women, who stop for lunch, and a fisherman or two in the spring, and the shooting tenants in August. There is not much material to be got out of that. I want to see life, to travel the world, and write things like Kipling and Conrad. But the most I\'ve done yet is to get some verses printed in Chambers\'s Journal."'
        ]
        assert segment_text(text, flatten=True) == expected

    def test_kipling_romance(self):
        text = '"That\'s what Kipling says," he said, his eyes brightening, and he quoted some verse about "Romance brings up the 9.15."'
        expected = ['"That\'s what Kipling says," he said, his eyes brightening, and he quoted some verse about "Romance brings up the 9.15."']
        assert segment_text(text, flatten=True) == expected

    def test_julia_cypher(self):
        text = 'It worked. The five letters of "Julia" gave me the position of the vowels. A was J, the tenth letter of the alphabet, and so represented by X in the cypher. E was U=XXI, and so on. "Czechenyi\' gave me the numerals for the principal consonants. I scribbled that scheme on a bit of paper and sat down to read Scudder\'s pages.'
        expected = [
            'It worked.',
            'The five letters of "Julia" gave me the position of the vowels.',
            'A was J, the tenth letter of the alphabet, and so represented by X in the cypher.',
            'E was U=XXI, and so on.',
            '"Czechenyi\' gave me the numerals for the principal consonants. I scribbled that scheme on a bit of paper and sat down to read Scudder\'s pages.'
        ]
        assert segment_text(text, flatten=True) == expected

    def test_black_stone_letter(self):
        text = 'I took a bit of paper and wrote these words in German as if they were part of a letter— ... "Black Stone. Scudder had got on to this, but he could not act for a fortnight. I doubt if I can do any good now, especially as Karolides is uncertain about his plans. But if Mr T. advises I will do the best I...." I manufactured it rather neatly, so that it looked like a loose page of a private letter.'
        expected = ['I took a bit of paper and wrote these words in German as if they were part of a letter— ... "Black Stone. Scudder had got on to this, but he could not act for a fortnight. I doubt if I can do any good now, especially as Karolides is uncertain about his plans. But if Mr T. advises I will do the best I...." I manufactured it rather neatly, so that it looked like a loose page of a private letter.']
        assert segment_text(text, flatten=True) == expected

    def test_innkeeper_excitement(self):
        text = 'The innkeeper appeared in great excitement. "Your paper woke them up," he said gleefully. "The dark fellow went as white as death and cursed like blazes, and the fat one whistled and looked ugly. They paid for their drinks with half-a-sovereign and wouldn\'t wait for change." "Now I\'ll tell you what I want you to do," I said. "Get on your bicycle and go off to Newton-Stewart to the Chief Constable. Describe the two men, and say you suspect them of having had something to do with the London murder. You can invent reasons. The two will come back, never fear. Not tonight, for they\'ll follow me forty miles along the road, but first thing tomorrow morning. Tell the police to be here bright and early."'
        expected = [
            'The innkeeper appeared in great excitement.',
            '"Your paper woke them up," he said gleefully.',
            '"The dark fellow went as white as death and cursed like blazes, and the fat one whistled and looked ugly. They paid for their drinks with half-a-sovereign and wouldn\'t wait for change."',
            '"Now I\'ll tell you what I want you to do," I said.',
            '"Get on your bicycle and go off to Newton-Stewart to the Chief Constable. Describe the two men, and say you suspect them of having had something to do with the London murder. You can invent reasons. The two will come back, never fear. Not tonight, for they\'ll follow me forty miles along the road, but first thing tomorrow morning. Tell the police to be here bright and early."'
        ]
        assert segment_text(text, flatten=True) == expected

    def test_peter_pienaar_atmosphere(self):
        text = 'But suddenly I remembered a thing I once heard in Rhodesia from old Peter Pienaar. I have quoted Peter already in this narrative. He was the best scout I ever knew, and before he had turned respectable he had been pretty often on the windy side of the law, when he had been wanted badly by the authorities. Peter once discussed with me the question of disguises, and he had a theory which struck me at the time. He said, barring absolute certainties like fingerprints, mere physical traits were very little use for identification if the fugitive really knew his business. He laughed at things like dyed hair and false beards and such childish follies. The only thing that mattered was what Peter called "atmosphere".'
        expected = [
            'But suddenly I remembered a thing I once heard in Rhodesia from old Peter Pienaar.',
            'I have quoted Peter already in this narrative.',
            'He was the best scout I ever knew, and before he had turned respectable he had been pretty often on the windy side of the law, when he had been wanted badly by the authorities.',
            'Peter once discussed with me the question of disguises, and he had a theory which struck me at the time.',
            'He said, barring absolute certainties like fingerprints, mere physical traits were very little use for identification if the fugitive really knew his business.',
            'He laughed at things like dyed hair and false beards and such childish follies.',
            'The only thing that mattered was what Peter called "atmosphere".'
        ]
        assert segment_text(text, flatten=True) == expected
