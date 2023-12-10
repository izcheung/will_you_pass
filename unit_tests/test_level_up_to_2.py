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
        expected = (f"YOU LEVELED UP TO LEVEL 2! (Stats - HP: 20 (+10), Intelligence: 100 (+100)) You have now advanced"
                    f" to the Student Lounge. Be careful, the quizzes now deal twice the damage!\n")
        self.assertEqual(expected, printed_output)

    def test_level_up_to_2_character_stats(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 5}
        surprise_questions = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                              "Why are pizza boxes square but pizzas are circular?": 3,
                              "Is the opposite of opposite the same or opposite": 2}
        level_up_to_2(player, surprise_questions)
        actual = player
        expected = {'name': 'Irene', 'level': 2, 'intelligence': 100, 'HP': 20, 'position': [3, 1],
                    'location': 'student_lounge', 'chocolate': 5}
        self.assertEqual(expected, actual)

    def test_level_up_to_2_surprise_question_stats(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 5}
        surprise_questions = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: Because it is '
            'easier to take out a slice when the box is square.\n3: Because nothing makes sense in the world.\n4: '
            'Because why not?': 3,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite opposite\n4'
            ': Opposite squared': 2}
        actual = level_up_to_2(player, surprise_questions)
        expected = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 4,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 8,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: Because it'
            ' is easier to take out a slice when the box is square.\n3: Because nothing makes sense in the world.\n4: '
            'Because why not?': 6,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite opposite\n4:'
            ' Opposite squared': 4}
        self.assertEqual(expected, actual)
