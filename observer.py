import pygame

ENEMY_KILLED = "enemy_was_killed"
LIVES_LOST = "life_was_lost"


class Observer:
    def __init__(self):
        self.events = {}

    def register(self, event, event_handler):
        if event not in self.events:
            self.events[event] = []
        self.events[event].append(event_handler)

    def notify(self, event):
        for event_handler in self.events[event]:
            event_handler()
