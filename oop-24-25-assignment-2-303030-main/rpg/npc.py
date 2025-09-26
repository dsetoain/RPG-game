from rpg.inspectable import Inspectable
from rpg.interactable import Interactable
from rpg.character import Character
from rpg.io_utils import Scanner
from rpg.combat import Combat
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from rpg.player import Player


class NPC(Inspectable, Interactable, Character):
    """
    The NPC class which inherits from inspectable, interactable, and character.
    """
    def __init__(
            self,
            description: str,
            interaction: str,
            health: int,
            damage: str
            ) -> None:
        """
        Initializes an NPC with its description, interaction, health, and
        damage. Also initialize inspectable, interactable and character.
        """
        Inspectable.__init__(self, description)
        Interactable.__init__(self, interaction)
        Character.__init__(self, description, health, damage)

    def inspect(self) -> None:
        """
        Prints the description of the NPC.
        """
        print(self.description)

    def interact(self, player: 'Player') -> None:
        """
        Handles the interaction between the player and the NPC.
        Shows the interaction options and makes the player's choice.

        parameters:
        player (Player): The player that is interacting with the NPC
        """
        self._options()
        player_interaction = Scanner.read_input()
        if player_interaction == 0:
            self._dialogue(player)
        elif player_interaction == 1:
            fight = Combat(player, self)
            fight.start()
        else:
            print("Please select a valid number.")

    def _dialogue(self, player: 'Player'):
        """
        Shows the NPC's interaction message.

        parameters:
        player (Player): The player interacting with the NPC.
        """
        print(self.interaction)
        print("Nothing else happens, and you decide "
              "to continue investigating the room.")

    def _options(self) -> None:
        """
        Shows the options available to the player when interaction
        with an NPC.
        """
        print(f"\nWhat do you want to do with the {self.description}?")
        print("(0) Speak")
        print("(1) Start a fight")

    @staticmethod
    def from_JSON(data: dict) -> 'NPC':
        """
        Creates an NPC instance from the JSON representation.

        parameters:
        data (dict): A dictionary with the representation of the NPC in JSON
        format.

        returns: The NPC instance recreated
        """
        description = data.get("description")
        interaction = data.get("interaction")
        return NPC(description, interaction)
