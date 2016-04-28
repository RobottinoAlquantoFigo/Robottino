import math, pygame, random # importo librerie 

pygame.init() # inizializzazione pygame

width = 800 # dimensione finestra
height = 600
size = (width, height)


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


screen = pygame.display.set_mode(size) # creazione finestra
pygame.display.set_caption('Robottino')
clock = pygame.time.Clock()

x = 200 # x e y del punto
y = 150

xo1 = 300
yo1 = 200
xo2 = 400
yo2 = 200
xo3 = 300
yo3 = 300

##xo1 = 401
##yo1 = 301
##xo2 = 410
##yo2 = 310
##xo3 = 401
##yo3 = 310

x1 = 400
y1 = 300
x2 = 400
y2 = 320
x3 = 400
y3 = 280
x4 = 600
y4 = 320
x5 = 600
y5 = 280
x6 = 0
y6 = 0
x7 = 0
y7 = 0
x8 = 0
y8 = 0
x9 = 0
y9 = 0

r1c = 20
r1l = 200
r2c = 20
r2l = 150

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
pixAr[x][y] = (240, 155, 200)

dx = 0 # spostamento punto
dy = 0

def rotation(x, y, angle, r, x1, y1): # definisco funzione rotation 

    angle += 1

    if angle > 360: # stop a 360° torna indetro 
        angle -= 360

    x = (x1) + r * math.cos(math.radians(angle)) 
    y = (y1) + r * math.sin(math.radians(angle))

    return x, y, angle # ritorna i valori x, y, angolo

def triangle(x, y, z): # definisco funzione triangle
    # creo un triangolo
    line1 = pygame.draw.line(screen, Rosso, (x), (y), 2)
    line2 = pygame.draw.line(screen, Rosso, (y), (z), 2)
    line3 = pygame.draw.line(screen, Rosso, (z), (x), 2)

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

def collision(m, q, yo1, yo2, yo3, xo1, xo2, xo3, angle):
    global n
    
    a = 0
    b = ""
    if angle <= 270 and angle >= 90:
        if yo1 >= m*xo1 + q:
            a += 1
            b += "1 "
            n += 1
        if yo2 >= m*xo2 + q:
            a += 1
            b += "2 "
            n += 1
        if yo3 >= m*xo3 + q:
            a += 1
            b += "3 "
            n += 1
    if ((angle <= 360 and angle >= 270) or
        (angle >= 0 and angle < 90)):
        if yo1 <= m*xo1 + q:
            a += 1
            b += "1 "
            n += 1
        if yo2 <= m*xo2 + q:
            a += 1
            b += "2 "
            n += 1
        if yo3 <= m*xo3 + q:
            a += 1
            b += "3 "
            n += 1
    return a, b
        
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

    if x <= 0:
        x = width - 1
    elif x >= width - 1:
        x = 1

    if y <= 0:
        y = height - 1
    elif y >= height - 1:
        y = 1

    x0 = (x4+x5)/2
    y0 = (y4+y5)/2
    
    pixAr[x][y] = (125, 205, 245)# disegna il punto 

    # disegno le linee del primo braccio (colore cordinate spessore)
    pygame.draw.line(screen, VerdeForesta, (x2, y2), (x3, y3), 2)
    pygame.draw.line(screen, VerdeForesta, (x2, y2), (x4, y4), 2)
    pygame.draw.line(screen, VerdeForesta, (x3, y3), (x5, y5), 2)
    pygame.draw.line(screen, VerdeForesta, (x4, y4), (x5, y5), 2)
    pygame.draw.line(screen, VerdeForesta, (x4, y4), (x3, y3), 2)

    # disegno le linne del secondo braccio (colore cordinate spessore)
    
    pygame.draw.line(screen, Viola, (x6, y6), (x7, y7), 2)
    pygame.draw.line(screen, Viola, (x6, y6), (x8, y8), 2)
    pygame.draw.line(screen, Viola, (x7, y7), (x9, y9), 2)
    pygame.draw.line(screen, Viola, (x8, y8), (x9, y9), 2)
    pygame.draw.line(screen, Viola, (x8, y8), (x7, y7), 2)
    
    if angle5 == 360: # se la seconda linea completa un giro
        x2, y2, angle1 = rotation(x2, y2, angle1, r1c, x1, y1)
        x3, y3, angle2 = rotation(x3, y3, angle2, r1c, x1, y1)
        x4, y4, angle3 = rotation(x4, y4, angle3, r1l, x1, y1)
        x5, y5, angle4 = rotation(x5, y5, angle4, r1l, x1, y1)

    x6, y6, angle5 = rotation(x6, y6, angle5, r2c, x0, y0)
    x7, y7, angle6 = rotation(x7, y7, angle6, r2c, x0, y0)
    x8, y8, angle7 = rotation(x8, y8, angle7, r2l, x0, y0)
    x9, y9, angle8 = rotation(x9, y9, angle8, r2l, x0, y0)

    # coefficienti angolari e collisioni del braccio

    # linea 1
    m1, q1 = retta(x2, y2, x3, y3)

    check_collision(m1, q1, x, y, x2, y2, x3, y3)

    # linea 2
    m2, q2 = retta(x3, y3, x4, y4)

    check_collision(m2, q2, x, y, x3, y3, x4, y4)

    # linea 3
    m3, q3 = retta(x4, y4, x2, y2)

    check_collision(m3, q3, x, y, x4, y4, x2, y2)

    # ostacolo
    triangle((xo1, yo1), (xo2, yo2), (xo3, yo3))

    # prima linea primo ostacolo
    m4, q4 = retta(xo1, yo1, xo2, yo2)

    check_collision(m4, q4, x, y, xo1, yo1, xo2, yo2)

    # seconda linea primo ostacolo
    m5, q5 = retta(xo2, yo2, xo3, yo3)

    check_collision(m5, q5, x, y, xo2, yo2, xo3, yo3)

    # terza linea primo ostacolo
    m6, q6 = retta(xo3, yo3, xo1, yo1)

    check_collision(m6, q6, x, y, xo3, yo3, xo1, yo1)
    
    a1, b1 = collision(m1, q1, yo1, yo2, yo3, xo1, xo2, xo3, angle1)

    if a1 > 0:
        print(str(n) + " " + str(a1) + " " + str(b1))
        print(angle1)
    
    pygame.display.update() 
    screen.fill(Arancione)

    clock.tick(100) # fps
