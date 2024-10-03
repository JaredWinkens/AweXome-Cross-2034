# Author: Jared Winkens
import pygame
from pygame.locals import *

# Constants
ACC = 0.5
FRIC = -0.12

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self,
                 screen_width,
                 screen_height,
                 image = []):
        super().__init__()

        # Create the player
        self.surf = pygame.Surface((screen_width*0.08, screen_height*0.1))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(screen_width*0.1, screen_height * 0.95))
        self.vec = pygame.math.Vector2
        self.pos = self.vec((screen_width*0.1, screen_height * 0.95))
        self.acc = self.vec(0,0)
        self.vel = self.vec(0,0)
    
    # Move the player    
    def move(self,screen_width):
        self.acc = self.vec(0,0.5)
        pressed_keys = pygame.key.get_pressed()
        
        # Change the acceleration based on the keys pressed        
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        
        # Apply friction            
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        # Keep the player on the screen    
        if self.pos.x > screen_width:
            self.pos.x = screen_width
        if self.pos.x < 0:
            self.pos.x = 0
        
        # Update the player's position        
        self.rect.midbottom = self.pos
    
    # Jump the player
    def jump(self,platforms):
        
        # Check if the player is on the ground
        hits = pygame.sprite.spritecollide(self, platforms, False)
        
        # If the player is on the ground, jump
        if hits:
            self.vel.y = -15
    
    # Update the player
    def update(self,platforms):
        
        # Check if the player is on the ground
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        
        # If the player is on the ground, stop falling
        if self.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
        