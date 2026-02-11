# ----------------------- Imports -----------------------
from death_loop import death_loop
from defend import defend
from Character import hero, bandit, fire_bandit, electric_bandit, heavy_bandit, weak_bandit, mage, moon_mage, electric_mage, golem, sharp_golem, impenetrable_golem, ranged_golem, swift_golem
from health_bar import HealthBar
from weapon import short_bow, fire_breath, electric_staff, fists, iron_sword, short_bow, fire_spear, golden_sabre, infected_gun , weapons, mythical_scythe , weapon_cost
from shop import shop
import time
import os
import random
from death_loop import death_loop
enemies = [bandit, fire_bandit, electric_bandit, heavy_bandit, weak_bandit, mage, moon_mage, electric_mage, golem, sharp_golem, impenetrable_golem, ranged_golem, swift_golem]

enemies_name = [bandit.name, fire_bandit.name, electric_bandit.name, heavy_bandit.name, weak_bandit.name, mage.name, moon_mage.name, electric_mage.name, golem.name, sharp_golem.name, impenetrable_golem.name, ranged_golem.name, swift_golem.name]

# ----------------------- Reusable Functions -----------------------
def main_loop():


  # Asks user for an input and verifies it, then initiates a call to another function
  choice_2 = 0
  while True:
    print(f"{hero.name} is currently standing in the feild, what do you want to do? ")
    hero.health_bar.update()
    hero.health_bar.draw()
    print(f"Pick your action, {hero.name}.")
    print("1. to choose an enemy to attack.")
    print("2. to start an attack (Or Enter).")
    print("3. to shop ")
    try:
      choice_2 = int(input("Pick your option; "))
    except ValueError: 
      print("Not a valid option! ")
    print(choice_2)
    if choice_2 == 1: 
      os.system("clear")
      print("Which enemy do you want to attack?")
      for i in range(len(enemies)):
        print(enemies[i].name)
      print("Enter the name of the enemy you would next like to battle.")
      print("-----------------------------------------------------")
      try:
        enemy_choice = input("Enter Here; ")
        if enemy_choice in enemies_name:
          enemy_index = enemies_name.index(enemy_choice)
          hero.enemy = enemies[enemy_index-1]
          time.sleep(2)
          print(f"Your enemy is now {hero.enemy}")
          os.system("clear")
        else:
          print("Not a valid enemy!")
          time.sleep(2)
          os.system("clear")
      except ValueError or ZeroDivisionError:
        print("Not a valid enemy!")
        os.system("clear")

    if int(choice_2) == 2:
      print("Attacking....")
      time.sleep(1)
      attack_loop()
      os.system("clear")
      break

    if int(choice_2) == 3:
      print("Going to the shop")
      time.sleep(1)
      shop()
    else:
      os.system("clear")
      continue

  # Calls the attack function from Character, using the health_bar class draws and updates the bar to reflect health of both enemy and hero, attack starts on input from user 

def attack_loop():
  print(hero.enemy.name)
  if hero.enemy.health >= 0 and hero.enemy in enemies:
    os.system("clear")
    hero.attack(hero.enemy)
    hero.enemy.attack(hero)
    hero.health_bar.update()
    hero.enemy.health_bar.update()
    hero.health_bar.draw()
    hero.enemy.health_bar.draw()
    time.sleep(0.01)
    if hero.health == 0:
      death_loop()
    if hero.enemy.health <= 0:
      hero.money += random.randrange(3,6)
      print(f"You have {hero.money} coins!")
      print("\n")
      input("Enter to continue ")
      os.system("clear")
      enemy_index = enemies.index(hero.enemy)
      enemies.remove(hero.enemy)
      hero.enemy = enemies[enemy_index]
      print("You have moved on to the next enemy!")
      time.sleep(2)
      os.system("clear")
      main_loop()
  else:
    print("You can not attack No one, pick an enemy!")
    time.sleep(2)
    os.system("clear")

# Heals if the hero has money, if not goes back to loop it was called from
def heal():
  print("You have decided to heal, can you pay $5 to do so? ")
  time.sleep(.5)
  print(f"You have {hero.money} coins")
  time.sleep(1)
  if hero.money >= 1:
    hero.health += 15
    hero.money -= 1
    hero.health_bar.update()
    hero.health_bar.draw()
    time.sleep(1)
    os.system("clear")
    if hero.health >= hero.health_max:
      hero.health = hero.health_max
      print("You have healed to full health!")
      time.sleep(2)
      os.system("clear")
  else:
    print("Insufficient Funds")

fighting = True
def fighting_loop():
  while fighting is True:
    print("What would you like to do? ")
    print("\033[0m1.", "\033[31mAttack")
    print("\033[0m2.", "\033[36mDefend")
    print("\033[0m3.", "\033[35mHeal")
    try:
        action = int(input("\033[0mEnter here: "))
    except ValueError:
        print("Invalid action")
        time.sleep(.15)
        action = 0
        os.system("clear")
    print(action)
    try:
      if action == 1: 
        os.system("clear")
        print("Attacking...")
        time.sleep(.5)
        attack_loop()
      if action == 2:
        os.system("clear")
        time.sleep(.5)
        print("Defending....")
        defend()
      if action == 3:
        os.system("clear")
        time.sleep(.5)
        print("Healing...")
        heal()
      elif action != 1 or 2 or 3:
        time.sleep(1)
        os.system("clear")
    except ValueError or ZeroDivisionError:
        pass