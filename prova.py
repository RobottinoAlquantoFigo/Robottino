import math, pygame # importo librerie 

pygame.init() # inizializzazione pygame

width = 800 # dimensione finestra
height = 600
size = (width, height)

screen = pygame.display.set_mode(size) # creazione finestra
pygame.display.set_caption('Robottino')
clock = pygame.time.Clock()

x = 200 # x e y del punto
y = 150

xr = 20 # dimensioni e posizione del rettangolo
yr = 20
w = 100
h = 50

x1 = 400 # primo punto prima linea
y1 = 300
x2 = 250 # secondo punto prima linea e primo punto seconda linea
y2 = 300
x3 = 360 # secondo punto seconda linea
y3 = 120

r = math.sqrt((x2-x1)**2 + (y2-y1)**2) # dimensione linea

angle = 0 # angolo prima linea
angle2 = 100 # angolo seconda linea
n = 0 # contatore a caso

pixAr = pygame.PixelArray(screen) # creazione punto
pixAr[x][y] = (255, 255, 255)

dx = 0 # spostamento punto
dy = 0

def rotation(x, y, angle, r, x1, y1): # definisco funzione rotation 
    
    x = (x1) + r * math.cos(math.radians(angle)) 
    y = (y1) + r * math.sin(math.radians(angle))
    angle += 1

    if angle > 360: # stop a 360° torna indetro 
        angle -= 360

    return x, y, angle # ritorna i valori x, y, angolo

x2, y2, angle = rotation(x2, y2, angle, r, x1, y1) # creaqzione line a rotaz<ione 

while 1: 
    for event in pygame.event.get(): # schiaccia x esce dalla finestra 
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN: # comandi a tastiera 
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                dx = 1
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                dx = -1
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                dy = 1
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                dy = -1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                dx = 0
            if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                dx = 0
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                dy = 0
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                dy = 0

    x += dx # inc punto x
    y += dy # inc punto y
    
    pixAr[x][y] = (255, 255, 255)# disegna il punto 

    pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 1) # dignare la linea colore cordinate spessore 
    pygame.draw.line(screen, (255, 255, 255), (x2, y2), (x3, y3), 1) 

    if angle2 == 360: # se la seconda linea completa un giro
        x2, y2, angle = rotation(x2, y2, angle, r, x1, y1) # ruoto la prima
        
    x3, y3, angle2 = rotation(x3, y3, angle2, r, x2, y2) # ruoto la seconda linea
            
    if x2-x1 == 0: #caclolo coeficente angiolare e q
        m = 1
    else:
        m = (y2-y1)/(x2-x1)
    q = y1-(m*x1)
    
    if y >= (m*x + q) - 1 and y <= (m*x + q) + 1:
        if ((x >= x1 and x <= x2) or (x >= x2 and x <= x1)) and (
            (y >= y1 and y <= y2) or (y >= y2 and x <= y1)):
            pygame.quit()
            quit()
##            n += 1
##            print("Collisione n° %d" %(n))

    if x3-x2 == 0: # calcolo coeficente angoloare e Q 
        m2 = 1
    else:
        m2 = (y3-y2)/(x3-x2)
    q2 = y2-(m2*x2)
    
    if y >= (m2*x + q2) - 1 and y <= (m2*x + q2) + 1:
        if ((x >= x2 and x <= x3) or (x >= x3 and x <= x2)) and (
            (y >= y2 and y <= y3) or (y >= y3 and x <= y2)):
##            pygame.quit()
##            quit()
            n += 1
            print("Collisione n° %d" %(n))

##    print("x : " + str(x)) # printa x e converte in stringa
##    print("y : " + str(y)) # printa y e converte in stringa
##    print("x2: " + str(int(x2))) # printa x2 e converte in stringa e in intero
##    print("y2: " + str(int(y2))) # printa y2 e converte in stringa e in intero

        
    pygame.display.update() 
    screen.fill((0, 0, 0))

    clock.tick(100)  # tempo di frame 
