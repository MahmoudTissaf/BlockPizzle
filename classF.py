from random import *
from math import *
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')
import pygame

couleurs = [
(0,   0,   0  ),
(255, 85,  85),

(100, 200, 115),
(120, 108, 245),
(255, 140, 50 ),
(50,  120, 52 ),
(146, 202, 73 ),
(150, 161, 218 ),
(35,  35,  35) 
]

color=(255,255,255)

######1 CASE##########

L1_1=[[0,0]] #-

L1=[L1_1]

######2 CASES#########

L2_1=[[0,0],[1,0]] #vertical |
L2_2=[[0,0],[0,1]] #horizontal --

L2=[L2_1,L2_2]



######3 CASES#########

L3_1=[[0,0],[0,1],[0,2]] #---
L3_2=[[0,0],[1,0],[1,1]] #|_
##L3_3=[[0,0],[0,1],[-1,1]] #_|
L3_3=[[1,0],[1,1],[0,1]] #_|
L3_4=[[0,1],[1,1],[0,0]] #-|
L3_5=[[0,0],[1,0],[0,1]] #|-
L3_6=[[0,0],[1,0],[2,0]] #|

L3=[L3_1,L3_2,L3_3,L3_4,L3_5,L3_6]

######4 CASES#########

L4_1=[[0,0],[0,1],[0,2],[1,0]] #|--
#L4_2=[[0,0],[-1,0],[0,-1],[0,-2]] #__|
L4_2=[[1,2],[0,2],[1,1],[1,0]] #__|
#L4_3=[[0,0],[0,-1],[2,0],[1,0]] #-|
L4_3=[[0,1],[0,0],[2,1],[1,1]] #-|
L4_4=[[0,0],[1,0],[2,0],[0,1]] #|-
#L4_5=[[0,0],[0,-1],[0,1],[1,0]] #-|-
L4_5=[[0,1],[0,0],[0,2],[1,1]] #-|-
L4_6=[[1,1],[0,1],[1,2],[1,0]] #_|_
L4_7=[[0,0],[0,1],[0,2],[0,3]] #----
L4_8=[[0,0],[1,0],[2,0],[3,0]] #|
L4_9=[[1,0],[0,0],[1,1],[0,1]] #||
#L4_10=[[0,0],[0,1],[1,1],[-1,1]] #-|
L4_10=[[1,0],[1,1],[2,1],[0,1]] #-|
##L4_11=[[0,0],[0,-1],[1,-1],[-1,-1]] #|-
L4_11=[[1,1],[1,0],[2,0],[0,0]] #|-
#L4_12=[[0,0],[0,-1],[0,-2],[1,0]] #--|
L4_12=[[0,0],[0,1],[0,2],[1,0]] #--|
#L4_13=[[0,0],[0,1],[0,2],[-1,0]] #|__
L4_13=[[1,0],[1,1],[1,2],[0,0]] #|__


L4=[L4_1,L4_2,L4_3,L4_4,L4_5,L4_6,L4_7,L4_8,L4_9,L4_10,L4_11,L4_12,L4_13]

#L=[L1,L2,L3,L4]
L=[L1_1,L2_1,L2_2,L3_1,L3_2,L3_3,L3_4,L3_5,L3_6,L4_1,L4_2,L4_3,L4_4,L4_5,L4_6,L4_7,L4_8,L4_9,L4_10,L4_11,L4_12,L4_13]
CentreL=[()]
def MinMax(L,i,j):         
    maxx=-999999
    minx=999999
    maxy=-999999
    miny=999999
    for p in range (len(L)):
        y=j+(L[p][0]*80)
        x=i+(L[p][1]*80)
        maxx=max(x,maxx)
        maxy=max(y,maxy)
        minx=min(x,minx)
        miny=min(y,miny)
    return(minx,miny,maxx,maxy)

