import pygame
import pygame.mixer as mixer
import random
from sprites import JoeSprite, BGSprite, ControlsSprite, ScoreBoard, ScoreBoardSprite, MainMenuSprite, JoeLives, JoeLivesSprite
from observer import Observer, ENEMY_KILLED, LIVES_LOST
from enemyProto import *
from bulletProto import *
from common import *


# ENTITIES AND THEIR GROUPS

Joe = JoeSprite()

enemy_d = EnemyPrototypeDown()
enemy_u = EnemyPrototypeUp()
enemy_l = EnemyPrototypeLeft()
enemy_r = EnemyPrototypeRight()

enemy_group = [enemy_d, enemy_l, enemy_r, enemy_u]

r = BulletPrototypeRight(Joe)
l = BulletPrototypeLeft(Joe)
u = BulletPrototypeUp(Joe)
d = BulletPrototypeDown(Joe)


bullets_input_iterator = {
    pygame.K_RIGHT: r,
    pygame.K_LEFT: l,
    pygame.K_DOWN: d,
    pygame.K_UP: u
}

scoreboard = ScoreBoard(Joe)
scoreboard_sprite = ScoreBoardSprite(scoreboard)

joe_lives = JoeLives(Joe)
joe_lives_sprite = JoeLivesSprite(joe_lives)

sprites = pygame.sprite.Group()
sprites.add(BGSprite())
sprites.add(ControlsSprite())
sprites.add(Joe)
sprites.add(scoreboard_sprite)
sprites.add(joe_lives_sprite)

enemy_spawner = EnemySpawner()
enemy_sprites = pygame.sprite.Group()

bullet_spawner = BulletSpawner()
bullet_sprites = pygame.sprite.Group()

gun_sound_path = "Art/shot.wav"
gun_sound = mixer.Sound(gun_sound_path)
gun_sound.set_volume(0.05)

hurt_sound_path = "Art/hurt.wav"
hurt_sound = mixer.Sound(hurt_sound_path)
hurt_sound.set_volume(0.05)

music_path = "Art/track.wav"
music = mixer.music.load(music_path)
music_play = mixer.music.play(-1)
music_volume = mixer.music.set_volume(0.02)

main_menu = MainMenuSprite(scoreboard)


# INTERACTION FUNCTIONS WITH ENTITIES

def lose():
    if enemy_sprites:
        for enemy in enemy_sprites.sprites():
            if enemy.rect.colliderect(Joe.rect) and Joe.damaged == False:
                hurt_sound.play()
                if Joe.health == 1:
                    return True
                else:
                    Joe.damaged = True
                    Joe.health -= 1
                    Joe.notify(LIVES_LOST)
                    pygame.time.set_timer(joe_damage_timer, 500, 1)


def remove_bullet():
    if bullet_sprites:
        for bullet in bullet_sprites:
            bullet.erase(bullet_sprites)


def remove_enemies():
    for enemy in enemy_sprites.sprites():
        enemy.erase(enemy_sprites)


def animate_enemies():
    for sprite in enemy_sprites.sprites():
        sprite.animate()


def spawn_enemies():
    enemy_sprites.add(enemy_spawner.spawn_enemy(
        random.choice(enemy_group)))


def spawn_bullets(tecla):
    k = pygame.key.get_pressed()
    for keys in bullets_input_iterator:
        if k[keys] and keys == tecla:
            bullet_sprites.add(bullet_spawner.spawn_bullet(
                bullets_input_iterator[keys]))
            gun_sound.play()


def killed_enemy():
    if enemy_sprites and bullet_sprites:
        for enemy in enemy_sprites:
            for bullet in bullet_sprites:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.health -= 1
                    if enemy.health == 0:
                        enemy_sprites.remove(enemy)
                        Joe.notify(ENEMY_KILLED)
                    elif enemy.image_index == 0:
                        enemy.image = pygame.image.load("Art/cop1damage.png")
                    elif enemy.image_index == 1:
                        enemy.image = pygame.image.load("Art/cop2damage.png")
                    bullet_sprites.remove(bullet)


def game_restarted():
    for enemy in enemy_sprites:
        enemy_sprites.remove(enemy)
    for bullet in bullet_sprites:
        bullet_sprites.remove(bullet)
    Joe.rect.update(WIDTH / size_division, HEIGHT /
                    size_division, grid_size, grid_size)
    Joe.health = joe_health
    scoreboard.scores = 0
    joe_lives.index = 2
    pygame.time.set_timer(enemy_spawn_timer, enemy_spawn_ms)
