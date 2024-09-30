# Author: Jared Winkens
import platform
import player
import pygame
import sys
from pygame.locals import *

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Initialize Pygame
pygame.init()
window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.SCALED)
pygame.display.set_caption("Game")

# Create the player and platform objects
P1 = player.Player(SCREEN_WIDTH,SCREEN_HEIGHT)
PT1 = platform.Platform(SCREEN_WIDTH,SCREEN_HEIGHT)

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
                
    # Fill the window with black            
    window.fill((0,0,0))
    
    # Move & update the player
    P1.move(SCREEN_WIDTH)
    P1.update(platforms)
    
    # Render all sprites
    for entity in all_sprites:
        window.blit(entity.surf,entity.rect)
    
    # Update the display    
    pygame.display.update()
    pygame.time.Clock().tick(FPS)
    

