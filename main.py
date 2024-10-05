# Author: Jared Winkens
import winkenj_files.platform as platform
import winkenj_files.player as player
import winkenj_files.passible_enemy as enemySmall
import winkenj_files.not_passible_enemy as enemyLarge
import carterad_files.Splash_screenv3 as Splash_screen
import carterad_files.cop as cop  # Add the Cop class
import pygame
import sys
from pygame.locals import *
import random
import time

# Initialize Pygame
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

# Initialize constants
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w * 0.85
SCREEN_HEIGHT = screen_info.current_h * 0.90
FPS = 60
REG_SCORE = 59 
BONUS_SCORE = 1000

# Define variables for scorekeeper
score: int = 0
minute: int = 1000 * 60
second: int = 1000
fSizeScore = int(SCREEN_HEIGHT // 25)
fColor = (0, 255, 0)  # Green
scoreXPos = SCREEN_HEIGHT * .01
scoreYPos = SCREEN_WIDTH * .01

window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED)
pygame.display.set_caption("Game")

# Create the player and platform objects
P1 = player.Player(SCREEN_WIDTH, SCREEN_HEIGHT)
PT1 = platform.Platform(SCREEN_WIDTH, SCREEN_HEIGHT)

Splash_screen.SplashScreen.run(window)

# Timer (one minute)
timerMin = pygame.event.custom_type()
pygame.time.set_timer(timerMin, minute)

# Timer (one second)
timerSec = pygame.event.custom_type()
pygame.time.set_timer(timerSec, second)

# Timer (two second)
timerSec2 = pygame.event.custom_type()
pygame.time.set_timer(timerSec2, second * 2)

# Cop spawn timer
timerSpawnCop = pygame.event.custom_type()
pygame.time.set_timer(timerSpawnCop, 5000)

# Create sprite groups
platforms = pygame.sprite.Group()
platforms.add(PT1)
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
enemies = pygame.sprite.Group()

cop_spawned = False  # Track whether the cop has been spawned

def display_text(displaysurface, text, style, size, color, x, y):
    font = pygame.font.SysFont(style, size)
    textImg = font.render(text, True, color)
    displaysurface.blit(textImg, (x, y))
        
def spawn_enemySmall():
    if random.randint(1, 4) < 3:    
        enemy = enemySmall.PassibleEnemy(SCREEN_WIDTH, SCREEN_HEIGHT, PT1)
        enemies.add(enemy)
        all_sprites.add(enemy)

def spawn_enemyLarge():
    if random.randint(1, 5) < 3:
        enemy = enemyLarge.NotPassibleEnemy(SCREEN_WIDTH, SCREEN_HEIGHT, PT1)
        enemies.add(enemy)
        all_sprites.add(enemy)

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
            if event.key == pygame.K_SPACE:
                P1.jump(platforms)
        if event.type == timerSec:
            score += REG_SCORE
        if event.type == timerSec2:
            spawn_enemySmall()
            spawn_enemyLarge()
        if event.type == timerMin:
            score += BONUS_SCORE
        if event.type == timerSpawnCop and not cop_spawned:
            C1 = cop.Cop(SCREEN_WIDTH, SCREEN_HEIGHT, PT1)  # Spawn the cop
            all_sprites.add(C1)
            cop_spawned = True

    # Fill the window with black            
    window.fill((0, 0, 0))
    
    # Move & update the player
    P1.move(SCREEN_WIDTH)
    P1.update(platforms)
    
    # Render all sprites
    for entity in all_sprites:
        window.blit(entity.surf, entity.rect)
    
    # Move all enemies
    for enemy in enemies:
        enemy.move()

    # If the cop has been spawned, move and update it
    if cop_spawned:
        C1.move(enemies)  # Move cop
        C1.update(PT1)  # Update cop position if necessary

        # Check for collision between the player and cop
        if pygame.sprite.collide_rect(P1, C1):
            time.sleep(0.8)
            window.fill((255, 0, 0))
            display_text(window, 'Game Over', 'Verdana', 60, (1, 1, 1), SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.5)
            pygame.display.update()
            for entity in all_sprites:
                entity.kill() 
            time.sleep(1.5)
            pygame.quit()
            sys.exit()

    # Render the score
    display_text(window, 'Score: ' + str(score), 'Cooperplate Gothic Bold', fSizeScore, fColor, scoreXPos, scoreYPos)
    
    # Check for collisions with the player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(0.8)
        window.fill((255, 0, 0))
        display_text(window, 'Game Over', 'Verdana', 60, (1, 1, 1), SCREEN_WIDTH * 0.3, SCREEN_HEIGHT * 0.5)
        pygame.display.update()
        for entity in all_sprites:
            entity.kill() 
        time.sleep(1.5)
        pygame.quit()
        sys.exit()
    
    # Update the display    
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
