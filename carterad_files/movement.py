import pygame
import sys


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
    hits = pygame.sprite.spritecollide(self, platforms, False)
    if hits:
        self.vel.y = -15

    if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()