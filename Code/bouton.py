import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
main_font = pygame.font.SysFont("cambria", 50)


class Bouton():
    def __init__(self, position_x, position_y, texte, image=None, niveau = -1):
        self.position_x = position_x
        self.position_y = position_y
        self.text_input = texte
        self.texte = main_font.render(texte, True, "white")
        self.niveau = niveau

        if(image is None) :
            self.image = self.texte
        else :
            self.image = image

        self.rectangle = self.image.get_rect(center=(self.position_x, self.position_y))
        self.text_rectangle = self.texte.get_rect(center=(self.position_x, self.position_y))

    def get_niveau(self):
        return self.niveau
    
    def get_texte(self):
        return self.text_input
 
    def maj(self):
        screen.blit(self.image, self.rectangle)
        screen.blit(self.texte, self.text_rectangle)
        

    def checkForInput(self, position):
            if position[0] in range(self.rectangle.left, self.rectangle.right) and position[1] in range(self.rectangle.top, self.rectangle.bottom):
                return True
            else :
                return False

    def changeColor(self, position):
        if position[0] in range(self.rectangle.left, self.rectangle.right) and position[1] in range(self.rectangle.top, self.rectangle.bottom):
            self.texte = main_font.render(self.text_input, True, "green")
        else:
            self.texte = main_font.render(self.text_input, True, "white")


