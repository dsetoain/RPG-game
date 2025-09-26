from rpg.room_inspect import InspectableRoom
from rpg.character import Character
from copy import deepcopy


class Player(Character):
    """
    A class that describes the player in the game. Inherits from character and
    JsonSetializable.
    """
    def __init__(
            self,
            name: str,
            start_room: InspectableRoom,
            health: int,
            damage: int,
            ) -> None:
        """
        initializes an instance of the player with its characteristics
        (parameters). Also calls the super of character as the player
        is also a character.

        parameters:
        name (str): The name of the player.
        start_room (InspectableRoom): The room where the player starts
        the game.
        health (int): The health of the player.
        damage (int): The damage the player can do.
        """
        super().__init__(name, health, damage)
        self._room = start_room
        self._max_health = health

    @property
    def room(self) -> InspectableRoom:
        """
        Getter for the current room the player is in.

        returns
        self._room (InspectableRoom): The room the player is currently in
        """
        return self._room

    @property
    def max_health(self) -> int:
        """
        Getter for the health of the player.

        returns:
        a deepcopy of the max health of the player
        """
        return deepcopy(self._max_health)

    @max_health.setter
    def max_health(self, new_max: int) -> None:
        """
        Setter for a new max health for the player.

        parameters:
        new_max (int): The new max health the player has
        """
        if not isinstance(new_max, int):
            raise TypeError("Argument has to be of type int")
        self._max_health = new_max

    @room.setter
    def room(self, new_room: InspectableRoom) -> None:
        """
        Sets a new room for the player.

        parameters:
        new_room (InspectableRoom): Ther new room the player is in
        """
        if isinstance(new_room, InspectableRoom):
            print(f"\nYou enter {new_room.description}\n")
            self._previous_room = self._room
            self._room = new_room
        else:
            raise TypeError("argument has to be of type Room")
