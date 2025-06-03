import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncing Ball")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Ball properties
ball_radius = 20
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_vel = [3, 3]

clock = pygame.time.Clock()

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Update ball position
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # Bounce off walls
    if ball_pos[0] - ball_radius <= 0 or ball_pos[0] + ball_radius >= WIDTH:
        ball_vel[0] = -ball_vel[0]
    if ball_pos[1] - ball_radius <= 0 or ball_pos[1] + ball_radius >= HEIGHT:
        ball_vel[1] = -ball_vel[1]

    # Clear screen
    screen.fill(WHITE)

    # Draw ball
    pygame.draw.circle(screen, RED, (int(ball_pos[0]), int(ball_pos[1])), ball_radius)

    # Update display
    pygame.display.flip()
    clock.tick(60)
