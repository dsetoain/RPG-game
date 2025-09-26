import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)

from rpg.player import Player  # noqa: E402
from rpg.enemy import Enemy  # noqa: E402


class TestEnemy(unittest.TestCase):
    def setUp(self):
        """
        Create an Enemy and Player for testing.
        """
        self.player = Player("david", 1, 100, 1000)
        self.enemy = Enemy(
            "a weird dude", "hey you, get back here idiot", 2, 5000
            )

    def test_initialization(self):
        """
        Test that the Enemy initializes with proper attributes.
        """
        self.assertEqual(self.enemy.description, "a weird dude")
        self.assertEqual(
            self.enemy.interaction, "hey you, get back here idiot"
            )
        self.assertEqual(self.enemy.health, 2)
        self.assertEqual(self.enemy.damage, 5000)


if __name__ == "__main__":
    unittest.main()
