import boss
import niveau
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
    
                
         
def lire_fichier_questions(nom_fichier):
    questions = []  # Une liste pour stocker les questions

    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()

    # Initialisation des variables pour une nouvelle question
    intitule = ""
    reponses = {}

    for ligne in lignes:
        ligne = ligne.strip()

        if not ligne:
            # Ligne vide, ce qui signifie la fin d'une question
            if intitule and reponses:
                questions.append((intitule, reponses))
            intitule = ""
            reponses = {}
        elif ':' in ligne:
            # Ligne de réponse au format "réponse:True/False"
            reponse, est_correcte = ligne.split(':')
            reponses[reponse] = est_correcte.lower() == 'true'
        else:
            # Ligne d'intitulé de la question
            intitule = ligne

    # Vérifie s'il reste une question non ajoutée à la liste
    if intitule and reponses:
        questions.append((intitule, reponses))

    return questions
                    
                    
# Exemple d'utilisation
nom_fichier = "./fichierTexte/questions.txt"
questions = lire_fichier_questions(nom_fichier)

for index, (intitule, reponses) in enumerate(questions, start=1):
    print(f"Question {index}: {intitule}")
    for reponse, est_correcte in reponses.items():
        print(f"  - {reponse} (Correcte: {est_correcte})")
    

#listeDico = selectAttributsInFile("./fichierTexte/boss.txt","img_perso")

#print(listeDico)

#boss = boss.Boss()
#boss.setAll(listeDico[0])
#print("GetImgPerso : ", boss.getImgPerso())
#print("GetImgPersoAt : ", boss.getImgPersoAt(0))