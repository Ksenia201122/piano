import cartinci
import nastroyky
import pygame as pg

class Menu:
    def __init__(self,igra):
        self.igra=igra
        self.cvet1=[255,255,255]
        self.cvet2=[255,0,0]
        self.cvet3=[255,0,0]
        self.nomtecpes=1
    def otrisovca(self):
        self.igra.okno.blit(cartinci.fonmenu,[0,0])
        self.igra.shrift.render_to(self.igra.okno,[70,150],"В лесу родилась елочка",self.cvet1)
        self.igra.shrift.render_to(self.igra.okno,[140,250],"Березка",self.cvet2)
        self.igra.shrift.render_to(self.igra.okno,[150,350],"Утро",self.cvet3)
    def sobitia(self):
        sobitia=pg.event.get()
        for sobitie in sobitia:
            if sobitie.type==pg.QUIT:
                self.igra.m=3
            if sobitie.type==pg.KEYDOWN:
                if sobitie.key==pg.K_DOWN:
                    if self.nomtecpes==1:
                        self.cvet1=[255,0,0]
                        self.cvet2=[255,255,255]
                        self.nomtecpes=2
                    elif self.nomtecpes==2:
                        self.cvet2=[255,0,0]
                        self.cvet3=[255,255,255]
                        self.nomtecpes=3
                    elif self.nomtecpes==3:
                        self.cvet3=[255,0,0]
                        self.cvet1=[255,255,255]
                        self.nomtecpes=1
                if sobitie.key==pg.K_UP:
                    if self.nomtecpes==1:
                        self.cvet1=[255,0,0]
                        self.cvet3=[255,255,255]
                        self.nomtecpes=3
                    elif self.nomtecpes==2:
                        self.cvet2=[255,0,0]
                        self.cvet1=[255,255,255]
                        self.nomtecpes=1
                    elif self.nomtecpes==3:
                        self.cvet3=[255,0,0]
                        self.cvet2=[255,255,255]
                        self.nomtecpes=2
                if sobitie.key==pg.K_RETURN:
                    self.igra.sostoanie="igra"
                    self.igra.colnajatnot=0
                    self.igra.proigr=0
                    self.igra.nomernot=0
                    self.igra.noti=[]
                    if self.nomtecpes==1:
                        self.igra.spisocnot=nastroyky.CHRISTMAS_TREE_NOTES
                        self.igra.spisocprodl=nastroyky.CHRISTMAS_TREE_DURATION
                        self.igra.colnenajatnot=len(self.igra.spisocnot)
                    elif self.nomtecpes==2:
                        self.igra.spisocnot=nastroyky.BIRCH_NOTES
                        self.igra.spisocprodl=nastroyky.BIRCH_DURATION
                        self.igra.colnenajatnot=len(self.igra.spisocnot)
                    elif self.nomtecpes==3:
                        self.igra.spisocnot=nastroyky.MORNING_NOTES
                        self.igra.spisocprodl=nastroyky.MORNING_DURATION
                        self.igra.colnenajatnot=len(self.igra.spisocnot)

    