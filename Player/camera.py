import pygame
WIDTH, HEIGHT = 1920, 1080
TILESIZE = 64
LIGHTGREY = (100, 100, 100)
BROWN = (139, 69, 19)
class Camera:
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height

    def apply(self, entity):
        return entity.rect.move(self.camera.topleft)

    def apply_rect(self, rect):
        return rect.move(self.camera.topleft)

    def update(self, target):
        x = -target.rect.centerx + int(WIDTH / 2)
        y = -target.rect.centery + int(HEIGHT / 2)

        x = min(0, x)  # Limit scrolling to the left
        y = min(0, y)  # Limit scrolling to the top
        x = max(-(self.width - WIDTH), x)  # Limit scrolling to the right
        y = max(-(self.height - HEIGHT), y)  # Limit scrolling to the bottom

        self.camera = pygame.Rect(x, y, self.width, self.height)
