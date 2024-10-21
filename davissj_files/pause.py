import pygame
from pygame.locals import *
from carterad_files.Splash_screenv3 import SplashScreen
import sys

def run(window):
        """Combines showing the splash screen and running the event loop in one method"""
        splash_active = True
        displaysurface = window
        while splash_active:
            SplashScreen.show(displaysurface)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:  # Unpause when P is pressed
                        splash_active = False


def pauseScreen(displaysurface):
    displaysurface.fill((0, 0, 0))
    w, h = displaysurface.get_size()
    fSize = int(h / 8)
    fColor = (255, 0, 0)
    scoreColor = (255, 255, 255)
    SplashScreen.display_text(displaysurface, 'Game Paused', 'Showcard Gothic', 
                                    fSize, fColor, int(w * 0.3), int(h * 0.3))
    SplashScreen.display_text(displaysurface, 'Press P to Unpause', 
                            'Showcard Gothic', fSize, scoreColor, int(w * 0.2), int(h * 0.5))
    pygame.display.update()
