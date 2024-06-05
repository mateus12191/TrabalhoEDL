import pygame

class Zombie(pygame.sprite.Sprite):
    def __init__(self, player, x=100, y=100):
        super().__init__()
        self.image = pygame.Surface((64, 64))
        self.image.fill((0, 255, 0))  # Zumbi será verde
        self.rect = self.image.get_rect(center=(x, y))
        self.player = player

    def movement(self):
        # Calcula a direção do zumbi em relação ao jogador
        direction = pygame.math.Vector2(self.player.rect.center) - pygame.math.Vector2(self.rect.center)
        
        # Verifica se o vetor de direção não é zero antes de normalizar
        if direction.length_squared() > 0:
            direction.normalize()
            speed = 2  # Ajuste a velocidade conforme necessário
            self.rect.move_ip(direction * speed)
        else:
            pass

    def update(self, game):
        self.movement()

    def draw(self, screen, offset):
        screen.blit(self.image, (self.rect.x + offset[0], self.rect.y + offset[1]))
