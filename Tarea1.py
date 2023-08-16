from pyglet.window import Window 
from pyglet.app import run
from pyglet import shapes
from pyglet import clock
from pyglet.graphics import Batch
import numpy as np
import random as rdm

WIDTH= 1300
HEIGHT = 780
WINDOW_TITTLE = "Tarea 1 Modelación"
FULL_SCREEN = False
Ventana = Window(WIDTH, HEIGHT, WINDOW_TITTLE, resizable=False)

Ventana.set_fullscreen(FULL_SCREEN)
batch = Batch()
batchS = Batch()

#Parametros utiles
W = Ventana.width//2
H = Ventana.height//2

#Colores
r=(224,63,63)
o=(250,125,39)
a=(206,253,80) #amarillo
b=(175,29,0) #burdeo
w=(255,255,255)

#Escala de verdes para la ventana
gdd=(85, 156, 142)
gd=(93, 181, 164)
g=(92, 214, 190)
gw=(0, 255, 204)

class ship1:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s

        #Cuerpo Superior
        self.g = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*1.5, W+self.x+self.s*0,
                                       H+self.y+self.s*3.5, W+self.x+self.s*-1, H+self.y+self.s*1.5, color=r, batch=batch)
        self.h = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*1.5, W+self.x+self.s*-1,
                                       H+self.y+self.s*1.5, W+self.x+self.s*1, H+self.y+self.s*1, color=r, batch=batch)
        self.i = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*1, W+self.x+self.s*-1,
                                       H+self.y+self.s*1.5, W+self.x+self.s*-1, H+self.y+self.s*1, color=r, batch=batch)
        self.j = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*1, W+self.x+self.s*-1,
                                       H+self.y+self.s*1, W+self.x+self.s*0, H+self.y+self.s*-1, color=r, batch=batch)
        
        #Ala derecha
        self.k = shapes.Triangle(W+self.x+self.s*2, H+self.y+self.s*-1, W+self.x+self.s*1,
                                       H+self.y+self.s*1, W+self.x+self.s*0.375, H+self.y+self.s*-0.25, color=o, batch=batch)
        self.l = shapes.Triangle(W+self.x+self.s*2, H+self.y+self.s*-1, W+self.x+self.s*0.375,
                                       H+self.y+self.s*-0.25, W+self.x+self.s*1, H+self.y+self.s*-1.5, color=o, batch=batch)
        self.o = shapes.Triangle(W+self.x+self.s*2, H+self.y+self.s*-1, W+self.x+self.s*1,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*3, H+self.y+self.s*-2, color=o, batch=batch)
        self.p = shapes.Triangle(W+self.x+self.s*3, H+self.y+self.s*-2, W+self.x+self.s*1,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*3, H+self.y+self.s*-2.5, color=o, batch=batch)
        
        #Centro   
        self.m = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*-1.5, W+self.x+self.s*0.375,
                                       H+self.y+self.s*-0.25, W+self.x+self.s*0, H+self.y+self.s*-1, color=b, batch=batch)
        self.n = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*-1.5, W+self.x+self.s*0,
                                       H+self.y+self.s*-1, W+self.x+self.s*0, H+self.y+self.s*-2, color=b, batch=batch)
        self.z = shapes.Triangle(W+self.x+self.s*0, H+self.y+self.s*-2, W+self.x+self.s*0,
                                       H+self.y+self.s*-1, W+self.x+self.s*-1, H+self.y+self.s*-1.5, color=b, batch=batch)
        self.w = shapes.Triangle(W+self.x+self.s*0, H+self.y+self.s*-1, W+self.x+self.s*-0.375,
                                       H+self.y+self.s*-0.25, W+self.x+self.s*-1, H+self.y+self.s*-1.5, color=b, batch=batch)
        
        #Ala izquierda  
        self.u = shapes.Triangle(W+self.x+self.s*-1, H+self.y+self.s*1, W+self.x+self.s*-2,
                                       H+self.y+self.s*-1, W+self.x+self.s*-0.375, H+self.y+self.s*-0.25, color=o, batch=batch)
        self.v = shapes.Triangle(W+self.x+self.s*-0.375, H+self.y+self.s*-0.25, W+self.x+self.s*-2,
                                       H+self.y+self.s*-1, W+self.x+self.s*-1, H+self.y+self.s*-1.5, color=o, batch=batch)
        self.aa = shapes.Triangle(W+self.x+self.s*-1, H+self.y+self.s*-1.5, W+self.x+self.s*-2,
                                       H+self.y+self.s*-1, W+self.x+self.s*-3, H+self.y+self.s*-2, color=o, batch=batch)
        self.ab = shapes.Triangle(W+self.x+self.s*-1, H+self.y+self.s*-1.5, W+self.x+self.s*-3,
                                       H+self.y+self.s*-2, W+self.x+self.s*-3, H+self.y+self.s*-2.5, color=o, batch=batch)

        #Ventana
        self.a = shapes.Triangle(W+self.x+self.s*0.5, H+self.y+self.s*1, W+self.x+self.s*0.5,
                                       H+self.y+self.s*1.5, W+self.x+self.s*0, H+self.y+self.s*1.25, color=g, batch=batch)
        self.b = shapes.Triangle(W+self.x+self.s*0.5, H+self.y+self.s*1.5, W+self.x+self.s*0,
                                       H+self.y+self.s*2.5, W+self.x+self.s*0, H+self.y+self.s*1.25, color=gw, batch=batch)
        self.c = shapes.Triangle(W+self.x+self.s*0, H+self.y+self.s*1.25, W+self.x+self.s*0,
                                       H+self.y+self.s*2.5, W+self.x+self.s*-0.5, H+self.y+self.s*1.5, color=g, batch=batch)
        self.d = shapes.Triangle(W+self.x+self.s*0, H+self.y+self.s*1.25, W+self.x+self.s*-0.5,
                                       H+self.y+self.s*1.5, W+self.x+self.s*-0.5, H+self.y+self.s*1, color=gd, batch=batch)
        self.e = shapes.Triangle(W+self.x+self.s*0, H+self.y+self.s*1.25, W+self.x+self.s*-0.5,
                                       H+self.y+self.s*1, W+self.x+self.s*0, H+self.y+self.s*0, color=gdd, batch=batch)
        self.f = shapes.Triangle(W+self.x+self.s*0.5, H+self.y+self.s*1, W+self.x+self.s*0,
                                       H+self.y+self.s*1.25, W+self.x+self.s*0, H+self.y+self.s*0, color=gd, batch=batch)
        
        #Llamas
        self.q = shapes.Triangle(W+self.x+self.s*2, H+self.y+self.s*-2, W+self.x+self.s*1.5,
                                       H+self.y+self.s*-1.75, W+self.x+self.s*1.5, H+self.y+self.s*-2.5, color=a, batch=batch)
        self.r = shapes.Triangle(W+self.x+self.s*2, H+self.y+self.s*-2, W+self.x+self.s*1.5,
                                       H+self.y+self.s*-2.5, W+self.x+self.s*2, H+self.y+self.s*-2.5, color=a, batch=batch)
        self.t = shapes.Triangle(W+self.x+self.s*2, H+self.y+self.s*-2.5, W+self.x+self.s*1.5,
                                       H+self.y+self.s*-2.5, W+self.x+self.s*1.75, H+self.y+self.s*-2.75, color=a, batch=batch)
        
        self.ac = shapes.Triangle(W+self.x+self.s*-2, H+self.y+self.s*-2, W+self.x+self.s*-1.5,
                                       H+self.y+self.s*-2.5, W+self.x+self.s*-1.5, H+self.y+self.s*-1.75, color=a, batch=batch)
        self.ad = shapes.Triangle(W+self.x+self.s*-2, H+self.y+self.s*-2, W+self.x+self.s*-1.5,
                                       H+self.y+self.s*-2.5, W+self.x+self.s*-2, H+self.y+self.s*-2.5, color=a, batch=batch)
        self.ae = shapes.Triangle(W+self.x+self.s*-2, H+self.y+self.s*-2.5, W+self.x+self.s*-1.75,
                                       H+self.y+self.s*-2.75, W+self.x+self.s*-1.5, H+self.y+self.s*-2.5, color=a, batch=batch)

