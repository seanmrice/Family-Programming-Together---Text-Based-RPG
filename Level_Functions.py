import json
from Classes.Player import Player
from Classes.Weapons.Sword import Sword

def load_level(level_number: int):
    level_folder = "Levels"
    with open(f'{level_folder}/level{level_number}.json', 'r') as json_file:
        level_data = json.load(json_file)
    return level_data

def instantiate_player(level_data, player_name):
    if level_data["player_inventory"]:
        # Each item in their inventory is a dictionary, so we need to convert it to a Sword object
        for i, item in enumerate(level_data["player_inventory"]):
            if item['class'] == 'Sword':
                level_data["player_inventory"][i] = Sword(name=item['name'], damage=item['damage'])
                                                          
    player = Player(name=player_name, inventory=level_data["player_inventory"])
    return player