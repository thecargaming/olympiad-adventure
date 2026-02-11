# ------------ imports ------------
from screen2 import screen
from Character import hero, bandit, mage, fire_bandit, electric_bandit, heavy_bandit, weak_bandit, mage, moon_mage, electric_mage, golem, sharp_golem, impenetrable_golem, ranged_golem, swift_golem
import time
import os
import pygame
import random
from weapon import short_bow, fire_spear, golden_sabre, infected_gun , mythical_scythe
enemies = [bandit, fire_bandit, electric_bandit, heavy_bandit, weak_bandit, mage, moon_mage, electric_mage, golem, sharp_golem, impenetrable_golem, ranged_golem, swift_golem]

enemies_name = [bandit.name, fire_bandit.name, electric_bandit.name, heavy_bandit.name, weak_bandit.name, mage.name, moon_mage.name, electric_mage.name, golem.name, sharp_golem.name, impenetrable_golem.name, ranged_golem.name, swift_golem.name]
global healing_potion
healing_potion = 0
pygame.init()
pygame.time.Clock()
fonts = pygame.font.get_fonts()
print(fonts)
# ------------ Varaible -------------




# ------------ main loop ------------
os.system("clear")

hero.name = "Bob"
clock = pygame.time.Clock()

# Font for displaying the timer
fonts = pygame.font.SysFont("Times New Roman", 10)

# Timer variables
start_ticks = pygame.time.get_ticks()

# ------------ setup ------------


# ------------ game loop ------------
# Game Story
hero.enemy = bandit
os.system("clear")

start_screen = pygame.image.load("Frames/Start Screen.png")
end_screen = pygame.image.load("Frames/End Screen.png")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
font = pygame.font.Font(None, 36)
stored_final = 0


swift = pygame.transform.scale(pygame.image.load("Frames/Swift.png"), (50,50))
hero_weapon = pygame.transform.scale(pygame.image.load(hero.weapon.sprite),
                                     (50, 50))
hero_sprite = pygame.transform.scale(pygame.image.load("hero.png"), (75, 75))
rect = hero_sprite.get_rect() 

enemy_sprite = pygame.transform.scale(pygame.image.load(hero.enemy.sprite),
                                      (50, 50))
enemy_rect = enemy_sprite.get_rect()
enemy_weapon = pygame.transform.scale(
    pygame.image.load(hero.enemy.weapon.sprite), (50, 50))
VEL = 25

shop_sprite = pygame.transform.scale(pygame.image.load(hero.enemy.sprite),
  (50, 50))
shop_rect = shop_sprite.get_rect()

test = "Frames/background.png"


backgorund_boundary = pygame.transform.scale( pygame.image.load(test), (500, 6000)).convert()
background_rect, background_width = backgorund_boundary.get_size()

symbol_remaining = []
rounded_symbol_remaining = symbol_remaining * (hero.health // hero.health_max)

myFont = pygame.font.SysFont("Arial", 12)
font = pygame.font.SysFont("Arial", 10)
bigger_font = pygame.font.SysFont("dejavusansmono", 24)

grass = pygame.transform.scale(
    pygame.image.load("Frames/background.png"), (500, 6000))
grass_rect = grass.get_rect()

counter = 0
healing_potion = 0
speed_potion = 0
all_enemies_defeated = False

button_rect = pygame.Rect(350, 250, 100, 50)
popup_rect = pygame.Rect(300, 200, 200, 150)
popup_inner_rect = pygame.Rect(310, 210, 180, 130)
button1_rect = pygame.Rect(320, 230, 160, 30)
button2_rect = pygame.Rect(320, 270, 160, 30)
button1_text = font.render("Buy Heal+", True, BLACK)
button2_text = font.render("Buy Speed+", True, BLACK)


popup_active = False
run = False

if counter == 0:
    enemy_rect.center = (random.randrange(50,500), random.randrange(450,675))
    counter = 1

def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def healing():
    global healing_potion
    if hero.money - 1 > 0:
        healing_potion += 1
        hero.money -= 1



def speed():
    global speed_potion
    if hero.money - 5 > 0:
        speed_potion += 1
        hero.money -= 5

def main_menu():
    global run
    event_looper = True
    while event_looper == True:
        screen.blit(start_screen, (0, 0))


        draw_text("Olympiad Adventure!", bigger_font, WHITE, 150, 50)

        play_button_rect = pygame.Rect(200, 150, 160, 50)
        play_button_text = bigger_font.render("Play", True, BLACK)

        controls_rect = pygame.Rect(200,225,160,50)    
        controls_text = bigger_font.render("Controls", True, BLACK)


        pygame.draw.rect(screen, WHITE, play_button_rect)
        pygame.draw.rect(screen, WHITE, controls_rect)


        screen.blit(play_button_text, (play_button_rect.x + 10, play_button_rect.y + 5))
        screen.blit(controls_text, (controls_rect.x + 10, controls_rect.y + 5))


        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):  
                    run = True
                    event_looper = False
                elif controls_rect.collidepoint(event.pos):
                    controls()
                    event_looper = False

