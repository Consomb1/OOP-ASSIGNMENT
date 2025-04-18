
# 🐾 Magical Creature Pet Simulator 🐉🌊🌪️🌱

Welcome to our team's submission for the **Digital Pet Python OOP Challenge**!  
This virtual pet simulator uses **Object-Oriented Programming in Python** and features a fantasy twist—your pets are **magical creatures** with **elemental powers**: Fire, Water, Earth, or Air.

---

## ✨ Project Overview

The `Pet` class creates magical creatures with unique personalities and powers. Each pet has a name, an elemental type, and dynamic attributes like hunger, energy, and happiness.  
They can:

- Eat special elemental meals 🍴  
- Sleep 😴  
- Play with magical items 🧸  
- Learn powerful tricks 🎩  
- Embark on epic quests 🌍  

Plus, a **mood system** and **emoji-enhanced outputs** make interactions engaging and immersive!

---

## 🔑 Key Features

- **🌋 Elemental Types:** Fire, Water, Earth, or Air—each with unique behaviors and flavor text.  
- **😺 Mood System:** Displays emotional states (Ecstatic, Cheerful, Grumpy, Miserable) based on current stats.  
- **🗺️ Quest System:** Epic adventures tailored to each element. Requires energy & happiness to unlock.  
- **😄 Emoji Outputs:** GitHub-friendly emoji shortcodes like `:fire:`, `:sparkles:` make output lively and fun.  
- **🎓 Bonus Tricks:** Pets can learn tricks with `train()` and showcase them via `show_tricks()`.  
- **🛡️ Robust Design:** Handles stat limits, edge cases, duplicate tricks, and provides clear feedback.  

---

## 🧱 Project Structure

```
├── pet.py      # Core Pet class with all methods and features  
├── main.py     # Script to create/test magical pets  
└── README.md   # Project overview and instructions (this file)  
```

---

## ⚙️ Setup & Running

### 🚀 How to Run

1. **Clone or Download the Repository**  
2. Navigate to the Project Folder  
3. Run the Main Script  

```bash
python main.py
```

### 🧪 Example Usage

In `main.py`:

```python
from pet import Pet

# Create pets
dragon = Pet("Flare", "Fire")
mermaid = Pet("Aqua", "Water")

# Test Flare
dragon.eat()
dragon.play()
dragon.train("flame spin")
dragon.go_on_quest()
dragon.get_status()

# Test Aqua
mermaid.play()
mermaid.eat()
mermaid.go_on_quest()
mermaid.energy = 1
mermaid.go_on_quest()  # Should fail due to low energy
```

---

## 🖥️ Sample Output

```
=== Creating Magical Pets ===
:sparkles: A magical Fire creature named Flare has joined you! :sparkles:
:sparkles: A magical Water creature named Aqua has joined you! :sparkles:

=== Testing Flare the Fire Creature ===
Flare munches on :fire: Spicy Ember Berries! :bone: Hunger down, happiness up!
Flare chases flaming comets! :fire: :tada: Happiness up, energy down!
Flare mastered the flame spin trick! :sparkles: Happiness boosted!
Flare battled a rogue phoenix! :world_map: Quest complete! Happiness up, energy down!

:star2: Flare, the Fire Creature :star2:
:apple: Hunger: 3/10
:zap: Energy: 2/10
:smiley_cat: Happiness: 10/10
:brain: Mood: Cheerful :feet:
:dart: Tricks: ['flame spin']
:trophy: Quests Completed: 1

=== Testing Aqua the Water Creature ===
Aqua splashes in enchanted puddles! :droplet: :tada: Happiness up, energy down!
Aqua munches on :droplet: Crystal Kelp! :bone: Hunger down, happiness up!
Aqua explored a sunken temple! :coral: :world_map: Quest complete! Happiness up, energy down!
Aqua needs more energy (3+) or happiness (3+) for a quest! :disappointed:
```

💡 *Note: Quest outcomes may vary due to random happiness boosts (1–3).*

---

## 🌟 Creative Enhancements

- **Elemental Flavors** – Fire pets eat Ember Berries, Earth pets dig through crystal caves, and more!  
- **Moods** – Adds personality based on combined stats  
- **Quests** – Track completions for progress and storytelling  
- **Emojis** – GitHub-compatible for fun and clarity  
- **Error Handling** – Clean feedback on invalid actions and stat thresholds  

---

## 🚀 Potential Future Features

- **⚔️ Pet Battles** – Pets duel with learned tricks  
- **📈 Leveling System** – Gain levels based on quests or training  
- **🖼️ GUI Integration** – Build a Tkinter interface  
- **🤝 Group Quests** – Pets can team up for cooperative missions  

---

## 📦 Submission Details

- `pet.py` - Pet class with all logic.  
- `main.py` - Demonstrates features and edge cases.  
- `README.md` - This file.  

---

🙌 **Acknowledgments**  
This was a collaborative team project crafted with passion for programming and fantasy.  
Thanks to the organizers for the fun and engaging challenge! 💖
