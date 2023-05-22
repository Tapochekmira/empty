import pygame


def increase_score(score, fps, ground_speed):
    if ground_speed:
        score += fps / 200
    return score


def check_start(ground_speed):
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE] and not ground_speed:
        return True
    return False


def check_game_over(dino, current_obstacles):
    if dino.rect.collidelist(current_obstacles) != -1:
        if dino.crash:
            dino.crash_sound.play()
            dino.crash = False
        return True
    return False



