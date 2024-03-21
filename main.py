import time
import pygame
from game import Game
pygame.init()

fps = 20
clock = pygame.time.Clock()

pygame.display.set_caption("Légume Samourai")
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
couleur_rond = (255, 255, 255)
width, height = screen.get_size()

background = pygame.image.load('background/background_1.jpeg')
stretchedbg = pygame.transform.smoothscale(background,(width, height))

gameisnotover = True
running = True
# Charger le jeu
game = Game()
# Boucle tant que la condition est vraie
while running:
    clock.tick(fps)
    # Appliquer l'arrière plan de notre jeu
    screen.blit(stretchedbg, (0, 0)) # Pour repositionner le fond d'écran changer les nombres

    # Appliquer l'image du fruit
    screen.blit(game.legume.image, game.legume.rect)
    # Mettre à jour l'écran
    pygame.display.flip()
    # Si le joueur ferme la fenêtre (ou clique sur le bouton quitter [plus tard])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #Detecter si un joueur lâche une touche du clavier
        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False
                pygame.quit()
                print("Fermeture du jeu")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #screen.fill(couleur_fond)
                pygame.draw.circle(screen, couleur_rond, event.pos, 2)
                pygame.display.flip()
                print(event.pos) #Coordonnées du clique
                print("Découpe enclenchée")
                #print(event.button)  # numéro du bouton
                #if event.type == pygame.MOUSEMOTION:
    """while gameisnotover:
        game.legume.throw_t_f()
        if game.legume.throw:
            print("yes")
            print(game.legume.rect.y)
            while 0 <= game.legume.rect.y <= height:
                game.legume.move_trajectory()
                screen.blit(stretchedbg, (0, 0))
                screen.blit(game.legume.image, game.legume.rect)
                pygame.display.flip()
                time.sleep(0.05) """


