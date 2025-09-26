from rpg.player import Player
from rpg.io_utils import Scanner
from rpg.entities_manager import EntitiesManager
from typing import List


class Game(EntitiesManager):
    """
    This class manages all the game, and player interactions
    """
    def __init__(self) -> None:
        """
        Initializes the Game instance, as well as calling the super() of the
        EntitiesManager class. Also asks the user what the character name is
        and sets the stats to the default.
        """
        super().__init__()
        self.player = Player("default", self.room1, 30, 3)

    def _options(self) -> None:
        """
        Used to display the actions the player can take during their turn.
        """
        print("\nWhat do you want to do?")
        print("(0) Look around")
        print("(1) Look for a way out")
        print("(2) Look for company")
        print("(3) Check your stats")
        print("(9) Quit Game")

    def run(self) -> None:
        """
        The main game loop that allows the player to perform actions
        until the game finishes or is quitted
        """
        player_name = input("Enter your character's name: ")
        self.player.name = player_name
        while True:
            self._options()
            player_option = Scanner.read_input()

            if player_option == 0:
                self.player.room.inspect()
            elif player_option == 1:
                self._look_for_a_way_out()
            elif player_option == 2:
                self._look_for_company()
            elif player_option == 3:
                self.player.check_stats()
            elif player_option == 9:
                print("Quitting Game")
                break
            else:
                print("Please select a valid number.")

            self.player.room.remove_used_npcs()

            if self.player.room.description == self.final_room.description:
                self.outro()

    def _look_for_a_way_out(self) -> None:
        """
        Option that allows the player to inspect and interact
        with doors in the current room.
        """
        doors = self.player.room.door_list
        self.player.room.inspect_doors()
        door_number = self._get_valid_number([-1, len(doors)])
        doors[door_number].interact(self.player)
        Scanner.wait_for_input()

    def _look_for_company(self) -> None:
        """
        Option that allows the player to inspect and interact with the
        NPCs in the current room.
        """
        npcs = self.player.room.npc_list
        self.player.room.inspect_npcs()
        npc_number = self._get_valid_number([-1, len(npcs)])
        npcs[npc_number].interact(self.player)
        Scanner.wait_for_input()

    def _get_valid_number(self, valid_range: List[int]) -> int:
        """
        Asks the user for an input value until a valid number is provided.
        """
        user_input = Scanner.read_input()
        while not (valid_range[0] <= user_input < valid_range[1]):
            print("\nPlease select a valid number")
            user_input = Scanner.read_input()
        return user_input
