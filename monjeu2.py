from Tkinter import *
import random

class Jeu:
    def __init__ (self, _ile):
        self.ile=_ile
        self.njoueurs=0#nombre de joueurs
        self.ncpu=0#nombre d'ordinateurs
        self.colors=["Bleu", "Rouge", "Jaune", "Orange", "Vert"]#liste des couleurs a choisir
        self.currentcolor=""#couleur du joueur dont c'est le tour
        self.de=0#le resultat des des
        self.plyrcount=0#un compteur
        self.plyrcount2=0#un autre compteur
        self.listjoueurs={}
        self.order=[]#les des des joueurs ranges dans l'ordre, pour determiner la rotation des tours de jeu
        self.cards=["Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Chevalier","Victoire","Victoire","Victoire","Victoire","Victoire","Monopole", "Decouverte", "Decouverte", "Decouverte", "Monopole", "Monopole"]
        self.cards=random.sample(self.cards,len(self.cards)) #on bat les cartes
        self.numbackup=(0,0,0)#stocke le numero du sommet avant occupation par le brigand
        self.chevalier=0
    def transcolor (self, _couleur):#attribue au joueur, dont la couleur est en francais, sa couleur "informatique" (utile pour les routes)
        color = "grey"
        if _couleur == "Bleu": color = "blue"
        if _couleur == "Rouge": color = "red"
        if _couleur == "Jaune": color = "yellow"
        if _couleur == "Orange": color = "orange"
        if _couleur == "Vert": color = "dark green"
        return color
    def findplyr (self, _listjoueurs, _numde): #trouve le joueur dont c'est le de dans "order"
        for i in _listjoueurs.keys():
            if _numde==_listjoueurs[i].numplyr:
                return _listjoueurs[i].color
    def find (self, _listjoueurs):#donne un de au joueur en evitant les repetitions
        for i in range (0,1000):
            a =self.testde(_listjoueurs)
            if  a != 0:
                return a
    def testde (self, _listjoueurs):#verifie les des deja tombes
        a=random.randint(1,6)+random.randint(1,6)
        for i in _listjoueurs.keys():
            if a == _listjoueurs[i].numplyr:
                return 0
        return a
    def des (self):
        a=random.randint(1,6)+random.randint(1,6)
        return a
    def routeverif (self, _num, _numans, _jeu):#verifie que les deux "bouts" d'une route sont proches
        for i in _jeu.ile.sommets[_num].listsuccess:
            if i.num == _numans:
                return 1
        return 0
    def compteur (self, _jeu, _gestionfenetres):#le decompte des points
        for i in _jeu.listjoueurs.keys():
            compteur = 0
            for j in _jeu.listjoueurs[i].villages.keys():
                if _jeu.listjoueurs[i].villages[j].constr[0]==1:
                    compteur += 1
                if _jeu.listjoueurs[i].villages[j].constr[0]==2:
                    compteur += 2
            if _jeu.listjoueurs[i].knight > 2 and _jeu.chevalier == 0:
                _jeu.listjoueurs[i].knight2 = 2
                _jeu.chevalier +=1
            _jeu.listjoueurs[i].pts.set(compteur+_jeu.listjoueurs[i].victory+_jeu.listjoueurs[i].knight2)
            if _jeu.listjoueurs[i].pts.get() > 8:
                print "LE JOUEUR "+str(_jeu.listjoueurs[i].color)+" EST LE VAINQUEUR !"
    def monop (self,_fenetre, _matiere):#la carte monopole donne toutes les matieres d'un type au joueur qui la joue
        compteur=0
        if _matiere == "bois":
            for i in self.listjoueurs.keys():
                compteur = compteur + self.listjoueurs[i].bois.get()
                self.listjoueurs[i].bois.set(0)
            self.listjoueurs[self.currentcolor].bois.set(compteur)
        if _matiere == "argile":
            for i in self.listjoueurs.keys():
                compteur = compteur + self.listjoueurs[i].argile.get()
                self.listjoueurs[i].argile.set(0)
            self.listjoueurs[self.currentcolor].argile.set(compteur)
        if _matiere == "ble":
            for i in self.listjoueurs.keys():
                compteur = compteur + self.listjoueurs[i].ble.get()
                self.listjoueurs[i].ble.set(0)
            self.listjoueurs[self.currentcolor].ble.set(compteur)
        if _matiere == "laine":
            for i in self.listjoueurs.keys():
                compteur = compteur + self.listjoueurs[i].laine.get()
                self.listjoueurs[i].laine.set(0)
            self.listjoueurs[self.currentcolor].laine.set(compteur)
        if _matiere == "minerai":
            for i in self.listjoueurs.keys():
                compteur = compteur + self.listjoueurs[i].minerai.get()
                self.listjoueurs[i].minerai.set(0)
            self.listjoueurs[self.currentcolor].minerai.set(compteur)
        _fenetre.destroy()
    def discov (self, _fenetre, _matiere):#carte decouverte, donne deux de matiere a un joueur
        if _matiere == "bois":
            self.listjoueurs[self.currentcolor].bois.set(self.listjoueurs[self.currentcolor].bois.get()+2)
        if _matiere == "argile":
            self.listjoueurs[self.currentcolor].argile.set(self.listjoueurs[self.currentcolor].argile.get()+2)
        if _matiere == "ble":
            self.listjoueurs[self.currentcolor].ble.set(self.listjoueurs[self.currentcolor].ble.get()+2)
        if _matiere == "laine":
            self.listjoueurs[self.currentcolor].laine.set(self.listjoueurs[self.currentcolor].laine.get()+2)
        if _matiere == "minerai":
            self.listjoueurs[self.currentcolor].minerai.set(self.listjoueurs[self.currentcolor].minerai.get()+2)
        _fenetre.destroy()
