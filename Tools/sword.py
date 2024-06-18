import pygame
class Sword(pygame.sprite.Sprite):
    def __init__(self,game) -> None:
        super().__init__()
        self.sword=pygame.image.load('Graphics\\sword_freeze.png')
        self.image=self.sword
        self.game=game
        self.player=self.game.player
        self.rect=self.image.get_rect()
        self.animationlist=[pygame.image.load('Graphics\\sword_animation_1.png'),pygame.image.load('Graphics\\sword_animation_2.png'),pygame.image.load('Graphics\\sword_animation_3.png')]
        self.animation_speed=0.1
        self.index=0
        self.mask=pygame.mask.from_surface(self.image)
    def placeitem(self):
        self.rect.topleft = (self.player.rect.centerx + 30, self.player.rect.centery+15)
        self.game.screen.blit(self.image, self.game.camera.apply(self))
    def animation(self):
      while self.index<=len(self.animationlist):
        self.index+=self.animation_speed
        if self.index>=len(self.animationlist):
            self.index=0

            return
        self.image=self.animationlist[int(self.index)]
    def action(self):
        self.animation()
        
        

        
    