import pygame

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
height -= 100
pourcentage_x = width / 1920
pourcentage_y = height / 1080

# Création d'une classe représentant les boutons
class Resume_button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("button/start_button2.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300 * pourcentage_x, 100 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width/2 - (140 * pourcentage_x)  # attribue à la position du légume sa position initiale
        self.rect.y = height/2 - (200 * pourcentage_y)  # place le légume en bas de l'écran


class Option_Button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("button/option_button.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300 * pourcentage_x, 100 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width/2 - (140 * pourcentage_x)  # attribue à la position du légume sa position initiale
        self.rect.y = height/2 # place le légume en bas de l'écran

class Quit_Button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("button/quit_button.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300 * pourcentage_x, 100 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width/2 - (140 * pourcentage_x)  # attribue à la position du légume sa position initiale
        self.rect.y = height/2 + (200 * pourcentage_y) # place le légume en bas de l'écran


class Exit_Button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("menu_assets/exit-removebg-preview.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300 * pourcentage_x, 100 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = 20 * pourcentage_x # attribue à la position du légume sa position initiale
        self.rect.y = height - (50 * pourcentage_y) # place le légume en bas de l'écran

class Survie_Button(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("menu_assets/exit-removebg-preview.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (300 * pourcentage_x, 100 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width - (300 * pourcentage_x)  # attribue à la position du légume sa position initiale
        self.rect.y = height - (50 * pourcentage_y) # place le légume en bas de l'écran


class Start_Button(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load("menu_assets/button-removebg-preview.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (904 * pourcentage_x, 101 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = 510 * pourcentage_x  # attribue à la position du légume sa position initiale
        self.rect.y = 120 * pourcentage_y  # place le légume en bas de l'écran