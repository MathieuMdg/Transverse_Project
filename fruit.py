import pygame
import math
import time
import random

G = 9.80665 #constante de gravitation
T = 0
angle = random.uniform(-math.pi, -math.pi / 2)
vitesse = random.randint(100, 150)


# Création d'une classe représentant les fruits
class Fruit(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__() #fais de la pasteque un sprite sur le jeu
        self.velocity = 10 #vitesse de la pasteque
        self.image = pygame.image.load("assets/pasteque.png") #attribue l'image de la pasteque
        self.rect = self.image.get_rect() #Récupérer les coordonnées de la pasteque
        self.rect.x = 250
        self.rect.y = 250

    def move_trajectory(self):
        global T
        self.rect.y = 1/2 * G * T * T + vitesse * math.sin(angle) * T + 250
        print()
        self.rect.x = vitesse * math.cos(angle) * T + 250
        print(math.cos(angle))
        print("angle ", angle)
        print(" vitesse ", vitesse)
        print(self.rect.y)
        print(self.rect.x)
        T = T + 1




#v0 = 100
       # x0 = 500
        #a = 60
        #t = 1
        #for i in range (10):
            #self.rect.x = v0 * math.cos(a) * t + x0
         #   self.rect.y += 1/2 * G * (t*t)
          #  time.sleep(1)
           # print(" x = ", self.rect.x)
            #print("y = ", self.rect.y)
            #screen.blit(game.pasteque.image, game.pasteque.rect)
            #t += 0.0000001
