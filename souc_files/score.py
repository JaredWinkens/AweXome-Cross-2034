# Written by: Chakriya Sou
# Created: 10/3/2024 3p
# Score feature
# Description: Based on time survived. The longer the game continues 
# the score increases and is displayed. 

# Tester: Copy this file to your folder so you can play around with the 
# numbers to help you test and record data

import pygame
import sys
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
REG_SCORE = 59 
BONUS_SCORE = 1000

score: int = 0
minute: int = 1000 * 60
second: int = 1000
fSizeScore = int(SCREEN_HEIGHT // 25)
fColor = (0, 255, 0) # Green
scoreXPos = SCREEN_HEIGHT * .01
scoreYPos = SCREEN_WIDTH * .01

window = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

# Timer (one minute)
timerMin = pygame.event.custom_type()
pygame.time.set_timer(timerMin, minute)

# Timer (one second)
timerSec = pygame.event.custom_type()
pygame.time.set_timer(timerSec, second)

# Written by: Aiden Carter
# Function name: display_text 
# Description: Helper function to display text on the screen
def display_text(displaysurface,text, font, size, color, x, y):
        """Helper function to display text on the screen"""
        font = pygame.font.SysFont(font, size)
        textImg = font.render(text, True, color)
        displaysurface.blit(textImg, (x, y))

while True: 

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == timerSec:
            score += REG_SCORE
        if event.type == timerMin:
            score += BONUS_SCORE
          
    window.fill((0, 0, 0,))

    display_text(window, 'Score: ' + str(score),'ShowCard Gothic', 
                                fSizeScore, fColor, scoreXPos, scoreYPos)
    pygame.display.update()
