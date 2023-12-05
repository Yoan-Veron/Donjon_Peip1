
import math
import random
import copy
import time
import pygame


def heal(creature, unique=True):
    creature.hp = creature.hp + 3
    theGame()._hero.poison = False # soigne du poison
    return unique

def teleport(creature, unique=True):
    n=random.randint(0,len(theGame()._floor._rooms)-1) # prend une salle aléatoire
    r=theGame()._floor._rooms[n] # récupère la salle n dans la liste
    c=r.randEmptyCoord(theGame()._floor) # prend une coordonnée aléatoire dans cette salle
    posHero = theGame()._floor.pos(theGame()._hero) # récupère la position du héro
    theGame()._floor.rm(posHero) # supprime la position du héro
    theGame()._floor.put(c,theGame()._hero) # positionne le héro à la nouvelle coordonnée
    theGame()._floor._elem[theGame()._hero] = c # met à jour le dictionnaire d'éléments
    return unique

def throw(n, unique=False):

    ##CODE A METTRE

    return unique



class PartieGraph(object):
    def __init__(self,window_width=0,window_height=0):
        pygame.init() # Initialisation de Pygame

        self.theme = pygame.mixer.Sound("Sons/theme.ogg") # récupère tous les sons
        self.merchant = pygame.mixer.Sound("Sons/merchant.ogg")
        self.merchantHappy = pygame.mixer.Sound("Sons/merchantHappy.ogg")
        self.merchantNotHappy = pygame.mixer.Sound("Sons/merchantNotHappy.ogg")
        self.merchantNotGold = pygame.mixer.Sound("Sons/merchantNotGold.ogg")
        self.Stairs = pygame.mixer.Sound("Sons/Stairs.ogg")
        self.Gold = pygame.mixer.Sound("Sons/Gold.ogg")
        self.gameOver = pygame.mixer.Sound("Sons/game over.ogg")
        self.Chest = pygame.mixer.Sound("Sons/Chest.ogg")
        self.itemBroke = pygame.mixer.Sound("Sons/itemBroke.ogg")
        self.damage = pygame.mixer.Sound("Sons/damage.ogg")

        self.theme.play(loops=-1)
        self.theme.set_volume(0.1)  # volume à 10%

        screen_info = pygame.display.Info() # récupère les dimensions de l'écran
        self.window_width = screen_info.current_w
        self.window_height = screen_info.current_h

        # Créé une fenêtre
        self.window = pygame.display.set_mode((self.window_width, self.window_height), pygame.FULLSCREEN)

        icone = pygame.image.load("Images/icone.ico")
        pygame.display.set_icon(icone) # icone
        pygame.display.set_caption("ROGLIKE GAME")  # Titre de la fenêtre
        self.window.fill("midnightblue") # background couleur

        self.Space = self.window_height/theGame().size # définit l'espace entre les images et la taille des images en fonction de la taille de l'écran

    def Rectangle(self):

        rx = theGame().size*self.Space # paramètre du rectangle pour cacher le texte écrit
        ry = 250
        rl = self.window_width - rx
        rh = theGame().size*self.Space - ry
        pygame.draw.rect(self.window, "grey25", (rx, ry, rl, rh))

    def Intro(self):

        police = pygame.font.Font("police.ttf", 80)
        texte = police.render("---- Welcome "+str(theGame()._hero._name)+" ! ----", False, "white")
        rect_texte = texte.get_rect() # dimensions du texte

        x = (self.window_width - rect_texte.width) // 2 # position centrale pour le texte
        y = (self.window_height - rect_texte.height) // 2
        self.window.blit(texte, (x, y))

        pygame.display.update()  # Mettre à jour l'affichage


    def Afficher(self):

        # Charge les images
        ground = pygame.image.load("Images/ground.png")
        empty = pygame.image.load("Images/empty.png")
        hero = pygame.image.load("Images/hero.png")
        heal = pygame.image.load("Images/heal.png")
        Gold  = pygame.image.load("Images/Gold.png")
        potion = pygame.image.load("Images/potion.png")
        dagger = pygame.image.load("Images/dagger.png")
        sword = pygame.image.load("Images/sword.png")
        bow = pygame.image.load("Images/bow.png")
        leathervest = pygame.image.load("Images/leather vest.png")
        portoloin = pygame.image.load("Images/portoloin.png")
        chainmail = pygame.image.load("Images/chainmail.png")
        Goblin = pygame.image.load("Images/Goblin.png")
        Bat = pygame.image.load("Images/Bat.png")
        Ork = pygame.image.load("Images/Ork.png")
        Blob = pygame.image.load("Images/Blob.png")
        Dragon = pygame.image.load("Images/Dragon.png")
        Stairs = pygame.image.load("Images/Stairs.png")
        Chest = pygame.image.load("Images/Chest.png")
        Merchant = pygame.image.load("Images/Merchant.png")
        Spider = pygame.image.load("Images/Spider.png")
        Snake = pygame.image.load("Images/Snake.png")
        Bigsword = pygame.image.load("Images/big sword.png")
        Mastersword = pygame.image.load("Images/master sword.png")
        BigOrk = pygame.image.load("Images/Big Ork.png")
        Fantome = pygame.image.load("Images/Fantome.png")
        Ogre = pygame.image.load("Images/Ogre.png")


        # Redimensionne les images
        ground = pygame.transform.scale(ground, (self.Space, self.Space))
        empty = pygame.transform.scale(empty, (self.Space, self.Space))
        hero = pygame.transform.scale(hero, (self.Space, self.Space))

        IMAGES = {
        "heal" : pygame.transform.scale(heal, (self.Space, self.Space)),
        "Gold"  : pygame.transform.scale(Gold, (self.Space, self.Space)),
        "potion" : pygame.transform.scale(potion, (self.Space, self.Space)),
        "dagger" : pygame.transform.scale(dagger, (self.Space, self.Space)),
        "sword" : pygame.transform.scale(sword, (self.Space, self.Space)),
        "bow" : pygame.transform.scale(bow, (self.Space, self.Space)),
        "leather vest" : pygame.transform.scale(leathervest, (self.Space, self.Space)),
        "portoloin" : pygame.transform.scale(portoloin, (self.Space, self.Space)),
        "chainmail" : pygame.transform.scale(chainmail, (self.Space, self.Space)),
        "Goblin" : pygame.transform.scale(Goblin, (self.Space, self.Space)),
        "Bat" : pygame.transform.scale(Bat, (self.Space, self.Space)),
        "Ork" : pygame.transform.scale(Ork, (self.Space, self.Space)),
        "Blob" : pygame.transform.scale(Blob, (self.Space, self.Space)),
        "Dragon" : pygame.transform.scale(Dragon, (self.Space, self.Space)),
        "Stairs" : pygame.transform.scale(Stairs, (self.Space, self.Space)),
        "Chest" : pygame.transform.scale(Chest, (self.Space, self.Space)),
        "Merchant" : pygame.transform.scale(Merchant, (self.Space, self.Space)),
        "Spider" : pygame.transform.scale(Spider, (self.Space, self.Space)),
        "Snake" : pygame.transform.scale(Snake, (self.Space, self.Space)),
        "master sword" : pygame.transform.scale(Mastersword, (self.Space, self.Space)),
        "big sword" : pygame.transform.scale(Bigsword, (self.Space, self.Space)),
        "Big Ork" : pygame.transform.scale(BigOrk, (self.Space, self.Space)),
        "Fantome" : pygame.transform.scale(Fantome, (self.Space, self.Space)),
        "Ogre" : pygame.transform.scale(Ogre, (self.Space, self.Space)),
            }


        self.window.fill("grey25") # background couleur
        # Affiche les images
        for yi in range(len(m._floor._mat)):
            for xi in range(len(m._floor._mat[yi])):
                c = Coord(xi, yi)
                e = m._floor.get(c)
                if e != Map.empty:
                    self.window.blit(ground, (xi * self.Space, yi * self.Space)) # pour mettre le sol en dessous du héro ou de l'élément
                    if isinstance(e, Hero):
                        self.window.blit(hero, (xi * self.Space, yi * self.Space))
                    elif e != Map.ground:
                        self.window.blit(IMAGES[str(e._name)], (xi * self.Space, yi * self.Space))
                else:
                    self.window.blit(empty, (xi * self.Space, yi * self.Space))

        # Affiche le texte
        x = theGame().size*self.Space + 50 # placement du texte par rapport à la map
        police = pygame.font.Font("police.ttf", 25)
        self.window.blit(police.render("--- Game Level : "+str(theGame()._level)+" ---", False, "cornflowerblue"), (x, 60))
        self.window.blit(police.render(str(theGame()._hero.description()), False, "cornflowerblue"), (x, 200))
        police = pygame.font.Font("police.ttf", 22)
        self.window.blit(police.render(str(theGame()._floor.around()), False, "cornflowerblue"), (x, 260))
        self.window.blit(police.render(str(theGame().readMessages()), False, "cornflowerblue"), (x, 340))


        pygame.display.update()  # Mettre à jour l'affichage


    def listeMerchant(self,e):

        x = theGame().size*self.Space + 50 # placement du texte par rapport à la map
        y = 250
        if e.gold>0 : # si le héro a de l'or et de la place dans son inventaire
            if len(e._inventory) < e.sizeInventory:
                self.merchant.play() # sound
                time.sleep(1)

                self.Rectangle() # rectangle pour cacher le texte écrit

                police = pygame.font.Font("police.ttf", 25)
                texte = police.render("You have "+str(e.gold)+" Gold.", False, "cornflowerblue")
                rect_texte = texte.get_rect()
                self.window.blit(texte, (x, y))
                y = y + rect_texte.height

                texte = police.render("Choose item to buy (N°...) :", False, "cornflowerblue")
                rect_texte = texte.get_rect()
                self.window.blit(texte, (x, y))
                y = y + rect_texte.height+15

                n=0
                for i in Game.equipments: # affiche les items vendus
                    if n > 9:
                        break  # sort de la boucle si on atteint le 9ième élément
                    police = pygame.font.Font("police.ttf", 25)
                    texte = police.render("The price is "+str(i+1)+" Gold :", False, "cornflowerblue")
                    rect_texte = texte.get_rect()
                    self.window.blit(texte, (x, y))
                    y = y + rect_texte.height

                    for item in Game.equipments[i]:
                        police = pygame.font.Font("police.ttf", 20)
                        texte = police.render("  N°"+str(n)+" : "+str(item._name), False, "cornflowerblue")
                        rect_texte = texte.get_rect()
                        self.window.blit(texte, (x, y))
                        y = y + rect_texte.height
                        n=n+1
                    y = y + 15

                pygame.display.update()  # Mettre à jour l'affichage
                commande=getch()
                if str.isdigit(commande)==True and int(commande)<n:
                    n=0
                    for i in Game.equipments: # retrouve l'item choisi et l'ajoute à l'inventaire
                        for item in Game.equipments[i]:
                            if n==int(commande):
                                if e.gold >= i+1: # que si on a assez de gold pour acheter...
                                    if isinstance(item,Gold)==True: # si on veut acheter un gold ça sert à rien...
                                        e.gold = e.gold - i
                                    else:
                                        e._inventory.append(item) # on ajoute l'item à l'inventaire
                                        e.gold = e.gold - (i+1)  # on enlève le prix de l'item qui est la clé du dictionnaire
                                    self.merchantHappy.play()
                                    msg=str("Thank You, see you next time.")
                                    Game.addMessage(theGame(),msg)
                                else:
                                    self.merchantNotHappy.play()
                                    msg=str("You don't have enough money..")
                                    Game.addMessage(theGame(),msg)
                            n=n+1
                else:
                    self.merchantNotGold.play()
                    msg=str("You made a wrong choice..")
                    Game.addMessage(theGame(),msg)
            else:
                self.merchantNotGold.play()
                msg=str("Your inventory is full")
                Game.addMessage(theGame(),msg)
        else:
            self.merchantNotGold.play()
            msg=str("You need Gold")
            Game.addMessage(theGame(),msg)

    def selectGraph(self,l):
        x = theGame().size*self.Space + 50 # placement du texte par rapport à la mappe
        y = 250

        self.Rectangle() # rectangle pour cacher le texte écrit

        police = pygame.font.Font("police.ttf", 25)
        texte = police.render("Choose item> ", False, "cornflowerblue")
        rect_texte = texte.get_rect()
        self.window.blit(texte, (x, y))
        y = y + rect_texte.height + 15

        police = pygame.font.Font("police.ttf", 22)
        for i in l:
            texte = police.render(str(l.index(i))+": "+str(i._name), False, "cornflowerblue")
            rect_texte = texte.get_rect()
            self.window.blit(texte, (x, y))
            y = y + rect_texte.height + 5

        pygame.display.update()  # Mettre à jour l'affichage

    def fullDescriptionGraph(self,hero):
        x = theGame().size*self.Space + 50 # placement du texte par rapport à la map
        y = 250

        self.Rectangle() # rectangle pour cacher le texte écrit

        police = pygame.font.Font("police.ttf", 25)
        for i in hero.__dict__:

            if i != "_inventory" and i != "wear": # le cas de l'inventaire est traité à la fin
                if i[0]=="_": # Pour enlever le _ des attributs protégés
                    texte = police.render("> "+str(i[1:])+" : "+str(hero.__dict__[i]), False, "cornflowerblue")
                else:
                    texte = police.render("> "+str(i[0:])+" : "+str(hero.__dict__[i]), False, "cornflowerblue")
                rect_texte = texte.get_rect()
                self.window.blit(texte, (x, y))
                y = y + rect_texte.height + 15

        texte = police.render("> INVENTORY :", False, "cornflowerblue")
        rect_texte = texte.get_rect()
        self.window.blit(texte, (x, y))
        y = y + rect_texte.height + 15
        texte = police.render(str([x._name for x in hero._inventory]), False, "cornflowerblue")
        rect_texte = texte.get_rect()
        self.window.blit(texte, (x, y))
        y = y + rect_texte.height + 15

        texte = police.render("> WEARABLE :", False, "cornflowerblue")
        rect_texte = texte.get_rect()
        self.window.blit(texte, (x, y))
        y = y + rect_texte.height + 15
        texte = police.render(str([i+" : "+str(hero.wear[i]) for i in hero.wear]), False, "cornflowerblue")
        self.window.blit(texte, (x, y))

        pygame.display.update()  # Mettre à jour l'affichage

        commande = getch() # pour mettre en pause le jeu

    def affiche_commandes(self,hero):
            x = theGame().size*self.Space + 50 # placement du texte par rapport à la map
            y = 250

            self.Rectangle() # rectangle pour cacher le texte écrit

            texte = police.render("Ceci est un essai")
            self.window.blit(texte,(x,y))

            pygame.display.update()  # Mettre à jour l'affichage

            commande = getch() # pour mettre en pause le jeu


    def endGraph(self):

        self.theme.stop()
        self.gameOver.play()

        self.window.fill("midnightblue") # background couleur
        police = pygame.font.Font("police.ttf", 80)
        texte1 = police.render("---- GAME OVER ----", False, "crimson")

        police = pygame.font.Font("police.ttf", 45)
        texte2 = police.render("Game Level : "+str(theGame()._level), False, "white")
        texte3 = police.render("You killed "+str(theGame()._hero.kill)+" monsters ! Press space bar to exit.", False, "white")

        rect_texte1 = texte1.get_rect() # dimensions du texte
        rect_texte2 = texte2.get_rect()
        rect_texte3 = texte3.get_rect()

        x1 = (self.window_width - rect_texte1.width) // 2 # position centrale pour le texte
        y1 = (self.window_height - rect_texte1.height) // 2
        x2 = (self.window_width - rect_texte2.width) // 2
        y2 = (self.window_height - rect_texte2.height) // 2
        x3 = (self.window_width - rect_texte3.width) // 2
        y3 = (self.window_height - rect_texte3.height) // 2

        self.window.blit(texte1, (x1,y1-200)) # placement des textes
        self.window.blit(texte2, (x2,y2))
        self.window.blit(texte3, (x3,y3+200))

        pygame.display.update()  # Mettre à jour l'affichage



