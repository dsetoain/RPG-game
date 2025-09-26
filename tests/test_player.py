import unittest
import os
import sys
from unittest.mock import patch

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)

from rpg.player import Player  # noqa: E402
from rpg.room_inspect import InspectableRoom  # noqa: E402


class TestPlayer(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test.
        It sets up an InspectableRoom and a Player for testing.
        """
        self.room = InspectableRoom("test room")
        self.player = Player("david", self.room, 100, 100)

    def test_initialization(self):
        """
        Test that the Player initializes with correct attributes.
        """
        self.assertEqual(self.player.name, "david")
        self.assertEqual(self.player.room, self.room)
        self.assertEqual(self.player.health, 100)
        self.assertEqual(self.player.damage, 100)

    def test_room_property(self):
        """
        Test that the room property returns the current room.
        """
        self.assertEqual(self.player.room, self.room)

    def test_set_room(self):
        """
        Test that setting a new room updates the player's room.
        """
        new_room = InspectableRoom("new test room")
        with patch('builtins.print') as mocked_print:
            self.player.room = new_room
            self.assertEqual(self.player.room, new_room)
            mocked_print.assert_called_once_with("\nYou enter new test room\n")

    def test_set_room_invalid_type(self):
        """
        Test that setting a room to an invalid type raises TypeError.
        """
        with self.assertRaises(TypeError):
            self.player.room = "invalid room"

    def test_set_max_health(self):
        """
        Test that setting a new max health updates correctly.
        """
        self.player.max_health = 1250
        self.assertEqual(self.player.max_health, 1250)

    def test_set_max_health_invalid_type(self):
        """
        Test that setting max health to a non-integer raises TypeError.
        """
        with self.assertRaises(TypeError):
            self.player.max_health = "invalid health"


if __name__ == '__main__':
    unittest.main()
