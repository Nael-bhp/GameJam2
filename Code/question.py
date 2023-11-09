
class Question:

    def __init__(self, intitule) :
        
        self.intitule = intitule
        self.reponses = {}
        self.reponse_utilisateur = None


    def get_intitule(self) :
        return self.intitule
    
    def get_reponses(self) :
        return self.reponses
    
    def get_reponse_utilisateur(self) :
        return self.reponse_utilisateur
    
    def set_reponse_utilisateur(self, reponse) :
        self.reponse_utilisateur = reponse
    
    def add_reponse(self, intitule, booleen) :
        self.reponses[intitule] = booleen