class ship2:
    def __init__(self,x,y,s):
        self.x = x
        self.y = y
        self.s = s

        #Cuerpo Superior
        self.g = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*1, W+self.x+self.s*0,
                                       H+self.y+self.s*3, W+self.x+self.s*-1, H+self.y+self.s*1, color=r, batch=batch)
        self.h = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*1, W+self.x+self.s*-1,
                                       H+self.y+self.s*1, W+self.x+self.s*1, H+self.y+self.s*0.5, color=r, batch=batch)
        self.i = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*0.5, W+self.x+self.s*-1,
                                       H+self.y+self.s*1, W+self.x+self.s*-1, H+self.y+self.s*0.5, color=r, batch=batch)
        self.j = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*0.5, W+self.x+self.s*-1,
                                       H+self.y+self.s*0.5, W+self.x+self.s*0, H+self.y+self.s*-1.5, color=r, batch=batch)

        #Ventana
        self.a = shapes.Triangle(W+self.x+self.s*0.5, H+self.y+self.s*0.5, W+self.x+self.s*0.5,
                                       H+self.y+self.s*1, W+self.x+self.s*0, H+self.y+self.s*0.75, color=g, batch=batch)
        self.b = shapes.Triangle(W+self.x+self.s*0.5, H+self.y+self.s*1, W+self.x+self.s*0,
                                       H+self.y+self.s*2, W+self.x+self.s*0, H+self.y+self.s*0.75, color=gw, batch=batch)
        self.c = shapes.Triangle(W+self.x+self.s*0, H+self.y+self.s*0.75, W+self.x+self.s*0,
                                       H+self.y+self.s*2, W+self.x+self.s*-0.5, H+self.y+self.s*1, color=g, batch=batch)
        self.d = shapes.Triangle(W+self.x+self.s*0, H+self.y+self.s*0.75, W+self.x+self.s*-0.5,
                                       H+self.y+self.s*1, W+self.x+self.s*-0.5, H+self.y+self.s*0.5, color=gd, batch=batch)
        self.e = shapes.Triangle(W+self.x+self.s*0, H+self.y+self.s*0.75, W+self.x+self.s*-0.5,
                                       H+self.y+self.s*0.5, W+self.x+self.s*0, H+self.y+self.s*-0.5, color=gdd, batch=batch)
        self.f = shapes.Triangle(W+self.x+self.s*0.5, H+self.y+self.s*0.5, W+self.x+self.s*0,
                                       H+self.y+self.s*0.75, W+self.x+self.s*0, H+self.y+self.s*-0.5, color=gd, batch=batch)
        
        #Ala derecha
        self.k = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*0.5, W+self.x+self.s*0.625,
                                       H+self.y+self.s*-0.25, W+self.x+self.s*3, H+self.y+self.s*-0.5, color=o, batch=batch)
        self.l = shapes.Triangle(W+self.x+self.s*0.625, H+self.y+self.s*-0.25, W+self.x+self.s*1,
                                       H+self.y+self.s*-1, W+self.x+self.s*3, H+self.y+self.s*-0.5, color=o, batch=batch)
        self.m = shapes.Triangle(W+self.x+self.s*3, H+self.y+self.s*-0.5, W+self.x+self.s*1,
                                       H+self.y+self.s*-1, W+self.x+self.s*3, H+self.y+self.s*-1.5, color=o, batch=batch)
        self.n = shapes.Triangle(W+self.x+self.s*3, H+self.y+self.s*-0.5, W+self.x+self.s*3,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*3.5, H+self.y+self.s*-1.5, color=o, batch=batch)
        self.o = shapes.Triangle(W+self.x+self.s*3.5, H+self.y+self.s*-1.5, W+self.x+self.s*3,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*3.5, H+self.y+self.s*-2.5, color=o, batch=batch)
        
        #Cuerpo
        self.p = shapes.Triangle(W+self.x+self.s*0.625, H+self.y+self.s*-0.25, W+self.x+self.s*0,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*1, H+self.y+self.s*-1, color=b, batch=batch)
        self.q = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*-1, W+self.x+self.s*0,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*0.5, H+self.y+self.s*-1.5, color=b, batch=batch)
        self.z = shapes.Triangle(W+self.x+self.s*-0.5, H+self.y+self.s*-1.5, W+self.x+self.s*0.5,
                                       H+self.y+self.s*-2, W+self.x+self.s*0.5, H+self.y+self.s*-1.5, color=b, batch=batch)
        self.aa = shapes.Triangle(W+self.x+self.s*-0.5, H+self.y+self.s*-1.5, W+self.x+self.s*-0.5,
                                       H+self.y+self.s*-2, W+self.x+self.s*0.5, H+self.y+self.s*-2, color=b, batch=batch)
        self.ab = shapes.Triangle(W+self.x+self.s*-0.5, H+self.y+self.s*-2, W+self.x+self.s*0,
                                       H+self.y+self.s*-3, W+self.x+self.s*0.5, H+self.y+self.s*-2, color=b, batch=batch)
        self.ad = shapes.Triangle(W+self.x+self.s*-0.5, H+self.y+self.s*-1.5, W+self.x+self.s*0,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*-1, H+self.y+self.s*-1, color=b, batch=batch)
        self.ae = shapes.Triangle(W+self.x+self.s*-1, H+self.y+self.s*-1, W+self.x+self.s*0,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*-0.625, H+self.y+self.s*-0.25, color=b, batch=batch)
        
        #Ala Izquierda
        self.af = shapes.Triangle(W+self.x+self.s*-1, H+self.y+self.s*0.5, W+self.x+self.s*-3,
                                       H+self.y+self.s*-0.5, W+self.x+self.s*-0.625, H+self.y+self.s*-0.25, color=o, batch=batch)
        self.ag = shapes.Triangle(W+self.x+self.s*-3, H+self.y+self.s*-0.5, W+self.x+self.s*-1,
                                       H+self.y+self.s*-1, W+self.x+self.s*-0.625, H+self.y+self.s*-0.25, color=o, batch=batch)
        self.ah = shapes.Triangle(W+self.x+self.s*-3, H+self.y+self.s*-0.5, W+self.x+self.s*-3,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*-1, H+self.y+self.s*-1, color=o, batch=batch)
        self.ai = shapes.Triangle(W+self.x+self.s*-3, H+self.y+self.s*-0.5, W+self.x+self.s*-3.5,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*-3, H+self.y+self.s*-1.5, color=o, batch=batch)
        self.aj = shapes.Triangle(W+self.x+self.s*-3.5, H+self.y+self.s*-1.5, W+self.x+self.s*-3.5,
                                       H+self.y+self.s*-2.5, W+self.x+self.s*-3, H+self.y+self.s*-1.5, color=o, batch=batch)
        
        #Llamas
        self.r = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*-1, W+self.x+self.s*0.5,
                                       H+self.y+self.s*-1.5, W+self.x+self.s*1, H+self.y+self.s*-2, color=a, batch=batch)
        self.t = shapes.Triangle(W+self.x+self.s*1, H+self.y+self.s*-1, W+self.x+self.s*1,
                                       H+self.y+self.s*-2.5, W+self.x+self.s*1.5, H+self.y+self.s*-1.5, color=a, batch=batch)
        self.u = shapes.Triangle(W+self.x+self.s*1.5, H+self.y+self.s*-1.5, W+self.x+self.s*1,
                                       H+self.y+self.s*-2.5, W+self.x+self.s*1.5, H+self.y+self.s*-2.5, color=a, batch=batch)
        self.v = shapes.Triangle(W+self.x+self.s*1.5, H+self.y+self.s*-2.5, W+self.x+self.s*1,
                                       H+self.y+self.s*-2.5, W+self.x+self.s*1.25, H+self.y+self.s*-2.75, color=a, batch=batch)
        
        self.ak = shapes.Triangle(W+self.x+self.s*-1, H+self.y+self.s*-1, W+self.x+self.s*-1,
                                       H+self.y+self.s*-2, W+self.x+self.s*-0.5, H+self.y+self.s*-1.5, color=a, batch=batch)
        self.al = shapes.Triangle(W+self.x+self.s*-1, H+self.y+self.s*-1, W+self.x+self.s*-1.5,
                                       H+self.y+self.s*-1.5 , W+self.x+self.s*-1, H+self.y+self.s*-2.5, color=a, batch=batch)
        self.ao = shapes.Triangle(W+self.x+self.s*-1, H+self.y+self.s*-2.5, W+self.x+self.s*-1.5,
                                       H+self.y+self.s*-1.5 , W+self.x+self.s*-1.5, H+self.y+self.s*-2.5, color=a, batch=batch)
        self.ap = shapes.Triangle(W+self.x+self.s*-1.25, H+self.y+self.s*-2.75, W+self.x+self.s*-1,
                                       H+self.y+self.s*-2.5 , W+self.x+self.s*-1.5, H+self.y+self.s*-2.5, color=a, batch=batch)
        
