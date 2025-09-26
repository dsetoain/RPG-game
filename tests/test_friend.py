import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)

from rpg.player import Player  # noqa: E402
from rpg.friend import Friend  # noqa: E402


class TestFriend(unittest.TestCase):
    def setUp(self):
        """
        Create a Friend and a Player for testing.
        """
        self.player = Player("david", 1,  10, 1)
        self.friend = Friend(
            "a worried old man",
            "here young adventurer!", 5, 3, "spell of strength", 2
            )

    def test_initialization(self):
        """
        Test that the Friend initializes with correct attributes.
        """
        self.assertEqual(self.friend.description, "a worried old man")
        self.assertEqual(self.friend.interaction, "here young adventurer!")
        self.assertEqual(self.friend.health, 5)
        self.assertEqual(self.friend.damage, 3)
        self.assertEqual(self.friend.weapon, "spell of strength")
        self.assertEqual(self.friend.damage_increase, 2)

    def test_dialogue_increases_player_damage(self):
        """
        Test that the player's damage increases after the friend helps.
        """
        original_damage = self.player.damage
        self.friend._dialogue(self.player)
        self.assertEqual(
            self.player.damage, original_damage + self.friend.damage_increase
            )

    def test_dialogue_kills_friend(self):
        """
        Test that the Friend dies after interaction, making it
        non-interactable.
        """
        self.friend._dialogue(self.player)
        self.assertEqual(self.friend.health, 0)


if __name__ == "__main__":
    unittest.main()
