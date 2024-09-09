#Imports
import pygame, sys
from pygame.locals import *
import random, time
 
#Initializing 
pygame.init()
 
#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()
 
#Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
 
#Other Variables for use in the program
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0
ACC = 0.5
FRIC = -0.12
vec = pygame.math.Vector2

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)
 
#Create a white screen 
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")
 
 
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        temp_image = pygame.image.load('enemy1.png')
        self.image = pygame.transform.scale(temp_image,(100,100))
        self.surf = pygame.Surface((30, 30))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH,700))
 
      def move(self):
        global SCORE
        self.rect.move_ip(-SPEED,0)
        if (self.rect.left < 0):
            SCORE += 1
            self.rect.left = 0
            self.rect.center = (SCREEN_WIDTH,700)
 
 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        temp_image = pygame.image.load('tire.gif')
        self.image = pygame.transform.scale(temp_image,(100,100))
        self.surf = pygame.Surface((30, 30))
        self.rect = self.surf.get_rect(center = (160, 520))
        
        self.pos = vec((100, 360))
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
        
        if self.pos.x > SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 0
             
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
        temp_image = pygame.image.load('road.png')
        self.image = pygame.transform.scale(temp_image,(SCREEN_WIDTH,100))
        self.surf = pygame.Surface((SCREEN_WIDTH,40))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, 720))
 
    def move(self):
        pass

# Horizontal Background
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('background1.jpg')
            self.rectBGimg = self.bgimage.get_rect()
 
            self.bgY1 = 0
            self.bgX1 = 0
 
            self.bgY2 = 0
            self.bgX2 = self.rectBGimg.width
 
            self.moving_speed = 5
         
      def update(self):
        self.bgX1 -= self.moving_speed
        self.bgX2 -= self.moving_speed
        if self.bgX1 <= -self.rectBGimg.width:
            self.bgX1 = self.rectBGimg.width
        if self.bgX2 <= -self.rectBGimg.width:
            self.bgX2 = self.rectBGimg.width
             
      def render(self):
         DISPLAYSURF.blit(self.bgimage, (self.bgX1, self.bgY1))
         DISPLAYSURF.blit(self.bgimage, (self.bgX2, self.bgY2))

#Setting up Sprites
PT1 = platform()      
P1 = Player()
E1 = Enemy()
 
back_ground = Background()
 
#Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
all_sprites.add(E1)

platforms = pygame.sprite.Group()
platforms.add(PT1)
 
#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
#Game Loop
while True:
       
    #Cycles through all occurring events   
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.5
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()     
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
 
 
    back_ground.update()
    back_ground.render()
 
    #DISPLAYSURF.blit(background, (0,0))
    scores = font.render(str(SCORE), True, WHITE)
    DISPLAYSURF.blit(scores, (10,10))
    
    P1.update()
 
    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()
 
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('crash.mp3').play()
          time.sleep(0.8)
                    
          DISPLAYSURF.fill(RED)
          DISPLAYSURF.blit(game_over, (30,250))
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(1.5)
          pygame.quit()
          sys.exit()        
         
    pygame.display.update()
    FramePerSec.tick(FPS)