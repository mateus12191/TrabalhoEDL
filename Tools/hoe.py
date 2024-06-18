import pygame

class Hoe(pygame.sprite.Sprite):
    def __init__(self,game):
        super().__init__()
        self.game=game
        self.player=game.player
        self.image = pygame.image.load('Graphics/hoe.jpg')
        self.rect = self.image.get_rect()

    def action(self, game):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        tile_x = mouse_x // game.TILESIZE
        tile_y = mouse_y // game.TILESIZE

        if (abs((game.player.rect.centerx // game.TILESIZE) - tile_x) <= 1 and
            abs((game.player.rect.centery // game.TILESIZE) - tile_y) <= 1):
            if 0 <= tile_y < len(game.map.map_data) and 0 <= tile_x < len(game.map.map_data[0]):
                if game.map.map_data[tile_y][tile_x] in [0, 1, 2, 3]:
                    game.map.map_data[tile_y][tile_x] = 4
                    game.map.map_surface.blit(game.map.tile_images[4], (tile_x * game.TILESIZE, tile_y * game.TILESIZE))
    def placeitem(self):
        self.rect=(self.player.rect.centerx+45,self.player.rect.centery)
        self.game.screen.blit(self.image,self.game.camera.apply(self.rect))