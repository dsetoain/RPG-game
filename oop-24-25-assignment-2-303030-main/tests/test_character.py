import unittest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)

sys.path.insert(0, parentdir)

from rpg.character import Character  # noqa: E402


class TestCharacter(unittest.TestCase):
    def setUp(self):
        """
        Create a character instance for testing.
        """
        self.character = Character("david", 10, 5)

    def test_initialization(self):
        """
        Test character properties are correct.
        """
        self.assertEqual(self.character.name, "david")
        self.assertEqual(self.character.health, 10)
        self.assertEqual(self.character.damage, 5)

    def test_setting_health(self):
        """
        Test the setter for setting health.
        """
        self.character.health = 1000
        self.assertEqual(self.character.health, 1000)

    def test_setting_damage(self):
        """
        Test the setter for setting damage.
        """
        self.character.damage = 300
        self.assertEqual(self.character.damage, 300)

    def test_setter_health_type(self):
        """
        Test setter for health is type int.
        """
        with self.assertRaises(TypeError):
            self.character.health = "not an int"

    def test_setter_damage_type(self):
        """
        Test setter for damage is type int.
        """
        with self.assertRaises(TypeError):
            self.character.damage = "not an int"


if __name__ == "__main__":
    unittest.main()
