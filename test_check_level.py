from unittest import TestCase
from game import check_level
from unittest.mock import patch
from game import level_up_to_2


class TestCheckLevel(TestCase):

    def test_check_level_in_between_level_1(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 3}
        surprise_questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                              "Why are pizza boxes square but pizzas are circular?": 3,
                              "Is the opposite of opposite the same or opposite": 2}
        actual = check_level(player, surprise_questions)
        expected = None
        self.assertEqual(expected, actual)
    @patch('random.sample',
           side_effect=lambda population, k: [(0, 6)] if k == 1 else [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)])
    def test_check_level_up_to_2(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 5}
        surprise_questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                    "Why are pizza boxes square but pizzas are circular?": 3,
                    "Is the opposite of opposite the same or opposite": 2}
        actual = check_level(player, surprise_questions)
        expected = [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)]
        self.assertEqual(expected, actual)

    def test_check_level_in_between_level_2_and_3(self):
        player = {'name': 'Irene', 'level': 2, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge',
                  'chocolate': 7}
        surprise_questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                              "Why are pizza boxes square but pizzas are circular?": 3,
                              "Is the opposite of opposite the same or opposite": 2}
        actual = check_level(player, surprise_questions)
        expected = None
        self.assertEqual(expected, actual)

    def test_check_level_up_to_3(self):
        player = {'name': 'Irene', 'level': 2, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge',
                  'chocolate': 10}
        surprise_questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                              "Why are pizza boxes square but pizzas are circular?": 3,
                              "Is the opposite of opposite the same or opposite": 2}
        actual = check_level(player, surprise_questions)
        expected = []
        self.assertEqual(expected, actual)





