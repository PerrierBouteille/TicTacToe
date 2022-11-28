#=== Import des modules
from cProfile import run
from fileinput import filename
import pygame
from pygame.locals import *
from random import *
#from yaml import *
from operator import itemgetter
from time import *
from MainConstructor import *
from Win import *


#

Prefix = "TicTacToe"

#

class TextProgress:
    def __init__(self, font, message, color, bgcolor):
        self.font = font
        self.message = message
        self.color = color
        self.bgcolor = bgcolor
        self.offcolor = [c^40 for c in color]
        self.notcolor = [c^0xFF for c in color]
        self.text = font.render(message, 0, (255,0,0), self.notcolor)
        self.text.set_colorkey(1)
        self.outline = self.textHollow(font, message, color)
        self.bar = pygame.Surface(self.text.get_size())
        self.bar.fill(self.offcolor)
        width, height = self.text.get_size()
        stripe = Rect(0, height/2, width, height/4)
        self.bar.fill(color, stripe)
        self.ratio = width / 100.0

    def textHollow(self, font, message, fontcolor):
        base = font.render(message, 0, fontcolor, self.notcolor)
        size = base.get_width() + 2, base.get_height() + 2
        img = pygame.Surface(size, 16)
        img.fill(self.notcolor)
        base.set_colorkey(0)
        img.blit(base, (0, 0))
        img.blit(base, (2, 0))
        img.blit(base, (0, 2))
        img.blit(base, (2, 2))
        base.set_colorkey(0)
        base.set_palette_at(1, self.notcolor)
        img.blit(base, (1, 1))
        img.set_colorkey(self.notcolor)
        return img

    def render(self, percent=50):
        surf = pygame.Surface(self.text.get_size())
        if percent < 100:
            surf.fill(self.bgcolor)
            surf.blit(self.bar, (0,0), (0, 0, percent*self.ratio, 100))
        else:
            surf.fill(self.color)
            global finished
            finished = 1
            global Menu
            Menu = 1

        surf.blit(self.text, (0,0))
        #surf.blit(self.outline, (-1,-1))
        surf.set_colorkey(self.notcolor)
        return surf

entry_info = '/////////////////////////'
ch = 0

if __name__ == '__main__':
    import random
    pygame.init()
    pygame.display.set_caption(Prefix)
    screen = pygame.display.set_mode((500, 600))

    font = pygame.font.Font(None, 60)
    font2 = pygame.font.SysFont('Comic Sans MS,Arial', 24)
    white = 0, 225, 0
    renderer = TextProgress(font, entry_info, white, (40, 40, 40))
    text = renderer.render(0)

    screen.blit(text, (115, 330))
    bar1 = font.render(' ____________ ', True, (255,255,255))
    bar2 = font.render('|____________|', True, (255,255,255))
    author = font2.render('Chargement en cours..', True, (255,255,255))
    screen.blit(author, (130,280))
    screen.blit(bar1, (105,290))
    screen.blit(bar2, (105,330))

    pygame.display.flip()

    progress = 1

    finished = 0
    while not finished:
        dly = randint(160,640)
        pygame.time.delay(120)
        ch += 1
        for event in pygame.event.get():
            if event.type in (QUIT,KEYDOWN,MOUSEBUTTONDOWN):
                finished = 1

        progress = (progress + random.randint(0,3)) % 120
        text = renderer.render(progress)
        screen.blit(text, (115, 330))
        pygame.display.flip()

#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

Menu = 1
Player1 = 0
Player2 = 0
Playing = 0
PlayingBis = 1
WRestart = 0

a,b,c,d,e,f,g,h,i = 0,0,0,0,0,0,0,0,0

screen = pygame.display.set_mode((500,600))

#▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬

