from rpg.npc import NPC
from rpg.enemy import Enemy
from rpg.room_inspect import InspectableRoom
from rpg.door import Door
from rpg.healer import Healer
from rpg.friend import Friend


class EntitiesManager:
    """
    This calss is responsible for managing all the entities in the game,
    such as all the rooms, npcs, and doors
    """
    def __init__(self) -> None:
        """
        Initializes the EntitiesManager by creating rooms, doors, and
        entities and connecting everything to the correct rooms.
        """
        self.room1 = InspectableRoom("a shadowy room with the faint smell of "
                                     "damp stone. Faint whispers echo through "
                                     "the corridor.")
        self.room2 = InspectableRoom("a room where piles of bones litter the "
                                     "ground, reminiscing of past adventurers "
                                     "who met their end here.")
        self.room3 = InspectableRoom("a quiet room with a small shrine at its "
                                     "center, bathed in an eerie glow.")
        self.room4 = InspectableRoom("a room filled with broken weapons and "
                                     "armor, remnants of battles long past.")
        self.room5 = InspectableRoom("a long hallway lined with tall mirrors, "
                                     "distorting your image.")
        self.room6 = InspectableRoom("a serene room filled with "
                                     "soft, golden light. The air is fragrant "
                                     "with herbs and flowers.")
        self.final_room = InspectableRoom("a vast chamber bathed in a golden "
                                          "light that seems to emanate from "
                                          "the Scepter of Power resting on a "
                                          "majestic pedestal at the center.")

        self.door1_2 = Door("heavy wooden door", self.room2)
        self.door1_3 = Door("rusted iron door", self.room3)
        self.door2_4 = Door("stone archway", self.room4)
        self.door3_5 = Door("polished marble door", self.room5)
        self.door5_4 = Door("heavy iron door", self.room4)
        self.door4_6 = Door("golden door", self.room6)
        self.door6_final = Door("narrow hallway", self.final_room)

        self.room1.add_door(self.door1_2)
        self.room1.add_door(self.door1_3)
        self.room2.add_door(self.door2_4)
        self.room3.add_door(self.door3_5)
        self.room4.add_door(self.door4_6)
        self.room5.add_door(self.door5_4)
        self.room6.add_door(self.door6_final)

        self.npc5 = NPC(
            "lost cat",
            "Startled, the cat runs away.",
            health=10,
            damage=2)
        self.npc6 = NPC(
            "beautiful priestess",
            "With a gentle smile, the priestess looks at you and says, "
            "'The Scepter of Power lies in the next room. You have come far, "
            "brave adventurer.'",
            health=200,
            damage=10
        )

        self.friend1 = Friend(
            "old soldier",
            "Looking exhausted but determined, he offers you his iron sword.",
            health=10,
            damage=3,
            weapon="iron sword",
            damage_increase=2)
        self.friend2 = Friend(
            "woman dressed like a grave robber",
            "A former grave robber, now regretful, offers you a weapon to "
            "aid your quest.",
            health=20,
            damage=5,
            weapon="blacksteel mace",
            damage_increase=4)
        self.friend4 = Friend(
            "tired blacksmith",
            "A weary blacksmith offers to forge you a stronger weapon.",
            health=30,
            damage=8,
            weapon="sacred halberd",
            damage_increase=5)

        self.healer3 = Healer(
            "priest dressed in a black robe",
            "The shadow priest mutters strange incantations and "
            "offers to heal your wounds.",
            health=50,
            damage=10,
            max_healing_done=7)
        self.healer4 = Healer(
            "ethereal spirit",
            "A spirit of light hovers nearby, ready to mend your wounds with "
            "a touch of magic.",
            health=100,
            damage=20,
            max_healing_done=10)

        self.enemy1 = Enemy(
            "small man with an eye patch",
            "You cautiously approach the man. Suddenly, he dashes towards you,"
            " attempting to stab you!",
            health=10,
            damage=2)
        self.enemy2 = Enemy(
            "human skeleton",
            "Animated by dark magic, the skeleton rises from the pile of bones"
            " and lifts their axe, ready to strike.",
            health=15,
            damage=3)
        self.enemy4_1 = Enemy(
            "dummy covered in heavy armor",
            "The dummy suddenly starts moving, and menacingly begins "
            "walking towards you.",
            health=40,
            damage=4)
        self.enemy5 = Enemy(
            "mirror image of yourself",
            "Your own reflection steps out of the mirror, "
            "attacking with your own moves!",
            health=20,
            damage=4)
        self.enemy6 = Enemy(
            "spectral figure",
            "The spectral figure reveals itself to be a banshee."
            "She swiftly lunges at you, releasing a mournful scream.",
            health=25,
            damage=5)

        self.room1.add_npc(self.friend1)
        self.room1.add_npc(self.enemy1)

        self.room2.add_npc(self.friend2)
        self.room2.add_npc(self.enemy2)

        self.room3.add_npc(self.healer3)

        self.room4.add_npc(self.friend4)
        self.room4.add_npc(self.enemy4_1)
        self.room4.add_npc(self.healer4)

        self.room5.add_npc(self.npc5)
        self.room5.add_npc(self.enemy5)

        self.room6.add_npc(self.npc6)
        self.room6.add_npc(self.enemy6)

    def intro(self):
        print(
            "\nYou are a lone adventurer on a quest to retrieve the Scepter of"
            " Power, hidden within the Labyrinth of Shadows. This ancient "
            "dungeon is filled with enemies and magical beings."
            )

    def outro(self):
        print(
            "\nAs you approach the pedestal, the Scepter of Power glimmers "
            "in the dim light, radiating a warm, golden glow that fills "
            "the room with an otherworldly energy. You reach out and grasp "
            "the scepter, feeling its weight and strength coursing through "
            "your veins. The whispers of the dungeon fade, replaced by a "
            "powerful hum resonating within you.\n\n"

            "Suddenly, the ground shakes, and a flash of light envelops you. "
            "You feel the presence of ancient spirits surrounding you, their "
            "voices echoing in your mind:\n\n"

            "\"You have proven your worth, brave adventurer. The Scepter is "
            "yours, a symbol of your triumph over the darkness that sought "
            "to consume this realm.\"\n\n"

            "As the light dissipates, you find yourself at the entrance of "
            "the Labyrinth of Shadows, the scepter firmly in hand. You turn "
            "to take one last look at the dungeon, now forever changed by "
            "your presence. The air is lighter, and the whispers have "
            "transformed into a gentle breeze, as if the dungeon itself is "
            "breathing a sigh of relief.\n\n"

            "With the Scepter of Power, you hold the key to reshape your "
            "destiny and restore balance to the world. Your journey has just "
            "begun, and many adventures await you beyond the shadows. Will "
            "you use the scepter to protect the innocent or pursue greater "
            "power? The choice is yours.\n\n"

            "Congratulations, you have completed the game!"
        )
        exit()
