from player import Player
import pygame

def test_player_move() -> None:
    p = Player(800,600)
    p.move()
    assert p.rect.center == (160, 500)
    
def test_player_jump() -> None:
    p = Player(800,600)
    p.jump()
    assert p.rect.center == (160, 500)

def test_player_update() -> None:
    p = Player(800,600)
    p.update()
    assert p.rect.center == (160, 500)