class Food:
    def __init__(self, name, price=1, weight=1, calories=100):
        self.name = name
        self.price = price
        self.weight = weight
        self.calories = calories

    def stamina_worth(self):
        return self.calories // 2
    
    def __str__(self):
        return f"{self.name}, worth {self.calories // 2} stamina."

    def __repr__(self):
        return f"{self.name} - {self.price} - {self.weight} - {self.calories}"