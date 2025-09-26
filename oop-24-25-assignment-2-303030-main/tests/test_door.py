import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from rpg.door import Door  # noqa: E402
from rpg.room_inspect import InspectableRoom  # noqa: E402
from rpg.player import Player  # noqa: E402


class TestDoor(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test.
        It sets up a room and a door for testing.
        """
        self.room1 = InspectableRoom("test room 1")
        self.room2 = InspectableRoom("test room 2")
        self.door = Door(
            default_description="A sturdy wooden door.",
            next_room=self.room2
            )

    def test_initialization(self):
        """
        Test if the Door is initialized correctly.
        """
        self.assertEqual(self.door.description, "A sturdy wooden door.")
        self.assertIs(self.door._next_room, self.room2)

    def test_next_room_property(self):
        """
        Test the next_room property returns a deepcopy of the room.
        """
        next_room_copy = self.door.next_room
        self.assertIsNot(next_room_copy, self.room2)

    def test_interact_updates_player_room(self):
        """
        Test the interact method updates the player's room.
        """
        mock_player = Player("test", self.room1, 1, 1)
        self.door.interact(mock_player)
        self.assertIs(mock_player.room.description, self.room2.description)

    def test_door_added_to_room(self):
        """
        Test if a door can be added to a room and accessed from the room.
        """
        self.room1.add_door(self.door)
        self.assertIn(self.door, self.room1.door_list)
        self.assertNotIn(self.door, self.room2.door_list)


if __name__ == '__main__':
    unittest.main()
