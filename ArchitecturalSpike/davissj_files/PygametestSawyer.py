import pygame
from pygame.locals import*

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
vec = pygame.math.Vector2

test_sfx = pygame.mixer.Sound("assets/vine-boom.mp3")
pygame.mixer.music.load("assets/Automation.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
HEIGHT = 450 
WIDTH = 400
ACC = 0.5 
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30,30))
        self.surf.fill((128,255,40))
        self.rect = self.surf.get_rect(center = (10, 420))

        self.pos = vec((10,385))
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def move(self):
        self.acc = vec(0,0)

        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_LEFT]:
            self.acc.x = -ACC
        if pressed_keys[K_RIGHT]:
            self.acc.x = ACC
        if pressed_keys[K_b]:
            test_sfx.play()

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x =WIDTH
        self.rect.midbottom = self.pos
        

class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT -10))

PT1 = platform()
P1 = Player()

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    displaysurface.fill((0,0,0))
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
    P1.move()