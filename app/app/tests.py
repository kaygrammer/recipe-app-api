from django.test import TestCase
from .calc import add, subtract

class CalcTests(TestCase):

    def test_add_numbers(self):
        """ Test that add two numbers together"""
        self.assertEqual(add(3, 8), 11)

    def test_subtract_number(self):
        """Test that vakues are subtracted and returned"""
        self.assertEqual(subtract(5, 11), 6)