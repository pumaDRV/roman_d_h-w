class Character:
    def __init__(self, name: str, hp: int):
        self.name = name
        self.hp = hp
    
    def status(self):
        return f"{self.name}: {self.hp} HP" 
    
    def is_alive(self):
        return self.hp > 0


class Wizard(Character):
    def __init__(self, name: str, hp: int, mana: int):
        super().__init__(name, hp)
        self.mana = mana
    
    def cast_spell(self, cost: int):
        if self.mana >= cost:
            self.mana -= cost
            return f"{self.status()}, осталось маны: {self.mana}"
        else:
            return "Недостаточно маны"


wizard = Wizard("Гендальф", 100, 50)
print(wizard.status())    
print(wizard.cast_spell(30))  
print(wizard.cast_spell(30))  
