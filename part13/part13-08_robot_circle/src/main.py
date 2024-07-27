import pygame
import math

# Initialize pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

# Load robot image
robot = pygame.image.load("robot.png")

# Initialize variables
num_robots = 10
angles = [i * (2 * math.pi / num_robots) for i in range(num_robots)]
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    window.fill((0, 0, 0))  # Clear the screen

    for i in range(num_robots):
        # Calculate position for each robot
        x = 320 + math.cos(angles[i]) * 100 - robot.get_width() / 2
        y = 240 + math.sin(angles[i]) * 100 - robot.get_height() / 2
        # Draw each robot
        window.blit(robot, (x, y))
        # Update angle for the next frame
        angles[i] += 0.1

    pygame.display.flip()  # Update the display
    clock.tick(60)  # Maintain 60 frames per second
