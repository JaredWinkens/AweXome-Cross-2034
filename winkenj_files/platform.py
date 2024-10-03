# Author: Jared Winkens
import pygame
from pygame.locals import *

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self,
                 screen_width,
                 screen_height,
                 image = []):
        super().__init__()
        
        # Create the platform
        self.surf = pygame.Surface((screen_width, screen_height * 0.10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(screen_width/2, screen_height))