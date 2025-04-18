import random

class Pet:
    def __init__(self, name, element="Earth"):
        """
        Initialize a magical pet with a name and elemental type.
        
        Args:
            name (str): The pet's name.
            element (str): The pet's element (Fire, Water, Earth, Air). Defaults to Earth.
        """
        self.name = name  # Pet's name
        self.element = element.capitalize()  # Elemental type (e.g., Fire, Water)
        self.hunger = 5  # Hunger level (0 = full, 10 = starving)
        self.energy = 5  # Energy level (0 = exhausted, 10 = vibrant)
        self.happiness = 5  # Happiness level (0 = gloomy, 10 = ecstatic)
        self.tricks = []  # List to store learned tricks
        self.quests_completed = 0  # Counter for completed quests
        self.mood = self._calculate_mood()  # Initial mood based on stats
        print(f"🪄 A magical {self.element} creature named {self.name} has joined you! ✨")

    def _calculate_mood(self):
        """
        Calculate the pet's mood based on hunger, energy, and happiness.
        
        Returns:
            str: Mood description (Ecstatic, Cheerful, Grumpy, Miserable) with emoji.
        """
        # Average stats: lower hunger and higher energy/happiness = better mood
        avg_stats = (self.hunger + (10 - self.energy) + (10 - self.happiness)) / 3
        if avg_stats < 3:
            return "Ecastic 😻"
        elif avg_stats < 5:
            return "Cheerful 🐾"
        elif avg_stats < 7:
            return "Grumpy 😾"
        else:
            return "Miserable 😿"

    def eat(self):
        """Feed the pet with magical, element-specific treats."""
        # Reduce hunger by 3, but not below 0
        self.hunger = max(0, self.hunger - 3)
        # Increase happiness by 1, but not above 10
        self.happiness = min(10, self.happiness + 1)
        # Update mood after eating
        self.mood = self._calculate_mood()
        # Element-specific treats for flavor
        treats = {
            "Fire": "🔥 Spicy Ember Berries",
            "Water": "💧 Crystal Kelp",
            "Earth": "🌱 Mystic Mushrooms",
            "Air": "☁️ Zephyr Cakes"
        }
        print(f"{self.name} munches on {treats[self.element]}! 🦴 Hunger down, happiness up!")

    def sleep(self):
        """Let the pet rest in an element-themed magical slumber."""
        # Increase energy by 5, but not above 10
        self.energy = min(10, self.energy + 5)
        # Update mood after sleeping
        self.mood = self._calculate_mood()
        # Element-specific dream descriptions
        dreams = {
            "Fire": "dreams of soaring volcanoes 🌋",
            "Water": "drifts in a sparkling ocean 🌊",
            "Earth": "naps under a glowing tree 🌳",
            "Air": "floats among starry clouds ☄️"
        }
        print(f"{self.name} {dreams[self.element]}! 😴 Energy restored!")

    def play(self):
        """Play with the pet using its elemental powers, if energy allows."""
        if self.energy >= 2:  # Check if pet has enough energy
            # Decrease energy by 2, but not below 0
            self.energy = max(0, self.energy - 2)
            # Increase happiness by 2, but not above 10
            self.happiness = min(10, self.happiness + 2)
            # Increase hunger by 1, but not above 10
            self.hunger = min(10, self.hunger + 1)
            # Update mood after playing
            self.mood = self._calculate_mood()
            # Element-specific play activities
            games = {
                "Fire": "chases flaming comets! 🔥",
                "Water": "splashes in enchanted puddles! 💦",
                "Earth": "rolls down sparkling hills! 🌿",
                "Air": "soars through rainbow winds! 🌬️"
            }
            print(f"{self.name} {games[self.element]} 🎉 Happiness up, energy down!")
        else:
            print(f"{self.name} is too tired to play! 😴 Try letting them sleep.")

    def get_status(self):
        """Display the pet's current state with magical flair."""
        print(f"\n🌟 {self.name}, the {self.element} Creature 🌟")
        print(f"🍎 Hunger: {self.hunger}/10")
        print(f"⚡ Energy: {self.energy}/10")
        print(f"😺 Happiness: {self.happiness}/10")
        print(f"🧠 Mood: {self.mood}")
        print(f"🎯 Tricks: {self.tricks if self.tricks else 'None yet!'}")
        print(f"🏆 Quests Completed: {self.quests_completed}")

    def train(self, trick):
        """
        Teach the pet a magical trick, if not already learned.
        
        Args:
            trick (str): The trick to learn.
        """
        if trick not in self.tricks:  # Check for duplicate tricks
            self.tricks.append(trick)  # Add new trick to list
            # Increase happiness by 1, but not above 10
            self.happiness = min(10, self.happiness + 1)
            # Update mood after training
            self.mood = self._calculate_mood()
            print(f"{self.name} mastered the {trick} trick! 🎇 Happiness boosted!")
        else:
            print(f"{self.name} already knows {trick}! Try a new one. 🧙")

    def show_tricks(self):
        """Show off all the pet's learned tricks."""
        if self.tricks:  # Check if any tricks are learned
            print(f"{self.name} performs their tricks: 🎭 {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet. Time to train! 📚")

    def go_on_quest(self):
        """Send the pet on an epic, element-themed quest, if stats allow."""
        if self.energy >= 3 and self.happiness >= 3:  # Check quest requirements
            # Decrease energy by 3, but not below 0
            self.energy = max(0, self.energy - 3)
            # Increase hunger by 2, but not above 10
            self.hunger = min(10, self.hunger + 2)
            # Increase happiness by random amount (1-3), but not above 10
            self.happiness = min(10, self.happiness + random.randint(1, 3))
            self.quests_completed += 1  # Increment quest counter
            # Update mood after quest
            self.mood = self._calculate_mood()
            # Element-specific quest stories
            quests = {
                "Fire": "battled a rogue phoenix! 🦅",
                "Water": "explored a sunken temple! 🪸",
                "Earth": "unearthed a hidden crystal cave! 💎",
                "Air": "raced a thunderstorm! ⚡"
            }
            print(f"{self.name} {quests[self.element]} 🗺️ Quest complete! Happiness up, energy down!")
        else:
            print(f"{self.name} needs more energy (3+) or happiness (3+) for a quest! 😓")