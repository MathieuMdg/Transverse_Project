import pygame
import math
import os
import random
import time

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


    def move(self, stretchedbg):
        if self.throw:
            print("start")
            angle = random.uniform(-math.pi / 2 - math.pi / 12, -math.pi / 2 + math.pi / 12)
            print(angle)
            vitesse = random.randint(100, 115)
            T = 0

            x0 = random.randint(1, width-1)
            self.restart(x0)

            while self.rect.y < height:
                self.move_trajectory(T, angle, vitesse, x0)
                screen.blit(stretchedbg, (0, 0))
                screen.blit(self.image, self.rect)
                pygame.display.flip()
                T = T + 1
                time.sleep(0.05)
            print("finish")