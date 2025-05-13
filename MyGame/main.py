from operator import ge
import pygame
import random
import os
from move import Move
from rotate import Rotate
from setting import Setting
from remove import Remove

#遊戲初始化
pygame.init()
pygame.mixer.init()
#創建視窗
screen = pygame.display.set_mode((WIDTH, HEIGHT))
#更改檔名
pygame.display.set_caption("TETRIS")
#創建物件(管理操控時間)
clock = pygame.time.Clock()

#創建類別物件
position = Position()
move = Move()
move.init()
rotate = Rotate()
break_line = Break()
break_line.init()

init = True

def draw_text(text, size, x, y):
    font_name = os.path.join("font.ttf")
    font = pygame.font.Font(font_name, size)
    #繪製文字(文字, 平滑值, 文字顏色, 背景顏色)
    TEXT = font.render(text, True, WHITE)
    TEXT_rect = TEXT.get_rect()
    TEXT_rect.centerx = x
    TEXT_rect.centery = y
    screen.blit(TEXT, TEXT_rect)



running = True

img = pygame.image.load(os.path.join("T_imgs", "level_1.jpg")).convert()
gameover_img = pygame.transform.scale(img, (200, 200))
icon = pygame.image.load(os.path.join("icon.png")).convert()
icon.set_colorkey(BLACK)
pygame.display.set_icon(icon)
pygame.mixer.music.load(os.path.join("T_sounds", "happytime.mp3"))
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.05)

get_score_sound = pygame.mixer.Sound(os.path.join("T_sounds", "score.mp3"))


while running:

    #1秒鐘內最多執行幾次
    clock.tick(FPS)

    while init == True:
        draw_text("TETRIS", 64, WIDTH//2, HEIGHT//2-100)
        draw_text("左右鍵移動 空白鍵直接落下 上鍵旋轉方塊", 32, WIDTH//2, HEIGHT//2)
        draw_text("按下任意鍵開始遊戲", 32, WIDTH//2, HEIGHT//2+100)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                init = False
                break
            if event.type == pygame.KEYUP:
                init = False
                break
            
    while move.gameover == True:
        screen.blit(gameover_img, (550, 200))
        draw_text("GAME OVER", 72, 650, 460)
        draw_text("按下任意鍵繼續遊戲", 32, 650, 550)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                move.gameover = False
            if event.type == pygame.KEYDOWN:
                move.init()
                break_line.init()

    #取得輸入
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN and move.gameover == False:
            #移動系統
            if event.key == pygame.K_SPACE:
                move.Go_Down = True
            if event.key == pygame.K_RIGHT:
                move.move("R") 
            if event.key == pygame.K_LEFT:
                move.move("L") 
            #旋轉系統
            if event.key == pygame.K_UP:
                rotate.rotate()
    
    #畫面顯示
    screen.fill(BLACK)
    
    #移動系統
    move.draw()
    for i, j in move.imgs:
        screen.blit(i, j)
    #消行系統
    break_line.break_judge()
    if break_line.score - break_line.score_old >= 80:
        break_line.score_old = break_line.score
        move.speed += 0.25
        break_line.level += 1
        
    draw_text(f"Score {break_line.score}", 32, 650, 100)
    draw_text(f"Level {break_line.level}", 32, 650, 150)

    #遊戲畫面顯示
    outline_rect = pygame.Rect(100, 50, BAR_WIDTH, BAR_HEIGHT)
    pygame.draw.rect(screen, LIGHT_GRAY, outline_rect, 2)
    for i in range(9):
        pygame.draw.line(screen, LIGHT_GRAY, (130+i*30, 50), (130+i*30, 648), 2)
    for i in range(19):
        pygame.draw.line(screen, LIGHT_GRAY, (100, 80+i*30), (398, 80+i*30), 2)
    
    pygame.display.update()
    
pygame.quit()