from unittest import TestCase
from game import update_hp_based_on_intelligence_for_final_exam


class TestUpdateHPBasedOnIntelligenceForFinalExam(TestCase):

    def test_update_hp_based_on_intelligence_for_final_exam_at_0(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 0, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        update_hp_based_on_intelligence_for_final_exam(player)
        actual = player['HP']
        expected = 1
        self.assertEqual(expected, actual)

    def test_update_hp_based_on_intelligence_for_final_exam_below_500(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 50, 'HP': 10, 'position': [3, 1], 'location': 'tech_hub',
                  'chocolate': 0}
        update_hp_based_on_intelligence_for_final_exam(player)
        actual = player['HP']
        expected = 1
        self.assertEqual(expected, actual)

    def test_update_hp_based_on_intelligence_for_final_exam_at_500(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 500, 'HP': 10, 'position': [3, 1],
                  'location': 'tech_hub', 'chocolate': 0}
        update_hp_based_on_intelligence_for_final_exam(player)
        actual = player['HP']
        expected = 2
        self.assertEqual(expected, actual)

    def test_update_hp_based_on_intelligence_for_final_exam_between_500_and_1000(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 749, 'HP': 10, 'position': [3, 1],
                  'location': 'tech_hub', 'chocolate': 0}
        update_hp_based_on_intelligence_for_final_exam(player)
        actual = player['HP']
        expected = 2
        self.assertEqual(expected, actual)

    def test_update_hp_based_on_intelligence_for_final_exam_at_1000(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 1000, 'HP': 10, 'position': [3, 1],
                  'location': 'tech_hub', 'chocolate': 0}
        update_hp_based_on_intelligence_for_final_exam(player)
        actual = player['HP']
        expected = 3
        self.assertEqual(expected, actual)

    def test_update_hp_based_on_intelligence_for_final_exam_over_1000(self):
        player = {'name': 'Irene', 'level': 1, 'intelligence': 1500, 'HP': 10, 'position': [3, 1],
                  'location': 'tech_hub', 'chocolate': 0}
        update_hp_based_on_intelligence_for_final_exam(player)
        actual = player['HP']
        expected = 3
        self.assertEqual(expected, actual)
