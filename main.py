import pygame
from pytmx.util_pygame import load_pygame
from camera import Camera
from Player.player import Player
from Player.player import Inventory
from Enemies.zombie import Zombie
import sqlite3
from db import database
from map.map import Map
from sys import exit
import json

WIDTH, HEIGHT = 1920, 1080
TILESIZE = 64
LIGHTGREY = (100, 100, 100)
BROWN = (139, 69, 19)

import pygame
import json

WIDTH, HEIGHT = 1920, 1080
TILESIZE = 64
BROWN = (139, 69, 19)

def update_sprites(sprites):
    list(map(lambda sprite: sprite.update(), sprites))

class Game:
    TILESIZE = 64

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Jogo")
        self.clock = pygame.time.Clock()
        self.map = Map(self)
        self.player = Player(self)
        self.player.inventory = Inventory(self)
        self.allsprites = pygame.sprite.Group()
        self.playersprite = pygame.sprite.GroupSingle(self.player)
        self.enemy = Zombie(self)
        self.allsprites.add(self.enemy)
        self.dt = 0
        self.grid = False
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)

        self.camera = Camera(self)  # Adicionando a câmera

        # Criar a tabela do jogador no banco de dados
        database.create_player_table()

        # Carregar os dados do jogador
        self.load_player_data()

    def drawCoord(self):
        text_surface = self.font.render(f'Playerpos: [{self.player.rect.centerx}, {self.player.rect.centery}]', True, 'White')
        text_surface1 = self.font.render(f'Offset: [{self.camera.camera.x}, {self.camera.camera.y}]', True, 'White')
        self.screen.blit(text_surface, (1645, 0))
        self.screen.blit(text_surface1, (0, 1055))

    def drawGrid(self):
        draw_line = lambda start, end: pygame.draw.line(self.screen, LIGHTGREY, start, end)
        list(map(draw_line, [(x, 0) for x in range(0, WIDTH, TILESIZE)], [(x, HEIGHT) for x in range(0, WIDTH, TILESIZE)]))
        list(map(draw_line, [(0, y) for y in range(0, HEIGHT, TILESIZE)], [(WIDTH, y) for y in range(0, HEIGHT, TILESIZE)]))

    def startmenu(self):
        startmen = pygame.Surface((1920, 1080))

    def load_player_data(self):
        player_data = database.get_player_data('Jogador')
        if player_data:
            pos_x, pos_y, health = player_data
            self.player.rect.centerx = pos_x
            self.player.rect.centery = pos_y
            self.player.healthbar.life = health

    def save_player_data(self):
        name = 'Jogador'
        pos_x = self.player.rect.centerx
        pos_y = self.player.rect.centery
        health = self.player.healthbar.life
        database.insert_player_data(name, pos_x, pos_y, health)

    def run(self):
        global game_state
        game_state = {'running': True}

        while game_state['running']:
            self.dt = self.clock.tick(60) / 1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_state['running'] = False
                    self.save_player_data()
                    pygame.quit()
                    exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.player.inventory.action()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_g:
                        self.grid = not self.grid

            self.camera.update()  # Atualizar a câmera

            self.screen.fill((0, 0, 0))  # Limpar a tela
            self.map.draw_visible_map(self.camera.camera.x, self.camera.camera.y)  # Desenhar o mapa visível
            
            # Usar update_sprites para atualizar todos os sprites
            update_sprites(self.allsprites)
            update_sprites(self.playersprite)

            # Desenhar todos os sprites em relação à câmera
            for sprite in self.allsprites:
                self.screen.blit(sprite.image, self.camera.apply(sprite))
            for sprite in self.playersprite:
                self.screen.blit(sprite.image, self.camera.apply(sprite))

            self.drawCoord()

            if self.grid:
                self.drawGrid()
            self.player.inventory.place_inventory()

            pygame.display.update()  # Atualizar a tela


if __name__ == '__main__':
    game = Game()
    game.run()
