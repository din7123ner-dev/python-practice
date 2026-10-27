import pygame
import random
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Auto move")
ball_x = 250
ball_y = 250
rect_x = 100
rect_y = 100
size_x = 30
size_y = 30
speed = 5
running = True
game_over = False

snake = []
for i in range(7):
    snake.append((ball_x+i*20,ball_y))

direction_x = 0
direction_y = 0
snake_update = 0
score = 0
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if not game_over:
                if event.key == pygame.K_UP:
                  direction_x = 0
                  direction_y = 0 - speed
                elif event.key == pygame.K_DOWN:
                 direction_x = 0
                 direction_y = speed
                elif event.key == pygame.K_LEFT:
                 direction_x = 0 - speed
                 direction_y = 0 
                elif event.key == pygame.K_RIGHT:
                 direction_x = speed
                 direction_y = 0
            else:
                if event.key == pygame.K_q:
                    running = False
                elif event.key == pygame.K_c:
                    ball_x = random.randint(20, 480)
                    ball_y = random.randint(20, 480)
                    direction_x = 0
                    direction_y = 0
                    snake = []
                    for i in range(7):
                        snake.append((ball_x - i*20,ball_y))
                    game_over = False
    if not game_over:
        ball_x += direction_x
        ball_y += direction_y
        snake_update += speed
        while snake_update >= 20:
            snake.insert(0,(ball_x,ball_y))
            snake.pop()
            snake_update += -20

    if(abs(ball_x - rect_x)<30 and abs(ball_y - rect_y)<30):
        rect_x = random.randint(20,480)
        rect_y = random.randint(20,480)
        if score < 12:
            size_x = 30 - score * 2
            size_y = 30 - score * 2
        else:
            size_x = 5
            size_y = 5
        score += 1
    screen.fill((20,60,20))
    if score > 15:
        speed = 20
    else:
        speed = score + 5
    # 蛇作る


    pygame.draw.circle(screen,(160,0,250),snake[6],11)
    pygame.draw.circle(screen,(0,40,250),snake[5],14)
    pygame.draw.circle(screen,(0,250,200),snake[4],16)
    pygame.draw.circle(screen,(0,250,0),snake[3],20)
    pygame.draw.circle(screen,(250,250,0),snake[2],23)
    pygame.draw.circle(screen,(250,120,0),snake[1],26)
    pygame.draw.circle(screen,(250,120,0),snake[0],26)

    head_x = snake[0][0]
    head_y = snake[0][1]

    pygame.draw.circle(screen,(255,0,0),(head_x,head_y),30)
    pygame.draw.circle(screen,(255,255,255),(head_x+20,head_y-19),6)
    pygame.draw.circle(screen,(255,255,255),(head_x-19,head_y-19),6)
    pygame.draw.circle(screen,(0,0,0),(head_x-18,head_y-18),3)
    pygame.draw.circle(screen,(0,0,0),(head_x+18,head_y-18),3)
    pygame.draw.rect(screen,(0,0,0),(head_x-12,head_y+10,25,2))
    font = pygame.font.SysFont(None,50)
    point_text = font.render(f"Score: {score}",True,(239,244,234))
    screen.blit(point_text,(30,30))
    # ゴール作る
    pygame.draw.rect(screen,(217,234,19),(rect_x,rect_y,size_x,size_y))
    font = pygame.font.SysFont(None,50)
    if(ball_x>500 or ball_x<0 or ball_y>500 or ball_y<0):
        game_over = True
    if game_over:
        font = pygame.font.SysFont(None,30)
        text = font.render("Game Over! (Q:quit, C:play again)",True,(239,244,234))
        screen.blit(text,(10,250))
    pygame.display.update()
    clock.tick(60)
pygame.quit()