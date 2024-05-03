import pygame
import time
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

        # Définir le timer pour les niveaux
        self.level_timer = 0

        # Définir le temps initial
        self.time_start = time.time()

    def timer_update(self):
        self.level_timer = int(time.time() - self.time_start)
        heures = self.level_timer // 3600
        secondes_restantes = self.level_timer % 3600
        minutes = secondes_restantes // 60
        secondes_final = secondes_restantes % 60
        timer = str(heures) + ":" + str(minutes) + ":" + str(secondes_final)
        return timer

    def lunch_legume(self):

        # Ajouter le légume dans le groupe
        self.all_legumes.add(Legume(self))
