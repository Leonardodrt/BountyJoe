
import pygame
from pygame import *
from entities import *


pygame.init()


# DEPOIS COLOCAR AUDIO

running = True

# game loop
while running:

    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # spawn bullets
            if game_active:
                spawn_bullets(event.key)
            else:
                game_active = True
                game_restarted()
        if event.type == enemy_spawn_timer:
            # spawn enemies with timer
            spawn_enemies()
        if event.type == enemy_animate_timer:
            # animate enemies between 2 simple sprites with timer
            animate_enemies()
        if event.type == enemy_delete_timer and enemy_sprites:
            # delete out of screen enemies
            remove_enemies()
        if event.type == joe_damage_timer:
            # timer for spacing damage taken (so the player doesn't take damage every clock.tick if he collides)
            Joe.damaged = False
        if event.type == joe_animate_timer:
            # timer for animating Joe
            Joe.switch_index()

    # secondary game loop
    if game_active:

        # draw and update sprites

        sprites.draw(screen)
        sprites.update()
        bullet_sprites.draw(screen)
        bullet_sprites.update()
        enemy_sprites.draw(screen)
        enemy_sprites.update()

        # damage taken and game lost
        if lose():
            game_active = False
        # delete out of screen bullets
        remove_bullet()
        # kill or damage enemy
        killed_enemy()

    else:

        main_menu.draw(screen)

    display.update()
    clock.tick(30)
