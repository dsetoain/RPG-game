Character class:

The Character class serves as a blueprint for all character types in the game, including players, NPCs, and enemies.
The attributes name, health, and damage are made private to prevent manipulation of these values from outside the class.
However, by using the property decorator for health and damage, we can update these values as the game progresses, allowing
them to change depending on various scenarios. Furthermore, by returning deep copies of these values in the getters, we ensure
that the values remain immutable outside the class.


Combat class:

The Combat class is responsible for managing combat between a player and an enemy. It takes instances of Player and NPC as
parameters, allowing it to handle many character types within the combat system. The public attributes player, enemy, and
in_combat enable access to the combat state and the use of private methods for player and enemy turns encapsulates the combat
logic.
Randomness is introduced in the escape mechanics through the _escape_attempt method, which calculates the success of escaping
based on the damage values. 


Door class: 

The Door class represents a connection between two different rooms in the game. It inherits from Inspectable, Interactable,
and JsonSerializable. This design choice allows the Door class to have very different functionalities, such as: can be inspected
for a description, interacted with to change rooms, and serialized/deserialized for saving and loading game states.
The constructor initializes the door with a description and a reference to the next room, using the Inspectable parent class
initialization to set the door's description. 
The private attribute _next_room ensures that the internal state of the door is protected from outside changes.
The next_room property returns a deep copy of the _next_room attribute, ensuring immutability as we dont want to change it when
çaccessed from outside the class. The interact method modifies the player's room based on the door's connection, making it easy
for the player to move around in the game. 


Enemy:

The Enemy class extends the functionality of the NPC class in order to create enemies that can engage in combat with the player. 
The constructor initializes the enemy with attributes such as description, interaction, health, and damage, calling the NPC
superclass's initializer to set these inherited properties. This allows the Enemy class to inherit and extend the behaviors
defined in the NPC class.
The interact method is overridden to define how the player combats with the enemy. When a player interacts with an enemy,
it prints the interaction message and initializes a Combat instance, therefore transitioning the game state into a combat
not an NPC interaction. 


EntetiesManager class:

The EntitiesManager class serves as a centrer for managing all the entities in the game, including rooms, NPCs, doors.
Basically this class exists in order to contain and organize various components of the game seperately from the game code.
When initialized, the EntitiesManager creates several instances of InspectableRoom, Door, NPC, Enemy, Friend, and Healer,
which is where the layout of the game is made, and each entity is instantiated with their specific attributes, such as
descriptions, health, and damage.
The use of the add_door and add_npc methods connect the doors and NPCs to their rooms, makig sure that the details of these
relationships are managed within the EntitiesManager. This makes the code easier to understand.


Friend class:

The Friend class extends from the NPC class, and is used to make friendly NPCs that help thje playerby giving him weapons
and damage boosts. Inheriting from the NPC class allows us to reuse code and extend from existing functionalities.
In the constructor, the Friend class initializes its attributes, plus weapon and damage_increase, which are unique to friendly
NPCs. The use of the superclass's constructor NPC.__init__ gives us the intialization for properties like description,
interaction, health, and damage. 
The _dialogue method serves not only to display the interaction message but also modifies the player's state by increasing
their damage and providing a weapon. 
Additionally, setting self.health to 0 which "removes" the NPC from the game, preventing further interaction.


Game class:

The Game class handles the main game loop and player interactions. It inherits from the EntitiesManager, which helps in
setting up the rooms, doors, and NPCs. 
The constructor initializes a Player object with a name, current room, health, and damage values. And the use of super()
ensures that the game world is initialized by the EntitiesManager before the game starts.
The _options() method displays the player's available actions during their turn. 
And the run() method contains the main game loop, which reads user input and then calls the appropriate methods based on
the player's choice. 
The private methods _look_for_a_way_out() and _look_for_company() encapsulate player interactions with the doors and NPCs,
in order to provide reusable code for these actions. Both of these methods interact with the player's current room, and
retrieve lists of doors and NPCs to inspect or interact with.
The _get_valid_number() method makes sure that user input is valid, making the game smoother.


Healer class:

