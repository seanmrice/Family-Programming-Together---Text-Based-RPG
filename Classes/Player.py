class Player:
    def __init__(self, name, inventory=None):
        self.name = name
        self.health = 100
        if inventory is not None:
            self.inventory = inventory
        else:
            self.inventory = []
        self.location = {"x": 0, "y": 0}
        self.__alive = True
        self.__stamina = 100
        self.__mana = 100
        self.__lives = 3
        self.__sight_range = 2
        self.__in_darkness = False
        self.__attack_range = 1
        self.__base_attack = 10
        self.__equipped_weapon = None
        self.__last_move = None
    
    def heal(self, heal_amount) -> int:
        # if health is 100, player is at full health
        if self.health == 100:
            print("You are at full health.")
        elif self.health + heal_amount > 100:
            print(f"You heal by {100 - self.health}. You are at full health.")
            self.health = 100
        elif self.health + heal_amount <= 0 or self.health <= 0:
            print("You died.")
            self.health = 0
            self.__alive = False
        else:
            print(f"You heal by {heal_amount}. You have {self.health} health remaining.")
            self.health += heal_amount
    
    def get_current_position(self) -> tuple:
        return (self.location["x"], self.location["y"])
    
    def can_move(self):
        if self.__alive and self.__stamina > 0:
            return True
        if not self.__alive:
            print("You are dead.")
            return False
        if self.__stamina <= 0:
            print("You are out of stamina.  You must eat or rest first.")
            return False
    
    def move(self, direction: str) -> None:
        '''
        Moving costs stamina, for every 1 movement, we reduce 1 stamina
        '''
        direction = direction.lower()
        if direction == "north":
            self.location["y"] += 1
            self.__stamina -= 1
        elif direction == "south":
            self.location["y"] -= 1
            self.__stamina -= 1
        elif direction == "east":
            self.location["x"] += 1
            self.__stamina -= 1
        elif direction == "west":
            self.location["x"] -= 1
            self.__stamina -= 1
        else:
            print("Invalid direction.")

    def eat(self, food_name) -> None:
        # Check if any food items are in the player's inventory
        food = None
        for item in self.inventory:
            if item.name.lower() == food_name.lower():
                food = item
        # Check if the food is in the player's inventory
        if food in self.inventory:
            print(f"You have {self.health} health.")
            print(f"Eating the {food.name} will give you {food.stamina_worth()} health.")
            print(f"Are you sure you want to eat the {food.name}?")
            response = input("(Y)es or (N)o: ")
            if response.lower().startswith("y"):
                # Remove the food from the player's inventory
                self.inventory.remove(food)
                # Increase the player's health by the food's health value
                self.health += food.stamina_worth()
                print(f"You eat the {food.name}. You gain {food.stamina_worth()} health.")
                print(f"You now have {self.health} health.")
            else:
                print("You decide not to eat the food.")
        else:
            print("You do not have that item in your inventory.")