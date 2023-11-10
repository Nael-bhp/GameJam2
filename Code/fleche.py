
import pygame
import math
from pygame.sprite import Group


class Fleche():
    def __init__(self, direction, apparition, img_fleche, absisse, ordonnee):

        self.direction = direction
        self.apparition = apparition
        self.score = 0
        self.img_fleche = img_fleche
        self.absisse = absisse
        self.ordonnee = ordonnee
        self.score_modifiable = True

    # Setters
    def setAll(self,dicoAttributs):
        for cle, valeur in dicoAttributs.items():
            if hasattr(self, cle):
                setattr(self, cle, valeur)
            else:
                print(f"L'attribut {cle} n'existe pas dans la classe.")

    def get_direction(self):
        return self.direction

    def get_apparition(self):
        return self.apparition
    
    def get_score_modifiable(self):
        return self.score_modifiable

    def set_score(self, x):
        self.score = x

    def get_img_fleche(self):
        return self.img_fleche

    def get_absisse(self):
        return self.absisse

    def get_ordonnee(self):
        return self.ordonnee

    def get_score(self):
        return self.score

    def set_absisse(self,absisse):
        self.absisse = absisse

    def set_ordonnee(self,ordonnee):
        self.ordonnee = ordonnee

    def calcul_score(self, score, ordonnee):
        if score <  (ordonnee-30) or score > (ordonnee+30):
            return 0
        elif score < (ordonnee -20) or score > (ordonnee+20):
            return 1
        elif score < (ordonnee-10) or score > (ordonnee+10):
            return 2
        else:
            return 3
    



