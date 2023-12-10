from unittest import TestCase
from game import final_exam_intro
import io
from unittest.mock import patch


class TestFinalExamIntro(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_exam_intro_intelligence_at_0(self, mock_output):
        character = {'name': 'Irene', 'level': 3, 'intelligence': 0, 'HP': 10, 'position': [6, 1],
                     'location': 'room_645', 'chocolate': 0}
        expected = ("MWAHAHAHAHAHA\nWelcome to COMP1510, it is I, Chris! Will you pass this final test? Based on your "
                    "intelligence, I will grant you 1 tries.\n")
        final_exam_intro(character)
        printed_output = mock_output.getvalue()
        self.assertEqual(expected, printed_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_exam_intro_intelligence_below_500(self, mock_output):
        character = {'name': 'Irene', 'level': 3, 'intelligence': 250, 'HP': 10, 'position': [6, 1],
                     'location': 'room_645', 'chocolate': 0}
        expected = ("MWAHAHAHAHAHA\nWelcome to COMP1510, it is I, Chris! Will you pass this final test? Based on your "
                    "intelligence, I will grant you 1 tries.\n")
        final_exam_intro(character)
        printed_output = mock_output.getvalue()
        self.assertEqual(expected, printed_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_exam_intro_intelligence_at_500(self, mock_output):
        character = {'name': 'Irene', 'level': 3, 'intelligence': 500, 'HP': 10, 'position': [6, 1],
                     'location': 'room_645', 'chocolate': 0}
        expected = ("MWAHAHAHAHAHA\nWelcome to COMP1510, it is I, Chris! Will you pass this final test? Based on your "
                    "intelligence, I will grant you 2 tries.\n")
        final_exam_intro(character)
        printed_output = mock_output.getvalue()
        self.assertEqual(expected, printed_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_exam_intro_intelligence_between_500_and_1000(self, mock_output):
        character = {'name': 'Irene', 'level': 3, 'intelligence': 750, 'HP': 10, 'position': [6, 1],
                     'location': 'room_645', 'chocolate': 0}
        expected = ("MWAHAHAHAHAHA\nWelcome to COMP1510, it is I, Chris! Will you pass this final test? Based on your "
                    "intelligence, I will grant you 2 tries.\n")
        final_exam_intro(character)
        printed_output = mock_output.getvalue()
        self.assertEqual(expected, printed_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_exam_intro_intelligence_at_1000(self, mock_output):
        character = {'name': 'Irene', 'level': 3, 'intelligence': 1000, 'HP': 10, 'position': [6, 1],
                     'location': 'room_645', 'chocolate': 0}
        expected = ("MWAHAHAHAHAHA\nWelcome to COMP1510, it is I, Chris! Will you pass this final test? Based on your "
                    "intelligence, I will grant you 3 tries.\n")
        final_exam_intro(character)
        printed_output = mock_output.getvalue()
        self.assertEqual(expected, printed_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_final_exam_intro_intelligence_over_1000(self, mock_output):
        character = {'name': 'Irene', 'level': 3, 'intelligence': 1500, 'HP': 10, 'position': [6, 1],
                     'location': 'room_645', 'chocolate': 0}
        expected = ("MWAHAHAHAHAHA\nWelcome to COMP1510, it is I, Chris! Will you pass this final test? Based on your "
                    "intelligence, I will grant you 3 tries.\n")
        final_exam_intro(character)
        printed_output = mock_output.getvalue()
        self.assertEqual(expected, printed_output)
