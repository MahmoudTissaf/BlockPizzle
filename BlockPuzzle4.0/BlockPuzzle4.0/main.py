from random import *


import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')
import pygame
import numpy
from classF import *
from math import *
def entiere(n):
    if floor(n%1)>= 0.5 :
        return(floor(n)+1)
        #return(int(n)+1)
    else:
        return(floor(n))
        #return(int(n))


def Permis(groupForme,groupBlock):                                 #permissions
    #return(True)
    for blocF in groupForme :
        for bloc in groupBlock :
            if blocF.x+blocF.cote >=900 or  blocF.y+blocF.cote >=900 :
                return(False)
            if blocF.rect.colliderect(bloc.rect) :
                    return(False) #print("Rencontre",blocF.rect,bloc.rect)
    return(True)

grille1=Grille(10,0)
grille1.damier=pygame.transform.scale(grille1.damier,(800,800))
grille1.screen.blit(grille1.damier,(50,50))




##grille1.placer3(0,0,L4_7,"o")
##grille1.placer3(0,4,L4_7,"o")
##grille1.placer3(0,8,L2_2,"o")
##grille1.placer3(7,0,L4_13,"o")

#Groupe de bloc
groupBlock=pygame.sprite.Group()
groupForme=pygame.sprite.Group()
##groupBlock.add(Block([0,0]))
##groupBlock.add(Block([0,1]))
##groupBlock.add(Block([0,2]))



##grille1.affiche()
##grille1.destruction()
##grille1.affiche()
##
###damier = pygame.image.load("grille10.png")
##pygame.display.flip()
##

Fini=False
##
##j=250#event.pos[0]
##i=200#event.pos[1]
##L=L4_13
##
##for p in range (len(L)):
####    x=i+L[p][0]
####    y=j+L[p][1]
####    print(L[p][0],L[p][1])
####    print(x,y)
##    x=50+i+(L[p][0]*80)
##    y=50+j+(L[p][1]*80)
##    print(x,y)
##    grille1.screen.blit(grille1.block.image, ( y,x))
###grille1.Placer3(j,i,L4_13,"o")
##
##pygame.display.flip()

L1=grille1.generer()                                                        #liste des 3 formes aléatoires
L=L1[0]
ii=0
#L=L4_11
MVT=True                                                                    #mouvement de la souris
pygame.draw.rect(grille1.screen,(0,0,255),(900,100,400,700))                #écran
#grille1.affiche_forme_suiv(L1)
font=pygame.font.Font(None, 24)
nbbloclig=0
nbbloccol=0
Clic=0
while Fini==False:
        if (MVT==True) :
            grille1.screen = pygame.display.set_mode((grille1.WIDTH,grille1.HEIGHT))
            grille1.screen.blit(grille1.damier,(50,50))                                        #affichage de la grille
            #pygame.draw.rect(grille1.screen,(0,0,255),(900,100,400,700))
            pygame.draw.rect(grille1.screen,(0,150,150),(900,50,350,880))
            grille1.affiche_forme_suiv1(L1[0],90,980)                                       #affichage des formes à placer
            grille1.affiche_forme_suiv1(L1[1],400,980)
            grille1.affiche_forme_suiv1(L1[2],700,980)

        for event in pygame.event.get():
                (i,j) = pygame.mouse.get_pos()                                          #récupérer les coordonnees de la souris
                (X,Y)=(entiere((i-50)/80),entiere((j-50)/80))                           #récupérer les coordonnees par rapport à la grille

                if event.type == pygame.QUIT:                                           #cas ou le programme est fini
                        Fini=True
                        print("FINI")
                        pygame.display.update()
                        pygame.quit()
                        sys.exit()


                elif event.type == pygame.MOUSEMOTION and MVT==True:
                    toto=1



##
##                    for p in range (len(L)):
##                            y=j+(L[p][0]*80)
##                            x=i+(L[p][1]*80)
##                            groupBlock.add(Block(80,'carre.gif',x,y))
##
                     #print(X,Y)
                        #print(i,j)

                        #if minx>=0 and miny>0 :
##                        for p in range (len(L)):
##                            y=j+(L[p][0]*80)
##                            x=i+(L[p][1]*80)
##                            #print(x,y)
##
##                            #print(floor(i-50)/80,floor(j-50)/80)
##                            grille1.screen.blit(grille1.block.image, (x,y))
##                            groupBlock.add(Block([x,y]))
##                         for p in range (len(L)):
##                            y=j+(L[p][0]*80)
##                            x=i+(L[p][1]*80)
##                            #print(x,y)
##                            (X,Y)=(entiere((i-50)/80),entiere((j-50)/80))
##                            if X>=0 and Y>0 :
##                                print(X,Y)
##                            #print(floor(i-50)/80,floor(j-50)/80)
##                            grille.screen.blit(grille1.block.image, (x,y))


                        #pygame.display.flip()
                        #grille1.affiche()

                elif  event.type == pygame.MOUSEBUTTONDOWN:                        #activation lors d'un clic
                    #grille1.screen.blit(grille1.damier,(50,50))

