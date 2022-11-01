import pygame
from pathlib import Path
from pygame.locals import *
import random

BASE_DIR = Path(__file__).parent

pygame.init()

screen_size = [360, 600]
screen = pygame.display.set_mode(screen_size)

background = pygame.image.load(BASE_DIR / 'background.png')

planets = [BASE_DIR/ 'planet_one.png', BASE_DIR/ 'planet_two.png',BASE_DIR/ 'planet_three.png']
p_index = 0
pp=random.shuffle(planets)

planet = pygame.image.load(BASE_DIR/'planet_one.png')
planet_x = 140
move_direction = 'right'
spaceship = pygame.image.load(BASE_DIR/'spaceship.png')
bullet = pygame.image.load(BASE_DIR/'bullet.png')
bullet_y = 500
fired = False
clock = pygame.time.Clock()

keep_alive = True


while keep_alive:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            keep_alive=False
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] == True:
        fired = True
        

    if move_direction == 'right':
        planet_x = planet_x + 5
        if planet_x == 300:
            move_direction = 'left'
    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = 'right'


    if fired is True:
        bullet_y = bullet_y - 5
        if bullet_y == 50:
            fired = False
            bullet_y = 500

    screen.blit(background, [0, 0])
    screen.blit(planet, [planet_x, 50])
    screen.blit(bullet, [180, bullet_y])
    screen.blit(spaceship, [160, 500])

    if bullet_y < 80 and planet_x > 120 and planet_x < 180:
        p_index=p_index + 1
        if p_index<len(planets):
            planet=pygame.image.load(random.choice(planets))
            planet_x=10
        else:
            print('BOOM')
            # keep_alive=False

    pygame.display.update()
    clock.tick(60)

