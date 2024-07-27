import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_width = robot.get_width()
robot_height = robot.get_height()

x1 = 0
y1 = height // 4
x2 = width - robot_width
y2 = 3 * height // 4
speed1 = 5
speed2 = -5
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill((0, 0, 0))
    screen.blit(robot, (x1, y1))
    screen.blit(robot, (x2, y2))
    pygame.display.flip()

    x1 += speed1
    if x1 <= 0 or x1 + robot_width >= width:
        speed1 = -speed1

    x2 += speed2
    if x2 <= 0 or x2 + robot_width >= width:
        speed2 = -speed2

    clock.tick(60)
