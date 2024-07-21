from Classes.Items.Food import Food
class Cow:
    def __init__(self):
        self.health = 100
        self.position = None
        self.__sight_range = 3
        self.__last_move = None
        self.__is_alive = True
    
    def can_see_target(self, target: object) -> bool:
        target_x, target_y = self.get_target_postion(target)
        current_x, current_y = self.get_current_position()
        
        if abs(target_x - current_x) <= self.__sight_range and abs(target_y - current_y) <= self.__sight_range:
            return True
        return False
            
    def take_damage(self, damage: int) -> None:
        self.health -= damage
        if self.health <= 0:
            self.__is_alive = False
            print("Cow has died.")
            return self.drop_food()
            
    def drop_food(self) -> object:
        if self.__is_alive == False:
            return Food("Beef", 2, 1, 50)