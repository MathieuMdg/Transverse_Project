from game import Game
import time
import pygame
import random
import math


pygame.init()
fps = 20
clock = pygame.time.Clock()




pygame.display.set_caption("Légume Samouraï")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
couleur_rond = (255, 255, 255)
color_light = (170, 170, 170)
width, height = screen.get_size()

pourcentage_x = width / 1280
pourcentage_y = height / 720

mouse = pygame.mouse.get_pos()

menu_background = pygame.image.load('menu_assets/Menu_bg.jpg')
menu_stretchedbg = pygame.transform.smoothscale(menu_background, (width, height))
screen.blit(menu_stretchedbg, (0, 0))
game = Game()

"""screen.blit(game.start_button.image, game.start_button.image.get_rect(center = screen.get_rect().center))"""
pygame.display.flip()

start = False

while start != True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False
            pygame.quit()
            print("Fermeture du jeu")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:

                print(event.pos)  # Coordonnées du clique

                # Detecte si le joueur a cliquer sur le bouton start
                if (730 * pourcentage_x > event.pos[0] > 510 * pourcentage_x) and (630 * pourcentage_y < event.pos[1] < 675 * pourcentage_y):
                    start = True


        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                print("Fermeture du jeu")

background = pygame.image.load('background/background_1.jpeg')
stretchedbg = pygame.transform.smoothscale(background, (width, height))

x = 0

running = True
# Charger le jeu
game = Game()
# Boucle tant que la condition est vraie
while running:

    clock.tick(fps)

    # Appliquer l'arrière plan de notre jeu
    screen.blit(stretchedbg, (0, 0))  # Pour repositionner le fond d'écran changer les nombres


    if random.randint(1, 8) < 2:
        game.lunch_legume()

    # Récupérer tous les légumes
    for legumes in game.all_legumes:

        # Déclenche le mouvement des fruits
        legumes.move_trajectory()

    # Appliquer l'ensemble des images de légumes
    game.all_legumes.draw(screen)

    # Mettre à jour l'écran
    pygame.display.flip()


    pos_souris = pygame.mouse.get_pos()

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

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for legumes in game.all_legumes:
                    if legumes.rect.collidepoint(event.pos):

                        # Supprime le legume si touché
                        legumes.remove()


                # screen.fill(couleur_fond)
                pygame.draw.circle(screen, couleur_rond, event.pos, 2)
                pygame.display.flip()
                print(event.pos)  # Coordonnées du clique
                print("Découpe enclenchée")




