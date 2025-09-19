import pygame as pg
import random
import os
from classes.App import App

class Missile:
    def __init__(self, image):
        self.exploded_time = 0
        self.exploded_pos = None
        self.step = 2
        self.is_on = False
        self.image = image
        self.rect = self.image.get_rect()
        self.explosion_image = pg.image.load("images/boom.png").convert_alpha()
        self.explosion_sound = pg.mixer.Sound("sounds/impact.ogg")


    def move_to(self, x, y):
        self.rect.x = x
        self.rect.y = y

    def check_if_collision(self, aliens):
        for alien in aliens:
            if self.rect.colliderect(alien.rect):
                aliens.remove(alien)
                self.is_on = False
                self.exploded_pos = alien.rect.center  
                self.exploded_time = pg.time.get_ticks()  
                self.explosion_sound.play()
                break


    def move_by(self, aliens):
        self.rect.y -= self.step
        self.check_if_collision(aliens)
        if self.rect.y < -self.rect.height:
            self.is_on = False

    def check_if_space_pressed(self, ship):
        keys = pg.key.get_pressed()
        if keys[pg.K_SPACE]:
            self.rect.x = ship.rect.x + ship.rect.width/2 - self.rect.width/2
            self.rect.y = ship.rect.y
            self.is_on = True

    def run(self, screen, ship, aliens):
        self.check_if_space_pressed(ship)
        if  self.is_on:
            self.move_by(aliens)
            screen.blit(self.image, self.rect)
        if self.exploded_pos:
            boom_time = pg.time.get_ticks()
            if boom_time - self.exploded_time < 300:
                explosion_rect = self.explosion_image.get_rect(center=self.exploded_pos)
                screen.blit(self.explosion_image, explosion_rect)
            else:
                self.exploded_pos = None