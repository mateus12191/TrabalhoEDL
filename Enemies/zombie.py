import pygame
from Enemies.enemies import Enemy
class Zombie(Enemy):
    def movement(self):
         # Calcula a direção do zumbi em relação ao jogador
        direction = pygame.math.Vector2(self.game.player.rect.center) - pygame.math.Vector2(self.rect.center)
        
        # Verifica se o vetor de direção não é zero antes de normalizar
        if direction.length_squared() > 0:
            direction.normalize()
            speed = 1  # Velocidade de movimento do zumbi
            self.rect.move_ip(direction * speed * self.game.dt)
        
        # Verifica colisão com o jogador
        if pygame.sprite.spritecollide(self,self.game.playersprite,False,pygame.sprite.collide_mask):
            gameover = pygame.Surface((1920, 1080))
            gameover.fill('Blue')
            pygame.font.init()
            self.font = pygame.font.Font(None, 36)
            self.text = self.font.render('Game Over', True, 'White')
            self.game.screen.blit(self.text, (960, 540))