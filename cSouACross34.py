import pygame
from pygame.locals import *
import sys
import random

pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

# Define font
font = pygame.font.SysFont('Showcard Gothic', 30)

# Define color
green = (0, 255, 0)
white = (253, 253, 253)

HEIGHT = 450
WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60
 
score = 0
scoreIncrement = 5

FramePerSec = pygame.time.Clock()
 
displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        #self.image = pygame.image.load("character.png")
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()
   
        self.pos = vec((10, 360))
        self.vel = vec(0,0)
        self.acc = vec(0,0)
 
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
         
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
             
        self.rect.midbottom = self.pos
 
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
           self.vel.y = -15
 
 
    def update(self):
        hits = pygame.sprite.spritecollide(P1 ,platforms, False)
        if P1.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
 
 
class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT - 10))
 
    def move(self):
        pass

# Class create a coin image
class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        pygame.sprite.Sprite.__init__(self)
        coin = pygame.image.load('images/coin.jpg').convert()
        self.image = pygame.Surface((20, 20)).convert()
        self.image = pygame.transform.scale(coin, (20, 20))
        self.rect = self.image.get_rect()
        self.image.set_colorkey(color)
        self.rect.x = x
        self.rect.y = y
        

# Render text to screen  
def text(text, font, color, x, y):
    textImg = font.render(text, True, color)
    displaysurface.blit(textImg, (x, y))


PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

platforms = pygame.sprite.Group()
platforms.add(PT1)

coinGroup = pygame.sprite.Group()
y = 390
# Randomize coins (test)
for x in range(5):
    x = random.randint(30, WIDTH - 20)
    coin = Coin(x, y, white)
    coinGroup.add(coin)
 
while True: 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
         
    displaysurface.fill((0,0,0))
  
    coinGroup.draw(displaysurface) # Render coin to screen

    # Detect collision
    if pygame.sprite.spritecollide(P1, coinGroup, True):
        score += scoreIncrement

    text(f'Score: {score}', font, green, 10, 10) # Display score

    P1.update()
    
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)
        entity.move()

    pygame.display.update()
    FramePerSec.tick(FPS) 

