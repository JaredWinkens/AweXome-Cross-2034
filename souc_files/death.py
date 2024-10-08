# Written by: Chakriya Sou
# Created: 10/07/2024 @6p
# Splash_screenv3
# Add death(score) to class Splash_screenv3
# Description: Splash screen that appears when the player is caught by 
# the cop. It displays Game Over and the score that was achieved.  

import pygame
from carterad_files.Splash_screenv3 import SplashScreen

def deathScreen(displaysurface, score):
    displaysurface.fill((0, 0, 0))  # Fill the screen with black
    SplashScreen.display_text(displaysurface, "Game Over", 'Showcard Gothic', 80, (255, 0, 0), 250, 200)
    SplashScreen.display_text(displaysurface, f"Score: {score}", 'Showcard Gothic', 60, (255, 255, 255), 300, 400)
    pygame.display.update()
    
    # float object cannot be interpreted as integer error
    # Will look into further, for now position is hard coded

    '''displaysurface.fill((0, 0, 0))
    w, h = displaysurface.get_size()
    fSize = int(h / 25)
    fColor = (255, 0, 0)
    SplashScreen.display_text(displaysurface, 'Game Over', 'Verdana', fSize, fColor, int(w * 0.3), int(h * 0.5))
    SplashScreen.display_text(displaysurface, 'Final Score: ' + str(score), 'Verdana', fSize, fColor, int(w * 0.3), int(h * 0.7))
    pygame.display.update()'''
