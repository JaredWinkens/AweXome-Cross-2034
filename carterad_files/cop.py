import pygame

SPEED = 5
JUMP_HEIGHT = 15
JUMP_THRESHOLD = 200  # Distance at which the cop will jump when near an enemy

class Cop(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, platform):
        super().__init__()
        # Cop size is 2x the player size
        self.surf = pygame.Surface((screen_width * 0.12, screen_height * 0.2))
        self.surf.fill((255, 255, 0))  # Yellow to distinguish the cop
        self.rect = self.surf.get_rect(center=(-screen_width * 0.1, platform.rect.top))  # Start off the left edge
        self.vel = pygame.math.Vector2(0, 0)
        self.on_ground = True
        self.screen_width = screen_width

    def move(self, enemies):
        # Move the cop constantly to the right
        self.rect.move_ip(SPEED, 0)

        # Check for proximity to enemies to trigger a jump
        for enemy in enemies:
            distance = self.rect.centerx - enemy.rect.centerx
            if abs(distance) < JUMP_THRESHOLD and self.on_ground:
                self.jump()

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
