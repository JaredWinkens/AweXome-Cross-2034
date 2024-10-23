import pygame
from pygame.locals import *
import sys

# Define color
green = (0, 255, 0)
white = (253, 253, 253)
black = (0, 0, 0)

class SplashScreen:
    def display_text(displaysurface,text, style, size, color, x, y):
        """Helper function to display text on the screen"""
        font = pygame.font.SysFont(style, size)
        textImg = font.render(text, True, color)
        displaysurface.blit(textImg, (x, y))

    def show(displaysurface):
        """Display the splash screen content"""
        displaysurface.fill(black)  # Fill the screen with a background color

        # Display game title and controls with adjusted positions
        SplashScreen.display_text(displaysurface,"WELCOME TO THE GAME!", 'Showcard Gothic', 80, green, 200, 200)
        SplashScreen.display_text(displaysurface,"Press SPACE to Start", 'Showcard Gothic', 50, white, 300, 400)
        SplashScreen.display_text(displaysurface,"Controls:", 'Showcard Gothic', 50, white, 300, 500)
        SplashScreen.display_text(displaysurface,"Move Left: Left Arrow Key", 'Showcard Gothic', 30, white, 300, 550)
        SplashScreen.display_text(displaysurface,"Move Right: Right Arrow Key", 'Showcard Gothic', 30, white, 300, 600)
        SplashScreen.display_text(displaysurface,"Jump: Space Bar", 'Showcard Gothic', 30, white, 300, 650)

        pygame.display.update()

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
                    if event.key == pygame.K_SPACE:  # Start the game when space is pressed
                        splash_active = False

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
    
    def pauseScreen(displaysurface):
        displaysurface.fill((0, 0, 0))
        w, h = displaysurface.get_size()
        fSize = int(h / 8)
        fColor = (255, 0, 0)
        scoreColor = (255, 255, 255)
        isActive = True
        while isActive:
            SplashScreen.display_text(displaysurface, 'Game Paused', 'Showcard Gothic', 
                                        fSize, fColor, int(w * 0.3), int(h * 0.3))
            SplashScreen.display_text(displaysurface, 'Press P to Unpause', 
                                'Showcard Gothic', fSize, scoreColor, int(w * 0.2), int(h * 0.5))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        isActive = False
            