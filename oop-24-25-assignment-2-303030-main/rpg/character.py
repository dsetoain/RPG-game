from copy import deepcopy


class Character:
    """
    This class is used as a base class for all the characters in the game,
    including the player, NPCs, and enemies. It defines the attributes
    of name, health, and damage
    """
    def __init__(self, name: str, health: int, damage: int):
        """
        Initializes a new instance of the character class. The parameters,
        are stored as privatte attributes in order to not allow them to be
        changed by the user

        Parameters:
        name (str): The characters name
        health (int): The amount of hp the character has
        damage (int): The amount of damage they do every attack
        """
        self._name = name
        self._health = health
        self._damage = damage

    @property
    def name(self):
        """
        Getter for the characters name

        Returns:
        A deepcopy of self._name to ensure the original value
        remains immutable outside the class.
        """
        return deepcopy(self._name)

    @property
    def health(self):
        """
        Getter for the health of the character

        Returns:
        A deepcopy of self._health in order to not be able to modify the value
        """
        return deepcopy(self._health)

    @property
    def damage(self):
        """
        A getter for the damage a character does

        Returns:
        A deepcopy of self.damage in order to maintain the value of self.damage
        immutable.
        """
        return deepcopy(self._damage)

    @name.setter
    def name(self, new_name: str):
        """
        The setter to set the value for a characters name

        Parameters:
        new_name (str): The new name the character has
        """
        if not isinstance(new_name, str):
            raise TypeError("Argument must be of type str.")
        self._name = new_name

    @health.setter
    def health(self, new_health: int):
        """
        The setter to set the value for a characters health

        Parameters:
        new_health (int): The new health the character has
        """
        if not isinstance(new_health, int):
            raise TypeError("Argument must be of type int.")
        self._health = new_health

    @damage.setter
    def damage(self, new_damage):
        """
        The setter to set the value for a characters damage

        Parameters:
        new_damage (int): The new damage value to assign to the character
        """
        if not isinstance(new_damage, int):
            raise TypeError("Argument must be of type int.")
        self._damage = new_damage

    def check_stats(self):
        """
        This method displays the character's current stats
        (health and damage) in a formatted string.
        """
        print(f"\n{self.name}:\n {self.health} HP\n {self.damage} ATK")
