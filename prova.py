import math, pygame

pygame.init()

width = 800
height = 600
size = (width, height)

screen = pygame.display.set_mode(size)
pygame.display.set_caption('rotazione')
clock = pygame.time.Clock()

x = 400
y = 300

xr = 20
yr = 20
w = 100
h = 50

x1 = 150
y1 = 150
x2 = 250
y2 = 300
x3 = 360
y3 = 120

r = math.sqrt((x2-x1)**2 + (y2-y1)**2)

angle = 0
n = 0

pixAr = pygame.PixelArray(screen)
pixAr[x][y] = (255, 255, 255)

dx = 0
dy = 0

def rotation(x, y, angle, r, x1, y1):
    
    x = (x1) + r * math.cos(math.radians(angle))
    y = (y1) + r * math.sin(math.radians(angle))
    angle += 1

    if angle > 360:
        angle -= 360

    return x, y, angle

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
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

    x += dx
    y += dy
    
    pixAr[x][y] = (255, 255, 255)

    pygame.draw.rect(screen, (255, 255, 255), (xr, yr, w, h))

    pygame.draw.line(screen, (255, 255, 255), (x1, y1), (x2, y2), 1)

    x2, y2, angle = rotation(x2, y2, angle, r, x1, y1)

    
    m = (y2-y1)/(x2-x1)
    q = y1-(m*x1)
    
    if y == (m*x + q) or y == (m*x + q) + 1 or y == (m*x + q) - 1:
        if x >= x1 and x <= x2 and y >= y1 and y <= y2:
            pygame.quit()
            quit()
##            n += 1
##            print("Collisione n° %d" %(n))
        
    if x >= xr and x <= xr + w and y >= yr and y <= yr + h:
        pygame.quit
        quit()
        
    pygame.display.update()
    screen.fill((0, 0, 0))

    clock.tick(100)
