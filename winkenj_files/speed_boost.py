import pygame

class SpeedBoost(pygame.sprite.Sprite):
    def __init__(self,
                 screen_width,
                 screen_height,
                 image):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect(center = (screen_width,screen_height*0.89))
 
    def move(self,speed):
        self.rect.move_ip(-speed,0)
        # Check if speed boost has gone off screen
        if self.rect.right <= 0:
            self.kill()
    
    def draw(self, displaysurface):
        pygame.draw.rect(displaysurface, (0, 255, 0), self.rect, 2)