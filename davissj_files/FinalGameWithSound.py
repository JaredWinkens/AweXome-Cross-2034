import pygame
from pygame.locals import *
import sys
import random
import time

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
vec = pygame.math.Vector2 #2 for two dimensional

#Sound Initilization
coin_sfx = pygame.mixer.Sound("assets/coinGet.mp3")
pygame.mixer.music.load("assets/Automation.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Define font
#font = pygame.font.SysFont('Showcard Gothic', 30)

# Define color
green = (0, 255, 0)
white = (253, 253, 253)
black = (0, 0 , 0)
red = (255, 0, 0)

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
SPEED = 5
#HEIGHT = 450
#WIDTH = 400
ACC = 0.5
FRIC = -0.12
FPS = 60

startTime = 0
currentTime = 0
duration = 50
score = 0
scoreIncrement = 5
energy = 100.01
gameOver = 0

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        temp_image = pygame.image.load('assets/enemy1.png')
        self.image = pygame.transform.scale(temp_image,(100,100))
        self.surf = pygame.Surface((30, 30))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH,700))
 
      def move(self):
        #global SCORE
        self.rect.move_ip(-SPEED,0)
        if (self.rect.left < 0):
            #SCORE += 1
            self.rect.left = 0
            self.rect.center = (SCREEN_WIDTH,700)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        #self.image = pygame.image.load("character.png")
        '''self.surf = pygame.Surface((30, 30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect()'''
        temp_image = pygame.image.load('assets/wheel.png')
        self.image = pygame.transform.scale(temp_image,(100,100))
        self.surf = pygame.Surface((40, 40))
        self.rect = self.surf.get_rect(center = (160, 400))

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
        temp_image = pygame.image.load('assets/road.png')
        self.image = pygame.transform.scale(temp_image,(SCREEN_WIDTH,100))
        self.surf = pygame.Surface((SCREEN_WIDTH,40))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, 720))
 
    def move(self):
        pass

# Class create a coin image
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        coin = pygame.image.load('assets/coin.png')
        self.image = pygame.transform.scale(coin, (50, 50))
        self.surf = pygame.Surface((100, 100))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH, 560))
        #self.image.set_colorkey()
        self.move_direction = 5
        #self.rect.y = y
    
    def move(self):
        self.rect.x -= self.move_direction
        # Check if coin has gone off screen
        if self.rect.right <= 0:
            self.kill()
        
class Button():
    pass
# Horizontal Background
class Background():
      def __init__(self):
            self.bgimage = pygame.image.load('assets/background1.jpg')
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
         displaysurface.blit(self.bgimage, (self.bgX1, self.bgY1))
         displaysurface.blit(self.bgimage, (self.bgX2, self.bgY2))


# Render text to screen  
def text(text, style, size, color, x, y):
    font = pygame.font.SysFont(style, size)
    textImg = font.render(text, True, color)
    displaysurface.blit(textImg, (x, y))

back_ground = Background()
PT1 = platform()
P1 = Player()
coin = Coin()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coinGroup = pygame.sprite.Group()
#coinGroup.add(coin)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin)

platforms = pygame.sprite.Group()
platforms.add(PT1)

'''y = 390
# Randomize coins (test)
for x in range(5):
    x = random.randint(30, SCREEN_WIDTH - 20)'''

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)
 
while True: 
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
        if (random.randint(1, 10) < 3):
            coin = Coin()
            coinGroup.add(coin)
            all_sprites.add(coin)
        
    currentTime = pygame.time.get_ticks() 

    back_ground.update()
    back_ground.render()   
    #displaysurface.fill((0,0,0))

    # Detect collision
    if pygame.sprite.spritecollide(P1, coinGroup, True):
        coin_sfx.play()
        score += scoreIncrement
    text(f'Score: {score}', 'Showcard Gothic', 30, green, 10, 10) # Display score

    P1.update()

    for entity in all_sprites:
        displaysurface.blit(entity.image, entity.rect)
        entity.move()
     # Display players energy level
    text(f'Energy Level: {energy:3.2f}%', 'Showcard Gothic', 30, green, 10, 40)
    if currentTime - startTime >= duration: 
            startTime = currentTime
            energy -= .01
            if energy == 0:
                gameOver = -1
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('assets/crash.mp3').play()
          time.sleep(0.8)
                
          displaysurface.fill(red)
          text(f'Game Over','Verdana', 60, black, 400, 200)
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(1.5)
          pygame.quit()
          sys.exit()        
    print(coinGroup)  
    pygame.display.update()
    FramePerSec.tick(FPS) 

