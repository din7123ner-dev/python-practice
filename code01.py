import pygame
import random
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Move Hero")
hero_x = 250
hero_y = 250
rect_x = 100
rect_y = 100
hero_color = (244,67,54)
running = True

snake = []
for i in range(7):
    snake.append((hero_x+i*20,hero_y))

while running:
    moved = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.mod & pygame.KMOD_SHIFT:
                move = 100
            else:
                move = 20
            hero_color = (227,217,27)
            if event.key == pygame.K_UP:
                hero_y -= move
                moved = True
            elif event.key == pygame.K_DOWN:
                hero_y += move
                moved = True
            elif event.key == pygame.K_LEFT:
                hero_x -= move
                moved = True
            elif event.key == pygame.K_RIGHT:
                hero_x += move
                moved = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LSHIFT:
                speed = 20
            hero_color = (255,0,0)
    
    if moved:
        snake.insert(0,(hero_x,hero_y))
        snake.pop()

    if(abs(hero_x - rect_x)<30 and abs(hero_y - rect_y)<30):
        rect_x = random.randint(20,480)
        rect_y = random.randint(20,480)
    screen.fill((20,60,20))
    # 蛇作る


    pygame.draw.circle(screen,(160,0,250),snake[6],11)
    pygame.draw.circle(screen,(0,40,250),snake[5],14)
    pygame.draw.circle(screen,(0,250,200),snake[4],16)
    pygame.draw.circle(screen,(0,250,0),snake[3],20)
    pygame.draw.circle(screen,(250,250,0),snake[2],23)
    pygame.draw.circle(screen,(250,120,0),snake[1],26)

    head_x = snake[0][0]
    head_y = snake[0][1]

    pygame.draw.circle(screen,hero_color,(head_x,head_y),30)
    pygame.draw.circle(screen,(255,255,255),(head_x+20,head_y-19),6)
    pygame.draw.circle(screen,(255,255,255),(head_x-19,head_y-19),6)
    pygame.draw.circle(screen,(0,0,0),(head_x-18,head_y-18),3)
    pygame.draw.circle(screen,(0,0,0),(head_x+18,head_y-18),3)
    pygame.draw.rect(screen,(0,0,0),(head_x-12,head_y+10,25,2))
    # ゴール作る
    pygame.draw.rect(screen,(217,234,19),(rect_x,rect_y,30,30))
    font = pygame.font.SysFont(None,50)
    if(hero_x>500 or hero_x<0 or hero_y>500 or hero_y<0):
        font = pygame.font.SysFont(None,50)
        text = font.render("GAME OVER!",True,(239,244,234))
        screen.blit(text,(150,250))
    pygame.display.update()
    
pygame.quit()