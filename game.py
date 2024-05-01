import pygame
from legume import Legume


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()


# Création d'une classe qui va représenter le jeu
class Game:

    def __init__(self):
        # Générer les légumes
        self.legume = Legume(self)
        self.all_legumes = pygame.sprite.Group()


    def lunch_legume(self):

        #Créer une nouvelle instance de legume
        self.all_legumes.add(Legume(self))



