import pygame


class Command:
    def execute(self):
        raise NotImplemented


class Up(Command):
    def execute(actor):
        actor.up()


class Down(Command):
    def execute(actor):
        actor.down()


class Left(Command):
    def execute(actor):
        actor.left()


class Right(Command):
    def execute(actor):
        actor.right()


controls = {
    pygame.K_w: Up,
    pygame.K_s: Down,
    pygame.K_a: Left,
    pygame.K_d: Right
}


class InputHandler:

    def handle_input_move(self):

        pressed = pygame.key.get_pressed()

        for key in controls:
            if pressed[key]:
                return controls[key]
