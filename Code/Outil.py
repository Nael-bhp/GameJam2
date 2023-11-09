import boss
def selectAttributsInFile(nomFichier, listeAttributSep = [], sep=","):
    listeDico = []
    listeAttributs = []
    
    try:
        with open(nomFichier, "r") as contenuFichier:
            
            ligne=contenuFichier.readline()
            ligne = ligne.strip() # Suppr espace + \n

            while ligne != "" :
                #print("Voici la ligne : ", ligne)
                
                if not ligne :
                    raise EOFError("Ligne non trouvée") # Renvoie une erreur si la ligne n'est pas trouvée
                # Erreur à créer ou à trouver déjà existante
                
                else : # plus lisible avec le else -- Cas où pas d'erreur
                    listeAttributs.append(ligne)
                
                # Prochaine ligne    
                ligne = contenuFichier.readline()
                ligne = ligne.strip() # Suppr espace + \n

                #print("Voici listeAttributs : " , listeAttributs)

            if len(listeAttributs) != 0 :
                i = 0
                _max = len(listeAttributs)
                ligne=contenuFichier.readline()
                ligne = ligne.strip() # Suppr espace + \n
                
                while ligne:
                    if ligne!= '\n':
                        #print('Arrivé ici')
                        if i==0 :
                            listeDico.append({})
                            #print("Dico : " , listeDico)

                        #print("Voici la ligne : ", ligne)
                        ligne = ligne.strip()# Suppr espace + \n
                        if listeAttributs[i] in listeAttributSep : ligne = ligne.split(sep) # Pas le droit d'avoir des virgules dans non les noms
                        
                        listeDico[-1][listeAttributs[i]] = ligne

                        i+=1  
                        if i == _max :
                            i = 0
                
                    # Prochaine ligne    
                    ligne = contenuFichier.readline() 
                    
                         
                    
                    
                
    except FileNotFoundError:
        raise FileNotFoundError("Le fichier ", nomFichier,  "n'existe pas.")

    return listeDico
    
    

#listeDico = selectAttributsInFile("./fichierTexte/boss.txt","img_perso")

#print(listeDico)

#boss = boss.Boss()
#boss.setAll(listeDico[0])
#print("GetImgPerso : ", boss.getImgPerso())
#print("GetImgPersoAt : ", boss.getImgPersoAt(0))