##                    grille1.screen.fill((0,0,0))
##                    pygame.display.flip()
##                    grille1.screen.blit(grille1.damier,(50,50))



##                    Clic +=1
##                    if Clic==1:
##                        print("Premier Clic")

                    #print("Forme :",end=" ")
                    for p in range (len(L)):
                        X1=X+L[p][1]
                        Y1=Y+L[p][0]
                        #b=Block(80,'carre.gif',X1*80+50,Y1*80+50)
                        b=Block(80,'carre.gif',X1,Y1)
                        groupForme.add(b)                                            #ajout du bloc au groupe
                        #print(b.rect, end=" , ")
                    #print()

                    if Permis(groupForme,groupBlock)==False :# or X1<0 or Y1<0 or X1>9 or Y1>9:         #cas où la permission n'est pas accordée
                        print("On ne peut placer la forme ici")
                    else :

                        MVT=False
                        (X,Y)=(entiere((i-50)/80),entiere((j-50)/80))
                        print(X,Y,' : ')
                        for p in range (len(L)):
                            y=j+(L[p][0]*80)
                            x=i+(L[p][1]*80)
                            #print(x,y)
                            X1=X+L[p][1]
                            Y1=Y+L[p][0]
                            #print(X1,Y1,'*')

    ##                        if (50+i%80!=0 or 50+j%80!=0):
    ##                           grille1.screen.blit(grille1.block.image,(50+X1*80,50+Y1*80))
    ##                        else:
    ##                            grille1.screen.blit(grille1.block.image,  (50+X1*80, 50+Y1*80))

                            grille1.screen.blit(grille1.block.image,(50+X1*80,50+Y1*80))                         #affichage du bloc a l'endroit ou l'on a clicé
                            print(i,j,X1,Y1)
                            if Y1>=0 and Y1<len(grille1.g) and X1>=0 and X1 <len(grille1.g):
                                grille1.g[Y1][X1]=1#'*'
                            #b=Block(80,'carre.gif',50+X1*80,50+Y1*80)
                            b=Block(80,'carre.gif',X1,Y1)
                            groupBlock.add(b)
                            #print("Ligne ", X1, " Colonne ",Y1)
                        SumCol = numpy.sum(grille1.g,axis=0)
                        SumLig = numpy.sum(grille1.g,axis=1)
                        
                        
##                            text = font.render("Lignes : ",2,(255,0,0))
##                            grille1.screen.blit(text, (300, 900))
##                            text = font.render("Colonnes : ",2,(255,0,0))
##                            grille1.screen.blit(text, (300, 950))
                        c=d=350
                        #print('LIGNES!!!')
                        for a in range(len(SumCol)):                                                    #Calcul des lignes/colonnes remplies
                            if(SumLig[a]==10):
                                print("Ligne ", a, "est pleine")
                                grille1.affiche()
                                for bloc in groupBlock :
                                    #print(bloc.y,bloc.x) # affiche les blocs à détruire
                                    if bloc.y==a  :
                                        groupBlock.remove(bloc) #detruire les blocs de la ligne pleine cad les enlever du groupe des sprites pour qu'ils ne s'affichent pas
                                grille1.screen.blit(grille1.damier,(50,50)) # pour reactualiser l'affichage du damier
                                for bloc in groupBlock : # pour refficher tous les blocs restants qui n'ont pas été effacés
                                    grille1.screen.blit(bloc.image,(50+bloc.x*80,50+bloc.y*80))
 
                                for col in range(10): # remettre le compteur à 0 de la ligne effacee
                                    grille1.g[0][col]=0 
                                        
                                print()
                                grille1.affiche()



                            if(SumCol[a]==10):
                                print("Colonne ", a, "est pleine")
                                #A FAIRE .....



                            #print(i,j,X1,Y1,SumCol[X1],SumLig[Y])

                            #print("Ajout du bloc ",b.rect)

                        #grille1.affiche()
                        ii +=1
                        if ii>2:
                            ii=0
                            L1=grille1.generer()                                                                     #réactualisation des 3 formes lorsque les 3 precédentes ont été placés
                            pygame.draw.rect(grille1.screen,(0,0,0),(900,50,1080,1080))
                            pygame.draw.rect(grille1.screen,(0,150,150),(900,50,350,880))

                        L=L1[ii]
                        #MVT=True
    ##                    pygame.draw.rect(self.screen,(0,0,0),(850,1080)
                        grille1.affiche_forme_suiv1(L1[0],90,980)                                                   #affichage des 3 nouvelles fornes
                        grille1.affiche_forme_suiv1(L1[1],400,980)
                        grille1.affiche_forme_suiv1(L1[2],700,980)
                        #pygame.draw.rect(grille1.screen,(0,0,0),(950,50,200,1080))

                    for blocF in groupForme :
                         groupForme.remove(blocF)
                    #groupForme[:] = []
                elif  event.type == pygame.MOUSEBUTTONUP:
                    (i,j) = pygame.mouse.get_pos()
                pygame.display.flip()
                #if event.type == pygame.MOUSEBUTTONDOWN:



pygame.display.flip()
