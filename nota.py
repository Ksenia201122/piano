import pygame as pg
import cartinci
import random


class Not:
    def __init__(self,dliteln,nazvanie):
        self.dliteln=dliteln
        self.zvuk=pg.mixer.Sound("Sounds/"+nazvanie+".ogg")
        self.zvuk.set_volume(0.3)
        self.najata=0
        x=random.randint(0,3)
        if self.dliteln==1:
           self.cartina=cartinci.nenajatcnop
        else:
            self.cartina=cartinci.dlcnopnenaj
        self.pramougol=pg.rect.Rect([x*100,-100],self.cartina.get_size())
        self.nazvanie=nazvanie
    def otrisovca(self,okno):
        okno.blit(self.cartina,self.pramougol)
    def dvijenie(self):
        self.pramougol.y=self.pramougol.y+3
    def clic(self):
        self.najata=1
        canal=pg.mixer.find_channel()
        if canal==None:
            pg.mixer.stop()
        self.zvuk.play()
        if self.dliteln==1:
            self.cartina=cartinci.najatchop
        else:
            self.cartina=cartinci.dlcnopnaj
            
        
        

        
