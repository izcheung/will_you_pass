from unittest import TestCase
from game import pick_up_chocolate
import io
from unittest.mock import patch

class TestPickUpChocolate(TestCase):
    def test_pick_up_chocolate_successfully(self):
        player = player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [0, 6], 'location': 'tech_hub',
                  'chocolate': 5}
        chocolate_coordinates = [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)]
        actual = pick_up_chocolate(player, chocolate_coordinates)
        expected = [(0, 0), (4, 6), (4, 2), (2, 6)]
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pick_up_chocolate_successfully_printed(self, mock_output):
        player = player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [0, 6], 'location': 'tech_hub',
                  'chocolate': 5}
        chocolate_coordinates = [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)]
        pick_up_chocolate(player, chocolate_coordinates)
        expected = f"\nYou picked up a Reese's chocolate! You now have 6.\n\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_pick_up_chocolate_nothing_picked_up(self):
        player = player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 2], 'location': 'tech_hub',
                  'chocolate': 5}
        chocolate_coordinates = [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)]
        actual = pick_up_chocolate(player, chocolate_coordinates)
        expected = None
        self.assertEqual(expected, actual)
