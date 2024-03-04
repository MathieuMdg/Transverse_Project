import pygame
from fruit import Fruit

# Création d'une classe qui va représenter le jeu
class Game:

    def __init__(self):
        # Générer les fruits
        self.pasteque = Fruit()
