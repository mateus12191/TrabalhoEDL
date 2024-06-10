import pygame
from Tools import Axe, Sword, Hoe

class Inventory:
    def __init__(self, game):
        self.game = game
        self.slot_size = 64
        self.slots = 5
        self.inventory = [Sword(), Hoe(), None, None, None]
        self.current_item = 0

    def place_inventory(self):
        # Desenhar os slots do inventário
        for i in range(self.slots):
            slot_rect = pygame.Rect(
                (self.slot_size + 10) * i + 10, 
                self.game.screen.get_height() - self.slot_size - 10, 
                self.slot_size, 
                self.slot_size
            )
            pygame.draw.rect(self.game.screen, (200, 200, 200), slot_rect)
            
            # Desenhar a borda do slot selecionado
            if i == self.current_item:
                pygame.draw.rect(self.game.screen, (255, 255, 0), slot_rect, 3)

            # Desenhar o item no slot
            if self.inventory[i]:
                item_image = self.inventory[i].image
                item_rect = item_image.get_rect(center=slot_rect.center)
                self.game.screen.blit(item_image, item_rect)

    def next_item(self):
        self.current_item = (self.current_item + 1) % self.slots

    def previous_item(self):
        self.current_item = (self.current_item - 1) % self.slots

    def get_current_item(self):
        return self.inventory[self.current_item]
    def action(self):
        self.inventory[self.current_item].action(self.game)


        
        