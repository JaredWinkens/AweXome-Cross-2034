import pygame
from pygame.locals import *
import sys
import platform
import player

screen_info = pygame.display.Info()

SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
SPEED = 5
ACC = 0.5
FRIC = -0.12
vec = pygame.math.Vector2


def move(self):
    self.acc = vec(0,0.5)
    
    pressed_keys = pygame.key.get_pressed()
            
    if pressed_keys[K_LEFT]:
        self.acc.x = -ACC
    if pressed_keys[K_RIGHT]:
        self.acc.x = ACC
                 
    self.acc.x += self.vel.x * FRIC
    self.vel += self.acc
    self.pos += self.vel + 0.5 * self.acc
         
    if self.pos.x > SCREEN_WIDTH:
        self.pos.x = SCREEN_WIDTH-100
    if self.pos.x < 0:
        self.pos.x = 0
             
        self.rect.midbottom = self.pos
 
def jump(self):
    hits = pygame.sprite.spritecollide(self, platform, False)
    if hits:
        self.vel.y = -15
#might have to put in main game loop in main file not sure yet
    #if event.type == pygame.KEYDOWN:    
            #if event.key == pygame.K_SPACE:
                #P1.jump()


P1 = player()
P1.update()