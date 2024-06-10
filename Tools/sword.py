import pygame
class Sword(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image=pygame.image.load('Graphics\\sword_freeze.png')
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
    