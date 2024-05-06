from game import Game
import time
import pygame
import random
import math

pygame.init()

pygame.display.set_caption("Légume Samouraï")
couleur_rond = (255, 255, 255)
color_light = (170, 170, 170)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

pourcentage_x = width / 1280
pourcentage_y = height / 720

print(width)
print(height)
mouse = pygame.mouse.get_pos()

# Attribut
game = Game()

# Pour afficher le menu avant l'execution ou non
game_menu = True

# Initialise la variable mouse_down
mouse_down = 0

# Pour démarrer le jeu
running = True

# Si un niveau est chargé ou non
game_level_load = False

# tant qu'un niveau n'est pas sélectionné
game_level_selection = True


# Boucle tant que la condition est vraie
while running:

    while game_menu:

        # Charge le menu du jeu
        game.game_menu()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                running = False
                game_menu = False
                game_level_selection = True
                pygame.quit()
                print("Fermeture du jeu")

            elif event.type == pygame.MOUSEBUTTONDOWN:

                if event.button == 1:

                    print(event.pos)  # Coordonnées du clique

                    # Detecte si le joueur a cliqué sur le bouton START
                    if (935 * pourcentage_x > event.pos[0] > 341 * pourcentage_x) and (79 * pourcentage_y < event.pos[1] < 146 * pourcentage_y):
                        game_menu = False
                        game_level_selection = False

                    # Detecte si le joueur a cliqué sur le bouton EXIT
                    if (705 * pourcentage_x > event.pos[0] > 577 * pourcentage_x) and (190 * pourcentage_y < event.pos[1] < 232 * pourcentage_y):
                        game_menu = False
                        running = False
                        game_level_selection = True
                        pygame.quit()
                        print("Fermeture du jeu")


            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()
                    print("Fermeture du jeu")
                    game_menu = False
                    game_level_selection = True



    # Tant que le niveau n'a pas été choisi
    while not game_level_selection:

        game_level_selection = game.game_level_selection()

        if game_level_selection == -1:
            game_level_selection = True
            game_level_load = False
            game_menu = True
            print("Retour au menu")

        elif game_level_selection:
            game_level_load = True





    while game_level_load:

        # Charge le niveau du jeu
        game.game_load_level(mouse_down)

        # Si le joueur ferme la fenêtre (ou clique sur le bouton quitter [plus tard])
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                print("Fermeture du jeu")



            # Detecter si un joueur lâche une touche du clavier
            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:

                    button_pressed = 0

                    print("Ouverture du menu pause")

                    while not button_pressed:

                        button_pressed = game.pause()

                    if button_pressed == 3:

                        game_level_selection = False
                        game_level_load = False
                        print("Retour à la selection des niveaux")

                if event.key == pygame.K_RIGHT:
                    print("start")
                    print("finish")


            # Si le bouton de la souris est préssé
            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Détecte si c'est le clic gauche de la souris
                if event.button == 1:

                    # Change la valeur de la variable pour détecter si un bouton de la souris est préssé
                    mouse_down = 1

            # Si le bouton de la souris est relevé
            elif event.type == pygame.MOUSEBUTTONUP:

                # Détecte si c'est le clic gauche de la souris
                if event.button == 1:
                    # Change la valeur de la variable pour détecter si un bouton de la souris est préssé
                    mouse_down = 0
