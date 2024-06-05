import pygame
from Tools.hoe import Hoe
from Tools.axe import Axe

PLAYER_SPEED = 3
WIDTH, HEIGHT = 1920, 1080

class Player(pygame.sprite.Sprite):
    def __init__(self, x=960, y=540, sprite='Graphics/player_stand.png'):
        super().__init__()
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = PLAYER_SPEED
        self.inventory = [Hoe(), Axe()]
        self.current_item = 0

    def gettool(self):
        return self.inventory[self.current_item]

    def placeplayer(self, screen, offset):
        screen.blit(self.image, (self.rect.x + offset[0], self.rect.y + offset[1]))
        self.placeitem(screen, offset)

    def placeitem(self, screen, offset):
        current_item = self.gettool()
        item_x, item_y = self.rect.midright
        current_item.rect.midleft = (item_x + offset[0] - 10, item_y + offset[1])
        screen.blit(current_item.image, current_item.rect)

    def getInput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.movement(0, -self.speed)
        if keys[pygame.K_s]:
            self.movement(0, self.speed)
        if keys[pygame.K_a]:
            self.movement(-self.speed, 0)
        if keys[pygame.K_d]:
            self.movement(self.speed, 0)
        if keys[pygame.K_SPACE]:  # Use espaço ou outra tecla para alternar entre ferramentas
            self.current_item = (self.current_item + 1) % len(self.inventory)

    def movement(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy

    def get_position(self):
        return self.rect.center

    def calculate_offset(self, map_width, map_height):
        offset_x = WIDTH // 2 - self.rect.centerx
        offset_y = HEIGHT // 2 - self.rect.centery

        offset_x = min(0, offset_x)
        offset_x = max(WIDTH - map_width, offset_x)
        offset_y = min(0, offset_y)
        offset_y = max(HEIGHT - map_height, offset_y)

        return offset_x, offset_y

    def update(self, game):
        self.getInput()
        offset = self.calculate_offset(game.map_surface.get_width(), game.map_surface.get_height())
        self.placeplayer(game.screen, offset)
