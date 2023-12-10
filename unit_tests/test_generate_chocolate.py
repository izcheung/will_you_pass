"""
Irene Cheung
A01349998
"""

import io
import unittest
from unittest.mock import patch
from game import generate_chocolate


class TestGenerateChocolate(unittest.TestCase):

    @patch('random.sample',
           side_effect=lambda population, k: [(0, 6)] if k == 1 else [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)])
    def test_generate_chocolate(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        area_description = {
            'rows': 8,
            'columns': 7,
            'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5),
                          (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
            'Chris': None
        }
        expected = [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)]
        generate_chocolate(player, area_description)
        actual = area_description["chocolate_coordinates"]
        self.assertEqual(expected, actual)

    @patch('random.sample', side_effect=lambda population, k: [(0, 3)] if k == 1 else [(0, 3), (0, 0), (1, 3),
                                                                                       (0, 2), (2, 0)])
    def test_generate_chocolate_student_lounge(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location':
            'student_lounge',
                  'chocolate': 0}
        area_description = {
            'rows': 10,
            'columns': 7,
            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3), (6, 3),
                          (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7),
                          (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9)],
            'Chris': None
        }
        expected = [(0, 3), (0, 0), (1, 3), (0, 2), (2, 0)]
        generate_chocolate(player, area_description)
        actual = area_description["chocolate_coordinates"]
        self.assertEqual(expected, actual)

    @patch('random.sample',
           side_effect=lambda population, k: [(0, 3)] if k == 1 else [(8, 2), (7, 0), (10, 0), (0, 2), (4, 0)])
    def test_generate_chocolate_room_645(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        area_description = {
            'rows': 8,
            'columns': 7,
            'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5),
                          (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
            'Chris': None
        }
        expected = [(8, 2), (7, 0), (10, 0), (0, 2), (4, 0)]
        generate_chocolate(player, area_description)
        actual = area_description["chocolate_coordinates"]
        self.assertEqual(expected, actual)
