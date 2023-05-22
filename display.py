from random import randint

import pygame
from classes import Cloud


def draw_world(sc, ground, clouds, score, width):
    sc.fill(pygame.Color('white'))
    ground.draw(sc)
    draw_clouds(clouds, sc)
    draw_score(sc, score, width)


def create_clouds(cloud_count, width, max_height, image_path, speed):
    clouds = []
    for _ in range(cloud_count):
        x = randint(width, width * 2)
        y = randint(0, max_height)
        clouds.append(Cloud(image_path, x, y, speed))
    return clouds


def draw_clouds(clouds, sc):
    for cloud in clouds:
        cloud.draw(sc)


def draw_score(sc, score, width):
    score = int(score)
    zero_count = 5 - len(str(score))
    zeros = '0' * zero_count
    score = f'{zeros}{score}'

    font = pygame.font.SysFont(None, 30)
    text = font.render(score, True, pygame.Color('Grey'))
    sc.blit(text, (width - 70, 20))


def add_background_music(file_path):
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)