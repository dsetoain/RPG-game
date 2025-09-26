from rpg.npc import NPC
from rpg.door import Door
from typing import List


class Room:
    """
    A class that manages the rooms in the game. Inherits from JsonSerializable.
    """
    def __init__(self) -> None:
        """
        Initializes a Room instance with empty lists for doors and NPCs.
        """
        self._door_list: List[Door] = []
        self._npc_list: List[NPC] = []

    @property
    def door_list(self) -> List[Door]:
        """
        getter for the list of doors

        returns:
        List[Door]: The list of doors in the room.
        """
        return self._door_list

    @property
    def npc_list(self) -> List[NPC]:
        """
        getter for the list of npcs

        returns:
        List[NPC]: The list of NPCs in the room.
        """
        return self._npc_list

    def add_door(self, door: Door) -> None:
        """
        Adds a door to a room.

        parameters:
        door (Door): The door that wants to be added to the room
        """
        if not isinstance(door, Door):
            raise TypeError("argument has to be of type Door")
        self._door_list.append(door)

    def add_npc(self, npc: NPC) -> None:
        """
        Adds a NPC to a room.

        parameters:
        npc (NPC): The NPC that wants to be added to the room
        """
        if not isinstance(npc, NPC):
            raise TypeError("argument has to be of type NPC")
        self._npc_list.append(npc)

    def remove_used_npcs(self) -> None:
        """
        Removes an NPC from the room if their health is less than or equal
        to zero.
        """
        for npc in self._npc_list:
            if npc.health <= 0:
                self._npc_list.remove(npc)
