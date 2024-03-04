import pygame
from game import Game

pygame.init()

pygame.display.set_caption("Fruit Ninja")
screen = pygame.display.set_mode((1000, 600))
couleur_rond = (255,255,255)

background = pygame.image.load('assets/fruit ninja.jpg')

running = True

# Charger le jeu
game = Game()

# Boucle tant que la condition est vraie
while running:

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
        #elif event.type == pygame.KEYDOWN:
            # quelle touche a été utilisé
            #if event.key == pygame.K_LEFT: #Marche pas encore mais désigne le clique de la souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                #screen.fill(couleur_fond)
                pygame.draw.circle(screen, couleur_rond, event.pos, 2)
                pygame.display.flip()
                print(event.pos) #Coordonnées du clique
                print("Découpe enclenchée")
                #print(event.button)  # numéro du bouton
                #if event.type == pygame.MOUSEMOTION:
                   #pygame.draw.circle(pygame.display.set.mode((800,600)), (0,0,0), event.pos, 40) #Trace un rond à la position de la souris
