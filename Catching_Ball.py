import pygame
import random

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = pygame.display.Info().current_w, pygame.display.Info().current_h
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.FULLSCREEN)
pygame.display.set_caption("Catch the Falling Objects")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
basket_width = 70
basket_height = 20
basket_speed = 7
basket = pygame.Rect(SCREEN_WIDTH // 2 - basket_width // 2, SCREEN_HEIGHT - basket_height - 10, basket_width, basket_height)
object_width = 30
object_height = 30
object_speed = 3
object_list = []
score = 0
lives = 5
font = pygame.font.SysFont(None, 36)

def create_falling_object():
    x_pos = random.randint(0, SCREEN_WIDTH - object_width)
    return pygame.Rect(x_pos, 0, object_width, object_height)

def draw_text(text, font, color, x, y):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))

running = True
clock = pygame.time.Clock()
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and basket.left > 0:
        basket.move_ip(-basket_speed, 0)
    if keys[pygame.K_RIGHT] and basket.right < SCREEN_WIDTH:
        basket.move_ip(basket_speed, 0)

    if len(object_list) < 3 and random.randint(1, 40) == 1:
        object_list.append(create_falling_object())

    for obj in object_list[:]:
        obj.move_ip(0, object_speed)
        pygame.draw.rect(screen, RED, obj)
        if basket.colliderect(obj):
            score += 1
            object_list.remove(obj)
        elif obj.top > SCREEN_HEIGHT:
            lives -= 1
            object_list.remove(obj)
    pygame.draw.rect(screen, GREEN, basket)

    draw_text(f"Score: {score}", font, BLACK, 10, 10)
    draw_text(f"Lives: {lives}", font, BLACK, SCREEN_WIDTH - 150, 10)
    if lives <= 0:
        draw_text("Game Over", font, RED, SCREEN_WIDTH // 2 - 100, SCREEN_HEIGHT // 2)
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
