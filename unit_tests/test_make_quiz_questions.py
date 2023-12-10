from unittest import TestCase
from game import make_quiz_questions


class TestMakeQuizQuestions(TestCase):
    def test_make_quiz_questions(self):
        expected = {'Are hot dogs sandwiches?\nChoices:\n1: Yes\n2: No, they are tacos.\n3: No, they cannot be '
                    'classified as anything other than hot dogs.\n4: Maybe, it depends on my mood': 4,
                    'Is the dress blue/black or white/gold?\nChoices:\n1: Blue/black\n2: White/gold:\n3: Neither\n4: '
                    'Both': 2,
                    'Is the opposite of opposite the same or opposite?\nChoices:\n1: Same\n2: Opposite\n3: Opposite '
                    'opposite\n4: Opposite '
                    'squared': 2,
                    'Why are pizza boxes square but pizzas are circular?\nChoices:\n1: Because it is cheaper\n2: '
                    'Because it is easier to take out a slice when the box is square.\n3: Because nothing makes sense '
                    'in the world.\n4: Because why not?': 3}
        actual = make_quiz_questions()
        self.assertEqual(expected, actual)
