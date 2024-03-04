import pygame

# Création d'une classe représentant les fruits
class Fruit(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__() #fais de la pasteque un sprite sur le jeu
        self.velocity = 10 #vitesse de la pasteque
        self.image = pygame.image.load("assets/pasteque.png") #attribue l'image de la pasteque
        self.rect = self.image.get_rect() #Récupérer les coordonnées de la pasteque
        self.rect.x = 400
        self.rect.y = 300
