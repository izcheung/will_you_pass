from unittest import TestCase
from game import give_location_description


class Test(TestCase):
    def test_give_location_description_tech_hub(self):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                     'location': 'tech_hub', 'chocolate': 0}
        expected = {
            'rows': 8,
            'columns': 7,
            'obstacles': [(1, 1), (2, 1), (1, 2), (2, 2), (6, 2), (5, 3), (6, 3), (1, 4), (6, 4), (1, 5),
                          (1, 6), (1, 7), (2, 7), (3, 7), (4, 7)],
            'Chris': None
        }
        actual = give_location_description(character)
        self.assertEqual(expected, actual)

    def test_give_location_description_student_lounge(self):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                     'location': 'student_lounge', 'chocolate': 0}
        expected = {
            'rows': 10,
            'columns': 7,
            'obstacles': [(1, 1), (2, 1), (5, 1), (6, 1), (1, 2), (2, 2), (5, 2), (6, 2), (5, 3), (6, 3),
                          (5, 4), (6, 4), (1, 5), (2, 5), (1, 6), (2, 6), (1, 7), (2, 7), (5, 7), (6, 7),
                          (1, 8), (2, 8), (5, 8), (6, 8), (1, 9), (2, 9), (5, 9), (6, 9)],
            'Chris': None
        }
        actual = give_location_description(character)
        self.assertEqual(expected, actual)

    def test_give_location_description_room_645(self):
        character = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1],
                     'location': 'room_645', 'chocolate': 0}
        expected = {
            'rows': 4,
            'columns': 12,
            'obstacles': [(1, 1), (2, 1), (3, 1), (7, 1), (8, 1), (10, 2), (1, 3), (10, 3)],
            'Chris': (6, 1)
        }
        actual = give_location_description(character)
        self.assertEqual(expected, actual)
