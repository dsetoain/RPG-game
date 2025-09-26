from rpg.inspectable import Inspectable
from rpg.interactable import Interactable
from copy import deepcopy
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from rpg.room import Room
    from rpg.player import Player


class Door(Inspectable, Interactable):
    """
    This class represents a Door object that connects two rooms.
    The Door can be inspected, interacted with,
    and serialized to/from JSON format.

    This class inherits from Inspectable, Interactable and JsonSerializable.
    """
    def __init__(
            self,
            default_description: str,
            next_room: 'Room'
            ) -> None:
        """
        Initializes a door with a description and the attached room.

        parameters:
        default_description (str): The doors description that appears
        when inspecting it next_room (Room): The room that the player
        will be in if he interacts with the door

        Also, the Inspectable class is initiated here.
        """
        Inspectable.__init__(self, default_description)
        self._next_room = next_room

    @property
    def next_room(self) -> 'Room':
        """
        Getter for the room the door leads to.

        returns:
        Room : A deepcopy of the room the door leads to.
        """
        return deepcopy(self._next_room)

    def inspect(self) -> None:
        """
        This method displays the door's description,
        typically used for the player when he inspects the door.
        """
        print(self.description)

    def interact(self, player: 'Player') -> None:
        """
        Allows the player to interact with the door,
        the player's current room is then updated to the room on the
        other side of the door.

        parameters:
        player (Player): The player that interacts with the door
        """
        player.room = self.next_room
