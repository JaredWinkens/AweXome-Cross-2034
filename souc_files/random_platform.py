# Written by: Chakriya Sou
# Created: 10/20/2024 3p
# Random platform feature
# Description: Sprite that randomly generates from the right of the screen
# or generates just before the large randomly generated obstacle to help 
# players avoid obstacle.

import pygame
from pygame.locals import *

class RandomPlatform(pygame.sprite.Sprite):

    def __init__(self, screen_width, screen_height, image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (screen_width, screen_height * 0.72))


    def move(self, speed):
        self.rect.move_ip(-speed, 0)
        if self.rect.right <= 0:
            self.kill()

    def draw(self, displaysurface):
        pygame.draw.rect(displaysurface, (255, 0, 0), self.rect, 2)