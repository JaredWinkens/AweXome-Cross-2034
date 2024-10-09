import pygame


class Background():
    def __init__(self,bg_imgs):
        
        self.bg_img = bg_imgs[0]
        self.rect = self.bg_img.get_rect()

        self.Y1 = 0
        self.X1 = 0
        self.Y2 = 0
        self.X2 = self.rect.width
        
    def update(self,speed):
        self.X1 -= speed
        self.X2 -= speed
        if self.X1 <= -self.rect.width:
            self.X1 = self.rect.width
        if self.X2 <= -self.rect.width:
            self.X2 = self.rect.width
             
    def render(self,window):
        window.blit(self.bg_img, (self.X1, self.Y1))
        window.blit(self.bg_img, (self.X2, self.Y2))
        
        