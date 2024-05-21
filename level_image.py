import pygame

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()
print(width)
print(height)

pourcentage_x = width / 1920
pourcentage_y = height / 1080

# Création d'une classe représentant les images de niveaux
class Level1(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load(
            "assets/Level_background/background_salon.jpeg")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (int(400 * pourcentage_x), int(300 * pourcentage_y)))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = 200 * pourcentage_x  # attribue à la position du légume sa position initiale
        self.rect.y = 100 * pourcentage_y  # place le légume en bas de l'écran




class Level3(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load(
            "assets/Level_background/background_desert.jpeg")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (400 * pourcentage_x, 300 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width - (600 * pourcentage_x)  # attribue à la position du légume sa position initiale
        self.rect.y = 100 * pourcentage_y  # place le légume en bas de l'écran

class Level2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load(
            "assets/Level_background/background_arbre.jpg")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (400 * pourcentage_x, 300 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width / 2 - (200 * pourcentage_x)  # attribue à la position du légume sa position initiale
        self.rect.y = (100 * pourcentage_y)  # place le légume en bas de l'écran


class Level4(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load(
            "assets/Level_background/background_cuisine.jpeg")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (400 * pourcentage_x, 300 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = 500 * pourcentage_x  # attribue à la position du légume sa position initiale
        self.rect.y = 500 * pourcentage_y # place le légume en bas de l'écran


class Level5(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load(
            "assets/Level_background/background_dojo.jpg")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (400 * pourcentage_x, 300 * pourcentage_y))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = width / 2 + (100 * pourcentage_x)  # attribue à la position du légume sa position initiale
        self.rect.y = 500 * pourcentage_y # place le légume en bas de l'écran

class Level_Cadre(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()  # fais des légumes un sprite sur le jeu
        self.image = pygame.image.load(
            "assets/Level_background/level_cadre-removebg-preview.png")  # attribue l'image des butons
        self.image = pygame.transform.scale(self.image, (400, 300))  # redimensionne l'image sur l'écran
        self.rect = self.image.get_rect()  # Récupérer les coordonnées des légumes
        self.rect.x = 0  # attribue à la position du légume sa position initiale
        self.rect.y = 0  # place le légume en bas de l'écran

