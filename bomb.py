import pygame
import math
import os
import random

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
height -= 100
pourcentage_x = width / 1280
pourcentage_y = height / 720

G = 9.80665 # Constante de gravitation

class Bomb(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.velocity = random.randint(int(90 * pourcentage_y), int(100 * pourcentage_y))  # vitesse initiale des légumes
        self.game = game # importe la classe game dans la classe légume
        self.image = pygame.image.load("assets/bomb_pixelart.png")  # attribue l'image des légumes aléatoirement
        self.point_given = -3 # Défini le nombre de points que donne le légume
        self.x_init = random.randint(int(100 * pourcentage_x), width - int(100 * pourcentage_x)) # position initiale du légume
        self.angle = random.uniform(-math.pi / 2 + math.pi / 20, -math.pi / 2 - math.pi / 20) # angle initial du légume
        self.image = pygame.transform.scale(self.image, (100, 100)) # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = self.x_init # attribue à la position du légume sa position initiale
        self.rect.y = height # place le légume en bas de l'écran
        self.clock = 0 # temps initial du légume


    def remove(self):

        # Retirer le légume du groupe (le supprime également de l'écran
        self.game.all_bombs.remove(self)

    def move_trajectory(self, mouse_down, pos_souris):

        # Equations horaires pour le mouvement du légume (trajectoire)
        self.rect.y = 1/2 * G * self.clock * self.clock + self.velocity * math.sin(self.angle) * self.clock + height
        self.rect.x = self.velocity * math.cos(self.angle) * self.clock + self.x_init

        # Ajoute le temps pour changer le mouvement
        self.clock += 0.5

        # Vérifier si le legume touche la souris
        if mouse_down:

            # Si le sprite légume est touché par la souris
            if self.rect.collidepoint(pos_souris):

                # Ajoute le nombre de points donné par le légume aux points du joueur
                self.game.player_score += self.point_given

                # Supprime le légume
                self.remove()

        # Vérifier que le légume est hors écran
        if self.rect.y > width:

            # Supprime le légume
            self.remove()