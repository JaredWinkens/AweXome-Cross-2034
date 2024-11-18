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
    
    # Update the background
    def update(self,speed):
        '''
        self.X1 -= speed
        self.X2 -= speed
        if self.X1 <= -self.rect.width:
            self.X1 = self.rect.width
        if self.X2 <= -self.rect.width:
            self.X2 = self.rect.width
        '''
        layer_index = len(self.layers)  # Start at the back
        for layer in self.layers: 
            layer["speed"] = speed-layer_index # Set the speed of the layer
            layer["x"] -= layer["speed"]  # Move each layer based on its speed
            if layer["x"] <= -layer["image"].get_width():
                layer["x"] = 0 # Reset when it goes off-screen
            layer_index -= 1 # Move to the next layer
            
    def render(self,window):
        '''
        window.blit(self.bg_img, (self.X1, self.Y1))
        window.blit(self.bg_img, (self.X2, self.Y2))
        '''
        for layer in self.layers:
            window.blit(layer["image"], (layer["x"], 0))  # Draw the image
            # Draw a second image to ensure seamless scrolling
            window.blit(layer["image"], (layer["x"] + layer["image"].get_width(), 0))
        