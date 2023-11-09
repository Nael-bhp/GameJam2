


class Boss():
    
    def __init__(self, nom ="", taux_reussite=0, img_perso=None, music = None):
        self.nom=nom
        self.taux_reussite = taux_reussite
        if img_perso==None: self.img_perso = ["./Img/user.png"]
        else: 
            self.img_perso=img_perso
        self.music = music
            
    
    # Setters
    def setAll(self,dicoAttributs):
        for cle, valeur in dicoAttributs.items():
            if hasattr(self, cle):
                setattr(self, cle, valeur)
            else:
                print(f"L'attribut {cle} n'existe pas dans la classe.")
        
        # A terminer après avoir fini Outil
       
    def getMusic(self): # le chemin
        return self.music 
        
    #Getters
    def getNom(self):
        return self.nom
    
    def getTauxReussite(self):
        return self.taux_reussite
    
    def getImgPerso(self):
        return self.img_perso
    
    def getImgPersoAt(self, index):
        if index < len(self.img_perso) and index > -2 :
            return self.img_perso[index]
    
    def __str__(self):
        return "Nom : " + self.nom + "| Taux : " + self.taux_reussite + "| Img : " + self.img_perso
        
    
    
#boss1 = Boss()
#boss1 = Boss(nom="Garagamoule", taux_reussite=0.6, img_perso=["./Img/user.png", "./Img/boss1.png"])

#print(boss1)

