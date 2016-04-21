import math, pygame, random # importo librerie 

pygame.init() # inizializzazione pygame

width = 800 # dimensione finestra
height = 600
size = (width, height)

screen = pygame.display.set_mode(size) # creazione finestra
pygame.display.set_caption('Robottino')
clock = pygame.time.Clock()

x = 200 # x e y del punto
y = 150

xr = 300 # dimensioni e posizione del rettangolo
yr = 200
w = 100
h = 50

x1 = 400
y1 = 300
x2 = 0
y2 = 0
x3 = 0
y3 = 0
x4 = 0
y4 = 0
x5 = 0
y5 = 0
x6 = 0
y6 = 0

r1c = 20
r1l = 100
r2c = 20
r2l = 75

angle1 = 90
angle2 = 270
angle3 = math.degrees(math.atan(r1c/r1l))
angle4 = math.degrees(math.atan(-r1c/r1l))
angle5 = 90
angle6 = 270
angle7 = math.degrees(math.atan(r2c/r2l))
angle8 = math.degrees(math.atan(-r2c/r2l))

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

def triangle(x, y, z): # definisco funzione triangle
    # creo un triangolo
    line1 = pygame.draw.line(screen, (255, 255, 255), (x), (y), 1)
    line2 = pygame.draw.line(screen, (255, 255, 255), (y), (z), 1)
    line3 = pygame.draw.line(screen, (255, 255, 255), (z), (x), 1)

def retta(x1, y1, x2, y2):
    
    if x2-x1 == 0: # caclolo coeficente angiolare e q
        m = 0
    else:
        m = (y2-y1)/(x2-x1)
    q = y1-(m*x1)

    return m, q

def check_collision(m, q, x, y, x1, y1, x2, y2):
    global n
    
    if (y >= (m*x + q) - 1 and y <= (m*x + q) + 1) or (x == q):
        if ((x >= x1 and x <= x2) or (x >= x2 and x <= x1)) and (
            (y >= y1 and y <= y2) or (y >= y2 and y <= y1)):
            n += 1
            print("Collisione n° %d" %(n))

def line_collision(m1, q1, m2, q2):
    global n

    y1 = m1*x + q1
    y2 = m2*x + q2

    if y1 - 1 >= y2 and y1 + 1 <= y2:
        n += 1
        print("Collisione linea n° %d" %(n))

##x2, y2, angle = rotation(x2, y2, angle, r, x1, y1)

while 1: 
    for event in pygame.event.get(): # clicco la x per chiudere il programma
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN: # comandi tastiera 
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

    # digno le due linee (colore cordinate spessore)
    pygame.draw.line(screen, (255, 255, 255), (x2, y2), (x3, y3), 1)
    pygame.draw.line(screen, (255, 255, 255), (x2, y2), (x4, y4), 1)
    pygame.draw.line(screen, (255, 255, 255), (x3, y3), (x5, y5), 1)
    pygame.draw.line(screen, (255, 255, 255), (x4, y4), (x5, y5), 1)
    pygame.draw.line(screen, (255, 255, 255), (x4, y4), (x3, y3), 1)
    pygame.draw.line(screen, (255, 255, 255), (x5, y5), (x2, y2), 1)
    pygame.draw.line(screen, (255, 255, 255), (x6, y6), (x, y), 1) 

##    if angle2 == 360: # se la seconda linea completa un giro
    x2, y2, angle1 = rotation(x2, y2, angle1, r1c, x1, y1)
    x3, y3, angle2 = rotation(x3, y3, angle2, r1c, x1, y1)
    x4, y4, angle3 = rotation(x4, y4, angle3, r1l, x1, y1)
    x5, y5, angle4 = rotation(x5, y5, angle4, r1l, x1, y1)
    x6, y6, angle5 = rotation(x6, y6, angle5, r1l, x1, y1)

    # coefficienti angolari e collisioni delle linee

    # linea 1
    m1, q1 = retta(x1, y1, x2, y2)

    check_collision(m1, q1, x, y, x1, y1, x2, y2)

    # linea 2
    m2, q2 = retta(x2, y2, x3, y3)

    check_collision(m2, q2, x, y, x2, y2, x3, y3)

    # ostacolo
    triangle((xr, yr), (xr+100, yr), (xr, yr+100))

    # prima linea primo ostacolo
    m3, q3 = retta(xr, yr, xr+100, yr)

    check_collision(m3, q3, x, y, xr, yr, xr+100, yr)

    # seconda linea primo ostacolo
    m4, q4 = retta(xr+100, yr, xr, yr+100)

    check_collision(m4, q4, x, y, xr+100, yr, xr, yr+100)

    # terza linea primo ostacolo
    m5, q5 = retta(xr, yr+100, xr, yr)

    check_collision(m5, q5, x, y, xr, yr+100, xr, yr)
        
    pygame.display.update() 
    screen.fill((0, 0, 0))

    clock.tick(100) # fps
