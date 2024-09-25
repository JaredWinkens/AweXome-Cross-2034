import pygame
from pygame.locals import *
import sys
import random
import time

pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
screen_info = pygame.display.Info()

# Define color
green = (0, 255, 0)
white = (253, 253, 253)
black = (0, 0 , 0)
red = (255, 0, 0)

# initialize constants
SCREEN_WIDTH = screen_info.current_w
SCREEN_HEIGHT = screen_info.current_h

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

def display_text(text, style, size, color, x, y):
    font = pygame.font.SysFont(style, size)
    textImg = font.render(text, True, color)
    displaysurface.blit(textImg, (x, y))

#Calls splash screen will go above main game loop
splash_screen()