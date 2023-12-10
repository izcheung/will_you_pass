from unittest import TestCase
from game import initialize_map


class TestInitializeMap(TestCase):
    def test_initialize_map_room_645(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'room_645', 'chocolate': 0}
        areas = initialize_map(player)
        actual = areas["room_645"]["chocolate_coordinates"]
        expected = []
        self.assertEqual(actual, expected)

    def test_initialize_map_student_lounge(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'student_lounge', 'chocolate': 0}
        areas = initialize_map(player)
        actual = len(areas["student_lounge"]["chocolate_coordinates"])
        expected = 5
        self.assertEqual(actual, expected)

    def test_initialize_map_tech_hub(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                  'location': 'tech_hub', 'chocolate': 0}
        areas = initialize_map(player)
        actual = len(areas["tech_hub"]["chocolate_coordinates"])
        expected = 5
        self.assertEqual(actual, expected)
