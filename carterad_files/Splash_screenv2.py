import pygame
from pygame.locals import *
import sys

pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

# Define color
green = (0, 255, 0)
white = (253, 253, 253)
black = (0, 0, 0)

# Create a resizable window
#displaysurface = pygame.display.set_mode((SCREEN_WIDTH - 20, SCREEN_HEIGHT - 100))
#pygame.display.set_caption("Game")


class SplashScreen:
    #@staticmethod
    def display_text(displaysurface,text, style, size, color, x, y):
        """Helper function to display text on the screen"""
        font = pygame.font.SysFont(style, size)
        textImg = font.render(text, True, color)
        displaysurface.blit(textImg, (x, y))

    #@staticmethod
    def show(displaysurface, current_width, current_height):
        """Display the splash screen content"""
        displaysurface.fill(black)  # Fill the screen with a background color

        # Adjust the font sizes dynamically based on the window height
        title_font_size = current_height // 10
        subtitle_font_size = current_height // 20
        control_font_size = current_height // 25

        # Adjust the y-position to make the text appear higher
        title_y_pos = current_height // 6   # Higher position
        subtitle_y_pos = current_height // 3   # Higher position
        controls_y_start = subtitle_y_pos + current_height // 8   # Higher position

        # Display game title and controls with adjusted positions
        SplashScreen.display_text(displaysurface,"AWEXOME CROSS 2034", 'Showcard Gothic', title_font_size, green, current_width // 4, title_y_pos)
        SplashScreen.display_text(displaysurface,"Press SPACE to Start", 'Showcard Gothic', subtitle_font_size, white, current_width // 4, subtitle_y_pos)
        SplashScreen.display_text(displaysurface,"Controls:", 'Showcard Gothic', subtitle_font_size, white, current_width // 4, controls_y_start)
        SplashScreen.display_text(displaysurface,"Move Left: Left Arrow Key", 'Showcard Gothic', control_font_size, white, current_width // 4, controls_y_start + control_font_size * 2)
        SplashScreen.display_text(displaysurface,"Move Right: Right Arrow Key", 'Showcard Gothic', control_font_size, white, current_width // 4, controls_y_start + control_font_size * 4)
        SplashScreen.display_text(displaysurface,"Jump: Space Bar", 'Showcard Gothic', control_font_size, white, current_width // 4, controls_y_start + control_font_size * 6)

        pygame.display.update()

    #@staticmethod
    def run(window, screen_width, screen_height):
        """Combines showing the splash screen and running the event loop in one method"""
        splash_active = True
        current_width, current_height = screen_width, screen_height
        displaysurface = window # Resize window
        #current_width, current_height = SCREEN_WIDTH - 20, SCREEN_HEIGHT - 100
        while splash_active:
            SplashScreen.show(displaysurface,current_width, current_height)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == VIDEORESIZE:
                    current_width, current_height = event.w, event.h
                    #displaysurface = pygame.display.set_mode((current_width, current_height), RESIZABLE)  # Resize window
                    #displaysurface = window
                    SplashScreen.show(displaysurface,current_width,current_height)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:  # Start the game when space is pressed
                        splash_active = False