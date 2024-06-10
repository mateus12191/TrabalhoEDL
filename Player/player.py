import pygame
from Tools.hoe import Hoe
from Tools.axe import Axe
from Player.inventory import Inventory

PLAYER_SPEED = 200
WIDTH, HEIGHT = 1920, 1080
class HealthBar:
    def __init__(self, game):
        self.game = game
        self.hearts = 4
        self.life = 8
        self.fullheart = pygame.image.load('Graphics\\fullheart.png')
        self.halfheart = pygame.image.load('Graphics\\halfheart.png')
        self.emptyheart = pygame.image.load('Graphics\\emptyheart.png')
        self.heart_width = 32
        self.heart_height = 32
        self.fullheart = pygame.transform.scale(self.fullheart, (self.heart_width, self.heart_height))
        self.halfheart = pygame.transform.scale(self.halfheart, (self.heart_width, self.heart_height))
        self.emptyheart = pygame.transform.scale(self.emptyheart, (self.heart_width, self.heart_height))
        self.fullheart_rect = self.fullheart.get_rect()
        self.halfheart_rect = self.halfheart.get_rect()
        self.emptyheart_rect = self.emptyheart.get_rect()

    def draw(self):
        x = 10  # X posição inicial para o primeiro coração
        y = 10  # Y posição inicial para o primeiro coração
        for i in range(self.hearts):
            if self.life >= (i + 1) * 2:
                self.game.screen.blit(self.fullheart, (x, y))
            elif self.life == (i * 2) + 1:
                self.game.screen.blit(self.halfheart, (x, y))
            else:
                self.game.screen.blit(self.emptyheart, (x, y))
            x += self.fullheart_rect.width + 5  # Ajuste de espaçamento entre os corações

        
class Player(pygame.sprite.Sprite):
    def __init__(self,game, x=960, y=540, sprite='Graphics/player_stand.png'):
        super().__init__()
        self.game=game
        self.standing_image = pygame.image.load(sprite).convert_alpha()
        self.healthbar=HealthBar(game)
        self.image = self.standing_image
        self.rect = self.image.get_rect(center=(x, y))
        self.mask=pygame.mask.from_surface(self.image)
        self.speed = PLAYER_SPEED
        self.inventory = Inventory(self.game)
        self.player_index = 0
        self.player_walk_images = [
            pygame.image.load('Graphics/player_walk_1.png').convert_alpha(),
            pygame.image.load('Graphics/player_walk_2.png').convert_alpha()
        ]
        self.animation_speed = 0.1
        self.is_moving = False

    def placeplayer(self, screen, offset):
        screen.blit(self.image, (self.rect.x + offset[0], self.rect.y + offset[1]))
        self.placeitem(screen, offset)

    def placeitem(self):
        current_item = self.inventory.get_current_item()
        current_item.rect.center=(self.rect.centerx+45,self.rect.centery)
        self.game.screen.blit(current_item.image,self.game.camera.apply(current_item))

    def getInput(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False  # Reset movement flag
        
        if keys[pygame.K_w]:
            self.movement(0, -self.speed)
            self.is_moving = True
        if keys[pygame.K_s]:
            self.movement(0, self.speed)
            self.is_moving = True
        if keys[pygame.K_a]:
            self.animation()
            self.movement(-self.speed, 0)
            self.is_moving = True
        if keys[pygame.K_d]:
            self.animation()
            self.movement(self.speed, 0)
            self.is_moving = True
        if keys[pygame.K_SPACE]:
            self.current_item = (self.current_item + 1) % len(self.inventory)
        if keys[pygame.K_1]:
            self.inventory.current_item=0
        if keys[pygame.K_2]:
            self.inventory.current_item=1

        if not self.is_moving:
            self.image = self.standing_image

    def movement(self, dx, dy):
        self.rect.x += dx * self.game.dt
        self.rect.y += dy * self.game.dt

    def animation(self):
        self.player_index += self.animation_speed
        if self.player_index >= len(self.player_walk_images):
            self.player_index = 0
        self.image = self.player_walk_images[int(self.player_index)]

    def update(self, *args):
        self.getInput()
        self.placeitem()
        self.healthbar.draw()
