from cProfile import run
from pdb import Restart
import pygame
from pygame.locals import *
from random import *
from time import *
from MainConstructor import *

def checkwin(a,b,c,d,e,f,g,h,i,screen):
    #Player 1 Gagnant


        #Horizontal
        if(a==1 and b==1 and c==1):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 1 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(d==1 and e==1 and f==1):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 1 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(g==1 and h==1 and i==1):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 1 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        #Vertical
        if(a==1 and d==1 and g==1):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 1 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(b==1 and e==1 and h==1):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 1 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(c==1 and f==1 and i==1):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 1 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        #Diagonal
        if(a==1 and e==1 and i==1):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 1 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(c==1 and e==1 and g==1):
           screen.fill((5,5,5))
           cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
           cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
           Texte('Player 1 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
           pygame.display.flip()
           return 1

        #Player 2 Gagant
        #Horizontal
        if(a==2 and b==2 and c==2):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 2 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(d==2 and e==2 and f==2):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 2 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(g==2 and h==2 and i==2):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 2 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        #Vertical
        if(a==2 and d==2 and g==2):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 2 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(b==2 and e==2 and h==2):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 2 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(c==2 and f==2 and i==2):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 2 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        #Diagonal
        if(a==2 and e==2 and i==2):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 2 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        if(c==2 and e==2 and g==2):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('Player 2 Won !', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
        #Match null
        if(a!=0 and b!=0 and c!=0 and d!=0 and e!=0 and f!=0 and g!=0 and h!=0 and i!=0):
            screen.fill((5,5,5))
            cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
            cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
            Texte('match nul', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)
            pygame.display.flip()
            return 1
