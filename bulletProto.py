import pygame
import pygame.sprite
from sprites import BulletSprite
from commands import InputHandler
from common import bullet_movement, grid_size


class BulletPrototypeRight(BulletSprite):
    def __init__(self, joe) -> None:
        super().__init__(joe)

        self.image = pygame.image.load("Art/bulletright.png")
        self.rect = self.image.get_rect(
            center=(self.joe.rect[0] + grid_size, self.joe.rect[1] + grid_size / 2))

    def update(self):
        super().update()

        self.rect.update(self.rect[0] + bullet_movement,
                         self.rect[1], 16, 16)

    def clone(self) -> BulletSprite:
        return BulletPrototypeRight(self.joe)


class BulletPrototypeLeft(BulletSprite):
    def __init__(self, joe) -> None:
        super().__init__(joe)

        self.image = pygame.image.load("Art/bulletleft.png")
        self.rect = self.image.get_rect(
            center=(self.joe.rect[0], self.joe.rect[1] + grid_size / 2))

    def update(self):
        super().update()

        self.rect.update(self.rect[0] - bullet_movement,
                         self.rect[1], 16, 16)

    def clone(self) -> BulletSprite:
        return BulletPrototypeLeft(self.joe)


class BulletPrototypeUp(BulletSprite):
    def __init__(self, joe) -> None:
        super().__init__(joe)

        self.image = pygame.image.load("Art/bulletup.png")
        self.rect = self.image.get_rect(
            center=(self.joe.rect[0] + grid_size / 2, self.joe.rect[1]))

    def update(self):
        super().update()

        self.rect.update(self.rect[0], self.rect[1] -
                         bullet_movement, 16, 16)

    def clone(self) -> BulletSprite:
        return BulletPrototypeUp(self.joe)


class BulletPrototypeDown(BulletSprite):
    def __init__(self, joe) -> None:
        super().__init__(joe)

        self.image = pygame.image.load("Art/bulletdown.png")
        self.rect = self.image.get_rect(
            center=(self.joe.rect[0] + grid_size / 2, self.joe.rect[1] + 30))

    def update(self):
        super().update()

        self.rect.update(self.rect[0], self.rect[1] +
                         bullet_movement, 16, 16)

    def clone(self) -> BulletSprite:
        return BulletPrototypeDown(self.joe)


class BulletSpawner:

    def spawn_bullet(self, prototype) -> BulletSprite:
        return prototype.clone()
