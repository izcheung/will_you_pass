from unittest import TestCase
from game import make_character


class TestMakeCharacter(TestCase):
    def test_make_character_all_letters(self):
        expected = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                    'chocolate': 0}
        actual = make_character('Irene')
        self.assertEqual(expected, actual)

    def test_make_character_all_symbols(self):
        expected = {'name': '@!#$%$', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                    'chocolate': 0}
        actual = make_character('@!#$%$')
        self.assertEqual(expected, actual)

    def test_make_character_all_numbers(self):
        expected = {'name': '12345', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                    'chocolate': 0}
        actual = make_character('12345')
        self.assertEqual(expected, actual)

    def test_make_character_mix_letters_symbols_numbers(self):
        expected = {'name': '!@#Abc123', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                    'location': 'tech_hub',
                    'chocolate': 0}
        actual = make_character('!@#Abc123')
        self.assertEqual(expected, actual)
