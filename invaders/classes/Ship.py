import pygame
import random
import os
from classes.App import App

class Ship:
    def __init__(self, image):
        self.step = 1.5
        self.top = 200
        self.image = image
        self.rect = self.image.get_rect()  #x, y, width, height

    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def move_by(self):
        self.rect.x += self.step
        self.rect.y += self.step

    def check_if_collision(self, aliens):
        for alien in aliens:
            if self.rect.colliderect(alien.rect):
                App.scene = 2
                break

    def check_if_side(self):
        keys = pygame.key.get_pressed()  # Get the current state of all keys
        if keys[pygame.K_UP]:  # Check if the UP key is pressed
            if self.rect.y > App.HEIGHT - self.top:
                self.rect.y -= self.step
        if keys[pygame.K_DOWN]:  # Check if the DOWN key is pressed
            if self.rect.y < App.HEIGHT - self.rect.height:
                self.rect.y += self.step
        if keys[pygame.K_LEFT]:  # Check if the UP key is pressed
            if self.rect.x > 0:
                self.rect.x -= self.step
        if keys[pygame.K_RIGHT]:  # Check if the DOWN key is pressed
            if self.rect.x < App.WIDTH - self.rect.width:
                self.rect.x += self.step


    def run(self, screen, aliens):
        self.check_if_side()
        self.check_if_collision(aliens)
        screen.blit(self.image, self.rect)