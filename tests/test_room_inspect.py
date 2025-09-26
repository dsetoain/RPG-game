import unittest
from unittest.mock import patch
import os
import sys
from io import StringIO

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from rpg.door import Door  # noqa: E402
from rpg.npc import NPC  # noqa: E402
from rpg.room_inspect import InspectableRoom  # noqa: E402


class TestInspectableRoom(unittest.TestCase):
    def setUp(self):
        """
        This method is called before each test.
        It sets up an InspectableRoom instance for testing.
        """
        self.room = InspectableRoom(default_description="a cozy room.")
        self.door = Door(
            default_description="sturdy wooden door",
            next_room=self.room
            )
        self.npc = NPC(
            description="friendly NPC",
            interaction="Hello!",
            health=100,
            damage="10"
            )

    def test_initialization(self):
        """
        Test if the InspectableRoom initializes correctly with a description.
        """
        self.assertEqual(self.room.description, "a cozy room.")
        self.assertEqual(len(self.room.door_list), 0)
        self.assertEqual(len(self.room.npc_list), 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_inspect_empty_room(self, mock_stdout):
        """
        Test the inspect method for an empty room.
        """
        self.room.inspect()
        expected_output = (
            "\nYou are in a cozy room."
            "\nThe room has 0 doors."
            "\nThere are no npcs in this room.\n"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_inspect_room_with_doors_and_npcs(self, mock_stdout):
        """
        Test the inspect method when the room has doors and NPCs.
        """
        self.room.add_door(self.door)
        self.room.add_npc(self.npc)

        self.room.inspect()
        expected_output = (
            "\nYou are in a cozy room.\n"
            "The room has only 1 door.\n"
            "The room has only 1 npc"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_inspect_doors(self, mock_stdout):
        """
        Test the inspect_doors method when there are doors in the room.
        """
        self.room.add_door(self.door)
        self.room.inspect_doors()
        expected_output = (
            "\nYou look around for doors. You see:\n"
            "(0) A sturdy wooden door\n"
            "\nChoose which door to interact with. (-1 : do nothing)"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_inspect_npcs(self, mock_stdout):
        """
        Test the inspect_npcs method when there are NPCs in the room.
        """
        self.room.add_npc(self.npc)
        self.room.inspect_npcs()
        expected_output = (
            "\nYou look around for living beings. You see:\n"
            "(0) A friendly NPC\n"
            "\nChoose which living being to interact with. (-1 : do nothing)"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_inspect_empty_doors(self, mock_stdout):
        """
        Test inspect_doors when there are no doors in the room.
        """
        self.room.inspect_doors()
        expected_output = (
            "\nThere are no doors in this room"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_inspect_empty_npcs(self, mock_stdout):
        """
        Test inspect_npcs when there are no NPCs in the room.
        """
        self.room.inspect_npcs()
        expected_output = (
            "\nThere are no living beings in this room"
        )
        self.assertIn(expected_output, mock_stdout.getvalue())


if __name__ == '__main__':
    unittest.main()