class Element(object):
    def __init__(self,name,abbrv="None"):
        self._name = name
        if abbrv=="None":
            abbrv=name[0]
        self._abbrv = abbrv

    def __repr__(self):
        return self._abbrv

    def description(self):
        return "<"+self._name+">"

    def meet(self,hero):
        raise NotImplementedError("Not implemented yet")


class Equipment(Element):
    def __init__(self,name,abbrv="None",usage=None,unique=True):
        Element.__init__(self,name,abbrv)
        self.usage = usage
        self.unique = unique

    def description(self):
        return "<"+str(self._name)+">"

    def meet(self,hero):
        hero.take(self)
        msg=str("You pick up a "+self.name)
        Game.addMessage(theGame(),msg)
        return True

    def use(self,creature):
        if self.usage != None:
            theGame()._message = []
            theGame().addMessage(str(creature._name)+" uses the "+str(self._name))
            return self.usage(creature, self.unique)
        else:
            theGame()._message = []
            theGame().addMessage("The "+str(self._name)+" is not usable")
            return False


class Wearable(Equipment):
    """A wearable equipment."""
    def __init__(self, name, place, effect, abbrv="",usage=None,unique=False,solidity=5):
        Equipment.__init__(self, name, abbrv, usage)
        self.place = place
        self.effect = effect
        self.unique = unique
        self.solidity = solidity


