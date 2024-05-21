
nom_joueur = str(input("Choisir le nom du joueur : "))
while nom_joueur == "":
    nom_joueur = str(input("Choisir le nom du joueur : "))

import pygame
from game import Game

pygame.init()

# Attribut
game = Game()

game.joueur = nom_joueur

pygame.display.set_caption("Légume Samouraï")
couleur_rond = (255, 255, 255)
color_light = (170, 170, 170)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

pourcentage_x = width / 1920
pourcentage_y = height / 1080

print(width)
print(height)
mouse = pygame.mouse.get_pos()

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

game_menu_return = 0

# Boucle tant que la condition est vraie
while running:

    while game_menu:

        # Charge le menu du menu
        game_menu_return = game.game_menu()

        # Lorsque le bouton exit est cliqué
        if game_menu_return == -1:
            game_menu = False
            running = False
            game_level_selection = True
            pygame.quit()
            print("Fermeture du jeu")
            exit()

        # Lorsque le bouton start est cliqué
        if game_menu_return == 1:
            game_menu = False
            game_level_selection = False

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
                game_menu = False
                game_level_selection = True
                pygame.quit()
                print("Fermeture du jeu")

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

    game.game_restart_level()

    while game_level_load:

        # Charge le niveau du jeu
        if game.game_load_level(mouse_down) == 0:
            game_level_load = False
            game_level_selection = False

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
