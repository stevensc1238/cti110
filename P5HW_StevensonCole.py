#StevensonCole
#5/2/2025
#P5HW
#create a Python program that simulates a simple character creation game

import random

def get_limited_input(prompt, min_val=1, max_val=50):
    """
    Prompts the user for an integer input within a specified range.
    
    Parameters:
        prompt (str): The message to display to the user.
        min_val (int): The minimum valid value (default 1).
        max_val (int): The maximum valid value (default 50).
        
    Returns:
        int: A valid input number within the range.
    """
    value = None
    attempts = 0
    while value is None and attempts < 5:
        try:
            val = int(input(f"{prompt} ({min_val}-{max_val}): "))  # Get input from the user
            if min_val <= val <= max_val:  # Check if input is within valid range
                value = val
            else:
                print(f"Value must be between {min_val} and {max_val}.")  # Inform the user if input is out of range
        except ValueError:  # Handle case when the user enters non-integer input
            print("Please enter a valid number.")
        attempts += 1
    return value if value is not None else min_val  # Fallback to minimum value if user fails to provide valid input

def create_warlord(index):
    """
    Prompts the user to input attributes for creating a warlord.
    
    Parameters:
        index (int): The index of the warlord being created (for naming purposes).
    
    Returns:
        dict: A dictionary representing the created warlord.
    """
    print(f"\nCreating warlord #{index + 1}")
    name = input("Enter the warlord's name: ")
    # Get warlord attributes with validation for each
    power = get_limited_input(f"Enter {name}'s power")
    speed = get_limited_input(f"Enter {name}'s speed")
    size = get_limited_input(f"Enter {name}'s force size")
    return {'name': name, 'power': power, 'speed': speed, 'size': size, 'health': 100, 'level': 1}

def create_military(index):
    """
    Creates a random military unit with randomized attributes.
    
    Parameters:
        index (int): The index of the military unit being created.
    
    Returns:
        dict: A dictionary representing the created military unit.
    """
    return {
        'name': f"MILITARY FORCES #{index + 1}",
        'power': random.randint(1, 50),
        'speed': random.randint(1, 50),
        'size': random.randint(50, 150),
        'health': 100
    }

def display_warlords(warlords):
    """
    Displays the attributes of all the warlords.
    
    Parameters:
        warlords (list): List of warlord dictionaries.
    """
    print("\n\U0001F33B WARLORDS \U0001F33B")
    for i, war in enumerate(warlords):
        print(f"[{i}] {war['name']} - Power: {war['power']}, Speed: {war['speed']}, Size: {war['size']}, Health: {war['health']}, Level: {war['level']}")

def display_militaries(militaries):
    """
    Displays the attributes of all the military units that are still alive.
    
    Parameters:
        militaries (list): List of military unit dictionaries.
    """
    print("\n\U0001F6E1 MILITARY UNITS \U0001F6E1")
    # Filter out defeated militaries (size <= 0) from the list
    alive_militaries = [military for military in militaries if military['size'] > 0]
    
    if not alive_militaries:
        print("All military units have been defeated.")
        return
    
    for i, mil in enumerate(alive_militaries):
        print(f"[{i}] {mil['name']} - Power: {mil['power']}, Speed: {mil['speed']}, Size: {mil['size']}, Health: {mil['health']}")

def ambush(warlord, military):
    """
    Simulates an ambush where the warlord reduces the size of the military unit.
    
    Parameters:
        warlord (dict): The attacking warlord.
        military (dict): The defending military unit.
    
    Returns:
        int: The new size of the military unit after the ambush.
    """
    casualties = random.randint(0, warlord['power'])
    military['size'] -= casualties  # Reduce the size of the military unit
    print(f"\n{warlord['name']} ambushes {military['name']}! {military['name']} loses {casualties} troops.")
    return military['size']

def counter_attack(military, warlord):
    """
    Simulates a counter-attack by the military unit on the warlord.
    
    Parameters:
        military (dict): The defending military unit.
        warlord (dict): The attacking warlord.
    
    Returns:
        int: The warlord's updated health after the counter-attack.
    """
    if military['size'] > 0:
        retaliation = random.randint(0, military['power'])
        warlord['health'] -= retaliation  # Deduct health from the warlord
        print(f"{military['name']} counter-attacks! {warlord['name']} takes {retaliation} damage.")
    else:
        print(f"{military['name']} is too weak to counter-attack.")
    return warlord['health']

def follow_up_attacks(warlord, military):
    """
    Simulates follow-up attacks between the warlord and military.
    
    Parameters:
        warlord (dict): The attacking warlord.
        military (dict): The defending military unit.
    
    Returns:
        dict: A dictionary containing the updated health of the warlord and the size of the military unit.
    """
    rounds = max(warlord['speed'], military['speed'])  # Number of follow-up attacks based on speed
    print(f"{warlord['name']} and {military['name']} engage in {rounds} follow-up attacks!")
    attacker_turn = 'warlord' if warlord['speed'] >= military['speed'] else 'military'

    for i in range(rounds):
        if attacker_turn == 'warlord' and warlord['health'] > 0:
            damage = random.randint(0, warlord['power'])
            military['size'] -= damage  # Military loses troops based on warlord's power
            print(f"Turn {i+1}: {warlord['name']} attacks! {military['name']} loses {damage} troops.")
            attacker_turn = 'military'
        elif attacker_turn == 'military' and military['size'] > 0:
            retaliation = random.randint(0, military['power'])
            warlord['health'] -= retaliation  # Warlord takes damage from military retaliation
            print(f"Turn {i+1}: {military['name']} attacks! {warlord['name']} takes {retaliation} damage.")
            attacker_turn = 'warlord'
        else:
            print(f"Turn {i+1}: One side is too weak to continue.")
            break

    return {'warlord_health': warlord['health'], 'military_size': military['size']}

