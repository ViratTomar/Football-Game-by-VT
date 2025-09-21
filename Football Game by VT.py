import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Football Game by VT")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 60

# Players
player_width, player_height = 20, 80
player1 = pygame.Rect(50, HEIGHT//2 - player_height//2, player_width, player_height)
player2 = pygame.Rect(WIDTH-70, HEIGHT//2 - player_height//2, player_width, player_height)
player_speed = 5

# Ball
ball_size = 20
ball = pygame.Rect(WIDTH//2 - ball_size//2, HEIGHT//2 - ball_size//2, ball_size, ball_size)
ball_speed_x = 4
ball_speed_y = 4

# Scores
score1 = 0
score2 = 0
font = pygame.font.SysFont(None, 50)

# Game loop
running = True
while running:
    screen.fill(GREEN)  # Football field color
    pygame.draw.line(screen, WHITE, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 5)  # Midline
    pygame.draw.ellipse(screen, WHITE, (WIDTH//2 - 50, HEIGHT//2 - 50, 100, 100), 5)  # Center circle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_s] and player1.bottom < HEIGHT:
        player1.y += player_speed
    if keys[pygame.K_UP] and player2.top > 0:
        player2.y -= player_speed
    if keys[pygame.K_DOWN] and player2.bottom < HEIGHT:
        player2.y += player_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Collision with top/bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed_y *= -1

    # Collision with players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed_x *= -1

    # Scoring
    if ball.left <= 0:
        score2 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= -1
    if ball.right >= WIDTH:
        score1 += 1
        ball.center = (WIDTH//2, HEIGHT//2)
        ball_speed_x *= -1

    # Draw players and ball
    pygame.draw.rect(screen, RED, player1)
    pygame.draw.rect(screen, BLUE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    score_text = font.render(f"{score1} : {score2}", True, BLACK)
    screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, 20))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
