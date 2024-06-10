import pygame
from pytmx.util_pygame import load_pygame
from camera import Camera  
from Player.player import Player
from Enemies.zombie import Zombie
from map.map import Map
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
        self.map=Map(self)
        self.player = Player(self)
        self.allsprites = pygame.sprite.Group()
        self.playersprite = pygame.sprite.GroupSingle(self.player)
        self.enemy=Zombie(self)
        self.allsprites.add(self.enemy)
        self.dt=0
        self.grid = False
        pygame.font.init()
        self.font = pygame.font.Font(None, 36)


        self.camera = Camera(self)  # Adicionando a câmera

    def drawCoord(self):
        text_surface = self.font.render(f'Playerpos: [{self.player.rect.centerx}, {self.player.rect.centery}]', True, 'White')
        text_surface1 = self.font.render(f'Offset: [{self.camera.camera.x}, {self.camera.camera.y}]', True, 'White')
        self.screen.blit(text_surface, (1645, 0))
        self.screen.blit(text_surface1, (0, 1055))

    def drawGrid(self):
        for x in range(0, WIDTH, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))
    def startmenu(self):
        startmen=pygame.Surface((1920,1080))
        

    def run(self):
     self.run = True
     while self.run:
        self.dt = self.clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.player.inventory.action()
            if event.type==pygame.KEYDOWN:
                if event.key== pygame.K_g:
                    self.grid= not self.grid
        


        self.camera.update()  # Atualizar a câmera

        self.screen.fill((0, 0, 0))  # Limpar a tela
        self.map.draw_visible_map(self.camera.camera.x, self.camera.camera.y)  # Desenhar o mapa visível
        self.playersprite.update(self)  # Atualizar o jogador
        self.allsprites.update()  # Atualizar todos os sprites

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
