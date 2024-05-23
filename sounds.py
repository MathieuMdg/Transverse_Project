import pygame

class SoundManager:

    def __init__(self):
        self.sounds = {
            'click': pygame.mixer.Sound("assets/sounds/katana.mp3")
        }


    def play(self, name):
        self.sounds[name].play()