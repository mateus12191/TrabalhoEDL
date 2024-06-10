import pygame
from pygame import Rect
WIDTH, HEIGHT = 1920, 1080
TILESIZE = 64
class Camera:
    def __init__(self, game):
        self.game = game
        self.width = WIDTH
        self.height = HEIGHT
        self.camera = Rect(0, 0, self.width, self.height)

    def update(self):
        offset_x = WIDTH // 2 - self.game.player.rect.centerx
        offset_y = HEIGHT // 2 - self.game.player.rect.centery

        offset_x = min(0, offset_x)
        offset_x = max(WIDTH - self.game.map.map_surface.get_width(), offset_x)
        offset_y = min(0, offset_y)
        offset_y = max(HEIGHT - self.game.map.map_surface.get_height(), offset_y)
        
        self.camera = Rect(offset_x, offset_y, self.width, self.height)

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_offset(self, x, y):
        return x + self.camera.x, y + self.camera.y
