from unittest import TestCase
from unittest.mock import patch
from game import quiz_probability


class TestQuizProbability(TestCase):

    @patch('random.randint', return_value=1)
    def test_quiz_probability_quiz_initiated(self, _):
        expected = True
        actual = quiz_probability()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=2)
    def test_quiz_probability_quiz_not_initiated_2(self, _):
        expected = False
        actual = quiz_probability()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=3)
    def test_quiz_probability_quiz_not_initiated_3(self, _):
        expected = False
        actual = quiz_probability()
        self.assertEqual(expected, actual)

    @patch('random.randint', return_value=4)
    def test_quiz_probability_quiz_not_initiated_4(self, _):
        expected = False
        actual = quiz_probability()
        self.assertEqual(expected, actual)


    @patch('random.randint', return_value=5)
    def test_quiz_probability_quiz_not_initiated_5(self, _):
        expected = False
        actual = quiz_probability()
        self.assertEqual(expected, actual)