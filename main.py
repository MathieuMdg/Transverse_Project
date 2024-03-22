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

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:

                running = False
                pygame.quit()
                print("Fermeture du jeu")

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if width*(38 / 100) <= mouse[0] <= width*(59 / 100) and height * (86 / 100) <= mouse[1] <= height * (
                    95 / 100):

                start = True

    if width * (38 / 100) >= mouse[0] <= width * (59 / 100) and height * (86 / 100) >= mouse[1] >= height * (
            95 / 100):

        """screen.blit(menu_stretchedbg, (0, 0))""" #mettre image avec filtre lumineux

    else:
        """screen.blit(menu_stretchedbg, (0, 0))""" #mettre bouton normal
time.sleep(0.5)

background = pygame.image.load('background/background_1.jpeg')
stretchedbg = pygame.transform.smoothscale(background, (width, height))

running = True
# Charger le jeu
game = Game()
# Boucle tant que la condition est vraie
while running:
    clock.tick(fps)
    # Appliquer l'arrière plan de notre jeu
    screen.blit(stretchedbg, (0, 0))  # Pour repositionner le fond d'écran changer les nombres

    # Appliquer l'image du fruit
    screen.blit(game.legume.image, game.legume.rect)
    # Mettre à jour l'écran
    pygame.display.flip()

    game.legume.throw_t_f()

    if game.legume.throw:
        print("start")
        angle = random.uniform(-math.pi / 3, -2 * math.pi / 3)
        vitesse = random.randint(120, 150)
        T = 0

        while game.legume.rect.y < height:
            game.legume.move_trajectory(T, angle, vitesse)
            screen.blit(stretchedbg, (0, 0))
            screen.blit(game.legume.image, game.legume.rect)
            pygame.display.flip()
            T = T + 1
            time.sleep(0.05)
        print("finish")
        game.legume.restart()
        game.legume.throw = False

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
                angle = random.uniform(-math.pi / 3, -2 * math.pi / 3)
                vitesse = random.randint(120, 150)
                T = 0

                while game.legume.rect.y < height:
                    game.legume.move_trajectory(T, angle, vitesse)
                    screen.blit(stretchedbg, (0, 0))
                    screen.blit(game.legume.image, game.legume.rect)
                    pygame.display.flip()
                    T = T + 1
                    time.sleep(0.05)
                print("finish")
                game.legume.restart()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # screen.fill(couleur_fond)
                pygame.draw.circle(screen, couleur_rond, event.pos, 2)
                pygame.display.flip()
                print(event.pos)  # Coordonnées du clique
                print("Découpe enclenchée")
                # print(event.button)  # numéro du bouton
                # if event.type == pygame.MOUSEMOTION:
