# WRITE YOUR SOLUTION HERE:

import pygame
import random

# Initialize pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

# Load ball image
ball = pygame.image.load("ball.png")
ball_rect = ball.get_rect()

# Set initial position and velocity
ball_rect.x = random.randint(0, window.get_width() - ball_rect.width)
ball_rect.y = random.randint(0, window.get_height() - ball_rect.height)
velocity = [random.choice([-5, 5]), random.choice([-5, 5])]

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Update ball position
    ball_rect.x += velocity[0]
    ball_rect.y += velocity[1]

    # Check for collision with window edges
    if ball_rect.left <= 0 or ball_rect.right >= window.get_width():
        velocity[0] = -velocity[0]
    if ball_rect.top <= 0 or ball_rect.bottom >= window.get_height():
        velocity[1] = -velocity[1]

    window.fill((0, 0, 0))  # Clear the screen
    window.blit(ball, ball_rect)  # Draw the ball
    pygame.display.flip()  # Update the display

    clock.tick(60)  # Maintain 60 frames per second