class Joueur:
    def __init__ (self, _numplyr, _cpu, _color):
        self.numplyr=_numplyr
        self.cpu=_cpu
        self.color=_color
        self.pts=IntVar ()
        self.pts.set (0)
        self.villages={}
        self.bois = IntVar ()
        self.bois.set (0)
        self.argile = IntVar ()
        self.argile.set (0)
        self.ble = IntVar ()
        self.ble.set (0)
        self.laine = IntVar ()
        self.laine.set (0)
        self.minerai = IntVar ()
        self.minerai.set (0)
        self.cards=[0,0,0,0,0]#Victoire, Chevalier, Monopole, Decouverte, Route
        self.victory=0 #cartes point victoire revelees
        self.knight=0 #cartes chevalier revelees
        self.knight2=0 #premier (et dernier) a accumuler les 3 cartes chevalier
class Ile:#contient des fonctions de l'interface de jeu comme de creation du plateau
    def __init__ (self):
        self.hexacoord={}#hexagones par coordonnees
        self.hexanumde={}#par numero de de
        self.sommets={}#liste des sommets
        self.sommetscoord={}#sommets par coordonees
        self.routes={}
        self.taille=42#taille des hexagones
        self.nbhexaposes=0
    def income (self, _des, _listjoueurs):#revenus des joueurs...
        if self.hexanumde.has_key(_des):
            for i in self.hexanumde[_des]:
                if not i.numde == 7:
                    self.sommet(i,i.sommet1, _listjoueurs)
                    self.sommet(i,i.sommet2, _listjoueurs)
                    self.sommet(i,i.sommet3, _listjoueurs)
                    self.sommet(i,i.sommet4, _listjoueurs)
                    self.sommet(i,i.sommet5, _listjoueurs)
                    self.sommet(i,i.sommet6, _listjoueurs)
    def sommet (self, _i, _sommet, _listjoueurs):#combien rapporte chaque sommet (distinction vide/colonie/ville)
        if _sommet.constr[0] != 0:
            if _sommet.constr[0] == 1:
                if _i.matiere == "green":
                    _listjoueurs[_sommet.constr[1]].bois.set(_listjoueurs[_sommet.constr[1]].bois.get()+1)
                if _i.matiere == "brown":
                    _listjoueurs[_sommet.constr[1]].argile.set(_listjoueurs[_sommet.constr[1]].argile.get()+1)
                if _i.matiere == "yellow":
                    _listjoueurs[_sommet.constr[1]].ble.set(_listjoueurs[_sommet.constr[1]].ble.get()+1)
                if _i.matiere == "light green":
                    _listjoueurs[_sommet.constr[1]].laine.set(_listjoueurs[_sommet.constr[1]].laine.get()+1)
                if _i.matiere == "dark grey":
                    _listjoueurs[_sommet.constr[1]].minerai.set(_listjoueurs[_sommet.constr[1]].minerai.get()+1)
            if _sommet.constr[0] == 2:
                if _i.matiere == "green":
                    _listjoueurs[_sommet.constr[1]].bois.set(_listjoueurs[_sommet.constr[1]].bois.get()+2)
                if _i.matiere == "brown":
                    _listjoueurs[_sommet.constr[1]].argile.set(_listjoueurs[_sommet.constr[1]].argile.get()+2)
                if _i.matiere == "yellow":
                    _listjoueurs[_sommet.constr[1]].ble.set(_listjoueurs[_sommet.constr[1]].ble.get()+2)
                if _i.matiere == "light green":
                    _listjoueurs[_sommet.constr[1]].laine.set(_listjoueurs[_sommet.constr[1]].laine.get()+2)
                if _i.matiere == "dark grey":
                    _listjoueurs[_sommet.constr[1]].minerai.set(_listjoueurs[_sommet.constr[1]].minerai.get()+2)

    def somtest (self, _num, _success): #le sommet voisin est-il deja construit ?
        for i in _success:
            if self.sommets[i.num].constr[0] != 0:
                return 1
        return 0
    def somtest2 (self, _num, _currentcolor, _jeu):#le sommet a t-il une route qui y mene ?
        for i in _jeu.ile.sommets[_num].listsuccess:
            if _jeu.ile.routes.has_key((i.num, _num)) and _jeu.ile.routes[(i.num, _num)].color==_currentcolor:
                return 1
            if _jeu.ile.routes.has_key((_num, i.num)) and _jeu.ile.routes[(_num, i.num)].color==_currentcolor:
                return 1
        return 0
    def routetest (self, _bout1, _bout2, _currentcolor, _jeu):# y a t-il une route ou une colonie a l'un de ces deux bouts ?
        if _jeu.ile.sommets[_bout1].constr[1]==_currentcolor:
            return 1
        else:
            for i in _jeu.ile.sommets[_bout1].listsuccess:
                if _jeu.ile.routes.has_key((i.num, _bout1)) and _jeu.ile.routes[(i.num, _bout1)].color==_currentcolor:
                        return 1
                if _jeu.ile.routes.has_key((_bout1, i.num)) and _jeu.ile.routes[(_bout1, i.num)].color==_currentcolor:
                        return 1
        if _jeu.ile.sommets[_bout2].constr[1]==_currentcolor:
            return 1
        else:
            for i in _jeu.ile.sommets[_bout2].listsuccess:
                if _jeu.ile.routes.has_key((i.num, _bout2)) and _jeu.ile.routes[(i.num, _bout2)].color==_currentcolor:
                        return 1
                if _jeu.ile.routes.has_key((_bout2, i.num)) and _jeu.ile.routes[(_bout2, i.num)].color==_currentcolor:
                        return 1
        return 0
    def affiche(self): #fonction qui affichait les hexagones crees (pour le deboguage)
        listeHexagones=self.hexacoord.values()
        for hexagone in listeHexagones: print hexagone
        for sommet in self.sommets.values():
            chaine=""
            chaine+="sommet:"+str(sommet.num)+" successeurs:"
            for s in sommet.listsuccess:
                chaine+=" "+str(s.num)+" "
            print chaine
    def ajouterhexagone (self, hexagone):
        self.nbhexaposes=self.nbhexaposes+1
        self.hexacoord[hexagone.x, hexagone.y]=hexagone
        if self.hexanumde.has_key(hexagone.numde): #creation de la liste hexanumde avec ajout a une cle deja existante ou creation de la cle
            self.hexanumde[hexagone.numde].append(hexagone)
        else :
            self.hexanumde[hexagone.numde]=[hexagone]
    def hasHexagoneHautGauche(self,x,y):
        return self.hexacoord.has_key((x-self.taille/2,y+(3**(0.5))*self.taille/2))
    def getHexagoneHautGauche(self,x,y):
        if self.hexacoord.has_key((x-self.taille/2,y+(3**(0.5))*self.taille/2)):
            return self.hexacoord[(x-self.taille/2,y+(3**(0.5))*self.taille/2)]
        else: return None

    def hasHexagoneHautDroite(self,x,y):
        return self.hexacoord.has_key((x+self.taille/2,y+(3**(0.5))*self.taille/2))

    def getHexagoneHautDroite(self,x,y):
        if self.hexacoord.has_key((x+self.taille/2,y+(3**(0.5))*self.taille/2)):
            return self.hexacoord[(x+self.taille/2,y+(3**(0.5))*self.taille/2)]
        else: return None

    def hasHexagoneGauche(self,x,y):
        return self.hexacoord.has_key((x-self.taille,y))
    def getHexagoneGauche(self,x,y):
        if self.hexacoord.has_key((x-self.taille,y)):
            return self.hexacoord[(x-self.taille,y)]
        else: return None

    def hasHexagoneDroite(self,x,y):
        return self.hexacoord.has_key((x+self.taille,y))
    def getHexagoneDroite(self,x,y):
        if self.hexacoord.has_key((x+self.taille,y)):
            return self.hexacoord[(x+self.taille,y)]
        else: return None
    def hasHexagoneBasGauche(self,x,y):
        return self.hexacoord.has_key((x-self.taille/2,y-(3**(0.5))*self.taille/2))
    def getHexagoneBasGauche(self,x,y):
        if self.hexacoord.has_key((x-self.taille/2,y-(3**(0.5))*self.taille/2)):
            return self.hexacoord[(x-self.taille/2,y-(3**(0.5))*self.taille/2)]
        else: return None

    def hasHexagoneBasDroite(self,x,y):
        return self.hexacoord.has_key((x+self.taille/2,y-(3**(0.5))*self.taille/2))
    def getHexagoneBasDroite(self,x,y):
        if self.hexacoord.has_key((x+self.taille/2,y-(3**(0.5))*self.taille/2)):
            return self.hexacoord[(x+self.taille/2,y-(3**(0.5))*self.taille/2)]
        else: return None

    def hasVoisin(self,x,y):
        return self.hasHexagoneHautGauche(x,y) or self.hasHexagoneHautDroite(x,y) or self.hasHexagoneGauche(x,y) or self.hasHexagoneDroite(x,y) or self.hasHexagoneBasGauche(x,y) or self.hasHexagoneBasDroite(x,y)

