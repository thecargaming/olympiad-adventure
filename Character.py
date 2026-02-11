# ------------ imports ------------
from weapon import fists, iron_sword, short_bow, fire_breath, electric_staff, fire_spear, elven_hammer, aetherium_rapier, elden_crossbow, spirit_dagger, plasma_staff, lunar_sceptre
import pygame
pygame.init()


# ------------ parent class setup ------------
# Base class for all characters, it sets up the base stats for the characters, and the health bar for the character
class Character:
    def __init__(self,
                 name: str,
                 health: int, sprite
                 ) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.sprite = sprite
        self.weapon = fists

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)


        


        


# ------------ subclass setup ------------
# Gives hero special weapon pick up and drop functions
class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int, money: int, enemy, weapon, sprite
                 ) -> None:
        super().__init__(name=name, health=health, sprite=sprite)
        self.money = money
        self.default_weapon = self.weapon
        self.enemy = enemy
        self.weapon = weapon
        self.sprite = sprite

    def equip(self, weapon) -> None:
        self.weapon = weapon


    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon
    

# ------------ subclass setup ------------
# Gives subclasses for the enemies
class Bandit(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon, type: str, sprite):
        super().__init__(name=name, health=health, sprite=sprite)
        
        self.weapon = weapon
        self.sprite = sprite    

    


class Mage(Character):
    def __init__(self,
         name: str,
         health: int,
         weapon, type: str, sprite
         ) -> None:
        super().__init__(name=name, health=health, sprite=sprite)
        self.weapon = weapon
        self.sprite = sprite

        
class Golem(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 weapon, type: str, sprite
                 ) -> None:
        super().__init__(name=name, health=health, sprite=sprite)
        self.weapon = weapon
        self.sprite = sprite

class Merchant(Character):
    def __init__(self,
         name: str,
         health: int,
         weapon, sprite
         ) -> None:
        super().__init__(name=name, health=health, sprite=sprite)
        self.weapon = weapon
        self.sprite = sprite



# Initiates Character objects in a class besides main to avoid circular call

bandit = Bandit(name="Bandit", health=100, weapon=fists, type = "Weak", sprite = ("Frames/Bandit.png"))

fire_bandit = Bandit(name = "Fire Bandit", health = 110, weapon = fire_spear, type = "Weak", sprite = ("Frames/Bandit.png"))

electric_bandit = Bandit(name = "Electric Bandit", health = 120, weapon = electric_staff, type = "Weak", sprite = ("Frames/Bandit.png"))

heavy_bandit = Bandit(name = "Heavy Bandit", health = 130, weapon = iron_sword, type = "Weak", sprite = ("Frames/Bandit.png"))

weak_bandit = Bandit(name = "Weak Bandit", health = 90, weapon = short_bow, type = "Weak", sprite = ("Frames/Bandit.png"))


golem = Golem(name="Golem", health=200, weapon=fire_breath, type = "Mid", sprite = ("Frames/Golem.png"))

sharp_golem = Golem(name = "Sharp Golem", health = 210, weapon = spirit_dagger, type = "Mid", sprite = ("Frames/Golem.png"))

impenetrable_golem = Golem(name = "Impenetrable Golem", health = 220, weapon = elven_hammer, type = "Mid", sprite = ("Frames/Golem.png"))

swift_golem = Golem(name = "Swift Golem", health = 195, weapon = aetherium_rapier, type = "Mid", sprite = ("Frames/Golem.png"))

ranged_golem = Golem(name = "Ranged Golem", health = 215, weapon = elden_crossbow, type = "Mid", sprite = ("Frames/Golem.png"))


mage = Mage(name = "Mage", health = 150, weapon=plasma_staff, type = "Mid-High", sprite =  ("Frames/Mage.png"))

moon_mage = Mage(name = "Moon Mage", health = 120, weapon = lunar_sceptre, type = "Mid-High", sprite =  ("Frames/Mage.png"))

electric_mage = Mage(name = "Electric Mage", health = 140, weapon = electric_staff, type = "Mid-High", sprite = ("Frames/Mage.png"))


merchant = Merchant(name = "Merchant", health = 100, weapon = iron_sword, sprite =  ("Frames/Merchant.png"))


hero = Hero(name="Player", health=120, money = 20, enemy = bandit, weapon = iron_sword, sprite =  ("hero.png"))

# ------------ functions ------------

