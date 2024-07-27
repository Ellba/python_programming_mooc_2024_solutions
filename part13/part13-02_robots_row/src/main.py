# WRITE YOUR SOLUTION HERE:
import pygame
 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
 
robot = pygame.image.load("robot.png")
 
right_x = width-robot.get_width()
down_y = height-robot.get_height()
 
screen.fill((0, 0, 0))
x = 50
y = 100
for i in range(10):
    screen.blit(robot, (x, y))
    x += robot.get_width()
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()