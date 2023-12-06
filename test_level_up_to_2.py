import io
from unittest import TestCase
from game import level_up_to_2
from unittest.mock import patch


class TestLevelUpTo2(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_to_2_printed(self, mock_output):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 5}
        surprise_questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                              "Why are pizza boxes square but pizzas are circular?": 3,
                              "Is the opposite of opposite the same or opposite": 2}
        level_up_to_2(player, surprise_questions)
        printed_output = mock_output.getvalue()
        expected = "YOU LEVELED UP TO LEVEL 2!\n"
        self.assertEqual(expected, printed_output)

    def test_level_up_to_2_character_stats(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 5}
        surprise_questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                              "Why are pizza boxes square but pizzas are circular?": 3,
                              "Is the opposite of opposite the same or opposite": 2}
        level_up_to_2(player, surprise_questions)
        actual = player
        expected = {'name': 'Irene', 'level': 2, 'intelligence': 100, 'HP': 20, 'position': [3, 1], 'location': 'student_lounge',
              'chocolate': 5}
        self.assertEqual(expected, actual)

    def test_level_up_to_2_surprise_question_stats(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 5}
        surprise_questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                              "Why are pizza boxes square but pizzas are circular?": 3,
                              "Is the opposite of opposite the same or opposite": 2}
        level_up_to_2(player, surprise_questions)
        actual = surprise_questions
        expected = {"Is the dress blue/black or white/gold?": 4, "Are hot dogs sandwiches?": 8,
                              "Why are pizza boxes square but pizzas are circular?": 6,
                              "Is the opposite of opposite the same or opposite": 4}
        self.assertEqual(expected, actual)


