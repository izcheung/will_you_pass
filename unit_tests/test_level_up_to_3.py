from unittest import TestCase
from game import level_up_to_3
import io
from unittest.mock import patch


class TestLevelUpTo3(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_level_up_to_3_printed(self, mock_output):
        player = {'name': 'Irene', 'level': 2, 'intelligence': 100, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 10}
        surprise_questions = {"Is the dress blue/black or white/gold?": 4, "Are hot dogs sandwiches?": 8,
                              "Why are pizza boxes square but pizzas are circular?": 6,
                              "Is the opposite of opposite the same or opposite": 4}
        level_up_to_3(player, surprise_questions)
        printed_output = mock_output.getvalue()
        expected = ("YOU LEVELED UP TO LEVEL 3! (Stats - HP: 20 (+10), Intelligence: 300 (+200)) You have now advanced "
                    "to the Room 645. CAUTION: Some of the quizzes here can kill you in one shot. Your task now is to"
                    " find Chris and give him the chocolates.\n")
        self.assertEqual(expected, printed_output)

    def test_level_up_to_3_character_stats(self):
        player = {'name': 'Irene', 'level': 2, 'intelligence': 100, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 10}
        surprise_questions = {"Is the dress blue/black or white/gold?": 4, "Are hot dogs sandwiches?": 8,
                              "Why are pizza boxes square but pizzas are circular?": 6,
                              "Is the opposite of opposite the same or opposite": 4}
        level_up_to_3(player, surprise_questions)
        actual = player
        expected = {'name': 'Irene', 'level': 3, 'intelligence': 300, 'HP': 20, 'position': [1, 2],
                    'location': 'room_645', 'chocolate': 10}
        self.assertEqual(expected, actual)

    def test_level_up_to_3_surprise_question_stats(self):
        player = {'name': 'Irene', 'level': 2, 'intelligence': 100, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 10}
        surprise_questions = {"Is the dress blue/black or white/gold?": 4, "Are hot dogs sandwiches?": 8,
                              "Why are pizza boxes square but pizzas are circular?": 6,
                              "Is the opposite of opposite the same or opposite": 4}
        actual = level_up_to_3(player, surprise_questions)
        expected = {"Is the dress blue/black or white/gold?": 8, "Are hot dogs sandwiches?": 16,
                    "Why are pizza boxes square but pizzas are circular?": 12,
                    "Is the opposite of opposite the same or opposite": 8}
        self.assertEqual(expected, actual)
