import pygame
from legume import Legume


screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

class Start_button:

    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("menu_assets/startbutton.png")
        self.rect = self.image.get_rect()
        self.rect.x = width / 2
        self.rect.y = height - (height/3)



# Création d'une classe qui va représenter le jeu
class Game:

    def __init__(self):
        # Générer les légumes
        self.legume = Legume()
        self.start_button = Start_button()
