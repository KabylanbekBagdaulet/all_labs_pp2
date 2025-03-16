import pygame
import time
import math


pygame.init()
WIDTH, HEIGHT = 900, 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My game")


background = pygame.image.load("clock.png")
righthand = pygame.image.load("rightarm.png")
lefthand = pygame.image.load("leftarm.png")

background = pygame.transform.scale(background, (WIDTH, HEIGHT))

center_x, center_y = WIDTH // 2, HEIGHT // 2

running = True
while running:
    screen.fill((255, 255, 255)) 
    screen.blit(background, (0, 0))

    current_time = time.localtime()
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    minute_angle = -(minutes * 6) 
    second_angle = -(seconds * 6)

    rotated_right = pygame.transform.rotate(righthand, minute_angle)
    rotated_left = pygame.transform.rotate(lefthand, second_angle)

    right_rect = rotated_right.get_rect(center= (center_x, center_y))
    left_rect = rotated_left.get_rect(center = (center_x, center_y))

    screen.blit(rotated_right, right_rect.topleft)
    screen.blit(rotated_left, left_rect.topleft)






    pygame.display.flip()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)
pygame.quit()

