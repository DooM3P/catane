# from Tkinter import *
from monjeu2 import *
import math
jeu=Jeu (Ile())

class board:
    def __init__(self):
        self.num = IntVar () #dernier sommet selectionne
        self.num.set (1)
        self.numans = IntVar () #avant-dernier sommet selectionne
        self.numans.set (1)
        self.f1 = Frame (height=410 , width=410)
        self.f1.grid (column = 0, row = 0)
        self.cf1 = Canvas(self.f1, width=410, height=410, bg='blue')
        self.cf1.grid()
        for coord in jeu.ile.hexacoord.keys(): #trace des hexagones
            self.drawHexagon(self.cf1, coord[0]*1.75+200,coord[1]*1.75+200, jeu.ile.hexacoord[coord].matiere)
        self.drawNumbers (2, "deux.gif", "image2") #trace des numeros
        self.drawNumbers (3, "trois.gif", "image2")
        self.drawNumbers (4, "quatre.gif", "image2")
        self.drawNumbers (5, "cinq.gif", "image2")
        self.drawNumbers (6, "six.gif", "image2")
        self.drawNumbers (8, "huit.gif", "image2")
        self.drawNumbers (9, "neuf.gif", "image2")
        self.drawNumbers (10, "dix.gif", "image2")
        self.drawNumbers (11, "onze.gif", "image2")
        self.drawNumbers (12, "douze.gif", "image2")
        self.drawNumbers (0, "malandrin.gif", "voyou")
        self.cf1.bind('<Button-1>',self.mouse)
    def drawNumbers (self, _numde, _picture, _tags):
        for i in jeu.ile.hexacoord.keys():
            if jeu.ile.hexacoord[i].numde == _numde:
                photo = PhotoImage(file=_picture)
                label = Label(image=photo)
                label.image = photo
                item = self.cf1.create_image((i[0]*1.75)+200,(i[1]*1.75)+200, image=label.image, tags = _tags)
                self.cf1.lift(_tags)
    def drawHexagon (self, canvbox, cx, cy, color):
        l=74
        L=36
        h=90
        x1=cx-(l/2)
        x2=cx
        x3=cx+(l/2)
        y1=cy-(h/2)
        y2=cy-(L/2)
        y3=cy+(L/2)
        y4=cy+(h/2)
        canvbox.create_polygon(x1, y3, x2, y4, x3, y3 ,x3, y2, x2, y1, x1, y2 ,fill = color,outline='black', width = 1.2)
    def mouse (self, event): #fonction qui selectionne le sommet
        x, y = self.cf1.canvasx(event.x), self.cf1.canvasy(event.y)
        x = (x-200)/1.75
        y = (y-200)/1.75
        for i,j in jeu.ile.sommetscoord.keys():
            if ((x-i)**2 < 60) & ((y-j)**2 < 60):
                self.numans.set(self.num.get()) # on garde l'avant-dernier (pour les routes)
                self.num.set (jeu.ile.sommetscoord[i, j].num)
