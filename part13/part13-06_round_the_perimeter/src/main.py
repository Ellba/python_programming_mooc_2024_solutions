# # WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

x = 0
y = 0
speed = 5
clock = pygame.time.Clock()

direction = 'right'

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()

    if direction == 'right':
        x += speed
        if x + robot.get_width() >= width:
            x = width - robot.get_width()
            direction = 'down'
    elif direction == 'down':
        y += speed
        if y + robot.get_height() >= height:
            y = height - robot.get_height()
            direction = 'left'
    elif direction == 'left':
        x -= speed
        if x <= 0:
            x = 0
            direction = 'up'
    elif direction == 'up':
        y -= speed
        if y <= 0:
            y = 0
            direction = 'right'

    clock.tick(60)
