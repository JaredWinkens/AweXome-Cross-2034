# Author: Jared Winkens
import pygame

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self,
                 screen_width,
                 screen_height,
                 image = []):
        super().__init__()

        # Create the player
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(160, screen_height - 100))
    
        