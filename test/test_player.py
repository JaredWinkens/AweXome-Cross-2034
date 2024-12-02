# Written by: Chakriya Sou
# Created: 09/27/2024 at 1:30p
# Language: Python
# Description: (pytest) These test functions will be implemented in
# testing features in file player.py

# Written by: Chakriya Sou
# Created: 09/27/2024
# Last update: 11/29/2024 3p (Properly initailize display window to load image)
# Test: Player position (bottom left corner of screen) will 
# adjust according to users display resolution

import pytest, pygame
from carterad_files.cop import Cop
from winkenj_files.platform import Platform
from winkenj_files.player import Player
from winkenj_files.passible_enemy import PassibleEnemy

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
# Created: 11/29/2024
# Declare fixtures as argument for player attributes
@pytest.fixture
def player(screen_width, screen_height):
    images = []
    for i in range(8): images.append(pygame.transform.scale((pygame.image.load
                        ('assets/fugitive/fugitive_%d.png' % (i+1)).convert_alpha()),
                        (screen_width*0.06, screen_height*0.1)))
    return Player(screen_width, screen_height, images)

def test_Player(screen_width, screen_height, player):
    
    assert player.rect.center == (273, 768)