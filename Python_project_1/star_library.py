import pygame
import random 

def stars():
    
    for i in range(50):
        star_x = random.randrange(0, 800)
        star_y = random.randrange(0, 600)
        star_list.append([star_x, star_y])


