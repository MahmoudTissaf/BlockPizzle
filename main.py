from random import *
from classF import *
import numpy
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages/')
import pygame

from math import *
def entiere(n):
    if floor(n%1)>= 0.5 :
        return(floor(n)+1)
        #return(int(n)+1)
    else:
        return(floor(n))
        #return(int(n))
    
 
def Permis(groupForme,groupBlock):
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

L1=grille1.generer() 
L=L1[0]
ii=0
#L=L4_11
MVT=True
pygame.draw.rect(grille1.screen,(0,0,255),(900,100,400,700))
#grille1.affiche_forme_suiv(L1)
font=pygame.font.Font(None, 24)
nbbloclig=0
nbbloccol=0
Clic=0
while Fini==False:
        if (MVT==True) :
            grille1.screen = pygame.display.set_mode((grille1.WIDTH,grille1.HEIGHT))
            grille1.screen.blit(grille1.damier,(50,50))
            #pygame.draw.rect(grille1.screen,(0,0,255),(900,100,400,700))
            pygame.draw.rect(grille1.screen,(0,150,150),(900,50,350,880))
            grille1.affiche_forme_suiv1(L1[0],90,980)
            grille1.affiche_forme_suiv1(L1[1],400,980)
            grille1.affiche_forme_suiv1(L1[2],700,980)

            text = font.render("ligne : "+str(nbbloclig),2,(255,0,0))
            grille1.screen.blit(text, (300, 900))

            text = font.render("colonne : "+str(nbbloccol),2,(255,0,0))
            grille1.screen.blit(text, (300, 950))
        for event in pygame.event.get():
                (i,j) = pygame.mouse.get_pos()
                (X,Y)=(entiere((i-50)/80),entiere((j-50)/80))
                
                if event.type == pygame.QUIT:
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
                        
                elif  event.type == pygame.MOUSEBUTTONDOWN:
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
                        b=Block(80,'carre.gif',X1*80+50,Y1*80+50)
                        groupForme.add(b)
                        #print(b.rect, end=" , ")       
                    #print()

                    if Permis(groupForme,groupBlock)==False :# or X1<0 or Y1<0 or X1>9 or Y1>9:
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
                            
                            grille1.screen.blit(grille1.block.image,(50+X1*80,50+Y1*80))
                            #print(i,j,X1,Y1)
                            grille1.g[Y1][X1]=1#'*'
                            b=Block(80,'carre.gif',50+X1*80,50+Y1*80)
                            groupBlock.add(b)
                            SumCol = numpy.sum(grille1.g,axis=0)
                            SumLig = numpy.sum(grille1.g,axis=1)
                            for a in range(len(SumCol)):
                                if(SumCol[a]==10 or SumLig[a]==10):
                                    
                                    
                                    text = font.render("ligne : "+str(nbbloclig),2,(255,0,0))
                                    grille1.screen.blit(text, (300, 900))

                                    text = font.render("colonne : "+str(nbbloccol),2,(255,0,0))
                                    grille1.screen.blit(text, (300, 950))
                                    
                                    
                            
                            #print(i,j,X1,Y1,SumCol[X1],SumLig[Y])
                                
                            #print("Ajout du bloc ",b.rect)
                            
                        #grille1.affiche()
                        ii +=1
                        if ii>2:
                            ii=0
                            L1=grille1.generer()
                            pygame.draw.rect(grille1.screen,(0,0,0),(900,50,1080,1080))
                            pygame.draw.rect(grille1.screen,(0,150,150),(900,50,350,880))

                        L=L1[ii]
                        #MVT=True
    ##                    pygame.draw.rect(self.screen,(0,0,0),(850,1080)
                        grille1.affiche_forme_suiv1(L1[0],90,980)
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

