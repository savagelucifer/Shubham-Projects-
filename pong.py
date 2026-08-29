import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 900
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("PONG")

clock = pygame.time.Clock()

# Colors
BLACK = (10, 10, 20)
WHITE = (255, 255, 255)

# Paddles
PADDLE_WIDTH = 15
PADDLE_HEIGHT = 100
PADDLE_SPEED = 7

left_paddle = pygame.Rect(
    30, HEIGHT // 2 - PADDLE_HEIGHT // 2,
    PADDLE_WIDTH, PADDLE_HEIGHT
)

right_paddle = pygame.Rect(
    WIDTH - 45, HEIGHT // 2 - PADDLE_HEIGHT // 2,
    PADDLE_WIDTH, PADDLE_HEIGHT
)

# Ball
ball = pygame.Rect(
    WIDTH // 2 - 10,
    HEIGHT // 2 - 10,
    20, 20
)

ball_x = 6
ball_y = 5

# Score
left_score = 0
right_score = 0

font = pygame.font.Font(None, 80)
winner_font = pygame.font.Font(None, 100)
small_font = pygame.font.Font(None, 35)


def reset_ball():
    global ball_x, ball_y

    ball.center = (WIDTH // 2, HEIGHT // 2)

    ball_x = random.choice([-6, 6])
    ball_y = random.choice([-5, 5])


def reset_game():
    global left_score, right_score

    left_score = 0
    right_score = 0

    left_paddle.centery = HEIGHT // 2
    right_paddle.centery = HEIGHT // 2

    reset_ball()


running = True
game_over = False
winner = ""

while running:

    # ---------------- EVENTS ----------------
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            if game_over and event.key == pygame.K_r:
                reset_game()
                game_over = False
                winner = ""

    # ---------------- GAME ----------------
    if not game_over:

        keys = pygame.key.get_pressed()

        # Player 1
        if keys[pygame.K_w] and left_paddle.top > 0:
            left_paddle.y -= PADDLE_SPEED

        if keys[pygame.K_s] and left_paddle.bottom < HEIGHT:
            left_paddle.y += PADDLE_SPEED

        # Player 2
        if keys[pygame.K_UP] and right_paddle.top > 0:
            right_paddle.y -= PADDLE_SPEED

        if keys[pygame.K_DOWN] and right_paddle.bottom < HEIGHT:
            right_paddle.y += PADDLE_SPEED

        # Move ball
        ball.x += ball_x
        ball.y += ball_y

        # Top/bottom collision
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_y *= -1

        # Left paddle collision
        if ball.colliderect(left_paddle) and ball_x < 0:
            ball.left = left_paddle.right
            ball_x *= -1

        # Right paddle collision
        if ball.colliderect(right_paddle) and ball_x > 0:
            ball.right = right_paddle.left
            ball_x *= -1

        # Right player scores
        if ball.left <= 0:
            right_score += 1

            if right_score >= 5:
                winner = "PLAYER 2 WINS!"
                game_over = True
            else:
                reset_ball()

        # Left player scores
        if ball.right >= WIDTH:
            left_score += 1

            if left_score >= 5:
                winner = "PLAYER 1 WINS!"
                game_over = True
            else:
                reset_ball()

    # ---------------- DRAW ----------------
    screen.fill(BLACK)

    # Middle line
    for y in range(0, HEIGHT, 30):
        pygame.draw.rect(
            screen,
            WHITE,
            (WIDTH // 2 - 2, y, 4, 15)
        )

    # Paddles
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)

    # Ball
    pygame.draw.ellipse(screen, WHITE, ball)

    # Scores
    left_text = font.render(str(left_score), True, WHITE)
    right_text = font.render(str(right_score), True, WHITE)

    screen.blit(
        left_text,
        (WIDTH // 2 - 100, 30)
    )

    screen.blit(
        right_text,
        (WIDTH // 2 + 60, 30)
    )

    # Controls
    controls = small_font.render(
        "P1: W/S       P2: UP/DOWN       ESC: Quit",
        True,
        WHITE
    )

    screen.blit(
        controls,
        (WIDTH // 2 - controls.get_width() // 2, HEIGHT - 40)
    )

    # Winner screen
    if game_over:

        winner_text = winner_font.render(
            winner,
            True,
            WHITE
        )

        restart_text = small_font.render(
            "Press R to play again",
            True,
            WHITE
        )

        screen.blit(
            winner_text,
            (
                WIDTH // 2 - winner_text.get_width() // 2,
                HEIGHT // 2 - 80
            )
        )

        screen.blit(
            restart_text,
            (
                WIDTH // 2 - restart_text.get_width() // 2,
                HEIGHT // 2 + 30
            )
        )

    pygame.display.flip()

    clock.tick(60)


pygame.quit()
sys.exit()
