from unittest import TestCase
from game import is_alive
import io
from unittest.mock import patch


class TestIsAlive(TestCase):
    def test_is_alive_full_health(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        actual = is_alive(player)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_some_health(self):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 2, 'position': [3, 1],
                     'location': 'tech_hub',
                     'chocolate': 0}
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_one_health(self):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 1, 'position': [3, 1],
                     'location': 'tech_hub',
                     'chocolate': 0}
        actual = is_alive(character)
        expected = True
        self.assertEqual(expected, actual)

    def test_is_alive_zero_health(self):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 0, 'position': [3, 1],
                     'location': 'tech_hub',
                     'chocolate': 0}
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_alive_zero_health_printed(self, mock_output):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 0, 'position': [3, 1],
                     'location': 'tech_hub',
                     'chocolate': 0}
        is_alive(character)
        expected = "You wake up from a nightmare\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_is_alive_negative_health(self):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': -5, 'position': [3, 1],
                     'location': 'tech_hub',
                     'chocolate': 0}
        actual = is_alive(character)
        expected = False
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_is_alive_negative_health_printed(self, mock_output):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': -5, 'position': [3, 1],
                     'location': 'tech_hub',
                     'chocolate': 0}
        is_alive(character)
        expected = "You wake up from a nightmare\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
