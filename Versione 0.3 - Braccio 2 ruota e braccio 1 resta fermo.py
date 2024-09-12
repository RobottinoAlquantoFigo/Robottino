import pygame, math

pygame.init()

def rotazione(x1,y1,angle,r,x,y):
    
    x1 = x + r*math.cos(math.radians(angle))
    y1 = y + r*math.cos(math.radians(angle))

    angle += 50

    if angle == 360:
        angle -= 360
    return x1,y1,angle


#-----Colori-----
Arancione = (255, 165, 0)
Bianco = (255, 255, 255)
Blu = (0, 0, 255)
Giallo = (255, 255, 0)
Nero = (0, 0, 0)
Oro = (255, 215, 0)
Rame = (184, 115, 51)
Rosa = (255, 192, 203)
Rosso = (255, 0, 0)
Turchese = (48, 213, 173)
Verde = (0, 255, 0)
VerdeForesta = (34, 139, 34)
Viola = (143, 0, 255)

angle = 0.001

#-----Valori del braccio 1-----
Br1XPerno1DxA = 295      #Punto in alto a dx X
Br1YPerno1DxA = 160      #Punto in alto a dx Y
Br1XPerno2DxB = 295      #Punto in basso a dx X
Br1YPerno2DxB = 260      #Punto in basso a dx Y
Br1XPerno2SxB = 300      #Punto in basso a sx X
Br1YPerno2SxB = 260      #Punto in basso a sx Y
Br1XPerno1SxA = 300      #Punto in alto a sx X
Br1YPerno1SxA = 160      #Punto in alto a sx Y

#-----Valori del braccio 2-----
#Br2X = 295
#Br2Y = 260

Br2XPerno1DxA = 295      #Punto in alto a dx X
Br2YPerno1DxA = 260      #Punto in alto a dx Y
Br2XPerno2DxB = 295      #Punto in basso a dx X
Br2YPerno2DxB = 310      #Punto in basso a dx Y
Br2XPerno2SxB = 300      #Punto in basso a sx X
Br2YPerno2SxB = 310      #Punto in basso a sx Y
Br2XPerno1SxA = 300      #Punto in alto a sx X
Br2YPerno1SxA = 260      #Punto in alto a sx Y

#-----Perno tra i due bracci-----
PrnX = 300
PrnY = 260

#-----Definizione schermo-----
altezza = 460
lunghezza = 600

schermo = pygame.display.set_mode([lunghezza, altezza])
pygame.display.set_caption("Versione 0.3 - Braccio 2 ruota e braccio 1 resta fermo")

schermo.fill(Arancione)

#-----Braccio 1 e il suo raggio d'azione----- 
pygame.draw.line(schermo, VerdeForesta, (Br1XPerno1DxA, Br1YPerno1DxA), (Br1XPerno2DxB, Br1YPerno2DxB), 4)
pygame.draw.line(schermo, VerdeForesta, (Br1XPerno2DxB, Br1YPerno2DxB), (Br1XPerno2SxB, Br1YPerno2SxB), 4)
pygame.draw.line(schermo, VerdeForesta, (Br1XPerno2SxB, Br1YPerno2SxB), (Br1XPerno1SxA, Br1YPerno1SxA), 4)
pygame.draw.line(schermo, VerdeForesta, (Br1XPerno1SxA, Br1YPerno1SxA), (Br1XPerno1DxA, Br1YPerno1DxA), 4)

pygame.draw.circle(schermo, VerdeForesta, (300, 160), 100, 2)

#pygame.draw.rect(schermo, Nero, (295, 60, 10, 100))

#-----Braccio 2 e il suo raggio d'azione-----
pygame.draw.line(schermo, Viola, (Br2XPerno1DxA, Br2YPerno1DxA), (Br2XPerno2DxB, Br2YPerno2DxB), 4)
pygame.draw.line(schermo, Viola, (Br2XPerno2DxB, Br2YPerno2DxB), (Br2XPerno2SxB, Br2YPerno2SxB), 4)
pygame.draw.line(schermo, Viola, (Br2XPerno2SxB, Br2YPerno2SxB), (Br2XPerno1SxA, Br2YPerno1SxA), 4)
pygame.draw.line(schermo, Viola, (Br2XPerno1SxA, Br2YPerno1SxA), (Br2XPerno1DxA, Br2YPerno1DxA), 4)

pygame.draw.circle(schermo, Viola, (300, 160), 150, 2)  #Raggio massimo
pygame.draw.circle(schermo, Viola, (300, 160), 50, 2)   #Raggio minimo

#-----Perni dei bracci-----
#pygame.draw.circle(schermo, Nero, (300, 160), 5)
#pygame.draw.circle(schermo, Nero, (PrnX, PrnY), 5)

#-----Triangoli-----
pygame.draw.line(schermo, Rosso, (120, 120), (160, 160), 2) # -
pygame.draw.line(schermo, Rosso, (160, 160), (100, 220), 2) # |Triangolo esterno
pygame.draw.line(schermo, Rosso, (100, 220), (120, 120), 2) # -

pygame.draw.line(schermo, Rosso, (350, 300), (210, 210), 2) # -
pygame.draw.line(schermo, Rosso, (210, 210), (170, 290), 2) # |Triangolo interno
pygame.draw.line(schermo, Rosso, (170, 290), (350, 300), 2) # -



pygame.display.flip()


#while 1:
#-----Braccio 2 e il suo raggio d'azione in movimento-----
    #pygame.draw.line(schermo, Nero, (Br2XPerno1DxA, Br2YPerno1DxA), (Br2XPerno2DxB, Br2YPerno2DxB), 4)
    #pygame.draw.line(schermo, Nero, (Br2XPerno2DxB, Br2YPerno2DxB), (Br2XPerno2SxB, Br2YPerno2SxB), 4)
    #pygame.draw.line(schermo, Nero, (Br2XPerno2SxB, Br2YPerno2SxB), (Br2XPerno1SxA, Br2YPerno1SxA), 4)
    #pygame.draw.line(schermo, Nero, (Br2XPerno1SxA, Br2YPerno1SxA), (Br2XPerno1DxA, Br2YPerno1DxA), 4)

    #angolo = 0

    #if (angolo == 360):
        




    
