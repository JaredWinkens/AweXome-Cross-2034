# Written by: Chakriya Sou
# Created: 09/27/2024 at 1:30p
# Language: Python
# Description: (pytest) These test functions will be implemented in
# testing features in file player.py

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
    return screen_width #1366

# Written by: Chakriya Sou
# Created: 09/27/2024
# Declare fixtures as argument for users screen height
@pytest.fixture
def screen_height():
    info = pygame.display.Info()
    screen_height = info.current_h
    return screen_height # 768

# Written by: Chakriya Sou
# Created: 09/27/2024
# Last update: 09/30/2024 2p (Players initial position was not on platform. Fixed problem)
# Test: Player position (bottom left corner of screen) will 
# adjust according to users display resolution
def test_Player(screen_width, screen_height):
    player = Player(screen_width, screen_height)
    assert player.rect.center == (273, 768)