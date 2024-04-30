import pygame
import math
import os
import random
import time

T = 0
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
height -= 100

pourcentage_x = width / 1280
pourcentage_y = height / 720

G = 9.80665 #constante de gravitation

noms_legumes = os.listdir("assets") #Créer une liste qui prend tous les noms d'image de légume dans le dossier assets

# Création d'une classe représentant les legumes
class Legume(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.game = game
        self.velocity = random.randint(30, 150)  # vitesse initiale des légumes
        self.image = pygame.image.load("assets/" + str(random.choice(noms_legumes)))  # attribue l'image des légumes
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.x_init = random.randint(int(60 * pourcentage_x), width - int(60 * pourcentage_x))
        self.rect.x = self.x_init
        self.rect.y = height
        self.angle = random.uniform(-math.pi / 2 + math.pi / 12, -math.pi / 2 - math.pi /12)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.clock = 0




    def remove_(self):
        self.game.all_legumes.remove(self)

    def move_trajectory(self):
        self.rect.y = 1/2 * G * self.clock * self.clock + self.velocity * math.sin(self.angle) * self.clock + height
        self.rect.x = self.velocity * math.cos(self.angle) * self.clock + self.x_init
        self.clock += 0.7

        #Vérifier si le légume est touchée par la souris
        if self.game.check_collision(self, self.game.all_legumes):
            self.remove()
            print("miam")

        # Vérifier que le légume est hors écran
        if self.rect.y > width:

            # Supprime le projectile
            self.remove()