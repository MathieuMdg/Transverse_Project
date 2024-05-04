import pygame
import time
import random

from legume import Legume
from button import Resume_button
from button import Quit_Button
from button import Option_Button


# Création d'une classe qui va représenter le jeu
class Game:

    def __init__(self):

        # Générer les boutons
        self.resume_button = Resume_button()

        # Générer les boutons
        self.quit_button = Quit_Button()

        # Générer les boutons
        self.option_button = Option_Button()

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

        # Définir le fond d'écran du décor
        self.level_background = 'background/background_1.jpeg'



    def timer_update(self):
        self.level_timer = int(time.time() - self.time_start)
        heures = self.level_timer // 3600
        secondes_restantes = self.level_timer % 3600
        minutes = secondes_restantes // 60
        secondes_final = secondes_restantes % 60
        timer = str(heures) + ":" + str(minutes) + ":" + str(secondes_final)
        return timer

    def lunch_legume(self):

        if random.randint(0, 10) == 0:

            # Ajouter le légume dans le groupe
            self.all_legumes.add(Legume(self))


    def legume_trajectory(self, mouse_down, pos_souris):

        # Récupérer tous les légumes
        for legumes in self.all_legumes:

            # Déclenche le mouvement des fruits
            legumes.move_trajectory(mouse_down, pos_souris)


    def pause(self, screen):

        screen.blit(self.resume_button.image, (self.resume_button.rect.x, self.resume_button.rect.y))

        screen.blit(self.option_button.image, (self.option_button.rect.x, self.option_button.rect.y))

        screen.blit(self.quit_button.image, (self.quit_button.rect.x, self.quit_button.rect.y))

        # Mettre à jour l'écran
        pygame.display.flip()

        for event in pygame.event.get():

            # Si le bouton de la souris est préssé
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Détecte si c'est le clic gauche de la souris
                if event.button == 1:

                    # Récupérer les coordonnées de la souris
                    pos_souris = pygame.mouse.get_pos()

                    if self.resume_button.rect.collidepoint(pos_souris):

                        return 1

                    elif self.option_button.rect.collidepoint(pos_souris):

                        return 2

                    elif self.quit_button.rect.collidepoint(pos_souris):

                        return 3

                    else:

                        return 0
