from unittest import TestCase
from game import validate_move
from game import give_location_description
from game import add_map_boundaries


class TestValidateMove(TestCase):
    def test_validate_move_north_within_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 4], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "1"
        expected = True
        area_description = give_location_description(player)
        add_map_boundaries(area_description)
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_south_within_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 4], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "2"
        expected = True
        area_description = give_location_description(player)
        add_map_boundaries(area_description)
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_east_within_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 4], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "3"
        expected = True
        area_description = give_location_description(player)
        add_map_boundaries(area_description)
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_west_within_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 4], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "4"
        expected = True
        area_description = give_location_description(player)
        add_map_boundaries(area_description)
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    # Outside bounds
    def test_validate_move_north_outside_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "1"
        expected = False
        area_description = give_location_description(player)
        add_map_boundaries(area_description)
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_south_outside_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [6, 6], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "2"
        expected = False
        area_description = give_location_description(player)
        add_map_boundaries(area_description)
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_east_outside_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [5, 7], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "3"
        expected = False
        area_description = give_location_description(player)
        add_map_boundaries(area_description)
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)

    def test_validate_move_west_outside_bounds(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [1, 7], 'location': 'tech_hub',
                  'chocolate': 0}
        direction = "4"
        expected = False
        area_description = give_location_description(player)
        add_map_boundaries(area_description)
        actual = validate_move(player, area_description, direction)
        self.assertEqual(expected, actual)
