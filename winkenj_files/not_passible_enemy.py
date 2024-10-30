import pygame

class NotPassibleEnemy(pygame.sprite.Sprite):
      def __init__(self,
                   screen_width,
                   screen_height,
                   image):
        super().__init__()
        self.image = image
        self.surf = pygame.Surface((screen_width*0.2, screen_height*0.3))
        #self.surf.fill((0, 0, 255)) 
        self.rect = self.surf.get_rect(center = (screen_width,screen_height*0.85))
 
      def move(self,speed):
        self.rect.move_ip(-speed,0)
        # Check if enemy has gone off screen
        if self.rect.right <= 0:
            self.kill()
            
      def draw(self, displaysurface):
        pygame.draw.rect(displaysurface, (255, 0, 0), self.rect, 2)