def controls():
    control_on = True
    while control_on:
        screen.fill((0,0,0))
        draw_text("Controls", bigger_font, WHITE, 150, 50)
        draw_text("Arrow Keys to move", font, WHITE, 150, 150)
        draw_text("Space to attack", font, WHITE, 150, 200)
        draw_text("E to heal", font, WHITE, 150, 250)
        draw_text("R to open shop", font, WHITE, 150, 300)
        draw_text("Q to quit", font, WHITE, 150, 350)

        back_button = pygame.Rect(200,380,160,50)    
        back_button_text = bigger_font.render("Back", True, BLACK)

        pygame.draw.rect(screen, WHITE, back_button)
        screen.blit(back_button_text, (back_button.x + 10, back_button.y + 5))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    control_on = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.collidepoint(event.pos):
                    control_on = False
                    main_menu()

def end_game():
    global stored_final
    global run
    end = True

    while end:
        screen.blit(end_screen, (0,0))

        draw_text("You finished the game!", bigger_font, WHITE, 150, 50)
        draw_text(f"Time: {stored_final:.2f}", bigger_font, WHITE, 240, 200)
        draw_text("Left click to exit the program :)", bigger_font, WHITE, 80, 400)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False
                pygame.quit()

main_menu()


while run:
    if enemy_rect.x <= -25:
        enemy_rect.x += VEL
    if enemy_rect.x >= 450:
        enemy_rect.x -= VEL

    engaged = False
    
    pygame.draw.rect(screen, GRAY, button_rect)
    button_text = font.render("SHOP", True, BLACK)
    screen.blit(button_text, (button_rect.x + 10, button_rect.y + 10))
    idk = pygame.time.get_ticks()

    if grass_rect.y <= -5425 and all_enemies_defeated:
        elapsed_ticks = elapsed_seconds = (pygame.time.get_ticks() - start_ticks) / 1000
        stored_final = elapsed_ticks
        end_game()
    elif not all_enemies_defeated and grass_rect.y <= -5425:
       print("You have not defeated all the enemies yet!")

    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button_rect.collidepoint(event.pos):
                if popup_active:
                    if button1_rect.collidepoint(event.pos):
                        healing()
                    elif button2_rect.collidepoint(event.pos):
                        speed()
                else:
                    if button_rect.collidepoint(event.pos):
                        popup_active = True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                if popup_active:
                    popup_active = False
                else:
                    run = False    
    
    hero.sprite = pygame.transform.scale(pygame.image.load("hero.png"), (75,75))

    if rect.x <= -50:
        rect.x += VEL     
    if rect.x >= 475:
        rect.x -= VEL
    if rect.y <= -50:
        rect.y += VEL
    if rect.y >= 450:
        rect.y -= VEL
    if hero.health <= 0:        
        draw_text(f"{hero.name} has died!", myFont, (255, 0, 0), rect.x,
                  rect.y + 10)
        

    if popup_active:
        pygame.draw.rect(screen, BLACK, popup_rect)
        pygame.draw.rect(screen, WHITE, popup_inner_rect)

        # Draw buttons inside popup
        pygame.draw.rect(screen, GRAY, button1_rect)
        pygame.draw.rect(screen, GRAY, button2_rect)
        screen.blit(button1_text, (button1_rect.x + 10, button1_rect.y + 5))
        screen.blit(button2_text, (button2_rect.x + 10, button2_rect.y + 5))


           
        
    coin = pygame.transform.scale(pygame.image.load("Frames/Coin.png"),
                                  (100, 100))
    screen.blit(coin, (80, -32.5))
    screen.blit(swift, (155, -12.5))
    rect_x, rect_y = 330, 0  # Top-right corner position
    rect_width, rect_height = 170, 30  # Width and height of the rectangle
    ratio = hero.health / hero.health_max

    pygame.draw.rect(screen, (255, 0, 0),
                     (rect_x, rect_y, rect_width, rect_height))
    pygame.draw.rect(screen, (0, 255, 105),
                     (rect_x, rect_y, rect_width * ratio, rect_height))

    draw_text(f"{hero.health}/{hero.health_max}", myFont, (0, 0, 0), 380, 10)
    draw_text(f"{hero.money}", myFont, (255, 255, 255), 150, 10)

    draw_text(f"{healing_potion}", myFont, (255, 255, 255), 250, 10)
    draw_text(f"{speed_potion}", myFont, (255, 255, 255), 200, 10)

    
    userInput = pygame.key.get_pressed()


    
    
    pygame.display.update()

    if rect.y - enemy_rect.y > 20:
        engaged = True
        
    if engaged:
        if rect.y != enemy_rect.y:
            enemy_rect.y += 10
            time.sleep(.1)
            
            if rect.x - enemy_rect.x < 0:
                enemy_rect.x -= 10
                time.sleep(.1)
            elif rect.x - enemy_rect.x > 0:
                enemy_rect.x += 10
                time.sleep(.1)



    if userInput[pygame.K_LEFT] and hero.health > 0:
        time.sleep(.1)
        rect.x -= VEL
        enemy_rect.x -= 20
        
    if userInput[pygame.K_RIGHT] and hero.health > 0:
        time.sleep(.1)
        rect.x += VEL
        enemy_rect.x += 20
    if userInput[pygame.K_UP] and hero.health > 0:
        if grass_rect.y >= -75:
            grass_rect.y -= VEL

        time.sleep(.1)
        rect.y -= VEL
        enemy_rect.y += 20
        
        grass_rect.y += VEL
    if userInput[pygame.K_DOWN] and hero.health > 0:
        time.sleep(.1)
        if grass_rect.y < -5400:
            grass_rect.y += VEL
            enemy_rect.y += VEL
        rect.y += VEL
        enemy_rect.y -= VEL
        grass_rect.y -= VEL

    if userInput[pygame.K_s]:
        if speed_potion >= 1:
            VEL += 2
            speed_potion -= 1

    if userInput[pygame.K_e]:
        if hero.health < 120 and healing_potion >= 1:
            hero.health += 15
            hero.money -= 1
            healing_potion -= 1

        
        elif hero.health > 120 and hero.money:
            hero.health = hero.health_max
        
    if userInput[pygame.K_1]:
        if hero.money >= 20:
            hero.equip(short_bow)
            hero_weapon = pygame.transform.scale(pygame.image.load(hero.weapon.sprite), (50, 50))
            hero.money -= 20
        else:
            print("Insuficient funds")
    if userInput[pygame.K_2]:
        if hero.money >= 40:
            hero.equip(fire_spear)
            hero_weapon = pygame.transform.scale(pygame.image.load(hero.weapon.sprite), (50, 50))
            hero.money -= 40
        else:
            print("Insuficient funds")
    if userInput[pygame.K_3]:
        if hero.money >= 60:
            hero.equip(golden_sabre)
            hero_weapon = pygame.transform.scale(pygame.image.load(hero.weapon.sprite), (50, 50))
            hero.money -= 60
        else:
            print("Insuficient funds")
    if userInput[pygame.K_4]:
        if hero.money >= 80:
            hero.equip(infected_gun)
            hero_weapon = pygame.transform.scale(pygame.image.load(hero.weapon.sprite), (50, 50))
            hero.money -= 80
        else:
            print("Insuficient funds")
    if userInput[pygame.K_5]:
        if hero.money >= 100:
            hero.equip(mythical_scythe)
            hero_weapon = pygame.transform.scale(pygame.image.load(hero.weapon.sprite), (50, 50))
            hero.money -= 100
        else:
            print("Insuficient funds")
        

    screen.blit(grass, (grass_rect.x, grass_rect.y))
    screen.blit(hero_sprite, rect)
    screen.blit(hero_weapon, (rect.x + 25, rect.y + 10))
    screen.blit(enemy_sprite, enemy_rect) 
    screen.blit(enemy_weapon, (enemy_rect.x + 10, enemy_rect.y - 5))
    

    if rect.colliderect(enemy_rect):  
        time.sleep(.1)
        hero.enemy.attack(hero)
        ratio2 = hero.enemy.health / hero.enemy.health_max
        pygame.draw.rect(screen, (255, 0, 0), (enemy_rect.x, enemy_rect.y-5, 30, 10))
        pygame.draw.rect(screen, (0, 255, 105), (enemy_rect.x, enemy_rect.y-5, 30 * ratio2, 10))


        if rect.colliderect(enemy_rect) and userInput[pygame.K_SPACE] and hero.health > 0:
            time.sleep(0.1)
            if hero.enemy.health <= 0:
                try:
                    print("enemy dead")
                    enemy_index = enemies.index(hero.enemy)
                    hero.enemy = enemies[enemy_index + 1]
                    enemy_sprite = pygame.transform.scale(pygame.image.load(hero.enemy.sprite), (50, 50))
                    enemy_weapon = pygame.transform.scale(pygame.image.load(hero.enemy.weapon.sprite), (50, 50))
                    del enemies[enemy_index]
                    del enemies_name[enemy_index]
                    hero.money += random.randrange(12,18)
                    enemy_rect.center = (random.randrange(25,500), random.randrange(450,675))
                    screen.blit(enemy_sprite, enemy_rect)
                    
                except IndexError:
                    all_enemies_defeated = True
                    print("You have defeated all enemies")
            else:
                hero.attack(hero.enemy)
                time.sleep(0.01)


    
