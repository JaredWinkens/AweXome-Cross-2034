# Author: Jared Winkens
import winkenj_files.platform as platform
import winkenj_files.player as player
import carterad_files.Splash_screenv3 as Splash_screen
import pygame
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()
pygame.mixer.pre_init(44100, 16, 2, 4096)

# Initialize constants
screen_info = pygame.display.Info()
SCREEN_WIDTH = screen_info.current_w*0.85
SCREEN_HEIGHT = screen_info.current_h*0.90
FPS = 60
REG_SCORE = 59 
BONUS_SCORE = 1000

# Define variables for scorekeeper
score: int = 0
minute: int = 1000 * 60
second: int = 1000
fSizeScore = int(SCREEN_HEIGHT // 25)
fColor = (0, 255, 0) # Green
scoreXPos = SCREEN_HEIGHT * .01
scoreYPos = SCREEN_WIDTH * .01

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SCALED)
pygame.display.set_caption("Game")

# Create the player and platform objects
P1 = player.Player(SCREEN_WIDTH,SCREEN_HEIGHT)
PT1 = platform.Platform(SCREEN_WIDTH,SCREEN_HEIGHT)

Splash_screen.SplashScreen.run(window)

# Timer (one minute)
timerMin = pygame.event.custom_type()
pygame.time.set_timer(timerMin, minute)

# Timer (one second)
timerSec = pygame.event.custom_type()
pygame.time.set_timer(timerSec, second)

# Create sprite groups
platforms = pygame.sprite.Group()
platforms.add(PT1)
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

##############################################
# GAME LOOP
##############################################
while True: 
    #Cycle through all events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump(platforms)
        if event.type == timerSec:
            score += REG_SCORE
        if event.type == timerMin:
            score += BONUS_SCORE

    # Fill the window with black            
    window.fill((0,0,0))
    
    # Move & update the player
    P1.move(SCREEN_WIDTH)
    P1.update(platforms)
    
    # Render all sprites
    for entity in all_sprites:
        window.blit(entity.surf,entity.rect)
    
    Splash_screen.SplashScreen.display_text(window, 'Score: ' + str(score),
                                        'Cooperplate Gothic Bold', 
                                        fSizeScore, fColor, scoreXPos, scoreYPos)
    # Update the display    
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    