class Block(pygame.sprite.Sprite):
    def __init__(self,c,image,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.cote=c
        self.image=pygame.transform.scale(self.image,(self.cote,self.cote))
        #self.L=L
        self.x=x
        self.y=y
        #print("Bloc ", x,y)
        self.rect=self.image.get_rect()
        self.rect.x=x
        self.rect.y=y
        #print(self.rect)
       
##    def update(self):
##        self.x=
        
        #Centre de gravité:self.rect.centerx
                           #self.rect.centery

##        self.groupBlock=pygame.sprite.Group()

class Forme(pygame.sprite.Sprite):
    def __init__(self,L):
        pygame.sprite.Sprite.__init__(self)
        self.bloc=Block( 80,'carre.gif',-1,-1)
        self.grille1=Grille(10,0)
        self.L=L



class Grille(pygame.sprite.Sprite):
    
    def __init__(self,n,val):
        pygame.sprite.Sprite.__init__(self)
        self.n=n
        self.g=[]
        self.val=val
        pygame.init()
        self.block =Block(80,'carre.gif',-1,-1)
        self.WIDTH=1280
        self.HEIGHT=1000
        self.screen = pygame.display.set_mode((self.WIDTH,self.HEIGHT))
        self.damier = pygame.image.load("grille10.png")
        self.damier=pygame.transform.scale(self.damier,(800,600))
        self.screen.fill(color)
        self.forme_suiv = L[randint(0,len(L)-1)]
        self.formes_suiv=[]
        
        for i in range (self.n) :
            self.g = self.g + [[self.val]*self.n]

    def generer(self):
        self.formes_suiv=[]
        for i in range(3):
            f=L[randint(0,len(L)-1)]
            self.formes_suiv.append(f)
            #self.affiche_forme_suiv(f)
        return self.formes_suiv
            



    def affiche_forme_suiv(self,L1):
        x1=900
        y1=200
        sautx=0
        sauty=0
        minx=x1
        miny=y1
        maxx=80
        maxy=80
        for L in L1:
           # L=L1[0]
            (minx,miny,maxx,maxy)=MinMax(L,980,200)
            #pygame.draw.rect(self.screen,(0,255,0),(minx+0,miny+80,(maxx-minx)+80,(maxy-miny)+80))
            pygame.draw.rect(self.screen,(0,255,0),(980,200,(maxx-minx)+80,(maxy-miny)+80))

            #print(minx,miny,maxx,maxy)
                
            for p in range (len(L)):
                y=200+(L[p][0]*80) #miny+(L[p][0]*80) #miny+floor((maxy-miny)/2 +80) +sauty+(L[p][0]*80)
                x=980+(L[p][1]*80)
                self.screen.blit(self.block.image, (x,y))

##            sautx =maxx+10
##            sauty =miny
##            ## += 5+80*len(L)
##            pygame.display.flip()
         


    def affiche_forme_suiv1(self,L,i,j):
        (minx,miny,maxx,maxy)=MinMax(L,j,i)
        pygame.draw.rect(self.screen,(0,255,0),(j,i,(maxx-minx)+80,(maxy-miny)+80))
    
        for p in range (len(L)):
            y=i+(L[p][0]*80) 
            x=j+(L[p][1]*80)
            self.screen.blit(self.block.image,(x,y))



    def affiche(self) :
##        self.screen.blit(self.damier,(50,50))
        n=len(self.g)
        for i in range (n):
            for j in range (n):
                print(self.g[i][j], end= " " )
##                if self.g[i][j]!=self.val:
##                    self.screen.blit(self.block.image, (50+j*80, 50+i*80))
            print()
        print()
        print()

    def placer(self,x,y,val2): #placer une case
        self.g[x][y]=val2
       # self.screen.blit(self.block.image,(900,700))

##        pygame.display.flip()


#   def placer2(self,L,val2): placer un bloc en haut a droite
#      for i in range(len(L)):
#         grille1.placer(L[i][0],L[i][1],val2)

    def placer3(self,x1,y1,L,val2):

        for p in range (len(L)):
            x=x1+L[p][0]
            y=y1+L[p][1]

            if x<0 or x>self.n-1 or y<0 or y>self.n-1 :
                print("Problèmes de bord")
                return False

            else :
                if  self.g[x][y]!=self.val:
                    print("Problèmes de cases remplies")
                    return False

        for p in range (len(L)):
            x=x1+L[p][0]
            y=y1+L[p][1]
            
            self.placer(x,y,val2)
        return True

   

    def ligne_remplie(self,i):
        for y in range(self.n):
            if self.g[i][y]==0:
                return False
        return True

    def colonne_remplie(self,i):
        for x in range(self.n):
            if self.g[x][i]==0:
                return False
        return True

    def destruction(self):
        C_remplies=[]
        L_remplies=[]
        for i in range(self.n):
            if self.colonne_remplie(i)==True:
                C_remplies.append(i)
        for j in range(self.n):
            if self.ligne_remplie(j)==True:
                L_remplies.append(j)

        for l in L_remplies:
            self.destructionLig(l)
        for l in C_remplies:    
            self.destructionCol(l)
        return self.g

    def destructionCol(self,y):

##        t=self.colonne_remplie(y)
##        if t==True:
        for j in range (self.n):
            self.g[j][y]=self.val
##            self.screen.blit(self.damier,(50,50))

        return self.g

    def destructionLig(self,x):

##        c=self.ligne_remplie(x)
##        if c==True:
        for j in range (self.n):
           self.g[x][j]=self.val
##           self.screen.blit(self.damier,(50,50))


        return self.g

##    ######3 CASES#########
##
##L3_1=[[0,0],[0,1],[0,2]] #---
##L3_2=[[0,0],[-1,0],[0,1]] #|_
##L3_3=[[0,0],[0,-1],[-1,0]] #_|
##L3_4=[[0,0],[1,0],[0,-1]] #-|
##L3_5=[[0,0],[1,0],[0,1]] #|-
##L3_6=[[0,0],[1,0],[2,0]] #|
##
##L3=[L3_1,L3_2,L3_3,L3_4,L3_5,L3_6]
##
########4 CASES#########
##
##L4_1=[[0,0],[0,1],[0,2],[1,0]] #|--
##L4_2=[[0,0],[-1,0],[0,-1],[0,-2]] #__|
##L4_3=[[0,0],[0,-1],[2,0],[1,0]] #-|
##L4_4=[[0,0],[1,0],[2,0],[0,1]] #|-
##L4_5=[[0,0],[0,-1],[0,1],[1,0]] #-|-
##L4_6=[[0,0],[-1,0],[0,1],[0,-1]] #_|_
##L4_7=[[0,0],[0,1],[0,2],[0,3]] #----
##L4_8=[[0,0],[1,0],[2,0],[3,0]] #|
##L4_9=[[0,0],[-1,0],[0,1],[-1,1]] #||
##L4_10=[[0,0],[0,1],[1,1],[-1,1]] #-|
##L4_11=[[0,0],[0,-1],[1,-1],[-1,-1]] #|-
##L4_12=[[0,0],[0,-1],[0,-2],[1,0]] #--|
##L4_13=[[0,0],[0,1],[0,2],[-1,0]] #|__