Very similar to friend, or enemy the Healer class represents an NPC that but in this case provides healing to the player,
rather than engaging in combat or giving a weapon. It inherits from the NPC class, allowing it to reuse the NPC functionality
and introduce unique behavior related to healers.
The constructor initializes the healer with a unique description, interaction message, health, damage (even though the healer
doesn't get attacked or attacks), and a maximum healing limit. 
The private attribute _max_healing_done is used to limit the health the healer can restore, in order to not give the player
more health than his maximum. 
The max_healing_done property decorator method returns a deep copy of this attribute to have immutability.
The _dialogue() method is used to descriube the interaction to the user between the player and the healer and it calculates
the healing required by the player, and then gives the healing, ensuring that the player's health does not exceed the maximum
limit. 


Inspectable class:

The Inspectable class is an abstract base class designed to represent objects in the game that can be inspected by the player.
This class is a blueprint for other classes,which use specific implementations of the inspect() method.
The constructor takes a description as a parameter, which is just the message that will be printed when the object is inspected.
The description is stored in the private attribute _description, restricting direct access to this data.
In order for the description to remain immutable, preventing it from being modified outside the class, a deepcopy is returned
from the getter.
The inspect() method is an abstract method, which means that all subclasses of Inspectable must implement this method. 


Interactable class:

This class is very similar to the inspectable class. The Interactable class is an abstract base class for objects that the
players can interact with. It has a private _interaction message, which can be accessed and modified through its getter and
setter. And the interact() method is abstract, meaning that all subclasses must have their version of it.


Scanner class:

The scanner class provides methods that manage the user input during the game. rread_input() makes sure that the input is an
integer and the wait_for_input() method pauses the game until the user presses enter which allows us to control the flow of
the game.
These methods are static methods as they dont need any instance data or nbehaviour and having read_input() and wait_for_input()
as static methods, all input logic is encapsulated in one class as well as making it more efficient.


NPC class:

The NPC class inherits from three abstract base classes: Inspectable, Interactable, and Character. This design choice was made
to allow the NPC to be inspected, interacted with , and also have character attributes such as health and damage. 
The constructor of the NPC class calls the __init__ methods of its parent classes, which makes sure that the attributes
description, interaction, health, and damage are properly initialized. 
The interact method, shows the interaction between the player and the NPC which is done by printing options for the player,
such as engaging in dialogue or starting a fight. Utilizing Scanner.read_input() for reading the user input allows the NPC
class to focus on interaction logic while the user input is managed by the scanner class. 


Player class:

The Player class inherits from both the Character and JsonSerializable classes.  By inheriting from Character, the Player
class has attributes like health and damage already which makes it easier to initialize.
In the constructor, the Player class initializes its properties, including the player's name, starting room, health, and
damage and calls the super().__init__() which makes sure the initialization from the Character class is done in order to
reducing code duplication. 
The class has properties for both the player's room and maximum health, which are accessed with setters and getters. The
room property decorator only retrieves the current room but also  prints a message when the player changes rooms to help with
the gameplay. 


Room class:

The Room class manages the rooms in the game and holds lists for the doors and npcs that are assigned to rooms. 
The constructor initializes the Room instance with the lists: _door_list for storing Doorsand _npc_list for storing NPCs.
These are made private as access to these lists would result in modifications being able to be made not only through the
required methods.
The door_list and npc_list property decorators give access to these private lists by the getters and setters. 
The add_door and add_npc methods make the addition of doors and NPCs to the room possible. Both these methods have type checks
to make sure that only valid instances of Door and NPC can be added. 
The remove_used_npcs method is used to removing NPCs whose health has fallen to zero or below as if not we would still be able
to interact with dead NPCs which makes no sense. This method lops over the _npc_list, and removes NPCs if their health is equal
or below 0. 


InspectableRoom class:

The InspectableRoom class improves on the Room class by giving it the ability to be inspected. This class inherits from Room
and Inspectable, which means it has to have the inspectable abstract method.
In the constructor, the class initializes the __init__() of Inspectable and Room.
The inspect method provides the description, the number of doors, and the number of NPCs in that specific room. This method gives the player information about the room they are in which is necessary for gameplay. 
The inspect_doors and inspect_npcs methods are used for players to indentify the doors and npcs in that room. These methods call the private method _inspect_items, which inspects any list of items, whether they are doors or NPCs. 
In order to do so, the _inspect_items method accepts a list of either Doors or NPCs and an item type as parameters.  The implementation checks if the list is empty and prints messages to the player, about the contents.