class Star:
    def __init__(self,n,c,v,re,ri):
        self.n = n 
        self.c = c
        self.v = v
        l=list(range(n))
        for i in range(n):
            l[i]=shapes.Star(rdm.random()*WIDTH, rdm.random()*HEIGHT, re, ri, 5, rotation=rdm.random()*180, color=c, batch=batchS)
        self.l = np.array(l)

    def vel(self):
        return self.v  

    def num(self):
        return self.n

    def list(self):
        return self.l  
    
def move(dt, Star):
    for i in range(Star.num()):
        Star.list()[i].y += dt*Star.vel()

def tras(dt, Star):
    for i in range(Star.num()):
        if Star.list()[i].y<=0:
            Star.list()[i].y += HEIGHT
            
#Naves       
Lider=ship2(0,0,35)
Segundo1=ship1(200,-100,25)
Segundo2=ship1(-200,-100,25)
Tercero1=ship2(350,-165,20)
Tercero2=ship2(-350,-165,20)

#Estrellas
StarFondo=Star(400,w,-200,1,1)
StarMedio=Star(300,w,-300,2,1)
StarCerca=Star(150,w,-400,2,1)
StarMuyCerca=Star(150,w,-600,4,1)

clock.schedule(move, StarFondo)
clock.schedule(move, StarMedio)
clock.schedule(move, StarCerca)
clock.schedule(move, StarMuyCerca)

clock.schedule(tras, StarFondo)
clock.schedule(tras, StarMedio)
clock.schedule(tras, StarCerca)
clock.schedule(tras, StarMuyCerca)

@Ventana.event
def on_draw():
    Ventana.clear()
    batchS.draw()
    batch.draw()

run()