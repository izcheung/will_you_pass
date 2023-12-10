from unittest import TestCase
from game import surprise_pop_quiz
from unittest.mock import patch
import io


class TestSurprisePopQuiz(TestCase):
    @patch('builtins.input', return_value='2')
    @patch('random.randint', return_value='2')
    @patch('random.choice', return_value='Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: '
                                         'White/gold:\n3: Neither\n4: Both')
    def test_surprise_pop_quiz_correct_guess_intelligence(self, _, __, ___):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        surprise_questions = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: '
            'Because it is easier to take out a slice when the box is square.\n3: Because nothing makes sense'
            ' in the world.\n4: Because why not?': 3,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite '
            'opposite\n4: Opposite squared': 2}
        expected = {'name': 'Irene', 'level': 1, 'intelligence': 25, 'HP': 10, 'position': [3, 1],
                    'location': 'tech_hub', 'chocolate': 0}
        surprise_pop_quiz(player, surprise_questions)
        actual = player
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='2')
    @patch('random.randint', return_value='1')
    @patch('random.choice',
           return_value='Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: '
                        'Neither\n4: Both')
    def test_surprise_pop_quiz_wrong_guess_HP_question_1(self, _, __, ___):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        surprise_questions = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: '
            'Because it is easier to take out a slice when the box is square.\n3: Because nothing makes sense'
            ' in the world.\n4: Because why not?': 3,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite '
            'opposite\n4: Opposite squared': 2}
        expected = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 8, 'position': [3, 1],
                    'location': 'tech_hub', 'chocolate': 0}
        surprise_pop_quiz(player, surprise_questions)
        actual = player
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='4')
    @patch('random.randint', return_value='3')
    @patch('random.choice',
           return_value='Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be '
                        'classified as anything other than hot dogs.\n4: Maybe, it depends on my mood')
    def test_surprise_pop_quiz_wrong_guess_question_2(self, _, __, ___):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        surprise_questions = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: Because it'
            ' is easier to take out a slice when the box is square.\n3: Because nothing makes sense in the world.\n4: '
            'Because why not?': 3,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite opposite\n4:'
            ' Opposite squared': 2}
        expected = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 6, 'position': [3, 1], 'location': 'tech_hub',
                    'chocolate': 0}
        surprise_pop_quiz(player, surprise_questions)
        actual = player
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='3')
    @patch('random.randint', return_value='2')
    @patch('random.choice',
           return_value='Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: '
                        'Because it is easier to take out a slice when the box is square.\n3: Because nothing makes '
                        'sense in the world.\n4: Because why not?')
    def test_surprise_pop_quiz_wrong_guess_question_3(self, _, __, ___):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        surprise_questions = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: Because it'
            ' is easier to take out a slice when the box is square.\n3: Because nothing makes sense in the world.\n4:'
            ' Because why not?': 3,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite '
            'opposite\n4: Opposite squared': 2}
        expected = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 7, 'position': [3, 1],
                    'location': 'tech_hub',
                    'chocolate': 0}
        surprise_pop_quiz(player, surprise_questions)
        actual = player
        self.assertEqual(expected, actual)

    @patch('builtins.input', return_value='4')
    @patch('random.randint', return_value='3')
    @patch('random.choice',
           return_value='Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3:'
                        ' Opposite opposite\n4: Opposite squared')
    def test_surprise_pop_quiz_wrong_guess_question_4(self, _, __, ___):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        surprise_questions = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: Because it'
            ' is easier to take out a slice when the box is square.\n3: Because nothing makes sense in the world.\n4:'
            ' Because why not?': 3,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite '
            'opposite\n4: Opposite squared': 2}
        expected = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 8, 'position': [3, 1], 'location': 'tech_hub',
                    'chocolate': 0}
        surprise_pop_quiz(player, surprise_questions)
        actual = player
        self.assertEqual(expected, actual)

    @patch('random.choice',
           return_value='Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: '
                        'Opposite opposite\n4: Opposite squared')
    @patch('builtins.input', return_value="1")
    @patch('random.randint', return_value="1")
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_surprise_pop_quiz_correct_guess_print(self, mock_output, _, __, ___):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        surprise_questions = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: Because it'
            ' is easier to take out a slice when the box is square.\n3: Because nothing makes sense in the world.\n4:'
            ' Because why not?': 3,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite '
            'opposite\n4: Opposite squared': 2}
        expected_substring = "That is correct! Your intelligence is now 25 points!\n"
        surprise_pop_quiz(player, surprise_questions)
        actual = mock_output.getvalue()
        self.assertIn(expected_substring, actual)

    @patch('random.choice',
           return_value='Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: '
                        'Opposite opposite\n4: Opposite squared')
    @patch('builtins.input', return_value='1')
    @patch('random.randint', return_value='2')
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_surprise_pop_quiz_wrong_guess_print(self, mock_output, _, __, ___):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        surprise_questions = {
            'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: Both': 2,
            'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be classified as '
            'anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
            'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: Because it'
            ' is easier to take out a slice when the box is square.\n3: Because nothing makes sense in the world.\n4:'
            ' Because why not?': 3,
            'Is the opposite of opposite the same or opposite\nChoices:\n1: Same\n2: Opposite\n3: Opposite '
            'opposite\n4: Opposite squared': 2}
        expected_substring = "Your HP takes a hit!"
        surprise_pop_quiz(player, surprise_questions)
        actual = mock_output.getvalue()
        self.assertIn(expected_substring, actual)
