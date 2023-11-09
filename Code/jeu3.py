import boss 
import niveau 
import pygame
import fleche 
import bouton
import time 
import Outil
import question

# Var globales pour les couleurs par ex
BLEU_CLAIR = (173, 216, 230)
NOIR = (0,0,0)
BLANC = (255,255,255)


question1 = question.Question("Qui a inventé Linux ?")
reponse_fausse1 = "JP"
reponse_fausse2 = "Moi"
reponse_fausse3 = "Napoléon"
reponse_juste = "Linus Torvald"

question1.add_reponse(reponse_fausse1, False)
question1.add_reponse(reponse_fausse2, False)
question1.add_reponse(reponse_fausse3, False)
question1.add_reponse(reponse_juste, True)


class Jeu:
    def __init__(self, screen : pygame.Surface, ):
        
        self.screen = screen
        
        self.background = pygame.Surface(self.screen.get_size())
        self.background.fill("black")
        
        # Dessine le font d'écran une première fois
        self.screen.blit(self.background,(0,0))
        
        # Creation liste de boss
        listeDicoBoss = Outil.selectAttributsInFile("./fichierTexte/boss.txt", "img_perso")
        listeBoss = []
        #print(listeDicoBoss)
        
        for elem in listeDicoBoss :
            currentBoss = boss.Boss()
            currentBoss.setAll(elem)
            listeBoss.append(currentBoss)
            #print(currentBoss)
        
        
        # Creation des background à la main (mais faire par fichier après)
        listeBg = ["./Img/bg_fleches/iut.png","./Img/bg_fleches/amphi.png","./Img//bg_fleches/camion.png","./Img//bg_fleches/classe.png","./Img//bg_fleches/center.png"]
        
        listeSon = ["./songs/"]
        
        if len(listeBoss) > len(listeBg) : _max = len(listeBg)
        else : _max = len(listeBoss)
        
        # Creation liste de niveaux
        self.niveaux = []
        
        #print(type(listeBoss[0]))
        #print(type(listeBoss[0].getNom()))
        
        
        for i in range(_max) :
            self.niveaux.append(niveau.Niveau(i+1, listeBg[i], listeBoss[i]))
            self.niveaux[i].set_fleches(self.niveaux[i].generer_fleche_aleatoire())
            self.niveaux[i].add_question(question1)

            #print (type(self.niveaux[i]))
            #
            #print(self.niveaux[i])
            
            
        #print(len(self.niveaux)) #OK car que 2 bg
        
        self.menu_prinipal()
            


    def isRunning(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
     
            
    def menu_prinipal(self):
        continuer = True

        pygame.mixer.music.load('./songs/ecran_titre.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play()


        while continuer :

            self.screen.fill("black")

            souris_utilisateur = pygame.mouse.get_pos()

            titre_menu = pygame.font.SysFont("cambria", 50).render((str) ("Menu Principal"),1,(255,255,255))
            fond_titre = titre_menu.get_rect(center=(640, 100))

            bouton_jouer = bouton.Bouton(640,300,"JOUER")
            bouton_regles = bouton.Bouton(640, 400, "RÈGLES")
            bouton_credits = bouton.Bouton(640, 500, "CRÉDITS")  # Ajout du bouton "Crédits"
            bouton_quitter = bouton.Bouton(640, 600, "QUITTER")

            self.screen.blit(titre_menu, fond_titre)

            for button in [bouton_jouer, bouton_credits, bouton_regles, bouton_quitter]:
                button.changeColor(souris_utilisateur)
                button.maj()
            
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    continuer = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if(bouton_jouer.checkForInput(souris_utilisateur)):
                        pygame.mixer.music.pause()
                        self.selectionNiveau()
                    if(bouton_quitter.checkForInput(souris_utilisateur)):
                        pygame.quit()
                        continuer = False
                    if bouton_credits.checkForInput(souris_utilisateur):  # Gestion du clic sur le bouton "Crédits"
                        self.afficherCredits()  # Appel d'une nouvelle méthode pour afficher les crédits
                    if bouton_regles.checkForInput(souris_utilisateur):  # Gestion du clic sur le bouton "Crédits"
                        self.afficherRegles()  # Appel d'une nouvelle méthode pour afficher les crédits
            
            pygame.display.flip()
            
    
    

    def afficherRegles(self):
        #print("Boup")
        police = pygame.font.Font(None, 24)
        couleur_texte = "white"
        
        continuer = True
        
        self.screen.fill("black")
        
        noms_texte = pygame.font.SysFont("cambria", 30).render("Règles :", 1, (255, 255, 255))
        debut = pygame.font.SysFont("cambria", 24).render("Appuyer sur les flèches de votre clavier en rythme", 1, (255, 255, 255))
        suite = pygame.font.SysFont("cambria", 24).render("Vous affrontez à chaque niveau un boss et devez obtenir plus de points que lui", 1, (255, 255, 255))
        suite2 = pygame.font.SysFont("cambria", 24).render("Et répondre à des questions posées par le boss", 1, (255, 255, 255))
        
        nom_rect = noms_texte.get_rect(center=(640, 100))
        debut_rect = debut.get_rect(center=(640, 150))
        suite_rect = suite.get_rect(center=(640, 200))
        suite2_rect = suite2.get_rect(center=(640, 250))
        
        while continuer:
            
            souris_utilisateur = pygame.mouse.get_pos()

            # Affichage des noms, par exemple :
            


            # Rafraîchissement de la fenêtre
            pygame.display.flip()
            self.screen.blit(noms_texte, nom_rect)
            self.screen.blit(debut, debut_rect)
            self.screen.blit(suite, suite_rect)
            self.screen.blit(suite2, suite2_rect)

            bouton_menu_principal = bouton.Bouton(200, 50, "Menu Principal")

            bouton_menu_principal.changeColor(souris_utilisateur)
            bouton_menu_principal.maj()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    continuer = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_menu_principal.checkForInput(souris_utilisateur):
                        # Retour au menu principal
                        self.menu_prinipal()
                        return  # Arrête la boucle actuelle

            pygame.display.flip()
        
    def afficherCreditsDyn(self):
        continuer = True
        noms = [
            ("Responsable graphique : Evann Colin", 620),  # Commence en bas de l'écran
            ("Développeurs : Naël Ben Hamida -- Pharabot, Axelle Broyer, Martin Loudoueineix", 670),
            ("Responsable storyboard : Martin Loudoueineix", 720)
            ("Musique d'accueil : Mexico, Alestorm", 720)
            ("Musique boss PHP : Seven Nation Army, The White Stripes", 720)
            ("Musique boss C++ : My melody my rules, Claerorn", 720)
            ("Musique boss Maths : Through The Fire And Flames, DragonForce", 720)
            ("Musique boss Réseau : Lone Digger, Caravan Palace", 720)
            ("Musique boss Shell : Hayloft, Mother Mother", 720)
        ]

        while continuer:
            
            self.screen.fill("black")
            souris_utilisateur = pygame.mouse.get_pos()
            
            # Test chargement du bg 
            
            

            # Affichage des noms qui montent de bas en haut
            noms_texte = pygame.font.SysFont("cambria", 30).render("Crédits:", 1, (255, 255, 255))
            noms_rect = noms_texte.get_rect(center=(640, 100))
            self.screen.blit(noms_texte, noms_rect)

            bouton_menu_principal = bouton.Bouton(200, 50, "Menu Principal")
            bouton_menu_principal.changeColor(souris_utilisateur)
            bouton_menu_principal.maj()

            # Mettre à jour la position verticale des noms et les afficher
            for nom, y_pos in noms:
                nom_texte = pygame.font.SysFont("cambria", 24).render(nom, 1, (255, 255, 255))
                nom_rect = nom_texte.get_rect(center=(640, y_pos))
                self.screen.blit(nom_texte, nom_rect)
                # Mettre à jour la position verticale pour les faire monter
                y_pos -= 1

            # Supprimer les noms qui ont atteint le haut de la page
            noms = [(nom, y_pos) for nom, y_pos in noms if y_pos > 0]  # Supprimer si la position est au-dessus de 0 (haut de l'écran)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    continuer = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_menu_principal.checkForInput(souris_utilisateur):
                        # Retour au menu principal
                        self.menu_prinipal()
                        return  # Arrête la boucle actuelle

            pygame.display.flip()


            
            
    def afficherCredits(self):
        continuer = True

        while continuer:
            self.screen.fill("black")
            souris_utilisateur = pygame.mouse.get_pos()

            # Affichage des noms, par exemple :
            noms_texte = pygame.font.SysFont("cambria", 30).render("Crédits:", 1, (255, 255, 255))
            nom2 = pygame.font.SysFont("cambria", 24).render("Nom 2", 1, (255, 255, 255))
            nom3 = pygame.font.SysFont("cambria", 24).render("Nom 3", 1, (255, 255, 255))
            
            nom1 = pygame.font.SysFont("cambria", 24).render("Responsable graphique : Evann Colin", 1, (255, 255, 255))  # Commence en bas de l'écran
            nom2 = pygame.font.SysFont("cambria", 24).render("Développeurs : Naël Ben Hamida -- Pharabot, Axelle Broyer, Martin Loudoueineix", 1, (255, 255, 255))
            nom3 = pygame.font.SysFont("cambria", 24).render("Responsable storyboard : Martin Loudoueineix",  1, (255, 255, 255))
            nom4 = pygame.font.SysFont("cambria", 24).render("Musique d'accueil : Mexico, Alestorm",  1, (255, 255, 255))
            nom5 = pygame.font.SysFont("cambria", 24).render("Musique boss PHP : Seven Nation Army, The White Stripes",  1, (255, 255, 255))
            nom6 = pygame.font.SysFont("cambria", 24).render("Musique boss C++ : My melody my rules, Claerorn",  1, (255, 255, 255))
            nom7 = pygame.font.SysFont("cambria", 24).render("Musique boss Maths : Through The Fire And Flames, DragonForce",  1, (255, 255, 255))
            nom8 = pygame.font.SysFont("cambria", 24).render("Musique boss Réseau : Lone Digger, Caravan Palace",  1, (255, 255, 255))
            nom9 = pygame.font.SysFont("cambria", 24).render("Musique boss Shell : Hayloft, Mother Mother",  1, (255, 255, 255))

            noms_rect = noms_texte.get_rect(center=(640, 100))
            nom1_rect = nom1.get_rect(center=(640, 150))
            nom2_rect = nom2.get_rect(center=(640, 200))
            nom3_rect = nom3.get_rect(center=(640, 250))
            nom4_rect = nom3.get_rect(center=(640, 300))
            nom5_rect = nom3.get_rect(center=(640, 350))
            nom6_rect = nom3.get_rect(center=(640, 400))
            nom7_rect = nom3.get_rect(center=(640, 450))
            nom8_rect = nom3.get_rect(center=(640, 500))
            nom9_rect = nom3.get_rect(center=(640, 550))


            self.screen.blit(noms_texte, noms_rect)
            self.screen.blit(nom1, nom1_rect)
            self.screen.blit(nom2, nom2_rect)
            self.screen.blit(nom3, nom3_rect)
            self.screen.blit(nom4, nom4_rect)
            self.screen.blit(nom5, nom5_rect)
            self.screen.blit(nom6, nom6_rect)
            self.screen.blit(nom7, nom7_rect)
            self.screen.blit(nom8, nom8_rect)
            self.screen.blit(nom9, nom9_rect)

            bouton_menu_principal = bouton.Bouton(200, 50, "Menu Principal")

            bouton_menu_principal.changeColor(souris_utilisateur)
            bouton_menu_principal.maj()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    continuer = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_menu_principal.checkForInput(souris_utilisateur):
                        # Retour au menu principal
                        self.menu_prinipal()
                        return  # Arrête la boucle actuelle

            pygame.display.flip()
    
    
    
    def selectionNiveau(self): # rajouter lock pour ceux pas débloquer 

        continuer = True
        
        self.screen.fill("black")
        boutons = []
        
        bouton_menu_principal = bouton.Bouton(200, 50, "Menu Principal")
        
        # Charger une police de texte
        police = pygame.font.Font(None, 36)

    
        titre_menu = pygame.font.SysFont("cambria", 50).render((str) ("SELECT YOUR LEVEL"),10,(255,255,255))
        fond_titre = titre_menu.get_rect(center=(640, 100))
        self.screen.blit(titre_menu, fond_titre)
        
        # Rectangle pour les flèches de gauche et de droite
        largeur, hauteur, ecartMur = 50,100,50
        

        # Créer une liste d'objets Niveau pour chaque niveau
        indexMax = len(self.niveaux) -1  # Pour savoir qd flèche doit faire quoi
        currentIndex = 0
        horloge = pygame.time.Clock()
        
        titre_menu = pygame.font.SysFont("cambria", 50).render((str) ("SELECT YOUR LEVEL"),10,(255,255,255))
        fond_titre = titre_menu.get_rect(center=(640, 100))
        self.screen.blit(titre_menu, fond_titre)
        
        self.niveaux[currentIndex].setDebloquer()
        
        while continuer:
            
            souris_utilisateur = pygame.mouse.get_pos()
            bouton_menu_principal.changeColor(souris_utilisateur)
            bouton_menu_principal.maj()

            self.screen.fill("black")
            
            # Affiche le numéro du niveau et le nom du boss
            
            niveau_actuel = self.niveaux[currentIndex]
            if (niveau_actuel.getDebloquer()):
                debloquer = " | DÉBLOQUÉ"
            else:
                debloquer = " | BLOQUÉ"
                
            
            niveau_texte = pygame.font.SysFont("cambria", 36).render(f"Niveau {niveau_actuel.get_num()}: {niveau_actuel.get_boss().getNom()}" + debloquer, 1, (255, 255, 255))
            niveau_rect = niveau_texte.get_rect(center=(self.screen.get_width() // 2, 100))
            self.screen.blit(niveau_texte, niveau_rect)
            
            # Affiche l'image du boss
            

            
            img_boss = pygame.image.load(niveau_actuel.get_boss().getImgPersoAt(0))
            desired_width, desired_height = 300,300
            img_boss = pygame.transform.scale(img_boss, (desired_width, desired_height))
            img_rect = img_boss.get_rect(center=(self.screen.get_width() // 2, self.screen.get_height() // 2))
            self.screen.blit(img_boss, img_rect)
        

            
            # Crée et affiche les boutons "Previous" et "Next"
            bouton_previous = bouton.Bouton(150, self.screen.get_height() - 50, "Précédent")
            bouton_menu_principal = bouton.Bouton(200, 50, "Menu Principal")
            bouton_next = bouton.Bouton(self.screen.get_width() - 150, self.screen.get_height() - 50, "Suivant")
            
            for button in [bouton_previous,bouton_menu_principal, bouton_next]:
                button.changeColor(souris_utilisateur)
                button.maj()
                
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    continuer = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if bouton_previous.checkForInput(souris_utilisateur):
                        # Gérer le passage au niveau précédent
                        if currentIndex > 0:
                            currentIndex -= 1
                    elif bouton_next.checkForInput(souris_utilisateur):
                        # Gérer le passage au niveau suivant
                        if currentIndex < indexMax:
                            currentIndex += 1
                    elif niveau_actuel.getDebloquer() and img_rect.collidepoint(event.pos):
                        pygame.mixer.music.pause()
                        self.loadNiveau(niveau_actuel,currentIndex)  # Charger le niveau en cliquant sur l'image du boss
                    elif bouton_menu_principal.checkForInput(souris_utilisateur):
                        pygame.mixer.music.pause()
                        self.menu_prinipal() # Retourner au menu principal en cliquant sur le bouton "Menu Principal"
                        


            pygame.display.flip()
            horloge.tick(60)  # Limite la fréquence d'images à 60 FPS
                
            
            
    def loadNiveau(self, current_niveau, currentIndex):
        
        #current_niveau.set_score_necessaire(30)
        
        if (current_niveau.get_boss().getMusic() != None):
            #pygame.mixer.init()
            pygame.mixer.music.load(current_niveau.get_boss().getMusic()) # current_niveau.get_boss().getMusic()
            pygame.mixer.music.set_volume(0.2)
            pygame.mixer.music.play()
        
        #Permet de remttre toute les flèches à l'ordonnée initiale
        for f in current_niveau.get_fleches():
            f.set_ordonnee(600)

        continuer = True
        temps = time.time()
        fleches_affichage = []

        boutons = []

        bouton_retour = bouton.Bouton(self.screen.get_width()//2, self.screen.get_height() -30,"RETOUR")
        boutons.append(bouton_retour)


        image_joueur = ["./Img/JP/JP_classsic0.png", "./Img/JP/JP_classsic1.png", "./Img/JP/JP_classsic2.png", "./Img/JP/JP_classsic3.png", 
                        "./Img/JP/JP_classsic4.png", "./Img/JP/JP_classsic5.png"]
        
        image_boss = current_niveau.get_boss().getImgPerso()
        
        #Trying to have a good bg for boss
        imageBgBoss = pygame.image.load(current_niveau.get_decor())
        largeurBgBoss, hauteurBgBoss = self.screen.get_width(), self.screen.get_height()
        imageBgBoss = pygame.transform.scale(imageBgBoss, (largeurBgBoss, hauteurBgBoss))
        
        while continuer :

            #self.screen.fill("black")
            #self.screen.blit(self.background, (-10,-60))

            souris_utilisateur = pygame.mouse.get_pos()
            
            
            self.screen.blit(imageBgBoss, (0, 0))

            
            
            #print(current_niveau.get_current_fleche())

            if(time.time() - temps >= current_niveau.get_fleche(current_niveau.get_current_fleche()).get_apparition()):

                if(current_niveau.get_fleche(current_niveau.get_current_fleche()) not in fleches_affichage):
                    fleches_affichage.append(current_niveau.get_fleche(current_niveau.get_current_fleche()))
                    #print (fleches_affichage)
                if(not current_niveau.fin()):
                    current_niveau.next_fleche()
            

            for i in range (1,(len(fleches_affichage))+1):
                # Mise à jour de la position de la flèche
                fleches_affichage[-i].set_ordonnee(fleches_affichage[-i].get_ordonnee() - 5)
                self.screen.blit(pygame.image.load(fleches_affichage[-i].get_img_fleche()).convert(), (fleches_affichage[-i].get_absisse(), fleches_affichage[-i].get_ordonnee()))
                self.screen.blit(pygame.image.load(fleches_affichage[-i].get_img_fleche()).convert(), (fleches_affichage[-i].get_absisse()+810, fleches_affichage[-i].get_ordonnee()))

                if (fleches_affichage[-i].get_ordonnee() <= 20):
                    fleches_affichage.pop(-i)

            for sprite_joueur in image_joueur:
                joueur = pygame.image.load(sprite_joueur).convert()
                self.screen.blit(joueur, (10, 600))
                
                
            
            for sprite_joueur in image_boss:
                bossSpritos = pygame.image.load(sprite_joueur).convert()
                image_rect_b = bossSpritos.get_rect()
                image_rect_b.bottomright = (self.screen.get_width() -10 , self.screen.get_height() -10)
                self.screen.blit(bossSpritos, image_rect_b)


            #Lorsque que la phase de rythme est terminée
            if(current_niveau.fin() and len(fleches_affichage) == 0) :

                #On pose toutes les question de culture générale à l'utilisateur
                for question in current_niveau.get_questions() :

                    self.screen.fill("black")
                    boutons_question = []

                    #Tant que l'utilisateur n'a pas répondu, on affiche les question
                    while question.get_reponse_utilisateur() is None :

                        font=pygame.font.Font(None, 50)
                        souris_utilisateur = pygame.mouse.get_pos()

                        #Liste des réponses pour une question
                        key_list = [k  for (k, val) in question.get_reponses().items()]
                        
                        current_question = font.render(question.get_intitule(),1,(255,255,255))
                        #On créer un bouton par réponse
                        reponse1 = bouton.Bouton(600,400,key_list[0])
                        reponse2 = bouton.Bouton(600,500,key_list[1])
                        reponse3 = bouton.Bouton(600,600,key_list[2])
                        reponse4 = bouton.Bouton(600,700,key_list[3])

                        boutons_question.append(reponse1)
                        boutons_question.append(reponse2)
                        boutons_question.append(reponse3)
                        boutons_question.append(reponse4)

                        self.screen.blit(current_question, (500, 300))
                        pygame.display.flip()

                        #Gestion de la mise à jour des boutons
                        for button in boutons_question :
                            button.changeColor(souris_utilisateur)
                            button.maj()

                        for event in pygame.event.get():

                            #Fermeture par fermeture de fenêtre
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                continuer = False

                            if event.type == pygame.MOUSEBUTTONDOWN:
                                #on enregistre la réponse choisie par l'utilisateur
                                if(reponse1.checkForInput(souris_utilisateur)):
                                    question.set_reponse_utilisateur(question.get_reponses()[reponse1.get_texte()])
                                if(reponse2.checkForInput(souris_utilisateur)):
                                    question.set_reponse_utilisateur(question.get_reponses()[reponse2.get_texte()])
                                if(reponse3.checkForInput(souris_utilisateur)):
                                    question.set_reponse_utilisateur(question.get_reponses()[reponse3.get_texte()])
                                if(reponse4.checkForInput(souris_utilisateur)):
                                    question.set_reponse_utilisateur(question.get_reponses()[reponse4.get_texte()])

                # Pour débloquer le lvl suivant
                current_niveau.setIsWon() # Pas très joli car fait le etst 2x mais ça marche et pas le tps
                if (current_niveau.getIsWon()):
                    if ( currentIndex +1 < len(self.niveaux)) :
                        self.niveaux[currentIndex +1].setDebloquer()

                    

                #Une fois que toutes les questions ont été répondues, on réinitialise le fond pour afficher le score
                self.screen.fill("black")

                #Affichage du score 
                score = pygame.font.Font(None, 30).render(("Score : " + (str) (current_niveau.total_score() + current_niveau.get_score())),1,(255,255,255))
                self.screen.blit(score, (500, 300))
                pygame.display.flip()



            pygame.display.flip()


            #Gestion de l'actualisation des boutons

            for button in boutons :
                button.changeColor(souris_utilisateur)
                button.maj()

            #Gestion des évènements

            for event in pygame.event.get():

                #Fermeture par fermeture de fenêtre
                if event.type == pygame.QUIT:
                    pygame.quit()
                    continuer = False

                if event.type == pygame.MOUSEBUTTONDOWN:
                    #Changement de fenêtre pour l'écran titre
                    if(bouton_retour.checkForInput(souris_utilisateur)):
                        pygame.mixer.music.pause()
                        self.selectionNiveau()
                        
                
                if event.type == pygame.KEYDOWN:
                    
                    #Pour éviter d'avoir un soucis de liste videfleches_affichage[0].get_ordonnee()
                    if(len(fleches_affichage)>0):

                        if (event.key == pygame.K_UP and fleches_affichage[0].get_direction() == "UP") :
                            if(fleches_affichage[0].get_score_modifiable()):
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('./songs/caisse_claire.wav'))
                                current_niveau.add_score(fleches_affichage[0].calcul_score(fleches_affichage[0].get_ordonnee(), 50))
                        else:
                            fleches_affichage[0].set_score(0)
                    
                        if (event.key == pygame.K_DOWN and fleches_affichage[0].get_direction() == "DOWN") :
                            if(fleches_affichage[0].get_score_modifiable()):
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('./songs/charleston.wav'))
                                current_niveau.add_score(fleches_affichage[0].calcul_score(fleches_affichage[0].get_ordonnee(), 160))
                        else:
                            fleches_affichage[0].set_score(0)

                        if (event.key == pygame.K_LEFT and fleches_affichage[0].get_direction() == "LEFT") :
                            if(fleches_affichage[0].get_score_modifiable()):
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('./songs/grosse_caisse.mp3'))
                                current_niveau.add_score(fleches_affichage[0].calcul_score(fleches_affichage[0].get_ordonnee(), 110))
                        else:
                            fleches_affichage[0].set_score(0)
                        
                        if (event.key == pygame.K_RIGHT and fleches_affichage[0].get_direction() == "RIGHT") :
                            if(fleches_affichage[0].get_score_modifiable()):
                                pygame.mixer.Channel(1).play(pygame.mixer.Sound('./songs/tambour.wav'))
                                current_niveau.add_score(fleches_affichage[0].calcul_score(fleches_affichage[0].get_ordonnee(), 110))
                        else:
                            fleches_affichage[0].set_score(0)
                    
            
            pygame.display.flip()
            

            
        def imgAnimation(self):
            print("boup")
        
    

def main():
    # Initialisation de pygame
    pygame.init()
    # Initalisation du module de gestion des fonts
    pygame.font.init()
    #Initialisation pour le son
    pygame.mixer.init()

    # Donne un nom à la fenêtre 
    pygame.display.set_caption("Le monde merveilleux de l'IUT")
    
    
    # Definition de la taille de l'écran
    largeur, hauteur = 1200, 720
    screen = pygame.display.set_mode((largeur, hauteur))
    
    # Creé un objet horloge pour gerer le temps entre deux images
    clock = pygame.time.Clock()
    # Nombre de millisecondes entre deux images 
    dt = 0
    
    # Creation du jeu
    jeu = Jeu(screen)
    
        
    
    
    # Fin utilisation de pygame
    pygame.quit()
    
            
            

#Appel automatiquement la fonction main si pas utilisé comme module
if __name__ == "__main__":
    main()       
    
def test():

    listeDicoBoss = Outil.selectAttributsInFile("./fichierTexte/boss.txt", "img_perso")
    listeBoss = []
    for elem in listeDicoBoss :
        currentBoss = boss.Boss()
        listeBoss.append(currentBoss.setAll(elem))
        print("Nom : ", currentBoss.getNom())
        print("Taux : ", currentBoss.getTauxReussite())
        print("Img : ", currentBoss.getImgPersoAt(0))
    
    # Creation des background à la main (mais faire par fichier après)
    listeBg = ["./background_game.png","./background_game1.png"]
    
    if len(listeBoss) > len(listeBg) : _max = len(listeBg)
    else : _max = len(listeBoss)
    
    # Creation liste de niveaux
    niveaux = []
    
    print(listeBoss[0])
    
    
    for i in range(_max) :
        niveaux.append(niveau.Niveau(i+1, listeBg[i], listeBoss[i]))
        
    for i in range(_max):
        print(niveaux[i])
        #print(niveaux[i].get_boss())
        
#test()

    