class Chest(Element):
    def __init__(self,name="Chest",abbrv="X",chestEquipment=None):
        Element.__init__(self, name, abbrv)
        if chestEquipment == None:
            level = theGame()._level*2
            chestEquipment = theGame().randElement(Game.equipments,level)
            self.chestEquipment = chestEquipment

    def __repr__(self):
        return self._abbrv
    def description(self):
        return "<"+str(self._name)+">"


class Stairs(Element):
    def __init__(self,name="Stairs",abbrv="E"):
        Element.__init__(self,name,abbrv)

    def __repr__(self):
        return self._abbrv
    def description(self):
        return "<"+str(self._name)+">"


class Gold(Element):
    def __init__(self,name="Gold",abbrv="o"):
        Element.__init__(self,name,abbrv)

    def __repr__(self):
        return self._abbrv
    def description(self):
        return "<"+str(self._name)+">"


class Merchant(Element):
    def __init__(self,name="Merchant",abbrv="M"):
        Element.__init__(self,name,abbrv)

    def __repr__(self):
        return self._abbrv
    def description(self):
        return "<"+str(self._name)+">"


class Creature(Element):
    def __init__(self,name,hp,abbrv="None",strength=1,key=False):
        Element.__init__(self,name,abbrv)
        self.hp = hp
        self.strength = strength
        self.key = key

    def description(self):
        return Element.description(self)+"("+str(self.hp)+")"

    def meet(self,other):
        self.hp=self.hp-other.strength
        msg=str("The "+other._name+" hits the "+self.description())
        Game.addMessage(theGame(),msg)

        if isinstance(other,Hero) == True: # pour la solidité de l'arme...
            if other.wear["right hand"] != None:
                other.wear["right hand"].solidity -=1
                if other.wear["right hand"].solidity <=0:
                    pGraph.itemBroke.play()
                    msg=str("You broke your "+str(other.wear["right hand"]._name))
                    Game.addMessage(theGame(),msg)
                    other.strength -= other.wear["right hand"].effect["strength"]
                    other.wear["right hand"] = None # enlève l'item du wearable inventory

        if self.hp<=0:
            return True
        return False


