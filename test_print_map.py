import io
from unittest import TestCase
from unittest.mock import patch
from game import generate_chocolate
from game import add_map_boundaries
from game import print_map


class TestPrintMap(TestCase):

    @patch('random.sample',
           side_effect=lambda population, k: [(1, 3)] if k == 1 else [(1, 3), (2, 5), (3, 3), (4, 2), (2, 3)])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_tech_hub(self, mock_output, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        area_description = {
            'rows': 8,
            'columns': 7,
            'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5),
                          (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
            'Chris': None
        }
        add_map_boundaries(area_description)
        chocolate_coordinates = [(1, 3), (2, 5), (3, 3), (4, 2), (2, 3)]
        print_map(player, area_description, chocolate_coordinates)
        expected = "#######\n###*  #\n### ! #\n#!!! ##\n##    #\n##!   #\n##    #\n#######\nYou are at position [3, 1]\n\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.sample',
           side_effect=lambda population, k: [(1, 2)] if k == 1 else [(1, 2), (2, 6), (3, 3), (4, 2), (2, 3)])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_student_lounge(self, mock_output, _):
        player = {'name': 'Irene', 'level': 3, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'room_645',
                  'chocolate': 10}
        area_description = {
            'rows': 4,
            'columns': 12,
            'obstacles': [(1, 1), (2, 1), (3, 1), (7, 1), (8, 1), (10, 2), (1, 3), (10, 3)],
            'Chris': (6, 1)
        }
        add_map_boundaries(area_description)
        chocolate_coordinates = [(1, 2), (2, 6), (3, 3), (4, 2), (2, 3)]
        print_map(player, area_description, chocolate_coordinates)
        expected = "############\n###*  C##  #\n#!  !     ##\n############\nYou are at position [3, 1]\n\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)

    @patch('random.sample',
           side_effect=lambda population, k: [(1, 3)] if k == 1 else [(1, 3), (2, 6), (3, 3), (4, 2), (2, 3)])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_map_student_lounge(self, mock_output, _):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge',
                  'chocolate': 5}
        area_description = {
            'rows': 10,
            'columns': 7,
            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3), (6, 3),
                          (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7),
                          (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9)],
            'Chris': None
        }
        add_map_boundaries(area_description)
        chocolate_coordinates = [(1, 3), (2, 6), (3, 3), (4, 2), (2, 3)]
        print_map(player, area_description, chocolate_coordinates)
        expected = "#######\n###* ##\n### !##\n#!!! ##\n#    ##\n###   #\n###   #\n###  ##\n###  ##\n#######\nYou are at position [3, 1]\n\n"
        actual = mock_output.getvalue()
        self.assertEqual(expected, actual)
