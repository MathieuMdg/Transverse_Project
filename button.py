import pygame

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
height -= 100
pourcentage_x = width / 1280
pourcentage_y = height / 720

# Création d'une classe représentant les boutons
class Resume_button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("button/start_button2.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300, 100))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width/2 - 140  # attribue à la position du légume sa position initiale
        self.rect.y = height/2 - 200  # place le légume en bas de l'écran


class Option_Button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("button/option_button.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300, 100))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width/2 - 140  # attribue à la position du légume sa position initiale
        self.rect.y = height/2 # place le légume en bas de l'écran

class Quit_Button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("button/quit_button.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300, 100))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width/2 - 140  # attribue à la position du légume sa position initiale
        self.rect.y = height/2 + 200 # place le légume en bas de l'écran


class Exit_Button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("menu_assets/exit-removebg-preview.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300, 100))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = 0  # attribue à la position du légume sa position initiale
        self.rect.y = 0 # place le légume en bas de l'écran
