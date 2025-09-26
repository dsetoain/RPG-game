# import unittest
# import os
# import sys
# from unittest.mock import patch
# from io import StringIO

# currentdir = os.path.dirname(os.path.realpath(__file__))
# parentdir = os.path.dirname(currentdir)
# sys.path.insert(0, parentdir)

# from rpg.game import Game  # noqa: E402
# from rpg.room_inspect import InspectableRoom  # noqa: E402
# from rpg.player import Player  # noqa: E402
# from rpg.io_utils import Scanner  # noqa: E402


# class TestGame(unittest.TestCase):
#     def setUp(self):
#         """
#         This method is called before each test.
#         It sets up a game instance for testing.
#         """
#         self.game = Game()

#     @patch.object(Scanner, 'read_input',
#                   side_effect=[
#                       1, 0, '\n', 1, 0, '\n', 1, 0, '\n', 1, 0, '\n'
#                       ])
#     def test_initialization(self, mock_input):
#         """
#         Full game test.
#         """
#         self.game.run()

#     @patch.object(Scanner, 'read_input', side_effect=['david'])
#     def test_initialization(self, mock_input):
#         """
#         Test that the Game initializes correctly and prompts for player name.
#         """
#         self.assertEqual(self.game.player.name, "david")

#     @patch.object(Scanner, 'read_input', side_effect=[1, 9])
#     def test_run_look_for_a_way_out(self, mock_input):
#         """
#         Test that the player can look for a way out and then quit the game.
#         """
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             self.game.run()
#             self.assertIn(
#                     "You look for a way out...",
#                     mock_stdout.getvalue()
#                     )

#     @patch.object(Scanner, 'read_input', side_effect=[2, 9])
#     def test_run_look_for_company(self, mock_input):
#         """
#         Test that the player can look for company and then quit the game.
#         """
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             self.game.run()
#             self.assertIn("You look for company...", mock_stdout.getvalue())
#             self.assertIn("Quitting Game", mock_stdout.getvalue())

#     @patch.object(Scanner, 'read_input', side_effect=[3, 9])
#     def test_run_check_stats(self, mock_input):
#         """
#         Test that the player can check stats and then quit the game.
#         """
#         with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
#             self.game.run()
#             self.assertIn("Checking stats...", mock_stdout.getvalue())
#             self.assertIn("Quitting Game", mock_stdout.getvalue())


# if __name__ == '__main__':
#     unittest.main()
