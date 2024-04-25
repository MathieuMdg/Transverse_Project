import pygame
import math
import os
import random
import time

T = 0
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
height -= 100

G = 9.80665 #constante de gravitation

noms_legumes = os.listdir("assets") #Créer une liste qui prend tous les noms d'image de légume dans le dossier assets

# Création d'une classe représentant les legumes
class Legume(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.velocity = random.randint(90, 110)  # vitesse initiale des légumes
        self.image = pygame.image.load("assets/" + str(random.choice(noms_legumes)))  # attribue l'image des légumes
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.x_init = random.randint(40, width - 40)
        self.rect.x = self.x_init
        self.rect.y = height
        self.angle = random.uniform(-math.pi / 2 + math.pi / 12, -math.pi / 2 - math.pi /12)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.throw = False
        self.all_legumes = pygame.sprite.Group()
        self.clock = 0



    def lunch_legume(self):
        self.all_legumes.add(Legume())

##    def throw_t_f(self):
##      if random.random() >= 0.9:
##            self.throw = True
##            self.all_legumes.add(Legume())

#            return True
#        else:
#            self.throw = False
#            return False

    def move_trajectory(self):
        self.rect.y = 1/2 * G * self.clock * self.clock + self.velocity * math.sin(self.angle) * self.clock + height
        self.rect.x = self.velocity * math.cos(self.angle) * self.clock + self.x_init
        self.clock += 0.7