class Hexagone:
    def __str__(self):#affichage utilise uniquement pour le deboguage
        chaine="x: "+str(self.x)+" y: "+str(self.y)+" "+self.matiere+" "+str(self.numde)+" "
        chaine+="sommets: "+str(self.sommet1.num)+","+str(self.sommet2.num)+","+str(self.sommet3.num)+","
        chaine+=str(self.sommet4.num)+","+str(self.sommet5.num)+","+str(self.sommet6.num)
        return chaine
    def __init__ (self, _ile, _x, _y, _matiere, _numde):
        self.ile=_ile
        self.matiere=_matiere#matiere premiere
        self.numde=_numde#numero de
        self.x=_x#coordonnees
        self.y=_y
        self.sommet1=Sommet (self.ile.nbhexaposes*6+1,self.x,self.y+26)
        self.ile.sommets[self.ile.nbhexaposes*6+1]=self.sommet1
        self.sommet2=Sommet (self.ile.nbhexaposes*6+2,self.x+21,self.y+10.86)
        self.ile.sommets[self.ile.nbhexaposes*6+2]=self.sommet2
        self.sommet3=Sommet (self.ile.nbhexaposes*6+3,self.x+21,self.y-10.86)
        self.ile.sommets[self.ile.nbhexaposes*6+3]=self.sommet3
        self.sommet4=Sommet (self.ile.nbhexaposes*6+4,self.x,self.y-26)
        self.ile.sommets[self.ile.nbhexaposes*6+4]=self.sommet4
        self.sommet5=Sommet (self.ile.nbhexaposes*6+5,self.x-21,self.y-10.86)
        self.ile.sommets[self.ile.nbhexaposes*6+5]=self.sommet5
        self.sommet6=Sommet (self.ile.nbhexaposes*6+6,self.x-21,self.y+10.86)
        self.ile.sommets[self.ile.nbhexaposes*6+6]=self.sommet6

        if self.ile.hasHexagoneHautGauche(self.x,self.y):#on renumerote les sommets qui sont "partages" avec un hexagone deja existant et adjacents en leur donnant les "anciens" numero ; il y a des numero de sommet qui "sautent" car supprimes comme etant redondants
            self.sommet1=self.ile.getHexagoneHautGauche(self.x,self.y).sommet3
            if len(self.ile.getHexagoneHautGauche(self.x,self.y).sommet3.listsuccess) < 3:
                self.ile.getHexagoneHautGauche(self.x,self.y).sommet3.listsuccess.append(self.sommet2)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+1):
                del self.ile.sommets[self.ile.nbhexaposes*6+1]

            self.sommet6=self.ile.getHexagoneHautGauche(self.x,self.y).sommet4
            if len(self.ile.getHexagoneHautGauche(self.x,self.y).sommet4.listsuccess) < 3:
                self.ile.getHexagoneHautGauche(self.x,self.y).sommet4.listsuccess.append(self.sommet5)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+6):
                del self.ile.sommets[self.ile.nbhexaposes*6+6]

        if self.ile.hasHexagoneHautDroite(self.x,self.y):

            self.sommet1=self.ile.getHexagoneHautDroite(self.x,self.y).sommet5
            if len(self.ile.getHexagoneHautDroite(self.x,self.y).sommet5.listsuccess) < 3:
                self.ile.getHexagoneHautDroite(self.x,self.y).sommet5.listsuccess.append(self.sommet6)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+1):
                del self.ile.sommets[self.ile.nbhexaposes*6+1]

            self.sommet2=self.ile.getHexagoneHautDroite(self.x,self.y).sommet4
            if len(self.ile.getHexagoneHautDroite(self.x,self.y).sommet4.listsuccess) < 3:
                self.ile.getHexagoneHautDroite(self.x,self.y).sommet4.listsuccess.append(self.sommet3)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+2):
                del self.ile.sommets[self.ile.nbhexaposes*6+2]
        if self.ile.hasHexagoneGauche(self.x,self.y):
            self.sommet6=self.ile.getHexagoneGauche(self.x,self.y).sommet2
            if len(self.ile.getHexagoneGauche(self.x,self.y).sommet2.listsuccess) < 3:
                self.ile.getHexagoneGauche(self.x,self.y).sommet2.listsuccess.append(self.sommet1)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+6):
                del self.ile.sommets[self.ile.nbhexaposes*6+6]

            self.sommet5=self.ile.getHexagoneGauche(self.x,self.y).sommet3
            if len(self.ile.getHexagoneGauche(self.x,self.y).sommet3.listsuccess) < 3:
                self.ile.getHexagoneGauche(self.x,self.y).sommet3.listsuccess.append(self.sommet4)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+5):
                del self.ile.sommets[self.ile.nbhexaposes*6+5]

        if self.ile.hasHexagoneDroite(self.x,self.y):

            self.sommet2=self.ile.getHexagoneDroite(self.x,self.y).sommet6
            if len(self.ile.getHexagoneDroite(self.x,self.y).sommet6.listsuccess) < 3:
                self.ile.getHexagoneDroite(self.x,self.y).sommet6.listsuccess.append(self.sommet1)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+2):
                del self.ile.sommets[self.ile.nbhexaposes*6+2]

            self.sommet3=self.ile.getHexagoneDroite(self.x,self.y).sommet5
            if len(self.ile.getHexagoneDroite(self.x,self.y).sommet5.listsuccess) < 3:
                self.ile.getHexagoneDroite(self.x,self.y).sommet5.listsuccess.append(self.sommet4)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+3):
                del self.ile.sommets[self.ile.nbhexaposes*6+3]

        if self.ile.hasHexagoneBasGauche(self.x,self.y):

            self.sommet4=self.ile.getHexagoneBasGauche(self.x,self.y).sommet2
            if len(self.ile.getHexagoneBasGauche(self.x,self.y).sommet2.listsuccess) < 3:
                self.ile.getHexagoneBasGauche(self.x,self.y).sommet2.listsuccess.append(self.sommet3)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+4):
                del self.ile.sommets[self.ile.nbhexaposes*6+4]

            self.sommet5=self.ile.getHexagoneBasGauche(self.x,self.y).sommet1
            if len(self.ile.getHexagoneBasGauche(self.x,self.y).sommet1.listsuccess) < 3:
                self.ile.getHexagoneBasGauche(self.x,self.y).sommet1.listsuccess.append(self.sommet6)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+5):
                del self.ile.sommets[self.ile.nbhexaposes*6+5]

        if self.ile.hasHexagoneBasDroite(self.x,self.y):

            self.sommet3=self.ile.getHexagoneBasDroite(self.x,self.y).sommet1
            if len(self.ile.getHexagoneBasDroite(self.x,self.y).sommet1.listsuccess) <3:
                self.ile.getHexagoneBasDroite(self.x,self.y).sommet1.listsuccess.append(self.sommet2)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+3):
                del self.ile.sommets[self.ile.nbhexaposes*6+3]

            self.sommet4=self.ile.getHexagoneBasDroite(self.x,self.y).sommet6
            if len(self.ile.getHexagoneBasDroite(self.x,self.y).sommet6.listsuccess) < 3:
                self.ile.getHexagoneBasDroite(self.x,self.y).sommet6.listsuccess.append(self.sommet5)
            if self.ile.sommets.has_key(self.ile.nbhexaposes*6+4):
                del self.ile.sommets[self.ile.nbhexaposes*6+4]

        if len(self.sommet1.listsuccess)<3: #on ne cree la liste des "voisins" (ou successeurs) de chaque sommet que lorsque tous les sommets ont bien etes nommes
            self.sommet1.listsuccess.append(self.sommet2)
            self.sommet1.listsuccess.append(self.sommet6)
        if len(self.sommet2.listsuccess)<3:
            self.sommet2.listsuccess.append(self.sommet1)
            self.sommet2.listsuccess.append(self.sommet3)
        if len(self.sommet3.listsuccess)<3:
            self.sommet3.listsuccess.append(self.sommet2)
            self.sommet3.listsuccess.append(self.sommet4)
        if len(self.sommet4.listsuccess)<3:
            self.sommet4.listsuccess.append(self.sommet3)
            self.sommet4.listsuccess.append(self.sommet5)
        if len(self.sommet5.listsuccess)<3:
            self.sommet5.listsuccess.append(self.sommet4)
            self.sommet5.listsuccess.append(self.sommet6)
        if len(self.sommet6.listsuccess)<3:
            self.sommet6.listsuccess.append(self.sommet5)
            self.sommet6.listsuccess.append(self.sommet1)

        for i in self.ile.sommets.keys():
            self.ile.sommetscoord[self.ile.sommets[i].x,self.ile.sommets[i].y]=self.ile.sommets[i]
class Sommet:
    def __init__ (self, _num, _x, _y):
        self.num=_num
        self.x=_x
        self.y=_y
        self.constr=(0,0) #colonie, joueur
        self.listsuccess=[]#les voisins
class Route:
    def __init__ (self, _coord, _color):
        self.coord = _coord
        self.coord2 = (self.coord[1], self.coord[0])
        self.color = _color
