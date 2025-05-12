import time
import nota
import cartinci
import pygame.freetype
import menu

import pygame as pg
import random
import nastroyky

pg.init()
pg.mixer.init()

# константы
# здесь записан порядок нот и их длительность для каждой песни

class Igra:
    def __init__(self):
        self.sostoanie="menu"
        self.okno=pg.display.set_mode(nastroyky.SIZE)
        self.menu=menu.Menu(self)
        self.m=2
        self.spisocnot=nastroyky.CHRISTMAS_TREE_NOTES
        self.spisocprodl=nastroyky.CHRISTMAS_TREE_DURATION
        self.colnenajatnot=len(self.spisocnot)
        self.sobitienot=pg.USEREVENT
        self.colnajatnot=0
        self.proigr=0
        self.shrift=pg.freetype.Font("Breeze Normal.Ttf",30)
        pg.time.set_timer(self.sobitienot,1000)
        self.noti=[]
        self.obhasov=pg.time.Clock()
        self.nomernot=0
    def otrisovca(self):
        self.okno.fill([255,255,255])
        if self.noti != []:
           poslnot=self.noti[-1]
        if self.colnajatnot==len(self.spisocnot) and poslnot.pramougol.y>500:
           self.shrift.render_to(self.okno,[100,400],"Вы выиграли")
        if self.proigr==1:
            self.shrift.render_to(self.okno,[100,400],"Вы проиграли")
        if self.colnenajatnot>self.colnajatnot:
            self.shrift.render_to(self.okno,[100,100],"Кол-во оставшихся нот:"+str(self.colnenajatnot-self.colnajatnot))
        colst=nastroyky.COLSTOLB
        x=nastroyky.SHIRINSTOLB
        if self.proigr==0:
            for nota in self.noti:
                nota.otrisovca(self.okno)
        while colst>0:
            pg.draw.line(self.okno,[0,0,0],[x,0],[x,600],4)
            x=x+nastroyky.SHIRINSTOLB
            colst=colst-1
            pg.draw.line(self.okno,[255,0,0],[0,500],[400,500],4)
    def logica(self):
        for nota in self.noti:
            if self.proigr==0:
               nota.dvijenie() 
            if nota.pramougol.y>500 and nota.najata==0:
                self.proigr=1
    def sobitie(self):
        sobitia=pg.event.get()
        for sobitie in sobitia:
            if sobitie.type==pg.QUIT:
                self.m=1
            if sobitie.type==self.sobitienot and self.nomernot<len(self.spisocnot) and self.proigr==0:
                n=nota.Not(self.spisocprodl[self.nomernot],self.spisocnot[self.nomernot])
                self.nomernot=self.nomernot+1
                self.noti.append(n)
            if sobitie.type==pg.KEYDOWN:
                if sobitie.key==pg.K_6:
                    self.sostoanie="menu"
            if sobitie.type==pg.MOUSEBUTTONDOWN and self.proigr==0:
                for n in self.noti:
                    if n.pramougol.collidepoint(sobitie.pos):
                        index=self.noti.index(n)
                        if self.colnajatnot==index:
                            self.colnajatnot=self.colnajatnot+1
                            n.clic()
                        else:
                            self.proigr=1
        


 
    def zapusc(self):
        while self.m==2:
            if self.sostoanie=="igra":
                self.otrisovca()
                self.logica()
                self.sobitie()
            else:
                self.menu.otrisovca()
                self.menu.sobitia()
            pg.display.update()
            self.obhasov.tick(60)

igra=Igra()
igra.zapusc()


