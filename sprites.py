import pygame
import pygame.sprite
from common import *
from observer import Observer, ENEMY_KILLED, LIVES_LOST
from commands import InputHandler


class BGSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Art/Background_start.png")
        self.rect = self.image.get_rect(
            center=(WIDTH / size_division, HEIGHT / size_division))


class ControlsSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("Art/keys.png")
        self.image = pygame.transform.scale(
            self.image, (control_sprites_width, grid_size))
        self.rect = self.image.get_rect(
            center=(control_sprites_xpos, control_sprites_ypos))


class JoeSprite(pygame.sprite.Sprite, InputHandler, Observer):
    def __init__(self):
        super().__init__()

        self.sprites_up = ["Art/JoeUp1.png", "Art/JoeUp2.png"]
        self.sprites_down = ["Art/JoeDown1.png", "Art/JoeDown2.png"]
        self.sprites_left = ["Art/JoeLeft1.png", "Art/JoeLeft2.png"]
        self.sprites_right = ["Art/JoeRight1.png", "Art/JoeRight2.png"]

        self.image = pygame.image.load("Art/Joe.png")
        self.rect = self.image.get_rect(
            center=(WIDTH / size_division, HEIGHT / size_division))
        self.health = joe_health
        self.damaged = False
        self.index = 0

        Observer.__init__(self)

    def switch_index(self):
        if self.index == 0:
            self.index = 1
        else:
            self.index = 0

    def animate(self, side):
        self.image = pygame.image.load(side[self.index])

    def right(self):

        # limitado ao viewport
        if self.rect[0] < WIDTH - grid_size:
            self.rect.update(self.rect[0] + movement,
                             self.rect[1], grid_size, grid_size)
            self.animate(self.sprites_right)

    def left(self):

        # limitado ao viewport
        if self.rect[0] > 0:
            self.rect.update(self.rect[0] - movement,
                             self.rect[1], grid_size, grid_size)
            self.animate(self.sprites_left)

    def up(self):

        # limitado ao viewport
        if self.rect[1] > 0:
            self.rect.update(
                self.rect[0], self.rect[1] - movement, grid_size, grid_size)
            self.animate(self.sprites_up)

    def down(self):

        # limitado ao viewport
        if self.rect[1] < HEIGHT - grid_size:
            self.rect.update(
                self.rect[0], self.rect[1] + movement, grid_size, grid_size)
            self.animate(self.sprites_down)

    def update(self):
        handler = self.handle_input_move()
        if handler != None:
            handler.execute(self)


class CopSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image_index = 0
        self.movement = random.randint(enemy_min_movement, enemy_max_movement)
        self.image = pygame.image.load("Art/cop1.png")
        self.rect = NotImplemented
        self.health = random.randint(enemy_min_health, enemy_max_health)

        self.enemyout = False

    def erase(self, group):
        if self.rect[0] > WIDTH or self.rect[0] < -erase_sprite or self.rect[1] > HEIGHT or self.rect[1] < - erase_sprite:
            group.remove(self)

    def animate(self):
        if self.image_index == 0:
            self.image_index = 1
            self.image = pygame.image.load("Art/cop2.png")
        elif self.image_index == 1:
            self.image_index = 0
            self.image = pygame.image.load("Art/cop1.png")


class BulletSprite(pygame.sprite.Sprite):
    def __init__(self, joe):
        super().__init__()

        self.joe = joe

        self.image = pygame.image.load("Art/bulletright.png")
        self.rect = self.image.get_rect(
            center=(self.joe.rect[0], self.joe.rect[1]))

    def erase(self, group):
        if self.rect[0] > WIDTH or self.rect[0] < -100 or self.rect[1] > HEIGHT or self.rect[1] < -1000:
            group.remove(self)


class ScoreBoard:
    def __init__(self, joe):
        self.scores = 0
        joe.register(ENEMY_KILLED, self.score)

    def score(self):
        self.scores += 1
        enemy_spawning(self.scores)


class ScoreBoardSprite(pygame.sprite.Sprite):
    def __init__(self, scoreboard: ScoreBoard):
        self.font = pygame.font.Font("Art/Pixeltype.ttf", grid_size)
        super().__init__()

        self.scoreboard = scoreboard
        self.txt = str(self.scoreboard.scores)
        self.image = self.font.render(
            f"Score:{self.txt}", True, "white")
        self.rect = self.image.get_rect(topleft=(grid_size, grid_size))

    def update(self):

        self.txt = " " + str(self.scoreboard.scores)
        self.image = self.font.render(
            f"Score:{self.txt}", True, "white")


class JoeLives:
    def __init__(self, joe):
        self.joe = joe
        self.index = 2
        joe.register(LIVES_LOST, self.sprite)

    def sprite(self):
        if self.joe.health == 3:
            self.index = 2
        elif self.joe.health == 2:
            self.index = 1
        elif self.joe.health == 1:
            self.index = 0


class JoeLivesSprite(pygame.sprite.Sprite):
    def __init__(self, lives: JoeLives):
        super().__init__()

        self.lives = lives
        self.images = ["Art/JoeLives1.png",
                       "Art/JoeLives2.png", "Art/JoeLives3.png"]
        self.image = pygame.image.load(self.images[self.lives.index])
        self.rect = self.image.get_rect(
            center=(WIDTH - 115, grid_size + 15))

    def update(self):
        self.image = pygame.image.load(self.images[self.lives.index])


class MainMenuSprite(pygame.sprite.Sprite):
    def __init__(self, scoreboard: ScoreBoard):

        self.scoreboard = scoreboard
        self.font = pygame.font.Font(
            "Art/Pixeltype.ttf", grid_size * size_division)
        self.image = pygame.image.load("Art/MainMenu.png")
        self.rect = self.image.get_rect()

    def draw(self, screen):

        self.txt = " " + str(self.scoreboard.scores)
        self.score = self.font.render(
            f"Your Score: {self.txt}", True, "white")
        self.score_rect = self.score.get_rect(
            center=(WIDTH / size_division, (WIDTH / size_division) + 20))

        screen.blit(self.image, self.rect)
        screen.blit(self.score, self.score_rect)
