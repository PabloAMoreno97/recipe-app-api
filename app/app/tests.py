"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module."""

    def test_add_numbers(self):
        """Test adding numbers together."""
        result = calc.add(8, 3)
        self.assertEqual(result, 11)
        self.assertTrue(isinstance(result, int), True)

    def test_subtract_numbers(self):
        """Test subtracting numbers."""
        result = calc.subtract(10, 3)
        self.assertEqual(result, 7)
        self.assertTrue(isinstance(result, int), True)
