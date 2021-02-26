import pygame
import os
pygame.init() #초기화


screen_width = 480  #가로(너비)
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임이름")
#FPS(화면속도 설정_Frame Per Seconds)
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)
image_path = os.path.join(current_path,"images")

background = pygame.image.load(os.path.join(image_path,"gunchim_background.png"))

running = True #게임 진행중?
while running:

    dt = clock.tick(60)#fps 설정
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창을 닫을때(x표시)
            running = False
    
    screen.blit(background,(0,0))
    pygame.display.update()

#pygame 종료
pygame.quit()
