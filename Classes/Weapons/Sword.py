class Sword:
    def __init__(self, name="standard", damage=20):
        self.name = name
        self.weapon_type = 'sword'
        self.damage = damage
        self.enchantment = None

    def enchant(self, enchantment):
        self.enchantment = enchantment
        print(f'{self.name} has been enchanted with {self.enchantment}!')
        
    def attack(self):
        print(f'Attacking with {self.name} for {self.damage} damage')
    
    def __load__(self, data):
        self.name = data['name']
        self.damage = data['damage']
        self.enchantment = data['enchantment']
        
    def __str__(self):
        return f'{self.name} sword with {self.damage} damage'
    
    def __dict__(self):
        return {'weapon_type': self.weapon_type,
                'class': self.__class__.__name__,
                'name': self.name,
                'damage': self.damage,
                'enchantment': self.enchantment}