import sys, pygame,time
from PIL import Image
from pygame.locals import *
from array import*
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.datasets import ClassificationDataSet
from pybrain.supervised import BackpropTrainer

n = 220*150


def entrenador(d):
    net = buildNetwork(d.indim, 8, d.outdim, recurrent=True)
    trainer = BackpropTrainer(net, d, learningrate=0.01, momentum=0.99, verbose = True)#consistencia para hacer modificaciones en los pesos
    for epoch in range(0, 30):
        trainer.train()
    return trainer

def test(trained, testarr):
    n=len(testarr)
    classyTestData=ClassificationDataSet(n,nb_classes=2,class_labels=['simbolo1','simbolo2'])
    classyTestData.appendLinked(testarr, [0])
    classyTestData.appendLinked(testarr, [1])
    trained.testOnData(classyTestData, verbose= True)

def makeElegantData(array1, array2, array3, array4, array5, array6):
    n = len(array1)
    CDS = ClassificationDataSet(n, nb_classes=2, class_labels=['simbolo1', 'simbolo2'])

    CDS.appendLinked(array1, [0])
    CDS.appendLinked(array2, [0])
    CDS.appendLinked(array3, [0])

    CDS.appendLinked(array4, [1])
    CDS.appendLinked(array5, [1])
    CDS.appendLinked(array6, [1])

    return CDS



pygame.init()

ventana = pygame.display.set_mode((220,150))
titulo = pygame.display.set_caption("[Red Neuronal]")

ventana.fill((255,255,255))

brush = pygame.image.load("brush.png")
brush = pygame.transform.scale(brush,(20,20))

erase = pygame.image.load("erase.png")
erase = pygame.transform.scale(erase,(200,200))

pygame.display.update()
clock = pygame.time.Clock()

t = 0

a = 1
b = 1

fuego1 = Image.open("figura1_a.png")
fuego2 = Image.open("figura1_b.png")
fuego3 = Image.open("figura1_c.png")

simbolo11 = array('i')
simbolo12 = array('i')
simbolo13 = array('i')
for f1x in range(1,220):
    for f1y in range(1,150):
        pixsimbolo11 = fuego1.load()
        pixsimbolo11[f1x,f1y] #Variable que almacena pixel por pixel
        
        if pixsimbolo11[f1x,f1y] == (255, 255, 255):
            simbolo11.append(0)
        else:
            simbolo11.append(1)
#            pixfuego1 = pixsimbolo11  #Cambio de variable para utilizar en otro lado
            
            #time.sleep(3) Para comprobar que si imprimen 1
for f2x in range (1,220):
    for f2y in range(1,150):
        pixsimbolo12 = fuego2.load()
        pixsimbolo12[f2x,f2y] #Variable que almacena pixel por pixel
        
        if pixsimbolo12[f2x,f2y] == (255, 255, 255):
            simbolo12.append(0)
        else:
            simbolo12.append(1)
            #pixfuego2 = pixsimbolo12

for f3x in range (1,220):
    for f3y in range (1,150):
        pixsimbolo13 = fuego3.load()
        pixsimbolo13[f3x,f3y] #Variable que almacena pixel por pixel
        if pixsimbolo13[f3x,f3y] == (255, 255, 255):
            simbolo13.append(0)
        else:
            simbolo13.append(1)

aire1 = Image.open("figura2_a.png")
aire2 = Image.open("figura2_b.png")
aire3 = Image.open("figura2_c.png")
simbolo21 = array('i')
simbolo22 = array('i')
simbolo23 = array('i')
for a1x in range(1,220):
    for a1y in range(1,150):
        pixair1 = aire1.load()
        pixair1[a1x,a1y] #Variable que almacena pixel por pixel
        if pixair1[a1x,a1y] == (255, 255, 255):
            simbolo21.append(0)
        else: 
            simbolo21.append(1)            

for a2x in range (1,220):
    for a2y in range(1,150):
        pixair2 = aire2.load()
        pixair2[a2x,a2y] #Variable que almacena pixel por pixel
        if pixair2[a2x,a2y] == (255, 255, 255):
            simbolo22.append(0)
        else: 
            simbolo22.append(1)
        
for a3x in range (1,220):
    for a3y in range (1,150):
        pixair3 = aire3.load()
        pixair3[a3x,a2y]#Variable que almacena pixel por pixel
        if pixair3 == (255, 255, 255):
            simbolo23.append(0)
        else: 
            simbolo23.append(1)

trainingdata=makeElegantData(simbolo11,simbolo12,simbolo13,simbolo21,simbolo22,simbolo23)
trained=entrenador(trainingdata)
                                                                          
while 1:
    clock.tick(60)
    x,y = pygame.mouse.get_pos()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        
        elif event.type == KEYDOWN:
            if event.key == K_p:
                print "mieu"
                pygame.image.save(ventana,"prueba.png")
                im = Image.open("prueba.png")#Hace el recorrido del dibujo
                runarray = array('i')
                for a in range(1,220): #Ancho
                    for b in range(1,150): #Largo
                        pix = im.load()
                        pix[a,b]
                        if pix[a,b] == (255, 255, 255):
                            runarray.append(0)
                        else:
                            runarray.append(1)
                print runarray
                test(trained, runarray)
            if event.key == K_c:
                ventana.blit(erase,(x-120,y-120))
                pygame.display.update()
                    
        elif event.type == MOUSEBUTTONDOWN:
            t = 1                                     
            
        elif event.type == MOUSEBUTTONUP:
            t = 0
                
        if t == 1:
            ventana.blit(brush,(x-10,y-10))
            pygame.display.update()