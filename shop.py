# ---------------------- Imports -------------------------
import os
import time
from Character import *
from weapon import short_bow, fire_breath, electric_staff, fists, iron_sword, fire_spear, golden_sabre, infected_gun , weapons, mythical_scythe , weapon_cost
from Character import hero

# Function calls the hero and its money attribute, using it it can call the equip function the hero has to give them the weapon if they can buy it

# Main logix verifies if the hero has enough money to buy the weapon, if they can, it will call the equip function to give the person the weapon, if not it will go back to the loop
def shop():
  print("Welcome to the shop!")
  print("Here are the items for sale:")
  for i in range(len(weapons)):
    print("\n")
    print(weapons[i].name,"; costing", weapon_cost[i], "coins. [", i+1,"]")
  print("\n")
  print("Enter the number of the item you would like to buy, or enter 0 to exit.")
  print("-----------------------------------------------------")
  print(hero.name, "has", hero.money, "coins.")
  try:
    choice = int(input("Enter Here; "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    choice = int(input("Enter Here; "))
  print("\n")
  os.system("clear")

  if choice == 1 and hero.money >= 20:
    hero.equip(short_bow)
    weapons.remove(short_bow)
    weapon_cost.remove(20)
    
    print("You have equipped the", short_bow.name)
    hero.money -= 20
    print("You have", hero.money, "coins left.")
    time.sleep(2)
    os.system("clear")
    
  elif choice == 2 and hero.money >= 40: 
    hero.equip(fire_spear)
    weapons.remove(fire_spear)
    weapon_cost.remove(40)

    print("You have equipped the", fire_spear.name)
    hero.money -= 40
    print("You have", hero.money, "coins left.")
    time.sleep(1)
    os.system("clear")
      

  elif choice == 3 and hero.money >= 60:
    hero.equip(golden_sabre)
    weapons.remove(golden_sabre)
    weapon_cost.remove(60)
    
    print("You have equipped the", golden_sabre.name)
    hero.money -= 60
    print("You have", hero.money, "coins left.")
    time.sleep(1)
    os.system("clear")
      

  elif choice == 4 and hero.money >= 80:
    hero.equip(infected_gun)
    weapons.remove(infected_gun)
    weapon_cost.remove(80)
    
    print("You have equipped the", infected_gun.name)
    hero.money -= 80
    print("You have", hero.money, "coins left.")
    time.sleep(1)
    os.system("clear")
    
  elif choice == 5 and hero.money >= 100:
    hero.equip(mythical_scythe)
    weapons.remove(mythical_scythe)
    weapon_cost.remove(100)
    
    print("You have equipped the", mythical_scythe.name)
    hero.money -= 100
    print("You have", hero.money, "coins left.")
    time.sleep(1)
    os.system("clear")
  else:
    time.sleep(.2)
    print("Invalid choice or Insufficient Coins")
    os.system("clear")

  
  
    
    