from rpg.io_utils import Scanner
from random import random
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from rpg.npc import NPC
    from rpg.player import Player


class Combat:
    """
    This class serves the purpose to only combat between a player and an enemy.
    It handles the combat turns, including attack options, escape attempts, and
    determining the outcome of the fight.
    """
    def __init__(self, player: 'Player', enemy: 'NPC') -> None:
        """
        Initializes a combat instance with a player and an enemy

        parameters:
        player (Player): The player engaging in combat
        enemy (NPC): The enemy also engaged in combat with the player
        """
        self.player = player
        self.enemy = enemy
        self.in_combat = True

    def start(self) -> None:
        """
        Starts the fight. This method repeatedly changers turns between
        the player and the enemy until either the player or the enemy's health
        reaches 0, or the player successfully escapes.
        """
        print("You prepare yourself for a fight.")
        while (self.player.health > 0 and self.enemy.health > 0
               and self.in_combat):
            self._player_turn()
            self._enemy_turn()
            self.player.check_stats()
            self.enemy.check_stats()
        self._end_combat()

    def _options(self) -> None:
        """
        Method to display the options to the player during their turn.
        The player can choose to attack the enemy or try to escape.
        """
        print("\nWhat do you want to do?")
        print("(0) Attack the opponent")
        print("(1) Try to escape the fight")
        # print("(2) Use food to heal") -> items system

    def _player_turn(self) -> None:
        """
        This method manages the player's turn in the fight.
        The player can either attack the enemy or attempt to flee.
        """
        self._options()
        player_choice = Scanner.read_input()
        if player_choice == 0:
            print(f"\nYou deal {self.player.damage} damage to "
                  f"the {self.enemy.description}.")
            self.enemy.health -= self.player.damage
        elif player_choice == 1:
            if (self._escape_attempt()):
                self.in_combat = False
            else:
                print("\nYou failed to escape.")

    def _enemy_turn(self) -> None:
        """
        This method manages the enemy's turn in the figtht.
        It checks if the enemy is still alive and the player has not escaped,
        to determine if the enemy attacks the player and reduces their health.
        """
        if self.enemy.health > 0 and self.in_combat:
            print(f"The {self.enemy.description} deals "
                  f"{self.enemy.damage} damage to you.")
            self.player.health -= self.enemy.damage

    def _escape_attempt(self) -> bool:
        """
        This method handles when the player want to escape the fight.
        The success of the escape is determined by comparing the player's
        and the enemy's damage values to calculate a probability.

        returns:
        Bool: True if the escape attempt is successful, if not false.
        """
        attack_diff = self.enemy.damage - self.player.damage
        base_chance = 0.4
        if attack_diff > 0:
            chance_to_flee = min(0.9, base_chance + (attack_diff * 0.1))
        else:
            chance_to_flee = max(0.1, base_chance + (attack_diff * 0.05))
        return random() < chance_to_flee

    def _end_combat(self) -> None:
        """
        In order to finish the fight, this methoid prints the result
        based on the final health values of the player and the enemy.
        If the player escapes or defeats the enemy, the fight ends.
        If the player dies, the game is over.
        """
        if self.player.health > 0 and self.enemy.health > 0:
            print("\nYou managed to escape succesfully.")
            self.enemy.health = 0
            return
        elif self.enemy.health <= 0:
            print(f"\nYou have defeated the {self.enemy.description}!")
            return
        else:
            print(f"\n{self.player.name} has been defeated by "
                  f"the {self.enemy.description}!\n"
                  f"GAME OVER")
            exit()
