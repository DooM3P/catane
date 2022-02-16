# from Tkinter import *
from monjeu2 import *
from fenetres import *

# generation du plateau de jeu
hexagoneCourant=Hexagone(jeu.ile,0,0,"brown",8)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,jeu.ile.taille,0,"yellow",8)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,(jeu.ile.taille)/2,(-(jeu.ile.taille)/2)*(3**(0.5)),"dark grey",3)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,-(jeu.ile.taille)/2,(-(jeu.ile.taille)/2)*(3**(0.5)),"green",4)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,-(jeu.ile.taille),0,"white",0)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,-(jeu.ile.taille)/2,((jeu.ile.taille)/2)*(3**(0.5)),"light green",5)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,(jeu.ile.taille)/2,((jeu.ile.taille)/2)*(3**(0.5)),"green",10)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,(jeu.ile.taille)*(1.5),(jeu.ile.taille)/2*(3**(0.5)),"light green",11)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,(jeu.ile.taille)*2,0,"green",10)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,(jeu.ile.taille)*(1.5),(-(jeu.ile.taille)/2)*(3**(0.5)),"brown",2)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,jeu.ile.taille,-(jeu.ile.taille)*(3**(0.5)),"green",11)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,0,-(jeu.ile.taille)*(3**(0.5)),"light green",12)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,-(jeu.ile.taille),-(jeu.ile.taille)*(3**(0.5)),"yellow",4)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,-(jeu.ile.taille)*(1.5),(-(jeu.ile.taille)/2)*(3**(0.5)),"light green",6)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,-(jeu.ile.taille)*2,0,"dark grey",9)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,-(jeu.ile.taille)*(1.5),(jeu.ile.taille)/2*(3**(0.5)),"brown",3)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,-(jeu.ile.taille),jeu.ile.taille*(3**(0.5)),"yellow",9)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,0,jeu.ile.taille*(3**(0.5)),"dark grey",6)
jeu.ile.ajouterhexagone(hexagoneCourant)
hexagoneCourant=Hexagone(jeu.ile,jeu.ile.taille,jeu.ile.taille*(3**(0.5)),"yellow",5)
jeu.ile.ajouterhexagone(hexagoneCourant)

#jeu.ile.affiche()
#for i in jeu.ile.sommetscoord.keys():
    #print jeu.ile.sommetscoord[i].num,"x :", jeu.ile.sommetscoord[i].x,"y :", jeu.ile.sommetscoord[i].y

#gestionnaire principal des changements de fenetres

root = Tk ()
class gestionnaireFenetres:
    def __init__(self, _root):
        self.root=_root
        self.fenetreCourante=board()#le plateau
        self.fenetreCourante2=config(self)# le coin inferieur droit, zone de commandes
        self.fenetreCourante3=score(self)# le panneau de score et des matieres premieres
        menubar = Menu()
        menubar.add_command(label="Info Jeu", command=self.info)
        menubar.add_command(label="Cartes Developpement", command=self.cartes)
        menubar.add_command(label="Quit", command=root.quit)
        root.config(menu=menubar)
    def info(self):#Option uniquement presente dans un but de deboguage pas forcement utile pour le joueur
        print(jeu.listjoueurs)
        for i in jeu.listjoueurs.keys():
            print(jeu.listjoueurs[i].villages)
        print(jeu.ile.routes.keys())
        for i in jeu.ile.routes.keys():
            print(jeu.ile.routes[i].color, i)

    def cartes(self): # le menu des cartes developpement
        if not jeu.currentcolor == "":
            self.fenetreCourante3=cartes(self, self.root)
    def loadFenetreSuivante(self,nomFenetre):
        if nomFenetre=="config2": #choix des ordinateurs
            self.fenetreCourante2=config2(self)
        if nomFenetre=="color": #choix des couleurs de chaque joueur
            self.fenetreCourante2=color(self)
        if nomFenetre=="build": #construction des colonies initiales
            self.fenetreCourante2=build(self)
        if nomFenetre=="road": #construction des routes initiales
            self.fenetreCourante2=road(self)
        if nomFenetre=="game1": #tour de jeu : lancer de des
            self.fenetreCourante2=game1(self)
        if nomFenetre=="game2": #tour de jeu : choix des actions
            self.fenetreCourante2=game2(self)
        if nomFenetre=="road2": #poser des routes
            self.fenetreCourante2=road2(self)
        if nomFenetre=="colonie": # poser des colonies
            self.fenetreCourante2=colonie(self)
        if nomFenetre=="ville": # poser des villes
            self.fenetreCourante2=ville(self)
        if nomFenetre=="trade": # commercer
            self.fenetreCourante8=trade(self.root)
        if nomFenetre=="monop": # choix de carte "monopole"
            self.fenetreCourante8=monop(self.root)
        if nomFenetre=="discov": # choix de carte "decouverte"
            self.fenetreCourante8=discov(self.root)
        if nomFenetre=="rogue": # le brigand
            self.fenetreCourante8=rogue(self)

interface=gestionnaireFenetres(root)
root.mainloop()
