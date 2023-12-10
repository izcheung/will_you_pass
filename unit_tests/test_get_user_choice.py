import io
from unittest import TestCase
from game import get_user_choice
from unittest.mock import patch


class TestGetUserChoice(TestCase):
    @patch('builtins.input', side_effect=["1"])
    def test_get_user_choice_north(self, _):
        expected = "1"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["2"])
    def test_get_user_choice_south(self, _):
        expected = "2"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["3"])
    def test_get_user_choice_east(self, _):
        expected = "3"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["4"])
    def test_get_user_choice_west(self, _):
        expected = "4"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    # Invalid direction - cannot test invalid direction by itself due to infinite loop
    @patch('builtins.input', side_effect=["5", "1"])
    def test_get_user_choice_invalid_direction_and_then_valid_direction(self, _):
        expected = "1"
        actual = get_user_choice()
        self.assertEqual(expected, actual)

    @patch('builtins.input', side_effect=["a", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_direction_out_of_range_printed(self, mock_output, _):
        expected = "Direction must be an integer.\n"
        get_user_choice()
        printed_output = mock_output.getvalue()
        self.assertEqual(expected, printed_output)

    @patch('builtins.input', side_effect=["5", "1"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_get_user_choice_invalid_direction_letters_input_printed(self, mock_output, _):
        get_user_choice()
        printed = mock_output.getvalue()
        expected = "Direction must be between 1 and 4, inclusive.\n"
        self.assertEqual(expected, printed)
