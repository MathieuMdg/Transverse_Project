import pygame
import time
import random

from legume import Legume
from button import Resume_button
from button import Quit_Button
from button import Option_Button
from bomb import Bomb

pygame.init()
fps = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.font.init()  ## INITIALIZE FONT
myfont = pygame.font.SysFont('berlinsansfbdemi', 90)







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

        # Générer les bombes
        self.bomb = Bomb(self)

        # Créer un groupe de légume pour pouvoir en afficher plusieurs
        self.all_legumes = pygame.sprite.Group()

        # Créer un groupe de légume pour pouvoir en afficher plusieurs
        self.all_bombs = pygame.sprite.Group()

        # Définir le score du joueur
        self.player_score = 0

        # Définir un timer qui augmente tant que le jeu est actif
        self.timer = 0

        # Définir le temps initial
        self.time_start = time.time()

        # Définir l'arrière plan du menu
        self.menu_background = 'menu_assets/menu_pixel_art.jpg'

        # Définir le fond d'écran du décor
        self.level_background = 'background/background_game_second.jpeg'

        # Définir le nombre de temps passé en "pause"
        self.timer_pause = 0

        # Définir le numéro du niveau
        self.level_number = 0


    def game_menu(self):

        menu_background = pygame.image.load(self.menu_background)
        menu_stretchedbg = pygame.transform.smoothscale(menu_background, (width, height))
        screen.blit(menu_stretchedbg, (0, 0))
        pygame.display.flip()


    def game_level_selection(self):

        menu_background = pygame.image.load('menu_assets/Menu_bg.jpg')
        menu_stretchedbg = pygame.transform.smoothscale(menu_background, (width, height))
        screen.blit(menu_stretchedbg, (0, 0))


        screen.blit(self.resume_button.image, (self.resume_button.rect.x, self.resume_button.rect.y))

        screen.blit(self.option_button.image, (self.option_button.rect.x, self.option_button.rect.y))

        screen.blit(self.quit_button.image, (self.quit_button.rect.x, self.quit_button.rect.y))

        pygame.display.flip()

        for event in pygame.event.get():


            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return -1

            # Si le bouton de la souris est préssé
            elif event.type == pygame.MOUSEBUTTONDOWN:

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





    def game_load_level(self, mouse_down):

        # Choix de l'arrière-plan du level
        background = pygame.image.load(self.level_background)

        # Applique l'arrière-plan en grand écran
        stretchedbg = pygame.transform.smoothscale(background, (width, height))

        # Régler le nombre d'images par seconde du jeu
        clock.tick(fps)

        # Appliquer l'arrière-plan de notre jeu
        screen.blit(stretchedbg, (0, 0))  # Pour repositionner le fond d'écran changer les nombres

        # Récupérer les coordonnées de la souris
        pos_souris = pygame.mouse.get_pos()

        # Lancement de manière aléatoire des légumes
        self.lunch_legume()

        # Déclencher la trajectoire des légumes
        self.legume_trajectory(mouse_down, pos_souris)

        # Déclencher la trajectoire des légumes
        self.bomb_trajectory(mouse_down, pos_souris)

        # Appliquer l'ensemble des images de légumes
        self.all_legumes.draw(screen)

        # Appliquer l'ensemble des images de légumes
        self.all_bombs.draw(screen)

        # Caractéristiques de l'affichage du timer
        timer_display = myfont.render(self.timer_update(), 1, (255, 255, 255))

        # Applique le timer à l'écran
        screen.blit(timer_display, (width - 190, 0))

        # Caractéristiques de l'affichage du score
        score_display = myfont.render(str(self.player_score), 1, (255, 255, 255))

        # Applique le score à l'écran
        screen.blit(score_display, (width - 90, 70))

        # Mettre à jour l'écran
        pygame.display.flip()


    def timer_update(self):

        self.timer = int(time.time() - self.time_start - self.timer_pause)
        heures = self.timer // 3600
        secondes_restantes = self.timer % 3600
        minutes = secondes_restantes // 60
        secondes_final = secondes_restantes % 60
        timer = str(heures) + ":" + str(minutes) + ":" + str(secondes_final)
        return timer


    def lunch_legume(self):

            if random.randint(0,8) == 0:

                # Ajouter le légume dans le groupe
                self.all_legumes.add(Legume(self))

            if random.randint(0, 30) == 0:

                # Ajouter la bomb dans le groupe
                self.all_bombs.add(Bomb(self))


    def legume_trajectory(self, mouse_down, pos_souris):

        # Récupérer tous les légumes
        for legumes in self.all_legumes:

            # Déclenche le mouvement des fruits
            legumes.move_trajectory(mouse_down, pos_souris)

    def bomb_trajectory(self, mouse_down, pos_souris):

        # Récupérer tous les légumes
        for bombs in self.all_bombs:

            # Déclenche le mouvement des fruits
            bombs.move_trajectory(mouse_down, pos_souris)


    def pause(self):

        # Applique l'image du bouton "RESUME"
        screen.blit(self.resume_button.image, (self.resume_button.rect.x, self.resume_button.rect.y))

        # Applique l'image du bouton "OPTION"
        screen.blit(self.option_button.image, (self.option_button.rect.x, self.option_button.rect.y))

        # Applique l'image du bouton "QUIT"
        screen.blit(self.quit_button.image, (self.quit_button.rect.x, self.quit_button.rect.y))

        # Mettre à jour l'écran
        pygame.display.flip()

        self.timer_pause = int(time.time() - self.time_start - self.timer)

        for event in pygame.event.get():

            # Si le bouton echap préssé
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    return 3

            # Si le bouton de la souris est préssé
            elif event.type == pygame.MOUSEBUTTONDOWN:

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
