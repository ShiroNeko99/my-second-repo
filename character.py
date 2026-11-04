import random

class Character:
    def __init__(self, name, hp, attack_power):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        
    def attack(self, other):
        damage_pencentage = random.uniform(0.3, 0.9)
        actual_damage = int(self.attack_power * damage_pencentage)
        other.hp -= actual_damage
        print(f"{self.name} attacks {other.name} for {actual_damage} damage!")

    def is_alive(self):
        return self.hp > 0

    def __str__(self):
        return f"{self.name}: {self.hp} HP"
