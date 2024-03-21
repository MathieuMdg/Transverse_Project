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
width, height = screen.get_size()

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
    print(game.legume.throw_t_f())

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
