"""
Sample tests for the app.
"""

from django.test import SimpleTestCase
from app import calc

class CalcTests(SimpleTestCase):
    def test_add_numbers(self):
        """Test that two numbers are added together"""
        self.assertEqual(calc.add(3, 8), 11)
    
    def test_substract_numbers(self):
        """Test that values are substracted and returned"""
        self.assertEqual(calc.substract(11, 5), 6)

   