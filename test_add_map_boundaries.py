from unittest import TestCase
from game import add_map_boundaries


class TestAddMapBoundaries(TestCase):

    def test_add_map_boundaries_large_square_map_no_obstacles(self):
        location_description = {'rows': 7, 'columns': 7, 'obstacles': [], 'Chris': None}
        add_map_boundaries(location_description)
        actual = location_description["obstacles"]
        expected = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5)]
        self.assertEqual(expected, actual)

    def test_add_map_boundaries_large_square_map_with_obstacles(self):
        location_description = {'rows': 7, 'columns': 7, 'obstacles': [(1, 5), (6, 3), (3, 4)], 'Chris': None}
        add_map_boundaries(location_description)
        actual = location_description["obstacles"]
        expected = [(1, 5), (6, 3), (3, 4), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (6, 1), (6, 2), (6, 4), (6, 5)]
        self.assertEqual(expected, actual)

    def test_add_map_boundaries_rectangle_map_without_obstacles(self):
        location_description = {'rows': 8, 'columns': 7,
                                'obstacles': [],
                                'Chris': None}
        add_map_boundaries(location_description)
        actual = location_description["obstacles"]
        expected = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6)]
        self.assertEqual(expected, actual)

    def test_add_map_boundaries_rectangle_map_with_existing_obstacles(self):
        location_description = {'rows': 8, 'columns': 7,
                                'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4),
                                              (6, 4), (1, 5), (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
                                'Chris': None}
        add_map_boundaries(location_description)
        actual = location_description["obstacles"]
        expected = [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5), (1, 6), (1, 7),
                    (2, 7), (3, 7), (4, 7), (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (0, 7), (1, 7),
                    (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (6, 1),
                    (6, 5), (6, 6)]
        self.assertEqual(expected, actual)

    def test_add_map_boundaries_smallest_square_map_no_obstacles(self):
        location_description = {'rows': 1, 'columns': 1, 'obstacles': [], 'Chris': None}
        add_map_boundaries(location_description)
        actual = location_description["obstacles"]
        expected = [(0, 0), (0, 0)]
        self.assertEqual(expected, actual)

    def test_add_map_boundaries_smallest_square_map_with_obstacles(self):
        location_description = {'rows': 1, 'columns': 1, 'obstacles': [(0, 0)], 'Chris': None}
        add_map_boundaries(location_description)
        actual = location_description["obstacles"]
        expected = [(0, 0), (0, 0), (0, 0)]
        self.assertEqual(expected, actual)


