import pygame
from pygame.locals import *
import sys
import random
import time

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screen_info = pygame.display.Info()

#Sound Initilization
pygame.mixer.music.load("assets/Automation.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)

# Define color
green = (0, 255, 0)
white = (253, 253, 253)
black = (0, 0 , 0)
red = (255, 0, 0)

# initialize constants
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h
SPEED = 5
ACC = 0.5
FRIC = -0.12
FPS = 60

# load images
background_image = pygame.image.load('assets/background1.jpg')
cone_image = pygame.transform.scale(pygame.image.load('assets/enemy1.png'),(100,100))
road_image = pygame.transform.scale(pygame.image.load('assets/road2.png'),(SCREEN_WIDTH,200))
coin_image = pygame.transform.scale(pygame.image.load('assets/coin.png'),(70,70))
wheel_images = []
for i in range(7): wheel_images.append(pygame.transform.scale((pygame.image.load('assets/wheel%d.png' % (i+1))),(100,100)))

# initialize global variables
startTime = 0
currentTime = 0
duration = 50
score = 0
scoreIncrement = 5
energy = 100.01
gameOver = 0
vec = pygame.math.Vector2 #2 for two dimensional
FramePerSec = pygame.time.Clock()
displaysurface = pygame.display.set_mode((SCREEN_WIDTH-20, SCREEN_HEIGHT-100))
pygame.display.set_caption("Game")

def splash_screen():
    splash_active = True
    displaysurface.fill(black)  # Fill the screen with a background color

    # Display game title and controls
    display_text("AWEXOME CROSS 2034", 'Showcard Gothic', 80, green, 200, 200)
    display_text("Press SPACE to Start", 'Showcard Gothic', 50, white, 300, 400)
    display_text("Controls:", 'Showcard Gothic', 50, white, 300, 500)
    display_text("Move Left: Left Arrow Key", 'Showcard Gothic', 30, white, 300, 550)
    display_text("Move Right: Right Arrow Key", 'Showcard Gothic', 30, white, 300, 600)
    display_text("Jump: Space Bar", 'Showcard Gothic', 30, white, 300, 650)

    pygame.display.update()

    # Splash screen event loop, waits for SPACE key press
    while splash_active:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Start the game when space is pressed
                    splash_active = False
                    
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = cone_image
        self.surf = pygame.Surface((30, 30))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH,SCREEN_HEIGHT-200))
 
      def move(self):
        self.rect.move_ip(-SPEED,0)
        # Check if enemy has gone off screen
        if self.rect.right <= 0:
            self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
                          
        self.index = 0
        self.image = wheel_images[self.index]
        self.surf = pygame.Surface((30, 30))
        self.rect = self.surf.get_rect(center = (160, SCREEN_HEIGHT-250))

        self.pos = vec((160, 360))
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
            self.pos.x = SCREEN_WIDTH-100
        if self.pos.x < 0:
            self.pos.x = 0
             
        self.rect.midbottom = self.pos
 
    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
           self.vel.y = -15
 
    def update(self):
        hits = pygame.sprite.spritecollide(self ,platforms, False)
        if self.vel.y > 0:        
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1

        self.index += 1
        if self.index >= len(wheel_images):
            self.index = 0
        self.image = wheel_images[self.index]
        
# Class create a coin image
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = coin_image
        self.surf = pygame.Surface((100, 100))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH, random.randint(SCREEN_HEIGHT-400,SCREEN_HEIGHT-300)))
    
    def move(self):
        self.rect.move_ip(-SPEED,0)
        # Check if coin has gone off screen
        if self.rect.right <= 0:
            self.kill()

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = road_image
        self.surf = pygame.Surface((SCREEN_WIDTH-10,100))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 150))
 
        self.Y1 = SCREEN_HEIGHT-200
        self.X1 = 0
        self.Y2 = SCREEN_HEIGHT-200
        self.X2 = self.rect.width
         
    def update(self):
        self.X1 -= SPEED
        self.X2 -= SPEED
        if self.X1 <= -self.rect.width:
            self.X1 = self.rect.width
        if self.X2 <= -self.rect.width:
            self.X2 = self.rect.width
             
    def render(self):
         displaysurface.blit(self.image, (self.X1, self.Y1))
         displaysurface.blit(self.image, (self.X2, self.Y2))
         
    def move(self):
        pass
    
# Horizontal Background
class Background():
    def __init__(self):
        self.bgimage = background_image
        self.rect = self.bgimage.get_rect()
        
        self.Y1 = 0
        self.X1 = 0
        self.Y2 = 0
        self.X2 = self.rect.width
          
    def update(self):
        self.X1 -= SPEED
        self.X2 -= SPEED
        if self.X1 <= -self.rect.width:
            self.X1 = self.rect.width
        if self.X2 <= -self.rect.width:
            self.X2 = self.rect.width
             
    def render(self):
        displaysurface.blit(self.bgimage, (self.X1, self.Y1))
        displaysurface.blit(self.bgimage, (self.X2, self.Y2))


# Render text to screen  
def display_text(text, style, size, color, x, y):
    font = pygame.font.SysFont(style, size)
    textImg = font.render(text, True, color)
    displaysurface.blit(textImg, (x, y))

def spawn_coin():
    coin = Coin()
    coinGroup.add(coin)
    all_sprites.add(coin)

def spawn_enemy():
    enemy = Enemy()
    enemies.add(enemy)
    all_sprites.add(enemy)

back_ground = Background()
PT1 = platform()
P1 = Player()
coin = Coin()
E1 = Enemy()

enemies = pygame.sprite.Group()
enemies.add(E1)

coinGroup = pygame.sprite.Group()
coinGroup.add(coin)

platforms = pygame.sprite.Group()
platforms.add(PT1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(coin)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#calls splash screen before game loop
splash_screen()

#Game Loop
while True: 
    #Cycles through all occurring events  
    for event in pygame.event.get():
        if event.type == INC_SPEED:
              SPEED += 0.1
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:    
            if event.key == pygame.K_SPACE:
                P1.jump()
        
    #currentTime = pygame.time.get_ticks() 
    
    back_ground.update()
    back_ground.render()   
    PT1.update()
    PT1.render()
    P1.update()
    
    
    for entity in all_sprites:
        displaysurface.blit(entity.image, entity.rect)
        entity.move()
    
    if (random.randint(1, 700) < 3):
        spawn_coin()
    if (random.randint(1, 1000) < 3):
        spawn_enemy()

    # Display players energy level (WIP)
    '''
    display_text(f'Energy Level: {energy:3.2f}%', 'Showcard Gothic', 30, green, 10, 40)
    if currentTime - startTime >= duration: 
            startTime = currentTime
            energy -= .1
            if energy == 0:
                gameOver = -1
    '''
    #To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollide(P1, coinGroup,True):
        pygame.mixer.Sound("assets/coinGet.mp3").play()
        score += scoreIncrement
    display_text(f'Score: {score}', 'Showcard Gothic', 30, green, 10, 10) # Display score
    
    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
          pygame.mixer.Sound('assets/crash.mp3').play()
          time.sleep(0.8)
                
          displaysurface.fill(red)
          display_text(f'Game Over','Verdana', 60, black, 400, 200)
           
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(1.5)
          pygame.quit()
          sys.exit()
          
    print(FramePerSec.get_fps())
    pygame.display.update()
    FramePerSec.tick(FPS)