import pygame
import random
import chicken_library
import player_library
import bullet_library
import star_library

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED   = (255, 0, 0)
BLUE  = (0, 0, 225)
GREEN = (0, 255, 0)
# Set height and width of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# Load image
image = pygame.image.load("giantchicken.gif")
 
#size
print(image.get_size()) 

class Game(object):
    def __init__(self):
        self.score = 0
        self.lives = 1
        self.frame_count = 0
        self.frame_rate = 60
        self.game_over = False
        self.level = 1
        

        #---Sprite Lists 
        self.bullet_list = pygame.sprite.Group()
        self.chicken_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # Create a player 
        self.player = player_library.Player()
        self.all_sprites_list.add(self.player)

        # Add a bunch of chickens in a row
        for x in range(0, 701, 300):
            self.tempChicken = chicken_library.Chicken(x, 50)
            self.chicken_list.add(self.tempChicken)
            self.all_sprites_list.add(self.tempChicken)
    
  

    def process_events(self):
        for event in pygame.event.get(): 
        # to close the window
            if event.type == pygame.QUIT: 
                return True
            
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(-5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(5, 0)
                elif event.key == pygame.K_SPACE:
                # Fire a bullet if the user clicks the mouse button
                    bullet = bullet_library.Bullet()
                # Set the bullet so it is where the player is
                    bullet.rect.x =  self.player.rect.x + 30 
                    bullet.rect.y = self.player.rect.y
                # Add the bullet to the lists
                    self.all_sprites_list.add(bullet)
                    self.bullet_list.add(bullet)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.game_over:
                        self.__init__()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    self.player.changespeed(5, 0)
                elif event.key == pygame.K_RIGHT:
                    self.player.changespeed(-5, 0)
        
        return False

    def run_logic(self):
        if not self.game_over:
            # Move the sprites
            self.all_sprites_list.update()
            # Collisions
            # Calculate mechanics for each bullet
            for bullet in self.bullet_list:

                # See if the bullet hit a chicken
                chicken_hit_list = pygame.sprite.spritecollide(bullet, self.chicken_list, True)

                # For each chicken hit, remove the bullet and add to the score
                for block in chicken_hit_list:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    self.score += 1
                    print(self.score)

                # Remove the bullet if it flies up off the screen
                if bullet.rect.y < -10:
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
            # See if the player has collided with the chicken
            player_hit_list = pygame.sprite.spritecollide(self.player, self.chicken_list, True)
            # Check the list of collisions.
            for block in player_hit_list:
                self.score -= 1
                self.lives -= 1
                print("Score:", self.score)                    

    def level1(self):
        self.run_logic()

        offScreen = False
        for chicken in self.chicken_list:
            if chicken.offScreen():
                self.game_over = True

        if self.lives <= 0:
            self.game_over = True

        elif len(self.chicken_list) == 0:
            self.level += 1
            # Add more bunch of chickens in a row
            for x in range(0, 701, 100):
                self.tempChicken = chicken_library.Chicken(x, 0)
                self.chicken_list.add(self.tempChicken)
                self.all_sprites_list.add(self.tempChicken)
            for x in range(0, 701, 100):
                self.tempChicken = chicken_library.Chicken(x, -100)
                self.chicken_list.add(self.tempChicken)
                self.all_sprites_list.add(self.tempChicken)
        

    def level2(self):
        self.level1()

        if self.lives <= 0:
            self.game_over = True

        elif len(self.chicken_list) == 0:
            self.level += 1
            for x in range(0, 701, 100):
                self.tempChicken = chicken_library.Chicken(x, 0)
                self.chicken_list.add(self.tempChicken)
                self.all_sprites_list.add(self.tempChicken)
    
    def level3(self):
        self.level2()
        if self.lives <= 0:
            self.game_over = True
    
    def level4(self):
        self.level3()


    def display_frame(self, screen):
        screen.fill(BLACK)

        if self.game_over:
            # If game over is True:
            # Drawing Game Over
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Game Over", True, WHITE)
            text_rect = text.get_rect()
            text_x = screen.get_width() / 2 - text_rect.width / 2
            text_y = screen.get_height() / 2 - text_rect.height / 2
            screen.blit(text, [text_x, text_y])
            # 
        #if not self.gameover
        else:
            self.all_sprites_list.draw(screen)

            # Draw all the sprites
            self.all_sprites_list.draw(screen)
            # draw stewie's sprite
            screen.blit(self.player.image,[self.player.rect.x, self.player.rect.y])

            # Drawing Score on the canvas
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render("Score: " + str(self.score), True, WHITE)
            screen.blit(text, [10, 570])

            #Draw Timer
            # Calc total seconds
            total_seconds = self.frame_count // self.frame_rate
            # get min
            minutes = total_seconds // 60
            # get seconds
            seconds = total_seconds % 60
            # Use python string formatting to format in leading zeros
            output_string = "Time: {0:02}:{1:02}".format(minutes, seconds)
            font = pygame.font.SysFont('Calibri', 25, True, False)
            text = font.render(output_string, True, WHITE)
            screen.blit(text, [120, 570])
            self.frame_count += 1    

            #Draw Level
            text = font.render("Level: "+str(self.level), True, WHITE)
            screen.blit(text, [10, 540])

            #Draw lives 
            text = font.render("Lives: "+str(self.lives), True, WHITE)
            screen.blit(text, [700, 10])

        # Update the screen
        pygame.display.flip()

    def game_logic(self, screen):
        if self.level == 1:
            self.level1()
            self.display_frame(screen) 
        elif self.level == 2: 
            self.level2()
            self.display_frame(screen)
        elif self.level3 == 3:
            self.level3()
            self.display_frame(screen)
            




         
def main():
    #Initialize pygame 
    pygame.init()
    #Set up window
    screen = pygame.display.set_mode([screen_width, screen_height])

    #Window name
    pygame.display.set_caption("Chicken Shooter")

    #Create objects and set data
    done = False
    clock = pygame.time.Clock()

    frame_rate = 60

    game = Game()

    # -------- Main Program Loop -----------
    while not done:
        
        
        # Process events (keystrokes, mouse clicks, etc)
        done = game.process_events()
 
        # Update object positions, check for collisions
        game.game_logic(screen)
        

        # Limit to 60 frames per second
        clock.tick(frame_rate)

        pygame.display.flip()

    #Close window and exit
    pygame.quit()

# Call the main function, start up the game
if __name__ == "__main__":
    main()
