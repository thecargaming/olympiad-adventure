# ------------ class setup ------------
import random
class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: float, sprite
                 
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.sprite = sprite
        


# ------------ object creation ------------
# Gives each weapon a name type and damage value to use in battle
iron_sword = Weapon(name="Iron Sword",
                    weapon_type="sharp",
                    damage=11, sprite = "Frames/Iron Sword.png"
                    )

short_bow = Weapon(name="Short Bow",
                   weapon_type="ranged",
                   damage=10,sprite = "Frames/Short Bow.png"
                   )

fire_breath = Weapon(name = "Fire Breath"                                     
                      , weapon_type = "fire"                                  
                      , damage = 10 , sprite = "Frames/Fire Breath.png"                                         
                      )

golden_sabre =  Weapon(name = "Golden Sabre"                             
                    , weapon_type = "fists"                                  
                    , damage = 15, sprite = "Frames/Golden Sabre.png"                                          
                    )
mythical_scythe =  Weapon(name = "Mythical Scythe"                         
                    , weapon_type = "sharp"                                  
                    , damage = 8, sprite = "Frames/Mythical Scythe.png"                                          
                    )
fire_spear = Weapon(name = "Fire Spear"                         
                    , weapon_type = "sharp"                                  
                    , damage = 9, sprite = "Frames/Fire Spear.png"                                          
                    )

elven_hammer = Weapon(name = "Elven Hammer", weapon_type = "sharp", damage = 8, sprite = "Frames/Elven Hammer.png")

aetherium_rapier = Weapon(name = "Aetherium Rapier", weapon_type = "sharp", damage = 7, sprite = "Frames/Aetherium Rapier.png")

elden_crossbow = Weapon(name = "Elden Crossbow", weapon_type = "ranged", damage = 8, sprite = "Frames/Elden Crossbow.png")

spirit_dagger = Weapon(name = "Spirit Dagger", weapon_type = "sharp", damage = 8, sprite = "Frames/Spirit Dagger.png")

plasma_staff = Weapon(name = "Plasma Staff", weapon_type = "sharp", damage = 7.5, sprite = "Frames/Plasma Staff.png")

lunar_sceptre = Weapon(name = "Lunar Sceptre", weapon_type = "sharp", damage = 11, sprite = "Frames/Lunar Sceptre.png")



infected_gun = Weapon(name = "Infected Gun"                         
                    , weapon_type = "long range"                                  
                    , damage = random.randrange(18, 23) , sprite = "Frames/Infected_Gun.png"                                         
                    )




electric_staff = Weapon(name = "Electric Staff", weapon_type= "Electric", damage = 7, sprite = "Frames/Electric Staff.png")

fists = Weapon(name="Fists",
               weapon_type="blunt",
               damage=2,
                sprite = "Frames/Fists.png")
weapons = [short_bow, fire_spear ,golden_sabre, infected_gun, mythical_scythe]
weapon_cost = [20, 40, 60, 80, 100]