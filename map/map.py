import pygame
import json
WIDTH, HEIGHT = 1920, 1080
TILESIZE = 64
BROWN = (139, 69, 19)
class Map:
    def __init__(self,game):
        self.tile_images = {
            0: pygame.image.load('Graphics/tile1.png').convert(),
            1: pygame.image.load('Graphics/tile2.png').convert(),
            2: pygame.image.load('Graphics/tile3.png').convert(),
            3: pygame.image.load('Graphics/tile4.png').convert(),
            4: self.create_colored_tile(BROWN)
        }
        self.map_data=self.load_map_data()
        self.map_surface= pygame.Surface((len(self.map_data[0]) * TILESIZE, len(self.map_data) * TILESIZE))
        self.game=game
      

    
    def create_colored_tile(self, color):
        tile = pygame.Surface((TILESIZE, TILESIZE))
        tile.fill(color)
        return tile

    def load_map_data(self):
        with open('obj.json', 'r') as file:
            data = json.load(file)
        return data
    def load_map(self):
        for i, row in enumerate(self.map_data):
            for j, tile_value in enumerate(row):
                if tile_value in self.tile_images:
                    self.map_surface.blit(self.tile_images[tile_value], (j * TILESIZE, i * TILESIZE))
    def draw_visible_map(self, offset_x, offset_y):
        start_col = max(0, -offset_x // TILESIZE)
        end_col = min(len(self.map_data[0]), (WIDTH - offset_x) // TILESIZE + 1)
        start_row = max(0, -offset_y // TILESIZE)
        end_row = min(len(self.map_data), (HEIGHT - offset_y) // TILESIZE + 1)

        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                tile_value = self.map_data[i][j]
                if tile_value in self.tile_images:
                    self.game.screen.blit(self.tile_images[tile_value], (j * TILESIZE + offset_x, i * TILESIZE + offset_y))