class Hero(Creature):
    def __init__(self,name="Hero",hp=10,abbrv="@",strength=2,armor=0,inventory=None,sizeInventory=10,kill=0,gold=0,key=False,poison=False):
        if inventory is None:
            inventory = []
        self._inventory=inventory
        Creature.__init__(self,name,hp,abbrv,strength)
        self.armor = armor
        self.kill = kill
        self.key = key
        self.poison = poison
        self.gold = gold
        self.sizeInventory = sizeInventory

        self.wear = {"right hand" : None , "torso" : None}

    def take(self,elem):
        if isinstance(elem,Equipment)==False:
            raise TypeError("Not a Equipment")
        self._inventory.append(elem)

    def description(self):
        return Creature.description(self)+str(self._inventory)

    def use(self,item):
        if item == None:
            theGame()._message = []
            theGame().addMessage("Not in inventory")
        elif isinstance(item,Equipment)==False:
            raise TypeError("Not a Equipment")
        elif item not in self._inventory:
            raise ValueError("Not in inventory")
        elif isinstance(item,Wearable)==True:
            for i in self.wear:
                if i == item.place:

                    del self._inventory[self._inventory.index(item)]
                    if self.wear[i] != None:
                        for cle, valeur in self.wear[i].effect.items():
                            if cle=="strength":
                                self.strength = self.strength - valeur
                            elif cle=="armor":
                                self.armor = self.armor - valeur
                        self._inventory.append(self.wear[i])
                    self.wear[i] = item

                    for cle, valeur in item.effect.items():
                        if cle=="strength":
                            self.strength = self.strength + valeur
                        elif cle=="armor":
                            self.armor = self.armor + valeur
                    theGame()._message = []
                    theGame().addMessage(str(self._name)+" equipped the "+str(item._name))


        elif item.use(self)==True:
            del self._inventory[self._inventory.index(item)]
        return "" # pour ne pas print "None"

    def throw(self,item): # jette l'élément de l'inventaire
        if item == None:
            theGame()._message = []
            theGame().addMessage("Not in inventory")
            return ""
        elif isinstance(item,Equipment)==False:
            raise TypeError("Not a Equipment")
        elif item not in self._inventory:
            raise ValueError("Not in inventory")

        c = theGame()._floor.pos(self)
        c1 = Coord(c.x,c.y-1)
        c2 = Coord(c.x,c.y+1)
        c3 = Coord(c.x-1,c.y)
        c4 = Coord(c.x+1,c.y)
        # trouve un coordonnée vide pour jeter l'élément de l'inventaire autour du héro -> teste tous les cas possibles
        if Map.__contains__(theGame()._floor,c1)==True:
            if Map.get(theGame()._floor,c1) == Map.ground:
                Map.put(theGame()._floor,c1,item)
                theGame()._floor._elem[item] = c1
                del self._inventory[self._inventory.index(item)]
                return ""
        if Map.__contains__(theGame()._floor,c2)==True:
            if Map.get(theGame()._floor,c2) == Map.ground:
                Map.put(theGame()._floor,c2,item)
                theGame()._floor._elem[item] = c2
                del self._inventory[self._inventory.index(item)]
                return ""
        if Map.__contains__(theGame()._floor,c3)==True:
            if Map.get(theGame()._floor,c3) == Map.ground:
                Map.put(theGame()._floor,c3,item)
                theGame()._floor._elem[item] = c3
                del self._inventory[self._inventory.index(item)]
                return ""
        if Map.__contains__(theGame()._floor,c4)==True:
            if Map.get(theGame()._floor,c4) == Map.ground:
                Map.put(theGame()._floor,c4,item)
                theGame()._floor._elem[item] = c4
                del self._inventory[self._inventory.index(item)]
                return ""
        msg=str("There is no place around")
        Game.addMessage(theGame(),msg)
        return "" # pour ne pas print "None"


