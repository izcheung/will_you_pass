from unittest import TestCase
from game import make_quiz_questions

class TestMakeQuizQuestions(TestCase):
    def test_make_quiz_questions(self):
        expected = {"Is the dress blue/black or white/gold?": 2, "Are hot dogs sandwiches?": 4,
                    "Why are pizza boxes square but pizzas are circular?": 3,
                    "Is the opposite of opposite the same or opposite": 2}
        actual = make_quiz_questions()
        self.assertEqual(expected, actual)
