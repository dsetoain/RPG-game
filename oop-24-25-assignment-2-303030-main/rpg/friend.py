from rpg.npc import NPC
from rpg.player import Player


class Friend(NPC):
    """
    This class represents a friendly NPC that can assist the player by
    providing a weapon and increasing the player's damage.
    """
    def __init__(
            self,
            description: str,
            interaction: str,
            health: str,
            damage: str,
            weapon: str,
            damage_increase: int
            ) -> None:
        """
        Used to initialize the friend instance. Also the NPC is initialized.

        parameters:
        description (str): The description of the NPC.
        interaction (str): The dialogue that appears when the player interacts
        with the NPC.
        health (int): The health of the friend.
        damage (int): The damage value of the friend which does not matter
        as they domnt attack.
        weapon (str): The weapon given to the player.
        damage_increase (int): The increase in player's damage.
        """
        NPC.__init__(self, description, interaction, health, damage)
        self.weapon = weapon
        self.damage_increase = damage_increase

    def _dialogue(self, player: Player) -> None:
        """
        This method serves for the interaction message when the player
        interacts with a friend NPC. Also increases the player's damage
        and kills the friend so the player can not interact with him again.
        """
        print(self.interaction)
        player.damage += self.damage_increase
        print(f"You have received a {self.weapon}. "
              f"ATK increased by {self.damage_increase}")
        self.health = 0  # Indicate that this NPC has been "used"
