import unittest


class Dog:
    def __init__(self, color, breed):
        self.color = color
        self.breed = breed

        if breed == "lab":
            self.size = "medium"
        else:
            self.size = "small"

    def bark(self):
        if self.size == "small":
            return "bark"
        else:
            return "BARK"

    def get_breed(self):
        return self.breed

    def get_color(self):
        return self.color


class TestStringMethods(unittest.TestCase):

    def test_setup(self):
        henry = Dog("brown", "lab")
        self.assertEqual(henry.get_breed(), 'lab')
        self.assertEqual(henry.get_color(), 'brown')

    def test_bark(self):
        henry = Dog("brown", "lab")
        self.assertEqual(henry.bark(), 'BARK')