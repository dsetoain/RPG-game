import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)

from rpg.player import Player  # noqa: E402
from rpg.healer import Healer  # noqa: E402


class TestHealer(unittest.TestCase):
    def setUp(self):
        """
        Create a Player and a Healer for testing.
        """
        self.player = Player("david", 1, 100, 100)
        self.healer = Healer(
            "a kind woman",
            "I can heal you.",
            3000,
            4,
            55
        )

    def test_initialization(self):
        """
        Test that the Healer initializes with correct attributes.
        """
        self.assertEqual(self.healer.description, "a kind woman")
        self.assertEqual(self.healer.interaction, "I can heal you.")
        self.assertEqual(self.healer.health, 3000)
        self.assertEqual(self.healer.damage, 4)
        self.assertEqual(self.healer.max_healing_done, 55)

    def test_heal_player(self):
        """
        Test that the player is healed correctly by the healer.
        """
        self.player.health = 5
        self.healer._dialogue(self.player)
        self.assertEqual(self.player.health, 60)

    def test_no_healing_needed(self):
        """
        Test that the player's health remains the
        same if healing is not necessary.
        """
        self.player.health = 100
        self.healer._dialogue(self.player)
        self.assertEqual(self.player.health, 100)


if __name__ == "__main__":
    unittest.main()
