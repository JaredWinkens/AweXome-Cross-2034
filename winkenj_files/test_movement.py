import pytest
from player import Player
from platform import Platform
import pygame

def test_player_move() -> None:
    p = Player(800,600)
    assert p.rect.center == (160, 500)
    
def test_player_jump() -> None:
    p = Player(800,600)
    assert p.rect.center == (160, 500)

def test_player_update() -> None:
    p = Player(800,600)
    assert p.rect.center == (160, 500)