while True:

    while Menu:
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
               pygame.quit()
               exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 50 <= mouse[0] <= 450 and 350 <= mouse[1] <= 450:
                    Menu = 0
                    Playing = 1
                    Player1 = 1
        screen.fill((5,5,5))
        cadre = Draw_rect().gen((0, 0, 0),((50,350),(400,100)),screen)
        cadre = Draw_rect().gen((0, 25, 0),((55,355),(395,95)),screen)
        textMenu = Texte("TicTacToe", 50, (15,150,15), (cadre.centerx,75), 'ressource/04B_30__.TTF').affiche(screen)
        textMenu = Texte("TicTacToe", 53, (10,200,10), (cadre.centerx,75), 'ressource/04B_30__.TTF').affiche(screen)
        textMenu = Texte('Start', 75, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/04B_30__.TTF').affiche(screen)
        pygame.display.flip()
    while Playing:
        if(PlayingBis == 1):
            screen.fill((5,5,5))

            Draw_rect().gen((0, 0, 0),((55,300),(390,5)),screen)
            Draw_rect().gen((0, 0, 0),((55,430),(390,5)),screen)
            Draw_rect().gen((0, 0, 0),((180,170),(5,390)),screen)
            Draw_rect().gen((0, 0, 0),((310,170),(5,390)),screen)
            PlayingBis = 0

        if(a != 0 and b != 0 and c != 0 and d != 0 and e != 0 and f != 0 and g != 0 and h != 0 and i != 0):
            WRestart = 1
            Playing = 0

        while Player1:
            if(a == 0 or b == 0 or c == 0 or d == 0 or e == 0 or f == 0 or g == 0 or h == 0 or i == 0):
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        print(str(mouse[0]) + " | " + str(mouse[1]))
                        if 55 <= mouse[0] <= 180 and 170 <= mouse[1] <= 300:
                            if(a==0):
                                screen.blit((Image('ressource/player1.png')),(50,170))
                                Player1 = 0
                                Player2 = 1
                                a = 1
                        if 185 <= mouse[0] <= 310 and 170 <= mouse[1] <= 300:
                            if(b==0):
                                screen.blit((Image('ressource/player1.png')),(185,170))
                                Player1 = 0
                                Player2 = 1
                                b = 1
                        if 315 <= mouse[0] <= 445 and 170 <= mouse[1] <= 300:
                            if(c==0):
                                screen.blit((Image('ressource/player1.png')),(315,170))
                                Player1 = 0
                                Player2 = 1
                                c = 1
                        if 55 <= mouse[0] <= 180 and 300 <= mouse[1] <= 425:
                            if(d==0):
                                screen.blit((Image('ressource/player1.png')),(50,305))
                                Player1 = 0
                                Player2 = 1
                                d = 1
                        if 185 <= mouse[0] <= 310 and 300 <= mouse[1] <= 425:
                            if(e==0):
                                screen.blit((Image('ressource/player1.png')),(185,305))
                                Player1 = 0
                                Player2 = 1
                                e = 1
                        if 315 <= mouse[0] <= 445 and 300 <= mouse[1] <= 425:
                            if(f==0):
                                screen.blit((Image('ressource/player1.png')),(315,305))
                                Player1 = 0
                                Player2 = 1
                                f = 1
                        if 55 <= mouse[0] <= 180 and 425 <= mouse[1] <= 550:
                            if(g==0):
                                screen.blit((Image('ressource/player1.png')),(50,435))
                                Player1 = 0
                                Player2 = 1
                                g = 1
                        if 185 <= mouse[0] <= 310 and 425 <= mouse[1] <= 550:
                            if(h==0):
                                screen.blit((Image('ressource/player1.png')),(185,435))
                                Player1 = 0
                                Player2 = 1
                                h = 1
                        if 315 <= mouse[0] <= 445 and 425 <= mouse[1] <= 550:
                            if(i==0):
                                screen.blit((Image('ressource/player1.png')),(315,435))
                                Player1 = 0
                                Player2 = 1
                                i = 1

                    cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
                    cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
                    textMenu = Texte('PLAYER 1', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/04B_30__.TTF').affiche(screen)

                pygame.display.flip()

            pygame.display.flip()

        checkwin(a,b,c,d,e,f,g,h,i,screen)
        if(checkwin(a,b,c,d,e,f,g,h,i,screen) == 1):
            Player1,Player2,WRestart,Playing = 0,0,1,0

        if(a != 0 and b != 0 and c != 0 and d != 0 and e != 0 and f != 0 and g != 0 and h != 0 and i != 0):
            WRestart = 1
            Playing = 0
            Player1,Player2 = 0,0

        while Player2:
            if(a == 0 or b == 0 or c == 0 or d == 0 or e == 0 or f == 0 or g == 0 or h == 0 or i == 0):
                for event in pygame.event.get():
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse = pygame.mouse.get_pos()
                        print(str(mouse[0]) + " | " + str(mouse[1]))
                        if 55 <= mouse[0] <= 180 and 170 <= mouse[1] <= 300:
                            if(a==0):
                                screen.blit((Image('ressource/player2.png')),(50,170))
                                Player1 = 1
                                Player2 = 0
                                a = 2
                        if 185 <= mouse[0] <= 310 and 170 <= mouse[1] <= 300:
                            if(b==0):
                                screen.blit((Image('ressource/player2.png')),(185,170))
                                Player1 = 1
                                Player2 = 0
                                b = 2
                        if 315 <= mouse[0] <= 445 and 170 <= mouse[1] <= 300:
                            if(c==0):
                                screen.blit((Image('ressource/player2.png')),(315,170))
                                Player1 = 1
                                Player2 = 0
                                c = 2
                        if 55 <= mouse[0] <= 180 and 300 <= mouse[1] <= 425:
                            if(d==0):
                                screen.blit((Image('ressource/player2.png')),(50,305))
                                Player1 = 1
                                Player2 = 0
                                d = 2
                        if 185 <= mouse[0] <= 310 and 300 <= mouse[1] <= 425:
                            if(e==0):
                                screen.blit((Image('ressource/player2.png')),(185,305))
                                Player1 = 1
                                Player2 = 0
                                e = 2
                        if 315 <= mouse[0] <= 445 and 300 <= mouse[1] <= 425:
                            if(f==0):
                                screen.blit((Image('ressource/player2.png')),(315,305))
                                Player1 = 1
                                Player2 = 0
                                f = 2
                        if 55 <= mouse[0] <= 180 and 425 <= mouse[1] <= 550:
                            if(g==0):
                                screen.blit((Image('ressource/player2.png')),(50,435))
                                Player1 = 1
                                Player2 = 0
                                g = 2
                        if 185 <= mouse[0] <= 310 and 425 <= mouse[1] <= 550:
                            if(h==0):
                                screen.blit((Image('ressource/player2.png')),(185,435))
                                Player1 = 1
                                Player2 = 0
                                h = 2
                        if 315 <= mouse[0] <= 445 and 425 <= mouse[1] <= 550:
                            if(i==0):
                                screen.blit((Image('ressource/player2.png')),(315,435))
                                Player1 = 1
                                Player2 = 0
                                i = 2

                    cadre = Draw_rect().gen((0, 0, 0),((50,50),(400,100)),screen)
                    cadre = Draw_rect().gen((0, 25, 0),((55,55),(395,95)),screen)
                    textMenu = Texte('PLAYER 2', 50, (10,200,10), (cadre.centerx,cadre.top + 45), 'ressource/04B_30__.TTF').affiche(screen)
                    pygame.display.flip()
            pygame.display.flip()


        checkwin(a,b,c,d,e,f,g,h,i,screen)
        if(checkwin(a,b,c,d,e,f,g,h,i,screen) == 1):
            Player1,Player2,WRestart,Playing = 0,0,1,0

    while WRestart:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                a,b,c,d,e,f,g,h,i = 0,0,0,0,0,0,0,0,0
                WRestart,Playing,PlayingBis=0,1,1
                Player1,Player2=1,0
                pygame.display.flip()
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                pygame.quit()
                exit()
        cadre = Draw_rect().gen((150, 105, 0),((45,295),(405,105)),screen)
        cadre = Draw_rect().gen((225, 155, 0),((50,300),(395,95)),screen)
        Texte('RESTART', 75, (10,10,10), (cadre.centerx,cadre.top + 45), 'ressource/Win.ttf').affiche(screen)

        pygame.display.flip()
