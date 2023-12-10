
from unittest import TestCase
from game import move_character


class TestMovePlayer(TestCase):

    def test_move_character_north(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "1"
        move_character(player, direction)
        expected = [3, 0]
        actual = player["position"]
        self.assertEqual(expected, actual)

    def test_move_character_south(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "2"
        move_character(player, direction)
        expected = [3, 2]
        actual = player["position"]
        self.assertEqual(expected, actual)

    def test_move_character_east(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "3"
        move_character(player, direction)
        expected = [4, 1]
        actual = player["position"]
        self.assertEqual(expected, actual)

    def test_move_character_west(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "4"
        move_character(player, direction)
        expected = [2, 1]
        actual = player["position"]
        self.assertEqual(expected, actual)
