import io
from unittest import TestCase
from unittest.mock import patch
from game import generate_chocolate
from game import add_map_boundaries
from game import print_map


class TestPrintMap(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_tech_hub(self, mock_output):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        area_description = {'rows': 8, 'columns': 7, 'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3),
                                                                   (6, 3), (1, 4), (6, 4), (1, 5), (1, 6), (1, 7),
                                                                   (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0),
                                                                   (3, 0), (4, 0), (5, 0), (6, 0), (0, 7), (1, 7),
                                                                   (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1),
                                                                   (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (6, 1),
                                                                   (6, 5), (6, 6)], 'Chris': None,
                            'chocolate_coordinates': [(4, 5), (4, 1), (4, 4), (2, 4), (2, 6)]}
        print_map(player, area_description)
        expected = ("#######\n###*! #\n###   #\n#    ##\n##! ! #\n##  ! #\n##!   #\n#######\n"
                    "You are at position [3, 1]\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_room_645(self, mock_output):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                          (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                          (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9),
                                          (6, 9), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 9),
                                          (1, 9), (2, 9), (3, 9), (4, 9), (5, 9), (6, 9), (0, 1), (0, 2), (0, 3),
                                          (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (6, 5), (6, 6)],
                            'Chris': None, 'chocolate_coordinates': [(3, 6), (3, 3), (4, 3), (3, 8), (3, 2)]}
        print_map(player, area_description)
        expected = ("#######\n\n###* ##\n###! ##\n#  !!##\n#    ##\n###   #\n###!  #\n###  ##\n###! ##\n#######\n"
                    "You are at position [3, 1]\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_room_645(self, mock_output):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'room_645', 'chocolate': 0}
        area_description = {'rows': 4, 'columns': 12, 'obstacles': [(1, 1), (2, 1), (3, 1), (7, 1), (8, 1), (10, 2), (1, 3), (10, 3), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (0, 1), (0, 2), (11, 1), (11, 2)], 'Chris': (6, 1), 'chocolate_coordinates': []}
        print_map(player, area_description)
        expected = ("############\n###*  C##  #\n#         ##\n############\n"
                    "You are at position [3, 1]\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_student_lounge(self, mock_output):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'room_645',
                  'chocolate': 0}
        area_description = {'rows': 4, 'columns': 12,
                            'obstacles': [(1, 1), (2, 1), (3, 1), (7, 1), (8, 1), (10, 2), (1, 3), (10, 3), (0, 0),
                                          (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0),
                                          (10, 0), (11, 0), (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3),
                                          (7, 3), (8, 3), (9, 3), (10, 3), (11, 3), (0, 1), (0, 2), (11, 1), (11, 2)],
                            'Chris': (6, 1), 'chocolate_coordinates': []}
        print_map(player, area_description)
        expected = ("############\n###*  C##  #\n#         ##\n############\n"
                    "You are at position [3, 1]\n\n")
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)


