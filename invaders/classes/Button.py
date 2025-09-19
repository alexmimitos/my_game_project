# import os
import pygame as pg

# root_path = os.path.dirname(os.path.abspath(__file__))
# print(root_path)

# font = pg.font.Font("fonts/FreckleFace-Regular.ttf", 70)

class Button:
    button = None
    def __init__(self, font, text = "", color = "black", x = 0, y = 0):
        self.text = text
        self.color = color
        self.button = font.render(self.text, True, self.color)
        self.rect = self.button.get_rect(center=(x, y))

    def is_clicked(self, point):
        return self.rect.collidepoint(point)

    def draw(self, screen):
        screen.blit(self.button, self.rect)
        pg.draw.rect(screen, self.color, self.rect, 2)