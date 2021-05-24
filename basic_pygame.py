import pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

import random

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 1000

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((0, 0, 0))
        self.rect = self.surf.get_rect()
        self.surf.set_colorkey((225, 225, 225), RLEACCEL)
        self.surf = pygame.image.load(r"C:\Users\alvin\Desktop\Projects\Basic PyGame Program\cat_face.png").convert_alpha()
        self.surf = pygame.transform.scale(self.surf, (50, 50))

        self.rect = self.surf.get_rect()
 
    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(1, -1)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(1, 2)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-2, 1)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(1, 1)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 10))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect(
            center = (
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
        
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)


player = Player()

enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False 

        elif event.type == ADDENEMY:
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

    pressed_keys = pygame.key.get_pressed() 
    player.update(pressed_keys) 

    enemies.update()

    screen.fill((0, 0, 0))

    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)

    if pygame.sprite.spritecollideany(player, enemies):
        player.kill()
        running = False

    clock = pygame.time.Clock()
    pygame.display.flip()

    clock.tick(60)