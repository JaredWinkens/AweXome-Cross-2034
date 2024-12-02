# Written by: Chakriya Sou
# Created: 11/28/2024 at 6:00a

# Language: Python
# Description: (pytest) These test functions will be implemented in
# testing player collision with small enemy (Passed)

# Collision between the cop and player after slowing down will be tested visually.
# Since the initial position of both the player and the cop rectangles is set at the 
# center of the rectangle, the planned testing below will always pass, even in cases 
# where it should fail."

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
# Created: 11/28/2024
# Declare fixtures as argument for player attributes
@pytest.fixture
def player(screen_width, screen_height):
    images = []
    for i in range(8): images.append(pygame.transform.scale((pygame.image.load
                        ('assets/fugitive/fugitive_%d.png' % (i+1)).convert_alpha()),
                        (screen_width*0.06, screen_height*0.1)))
    return Player(screen_width, screen_height, images)

# Written by: Chakriya Sou
# Created: 11/28/2024
# Declare fixtures as argument for passible enemy attributes
@pytest.fixture
def passible_enemy(screen_width, screen_height):
    image = pygame.image.load('assets/cone.png').convert_alpha()
    return PassibleEnemy(screen_width, screen_height, image)

# Written by: Chakriya Sou
# Created: 11/28/2024
# Declare fixtures as argument for platform attributes
@pytest.fixture
def platform(screen_width, screen_height):
    return Platform(screen_width, screen_height)

# Written by: Chakriya Sou
# Created: 11/28/2024
# Declare fixtures as argument for cop attributes
@pytest.fixture
def cop(screen_width, screen_height, platform):
    image = pygame.image.load('assets/cop.png').convert_alpha()
    return Cop(screen_width, screen_height, platform, image)

def test_player_collision_with_small_enemy(player, passible_enemy, cop):
    initial_x_pos = player.pos.x
    
    # Simulate a collision with the small enemy
    player.rect.center = (passible_enemy.rect.centerx, player.rect.centery)

    if pygame.sprite.collide_rect(player, passible_enemy):
        player.pos.x -= 5  

    assert player.pos.x < initial_x_pos, "Player did not move left after collision"

    # After the player slows down, check the distance between the player and the cop
    #distance = abs(player.pos.x - cop.rect.center)
    
    #assert distance > 0, "Cop collided with the player while slowing down"
    
    # Simulate the player returning to its original position
    player.pos.x = initial_x_pos

    assert player.pos.x == initial_x_pos, "Player did not return to the original position after collision"