class Coord(object):
    "Une coordonnee"
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if (self.x==other.x) and (self.y==other.y):
            return True
        else:
            return False

    def __repr__(self):
        return "<"+str(self.x)+","+str(self.y)+">"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        c = Coord(x,y)
        return c

    def __sub__(self, other):
        return Coord(self.x-other.x,self.y-other.y)

    def distance(self, other):
        c=self-other
        d=math.sqrt(math.pow(c.x,2) + math.pow(c.y,2))
        return d

    def direction(self, other):
        d=self.distance(other)
        sub=self-other
        cos = sub.x / abs(d)
        if cos > 1/math.sqrt(2):
            return Coord(-1,0)
        elif cos < -1/math.sqrt(2):
            return Coord(1,0)
        elif sub.y > 0:
            return Coord(0,-1)
        else:
            return Coord(0,1)


class Map(object):
    "Une carte"
    ground="."
    empty=" "
    dir={'z': Coord(0,-1), 's': Coord(0,1), 'd': Coord(1,0), 'q': Coord(-1,0)}

    def __init__(self,size=20,nbrooms=7,hero=None):
        if hero==None:
            hero=Hero()

        self._hero = hero

        self.size = size
        self._elem = {}

        M=[]
        for ym in range(size):
            m=[]
            for xm in range(size):
                m.append(Map.empty)
            M.append(m)
        self._mat = M

        self._roomsToReach = []
        self._rooms = []

        self.generateRooms(nbrooms) # Génère un nbre nbrooms de salles
        self.reachAllRooms() # Créé des corridors entre les salles

        pos=Room.center(self._rooms[0]) # Récupère le centre de la première salle
        self._mat[pos.y][pos.x]=self._hero # Positionne le héro dans la salle
        self._elem[self._hero] = pos
        for i in range(len(self._rooms)): # Décore les salles de la mappe avec 2 éléments
            self._rooms[i].decorate(self)

    def __repr__(self):
        m=""
        for i in self._mat:
            for j in i:
                m=m+str(j)
            m=m+"\n"
        return m

    def __len__(self):
        return self.size

    def __contains__(self, item):
        if isinstance(item, Coord)==True:
            CoordMax=Coord(self.size-1,self.size-1)
            if (item.x <= CoordMax.x) and (item.x >= 0) and (item.y <= CoordMax.y) and (item.y >= 0):
                return True

        elif item==self.hero:
            for i in self._mat:
                for j in i:
                    if j==self.hero:
                        return True
        return False

    def get(self,c): # Retourne l'élément aux coordonnées c
        self.checkCoord(c)
        return self._mat[c.y][c.x]

    def pos(self,e): # Retourne les coordonnées de l'élément e
        self.checkElement(e)
        for i in range(self.size):
            for j in range(self.size):
                if self._mat[i][j]==e:
                    return Coord(j,i)

    def put(self,c,e): # Place l'élément e aux coordonnées c dans la matrice et maj le dict _elem
        other = self.get(c) # Récupère l'élément en c
        self.checkElement(e)
        if e in self._elem:
            raise KeyError('Already placed')
        if other!=Map.ground or other==Map.empty:
            raise ValueError('Incorrect cell')
        self._mat[c.y][c.x] = e
        self._elem[e] = c

    def rm(self,c): # Supprime l'élément aux coordonnées c dans la matrice et maj le dict _elem
        e = self.get(c)
        self._mat[c.y][c.x] = Map.ground
        if e != Map.ground:
            del self._elem[e]

    def move(self,e,way): # Déplace un élément e dans une direction que si les coord sont valables et qu'il n'écrasse pas un autre élément
        pos=Map.pos(self,e)
        newPos=Coord(way.x+pos.x,way.y+pos.y)
        if (newPos in self) and (pos!=newPos): # A condition que la coordonnée entrée est valable
            other=Map.get(self,newPos) # Elément à la nouvelle position
            if other==Map.ground:
                Map.rm(self,pos)
                Map.put(self,newPos,e)
            elif other!=Map.empty:

                if isinstance(other, Creature)==True:
                    if Creature.meet(other,e)==True:
                        Map.rm(self,newPos)
                        self._hero.kill = self._hero.kill +1
                        if other.key == True:
                            self._hero.key = True
                            msg=str("You got a key !")
                            Game.addMessage(theGame(),msg)

                elif isinstance(other, Gold)==True: # gère la récupèration de gold
                    self.rm(newPos)
                    self._hero.gold = self._hero.gold +1
                    pGraph.Gold.play() # sound
                    msg=str("Gold : "+str(self._hero.gold))
                    Game.addMessage(theGame(),msg)

                elif isinstance(other, Stairs)==True:
                    pGraph.Stairs.play() # sound
                    theGame().buildFloor()
                    msg=str(str(theGame()._floor._hero._name)+" goes down")
                    theGame().addMessage(msg)
                    theGame()._level = theGame()._level +1

                elif isinstance(other, Chest)==True: # gère l'ouverture du coffre
                    if e.key==True:
                        pGraph.Chest.play() # sound (ouverture du coffre)
                        self.rm(newPos)
                        self.put(newPos,other.chestEquipment)
                        msg=str("You opened a "+other._name+" and got a "+other.chestEquipment._name)
                        Game.addMessage(theGame(),msg)
                        self._hero.key = False
                    else:
                        msg=str("You need a key to open the chest")
                        Game.addMessage(theGame(),msg)

                elif isinstance(other, Merchant)==True: # gère l'affichage de la liste d'objets à vendre
                    pGraph.listeMerchant(e)

                else:
                    if len(e._inventory) >= e.sizeInventory: # gère la taille de l'inventaire
                        msg=str("Your inventory is full")
                        Game.addMessage(theGame(),msg)
                    else:
                        Hero.take(e,other)
                        Map.rm(self,newPos)

    def addRoom(self,room):
        self._roomsToReach.append(room)
        for y in range(len(self._mat)):
            for x in range(len(self._mat[y])):
                c=Coord(x,y)
                if Room.__contains__(room,c)==True:
                    self._mat[y][x]=Map.ground

    def findRoom(self,coord):
        for r in self._roomsToReach:
            if Room.__contains__(r,coord)==True:
                return r
        return False

    def intersectNone(self,room):
        for r in self._roomsToReach:
            if Room.intersect(r,room)==True:
                return False
        return True

    def dig(self,coord):
        self._mat[coord.y][coord.x]=Map.ground
        r=self.findRoom(coord)
        if r!=False:
            self._rooms.append(r)
            for i in range(len(self._roomsToReach)): # On parcourt la liste pour trouver la position de la salle
                if self._roomsToReach[i]==r:
                    pos=i
            del self._roomsToReach[pos] # On supprime la salle

    def corridor(self,start,end):
        if start.y >= end.y: # = est la cas où le corridor est un ligne horizontale
            sensy=-1 # On recule
        else:
            sensy=1 # On avance
        if start.x >= end.x: # = est la cas où le corridor est un ligne verticale
            sensx=-1 # On recule
        else:
            sensx=1 # On avance
        coord=start
        while coord.y!=end.y:
            self.dig(coord)
            coord=Coord(coord.x,coord.y+1*sensy)
        self.dig(coord) # Fait la condition quand coord.y==end.y
        while coord.x!=end.x:
            self.dig(coord)
            coord=Coord(coord.x+1*sensx,coord.y)
        self.dig(coord) # Fait la condition quand coord.x==end.x

    def reach(self):
        A=random.choice(self._rooms)
        B=random.choice(self._roomsToReach)
        Am=Room.center(A)
        Bm=Room.center(B)
        self.corridor(Am,Bm)

    def reachAllRooms(self):
        if self._rooms == []:
            self._rooms.append(self._roomsToReach[0])
            del self._roomsToReach[0] # On transfère la première salle dans les salles reliées
        while self._roomsToReach != []:
            self.reach()

    def randRoom(self):
        x1=random.randint(0, len(self) - 3)
        y1=random.randint(0, len(self) - 3)
        l=random.randint(3,8) # Largeur de la salle
        h=random.randint(3,8) # Hauteur de la salle
        x2=min(len(self) - 1, x1 + l)
        y2=min(len(self) - 1, y1 + h)
        c1=Coord(x1,y1)
        c2=Coord(x2,y2)
        newRoom=Room(c1,c2)
        return newRoom

    def generateRooms(self,n):
        for i in range(n):
            newRoom=self.randRoom()
            if self.intersectNone(newRoom)==True:
                self.addRoom(newRoom)

    def checkCoord(self,c):
        if isinstance(c,Coord)==False:
            raise TypeError("Not a Coord")
        if c not in self:
            raise IndexError('Out of map coord')

    def checkElement(self,e):
        if isinstance(e,Element)==False:
            raise TypeError('Not a Element')

    def moveAllMonsters(self):
        for i in self._elem:
            if isinstance(i,Creature)==True and i!=self._hero:
                way=Coord.direction(self._elem[i], self.pos(self._hero))
                d=Coord.distance(self._elem[i], self.pos(self._hero))
                newCoord=Coord.__add__(self._elem[i], way)
                e=self.get(newCoord)
                if d<6 and e==Map.ground:
                    self._mat[self._elem[i].y][self._elem[i].x] = Map.ground
                    self._mat[newCoord.y][newCoord.x] = i
                    self._elem[i] = newCoord
                elif e==self._hero:
                    pGraph.damage.play() # sound (la créature frappe le héro)
                    self._hero.meet(i)
                    if i._name == "Spider": # empoisonne le héro si créature = spider
                        self._hero.poison = True

    def around(self): # Affichage des éléments et créatures autour du héro
        pos=self.pos(self._hero)
        around=""
        c1=Coord(pos.x,pos.y-1)
        c2=Coord(pos.x,pos.y+1)
        c3=Coord(pos.x-1,pos.y)
        c4=Coord(pos.x+1,pos.y)
        if c1 in self:
            elem1=self.get(c1)
            if elem1!=Map.ground and elem1!=Map.empty:
                around = around + str(elem1.description()) + " / "
        if c2 in self:
            elem2=self.get(c2)
            if elem2!=Map.ground and elem2!=Map.empty:
                around = around + str(elem2.description()) + " / "
        if c3 in self:
            elem3=self.get(c3)
            if elem3!=Map.ground and elem3!=Map.empty:
                around = around + str(elem3.description()) + " / "
        if c4 in self:
            elem4=self.get(c4)
            if elem4!=Map.ground and elem4!=Map.empty:
                around = around + str(elem4.description()) + " / "
        return around