def level_up_warlord(warlord):
    """
    Levels up the warlord, increasing one of their attributes (power, speed, or size).
    
    Parameters:
        warlord (dict): The warlord who will level up.
    """
    stat = random.choice(['power', 'speed', 'size'])
    increase = random.randint(1, 5)  # Level up attribute by 1 to 5 points
    warlord[stat] += increase
    warlord['level'] += 1  # Increase warlord's level
    print(f"\n🏅 {warlord['name']} levels up! {stat.capitalize()} increased by {increase}. New Level: {warlord['level']}")

def battle(warlords, militaries):
    """
    Runs the battle sequence between warlords and military units.
    
    Parameters:
        warlords (list): List of warlord dictionaries.
        militaries (list): List of military unit dictionaries.
    
    Returns:
        str: The status of the battle.
    """
    max_rounds = random.randint(1, 3)  # Randomize the number of rounds in the battle
    for round_count in range(max_rounds):
        alive_militaries = [m for m in militaries if m['size'] > 0]
        if not alive_militaries:
            print("\n🚨 All military units have been defeated.")
            return 'militaries_defeated'

        print(f"\n⚔️ --- Round {round_count + 1} of {max_rounds} --- ⚔️")
        display_warlords(warlords)
        display_militaries(militaries)

        valid_input = False
        while not valid_input:
            try:
                attacker_index = int(input("\nChoose a warlord to attack with (index): "))
                attacker = warlords[attacker_index]
                # Filter defeated militaries and only show those that are still alive
                alive_militaries = [m for m in militaries if m['size'] > 0]
                if not alive_militaries:
                    print("No valid military units to attack.")
                    break
                target_index = int(input("Choose a military unit to attack (index): "))
                target = alive_militaries[target_index]

                target['size'] = ambush(attacker, target)
                attacker['health'] = counter_attack(target, attacker)
                results = follow_up_attacks(attacker, target)

                attacker['health'] = results['warlord_health']
                target['size'] = results['military_size']

                if attacker['health'] <= 0:
                    print(f"\n💀 {attacker['name']} has been defeated!")
                    valid_input = True

                if target['size'] <= 0:
                    print(f"\n🎉 {target['name']} has been defeated!")
                    level_up_warlord(attacker)
                    valid_input = True

            except (IndexError, ValueError):
                print("Invalid choice. Please try again.")

    return 'battle_complete'

def main():
    print("\n🎮 Welcome to Warlord Battle Simulator ⚔️")
    playing = True
    warlords = []
    militaries = []

    # Initial setup
    num_warlords = int(input("\nHow many warlords would you like to create? "))
    warlords = [create_warlord(i) for i in range(num_warlords)]
    num_militaries = int(input("\nHow many military units would you like to create? "))
    militaries = [create_military(i) for i in range(num_militaries)]

    while playing:
        battle_status = battle(warlords, militaries)

        print("\n📈 Updated Warlord Stats:")
        display_warlords(warlords)

        if battle_status == 'militaries_defeated':
            print("\n🏆 Victory! All enemy military units have been defeated.")
            for warlord in warlords:
                warlord['health'] = 100
                print(f"{warlord['name']}'s health reset to 100 after victory.")

            victory_menu_active = True
            while victory_menu_active:
                choice = input("\nDo you want to quit or continue? (quit/continue): ").strip().lower()
                if choice == "quit":
                    print("\nThanks for playing!")
                    playing = False
                    victory_menu_active = False
                elif choice == "continue":
                    reuse = input("Do you want to reuse your current warlord(s)? (yes/no): ").strip().lower()
                    if reuse == "no":
                        num_warlords = int(input("\nHow many warlords would you like to create? "))
                        warlords = [create_warlord(i) for i in range(num_warlords)]
                    num_militaries = int(input("\nHow many new military units would you like to create? "))
                    militaries = [create_military(i) for i in range(num_militaries)]
                    victory_menu_active = False
                else:
                    print("Invalid input. Please type 'quit' or 'continue'.")

        elif any(w['health'] <= 0 for w in warlords):
            print("\n💀 One or more warlords have been defeated.")
            response = input("Do you want to continue with current warlord(s), create new one(s), or quit? (c/n/q): ").lower()
            while response not in ('c', 'n', 'q'):
                response = input("Please enter 'c' to continue, 'n' for new warlords, or 'q' to quit: ").lower()

            if response == 'c':
                for warlord in warlords:
                    if warlord['health'] <= 0:
                        warlord['health'] = 100
                        print(f"{warlord['name']}'s health reset to 100.")
            elif response == 'n':
                num_warlords = int(input("\nHow many warlords would you like to create? "))
                warlords = [create_warlord(i) for i in range(num_warlords)]
            elif response == 'q':
                print("\nThanks for playing!")
                break

        else:
            again = input("\nWould you like to continue battling? (y/n): ").lower()
            while again not in ('y', 'n'):
                again = input("Please enter 'y' or 'n': ").lower()
            if again != 'y':
                print("\nThanks for playing!")
                break

if __name__ == "__main__":
    main()
