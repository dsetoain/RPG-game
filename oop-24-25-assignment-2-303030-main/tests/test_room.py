import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from rpg.door import Door  # noqa: E402
from rpg.npc import NPC  # noqa: E402
from rpg.room import Room  # noqa: E402


class TestRoom(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test.
        It sets up a Room instance for testing.
        """
        self.room = Room()
        self.door = Door(
            default_description="A sturdy wooden door.",
            next_room=self.room
            )
        self.npc = NPC(
            description="A friendly NPC.",
            interaction="Hello!",
            health=100,
            damage="10"
            )

    def test_add_door(self):
        """
        Test if a door can be added to the room and is accessible.
        """
        self.room.add_door(self.door)
        self.assertIn(self.door, self.room.door_list)

    def test_add_npc(self):
        """
        Test if an NPC can be added to the room and is accessible.
        """
        self.room.add_npc(self.npc)
        self.assertIn(self.npc, self.room.npc_list)

    def test_add_door_invalid_type(self):
        """
        Test if adding a non-Door object raises a TypeError.
        """
        with self.assertRaises(TypeError):
            self.room.add_door("Not a door")

    def test_add_npc_invalid_type(self):
        """
        Test if adding a non-NPC object raises a TypeError.
        """
        with self.assertRaises(TypeError):
            self.room.add_npc("Not an NPC")

    def test_remove_used_npcs(self):
        """
        Test that NPCs with health <= 0 are removed from the room.
        """
        healthy_npc = NPC(
            description="Healthy NPC.",
            interaction="Hi!",
            health=50,
            damage="5"
            )
        dying_npc = NPC(
            description="Dying NPC.",
            interaction="Help!",
            health=0,
            damage="3")
        self.room.add_npc(healthy_npc)
        self.room.add_npc(dying_npc)

        self.assertIn(dying_npc, self.room.npc_list)
        self.room.remove_used_npcs()

        self.assertNotIn(dying_npc, self.room.npc_list)
        self.assertIn(healthy_npc, self.room.npc_list)


if __name__ == '__main__':
    unittest.main()
