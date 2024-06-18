import pygame
from abc import ABC,abstractmethod
class Enemy(pygame.sprite.Sprite,ABC):
    def __init__(self, game, x=100, y=100):
        super().__init__()
        self.game = game
        self.image = pygame.Surface((64, 64))
        self.image.fill((0, 255, 0))  # Zumbi será verde
        self.rect = self.image.get_rect(center=(x, y))
        self.mask=pygame.mask.from_surface(self.image)
        self.player = game.player
    @abstractmethod
    def movement(self):
        pass
       
            
    def addenemy(self):
        self.game.allsprites.add(self)

    def update(self):
        self.movement()