class rogue:
    def __init__ (self, _gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2= Frame ()
        self.f2.grid (column = 1 , row = 1)
        self.label3  =  Label(self.f2, bg="White", text ="Choisissez le nouvel emplacement du brigand puis cliquez", width = 45)
        self.label3.grid()
        self.gestionnaireFenetres.fenetreCourante.cf1.bind('<Button-1>',self.mouse2)
        self.f2.bouton4 =Button (self.f2, text = "OK")
        self.f2.bouton4.grid ()
    def mouse2 (self, event):
        x, y = self.gestionnaireFenetres.fenetreCourante.cf1.canvasx(event.x), self.gestionnaireFenetres.fenetreCourante.cf1.canvasy(event.y)
        x = (x-200)/1.75
        y = (y-200)/1.75
        for i,j in jeu.ile.hexacoord.keys():
            if ((x-i)**2 < 50) & ((y-j)**2 < 50):
                jeu.ile.hexacoord[(jeu.numbackup[1],jeu.numbackup[2])].numde=jeu.numbackup[0]
                jeu.numbackup=(jeu.ile.hexacoord[(i,j)].numde,i,j)
                jeu.ile.hexacoord[(i,j)].numde=7
                self.gestionnaireFenetres.fenetreCourante.cf1.delete("voyou")
                self.gestionnaireFenetres.fenetreCourante.cf1.delete("voyou2")
                self.gestionnaireFenetres.fenetreCourante.drawNumbers (7, "malandrin.gif", "voyou2")
                self.gestionnaireFenetres.fenetreCourante.cf1.lift("voyou2")
        self.f2.destroy()
        self.gestionnaireFenetres.fenetreCourante.cf1.bind('<Button-1>',self.gestionnaireFenetres.fenetreCourante.mouse)
        self.gestionnaireFenetres.loadFenetreSuivante("game2")
        #self.gestionnaireFenetres.loadFenetreSuivante.

class score: #ce panneau affiche principalement des infos sur les couts de constructions et les sommets selectionnes
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f3 = Frame ()
        self.f3.grid (column = 1, row = 0,sticky=N)
        self.label1  =  Label(self.f3, text = "Sommet Selectionne :", bg="White", width = 19,anchor=W)
        self.label1.grid(column = 0, row =0)
        self.label2  =  Label(self.f3, bg="White", textvariable  =  self.gestionnaireFenetres.fenetreCourante.num, width = 25,anchor=W)
        self.label2.grid(column = 1, row =0)
        self.labelblnk  =  Label(self.f3, text ="", width = 45)
        self.labelblnk.grid(column = 0, row =1, columnspan = 2)
        self.label3  =  Label(self.f3, bg="White", text ="Frais de Construction", width = 45)
        self.label3.grid(column = 0, row =2, columnspan = 2)
        self.label4  =  Label(self.f3, bg="White", text  =  "Route : ", width = 19,anchor=W)
        self.label4.grid(column = 0, row =3)
        self.label5  =  Label(self.f3, bg="White", text  =  "Colonie : ", width = 19,anchor=W)
        self.label5.grid(column = 0, row =4)
        self.label6  =  Label(self.f3, bg="White", text  =  "Ville : ", width = 19,anchor=W)
        self.label6.grid(column = 0, row =5)
        self.label7  =  Label(self.f3, bg="White", text  =  "Developpement : ", width = 19,anchor=W)
        self.label7.grid(column = 0, row =6)
        self.label8  =  Label(self.f3, bg="White", text  =  "1 Bois ; 1 Argile", width = 25,anchor=W)
        self.label8.grid(column = 1, row =3)
        self.label9  =  Label(self.f3, bg="White", text  =  "1 Bois ; 1 Argile ; 1 Ble ; 1 Laine", width = 25,anchor=W)
        self.label9.grid(column = 1, row =4)
        self.label10  =  Label(self.f3, bg="White", text  =  "2 Ble ; 3 Minerai", width = 25,anchor=W)
        self.label10.grid(column = 1, row =5)
        self.label11  =  Label(self.f3, bg="White", text  =  "1 Ble ; 1 Laine ; 1 Minerai", width = 25,anchor=W)
        self.label11.grid(column = 1, row =6)
class config:
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2 = Frame ()
        self.f2.grid (column = 1, row = 1)
        self.f2.label1 = Label (self.f2, text="Nombre total de joueurs")
        self.f2.label1.grid ()
        self.v = IntVar ()
        self.v.set (0)
        self.f2.bouton1 = Radiobutton(self.f2, text="2", variable=self.v, value=2)
        self.f2.bouton1.grid ()
        self.f2.bouton2 = Radiobutton(self.f2, text="3", variable=self.v, value=3)
        self.f2.bouton2.grid ()
        self.f2.bouton3 = Radiobutton(self.f2, text="4", variable=self.v, value=4)
        self.f2.bouton3.grid ()
        self.f2.bouton4 =Button (self.f2, text = "OK", command = self.ok)
        self.f2.bouton4.grid ()
    def ok (self):
        if self.v.get() > 0:
            self.f2.destroy()
            jeu.njoueurs = self.v.get()
            self.gestionnaireFenetres.loadFenetreSuivante("config2")

class config2:
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2 = Frame ()
        self.f2.grid (column = 1, row = 1)
        self.f2.label1 = Label (self.f2, text="Nombre de joueurs ordinateurs")
        self.f2.label1.grid ()
        self.v = IntVar ()
        self.v.set (0)
        #for i in range (0, jeu.njoueurs):
        self.f2.bouton1 = Radiobutton(self.f2, text=0, variable=self.v, value=0) #ordinateurs desactives
        self.f2.bouton1.grid ()
        self.f2.bouton4 =Button (self.f2, text = "OK")
        self.f2.bouton4.grid ()
        self.f2.bouton4.config (command = self.ok)
    def ok (self):
        self.f2.destroy()
        jeu.ncpu = self.v.get()
        self.gestionnaireFenetres.loadFenetreSuivante("color")

class color:
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2 = Frame ()
        self.f2.grid (column = 1, row = 1)
        self.f2.label1 = Label (self.f2, text=("Joueur",jeu.plyrcount+1))
        self.f2.label1.grid ()
        self.f2.label2 = Label (self.f2, text="Choisissez votre couleur")
        self.f2.label2.grid ()
        self.v = StringVar ()
        self.v.set ("")
        for i in jeu.colors:
            self.f2.bouton1 = Radiobutton(self.f2, text=i, variable=self.v, value=i)
            self.f2.bouton1.grid ()
        self.f2.bouton4 =Button (self.f2, text = "OK")
        self.f2.bouton4.grid ()
        self.f2.bouton4.config (command = self.ok)
    def ok (self):
        if not self.v.get() == "":
            self.f2.destroy()
            Plyr1 = Joueur (jeu.find(jeu.listjoueurs), 0, self.v.get())
            jeu.listjoueurs[Plyr1.color]=Plyr1
            jeu.plyrcount = jeu.plyrcount + 1
            jeu.colors.remove(self.v.get()) #on retire la couleur prise de la liste avant de relancer la boucle
            if jeu.plyrcount < jeu.njoueurs - jeu.ncpu:
                self.gestionnaireFenetres.loadFenetreSuivante("color")
            else:
                for i in range (0,jeu.ncpu): #une fois tous les joueurs humains crees, on cree les ordinateurs, si necessaire
                    Plyr1 = Joueur (jeu.find(jeu.listjoueurs), 1, jeu.colors[0])#la fonction find "trouve" le numero de de du joueur en relancant si necessaire
                    jeu.plyrcount = jeu.plyrcount + 1
                    del jeu.colors[0]
                    jeu.listjoueurs[Plyr1.color]=Plyr1
                for i in jeu.listjoueurs.keys():
                    jeu.order.append(jeu.listjoueurs[i].numplyr) #on cree une liste des des jetes
                jeu.order.sort(reverse=True) #on classe les des dans l'ordre
                jeu.plyrcount = 0
                self.gestionnaireFenetres.fenetreCourante4=score2(self)
                self.gestionnaireFenetres.loadFenetreSuivante("build")
class score2: #ici ressources mises a jour en temps reel, points de temps en temps
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f3 = Frame ()
        self.f3.grid (column = 0, row = 1,sticky=W)
        self.f3.bouton1 = Label(self.f3, bg="White", text = "Joueur", width = 5,anchor=N)
        self.f3.bouton1.grid (column = 0, row =0)
        self.f3.bouton1 = Label(self.f3, bg="White", text = "Points", width = 5,anchor=N)
        self.f3.bouton1.grid (column = 1, row =0)
        self.f3.bouton1 = Label(self.f3, bg="White", text = "Bois", width = 5,anchor=N)
        self.f3.bouton1.grid (column = 2, row =0)
        self.f3.bouton1 = Label(self.f3, bg="White", text = "Argile", width = 5,anchor=N)
        self.f3.bouton1.grid (column = 3, row =0)
        self.f3.bouton1 = Label(self.f3, bg="White", text = "Ble", width = 5,anchor=N)
        self.f3.bouton1.grid (column = 4, row =0)
        self.f3.bouton1 = Label(self.f3, bg="White", text = "Laine", width = 5,anchor=N)
        self.f3.bouton1.grid (column = 5, row =0)
        self.f3.bouton1 = Label(self.f3, bg="White", text = "Minerai", width = 7,anchor=N)
        self.f3.bouton1.grid (column = 6, row =0)
        self.f3.bouton1 = Label(self.f3, bg="White", text = "No. Ordre", width = 9,anchor=N)
        self.f3.bouton1.grid (column = 7, row =0)
        for i in range (0, len(jeu.listjoueurs)):
            self.f3.bouton1 = Label(self.f3, bg="White", text = jeu.findplyr(jeu.listjoueurs, jeu.order[i]), width = 5,anchor=N)
            self.f3.bouton1.grid (column = 0, row =i+1)
            self.f3.bouton1 = Label(self.f3, bg="White", textvariable  =  jeu.listjoueurs[jeu.findplyr(jeu.listjoueurs, jeu.order[i])].pts, width = 5,anchor=N)
            self.f3.bouton1.grid (column = 1, row =i+1)
            self.f3.bouton1 = Label(self.f3, bg="White", textvariable  =  jeu.listjoueurs[jeu.findplyr(jeu.listjoueurs, jeu.order[i])].bois, width = 5,anchor=N)
            self.f3.bouton1.grid (column = 2, row =i+1)
            self.f3.bouton1 = Label(self.f3, bg="White", textvariable  =  jeu.listjoueurs[jeu.findplyr(jeu.listjoueurs, jeu.order[i])].argile, width = 5,anchor=N)
            self.f3.bouton1.grid (column = 3, row =i+1)
            self.f3.bouton1 = Label(self.f3, bg="White", textvariable  =  jeu.listjoueurs[jeu.findplyr(jeu.listjoueurs, jeu.order[i])].ble, width = 5,anchor=N)
            self.f3.bouton1.grid (column = 4, row =i+1)
            self.f3.bouton1 = Label(self.f3, bg="White", textvariable  =  jeu.listjoueurs[jeu.findplyr(jeu.listjoueurs, jeu.order[i])].laine, width = 5,anchor=N)
            self.f3.bouton1.grid (column = 5, row =i+1)
            self.f3.bouton1 = Label(self.f3, bg="White", textvariable  =  jeu.listjoueurs[jeu.findplyr(jeu.listjoueurs, jeu.order[i])].minerai, width = 7,anchor=N)
            self.f3.bouton1.grid (column = 6, row =i+1)
            self.f3.bouton1 = Label(self.f3, bg="White", text = jeu.listjoueurs[jeu.findplyr(jeu.listjoueurs, jeu.order[i])].numplyr, width = 9,anchor=N)
            self.f3.bouton1.grid (column = 7, row =i+1)
class build: # on pose les deux premieres colonies gratuites
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2 = Frame ()
        self.f2.grid (column = 1, row = 1)
        if jeu.plyrcount >= jeu.njoueurs and jeu.plyrcount2 == 0:
            jeu.plyrcount = 0
            jeu.plyrcount2 += 1
            jeu.order.reverse()#comme les regles l'exigent, le dernier joueur a avoir pose est le premier a poser la seconde serie de colonies
            for j in range (2, 7):
                jeu.ile.income(j, jeu.listjoueurs)
            for j in range (8, 13):
                jeu.ile.income(j, jeu.listjoueurs)
        if jeu.plyrcount < jeu.njoueurs:
            jeu.currentcolor = jeu.findplyr(jeu.listjoueurs, jeu.order[jeu.plyrcount]) #la fonction jeu.findplyr permet un ordre conforme aux des
            self.f2.label1 = Label (self.f2, text=("Joueur "+str(jeu.currentcolor)+", a vous de poser votre colonie"))
            self.f2.label1.grid()
            self.f2.label2 = Label (self.f2, text=("Choisissez le sommet, puis appuyez sur OK"))
            self.f2.label2.grid()
            self.f2.bouton1 = Button (self.f2, text="OK", command = (lambda : self.ok("blank")))
            self.f2.bouton1.grid ()
            self.f2.bind_all ('<Return>', self.ok)
        else:
            self.f2.destroy()
            jeu.order.reverse() #on remet dans l'ordre les des avant d'entrer dans la phase de jeu standard
            jeu.plyrcount = 0
            self.gestionnaireFenetres.loadFenetreSuivante("game1")
    def ok (self, event):
        if jeu.currentcolor == 'Bleu':
            photo = PhotoImage(file='maisonbleu.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Rouge':
            photo = PhotoImage(file='maisonrouge.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Jaune':
            photo = PhotoImage(file='maisonjaune.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Orange':
            photo = PhotoImage(file='maisonorange.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Vert':
            photo = PhotoImage(file='maisonvert.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].constr == (0, 0) and jeu.ile.somtest(self.gestionnaireFenetres.fenetreCourante.num.get(), jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].listsuccess) == 0: #si la case n'est pas construite et le sommet a plus de deux aretes de distance, on peut poser
            jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].constr=1, jeu.currentcolor
            jeu.listjoueurs[jeu.currentcolor].villages[self.gestionnaireFenetres.fenetreCourante.num.get()]=jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()]
            item = self.gestionnaireFenetres.fenetreCourante.cf1.create_image((jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].x*1.75)+200,(jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].y*1.75)+200, image=label.image, tags = "image")
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("road")
        else:
            print("Sommet incorrect !")
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("build")

class road: #ici, pour poser la route, on ne demande que l'arrivee au joueur, le depart etant forcement la colonie tout juste posee
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2 = Frame ()
        self.f2.grid (column = 1, row = 1)
        jeu.route1 = Route ([self.gestionnaireFenetres.fenetreCourante.num.get(),0], jeu.currentcolor)
        self.f2.label1 = Label (self.f2, text=("Joueur "+str(jeu.currentcolor)+", posez maintenant l'arrivee de votre route"))
        self.f2.label1.grid()
        self.f2.bouton2 = Button (self.f2, text="OK",command = (lambda : self.ok2("blank")))
        self.f2.bouton2.grid ()
        self.f2.bind_all ('<Return>', self.ok2)

    def ok2 (self, event):
        if self.gestionnaireFenetres.fenetreCourante.num.get() != jeu.route1.coord[0]: #arrivee differente du depart
            for i in jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].listsuccess:
                if i.num == jeu.route1.coord[0]:#il faut que les sommets soient voisins !
                    jeu.route1.coord[1]=self.gestionnaireFenetres.fenetreCourante.num.get()
                    jeu.ile.routes[(jeu.route1.coord[0],jeu.route1.coord[1])]=jeu.route1
                    self.gestionnaireFenetres.fenetreCourante.cf1.create_line(jeu.ile.sommets[jeu.route1.coord[0]].x*1.75+200, jeu.ile.sommets[jeu.route1.coord[0]].y*1.75+200, jeu.ile.sommets[jeu.route1.coord[1]].x*1.75+200, jeu.ile.sommets[jeu.route1.coord[1]].y*1.75+200, width = 4, fill = jeu.transcolor(jeu.currentcolor))
                    self.gestionnaireFenetres.fenetreCourante.cf1.lift("image")
                    jeu.plyrcount = jeu.plyrcount + 1
                    self.f2.destroy()
                    self.gestionnaireFenetres.loadFenetreSuivante("build")
                    return "break"
        print("Sommet incorrect !")

class game1: #Juste le lancer de de au debut de chaque tour
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2 = Frame ()
        self.f2.grid (column = 1, row = 1)
        if jeu.plyrcount < jeu.njoueurs:
            jeu.currentcolor = jeu.findplyr(jeu.listjoueurs, jeu.order[jeu.plyrcount])#La couleur du joueur qui joue, determinee par l'ordre des des
            self.f2.label1 = Label (self.f2, text=("Joueur "+str(jeu.currentcolor)+", c'est votre tour de jouer."))
            self.f2.label1.grid()
            self.f2.bouton1 = Button (self.f2, text="Lancez les des !", command = (lambda : self.ok("blank")))
            self.f2.bouton1.grid ()
            self.f2.bind_all ('<Return>', self.ok)
        else:
            self.f2.destroy()
            jeu.plyrcount=0
            self.gestionnaireFenetres.loadFenetreSuivante("game1")
    def ok (self,event):
        jeu.de=jeu.des()
        jeu.ile.income(jeu.de, jeu.listjoueurs) #chaque joueur recoit ses matieres premieres
        self.f2.destroy()
        if jeu.de == 7:
            self.gestionnaireFenetres.loadFenetreSuivante("rogue")
        else :self.gestionnaireFenetres.loadFenetreSuivante("game2")
class game2:# les differents boutons d'action du joueurs (poser une route, une colonie, ville faire du commerce, acheter une carte)
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2 = Frame ()
        self.f2.grid (column = 1, row = 1)
        self.f2.label1 = Label (self.f2, text=str(jeu.currentcolor)+"\n"+str(jeu.de)+" ! Alea jacta est !")
        self.f2.label1.grid (column = 0, row = 0, columnspan =2)
        self.f2.bouton1 = Button (self.f2, text="Route",command = self.route, width=17)
        self.f2.bouton1.grid (column = 0, row = 1)
        self.f2.bouton2 = Button (self.f2, text="Colonie",command = self.colonie , width=17)
        self.f2.bouton2.grid (column = 0, row = 2)
        self.f2.bouton3 = Button (self.f2, text="Ville",command = self.ville , width=17)
        self.f2.bouton3.grid (column = 1, row = 1)
        self.f2.bouton4 = Button (self.f2, text="Carte Developpement",command = self.carte , width=17)
        self.f2.bouton4.grid (column = 1, row = 2)
        self.f2.bouton5 = Button (self.f2, text="Commerce",command = self.trade , width=36)
        self.f2.bouton5.grid (column = 0, row = 3, columnspan=2)
        self.f2.label2 = Label (self.f2, text="")
        self.f2.label2.grid (column = 0, row = 4, columnspan=2)
        self.f2.bouton6 = Button (self.f2, text="Fin de Tour",command = (lambda : self.findetour("blank")) , width=17)
        self.f2.bouton6.grid (column = 0, row = 5, columnspan=2)
        self.f2.bind_all ('<Return>', self.findetour)
    def route (self):
        if jeu.listjoueurs[jeu.currentcolor].bois.get() > 0 and jeu.listjoueurs[jeu.currentcolor].argile.get() > 0:
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("road2")
        else:
            print("Pas assez de matieres premieres")
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("game2")
    def trade(self):
        self.gestionnaireFenetres.loadFenetreSuivante("trade")
    def colonie (self):
        if jeu.listjoueurs[jeu.currentcolor].bois.get() > 0 and jeu.listjoueurs[jeu.currentcolor].argile.get() > 0 and jeu.listjoueurs[jeu.currentcolor].ble.get() > 0 and jeu.listjoueurs[jeu.currentcolor].laine.get() > 0:
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("colonie")
        else:
            print("Pas assez de matieres premieres")
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("game2")
    def ville (self):
        if jeu.listjoueurs[jeu.currentcolor].ble.get() > 1 and jeu.listjoueurs[jeu.currentcolor].laine.get() > 2:
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("ville")
        else:
            print("Pas assez de matieres premieres")
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("game2")
    def carte (self):
        if jeu.listjoueurs[jeu.currentcolor].ble.get() > 0 and jeu.listjoueurs[jeu.currentcolor].laine.get() > 0 and jeu.listjoueurs[jeu.currentcolor].minerai.get() > 0:
            if len(jeu.cards)>0:
                print("Vous avez pioche "+str(jeu.cards[0]))
                if jeu.cards[0]=="Victoire":
                    jeu.listjoueurs[jeu.currentcolor].cards[0] += 1
                if jeu.cards[0]=="Chevalier":
                    jeu.listjoueurs[jeu.currentcolor].cards[1] += 1
                if jeu.cards[0]=="Monopole":
                    jeu.listjoueurs[jeu.currentcolor].cards[2] += 1
                if jeu.cards[0]=="Decouverte":
                    jeu.listjoueurs[jeu.currentcolor].cards[3] += 1
                if jeu.cards[0]=="Route":
                    jeu.listjoueurs[jeu.currentcolor].cards[4] += 1
                jeu.listjoueurs[jeu.currentcolor].cards.append(jeu.cards[0])
                del jeu.cards[0]
                jeu.listjoueurs[jeu.currentcolor].ble.set(jeu.listjoueurs[jeu.currentcolor].ble.get()-1)
                jeu.listjoueurs[jeu.currentcolor].minerai.set(jeu.listjoueurs[jeu.currentcolor].minerai.get()-1)
                jeu.listjoueurs[jeu.currentcolor].laine.set(jeu.listjoueurs[jeu.currentcolor].laine.get()-1)
            else:
                print("Plus de cartes !")
        else:
            print("Pas assez de matieres premieres")
    def findetour (self, event):
        jeu.compteur(jeu, self.gestionnaireFenetres)
        jeu.plyrcount=jeu.plyrcount+1
        self.f2.destroy()
        self.gestionnaireFenetres.loadFenetreSuivante("game1")
class road2:#plus compliquee que road1 car deux extremites a definir et il faut veiller a respecter plus de contraintes
    def __init__ (self,_gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2 = Frame ()
        self.f2.grid (column = 1, row = 1)
        self.f2.label1 = Label (self.f2, text=("Joueur "+str(jeu.currentcolor)+", cliquez sur le depart \n puis l'arrivee de votre route, et appuyez sur OK"))
        self.f2.label1.grid()
        self.f2.bouton2 = Button (self.f2, text="OK",command = (lambda : self.ok2("blank")))
        self.f2.bouton2.grid ()
        self.f2.bind_all ('<Return>', self.ok2)
        self.f2.bouton3 = Button (self.f2, text="Annuler",command = self.ok3)
        self.f2.bouton3.grid ()
    def ok2 (self, event):
        if self.gestionnaireFenetres.fenetreCourante.num.get() != self.gestionnaireFenetres.fenetreCourante.numans.get() and jeu.routeverif(self.gestionnaireFenetres.fenetreCourante.num.get(), self.gestionnaireFenetres.fenetreCourante.numans.get(), jeu) == 1:#condition : depart et arrivee differentes ; sommets voisins
            if not jeu.ile.routes.has_key((self.gestionnaireFenetres.fenetreCourante.num.get(),self.gestionnaireFenetres.fenetreCourante.numans.get())) and not jeu.ile.routes.has_key((self.gestionnaireFenetres.fenetreCourante.numans.get(),self.gestionnaireFenetres.fenetreCourante.num.get())):#condition : la route ne doit pas deja exister ! (coordonnees testees dans les deux sens)
                if jeu.ile.routetest (self.gestionnaireFenetres.fenetreCourante.num.get(), self.gestionnaireFenetres.fenetreCourante.numans.get(), jeu.currentcolor, jeu)==1:#on verifie la presence d'une colonie ou route voisine de meme couleur
                    jeu.route1=Route ([self.gestionnaireFenetres.fenetreCourante.num.get(),self.gestionnaireFenetres.fenetreCourante.numans.get()], jeu.currentcolor)
                    self.gestionnaireFenetres.fenetreCourante.cf1.create_line(jeu.ile.sommets[jeu.route1.coord[0]].x*1.75+200, jeu.ile.sommets[jeu.route1.coord[0]].y*1.75+200, jeu.ile.sommets[jeu.route1.coord[1]].x*1.75+200, jeu.ile.sommets[jeu.route1.coord[1]].y*1.75+200, width = 4, fill = jeu.transcolor(jeu.currentcolor))
                    jeu.ile.routes[(jeu.route1.coord[0],jeu.route1.coord[1])]=jeu.route1 #on met la route dans la liste des routes
                    self.gestionnaireFenetres.fenetreCourante.cf1.lift("image")
                    jeu.listjoueurs[jeu.currentcolor].bois.set(jeu.listjoueurs[jeu.currentcolor].bois.get()-1)# on fait "payer" les ressources
                    jeu.listjoueurs[jeu.currentcolor].argile.set(jeu.listjoueurs[jeu.currentcolor].argile.get()-1)
                    self.f2.destroy()
                    self.gestionnaireFenetres.loadFenetreSuivante("game2")
                else : print("Il n'y a pas de route "+str(jeu.currentcolor)+" a cote")
            else : print("Il y a deja une route ici")
        else : print("Route mal mise")
    def ok3 (self):
        self.f2.destroy()
        self.gestionnaireFenetres.loadFenetreSuivante("game2")
class colonie:
    def __init__ (self, _gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2= Frame ()
        self.f2.grid (column = 1, row = 1)
        self.f2.label1 = Label (self.f2, text=("Joueur "+str(jeu.currentcolor)+", cliquez sur le sommet \n puis appuyez sur OK (ou Enter)"))
        self.f2.label1.grid()
        self.f2.bouton2 = Button (self.f2, text="OK",command = (lambda : self.ok2("blank")))
        self.f2.bouton2.grid ()
        self.f2.bind_all ('<Return>', self.ok2)
        self.f2.bouton3 = Button (self.f2, text="Annuler",command = self.ok3)
        self.f2.bouton3.grid ()
    def ok2 (self, event):
        if jeu.currentcolor == 'Bleu':
            photo = PhotoImage(file='maisonbleu.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Rouge':
            photo = PhotoImage(file='maisonrouge.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Jaune':
            photo = PhotoImage(file='maisonjaune.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Orange':
            photo = PhotoImage(file='maisonorange.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Vert':
            photo = PhotoImage(file='maisonvert.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].constr == (0, 0) and jeu.ile.somtest(self.gestionnaireFenetres.fenetreCourante.num.get(), jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].listsuccess) == 0:#pas de colonie adjacente ?
            if jeu.ile.somtest2(self.gestionnaireFenetres.fenetreCourante.num.get(), jeu.currentcolor, jeu)==1:# y a t-il une route voisine de la bonne couleur ?
                jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].constr=1, jeu.currentcolor
                jeu.listjoueurs[jeu.currentcolor].villages[self.gestionnaireFenetres.fenetreCourante.num.get()]=jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()]
                item = self.gestionnaireFenetres.fenetreCourante.cf1.create_image((jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].x*1.75)+200,(jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].y*1.75)+200, image=label.image, tags = "image")
                jeu.listjoueurs[jeu.currentcolor].bois.set(jeu.listjoueurs[jeu.currentcolor].bois.get()-1)
                jeu.listjoueurs[jeu.currentcolor].argile.set(jeu.listjoueurs[jeu.currentcolor].argile.get()-1)
                jeu.listjoueurs[jeu.currentcolor].laine.set(jeu.listjoueurs[jeu.currentcolor].laine.get()-1)
                jeu.listjoueurs[jeu.currentcolor].ble.set(jeu.listjoueurs[jeu.currentcolor].ble.get()-1)
                self.f2.destroy()
                self.gestionnaireFenetres.loadFenetreSuivante("game2")
            else:
                print("Pas de routes proches")
        else:
            print("SommetIncorrect")
    def ok3 (self):
        self.f2.destroy()
        self.gestionnaireFenetres.loadFenetreSuivante("game2")
class ville:
    def __init__ (self, _gestionnaireFenetres):
        self.gestionnaireFenetres=_gestionnaireFenetres
        self.f2= Frame ()
        self.f2.grid (column = 1, row = 1)
        self.f2.label1 = Label (self.f2, text=("Joueur "+str(jeu.currentcolor)+", cliquez sur le sommet \n puis appuyez sur OK (ou Enter)"))
        self.f2.label1.grid()
        self.f2.bouton2 = Button (self.f2, text="OK",command = (lambda : self.ok2("blank")))
        self.f2.bouton2.grid ()
        self.f2.bind_all ('<Return>', self.ok2)
        self.f2.bouton3 = Button (self.f2, text="Annuler",command = self.ok3)
        self.f2.bouton3.grid ()
    def ok2 (self, event):
        if jeu.currentcolor == 'Bleu':
            photo = PhotoImage(file='villebleu.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Rouge':
            photo = PhotoImage(file='villerouge.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Jaune':
            photo = PhotoImage(file='villejaune.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Orange':
            photo = PhotoImage(file='villeorange.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.currentcolor == 'Vert':
            photo = PhotoImage(file='villevert.gif')
            label = Label(image=photo)
            label.image = photo
        if jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].constr == (1, jeu.currentcolor) :#il faut qu'il y ait deja une ville de meme couleur
            jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].constr=2, jeu.currentcolor
            jeu.listjoueurs[jeu.currentcolor].villages[self.gestionnaireFenetres.fenetreCourante.num.get()]=jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()]
            item = self.gestionnaireFenetres.fenetreCourante.cf1.create_image((jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].x*1.75)+200,(jeu.ile.sommets[self.gestionnaireFenetres.fenetreCourante.num.get()].y*1.75)+200, image=label.image, tags = "image")
            jeu.listjoueurs[jeu.currentcolor].minerai.set(jeu.listjoueurs[jeu.currentcolor].minerai.get()-3)
            jeu.listjoueurs[jeu.currentcolor].ble.set(jeu.listjoueurs[jeu.currentcolor].ble.get()-2)
            self.f2.destroy()
            self.gestionnaireFenetres.loadFenetreSuivante("game2")
        else:
            print("SommetIncorrect")
    def ok3 (self):
        self.f2.destroy()
        self.gestionnaireFenetres.loadFenetreSuivante("game2")
class trade:
    def __init__ (self, _root):
        self.fenetretop=Toplevel(_root)
        self.fenetretop.f6 = Frame (self.fenetretop)
        self.fenetretop.f6.label = Label (self.fenetretop, text= "Entrez votre offre, "+str(jeu.currentcolor)+" \n une valeur positive equivaut a une demande \n le negatif a une offre")
        self.fenetretop.f6.label.grid(column = 0, row = 0, columnspan=2)
        self.fenetretop.f6.label = Label (self.fenetretop, text = "Bois :", width=15)
        self.fenetretop.f6.label.grid(column = 0, row = 1)
        self.fenetretop.f6.bois= Entry (self.fenetretop, width=15)
        self.fenetretop.f6.bois.insert(END, 0)
        self.fenetretop.f6.bois.grid(column = 1, row = 1)
        self.fenetretop.f6.label = Label (self.fenetretop, text = "Argile :", width=15)
        self.fenetretop.f6.label.grid(column = 0, row = 2)
        self.fenetretop.f6.argile= Entry (self.fenetretop, width=15)
        self.fenetretop.f6.argile.insert(END, 0)
        self.fenetretop.f6.argile.grid(column = 1, row = 2)
        self.fenetretop.f6.label = Label (self.fenetretop, text = "Ble :", width=15)
        self.fenetretop.f6.label.grid(column = 0, row = 3)
        self.fenetretop.f6.ble= Entry (self.fenetretop, width=15)
        self.fenetretop.f6.ble.insert(END, 0)
        self.fenetretop.f6.ble.grid(column = 1, row = 3)
        self.fenetretop.f6.label = Label (self.fenetretop, text = "Laine :", width=15)
        self.fenetretop.f6.label.grid(column = 0, row = 4)
        self.fenetretop.f6.laine= Entry (self.fenetretop, width=15)
        self.fenetretop.f6.laine.insert(END, 0)
        self.fenetretop.f6.laine.grid(column = 1, row = 4)
        self.fenetretop.f6.label = Label (self.fenetretop, text = "Minerai :", width=15)
        self.fenetretop.f6.label.grid(column = 0, row = 5)
        self.fenetretop.f6.minerai= Entry (self.fenetretop, width=15)
        self.fenetretop.f6.minerai.insert(END, 0)
        self.fenetretop.f6.minerai.grid(column = 1, row = 5)
        self.fenetretop.f6.button2 = Button (self.fenetretop, text = "Accepter Rouge", command = self.rouge, width=15)
        self.fenetretop.f6.button2.grid(column = 0, row = 6)
        self.fenetretop.f6.button2 = Button (self.fenetretop, text = "Accepter Vert", command = self.vert, width=15)
        self.fenetretop.f6.button2.grid(column = 1, row = 6)
        self.fenetretop.f6.button2 = Button (self.fenetretop, text = "Accepter Bleu", command = self.bleu, width=15)
        self.fenetretop.f6.button2.grid(column = 0, row = 7)
        self.fenetretop.f6.button2 = Button (self.fenetretop, text = "Accepter Orange", command = self.orange, width=15)
        self.fenetretop.f6.button2.grid(column = 1, row =7)
        self.fenetretop.f6.button2 = Button (self.fenetretop, text = "Accepter Jaune", command = self.jaune, width=15)
        self.fenetretop.f6.button2.grid(column = 0, row = 8)
        self.fenetretop.f6.button3 = Button (self.fenetretop, text = "Annuler", command = self.leave, width=15)
        self.fenetretop.f6.button3.grid(column = 1, row = 8)
    def rouge (self): #Ici, j'aurais vraiment pu mettre une fonction pour eviter ces repetitions...
        print(int(self.fenetretop.f6.bois.get()))
        if jeu.listjoueurs.has_key("Rouge"):
            if jeu.listjoueurs["Rouge"].bois.get() >= int(self.fenetretop.f6.bois.get()) and jeu.listjoueurs["Rouge"].argile.get() >= int(self.fenetretop.f6.argile.get()) and jeu.listjoueurs["Rouge"].ble.get() >= int(self.fenetretop.f6.ble.get()) and jeu.listjoueurs["Rouge"].laine.get() >= int(self.fenetretop.f6.laine.get()) and jeu.listjoueurs["Rouge"].minerai.get() >= int(self.fenetretop.f6.minerai.get()):
                jeu.listjoueurs["Rouge"].bois.set(jeu.listjoueurs["Rouge"].bois.get()-int(self.fenetretop.f6.bois.get()))#on effectue les echanges de ressources
                jeu.listjoueurs["Rouge"].argile.set(jeu.listjoueurs["Rouge"].argile.get()-int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs["Rouge"].ble.set(jeu.listjoueurs["Rouge"].ble.get()-int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs["Rouge"].laine.set(jeu.listjoueurs["Rouge"].laine.get()-int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs["Rouge"].minerai.set(jeu.listjoueurs["Rouge"].minerai.get()-int(self.fenetretop.f6.minerai.get()))
                jeu.listjoueurs[jeu.currentcolor].bois.set(jeu.listjoueurs[jeu.currentcolor].bois.get()+int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs[jeu.currentcolor].argile.set(jeu.listjoueurs[jeu.currentcolor].argile.get()+int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs[jeu.currentcolor].ble.set(jeu.listjoueurs[jeu.currentcolor].ble.get()+int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs[jeu.currentcolor].laine.set(jeu.listjoueurs[jeu.currentcolor].laine.get()+int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs[jeu.currentcolor].minerai.set(jeu.listjoueurs[jeu.currentcolor].minerai.get()+int(self.fenetretop.f6.minerai.get()))
    def vert (self):
        if jeu.listjoueurs.has_key("Vert"):
            if jeu.listjoueurs["Vert"].bois.get() >= int(self.fenetretop.f6.bois.get()) and jeu.listjoueurs["Vert"].argile.get() >= int(self.fenetretop.f6.argile.get()) and jeu.listjoueurs["Vert"].ble.get() >= int(self.fenetretop.f6.ble.get()) and jeu.listjoueurs["Vert"].laine.get() >= int(self.fenetretop.f6.laine.get()) and jeu.listjoueurs["Vert"].minerai.get() >= int(self.fenetretop.f6.minerai.get()):
                jeu.listjoueurs["Vert"].bois.set(jeu.listjoueurs["Vert"].bois.get()-int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs["Vert"].argile.set(jeu.listjoueurs["Vert"].argile.get()-int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs["Vert"].ble.set(jeu.listjoueurs["Vert"].ble.get()-int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs["Vert"].laine.set(jeu.listjoueurs["Vert"].laine.get()-int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs["Vert"].minerai.set(jeu.listjoueurs["Vert"].minerai.get()-int(self.fenetretop.f6.minerai.get()))
                jeu.listjoueurs[jeu.currentcolor].bois.set(jeu.listjoueurs[jeu.currentcolor].bois.get()+int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs[jeu.currentcolor].argile.set(jeu.listjoueurs[jeu.currentcolor].argile.get()+int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs[jeu.currentcolor].ble.set(jeu.listjoueurs[jeu.currentcolor].ble.get()+int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs[jeu.currentcolor].laine.set(jeu.listjoueurs[jeu.currentcolor].laine.get()+int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs[jeu.currentcolor].minerai.set(jeu.listjoueurs[jeu.currentcolor].minerai.get()+int(self.fenetretop.f6.minerai.get()))
    def bleu (self):
        if jeu.listjoueurs.has_key("Bleu"):
            if jeu.listjoueurs["Bleu"].bois.get() >= int(self.fenetretop.f6.bois.get()) and jeu.listjoueurs["Bleu"].argile.get() >= int(self.fenetretop.f6.argile.get()) and jeu.listjoueurs["Bleu"].ble.get() >= int(self.fenetretop.f6.ble.get()) and jeu.listjoueurs["Bleu"].laine.get() >= int(self.fenetretop.f6.laine.get()) and jeu.listjoueurs["Bleu"].minerai.get() >= int(self.fenetretop.f6.minerai.get()):
                jeu.listjoueurs["Bleu"].bois.set(jeu.listjoueurs["Bleu"].bois.get()-int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs["Bleu"].argile.set(jeu.listjoueurs["Bleu"].argile.get()-int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs["Bleu"].ble.set(jeu.listjoueurs["Bleu"].ble.get()-int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs["Bleu"].laine.set(jeu.listjoueurs["Bleu"].laine.get()-int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs["Bleu"].minerai.set(jeu.listjoueurs["Bleu"].minerai.get()-int(self.fenetretop.f6.minerai.get()))
                jeu.listjoueurs[jeu.currentcolor].bois.set(jeu.listjoueurs[jeu.currentcolor].bois.get()+int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs[jeu.currentcolor].argile.set(jeu.listjoueurs[jeu.currentcolor].argile.get()+int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs[jeu.currentcolor].ble.set(jeu.listjoueurs[jeu.currentcolor].ble.get()+int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs[jeu.currentcolor].laine.set(jeu.listjoueurs[jeu.currentcolor].laine.get()+int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs[jeu.currentcolor].minerai.set(jeu.listjoueurs[jeu.currentcolor].minerai.get()+int(self.fenetretop.f6.minerai.get()))
    def orange (self):
        if jeu.listjoueurs.has_key("Orange"):
            if jeu.listjoueurs["Orange"].bois.get() >= int(self.fenetretop.f6.bois.get()) and jeu.listjoueurs["Orange"].argile.get() >= int(self.fenetretop.f6.argile.get()) and jeu.listjoueurs["Orange"].ble.get() >= int(self.fenetretop.f6.ble.get()) and jeu.listjoueurs["Orange"].laine.get() >= int(self.fenetretop.f6.laine.get()) and jeu.listjoueurs["Orange"].minerai.get() >= int(self.fenetretop.f6.minerai.get()):
                jeu.listjoueurs["Orange"].bois.set(jeu.listjoueurs["Orange"].bois.get()-int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs["Orange"].argile.set(jeu.listjoueurs["Orange"].argile.get()-int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs["Orange"].ble.set(jeu.listjoueurs["Orange"].ble.get()-int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs["Orange"].laine.set(jeu.listjoueurs["Orange"].laine.get()-int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs["Orange"].minerai.set(jeu.listjoueurs["Orange"].minerai.get()-int(self.fenetretop.f6.minerai.get()))
                jeu.listjoueurs[jeu.currentcolor].bois.set(jeu.listjoueurs[jeu.currentcolor].bois.get()+int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs[jeu.currentcolor].argile.set(jeu.listjoueurs[jeu.currentcolor].argile.get()+int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs[jeu.currentcolor].ble.set(jeu.listjoueurs[jeu.currentcolor].ble.get()+int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs[jeu.currentcolor].laine.set(jeu.listjoueurs[jeu.currentcolor].laine.get()+int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs[jeu.currentcolor].minerai.set(jeu.listjoueurs[jeu.currentcolor].minerai.get()+int(self.fenetretop.f6.minerai.get()))
    def jaune (self):
        if jeu.listjoueurs.has_key("Jaune"):
            if jeu.listjoueurs["Jaune"].bois.get() >= int(self.fenetretop.f6.bois.get()) and jeu.listjoueurs["Jaune"].argile.get() >= int(self.fenetretop.f6.argile.get()) and jeu.listjoueurs["Jaune"].ble.get() >= int(self.fenetretop.f6.ble.get()) and jeu.listjoueurs["Jaune"].laine.get() >= int(self.fenetretop.f6.laine.get()) and jeu.listjoueurs["Jaune"].minerai.get() >= int(self.fenetretop.f6.minerai.get()):
                jeu.listjoueurs["Jaune"].bois.set(jeu.listjoueurs["Jaune"].bois.get()-int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs["Jaune"].argile.set(jeu.listjoueurs["Jaune"].argile.get()-int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs["Jaune"].ble.set(jeu.listjoueurs["Jaune"].ble.get()-int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs["Jaune"].laine.set(jeu.listjoueurs["Jaune"].laine.get()-int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs["Jaune"].minerai.set(jeu.listjoueurs["Jaune"].minerai.get()-int(self.fenetretop.f6.minerai.get()))
                jeu.listjoueurs[jeu.currentcolor].bois.set(jeu.listjoueurs[jeu.currentcolor].bois.get()+int(self.fenetretop.f6.bois.get()))
                jeu.listjoueurs[jeu.currentcolor].argile.set(jeu.listjoueurs[jeu.currentcolor].argile.get()+int(self.fenetretop.f6.argile.get()))
                jeu.listjoueurs[jeu.currentcolor].ble.set(jeu.listjoueurs[jeu.currentcolor].ble.get()+int(self.fenetretop.f6.ble.get()))
                jeu.listjoueurs[jeu.currentcolor].laine.set(jeu.listjoueurs[jeu.currentcolor].laine.get()+int(self.fenetretop.f6.laine.get()))
                jeu.listjoueurs[jeu.currentcolor].minerai.set(jeu.listjoueurs[jeu.currentcolor].minerai.get()+int(self.fenetretop.f6.minerai.get()))
    def leave (self):
        self.fenetretop.destroy()
class monop:#carte monopole
    def __init__ (self, _root):
        self.fenetretop=Toplevel(_root)
        self.fenetretop.bois = Label (self.fenetretop, text = "Choisissez la ressource \n a monopoliser")
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "Bois", command=(lambda : jeu.monop(self.fenetretop,"bois")), width=20)
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "Argile", command=(lambda : jeu.monop(self.fenetretop,"argile")), width=20)
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "Ble", command=(lambda : jeu.monop(self.fenetretop,"ble")), width=20)
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "Laine", command=(lambda : jeu.monop(self.fenetretop,"laine")), width=20)
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "Minerai", command=(lambda : jeu.monop(self.fenetretop,"minerai")), width=20)
        self.fenetretop.bois.grid()
class discov:#carte decouverte
    def __init__ (self, _root):
        self.fenetretop=Toplevel(_root)
        self.fenetretop.bois = Label (self.fenetretop, text = "Vous trouvez...")
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "2 Bois", command=(lambda : jeu.discov(self.fenetretop,"bois")), width=15)
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "2 Argile", command=(lambda : jeu.discov(self.fenetretop,"argile")), width=15)
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "2 Ble", command=(lambda : jeu.discov(self.fenetretop,"ble")), width=15)
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "2 Laine", command=(lambda : jeu.discov(self.fenetretop,"laine")), width=15)
        self.fenetretop.bois.grid()
        self.fenetretop.bois = Button (self.fenetretop, text = "2 Minerai", command=(lambda : jeu.discov(self.fenetretop,"minerai")), width=15)
        self.fenetretop.bois.grid()
class cartes:#menu des cartes (mis dans "menubar")
    def __init__ (self, _gestionnaireFenetres,_root):
        self.fenetretop=Toplevel(_root)
        if jeu.listjoueurs[jeu.currentcolor].cards[0] > 0:
            self.fenetretop.victoire = Button (self.fenetretop, text = ("Reveler Carte Victoire ("+str(jeu.listjoueurs[jeu.currentcolor].cards[0])+")"), command=self.victory, width=30)
            self.fenetretop.victoire.grid()
        if jeu.listjoueurs[jeu.currentcolor].cards[1] > 0:
            self.fenetretop.chevalier = Button (self.fenetretop, text = ("Reveler Carte Chevalier ("+str(jeu.listjoueurs[jeu.currentcolor].cards[1])+")"), command=(lambda : self.knight(_gestionnaireFenetres)), width=30)
            self.fenetretop.chevalier.grid()
        if jeu.listjoueurs[jeu.currentcolor].cards[2] > 0:
            self.fenetretop.monopole = Button (self.fenetretop, text = ("Reveler Carte Monopole ("+str(jeu.listjoueurs[jeu.currentcolor].cards[2])+")"), command=self.monop, width=30)
            self.fenetretop.monopole.grid()
        if jeu.listjoueurs[jeu.currentcolor].cards[3] > 0:
            self.fenetretop.decouvr = Button (self.fenetretop, text = ("Reveler Carte Decouverte ("+str(jeu.listjoueurs[jeu.currentcolor].cards[3])+")"), command=self.discovery, width=30)
            self.fenetretop.decouvr.grid()
        #if jeu.listjoueurs[jeu.currentcolor].cards[4] > 0:
            #self.fenetretop.route = Button (self.fenetretop, text = ("Reveler Carte Route ("+str(jeu.listjoueurs[jeu.currentcolor].cards[4])+")"), width=30)
            #self.fenetretop.route.grid() #carte "route la plus longue" desactivee, faute de temps pour l'implementer (necessiterait une fonction complexe)
    def victory (self):
        if jeu.listjoueurs[jeu.currentcolor].cards[0] > 0:
            jeu.listjoueurs[jeu.currentcolor].cards[0] = jeu.listjoueurs[jeu.currentcolor].cards[0] -1
            jeu.listjoueurs[jeu.currentcolor].victory +=1
            self.fenetretop.destroy()
    def knight (self, _gestionnaireFenetres):
        if jeu.listjoueurs[jeu.currentcolor].cards[1] > 0:
            jeu.listjoueurs[jeu.currentcolor].cards[1] = jeu.listjoueurs[jeu.currentcolor].cards[1] -1
            jeu.listjoueurs[jeu.currentcolor].knight +=1
        self.fenetretop.destroy()
        _gestionnaireFenetres.fenetreCourante2.f2.destroy()
        print("Chevalier !")
        _gestionnaireFenetres.loadFenetreSuivante("rogue")
    def monop (self):
        if jeu.listjoueurs[jeu.currentcolor].cards[2] > 0:
            jeu.listjoueurs[jeu.currentcolor].cards[2] = jeu.listjoueurs[jeu.currentcolor].cards[2] -1
            self.gestionnaireFenetres.loadFenetreSuivante("monop")
        self.fenetretop.destroy()
    def discovery (self):
        if jeu.listjoueurs[jeu.currentcolor].cards[3] > 0:
            jeu.listjoueurs[jeu.currentcolor].cards[3] = jeu.listjoueurs[jeu.currentcolor].cards[3] -1
            self.gestionnaireFenetres.loadFenetreSuivante("discov")
        self.fenetretop.destroy()
