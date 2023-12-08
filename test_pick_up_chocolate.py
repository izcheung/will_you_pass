from unittest import TestCase
from game import pick_up_chocolate
import io
from unittest.mock import patch

class TestPickUpChocolate(TestCase):
    def test_pick_up_chocolate_successfully(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [0, 6], 'location': 'tech_hub', 'chocolate': 0}
        area_description = {'rows': 8, 'columns': 7,
         'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5), (1, 6), (1, 7),
                       (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 7), (1, 7),
                       (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (6, 1),
                       (6, 5), (6, 6)], 'Chris': None,
         'chocolate_coordinates': [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)]}
        pick_up_chocolate(player, area_description)
        actual = area_description
        expected = {'rows': 8, 'columns': 7,
         'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5), (1, 6), (1, 7),
                       (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 7), (1, 7),
                       (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (6, 1),
                       (6, 5), (6, 6)], 'Chris': None,
         'chocolate_coordinates': [(0, 0), (4, 6), (4, 2), (2, 6)]}
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_pick_up_chocolate_successfully_printed(self, mock_output):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [0, 6], 'location': 'tech_hub',
                  'chocolate': 0}
        area_description = {'rows': 8, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4),
                                          (1, 5), (1, 6), (1, 7),
                                          (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                                          (6, 0), (0, 7), (1, 7),
                                          (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), (0, 4),
                                          (0, 5), (0, 6), (6, 1),
                                          (6, 5), (6, 6)], 'Chris': None,
                            'chocolate_coordinates': [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)]}
        pick_up_chocolate(player, area_description)
        expected = "\nYou picked up a Reese's chocolate! You now have 1.\n\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    def test_pick_up_chocolate_nothing_picked_up(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [0, 6], 'location': 'tech_hub',
                  'chocolate': 0}
        area_description = {'rows': 8, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4),
                                          (1, 5), (1, 6), (1, 7),
                                          (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
                                          (6, 0), (0, 7), (1, 7),
                                          (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), (0, 4),
                                          (0, 5), (0, 6), (6, 1),
                                          (6, 5), (6, 6)], 'Chris': None,
                            'chocolate_coordinates': [(0, 6), (0, 0), (4, 6), (4, 2), (2, 6)]}
        actual = pick_up_chocolate(player, area_description)
        expected = None
        self.assertEqual(expected, actual)
