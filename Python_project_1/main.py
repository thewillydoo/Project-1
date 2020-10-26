import pygame
import random
 
# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (0, 0, 225)
GREEN = (0, 255, 0)

# Initialize Pygame
pygame.init()
#Window name
pygame.display.set_caption("Giant Chicken Shooter")
# Set height and width of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
# class Game():

#Get the size of the image
image = pygame.image.load("giantchicken.gif")
 
print(image.get_size()) # you can get size




class Chicken(pygame.sprite.Sprite):
    """
    This class represents the ball.
    It derives from the "Sprite" class in Pygame.
    """
 
    def __init__(self, color, width, height):
        """ Constructor. Pass in the color of the block,
        and its size. """
 
        # Call the parent class (Sprite) constructor
        super().__init__()

        #loading the image 
        self.chicken_sprite = pygame.image.load("giantchicken.gif").convert()
        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # image.
        # Update the position of this object by setting the values
        # of rect.x and rect.y
        self.rect = self.image.get_rect()

    
 
class Player(pygame.sprite.Sprite):
    """ The class is the player-controlled sprite. """
 
    # -- Methods
    def __init__(self):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        #loading the image 
        self.player_sprite = pygame.image.load("stewie1.png").convert()
        
 
        # Set height, width
        self.image = pygame.Surface([68, 68])
        self.image.fill(BLUE)
 
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

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
 
        self.image = pygame.Surface([4, 10])
        self.image.fill(BLACK)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3
 
    




#Looping the stars 
star_list = []
for i in range(50):
    star_x = random.randrange(0, 800)
    star_y = random.randrange(0, 600)
    star_list.append([star_x, star_y])

# This is a list of 'sprites.' Each block in the program is
# added to this list. The list is managed by a class called 'Group.'
chicken_list = pygame.sprite.Group()


# This is a list of every sprite. 
# All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
for i in range(25):
    # This represents a block
    chicken = Chicken(WHITE, 20, 15)
 
    # Set a random location for the block
    chicken.rect.x = random.randrange(screen_width - 20)
    chicken.rect.y = random.randrange(screen_height - 15)
 
    # Add the block to the list of objects
    chicken_list.add(chicken)
    all_sprites_list.add(chicken)


# Create a player block
player = Player()
# screen.blit(player_sprite, x, y)
all_sprites_list.add(player)





# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
score = 0
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get(): 
        # to close the window
        if event.type == pygame.QUIT: 
            done = True

        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-4, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(4, 0)
 
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(4, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-4, 0)
            
    # Setting the background
    screen.fill(BLACK)

    #Process each star in the list
    for i in range(len(star_list)):
 
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, star_list[i], 3)
 
        # Move the snow flake down one pixel
        star_list[i][1] += 2
 
        # If the snow flake has moved off the bottom of the screen
        if star_list[i][1] > 600:
            # Reset it just above the top
            star_y = random.randrange(-50, -10)
            star_list[i][1] = star_y
            # Give it a new x position
            star_x = random.randint(0, 800)
            star_list[i][0] = star_x


    all_sprites_list.update()
    
    # See if the player block has collided with anything.
    blocks_hit_list = pygame.sprite.spritecollide(player, chicken_list, True)

 
    # Check the list of collisions.
    for block in blocks_hit_list:
        score += 1
        print(score)
    
    

    
    # Draw all the sprites
    all_sprites_list.draw(screen)
    # draw stewie's sprite
    screen.blit(player.player_sprite,[player.rect.x, player.rect.y])
    # draw giantchicken's sprite
    screen.blit(chicken.chicken_sprite,[chicken.rect.x, chicken.rect.y])
    # Drawing Score on the canvas
    font = pygame.font.SysFont('Calibri', 25, True, False)
    text = font.render("Score: " + str(score), True, WHITE)
    screen.blit(text, [10, 570])
    # Update the screen
    pygame.display.flip()
 
    # Limit to 60 frames per second
    clock.tick(60)
 
pygame.quit()

#Things to do:
# - Create a timer
# - Search how to remove the png background/turn the background black
# - How to change the width and height of the image
# - Check the collisions of the image so that the whole image gets detected when it makes contact with a block 
# - Remove the blocks and create an array of 'Chickens' that come from the top of the screen 
# - Make bullets
# - Make them be able to shoot on an event key
# - Check the collisions of the bullets and if it hits the 'Chicken' images
# - Create levels for the game so that it gets progressively harder
# - Review all the code so I understand it when I talk to Veldkamp
# - Don't act sus