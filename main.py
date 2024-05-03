from game import Game
import time
import pygame
import random
import math


pygame.init()
fps = 30
clock = pygame.time.Clock()

pygame.display.set_caption("Légume Samouraï")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
couleur_rond = (255, 255, 255)
color_light = (170, 170, 170)
width, height = screen.get_size()

print(width)
print(height)
mouse = pygame.mouse.get_pos()

menu_background = pygame.image.load('menu_assets/Menu_bg.jpg')
menu_stretchedbg = pygame.transform.smoothscale(menu_background, (width, height))
screen.blit(menu_stretchedbg, (0, 0))

# Attribut
game = Game()

pygame.display.flip()

pygame.font.init()  ## INITIALIZE FONT
myfont = pygame.font.SysFont('monospace', 16)

# Pour afficher le menu avant l'execution ou non
start = False

# Initialise la variable mouse_down
mouse_down = 0

while start != True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Fermeture du jeu")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                print(event.pos)  # Coordonnées du clique

                # Detecte si le joueur a cliqué sur le bouton start
                if (730 > event.pos[0] > 510) and (630 < event.pos[1] < 675):
                    start = True


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                print("Fermeture du jeu")

# Choix de l'arrière-plan du jeu
background = pygame.image.load(game.level_background)

# Applique l'arrière-plan en grand écran
stretchedbg = pygame.transform.smoothscale(background, (width, height))


# Pour démarrer le jeu
running = True

# Charger le jeu
game = Game()

# Boucle tant que la condition est vraie
while running:

    # Régler le nombre d'images par seconde du jeu
    clock.tick(fps)

    # Appliquer l'arrière-plan de notre jeu
    screen.blit(stretchedbg, (0, 0))  # Pour repositionner le fond d'écran changer les nombres

    # Récupérer les coordonnées de la souris
    pos_souris = pygame.mouse.get_pos()

    # Lancement de manière aléatoire des légumes
    game.lunch_legume()

    # Déclencher la trajectoire des légumes
    game.legume_trajectory(mouse_down, pos_souris)

    # Appliquer l'ensemble des images de légumes
    game.all_legumes.draw(screen)

    # Caractéristiques de l'affichage du timer
    timer_display = myfont.render(game.timer_update(), 1, (255, 255, 255))

    # Applique le timer à l'écran
    screen.blit(timer_display, (width - 50, 0))

    # Caractéristiques de l'affichage du score
    score_display = myfont.render(str(game.player_score), 1, (255, 255, 255))

    # Applique le score à l'écran
    screen.blit(score_display, (width - 50, 50))

    # Mettre à jour l'écran
    pygame.display.flip()

    # Si le joueur ferme la fenêtre (ou clique sur le bouton quitter [plus tard])
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")



        # Detecter si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                print("Fermeture du jeu")

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
