import pygame
import time
import random
import os

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pourcentage_x = width / 1920
pourcentage_y = height / 1080

from legume import Legume
from button import Resume_button, Quit_Button, Option_Button, Exit_Button, Start_Button, Survie_Button
from bomb import Bomb
from level_image import Level1, Level2, Level3, Level4, Level5


fps = 30
clock = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
pygame.font.init()  ## INITIALIZE FONT
myfont = pygame.font.SysFont('berlinsansfbdemi', int(70 * pourcentage_x))
texte_font = pygame.font.SysFont('berlinsansfbdemi', int(150 * pourcentage_x))
joueur_font = pygame.font.SysFont('berlinsansfbdemi', int(30 * pourcentage_x))

noms_level_background = os.listdir("assets/Level_background")





# Création d'une classe qui va représenter le jeu
class Game:

    def __init__(self):

        # Représente le nom du joueur
        self.joueur = ""

        # Créer un tableau pour stocker les meilleurs joueurs
        self.meilleur_joueur = []

        # Créer un tableau pour stocker les meilleurs scores
        self.meilleur_score = [0, 0, 0, 0, 0, 0]

        self.start_button = Start_Button()

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

        self.level_timer = [30, 30, 40, 50, 60, None]

        # Définir le temps initial
        self.time_start = time.time()

        # Définir l'arrière plan du menu
        self.menu_background = 'menu_assets/sky.jpg'

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

        # Régler le nombre d'images par seconde du jeu
        clock.tick(fps)

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

            # Detecter si un joueur lâche une touche du clavier
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:

                    self.reset_file()

        self.read_file()

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


        screen.blit(pygame.transform.scale(pygame.image.load("assets/menu_assets/sky.jpg"), (width, height)), (self.background_x, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("assets/menu_assets/sky_inverted.jpg"), (width, height)), (self.background_x2, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("assets/menu_assets/dirt.png"), (width, height)), (self.background_x, 0))
        screen.blit(pygame.transform.scale(pygame.image.load("assets/menu_assets/dirt_inverted.png"), (width, height)), (self.background_x2, 0))


    def game_level_selection(self):

        self.write_file()

        self.menu_defilement()

        # Caractéristiques de l'affichage du lose
        joueur_display = joueur_font.render(("Connecté en tant que " + self.joueur), 1, (255, 255, 255))
        joueur_rect = joueur_display.get_rect(center=(width / 2, height-20))
        screen.blit(joueur_display, joueur_rect)

        cadre = pygame.image.load("assets/Level_background/level_cadre-removebg-preview.png")
        cadre = pygame.transform.scale(cadre, (425 * pourcentage_x, 325 * pourcentage_y))


        screen.blit(cadre, (self.level1.rect.x - int(10 * pourcentage_x), self.level1.rect.y - int(10 * pourcentage_y)))
        screen.blit(self.level1.image, (self.level1.rect.x + int(55 * pourcentage_x), self.level1.rect.y + int(40 * pourcentage_y)))
        record_level1_display = joueur_font.render(("Record : " + str(self.meilleur_score[0]) + "s (" + self.meilleur_joueur[0] + ")"), 1, (255, 255, 255))
        record_level1_rect = record_level1_display.get_rect(center=(self.level1.rect.x + int(205 * pourcentage_x), self.level1.rect.y + int(252 * pourcentage_y)))
        screen.blit(record_level1_display, record_level1_rect)

        screen.blit(cadre, (self.level2.rect.x - int(10 * pourcentage_x), self.level2.rect.y - int(10 * pourcentage_y)))
        screen.blit(self.level2.image, (self.level2.rect.x + int(55 * pourcentage_x), self.level2.rect.y + int(40 * pourcentage_y)))
        record_level2_display = joueur_font.render(
            ("Record : " + str(self.meilleur_score[1]) + "s (" + self.meilleur_joueur[1] + ")"), 1, (255, 255, 255))
        record_level2_rect = record_level2_display.get_rect(
            center=(self.level2.rect.x + int(205 * pourcentage_x), self.level2.rect.y + int(252 * pourcentage_y)))
        screen.blit(record_level2_display, record_level2_rect)

        screen.blit(cadre, (self.level3.rect.x - int(10 * pourcentage_x), self.level3.rect.y - int(10 * pourcentage_y)))
        screen.blit(self.level3.image, (self.level3.rect.x + int(55 * pourcentage_x), self.level3.rect.y + int(40 * pourcentage_y)))
        record_level3_display = joueur_font.render(
            ("Record : " + str(self.meilleur_score[2]) + "s (" + self.meilleur_joueur[2] + ")"), 1, (255, 255, 255))
        record_level3_rect = record_level3_display.get_rect(
            center=(self.level3.rect.x + int(205 * pourcentage_x), self.level3.rect.y + int(252 * pourcentage_y)))
        screen.blit(record_level3_display, record_level3_rect)

        screen.blit(cadre, (self.level4.rect.x - int(10 * pourcentage_x), self.level4.rect.y - int(10 * pourcentage_y)))
        screen.blit(self.level4.image, (self.level4.rect.x + int(55 * pourcentage_x), self.level4.rect.y + int(40 * pourcentage_y)))
        record_level4_display = joueur_font.render(
            ("Record : " + str(self.meilleur_score[3]) + "s (" + self.meilleur_joueur[3] + ")"), 1, (255, 255, 255))
        record_level4_rect = record_level4_display.get_rect(
            center=(self.level4.rect.x + int(205 * pourcentage_x), self.level4.rect.y + int(252 * pourcentage_y)))
        screen.blit(record_level4_display, record_level4_rect)

        screen.blit(cadre, (self.level5.rect.x - int(10 * pourcentage_x), self.level5.rect.y - int(10 * pourcentage_y)))
        screen.blit(self.level5.image, (self.level5.rect.x + int(55 * pourcentage_x), self.level5.rect.y + int(40 * pourcentage_y)))
        record_level5_display = joueur_font.render(
            ("Record : " + str(self.meilleur_score[4]) + "s (" + self.meilleur_joueur[4] + ")"), 1, (255, 255, 255))
        record_level5_rect = record_level5_display.get_rect(
            center=(self.level5.rect.x + int(205 * pourcentage_x), self.level5.rect.y + int(252 * pourcentage_y)))
        screen.blit(record_level5_display, record_level5_rect)

        screen.blit(self.survie_button.image, (self.survie_button.rect.x, self.survie_button.rect.y))

        self.exit_button.rect.x = 20 * pourcentage_x
        self.exit_button.rect.y = (height - 100) - (50 * pourcentage_y)

        screen.blit(self.exit_button.image, (self.exit_button.rect.x, self.exit_button.rect.y))

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
        background = pygame.image.load('assets/Level_background/' + str(self.level_background[self.level_number - 1]))

        # Applique l'arrière-plan en grand écran
        stretchedbg = pygame.transform.smoothscale(background, (width, height))

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

        timer_rect = timer_display.get_rect(center=(width / 2, 20))

        # Applique le timer à l'écran
        screen.blit(timer_display, timer_rect)

        # Caractéristiques de l'affichage du score
        score_display = myfont.render("Score : " + str(self.player_score), 1, (255, 255, 255))

        score_rect = score_display.get_rect(center=(width / 2, 90 * pourcentage_y))

        # Applique le score à l'écran
        screen.blit(score_display, score_rect)

        if self.level_number == 6:

            record_survie_display = joueur_font.render(
                ("Record : " + str(self.meilleur_score[5]) + "points (" + self.meilleur_joueur[5] + ")"), 1, (255, 255, 255))
            screen.blit(record_survie_display, (0, height-30))

            if self.player_score > self.meilleur_score[5]:

                self.meilleur_score[5] = self.player_score

                self.meilleur_joueur[self.level_number - 1] = self.joueur


        if self.player_score < 0 or (self.timer == 0 and self.level_number != 6):
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
        background = pygame.image.load('assets/Level_background/' + str(self.level_background[self.level_number - 1]))

        # Applique l'arrière-plan en grand écran
        stretchedbg = pygame.transform.smoothscale(background, (width, height))

        # Appliquer l'arrière-plan de notre jeu
        screen.blit(stretchedbg, (0, 0))  # Pour repositionner le fond d'écran changer les nombres
        if self.level_number != 6:
            if self.player_score >= self.level_point_objectif[self.level_number - 1]:

                # Caractéristiques de l'affichage du win
                texte_display = texte_font.render("WIN", 1, (255, 128, 0))

                if self.level_timer[self.level_number - 1] - self.timer < self.meilleur_score[self.level_number - 1]:

                    self.meilleur_score[self.level_number - 1] = self.level_timer[self.level_number - 1] - self.timer

                    self.meilleur_joueur[self.level_number - 1] = self.joueur



            else:

                # Caractéristiques de l'affichage du lose
                texte_display = texte_font.render("LOSE", 1, (255, 128, 0))

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

        if self.level_number != 6:
            self.timer = int(self.level_timer[self.level_number - 1] - (time.time() - self.time_start - self.timer_pause))
            heures = self.timer // 3600
            secondes_restantes = self.timer % 3600
            minutes = secondes_restantes // 60
            secondes_final = secondes_restantes % 60

        else:
            self.timer = int(time.time() - self.time_start - self.timer_pause)
            heures = self.timer // 3600
            secondes_restantes = self.timer % 3600
            minutes = secondes_restantes // 60
            secondes_final = secondes_restantes % 60

        if heures == 0:
            timer = "00:"
        elif heures < 10:
            timer = "0" + str(heures) + ":"
        else:
            timer = str(heures) + ":"

        if minutes == 0:
            timer += "00:"
        elif minutes < 10:
            timer += "0" + str(minutes) + ":"
        else:
            timer += str(minutes) + ":"

        if secondes_final == 0:
            timer += "00"
        elif secondes_final < 10:
            timer += "0" + str(secondes_final)
        else:
            timer += str(secondes_final)

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

        if self.level_number == 6:
            self.timer_pause = int(time.time() - self.time_start - self.timer)
        else:
            self.timer_pause = int(time.time() - self.time_start - (self.level_timer[self.level_number - 1] - self.timer))

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

    def read_file(self):

        with open("Data.txt", 'r') as file:
            lignes = file.readlines()

        str_ = lignes[1]
        self.meilleur_score[0] = int(str_[26:-1])
        str_ = lignes[3]
        self.meilleur_score[1] = int(str_[26:-1])
        str_ = lignes[5]
        self.meilleur_score[2] = int(str_[26:-1])
        str_ = lignes[7]
        self.meilleur_score[3] = int(str_[26:-1])
        str_ = lignes[9]
        self.meilleur_score[4] = int(str_[26:-1])
        str_ = lignes[11]
        self.meilleur_score[5] = int(str_[25:])

        str_ = lignes[0]
        self.meilleur_joueur.append(str_[1:-2])
        str_ = lignes[2]
        self.meilleur_joueur.append(str_[1:-2])
        str_ = lignes[4]
        self.meilleur_joueur.append(str_[1:-2])
        str_ = lignes[6]
        self.meilleur_joueur.append(str_[1:-2])
        str_ = lignes[8]
        self.meilleur_joueur.append(str_[1:-2])
        str_ = lignes[10]
        self.meilleur_joueur.append(str_[1:-2])

        file.close()

    def write_file(self):

        with open("Data.txt", 'r') as file:
            lignes = file.readlines()

        str1 = lignes[1]
        str3 = lignes[3]
        str5 = lignes[5]
        str7 = lignes[7]
        str9 = lignes[9]
        str11 = lignes[11]


        with open("Data.txt", 'w') as file:
            file.writelines(['(' + str(self.meilleur_joueur[0]) + ')\n',str1[:26] + str(self.meilleur_score[0]) + "\n",'(' + str(self.meilleur_joueur[1]) + ')\n', str3[:26] + str(self.meilleur_score[1]) + "\n",'(' + str(self.meilleur_joueur[2]) + ')\n', str5[:26] + str(self.meilleur_score[2]) + "\n",'(' + str(self.meilleur_joueur[3]) + ')\n' , str7[:26] + str(self.meilleur_score[3]) + "\n",'(' + str(self.meilleur_joueur[4]) + ')\n', str9[:26] + str(self.meilleur_score[4]) + "\n",'(' + str(self.meilleur_joueur[5]) + ')\n', str11[:25] + str(self.meilleur_score[5])])


    def reset_file(self):

        for i in range(len(self.meilleur_joueur)):
            self.meilleur_joueur[i] = ""

        with open("Data.txt", 'w') as file:
            file.writelines(["()\n", "Meilleur temps (level_1): " + str(self.level_timer[0]) + "\n","()\n",
                            "Meilleur temps (level_2): " + str(self.level_timer[1]) + "\n","()\n", "Meilleur temps (level_3): " + str(self.level_timer[2]) + "\n","()\n",
                            "Meilleur temps (level_4): "+ str(self.level_timer[3]) + "\n","()\n", "Meilleur temps (level_5): "+ str(self.level_timer[4]) + "\n", "()\n", "Meilleur score (survie): 0"])

