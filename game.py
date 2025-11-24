import random

def print_divider():
    """Print a divider line to make the game easier to read."""
    print("-" * 50)

def roll_stat(min_value=5, max_value=15):
    """Return a random stat value between min_value and max_value."""
    return random.randint(min_value, max_value)

def create_character():
    """Ask the player for their name and role, then create stats."""
    print_divider()
    print("⚔️  WELCOME TO BLUDGEONS & FLAGONS  ⚔️")
    name = input("What is your hero's name? ")

    print("\nChoose your role:")
    print("1) Warrior (high HP)")
    print("2) Mage (high attack)")
    print("3) Rogue (balanced)")

    role_choice = input("Enter 1, 2, or 3: ")

    if role_choice == "1":
        role = "Warrior"
        hp = roll_stat(15, 25)      # Warriors are tanky
        attack = roll_stat(4, 8)
    elif role_choice == "2":
        role = "Mage"
        hp = roll_stat(10, 18)
        attack = roll_stat(6, 10)   # Mages hit hard
    else:
        role = "Rogue"
        hp = roll_stat(12, 20)
        attack = roll_stat(5, 9)

    # Return all character info in a dictionary
    return {
        "name": name,
        "role": role,
        "hp": hp,
        "attack": attack,
    }

def create_enemy():
    """Create a simple random enemy."""
    enemy_types = ["Goblin", "Skeleton", "Orc", "Bandit"]
    enemy_name = random.choice(enemy_types)
    enemy_hp = roll_stat(10, 20)
    enemy_attack = roll_stat(3, 6)

    return {
        "name": enemy_name,
        "hp": enemy_hp,
        "attack": enemy_attack,
    }

def player_turn(player, enemy):
    """Handle the player's turn. Returns True if the enemy is defeated."""
    print_divider()
    print(f"Your turn, {player['name']}!")
    print(f"1) Attack {enemy['name']}")
    print("2) Drink mysterious flagon (+random HP)")

    choice = input("Choose an action (1 or 2): ")

    if choice == "2":
        heal_amount = random.randint(4, 10)
        player["hp"] += heal_amount
        print(f"You drink the flagon and heal {heal_amount} HP!")
        print(f"Your HP is now {player['hp']}.")
        return False  # enemy not defeated
    else:
        # Basic attack
        damage = random.randint(1, player["attack"])
        enemy["hp"] -= damage
        print(f"You strike the {enemy['name']} for {damage} damage!")
        print(f"{enemy['name']} HP is now {max(enemy['hp'], 0)}.")
        return enemy["hp"] <= 0

def enemy_turn(player, enemy):
    """Handle the enemy's turn. Returns True if the player is defeated."""
    print_divider()
    print(f"{enemy['name']}'s turn!")
    damage = random.randint(1, enemy["attack"])
    player["hp"] -= damage
    print(f"The {enemy['name']} hits you for {damage} damage!")
    print(f"Your HP is now {max(player['hp'], 0)}.")
    return player["hp"] <= 0

def main():
    """Main game loop."""
    player = create_character()
    enemy = create_enemy()

    print_divider()
    print(f"{player['name']} the {player['role']} enters the tavern...")
    print(f"A wild {enemy['name']} appears!")
    print(f"YOUR STATS  | HP: {player['hp']}  ATTACK: {player['attack']}")
    print(f"ENEMY STATS | HP: {enemy['hp']}  ATTACK: {enemy['attack']}")

    # Simple battle loop
    while True:
        # Player turn
        enemy_defeated = player_turn(player, enemy)
        if enemy_defeated:
            print_divider()
            print(f"🎉 You defeated the {enemy['name']}! You win! 🎉")
            break

        # Enemy turn
        player_defeated = enemy_turn(player, enemy)
        if player_defeated:
            print_divider()
            print("💀 You have fallen in battle... Game over. 💀")
            break

    print_divider()
    print("Thanks for playing Bludgeons & Flagons!")

# This line actually starts the game when the file is run.
if __name__ == "__main__":
    main()

