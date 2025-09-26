import unittest
import os
import sys
from unittest.mock import patch

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)

from rpg.player import Player  # noqa: E402
from rpg.npc import NPC  # noqa: E402


class TestNPC(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test.
        It sets up a Player and NPC for testing.
        """
        self.player = Player("david", 1, 10, 20)
        self.npc = NPC(
            "a mysterious man",
            "I have secrets.",
            10,
            2
        )

    def test_initialization(self):
        """
        Test that the NPC initializes with correct attributes.
        """
        self.assertEqual(self.npc.description, "a mysterious man")
        self.assertEqual(self.npc.interaction, "I have secrets.")
        self.assertEqual(self.npc.health, 10)
        self.assertEqual(self.npc.damage, 2)

    def test_inspect(self):
        """
        Test that the inspect method prints the NPC's description.
        """
        with patch('builtins.print') as mocked_print:
            self.npc.inspect()
            mocked_print.assert_called_once_with("a mysterious man")


if __name__ == '__main__':
    unittest.main()
