import pygame


class Background():
    def __init__(self,bg_imgs,speeds):
        '''
        self.bg_img = bg_imgs[0]
        self.rect = self.bg_img.get_rect()

        self.Y1 = 0
        self.X1 = 0
        self.Y2 = 0
        self.X2 = self.rect.width
        '''
        self.layers = []
        for i in range(len(bg_imgs)):
            self.layers.append({
                "image": bg_imgs[i],
                "x": 0,
                "speed": speeds[i]
            })
            
    def update(self,speed):
        '''
        self.X1 -= speed
        self.X2 -= speed
        if self.X1 <= -self.rect.width:
            self.X1 = self.rect.width
        if self.X2 <= -self.rect.width:
            self.X2 = self.rect.width
        '''
        i = 3
        for layer in self.layers:
            layer["speed"] = speed-i
            layer["x"] -= layer["speed"]  # Move each layer based on its speed
            if layer["x"] <= -layer["image"].get_width():
                layer["x"] = 0 # Reset when it goes off-screen
            i -= 1
        i = 3
        
    def render(self,window):
        '''
        window.blit(self.bg_img, (self.X1, self.Y1))
        window.blit(self.bg_img, (self.X2, self.Y2))
        '''
        for layer in self.layers:
            window.blit(layer["image"], (layer["x"], 0))  # Draw the image
            # Draw a second image to ensure seamless scrolling
            window.blit(layer["image"], (layer["x"] + layer["image"].get_width(), 0))
        