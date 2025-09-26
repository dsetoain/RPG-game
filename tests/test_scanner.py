import unittest
import os
import sys
from unittest.mock import patch
from io import StringIO

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from rpg.io_utils import Scanner  # noqa: E402


class TestScanner(unittest.TestCase):
    def test_read_input_valid(self):
        """
        Test that read_input returns the correct value when
        a valid input is given.
        """
        with patch('builtins.input', side_effect=['3']):
            result = Scanner.read_input()
            self.assertEqual(result, 3)

    @patch('builtins.input', side_effect=['invalid', '5'])
    def test_read_input_invalid(self, mock_input):
        """
        Test that read_input handles invalid input and
        retries until valid input is provided.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = Scanner.read_input()
            self.assertEqual(result, 5)
            self.assertIn(
                "Invalid input, please provide a positive integer.",
                mock_stdout.getvalue()
                )


if __name__ == '__main__':
    unittest.main()
