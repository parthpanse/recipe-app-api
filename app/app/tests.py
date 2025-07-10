"""
Sample tests for the Django application.
"""

from django.test import TestCase
from app import calc


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test adding two numbers together."""
        res = calc.add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_numbers(self):
        """Test subtracting two numbers."""
        res = calc.subtract(10, 5)
        self.assertEqual(res, 5)