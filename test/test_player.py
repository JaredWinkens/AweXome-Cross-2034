# Written by: Chakriya Sou
# Created: 09/27/2024 at 1:30p
# Language: Python
# Description: (pytest) These test functions will be implemented in
# testing features in file player.py, and platform.py

import pytest
from winkenj_files.player import Player
from winkenj_files.platform import Platform
import pygame
import math

pygame.init()

# Written by: Chakriya Sou
# Created: 09/27/2024
# Declare fixtures as argument for user screen width
@pytest.fixture
def screen_width():
    info = pygame.display.Info()
    screen_width = info.current_w
    return screen_width

# Written by: Chakriya Sou
# Created: 09/27/2024
# Declare fixtures as argument for users screen height
@pytest.fixture
def screen_height():
    info = pygame.display.Info()
    screen_height = info.current_h
    return screen_height

# Written by: Chakriya Sou
# Created: 09/27/2024
# Last update: 09/29/2024 2p (Compute x,y coordinates)
# Test: Player position (bottom left corner of screen) will 
# adjust according to users display resolution
def test_Player(screen_width, screen_height):
    player = Player(screen_width, screen_height)
    assert player.rect.center == (math.ceil(screen_width * 0.1), screen_height * 0.75)
    #assert player.rect.center == (screen_width // 15, screen_height - 
    #                               (screen_height // 15))

# Written by: Chakriya Sou
# Created: 09/28/2024
# Last update: 09/29/2024 2p (Compute y coordinates)
# Test: Platform position (bottom of screen) will adjust according 
# to users display resolution
def test_Platform(screen_width, screen_height):
    platform = Platform(screen_width, screen_height)
    assert platform.rect.center == (screen_width // 2, math.ceil(screen_height * 0.95))
    #assert platform.rect.center == (screen_width // 2, screen_height - 
    #                               (screen_height * .075))