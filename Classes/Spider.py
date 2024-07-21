class Spider:
    def __init__(self):
        self.health = 100
        self.position = None
        self.attackable_mobs = ["Player", "Cow"]
        self.__sight_range = 2
        self.__last_move = None
    
    def can_attack(self, target: object) -> bool:
        if target.__class__.__name__ in self.attackable_mobs:
            return True
        return False
    
    def can_see_target(self, target: object) -> bool:
        target_x, target_y = self.get_target_postion(target)
        current_x, current_y = self.get_current_position()
        
        if abs(target_x - current_x) <= self.__sight_range and abs(target_y - current_y) <= self.__sight_range:
            return True
        return False
    
    def attack(self, target: object) -> None:
        target.health -= 10
        print(f"Spider attacks {target} for 10 damage. {target} has {target.health} health remaining.")
    
    def move(self, direction: str) -> None:
        direction = direction.lower()
        if direction == "north":
            self.position["y"] += 1
        elif direction == "south":
            self.position["y"] -= 1
        elif direction == "east":
            self.position["x"] += 1
        elif direction == "west":
            self.position["x"] -= 1
        else:
            print("Invalid direction.")
    
    def get_current_position(self) -> tuple:
        return (self.position["x"], self.position["y"])
    
    def get_target_postion(self, target: object) -> tuple:
        return (target.position["x"], target.position["y"])
    
    def move_towards_target(self, target: object):
        target_x, target_y = self.get_target_postion(target)
        current_x, current_y = self.get_current_position()
        
        if target_x > current_x:
            self.move("east")
        elif target_x < current_x:
            self.move("west")
        elif target_y > current_y:
            self.move("north")
        elif target_y < current_y:
            self.move("south")
        else:
            print("Spider is at target.")