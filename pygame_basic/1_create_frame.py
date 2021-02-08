import pygame
pygame.init() #초기화

#화면크기 설정
screen_width = 480  #가로(너비)
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("Game_Minseo")#게임이름 설정
#화면이 떴다 사라짐..<-설정한 부분이 아무것도 없기때문!
#이벤트 루프
running = True #게임 진행중?
while running:
    for event in pygame.event.get():#사용자가 입력을 하였는가?
        if event.type == pygame.QUIT: #창을 닫을때(x표시)
            running = False #그때 창을 종료하자
#pygame 종료
pygame.quit()
