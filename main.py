import pygame
from pytmx.util_pygame import load_pygame  
from Player.player import Player
from Enemies.zombie import Zombie
from sys import exit
import json

WIDTH, HEIGHT = 1920, 1080
TILESIZE = 64
LIGHTGREY = (100, 100, 100)
BROWN = (139, 69, 19)

class Game():
    TILESIZE = 64

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jogo")
        self.clock = pygame.time.Clock()
        self.player = Player()
        self.allsprites = pygame.sprite.Group()
        self.playersprite = pygame.sprite.GroupSingle(self.player)
        self.map_data = self.load_map_data()
        self.grid = False
        self.zombie=Zombie(self.player)
        self.allsprites.add(self.zombie)
        self.tile_images = {
            0: pygame.image.load('Graphics/tile1.png').convert(),
            1: pygame.image.load('Graphics/tile2.png').convert(),
            2: pygame.image.load('Graphics/tile3.png').convert(),
            3: pygame.image.load('Graphics/tile4.png').convert(),
            4: self.create_colored_tile(BROWN)
        }

        self.map_surface = pygame.Surface((len(self.map_data[0]) * TILESIZE, len(self.map_data) * TILESIZE))
        self.load_map()

    def create_colored_tile(self, color):
        tile = pygame.Surface((TILESIZE, TILESIZE))
        tile.fill(color)
        return tile

    def load_map(self):
        for i, row in enumerate(self.map_data):
            for j, tile_value in enumerate(row):
                if tile_value in self.tile_images:
                    self.map_surface.blit(self.tile_images[tile_value], (j * TILESIZE, i * TILESIZE))

    def load_map_data(self):
        with open('obj.json', 'r') as file:
            data = json.load(file)
        return data

    def drawGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def run(self):
        self.run = True
        while self.run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.player.gettool().action(self)

            keys = pygame.key.get_pressed()
            if keys[pygame.K_1]:
                self.grid = not self.grid


            offset_x, offset_y = self.player.calculate_offset(self.map_surface.get_width(), self.map_surface.get_height())

            self.screen.blit(self.map_surface, (offset_x, offset_y))

            if self.grid:
                self.drawGrid()

            self.playersprite.update(self)
            self.zombie.update(self)




            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()