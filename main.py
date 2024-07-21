from Level_Functions import load_level, instantiate_player
from Classes.Cow import Cow
debug = False
player_name = ""
current_move = 0

# Game Name:
# Principle Programmer:       Sean Rice
# Creative Director:          Carolyn Rice
# Moral Support/Cheerleader:  Alyssa Rice

# Clear the screen
print("\033[H\033[J")

# Game Description: (This is a text-based game, with Carolyn Rice as the creative director)
# Here is her current vision for the game:
# Commands should be "go [direction]" or "quit"
# Spiders attack the player when they get too close
# there are 2 types of mobs currently spiders and cows
# the player has a sword to kill the spiders the sword is also to kill cows for food player 
# needs to get to the end by killing spiders that get in the players way
# A key is needed to unlock the door to the next room
# The player has 3 lives
# Spiders and cows should be able to move:
# - Cows randomly and spiders towards the player if they are within a certain range

if not player_name:
    player_name = input("Please enter your name adventurer: ")

print("Which level would you like to play?")
print("1. Level 1")

level = input("Enter the level number: ")

if level == "1":
    level_data = load_level(1)
    if debug:
        print(level_data)
    player = instantiate_player(level_data=level_data, player_name=player_name)
    print(player.name, ", you are at the start of the level.")
    print("You have the following items in your inventory:")
    for item in player.inventory:
        print("    -", item)
        
    print("You have the following stats:")
    print("    - Health:", player.health)
    print("    - Stamina:", player._Player__stamina)
    print("    - Mana:", player._Player__mana)
    print("    - Lives:", player._Player__lives)
    print("    - Sight Range:", player._Player__sight_range)
    print("    - Darkness:", player._Player__in_darkness)
    print("    - Attack Range:", player._Player__attack_range)
    print("    - Base Attack:", player._Player__base_attack)
    print("    - Equipped Weapon:", player._Player__equipped_weapon)
    
    # Spawn a cow
    cow = Cow()
    print("A cow has appeared.")
    cow.take_damage(100)
    player.inventory.append(cow.drop_food())
    
    print("You have the following items in your inventory:")
    for item in player.inventory:
        print("    -", item)
        
    player.eat("Beef")