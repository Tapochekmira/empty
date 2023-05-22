import pygame
from random import randint


class Dino:
    def __init__(self, image_path_1, image_path_2, image_path_3, image_path_4, height, jump_sound_path,
                 landing_sound_path,
                 crash_sound_path):
        self.image_1 = pygame.image.load(image_path_1)
        self.image_2 = pygame.image.load(image_path_2)
        self.image_3 = pygame.image.load(image_path_3)
        self.image_4 = pygame.image.load(image_path_4)
        self.image_1.set_colorkey(pygame.Color('white'))
        self.image_2.set_colorkey(pygame.Color('white'))
        self.image_3.set_colorkey(pygame.Color('white'))
        self.image_4.set_colorkey(pygame.Color('white'))
        x = self.image_1.get_size()[0]
        self.y = height // 2 - self.image_2.get_size()[1]
        self.rect = self.image_2.get_rect(topleft=(x, self.y))
        self.speed = 0
        self.max_speed = -10
        self.dy = 0
        self.jump_sound = pygame.mixer.Sound(jump_sound_path)
        self.landing_sound = pygame.mixer.Sound(landing_sound_path)
        self.crash_sound = pygame.mixer.Sound(crash_sound_path)
        self.touch = False
        self.crash = False
        self.timer = 0
        self.down = False

    def draw(self, sc):
        if self.timer < 5 or self.dy != 0:
            if self.down:
                sc.blit(self.image_3, self.rect)
            else:
                sc.blit(self.image_1, self.rect)
        elif self.timer < 10:
            if self.down:
                sc.blit(self.image_4, self.rect)
            else:
                sc.blit(self.image_2, self.rect)
        else:
            if self.down:
                sc.blit(self.image_3, self.rect)
            else:
                sc.blit(self.image_1, self.rect)
            self.timer = 0
        self.timer += 1

    def sat_down(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN] and not self.dy:
            self.down = True
            self.rect = self.image_3.get_rect(bottomleft=self.rect.bottomleft)
        else:
            self.rect = self.image_1.get_rect(bottomleft=self.rect.bottomleft)
            self.down = False

    def check_jump_possibility(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and not self.dy:
            self.jump_sound.play()
            return True
        return False

    def jump(self):
        if self.check_jump_possibility():
            self.touch = True
            self.dy = 0.35
            self.speed = self.max_speed
        self.rect.y += self.speed
        self.speed += self.dy
        if self.rect.top >= self.y:
            if self.touch:
                self.landing_sound.play()
                self.touch = False
            self.dy = 0
            self.speed = 0


class Ground:
    def __init__(self, image_path, y, speed):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color('white'))
        self.rect = self.image.get_rect(topleft=(0, y))
        self.speed = speed

    def draw(self, sc):
        sc.blit(self.image, self.rect)

    def move(self, width):
        self.rect.x -= self.speed
        if self.rect.right <= width:
            self.rect.x = 0


class Cloud:
    def __init__(self, image_path, x, y, speed, ):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color('white'))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed

    def draw(self, sc):
        sc.blit(self.image, self.rect)

    def move(self, width, max_height):
        if self.rect.right < 0:
            self.rect.left = randint(width, width + 100)
            self.rect.top = randint(0, max_height)
        else:
            self.rect.x -= self.speed


class Obstacle:
    def __init__(self, speed, image_path, x, dino_bottom, flying):
        self.image = pygame.image.load(image_path)
        self.image.set_colorkey(pygame.Color('white'))
        y = dino_bottom - self.image.get_size()[1] + 20
        if flying:
            y -= 75
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = speed
        self.flying = flying

    def draw(self, sc):
        sc.blit(self.image, self.rect)

    def move(self):
        self.rect.x -= self.speed
