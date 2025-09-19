import pygame as pg
from classes.App import App
from classes.Ship import  Ship
from classes.Alien import  Alien
from classes.Missile import  Missile

pg.init()

#  screen
screen = pg.display.set_mode((App.WIDTH, App.HEIGHT))
pg.display.set_caption(App.title)

# load fonts
font = pg.font.Font("fonts/FreckleFace-Regular.ttf", 70)

# create start button
start_game = font.render("Start Game", True, "pink")
start_game_rect = start_game.get_rect(center=(App.WIDTH/2, App.HEIGHT/2))

# create game_over button
game_over = font.render("Game Over", True, "red")
game_over_rect = game_over.get_rect(center=(App.WIDTH/2, App.HEIGHT/2 + 200))

# bg image
bg_image = pg.image.load("images/bg.webp").convert_alpha()

# create ship
ship_image = pg.image.load("images/ship.png").convert_alpha()
ship = Ship(ship_image)
ship.move_to(App.WIDTH/2 - ship.rect.width/2, App.HEIGHT - ship.rect.height)

# create aliens
aliens = []
alien_image = pg.image.load("images/invader.png").convert_alpha()
for i in range(5):
    alien = Alien(alien_image)
    alien.move_to_random()
    aliens.append(alien)

# create missile
miss_image = pg.image.load("images/missile.png").convert_alpha()
miss = Missile(miss_image)
miss.move_to(App.WIDTH/2 - ship.rect.width/2, App.HEIGHT - ship.rect.height)

miss.is_on = False
miss.move_to(ship.rect.x + ship.rect.width / 2 - miss.rect.width / 2, ship.rect.y)


clock = pg.time.Clock()
is_on = True
while is_on:
    clock.tick(App.fps) # FPS
    screen.blit(bg_image, (0,0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            is_on = False
        if event.type == pg.MOUSEBUTTONUP:
            pos = pg.mouse.get_pos()
            if start_game_rect.collidepoint(pos):
                # todo
                App.scene = 1
                ship.move_to(App.WIDTH/2 - ship.rect.width/2, App.HEIGHT - ship.rect.height)
                aliens.clear()
                for i in range(5):
                    alien = Alien(alien_image)
                    alien.move_to_random()
                    aliens.append(alien)

                miss.is_on = False
                miss.move_to(ship.rect.x + ship.rect.width / 2 - miss.rect.width / 2, ship.rect.y)
            else:
                print("not clicked")


    if App.scene == 0:
        screen.blit(start_game, start_game_rect)
        pg.draw.rect(screen, "pink", start_game_rect, 2)
    elif App.scene == 1:
        ship.run(screen, aliens)
        miss.run(screen, ship, aliens)
        for alien in aliens: alien.run(screen)

        if len(aliens) == 0:
            App.scene = 2
    else:
        screen.blit(game_over, game_over_rect)
        pg.draw.rect(screen, "red", game_over_rect, 2)

        screen.blit(start_game, start_game_rect)
        pg.draw.rect(screen, "blue", start_game_rect, 2)

    pg.display.update()
# quit app
pg.quit()
