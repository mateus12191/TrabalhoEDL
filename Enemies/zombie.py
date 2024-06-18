import pygame
from Enemies.enemies import Enemy
class Zombie(Enemy):
    def movement(self):
        # Calcula a direção do zumbi em relação ao jogador
        player_center = pygame.math.Vector2(self.game.player.rect.center)
        zombie_center = pygame.math.Vector2(self.rect.center)
        direction = player_center - zombie_center

        # Normaliza o vetor de direção e multiplica pela velocidade constante
        if direction.length_squared() > 0:  # Evita divisão por zero
            direction = direction.normalize()
            speed = 180  # Velocidade constante do zumbi (pixels por segundo)
            displacement = direction * speed * self.game.dt
            self.rect.move_ip(displacement)

        # Verifica colisão com o jogador
        if pygame.sprite.spritecollide(self, self.game.playersprite, False, pygame.sprite.collide_mask):
            print("Collision Detected: Game Over")
            gameover = pygame.Surface((1920, 1080))
            gameover.fill('Blue')
            pygame.font.init()
            self.font = pygame.font.Font(None, 36)
            self.text = self.font.render('Game Over', True, 'White')
            self.game.screen.blit(self.text, (960, 540))





