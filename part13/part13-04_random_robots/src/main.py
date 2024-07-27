# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint
 
pygame.init()
screen = pygame.display.set_mode((640, 480))
 
robot = pygame.image.load("robot.png")

screen.fill((0, 0, 0))
for i in range(1000):
    screen.blit(robot, (randint(0,640-robot.get_width()), randint(0, 480-robot.get_height())))
pygame.display.flip()
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()