import pygame
import pygame.sprite
from sprites import CopSprite
from common import WIDTH, HEIGHT, grid_size, enemy_min_movement, enemy_max_movement
import random


class EnemyPrototypeRight(CopSprite):
    def __init__(self):
        super().__init__()

        self.rect = self.image.get_rect(
            center=(-grid_size, random.randint(grid_size, HEIGHT - grid_size)))

    def update(self):
        self.rect.update(
            self.rect[0] + self.movement, self.rect[1], grid_size, grid_size)

    def clone(self) -> CopSprite:
        return EnemyPrototypeRight()


class EnemyPrototypeLeft(CopSprite):
    def __init__(self):
        super().__init__()

        self.rect = self.image.get_rect(
            center=(WIDTH + grid_size, random.randint(grid_size, HEIGHT - grid_size)))

    def update(self):
        self.rect.update(
            self.rect[0] - self.movement, self.rect[1], grid_size, grid_size)

    def clone(self) -> CopSprite:
        return EnemyPrototypeLeft()


class EnemyPrototypeUp(CopSprite):
    def __init__(self):
        super().__init__()

        self.rect = self.image.get_rect(
            center=(random.randint(0, WIDTH), 0 - grid_size))

    def update(self):
        self.rect.update(self.rect[0], self.rect[1] +
                         self.movement, grid_size, grid_size)

    def clone(self) -> CopSprite:
        return EnemyPrototypeUp()


class EnemyPrototypeDown(CopSprite):
    def __init__(self):
        super().__init__()

        self.rect = self.image.get_rect(
            center=(random.randint(0, WIDTH), HEIGHT + grid_size))

    def update(self):
        self.rect.update(self.rect[0], self.rect[1] -
                         self.movement, grid_size, grid_size)

    def clone(self) -> CopSprite:
        return EnemyPrototypeDown()


class EnemySpawner:

    def spawn_enemy(self, prototype) -> CopSprite:
        return prototype.clone()
