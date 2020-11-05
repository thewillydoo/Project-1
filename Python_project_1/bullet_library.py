import pygame

RED   = (255, 0, 0)
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([4, 15])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3