import pygame
from pygame.locals import *
import sys

# Define color
green = (0, 255, 0)
white = (253, 253, 253)
black = (0, 0, 0)
red = (255, 0, 0)

class SplashScreen:
    def display_text(displaysurface,text, style, size, color, x, y):
        """Helper function to display text on the screen"""
        font = pygame.font.SysFont(style, size)
        textImg = font.render(text, True, color)
        displaysurface.blit(textImg, (x, y))

    def show(displaysurface,splash_image):
        """Display the splash screen content"""
        #displaysurface.fill(black)  # Fill the screen with a background color
        displaysurface.blit(splash_image, (0, 0))  # Display the splash image
        w, h = displaysurface.get_size()

        # Display game title and controls with adjusted positions
        SplashScreen.display_text(displaysurface,"AWEXOME CROSS 2034", 'Showcard Gothic', 80, green, w*0.01, h*0.05)
        SplashScreen.display_text(displaysurface,"Press SPACE", 'Showcard Gothic', 45, red, w*0.48, h*0.5)
        SplashScreen.display_text(displaysurface,"to Start", 'Showcard Gothic', 45, red, w*0.48, h*0.55)
        SplashScreen.display_text(displaysurface,"Controls:", 'Showcard Gothic', 45, green, w*0.48, h*0.65)
        SplashScreen.display_text(displaysurface,"Jump: Space Bar", 'Showcard Gothic', 30, green, w*0.48, h*0.72)
        SplashScreen.display_text(displaysurface,"Pause: [P]", 'Showcard Gothic', 30, green, w*0.48, h*0.77)

        pygame.display.update()

    def run(window, splash_image):
        """Combines showing the splash screen and running the event loop in one method"""
        splash_active = True
        displaysurface = window
        while splash_active:
            SplashScreen.show(displaysurface, splash_image)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Start the game when space is pressed
                        splash_active = False

    def deathScreen(displaysurface, coin, score,death_image):
        displaysurface.blit(death_image,(0, 0))
        w, h = displaysurface.get_size()
        fSize = int(h / 13)
        fColor = (255, 0, 0)
        scoreColor = (255, 255, 255)
        SplashScreen.display_text(displaysurface, 'Game Over', 'Showcard Gothic', 
                                        fSize, fColor, int(w * 0.3), int(h * 0.01))
        SplashScreen.display_text(displaysurface, 'Coins x 3: ' + str(coin), 
                                'Showcard Gothic', fSize, (20, 20, 255), int(w * 0.025), int(h * 0.85))
        SplashScreen.display_text(displaysurface, 'Final Score: ' + str(score), 
                                'Showcard Gothic', fSize, scoreColor, int(w * 0.025), int(h * 0.92))
        # Display "R to Restart" and "E to Exit" on the left side of the screen
        SplashScreen.display_text(displaysurface, 'R to Restart', 'Showcard Gothic', 50, red, int(w * 0.05), int(h * 0.2))
        SplashScreen.display_text(displaysurface, 'E to Exit', 'Showcard Gothic', 50, red, int(w * 0.05), int(h * 0.3))
        pygame.display.update()
        
    def pauseScreen(displaysurface,pause_image):
        displaysurface.blit(pause_image,(0, 0))
        w, h = displaysurface.get_size()
        fSize = int(h / 8)
        fColor = (255, 0, 0)
        scoreColor = (255, 255, 255)
        isActive = True
        while isActive:
            SplashScreen.display_text(displaysurface, 'Game Paused', 'Showcard Gothic', 
                                        fSize, fColor, int(w * 0.25), int(h * 0.01))
            SplashScreen.display_text(displaysurface, 'Press [P] to Unpause', 
                                'Showcard Gothic', fSize, scoreColor, int(w * .09), int(h * 0.87))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        isActive = False
            