import pygame
from legume import Legume


# Création d'une classe qui va représenter le jeu
class Game:

    def __init__(self):
        # Générer les légumes
        self.legume = Legume(self)

        # Créer un groupe de légume pour pouvoir en afficher plusieurs
        self.all_legumes = pygame.sprite.Group()

        # Définir le score du joueur
        self.player_score = 0

    def lunch_legume(self):

        #Ajouter le légume dans le groupe
        self.all_legumes.add(Legume(self))
