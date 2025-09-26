import unittest
from unittest.mock import patch
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from rpg.npc import NPC  # noqa: E402
from rpg.player import Player  # noqa: E402
from rpg.room_inspect import InspectableRoom  # noqa: E402
from rpg.io_utils import Scanner  # noqa: E402
from rpg.combat import Combat  # noqa: E402


class TestCombat(unittest.TestCase):

    def setUp(self):
        """
        Set up a player and an enemy for testing.
        """
        self.player = Player(
            name="Hero",
            start_room=InspectableRoom("Test Room"),
            health=100,
            damage=20
            )
        self.enemy = NPC(
            description="Goblin",
            interaction="A nasty little creature.",
            health=40,
            damage=5
            )

    @patch.object(Scanner, 'read_input', side_effect=[0, 0])
    def test_combat_defeat_enemy(self, mock_input):
        """
        Test that the player defeats the enemy in combat.
        """
        combat = Combat(self.player, self.enemy)
        combat.start()

        self.assertEqual(self.enemy.health, 0)
        self.assertGreater(self.player.health, 0)

    @patch.object(Scanner, 'read_input', side_effect=[1])
    @patch.object(Combat, '_escape_attempt', return_value=True)
    def test_escape_success(self, mock_escape_attempt, mock_input):
        """
        Test that the player can successfully escape from combat.
        """
        combat = Combat(self.player, self.enemy)
        combat.start()

        self.assertGreater(self.player.health, 0)

    @patch.object(Scanner, 'read_input', side_effect=[0])
    def test_combat_player_defeat(self, mock_input):
        """
        Test that the player is defeated by the enemy.
        """
        self.enemy.damage = 100
        combat = Combat(self.player, self.enemy)
        with self.assertRaises(SystemExit):
            combat.start()


if __name__ == '__main__':
    unittest.main()
