import io
from unittest import TestCase
from game import get_user_choice
from unittest.mock import patch


class TestGetUserChoice(TestCase):
    # Four valid directions
    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_north(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
    'chocolate': 0}
        expected = "1"
        actual = get_user_choice(player)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_south(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
                  'chocolate': 0}
        expected = "2"
        actual = get_user_choice(player)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_east(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
                  'chocolate': 0}
        expected = "3"
        actual = get_user_choice(player)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_west(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
                  'chocolate': 0}
        expected = "4"
        actual = get_user_choice(player)
        self.assertEqual(expected, actual)

    # Invalid direction - cannot test invalid direction by itself due to infinite loop
    @patch('builtins.input', side_effect=["0", "1"])
    def test_get_user_choice_invalid_direction_and_then_valid_return(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
                  'chocolate': 0}
        expected = "1"
        actual = get_user_choice(player)
        self.assertEqual(expected, actual)


    @patch('builtins.input', side_effect=["0", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_direction_and_then_valid_print(self, mock_output, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
                  'chocolate': 0}
        get_user_choice(player)
        printed = mock_output.getvalue()
        expected = "Invalid direction. \n"
        self.assertEqual(expected, printed)

    @patch('builtins.input', side_effect=["a", "1"])
    def test_get_user_choice_invalid_direction_and_then_valid_letter_return(self, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
                  'chocolate': 0}
        expected = "1"
        actual = get_user_choice(player)
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["a", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_direction_and_then_valid_letter_print(self, mock_output, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub', \
                  'chocolate': 0}
        get_user_choice(player)
        printed = mock_output.getvalue()
        expected = "Invalid direction. \n"
        self.assertEqual(expected, printed)

