# Written by: Chakriya Sou
# Created: 10/07/2024 @6p
# Updated: 10/11/2024 @3:55p
# Splash_screenv3
# Add death(score) to class Splash_screenv3
# Description: Splash screen that appears when the player is caught by 
# the cop. It displays Game Over and the score that was achieved.  

import pygame
from carterad_files.Splash_screenv3 import SplashScreen

def deathScreen(displaysurface, score):
    displaysurface.fill((0, 0, 0))
    w, h = displaysurface.get_size()
    fSize = int(h / 8)
    fColor = (255, 0, 0)
    scoreColor = (255, 255, 255)
    SplashScreen.display_text(displaysurface, 'Game Over', 'Showcard Gothic', 
                                    fSize, fColor, int(w * 0.3), int(h * 0.3))
    SplashScreen.display_text(displaysurface, 'Final Score: ' + str(score), 
                            'Showcard Gothic', fSize, scoreColor, int(w * 0.2), int(h * 0.5))
    pygame.display.update()
