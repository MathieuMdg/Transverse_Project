import time

import pygame
from game import Game
pygame.init()

fps = 20
clock = pygame.time.Clock()

pygame.display.set_caption("Legume Ninja")
screen = pygame.display.set_mode((1000, 600))
couleur_rond = (255,255,255)

background = pygame.image.load('background/Background_1.jpeg')

running = True
# Charger le jeu
game = Game()
# Boucle tant que la condition est vraie
while running:
    clock.tick(fps)
    # Appliquer l'arrière plan de notre jeu
    screen.blit(background, (0, 0)) # Pour repositionner le fond d'écran changer les nombres

    # Appliquer l'image du fruit
    screen.blit(game.pasteque.image, game.pasteque.rect)
    # Mettre à jour l'écran
    pygame.display.flip()
    # Si le joueur ferme la fenêtre (ou clique sur le bouton cliquer [plus tard])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #Detecter si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_RIGHT:
                print("yes")
                print(game.pasteque.rect.y)
                while (game.pasteque.rect.y < 598):
                    game.pasteque.move_trajectory()
                    screen.blit(background, (0, 0))
                    screen.blit(game.pasteque.image, game.pasteque.rect)
                    pygame.display.flip()
                    time.sleep(0.05)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #screen.fill(couleur_fond)
                pygame.draw.circle(screen, couleur_rond, event.pos, 2)
                pygame.display.flip()
                print(event.pos) #Coordonnées du clique
                print("Découpe enclenchée")
                #print(event.button)  # numéro du bouton
                #if event.type == pygame.MOUSEMOTION:
