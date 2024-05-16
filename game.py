import pygame
import time
import random
import os

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pourcentage_x = width / 1920
pourcentage_y = height / 1080

from legume import Legume
from button import Resume_button
from button import Quit_Button
from button import Option_Button
from button import Exit_Button
from button import Survie_Button
from bomb import Bomb
from level_image import Level1
from level_image import Level3
from level_image import Level2
from level_image import Level4
from level_image import Level5
from level_image import Level_Cadre
from button import Start_Button


pygame.init()
fps = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.font.init()  ## INITIALIZE FONT
myfont = pygame.font.SysFont('berlinsansfbdemi', int(90 * pourcentage_x))
texte_font = pygame.font.SysFont('berlinsansfbdemi', int(150 * pourcentage_x))

noms_level_background = os.listdir("background/Level_background")





# Création d'une classe qui va représenter le jeu
class Game:

    def __init__(self):

        self.start_button = Start_Button()

        self.level_cadre = Level_Cadre()

        # Créer un groupe de légume pour pouvoir en afficher plusieurs
        self.all_cadres = pygame.sprite.Group()

        self.survie_button = Survie_Button()

        self.exit_button = Exit_Button()

        # Générer les boutons
        self.level5 = Level5()

        # Générer les boutons
        self.level4 = Level4()

        # Générer les boutons
        self.level2 = Level2()

        # Générer les boutons
        self.level3 = Level3()

        # Générer les boutons
        self.level1 = Level1()

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
        self.menu_background = 'menu_assets/ciel.jpg'

        # Définir le fond d'écran du décor
        self.level_background = ["background_salon.jpeg", "background_arbre.jpg", "background_desert.jpeg", "background_cuisine.jpeg", "background_dojo.jpg", "background_montagne.jpg"]

        # Définir le nombre de temps passé en "pause"
        self.timer_pause = 0

        # Définir le numéro du niveau
        self.level_number = 0

        self.level_difficulty = 0

        self.background_x = 0

        self.background_x2 = width

        self.level_point_objectif = [10, 15, 20, 25, 30, None]






    def game_menu(self):

        self.menu_defilement()

        screen.blit(self.start_button.image, (self.start_button.rect.x, self.start_button.rect.y))

        self.exit_button.rect.x = width/2 - (150 * pourcentage_x)
        self.exit_button.rect.y = 250 * pourcentage_y

        screen.blit(self.exit_button.image, (self.exit_button.rect.x, self.exit_button.rect.y))

        pygame.display.flip()

        for event in pygame.event.get():

            # Si le bouton de la souris est préssé
            if event.type == pygame.MOUSEBUTTONDOWN:

                # Détecte si c'est le clic gauche de la souris
                if event.button == 1:

                    # Récupérer les coordonnées de la souris
                    pos_souris = pygame.mouse.get_pos()

                    if self.start_button.rect.collidepoint(pos_souris):

                        return 1

                    if self.exit_button.rect.collidepoint(pos_souris):

                        return -1
        return 0

    def game_restart_level(self):

        self.player_score = 0
        self.timer_pause = 0
        self.time_start = time.time()
        for legume in self.all_legumes:
            legume.remove()
        for bomb in self.all_bombs:
            bomb.remove()


    def menu_defilement(self):



        if self.background_x > -width:
            self.background_x -= 1
        else:
            self.background_x = width
        if self.background_x2 > -width:
            self.background_x2 -= 1
        else:
            self.background_x2 = width


        screen.blit(pygame.transform.scale(pygame.image.load("menu_assets/ciel.jpg"), (width, height)),(self.background_x, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("menu_assets/ciel2.jpg"), (width, height)),(self.background_x2, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("menu_assets/terre.png"), (width, height)),(self.background_x, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("menu_assets/terre2.png"), (width, height)),(self.background_x2, 0))


    def game_level_selection(self):

        self.menu_defilement()

        screen.blit(self.level1.image, (self.level1.rect.x, self.level1.rect.y))

        screen.blit(self.level3.image, (self.level3.rect.x, self.level3.rect.y))

        screen.blit(self.level2.image, (self.level2.rect.x, self.level2.rect.y))

        screen.blit(self.level4.image, (self.level4.rect.x, self.level4.rect.y))

        screen.blit(self.level5.image, (self.level5.rect.x, self.level5.rect.y))

        screen.blit(self.survie_button.image, (self.survie_button.rect.x, self.survie_button.rect.y))

        self.exit_button.rect.x = 20 * pourcentage_x
        self.exit_button.rect.y = (height - 100) - (50 * pourcentage_y)

        screen.blit(self.exit_button.image, (self.exit_button.rect.x, self.exit_button.rect.y))

        # Appliquer l'ensemble des images de légumes
        self.all_cadres.draw(screen)

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

                    if self.level1.rect.collidepoint(pos_souris):

                        self.level_number = 1

                        return 1

                    elif self.level2.rect.collidepoint(pos_souris):

                        self.level_number = 2

                        return 2

                    elif self.level3.rect.collidepoint(pos_souris):

                        self.level_number = 3

                        return 3

                    elif self.level4.rect.collidepoint(pos_souris):

                        self.level_number = 4

                        return 4

                    elif self.level5.rect.collidepoint(pos_souris):

                        self.level_number = 5

                        return 5

                    elif self.survie_button.rect.collidepoint(pos_souris):

                        self.level_number = 6

                        return 6

                    elif self.exit_button.rect.collidepoint(pos_souris):

                        self.level_number = 0

                        return -1
            else:

                return 0





    def game_load_level(self, mouse_down):

        # Choix de l'arrière-plan du level
        background = pygame.image.load('background/Level_background/' + str(self.level_background[self.level_number - 1]))

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
        screen.blit(timer_display, (width - (190 * pourcentage_x), 0))

        # Caractéristiques de l'affichage du score
        score_display = myfont.render(str(self.player_score), 1, (255, 255, 255))

        # Applique le score à l'écran
        screen.blit(score_display, (width - (90 * pourcentage_x), 70 * pourcentage_y))

        if self.player_score < 0:
            print("Objectif de point perdu")
            print(self.player_score)
            while self.level_number != 0:
                self.end()
            return 0
        if self.level_number != 6:
            if self.player_score >= self.level_point_objectif[self.level_number - 1]:
                print("Objectif de point fini")
                print(self.player_score)
                while self.level_number != 0:
                    self.end()
                return 0

        # Mettre à jour l'écran
        pygame.display.flip()


    def end(self):

        # Choix de l'arrière-plan du level
        background = pygame.image.load('background/Level_background/' + str(self.level_background[self.level_number - 1]))

        # Applique l'arrière-plan en grand écran
        stretchedbg = pygame.transform.smoothscale(background, (width, height))

        # Régler le nombre d'images par seconde du jeu
        clock.tick(fps)

        # Appliquer l'arrière-plan de notre jeu
        screen.blit(stretchedbg, (0, 0))  # Pour repositionner le fond d'écran changer les nombres

        if self.player_score >= self.level_point_objectif[self.level_number - 1]:

            # Caractéristiques de l'affichage du win
            texte_display = texte_font.render("WIN", 1, (255, 128, 0))

        else:

            # Caractéristiques de l'affichage du lose
            texte_display = texte_font.render("LOSE", 1, (255, 128, 0))

        # Déclencher la trajectoire des légumes
        self.legume_trajectory(0, (0,0))

        # Déclencher la trajectoire des légumes
        self.bomb_trajectory(0, (0,0))

        # Appliquer l'ensemble des images de légumes

        self.all_legumes.draw(screen)

        # Appliquer l'ensemble des images de légumes
        self.all_bombs.draw(screen)

        text_rect = texte_display.get_rect(center=(width / 2, height / 2))

        # Applique le timer à l'écran
        screen.blit(texte_display, text_rect)

        screen.blit(self.exit_button.image, (self.exit_button.rect.x, self.exit_button.rect.y))

        pygame.display.flip()

        # Récupérer les coordonnées de la souris
        pos_souris = pygame.mouse.get_pos()

        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                # Détecte si c'est le clic gauche de la souris
                if event.button == 1:

                    if self.exit_button.rect.collidepoint(pos_souris):

                        self.level_number = 0


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

    def set_level_difficulty(self, level_number):
        """
        Set the difficulty and attributes for each level.
        """
        if level_number == 1:
            self.level_difficulty = 1
        elif level_number == 2:
            self.level_difficulty = 1.5
        elif level_number == 3:
            self.level_difficulty = 2
        elif level_number == 4:
            self.level_difficulty = 2.5
        elif level_number == 5:
            self.level_difficulty = 3

    def chargement_level(self, mouse_down):
        """
        Load the game level based on the selected level number.
        """
        # Backgrounds for each level
        level_backgrounds = [
            'background/Background_1.jpeg',
            'background/background_salon.jpeg',
            'menu_assets/menu_pixel_art.jpg',
            'menu_assets/Menu_bg.jpg',
            'background/fruit ninja.jpg'
        ]

        # Set the appropriate background for the selected level
        background = pygame.image.load(level_backgrounds[self.level_number - 1])
        stretchedbg = pygame.transform.smoothscale(background, (width, height))

        clock.tick(fps)
        screen.blit(stretchedbg, (0, 0))

        # Retrieve mouse position and handle game logic
        pos_souris = pygame.mouse.get_pos()
        self.lunch_legume()
        self.legume_trajectory(mouse_down, pos_souris)
        self.bomb_trajectory(mouse_down, pos_souris)
        self.all_legumes.draw(screen)
        self.all_bombs.draw(screen)

        # Timer and score display
        timer_display = myfont.render(self.timer_update(), 1, (255, 255, 255))
        screen.blit(timer_display, (width - 190, 0))

        score_display = myfont.render(str(self.player_score), 1, (255, 255, 255))
        screen.blit(score_display, (width - 90, 70))

        pygame.display.flip()
