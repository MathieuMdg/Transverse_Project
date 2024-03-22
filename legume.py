import pygame
import math
import os
import random

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
height -= 100

G = 9.80665 #constante de gravitation

noms_legumes = os.listdir("assets") #Créer une liste qui prend tous les noms d'image de légume dans le dossier assets

# Création d'une classe représentant les legumes
class Legume(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.velocity = 10  # vitesse des légumes
        self.image = pygame.image.load("assets/" + str(random.choice(noms_legumes)))  # attribue l'image des légumes
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width / 2
        self.rect.y = height
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.throw = False

    def restart(self, x0):
        self.rect.x = x0
        self.rect.y = height
        self.image = pygame.image.load("assets/" + str(random.choice(noms_legumes)))
        self.image = pygame.transform.scale(self.image, (100, 100))


    def throw_t_f(self):
        if random.random() >= 0.9:
            self.throw = True
            return True
        else:
            self.throw = False
            return False

    def move_trajectory(self, T, angle, vitesse, x0):
        self.rect.y = 1/2 * G * T * T + vitesse * math.sin(angle) * T + height
        self.rect.x = vitesse * math.cos(angle) * T + x0




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

"""
1792  38%  41%

678
1052
1111
737

1024  86%  5%
884
970
135
"""