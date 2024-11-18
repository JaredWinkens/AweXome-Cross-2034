# Author: Jared Winkens
import pygame
from pygame.locals import *
import math

# Constants
ACC = 0.5
FRIC = -0.12
vec = pygame.math.Vector2

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self,
                 screen_width,
                 screen_height,
                 images):
        super().__init__()

        # Create the player
        self.index = 0
        self.images = images
        self.image = self.images[self.index]
        self.rect = self.image.get_rect(center=(screen_width*0.2, screen_height))
        self.pos = vec((screen_width*0.2, screen_height))
        self.acc = vec(0,0)
        self.vel = vec(0,0)
        self.cnt = 0
        self.rot_speed = 1/6
    
    # Move the player    
    def move(self,screen_width):
        pass
        '''
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
        '''
    
    # Jump the player
    def jump(self,platforms,ranPlats, screen_height):
        
        # Check if the player is on the ground
        hits = pygame.sprite.spritecollide(self, platforms, False)
        hits2 = pygame.sprite.spritecollide(self, ranPlats, False)
        # If the player is on the ground, jump
        if hits or hits2:
            self.vel.y = -(screen_height * 0.030)
            self.rot_speed = 1/4
    
    # Update the player
    def update(self,platforms,ranPlats,screen_width,speed):
        self.acc = vec(0,0.95)
        
        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        # Check if the player is on the ground
        hits = pygame.sprite.spritecollide(self ,platforms, False) # Check if the player is on the main platform
        hits2 = pygame.sprite.spritecollide(self, ranPlats, False) # Check if the player is on a random platform
        
        # If the player is falling
        if self.vel.y > 0:
            if hits: # If the player is on a the main platform
                self.rot_speed = 1/6 # Set the rotation speed
                self.vel.y = 0 # Stop the player from falling
                self.pos.y = hits[0].rect.top + 1 # Set the player's position to the top of the platform
            if hits2: # If the player is on a random platform
                self.rot_speed = 1/6 # Set the rotation speed
                if self.rect.bottom >= hits2[0].rect.top: # If the player is on top of the platform
                    self.vel.y = 0 # Stop the player from falling
                    self.pos.y = hits2[0].rect.top + 1 # Set the player's position to the top of the platform
                    
        # Ensure the player stays within screen bounds
        if self.pos.x > screen_width:
            self.pos.x = screen_width
        if self.pos.x < 0:
            self.pos.x = 0
        
        # rotate the player based on the speed of the game
        self.cnt += (self.rot_speed + (speed / 100))
        self.index = round(self.cnt) % 8
        self.image = self.images[self.index]
        
        self.rect.midbottom = self.pos
        
    def draw(self, displaysurface):
        pygame.draw.rect(displaysurface, (255, 0, 0), self.rect, 2)
        