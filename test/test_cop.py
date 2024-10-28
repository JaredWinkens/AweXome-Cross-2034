# Written by: Chakriya Sou
# Created: 10/08/2024 at 4:00p
# Modified: 10/27/20204 @ 4:15pm (Properly initailize display window to 
#                                  load image)
# Language: Python
# Description: (pytest) These test functions will be implemented in
# testing features in file cop.py

import pytest
from carterad_files.cop import Cop
from winkenj_files.player import Player
from winkenj_files.platform import Platform
import pygame

# Chatgpt assisted
# Description: Intialize display window for image to be loaded properly
@pytest.fixture(scope='module', autouse=True)
def init_pygame():
    """Initialize Pygame and create a display."""
    pygame.init()
    # Create a display to allow image loading
    screen_width = 1366  # You can adjust this as needed
    screen_height = 768
    pygame.display.set_mode((screen_width, screen_height))

    yield  # This allows the test to run after initializing Pygame

    pygame.quit()  # Cleanup after tests are done

@pytest.fixture
def screen_width():
    return 1366

@pytest.fixture
def screen_height():
    return 768

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
    image = pygame.image.load('assets/cop.png').convert_alpha()
    return Cop(screen_width, screen_height, platform, image)

# Written by: Chakriya Sou
# Created: 10/08/2024
# Test: Size of cop should be 2x the size of the player
def test_copSize(cop):
    assert cop.surf.get_size() == (163, 153)

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