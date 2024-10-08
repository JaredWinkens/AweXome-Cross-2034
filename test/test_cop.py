# Written by: Chakriya Sou
# Created: 10/08/2024 at 4:00p
# Language: Python
# Description: (pytest) These test functions will be implemented in
# testing features in file cop.py

import pytest
from carterad_files.cop import Cop
from winkenj_files.player import Player
from winkenj_files.platform import Platform
import pygame

pygame.init()

# Written by: Chakriya Sou
# Created: 10/08/2024
# Declare fixtures as argument for user screen width
@pytest.fixture
def screen_width():
    info = pygame.display.Info()
    screen_width = info.current_w
    return screen_width # 1366 

# Written by: Chakriya Sou
# Created: 10/08/2024
# Declare fixtures as argument for users screen height
@pytest.fixture
def screen_height():
    info = pygame.display.Info()
    screen_height = info.current_h
    return screen_height # 768

# Written by: Chakriya Sou
# Created: 10/08/2024
# Declare fixtures as argument for platform attributes
@pytest.fixture
def platform(screen_width, screen_height):
    return Platform(screen_width, screen_height)

# Written by: Chakriya Sou
# Created: 10/08/2024
# Declare fixtures as argument for cop attributes
@pytest.fixture
def cop(screen_width, screen_height, platform):
    return Cop(screen_width, screen_height, platform)

# Written by: Chakriya Sou
# Created: 10/08/2024
# Test: Size of cop should be 2x the size of the player
def test_copSize(cop):
    assert cop.surf.get_size() == (162, 154)

# Written by: Chakriya Sou
# Created: 10/08/2024
# Test: Bottom of cop rectangle should be at the same position as 
# the top of the platforms rectangle
def test_copStart(cop, platform):
    # Start on top of platform 
    assert cop.rect.bottom == platform.rect.top
    assert cop.on_ground  # Cop should be on the ground

# Written by: Chakriya Sou
# Created: 10/08/2024
# Test: Simulate the cop's movement for a bit without jumping
def test_cop_stays_on_platform_y_position(cop, platform):
    initial_y = cop.rect.y
    cop.move([], None)  # Move without enemies to avoid jumping
    assert cop.rect.y == initial_y  # Cop's y position should remain the same

# Written by: Chakriya Sou
# Created: 10/08/2024
# Test: Simulate cop jumping and landing back onto platform
def test_cop_lands_on_platform_after_jump(cop, platform):
    cop.jump()  # Trigger jump
    cop.update(platform)  # Update position after jump

    # Simulate gravity falling back to the platform
    cop.update(platform)  # Update again to let gravity pull down
    assert cop.rect.bottom == platform.rect.top  # Should land on the platform
    assert cop.on_ground  # Cop should be on the ground