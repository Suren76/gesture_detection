import pygame
import random
from time import sleep

WINDOW_SIZE = [600, 660]
FRAME_COLOR = (0, 255, 204)
WHITE = (255, 255, 255)
BLUE = (200, 255, 255)
SIZE_BLOCK = 20
MARGIN = 1
SNAKE_COLOR = (0, 255, 0)
x = 140
y = 320
step = 20
go = ""
apple = [int(random.randint(2, 27)*20), int(random.randint(2, 27)*20)]
apple_end = [int(random.randint(2, 27)*20), int(random.randint(2, 27)*20)]


def draw_background():
    screen.fill(FRAME_COLOR)
    for row in range(int(WINDOW_SIZE[0] / SIZE_BLOCK) - 3):
        for column in range(int(WINDOW_SIZE[1] / SIZE_BLOCK) - 6):
            if (row + column) % 2 == 0:
                color = BLUE
            else:
                color = WHITE
            if row == 0 or column == 0 or row == 26 or column == 26:
                pass
                # color = (0, 0, 255)
            pygame.draw.rect(screen, color, [20 + column * SIZE_BLOCK + MARGIN * (column + 1),
                                             20 + row * SIZE_BLOCK + MARGIN * (row + 1), SIZE_BLOCK, SIZE_BLOCK])


screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Օձի կծած")
snake_body = [[x, y], [x + 20, y], [x + 40, y]]
pygame.font.init()
font = pygame.font.SysFont("arial", 60, bold=True)

while True:
    pygame.time.delay(100)

    if len(snake_body)-2 == 0:
        print("Game over")
        game_over = font.render(f"Game Over", True, (255, 0, 0))
        screen.blit(game_over, (40, 600))
        pygame.display.flip()
        sleep(3)
        pygame.quit()
    if len(snake_body)-2 == 10:
        print("Game over")
        game_over = font.render(f"You Win", True, (25, 112, 221))
        screen.blit(game_over, (40, 600))
        pygame.display.flip()
        sleep(3)
        pygame.quit()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("exit")
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and go != "LEFT":
                go = "RIGHT"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and go != "RIGHT":
                go = "LEFT"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and go != "DOWN":
                go = "UP"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and go != "UP":
                go = "DOWN"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                go = ""
                print(snake_body)

    if go == "RIGHT":
        if x == 540:
            x = 0
        x += step
        snake_head = [x, y]
        snake_body.insert(0, snake_head)
        snake_body.pop()
        # print(snake_head)
    if go == "LEFT":
        if x == 20:
            x = 560
        x -= step
        snake_head = [x, y]
        snake_body.pop()
        snake_body.insert(0, snake_head)
        # print(snake_head)
    if go == "UP":
        if y == 20:
            y = 560
        y -= step
        snake_head = [x, y]
        snake_body.pop()
        snake_body.insert(0, snake_head)
        # print(snake_head)
    if go == "DOWN":
        if y == 540:
            y = 0
        y += step
        snake_head = [x, y]
        snake_body.pop()
        snake_body.insert(0, snake_head)
        # print(snake_head)

    draw_background()
    point = font.render(f"{int(len(snake_body) - 2)}", True, (255, 255, 255))
    screen.blit(point, (520, 600))
    for snake_block in snake_body:
        if snake_body.index(snake_block) == 0:
            # print("________", snake_block)
            SNAKE_COLOR = (0, 200, 0)
        else:
            SNAKE_COLOR = (0, 255, 0)
        pygame.draw.rect(screen, SNAKE_COLOR,
                         [snake_block[0] + int(snake_block[0] / 20), snake_block[1] + int(snake_block[1] / 20),
                          SIZE_BLOCK, SIZE_BLOCK])
    pygame.draw.rect(screen, (255, 0, 0), [apple[0] + int(apple[0] / 20), apple[1] + int(apple[1] / 20), SIZE_BLOCK, SIZE_BLOCK])
    if snake_body[0] == apple:
        snake_body.append(apple)
        print(apple)
        apple = [int(random.randint(2, 27)*20), int(random.randint(2, 27)*20)]
        apple_end = [int(random.randint(2, 27) * 20), int(random.randint(2, 27) * 20)]
        print(apple)
    pygame.draw.rect(screen, (0, 0, 255), [apple_end[0] + int(apple_end[0] / 20), apple_end[1] + int(apple_end[1] / 20), SIZE_BLOCK, SIZE_BLOCK])
    if snake_body[0] == apple_end:
        snake_body.pop()
        print(apple_end)
        apple_end = [int(random.randint(2, 27)*20), int(random.randint(2, 27)*20)]
        apple = [int(random.randint(2, 27) * 20), int(random.randint(2, 27) * 20)]
        print(apple_end)

    pygame.display.update()