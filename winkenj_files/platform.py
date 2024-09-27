# Author: Jared Winkens
import pygame

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self,
                 screen_width,
                 screen_height,
                 image = None):
        super().__init__()
        
        # Create the platform
        self.surf = pygame.Surface((screen_width, 100))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(center=(screen_width/2, screen_height - 50))