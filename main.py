# Author: Jared Winkens
import winkenj_files.platform as platform
import winkenj_files.player as player
import winkenj_files.passible_enemy as enemySmall
import winkenj_files.not_passible_enemy as enemyLarge
import carterad_files.Splash_screenv3 as Splash_screen
import carterad_files.cop as cop  # Add the Cop class
import carterad_files.cash as cash
import souc_files.random_platform as rPlatform
import winkenj_files.background as bg
import pygame
import sys
from pygame.locals import *
import random
import time
import math

# Initialize Pygame
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

#Sound Initilization
pygame.mixer.music.load("assets/Automation.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play(-1)

# Initialize constants
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w * 0.85
SCREEN_HEIGHT = screen_info.current_h * 0.90
FPS = 60
REG_SCORE = 59 
BONUS_SCORE = 1000
SPEED = 5

# Define variables for scorekeeper
score: int = 0
minute: int = 1000 * 60
second: int = 1000
fSizeScore = int(SCREEN_HEIGHT // 15)
fColor = (0, 255, 0)  # Green
scoreXPos = SCREEN_HEIGHT * .01
scoreYPos = SCREEN_WIDTH * .01
gameOver = 0
FramePerSec = pygame.time.Clock()

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Game")

# Load images
bg_img1 = pygame.transform.scale(pygame.image.load('assets/background_v2/foreground.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_img2 = pygame.transform.scale(pygame.image.load('assets/background_v2/back-buildings.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_img3 = pygame.transform.scale(pygame.image.load('assets/background_v2/far-buildings.png').convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_imgs = [bg_img3,bg_img2,bg_img1]
player_imgs = []
for i in range(8): player_imgs.append(pygame.transform.scale((pygame.image.load('assets/fugitive/fugitive_%d.png' % (i+1)).convert_alpha()),(SCREEN_WIDTH*0.06, SCREEN_HEIGHT*0.1)))
cone_image = pygame.transform.scale(pygame.image.load('assets/cone.png').convert_alpha(),(SCREEN_WIDTH*0.09, SCREEN_HEIGHT*0.13))
dumpster_image = pygame.transform.scale(pygame.image.load('assets/dumpster.png').convert_alpha(),(SCREEN_WIDTH*0.2, SCREEN_HEIGHT*0.3))
cop_image = pygame.transform.scale(pygame.image.load('assets/cop.png').convert_alpha(),(SCREEN_WIDTH*0.12, SCREEN_HEIGHT*0.2))

r_platform_image = pygame.transform.scale(pygame.image.load('assets/r_platform.png'), (SCREEN_WIDTH * .25, SCREEN_HEIGHT * .075))
r_platform_image2 = pygame.transform.scale(pygame.image.load('assets/r_platform.png'), (SCREEN_WIDTH * .15, SCREEN_HEIGHT * .075))

coin_image = pygame.transform.scale(pygame.image.load('assets/coin.png').convert_alpha(), (SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.05))  # Load coin image
coin_sound = pygame.mixer.Sound('assets/coinGet.mp3')

# Create the player and platform objects
P1 = player.Player(SCREEN_WIDTH, SCREEN_HEIGHT, player_imgs)
PT1 = platform.Platform(SCREEN_WIDTH, SCREEN_HEIGHT)
BG = bg.Background(bg_imgs, [SPEED-2, SPEED-1, SPEED])

Splash_screen.SplashScreen.run(window)

# Timer (Speed Timer) CHANGE MULTIPLIER TO TWEAK GAME SPEED
timerSpeed = pygame.event.custom_type()
pygame.time.set_timer(timerSpeed, second * 1)

# Timer (one minute)
timerMin = pygame.event.custom_type()
pygame.time.set_timer(timerMin, minute)

# Timer (one second)
timerSec = pygame.event.custom_type()
pygame.time.set_timer(timerSec, second)

# Timer (two second)
timerSec2 = pygame.event.custom_type()
pygame.time.set_timer(timerSec2, second * 2)

# Timer (three seconds)
timerSec3 = pygame.event.custom_type()
pygame.time.set_timer(timerSec3, 3000)

# Cop spawn timer
timerSpawnCop = pygame.event.custom_type()
pygame.time.set_timer(timerSpawnCop, 5000)

# Create sprite groups
platforms = pygame.sprite.Group()
platforms.add(PT1)
all_sprites = pygame.sprite.Group()
#all_sprites.add(PT1)
all_sprites.add(P1)
small_enemies = pygame.sprite.Group()
large_enemies = pygame.sprite.Group()
enemies = pygame.sprite.Group()
ranPlat = pygame.sprite.Group()
coins = pygame.sprite.Group()

#Create an instance of the cash class
cash_instance = cash.Cash(SCREEN_WIDTH, SCREEN_HEIGHT, coin_image)

cop_spawned = False  # Track whether the cop has been spawned
        
def spawn_enemy():
    seed = random.randint(1, 20)
    if seed <= 10:    
        enemy = enemySmall.PassibleEnemy(SCREEN_WIDTH, SCREEN_HEIGHT, cone_image)
        small_enemies.add(enemy)
        enemies.add(enemy)
        all_sprites.add(enemy)
    elif seed > 10 and seed <= 13:
        enemy = enemyLarge.NotPassibleEnemy(SCREEN_WIDTH, SCREEN_HEIGHT, dumpster_image)
        large_enemies.add(enemy)
        enemies.add(enemy)
        all_sprites.add(enemy)

        newPlatform = rPlatform.RandomPlatform(SCREEN_WIDTH, SCREEN_HEIGHT, r_platform_image)
        platforms.add(newPlatform)
        enemies.add(newPlatform)
        all_sprites.add(newPlatform)
    else:
        print("No enemy spawned")

# Description: Randomize platform at y position. Check for overlapping
# before spawning a new platform.
def spawnRandomPlatform():
    # Set bounds
    xPos = SCREEN_WIDTH
    yPos = random.randint(int(SCREEN_HEIGHT * 0.6), int(SCREEN_HEIGHT * 0.8))

    newPlatform = rPlatform.RandomPlatform(SCREEN_WIDTH, SCREEN_HEIGHT, r_platform_image2)
    newPlatform.rect.center = (xPos, yPos)

    # Check for overlapping
    for platform in platforms:
        if newPlatform.rect.colliderect(platform.rect):
            return  # If overlapping, do not spawn

    # If no overlap, add to groups
    ranPlat.add(newPlatform)
    platforms.add(newPlatform)
    all_sprites.add(newPlatform)

def spawn_coin():
    # Randomly choose a position within the screen boundaries
    x_pos = SCREEN_WIDTH + coin_image.get_width()
    y_pos = random.randint(int(SCREEN_HEIGHT / 2), int(SCREEN_HEIGHT * 0.9))

    coin = cash.Cash(SCREEN_WIDTH, SCREEN_HEIGHT, coin_image)  # Create a new coin instance
    coin.rect.center = (x_pos, y_pos)

    coins.add(coin)
    all_sprites.add(coin)


##############################################
# GAME LOOP
##############################################
while True: 
    # Cycle through all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_p:
                Splash_screen.SplashScreen.pauseScreen(window)
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                pygame.mixer.Sound('assets/jump.mp3').play()
                P1.jump(platforms)
        if event.type == timerSec:
            score += REG_SCORE
        if event.type == timerSec2:
            spawn_enemy()
        if event.type == timerMin:
            score += BONUS_SCORE
        if event.type == timerSec3:
            spawnRandomPlatform()
        if event.type == timerSpeed:
            SPEED = 5 + math.sqrt(SPEED)
        if event.type == timerSpawnCop and not cop_spawned:
            C1 = cop.Cop(SCREEN_WIDTH, SCREEN_HEIGHT, PT1, cop_image)  # Spawn the cop
            all_sprites.add(C1)
            cop_spawned = True
    if (random.randint(1, 700) < 3):
        spawn_coin()

    # Render the background
    BG.update(SPEED)
    # Fill the window with black            
    window.fill((0, 0, 0))
    BG.render(window)
    
    # Move & update the player
    #P1.move(SCREEN_WIDTH)
    P1.update(platforms, SCREEN_WIDTH)
    
    # Move randomize platforms
    for platform in ranPlat:
        platform.move(SPEED)

    # Render all sprites
    for entity in all_sprites:
        window.blit(entity.image, entity.rect)
    
    # Move all enemies
    for enemy in enemies:
        enemy.move(SPEED)

    # If the cop has been spawned, move and update it
    if cop_spawned:
        C1.move(enemies, P1)  # Move cop
        C1.update(PT1)  # Update cop position if necessary

        # Check for collision between the player and cop
        if pygame.sprite.collide_rect(P1, C1):
            pygame.time.set_timer(timerMin, 0)
            pygame.time.set_timer(timerSec, 0)
            pygame.mixer.Sound('assets/handcuff.mp3').play()

            gameOver = -1
            Splash_screen.SplashScreen.deathScreen(window, score)

            for entity in all_sprites:
                entity.kill() 
            time.sleep(5)
            pygame.quit()
            sys.exit()

# Check for coin collection
    for coin in coins:
        if pygame.sprite.collide_rect(P1, coin):
            coin_sound.play()  # Play the collection sound
            cash_instance.collect()  # Increment coins collected in the cash instance
            coin.kill()  # Remove the coin from the game

    # Update coins and remove off-screen coins
    coins.update()

    # Render the score
    Splash_screen.SplashScreen.display_text(window, 'Score: ' + str(score), 
                                        'Cooperplate Gothic Bold', fSizeScore, 
                                        fColor, scoreXPos, scoreYPos)
    
    # Display the number of coins collected using the Cash class
    cash_instance.display_coins(window, SCREEN_WIDTH)
    
    # Check for collisions with the player and enemies
    hits_large = pygame.sprite.spritecollide(P1, large_enemies, False)
    hits_small = pygame.sprite.spritecollide(P1, small_enemies, False)
    if hits_large:
        # Cop moves forward
        # Scrolling Background slows down(illusion that players pace has 
        # slowed down after collision)
        pygame.mixer.Sound('assets/dumpster.mp3').play()
        P1.vel.x = 0
        P1.pos.x = hits_large[0].rect.left - P1.rect.width
    if hits_small:
        pygame.mixer.Sound('assets/cone.mp3').play()
        P1.vel.x = -2
    
    # Update the display
    print(FramePerSec.get_fps())
    pygame.display.update()
    FramePerSec.tick(FPS)
