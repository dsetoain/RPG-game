from rpg.npc import NPC
from rpg.player import Player
from copy import deepcopy


class Healer(NPC):
    """
    This class is for a type of NPC that heals the player instead of
    doing damage. It inherits from NPC.
    """
    def __init__(
            self,
            description: str,
            interaction: str,
            health: int,
            damage: int,
            max_healing_done: int,
            ) -> None:
        """
        Initializes a healer and the NPC class.

        parameters:
        description (str): The description of the healer NPC.
        interaction (str): The message the healer provides when
        interacted with.
        health (int): The health of the healer NPC.
        damage (int): The damage the healer can do eventhough they dont attack.
        max_healing_done (int): The maximum amount of health that the healer
        can restore to the player.
        """
        NPC.__init__(self, description, interaction, health, damage)
        self._max_healing_done = max_healing_done

    @property
    def max_healing_done(self) -> int:
        """
        Getter for the healing amount the healer gives

        returns:
        A deepcopy of self._max_healing_done which is the value the healer can
        potentially heal the player
        """
        return deepcopy(self._max_healing_done)

    def _dialogue(self, player: Player) -> None:
        """
        This method handles the interaction with the healers to provide healing

        parameters:
        player (Player): The player that is going to be healed
        """
        print(self.interaction)
        healing_required = player.max_health - player.health
        healing_done = min(self.max_healing_done, healing_required)
        player.health += healing_done
        if healing_done == 0:
            print("However, you don't seem to require any healing.")
        else:
            print(f"You have been healed for {healing_done} health. "
                  f"You now have {player.health} HP.")