class Room(object):
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2

    def __repr__(self):
        x1=str(self.c1.x)
        y1=str(self.c1.y)
        x2=str(self.c2.x)
        y2=str(self.c2.y)
        return "[<"+x1+","+y1+">, <"+x2+","+y2+">]"

    def __contains__(self,c):
        if (c.x >= self.c1.x and c.y >= self.c1.y) and (c.x <= self.c2.x and c.y <= self.c2.y):
            return True

    def center(self):
        xmin=self.c1.x
        ymin=self.c1.y
        xmax=self.c2.x
        ymax=self.c2.y
        xm=((xmax-xmin)//2)+xmin # Max - Min divisé par 2 et on rajoute le Min la nouvelle valeur par de 0
        ym=((ymax-ymin)//2)+ymin # Max - Min divisé par 2 et on rajoute le Min la nouvelle valeur par de 0
        cm=Coord(xm,ym)
        return cm

    def intersect(self,r):
        cHGr=r.c1 # Coordonnée Haut Gauche de la salle r
        cBDr=r.c2 # Coordonnée Bas Droite de la salle r
        cHDr=Coord(cBDr.x,cHGr.y) # Coordonnée Haut Droite de la salle r
        cBGr=Coord(cHGr.x,cBDr.y) # Coordonnée Bas Gauche de la salle r
        cHGself=self.c1 # Coordonnée Haut Gauche de la salle self
        cBDself=self.c2 # Coordonnée Bas Droite de la salle self
        cHDself=Coord(cBDself.x,cHGself.y) # Coordonnée Haut Droite de la salle self
        cBGself=Coord(cHGself.x,cBDself.y) # Coordonnée Bas Gauche de la salle self
        if (cHGr in self) or (cBDr in self) or (cHDr in self) or (cBGr in self) or (cHGself in r) or (cBDself in r) or (cHDself in r) or (cBGself in r):
            return True
        return False

    def randCoord(self):
        x=random.randint(self.c1.x,self.c2.x)
        y=random.randint(self.c1.y,self.c2.y)
        return Coord(x,y) # Coordonnée dans la salle self

    def randEmptyCoord(self,m):
        cm=self.center()
        v=False
        while v==False:
            c=self.randCoord()
            if m.get(c)==m.ground and c!=cm:
                v=True
        return c

    def decorate(self,m):

        c1=self.randEmptyCoord(m) # Equipement
        e1=Game.randEquipment(theGame())
        m.put(c1,e1)
        m._elem[e1]=c1 # Rajoute l'élément au dictionnaire elem

        c2=self.randEmptyCoord(m) # Monstre
        e2=Game.randMonster(theGame())
        m.put(c2,e2)
        m._elem[e2]=c2 # Rajoute l'élément au dictionnaire elem


class Game(object):
    "Mécanique principale du jeu"

    equipments = { 0: [ Equipment("heal",abbrv="#",usage = heal), Gold() ],
                  1: [ Equipment("potion",abbrv="!",usage = teleport,unique = True), Wearable("dagger",abbrv="t",place = "right hand", usage=lambda self, hero : throw(2, False), effect={'strength': 1}) ],
                  2: [ Wearable("sword",abbrv="T",place='right hand',effect={'strength': 2}), Equipment("bow",abbrv="c", usage=lambda self, hero: throw(1, True)), Wearable("leather vest",abbrv="v",place='torso', effect={'armor': 1}) ],
                  3: [ Equipment("portoloin",abbrv="l",usage = teleport,unique = False) ],
                  4: [ Wearable("chainmail",abbrv="&",place='torso', effect={'armor': 3})],
                  6: [ Wearable("big sword",abbrv="L",place='right hand',effect={'strength': 4})],
                  10: [ Wearable("master sword",abbrv="P",place='right hand',effect={'strength': 8})] }

    monsters = { 0: [ Creature("Goblin",4,abbrv="g"), Creature("Bat",2,abbrv="w") ],
                1: [ Creature("Ork",6,strength=2), Creature("Blob",10,abbrv="b") ],
                2: [ Creature("Spider",5,strength=2,abbrv="m"), Creature("Snake",10,strength=3,abbrv="S") ],
                4: [ Creature("Ogre",8,strength=3,abbrv="G"), Creature("Fantome",6,strength=3,abbrv="F") ],
                6: [ Creature("Dragon",20,strength=3,abbrv="W"), Creature("Big Ork",12,strength=3,abbrv="B") ] }

    _actions = { 'z': lambda hero: theGame()._floor.move(hero,Coord(0,-1)), # Haut
    's': lambda hero: theGame()._floor.move(hero,Coord(0,1)), # Bas
    'q': lambda hero: theGame()._floor.move(hero,Coord(-1,0)), # Gauche
    'd': lambda hero: theGame()._floor.move(hero,Coord(1,0)), # Droite
    'a': lambda hero: theGame()._floor.move(hero,Coord(-1,-1)), # Diagonale Haut Gauche
    'e': lambda hero: theGame()._floor.move(hero,Coord(1,-1)), # Diagonale Haut Droite
    'w': lambda hero: theGame()._floor.move(hero,Coord(-1,1)), # Diagonale Bas Gauche
    'x': lambda hero: theGame()._floor.move(hero,Coord(1,1)), # Diagonale Bas Droite

    'i': lambda hero: pGraph.fullDescriptionGraph(hero), # infos sur le héro
    'k': lambda hero: hero.__setattr__("hp", 0), # tue le héro
    'u': lambda hero: print(hero.use(theGame().select(hero._inventory))), # pour utiliser un élément de l'inventaire
    't': lambda hero: print(hero.throw(theGame().select(hero._inventory))), # pour jeter un élément de l'inventaire
    'space': lambda hero: None,  # passer un tour

    'c': lambda hero: pGraph.affiche_commandes(hero)}#infos commandes


    def __init__(self,size=20,nbrooms=7,hero=None,level=1):
        if hero == None:
            hero = Hero()
        self._hero = hero
        self.size = size
        self.nbrooms = nbrooms
        self._level = level
        self._floor = None
        self._message = []

    def buildFloor(self):
        self._floor=Map(size=self.size,nbrooms=self.nbrooms,hero=self._hero) # création de la mappe
        cm=Room.center(self._floor._rooms[-1]) # placement de l'escalier
        self._floor._mat[cm.y][cm.x] = Stairs()

        r=random.choice(self._floor._rooms) # placement du coffre sur la mappe
        c=r.randEmptyCoord(self._floor)
        elemChest = Chest()
        self._floor._mat[c.y][c.x] = elemChest
        self._floor._elem[elemChest] = Coord(c.x,c.y)
        l=[]
        for i in self._floor._elem: # donne une cle à un monstre aléatoire sur la mappe
            if isinstance(i,Creature)==True and isinstance(i,Hero)==False:
                l.append(i)
        monsterKey=random.choice(l)
        monsterKey.key = True

        r=random.choice(self._floor._rooms) # placement du marchand sur la mappe
        c=r.randEmptyCoord(self._floor)
        elemMerchant = Merchant()
        self._floor._mat[c.y][c.x] = elemMerchant
        self._floor._elem[elemMerchant] = Coord(c.x,c.y)

    def addMessage(self,msg):
        self._message.append(msg)

    def readMessages(self):
        MSG=""
        for msg in range(len(self._message)):
            MSG=MSG+self._message[msg]+". "
        self._message=[]
        return MSG

    def randElement(self,collection,level=None): # si level n'est pas renseigné, il prend pas défaut le level de la game
        if level == None:
            level = self._level
        x=random.expovariate(1/level)
        for k in collection.keys():
            if k <= x:
                l = collection[k]
        return copy.copy(random.choice(l))

    def randEquipment(self):
        return self.randElement(Game.equipments)

    def randMonster(self):
        return self.randElement(Game.monsters)

    def select(self,l):
        pGraph.selectGraph(l)
        n=getch()
        if str.isdigit(n)==True and int(n)<len(l):
            return l[int(n)]
        else:
            return None


    def play(self):
        """Main game loop"""
        self.buildFloor()

        pGraph.Intro() # construit la fenêtre
        time.sleep(2)

        while self._hero.hp > 0:

            pGraph.Afficher() # met à jour la fenêtre

            commande = getch()
            if commande in Game._actions:
                Game._actions[commande](self._hero)
            self._floor.moveAllMonsters()
            if self._hero.poison == True: # si le héro est empoisonné on retire 1 hp à chaque tour
                pGraph.damage.play() # sound (la créature frappe le héro)
                msg=str("You are poisoned, take heal !")
                Game.addMessage(theGame(),msg)
                self._hero.hp -= 1

        pGraph.endGraph() # affiche de fin
        commande = getch()

        pygame.quit() # ferme la fenêtre




#####################################################################################################################


def getch(): # récupère la touche du clavier depuis l'interface graphique
    commandes = {
        pygame.K_z: "z",
        pygame.K_s: "s",
        pygame.K_q: "q",
        pygame.K_d: "d",
        pygame.K_a: "a",
        pygame.K_e: "e",
        pygame.K_w: "w",
        pygame.K_x: "x",
        pygame.K_i: "i",
        pygame.K_k: "k",
        pygame.K_u: "u",
        pygame.K_t: "t",

        #Test Commandes
        pygame.K_c: "c",


        pygame.K_SPACE: "space",
        pygame.K_0: "0",
        pygame.K_1: "1",
        pygame.K_2: "2",
        pygame.K_3: "3",
        pygame.K_4: "4",
        pygame.K_5: "5",
        pygame.K_6: "6",
        pygame.K_7: "7",
        pygame.K_8: "8",
        pygame.K_9: "9",
    }
    commande = ""
    while commande == "":
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: # si on presse une touche du clavier
                if event.key in commandes:
                    commande = commandes[event.key] # on met dans commande la touche
    return commande




n = input("Entrer votre pseudo : ")
#a = int(input("Entrer votre numéro d'avatar : "))
def theGame(game = Game(size=20,nbrooms=15,hero=Hero(name=n,hp=20,abbrv="@",strength=4,inventory=None))):  # A changer pour changer les paramètres du jeu
    return game




pGraph = PartieGraph()
m = theGame()
m.play()
