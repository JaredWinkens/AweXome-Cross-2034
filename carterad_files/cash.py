import pygame
import random

class Cash(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, image):
        super().__init__()
        self.image = image
        #self.rect = self.surf.get_rect(center = (screen_width, random.randint(screen_height-400,screen_height-300)))
        self.rect = self.image.get_rect(center=(screen_width, screen_height * 0.9))  # Set initial position
        self.coins_collected = 0  # Track number of coins collected

    def update(self):
        self.rect.move_ip(-7, 0)  # Move left with a speed of 5

        # Check if the cash has gone off screen
        if self.rect.right <= 0:
            self.kill()

    def collect(self):
        self.coins_collected += 1  # Increment the number of coins collected

    def display_coins(self, window, screen_width):
        font = pygame.font.SysFont('Cooperplate Gothic Bold', int(screen_width // 15))
        coin_text = font.render(f'Coins: {self.coins_collected}', True, (0, 255, 0))
        window.blit(coin_text, (screen_width - coin_text.get_width() - 10, 10))  # Position in the top right corner