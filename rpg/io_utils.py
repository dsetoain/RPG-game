# import os
# import json
# from rpg.player import Player


class Scanner():
    """
    A utility class in order to read user input to play the game.
    """
    @staticmethod
    def read_input() -> int:
        """
        Reads and returns an integer input the user inputted.

        returns:
        answer (int): The provided input from the user
        """
        while True:
            try:
                answer = input(" ")
                answer = int(answer)
                return answer
            except ValueError:
                print("Invalid input, please provide a positive integer.")

    @staticmethod
    def wait_for_input() -> None:
        """
        Waits for the user to press Enter before continuing with the game.
        """
        input("Press Enter to continue...")


# class Saver:
#     """
#     A class to save the game progression to a json file
#     and be able to extract it and load the game saved.
#     """
#     SAVE_DIRECTORY = "savedgames"
#     SAVE_FILE = "quicksave.json"

#     @classmethod
#     def check_directory(cls):
#         """
#         Checks if the directory exists, if not it creates it.
#         """
#         if not os.path.isdir(cls.SAVE_DIRECTORY):
#             os.makedirs(cls.SAVE_DIRECTORY)

#     @classmethod
#     def save_game(cls, player: Player) -> None:
#         """
#         Saves the current game conditions onto a JSON file.

#         parameters:
#         player (Player): The player from which the data has to be saved
#         """
#         cls.check_directory()
#         try:
#             filepath = os.path.join(cls.SAVE_DIRECTORY, cls.SAVE_FILE)
#             with open(filepath, 'w') as file:
#                 json_data = player.to_JSON()
#                 json.dump(json_data, file)
#             print("Game successfully saved.")
#         except Exception as e:
#             print(f"An error occurred while saving the game: {e}")

#     @classmethod
#     def load_game(cls) -> Player:
#         """
#         Loads the game from the previous saved game.

#         returns:
#         player (Player): The player from the previouslt saved game, in the
#         same room and with the same name and stats.
#         """
#         cls.check_directory()
#         try:
#             filepath = os.path.join(cls.SAVE_DIRECTORY, cls.SAVE_FILE)
#             with open(filepath, 'r') as file:
#                 json_data = json.load(file)
#                 player = Player.from_JSON(json_data)
#             print("Game successfully loaded.")
#             return player
#         except FileNotFoundError:
#             print("There is no saved game.")
#             return None
#         except Exception as e:
#             print(f"An error occurred while loading the game: {e}")
#             return None
