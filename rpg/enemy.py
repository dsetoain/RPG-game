from rpg.npc import NPC
from rpg.combat import Combat
from rpg.player import Player


class Enemy(NPC):
    """
    This class extends from the NPC functionality in order to create
    enemies that attack the player
    """
    def __init__(
            self,
            description: str,
            interaction: str,
            health: int,
            damage: int,
            ) -> None:
        """
        Initializes a enemy instance with a description,
        interaction text, health, and damage.
        Also NPC class is initialized.

        parameters:
        description (str): A small description to print for the user to see
        interaction (str): A message displayed when the player interacts with
        the enemy.
        health (int): The total health of the enemy
        damage (int): The amount of damage the enemy does every hit
        """
        NPC.__init__(self, description, interaction, health, damage)

    def interact(self, player: Player) -> None:
        """
        This method says that when the player interacts with the enemy,
        a combat session is started. A message is printed to describe the
        interaction, and then the initialization of a combat instance.

        paramteres:
        player (Player): The player that interacts with the enemy
        """
        print(self.interaction)
        fight = Combat(player, self)
        fight.start()
