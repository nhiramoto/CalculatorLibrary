"""
Unit tests for calculator library.
"""

import calculator


class TestCalculator:

    def test_add(self):
        assert 8 == calculator.add(5, 3)

    def test_sub(self):
        assert 3 == calculator.sub(10, 7)
