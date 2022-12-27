import pygame
from pygame import *
import random

pygame.init()

WIDTH = 640
HEIGHT = 480

game_active = False

joe_health = 3

control_sprites_width = 110
control_sprites_ypos = HEIGHT - 40
control_sprites_xpos = 75

grid_size = 32
size_division = 2
movement = 5
bullet_movement = 15
erase_sprite = 40

enemy_min_movement = 3
enemy_max_movement = 7
enemy_min_health = 1
enemy_max_health = 3
enemy_spawn_timer = pygame.USEREVENT + 1
enemy_spawn_ms = 250
pygame.time.set_timer(enemy_spawn_timer, enemy_spawn_ms)
enemy_animate_timer = pygame.USEREVENT + 2
pygame.time.set_timer(enemy_animate_timer, 300)
enemy_delete_timer = pygame.USEREVENT + 3
pygame.time.set_timer(enemy_delete_timer, 400)

joe_damage_timer = pygame.USEREVENT + 4
joe_animate_timer = pygame.USEREVENT + 5
pygame.time.set_timer(joe_animate_timer, 300)


def enemy_spawning(score):
    if score == 20:
        pygame.time.set_timer(enemy_spawn_timer, enemy_spawn_ms - 50)
    elif score == 40:
        pygame.time.set_timer(enemy_spawn_timer, enemy_spawn_ms - 100)
    elif score == 60:
        pygame.time.set_timer(enemy_spawn_timer, enemy_spawn_ms - 150)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
caption = pygame.display.set_caption("Bounty Joe")
icon = pygame.image.load("Art/JoeIcon.png")
set_icon = pygame.display.set_icon(icon)
clock = pygame.time.Clock()
