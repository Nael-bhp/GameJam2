import fleche
import time
import random

class Niveau:
    def __init__(self, num, decor, boss, score = 0):
        self.num = num
        self.boss = boss
        self.decor = decor
        self.fleches = []
        self.questions = []
        self.score = score
        self.scoreNecessaire = 0

        
        # Si le tps de l'implémenter
        self.isWon = False
        self.debloque = False
        
        self.current_flech = -1
        self.current_question = -1

    def set_score_necessaire(self, sc):
        self.scoreNecessaire = sc
                
    def get_num(self):
        return self.num

    def get_decor(self):
        return self.decor       # CHEMIN VERS LE FICHIER IMAGE

    def get_current_fleche(self):
        return self.current_flech

    def get_boss(self):
        return self.boss
    
    def get_score(self):
        return self.score
    
    def get_fleches(self):
        return self.fleches
    
    def set_fleches(self, fleches):
        self.fleches = fleches
        self.current_flech = 0


    def get_fleche(self, indice):
        if(self.current_fleche != -1):
            return self.fleches[indice]
        
        else:
            return -1 #Dans le cas d'une liste vide 
        
    def get_questions(self):
        return self.questions 

    # Setters
    def setAll(self,dicoAttributs):
        for cle, valeur in dicoAttributs.items():
            if hasattr(self, cle):
                setattr(self, cle, valeur)
            else:
                print(f"L'attribut {cle} n'existe pas dans la classe.")
                
    def setDebloquer(self):
        self.debloque=True
        
    def getDebloquer(self):
        return self.debloque
    
    def setIsWon(self):
        if(self.score >= self.scoreNecessaire): self.isWon=True
        
    def getIsWon(self):
        return self.isWon
    
    def set_current_fleche(self):
        self.current_flech = 1

    def add_fleche(self, fleche):
        self.fleches.append(fleche)
        if (self.current_flech == -1): #On passe d'une liste vide à une liste contenant des flèches
            self.current_flech = 0 

    def add_question(self, question):
        self.questions.append(question)
        if (self.current_question == -1):
            self.current_question = 0


    def current_fleche(self):
        return self.fleches[self.current_flech] 

    def next_fleche(self):
        self.current_flech += 1 # sert peut-être à rien

    def fin(self):
        return self.current_flech == len(self.fleches)-1

    """
    Fonction de calcul du score final 
    par somme des scores des flèches du niveau
    """


    def total_score(self):
        total = 0
        for f in self.fleches:
            total += f.get_score()
        for q in self.questions :
            if (q.get_reponse_utilisateur()):
                total+=5
        return total
    
    def add_score(self, val):
        self.score += val

    
    def generer_fleche_aleatoire(self):
        abscisse = 250
        ordonnee = 600
        fleches = []
        apparition = 0
        a = 0
        b = 1
        directions_possibles = ["UP", "DOWN", "LEFT", "RIGHT"]

        for i in range(100):
            direction_aleatoire = random.choice(directions_possibles)
            
            if(direction_aleatoire == "UP"):
                img = "./Img/Fleche_Up/sprite_0.png"
            elif(direction_aleatoire == "DOWN"):
                img = "./Img/Fleche_Down/sprite_0.png"
            elif(direction_aleatoire == "LEFT"):
                img = "./Img/Fleche_Left/sprite_0.png"
            else :
                img = "./Img/Fleche_Right/Fleche_Droite0.png"


            apparition = random.uniform(a, b)

            a = apparition+0.2
            b = apparition + 1

            current_fleche = fleche.Fleche(direction_aleatoire, apparition, img, abscisse, ordonnee)
            if (direction_aleatoire == "UP" or direction_aleatoire == "DOWN"):
                current_fleche.set_absisse(180)
            elif (direction_aleatoire == "LEFT"):
                current_fleche.set_absisse(70)
            else:
                current_fleche.set_absisse(280)

            fleches.append(current_fleche)
        return fleches
    
    def fin(self):
        return self.current_flech == len(self.fleches)-1