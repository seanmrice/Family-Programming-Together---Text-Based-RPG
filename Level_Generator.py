import json
import matplotlib.pyplot as plt
from Classes.Weapons.Sword import Sword

# Generate a json file with the level data
# The level data is a dictionary with the following keys:
# "level" : the level number
# "width" : the width of the level
# "height" : the height of the level
# "player" : the player's position
# "spiders" : a list of spider positions
# "cows" : a list of cow positions
# "key" : the key position
# "exit" : the exit position

# Example Level 1:
Level_1 = {
    "level": 1,
    "width": 10,
    "height": 10,
    "player": [0, 0],
    "spiders": [
        [1, 4], 
        [2, 0], 
        [3, 3],
        [4, 9],
        [8, 8],
        [7, 2]
        ],
    "cows": [
        [1, 0],
        [5, 8],
        [5, 2],
        [3, 7],
        [8, 6]
        ],
    "key": [1, 8],
    "exit": [9, 9],
    "player_inventory": ["torch", {'weapon_type': 'sword', 'class': 'Sword', 'name': 'Standard', 'damage': 20, 'enchantment': None}]
}

# Save the level data to a JSON file
with open('level1.json', 'w') as json_file:
    json.dump(Level_1, json_file, indent=4)
player_inventory = Level_1["player_inventory"]
print(player_inventory)
# Function to plot the level
def plot_level(level_data):
    width = level_data["width"]
    height = level_data["height"]
    
    fig, ax = plt.subplots()
    ax.set_xlim(-0.5, width-0.5)
    ax.set_ylim(-0.5, height-0.5)
    ax.set_xticks(range(width))
    ax.set_yticks(range(height))
    ax.grid(True)

    # Track added labels
    labels_added = set()

    # Define marker size
    marker_size = 10

    # Plot the player
    player_pos = level_data["player"]
    ax.plot(player_pos[0], player_pos[1], 'bo', markersize=marker_size, label='Player')
    labels_added.add('Player')

    # Plot the spiders
    for spider in level_data["spiders"]:
        if 'Spider' not in labels_added:
            ax.plot(spider[0], spider[1], 'ro', markersize=marker_size, label='Spider')
            labels_added.add('Spider')
        else:
            ax.plot(spider[0], spider[1], 'ro', markersize=marker_size)

    # Plot the cows
    for cow in level_data["cows"]:
        if 'Cow' not in labels_added:
            ax.plot(cow[0], cow[1], 'go', markersize=marker_size, label='Cow')
            labels_added.add('Cow')
        else:
            ax.plot(cow[0], cow[1], 'go', markersize=marker_size)

    # Plot the key
    key_pos = level_data["key"]
    if 'Key' not in labels_added:
        ax.plot(key_pos[0], key_pos[1], 'yo', markersize=marker_size, label='Key')
        labels_added.add('Key')
    else:
        ax.plot(key_pos[0], key_pos[1], 'yo', markersize=marker_size)

    # Plot the exit
    exit_pos = level_data["exit"]
    if 'Exit' not in labels_added:
        ax.plot(exit_pos[0], exit_pos[1], 'mo', markersize=marker_size, label='Exit')
        labels_added.add('Exit')
    else:
        ax.plot(exit_pos[0], exit_pos[1], 'mo', markersize=marker_size)

    ax.legend()
    # X axis should be called "X"
    plt.xlabel("X")
    # Y label should be vertical, not horizontal and offset to the left by 0.1
    plt.ylabel("Y", rotation=0, labelpad=10)

    plt.title(f'Level {level_data["level"]}')
    plt.savefig(f'level_{level_data["level"]}.png')

# Plot the example level
plot_level(Level_1)
sword = Sword("Standard", 20)
print(sword.dict_to_json())