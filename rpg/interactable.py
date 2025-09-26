from abc import ABC, abstractmethod
from copy import deepcopy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from rpg.player import Player


class Interactable(ABC):
    """
    An abstract base class that represents an interactable object.
    """
    def __init__(self, interaction: str) -> None:
        """
        Initializes the interactable instance

        parameters:
        interaction (str): The message of how the player can interact
        with the object.
        """
        self._interaction = interaction

    @property
    def interaction(self) -> str:
        """
        Getter for the interaction description

        returns:
        a deepcopy of the interaction message
        """
        return deepcopy(self._interaction)

    @interaction.setter
    def interaction(self, new_interaction: str) -> None:
        """
        Sets the new interaction description on the object

        parameters:
        new_interaction (str): The new interaction description to be set
        """
        self._interaction = new_interaction

    @abstractmethod
    def interact(self, player: 'Player') -> None:
        """
        An abstract method that all subclasses have to implement to interact
        with an object.

        parameters:
        player (Player): The player that interacts with the object.
        """
        pass
