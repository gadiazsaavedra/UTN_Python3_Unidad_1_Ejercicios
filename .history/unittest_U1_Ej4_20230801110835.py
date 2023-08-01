import unittest
import math
import io
import sys
from unittest.mock import patch
from unidad1_ejercicio4 import calculate_area_of_circle


class TestCalculateAreaOfCircle(unittest.TestCase):
    def test_calculate_area_of_circle(self):
        self.assertAlmostEqual(calculate_area_of_circle(1), math.pi)
        self.assertAlmostEqual(calculate_area_of_circle(2), 4 * math.pi)
        self.assertAlmostEqual(calculate_area_of_circle(0), 0)
        self.assertAlmostEqual(calculate_area_of_circle(0.5), math.pi / 4)
        self.assertAlmostEqual(calculate_area_of_circle(10), 100 * math.pi)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_output(self, mock_stdout):
        calculate_area_of_circle(1)
        self.assertEqual(mock_stdout.getvalue(), "The area is 3.14\n")

    def test_input_validation(self):
        with patch("builtins.input", side_effect=["a", "-1", "0", "1"]):
            self.assertAlmostEqual(calculate_area_of_circle(), math.pi)


if __name__ == "__main__":
    unittest.main()
