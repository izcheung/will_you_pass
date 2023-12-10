from unittest import TestCase
from game import validate_move


class TestValidateMove(TestCase):
    def test_validate_move_north_within_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7, 'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2),
                                                                    (5, 2), (6, 2), (5, 3), (6, 3), (5, 4), (6, 4),
                                                                    (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                                                    (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8),
                                                                    (1, 9), (2, 9), (5, 9), (6, 9)], 'Chris': None,
                            'chocolate_coordinates': [(3, 3), (2, 3), (1, 3),
                                                      (3, 5), (2, 5)]}
        direction = "1"
        expected = True
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_south_within_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                          (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                          (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9),
                                          (6, 9)], 'Chris': None,
                            'chocolate_coordinates': [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)]}
        direction = "2"
        expected = True
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_east_within_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                          (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                          (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9),
                                          (6, 9)], 'Chris': None,
                            'chocolate_coordinates': [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)]}
        direction = "3"
        expected = True
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_west_within_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 5],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                          (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                          (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9),
                                          (6, 9)], 'Chris': None,
                            'chocolate_coordinates': [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)]}
        direction = "4"
        expected = True
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_north_outside_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 2],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                          (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                          (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9),
                                          (6, 9)], 'Chris': None,
                            'chocolate_coordinates': [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)]}
        direction = "1"
        expected = False
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_south_outside_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 0],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                          (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                          (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9),
                                          (6, 9)], 'Chris': None,
                            'chocolate_coordinates': [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)]}
        direction = "2"
        expected = False
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_east_outside_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 1],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                          (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                          (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9),
                                          (6, 9)], 'Chris': None,
                            'chocolate_coordinates': [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)]}
        direction = "3"
        expected = False
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_west_outside_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 0}
        area_description = {'rows': 10, 'columns': 7,
                            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3),
                                          (6, 3), (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7),
                                          (5, 7), (6, 7), (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9),
                                          (6, 9)], 'Chris': None,
                            'chocolate_coordinates': [(3, 3), (2, 3), (1, 3), (3, 5), (2, 5)]}
        direction = "4"
        expected = False
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)
