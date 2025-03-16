import pygame


pygame.init()

width, height = 600, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("move ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

run = True

radius = 25
speed = 20
x, y = width/2, height/2

while run:
    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x - radius - speed >=0:
                x-=speed
            if event.key == pygame.K_RIGHT and x + radius + speed <=height:
                x+=speed
            if event.key == pygame.K_UP and y - radius - speed >=0:
                y-=speed
            if event.key == pygame.K_DOWN and y + radius + speed <=width:
                y+=speed

pygame.quit()
