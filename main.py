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
        self.zombie = Zombie(self.player)
        self.allsprites.add(self.zombie)
        self.offset_x=0
        self.offset_y=0
        self.tile_images = {
            0: pygame.image.load('Graphics/tile1.png').convert(),
            1: pygame.image.load('Graphics/tile2.png').convert(),
            2: pygame.image.load('Graphics/tile3.png').convert(),
            3: pygame.image.load('Graphics/tile4.png').convert(),
            4: self.create_colored_tile(BROWN)
        }
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

        self.map_surface = pygame.Surface((len(self.map_data[0]) * TILESIZE, len(self.map_data) * TILESIZE))
        self.load_map()
    def drawCoord(self):
        text_surface=self.font.render(f'Playerpos: [{self.player.rect.centerx,self.player.rect.centery}]',True,'White')
        text_surface1=self.font.render(f'Offset: [{self.offset_x,self.offset_y}]',True,'White')
        self.screen.blit(text_surface,(1645,0))
        self.screen.blit(text_surface1,(0,1055))
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

    def draw_visible_map(self, offset_x, offset_y):
        start_col = max(0, -offset_x // TILESIZE)
        end_col = min(len(self.map_data[0]), (WIDTH - offset_x) // TILESIZE + 1)
        start_row = max(0, -offset_y // TILESIZE)
        end_row = min(len(self.map_data), (HEIGHT - offset_y) // TILESIZE + 1)

        for i in range(start_row, end_row):
            for j in range(start_col, end_col):
                tile_value = self.map_data[i][j]
                if tile_value in self.tile_images:
                    self.screen.blit(self.tile_images[tile_value], (j * TILESIZE + offset_x, i * TILESIZE + offset_y))

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

            self.offset_x,  self.offset_y = self.player.calculate_offset(self.map_surface.get_width(), self.map_surface.get_height())

            self.draw_visible_map(self.offset_x, self.offset_y)

            if self.grid:
                self.drawGrid()

            self.playersprite.update(self)
            self.drawCoord()
            pygame.display.update()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()
import pygame
from Tools.hoe import Hoe
from Tools.axe import Axe
