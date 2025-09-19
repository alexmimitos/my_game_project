import pygame
import random
import os
from classes.App import App

class Alien:
    def __init__(self, image):
        self.stepX = random.choice([1, -1])
        self.stepY = 1
        self.image = image
        self.rect = self.image.get_rect()

    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move_to_random(self):
        y = -random.randrange(0, 300)
        x = random.randrange(0, App.WIDTH - self.rect.width)
        self.move_to(x, y)

    def move_by(self):
        self.rect.x += self.stepX
        self.rect.y += self.stepY

    def check_if_bounce(self):
        if self.rect.x >= App.WIDTH - self.rect.width:
            self.stepX = -self.stepX
        if self.rect.x <= 0:
            self.stepX = -self.stepX

    def run(self, screen):
        self.move_by()
        self.check_if_bounce()
        screen.blit(self.image, self.rect)