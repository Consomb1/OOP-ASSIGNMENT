from pet import Pet

# Create two magical pets with different elements
print("=== Creating Magical Pets ===")
dragon = Pet("Flare", "Fire")  # Fire-type pet named Flare
mermaid = Pet("Aqua", "Water")  # Water-type pet named Aqua

# Test Flare's abilities
print("\n=== Testing Flare the Fire Creature ===")
dragon.eat()  # Feed Flare
dragon.play()  # Play with Flare
dragon.sleep()  # Let Flare rest
dragon.train("flame spin")  # Teach a trick
dragon.train("ember dance")  # Teach another trick
dragon.train("flame spin")  # Try duplicate trick
dragon.go_on_quest()  # Send Flare on a quest
dragon.get_status()  # Show Flare's status
dragon.show_tricks()  # Display Flare's tricks

# Test Aqua's abilities
print("\n=== Testing Aqua the Water Creature ===")
mermaid.play()  # Play with Aqua
mermaid.eat()  # Feed Aqua
mermaid.go_on_quest()  # Send Aqua on a quest
mermaid.energy = 1  # Simulate low energy for edge case
mermaid.go_on_quest()  # Try quest with low energy (should fail)
mermaid.get_status()  # Show Aqua's status