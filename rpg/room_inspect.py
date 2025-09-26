from rpg.room import Room
from rpg.inspectable import Inspectable
from rpg.npc import NPC
from rpg.door import Door
from typing import List, Union


class InspectableRoom(Room, Inspectable):
    """
    This class manages the inspectable options in the room, and inherits from
    Room and Inspectable
    """
    def __init__(self, default_description: str):
        """
        Initializes an InspectableRoom instance with a default description.
        Also initializes the Inspectable and Room class.

        parameters:
        default_description (str): The room's description
        """
        Inspectable.__init__(self, default_description)
        Room.__init__(self)

    def inspect(self) -> None:
        """
        Inspects the room, providing information about the room's
        description, the number of doors, and the number of NPCs in that room.
        """
        print(f"\nYou are in {self.description}")
        amount_of_doors = len(self.door_list)
        if amount_of_doors == 1:
            print("The room has only 1 door.")
        else:
            print(f"The room has {amount_of_doors} doors.")
        amount_of_npcs = len(self.npc_list)
        if amount_of_npcs == 1:
            print("The room has only 1 npc")
        elif amount_of_npcs > 1:
            print(f"The room has {amount_of_npcs} npcs.")
        else:
            print("There are no npcs in this room.")

    def inspect_doors(self) -> None:
        """
        Inspects the doors in the room
        """
        self._inspect_items(self.door_list, "door")

    def inspect_npcs(self) -> None:
        """
        Inspects the NPCs in the room
        """
        self._inspect_items(self.npc_list, "living being")

    def _inspect_items(
            self,
            items: List[Union[Door, NPC]],
            item_type: str
            ) -> None:
        """
        Inspects a list of item in the room.

        parameters:
        items (List[Union[Door, NPC]]): The list of inspectable items.
        item_type (str): The type of items being inspected (NPC, door)
        """
        if not items:
            print(f"\nThere are no {item_type}s in this room")
        else:
            print(f"\nYou look around for {item_type}s. You see:")
            for idx, item in enumerate(items):
                print(f"({idx}) A {item.description}")
            print(f"\nChoose which {item_type} to interact with. "
                  f"(-1 : do nothing)")
