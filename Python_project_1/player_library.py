import pygame

BLUE  = (0, 0, 225)

class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        #loading the image 
        self.image = pygame.image.load("stewie1.png").convert()
        
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
 
        # -- Attributes
        # Set speed vector
        self.change_x = 0
        
    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        
        if self.rect.right > 800:
            self.rect.right = 800
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
        if self.rect.top < 0:
            self.rect.top = 0