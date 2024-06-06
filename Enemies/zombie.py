import pygame
class Zombie(pygame.sprite.Sprite):
    def __init__(self,player, x=100, y=100):
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
            speed = 1  # Velocidade de movimento do zumbi
            self.rect.move_ip(direction * speed)
        else:
            pass

    def placezombie(self,screen):
        screen.blit(self.image,self.rect)
    

    def update(self,game):
        self.placezombie(game.screen)
        self.movement()
