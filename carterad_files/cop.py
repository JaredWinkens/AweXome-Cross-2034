import pygame
import time

SPEED = 5
JUMP_HEIGHT = 15
JUMP_THRESHOLD = 100  # Distance at which the cop will jump when near an enemy
MOVE_BACK_DELAY = 15 #Timer for moving back. If player avoids cones/dumpsters for 15sec cop oves back 1 space/to start

class Cop(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, platform):
        super().__init__()
        # Cop size is 2x the player size
        self.surf = pygame.Surface((screen_width * 0.08, screen_height * 0.1))
        self.surf.fill((255, 255, 0))  # Yellow to distinguish the cop
        self.rect = self.surf.get_rect(center=(-screen_width * 0.1, platform.rect.top))  # Start off the left edge
        self.vel = pygame.math.Vector2(0, 0)
        self.on_ground = True
        self.screen_width = screen_width
        self.moving_forward = True  # Track if cop is moving forward
        self.moving_back = False  # Track if cop is moving back
        self.stop_x_position = screen_width * 0.05 # Stop position (half on, half off the screen)
        self.initial_position = self.rect.x  # Store the initial position to move back after 15 seconds

    def move(self, enemies, player):
        # Only move forward if the cop has not yet reached its stop position
        if self.moving_forward and self.rect.right < self.stop_x_position:
            self.rect.move_ip(SPEED, 0)
        else:
            self.moving_forward = False

        # Check for proximity to enemies to trigger a jump
        for enemy in enemies:
            distance = self.rect.right - enemy.rect.centerx
            if abs(distance) < JUMP_THRESHOLD and self.on_ground:
                self.jump()

        # Move back if player avoids obstacles for 15 seconds
        if self.moving_back:
            if self.rect.x > self.initial_position:  # Move back until reaching initial position
                self.rect.move_ip(-SPEED, 0)
            else:
                self.moving_back = False  # Stop moving back once cop reaches initial position

    def jump(self):
        if self.on_ground:
            self.vel.y = -JUMP_HEIGHT  # Set the upward velocity for the jump
            self.on_ground = False  # Cop is no longer on the ground

    def update(self, platform):
        # Apply gravity
        self.vel.y += 0.5  # Gravity acceleration
        self.rect.y += self.vel.y

        # Check if the cop lands on the platform again
        if self.rect.bottom >= platform.rect.top:
            self.rect.bottom = platform.rect.top
            self.vel.y = 0
            self.on_ground = True  # Cop is back on the ground
