import pygame
pygame.init() #초기화

#화면크기 설정
screen_width = 480  #가로(너비)
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("민서 최애게임")#게임이름 설정
#배경 이미지 불러오기
background = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//background.png")
#화면이 떴다 사라짐..<-설정한 부분이 아무것도 없기때문!
#이벤트 루프
running = True #게임 진행중?
while running:
    for event in pygame.event.get():# 어떠한 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창을 닫을때(x표시)
            running = False #그때 창을 종료하자
    screen.blit(background,(0,0))#배경그리기_(0,0)은 background 나타나는 위치  
    #참고#screen.fill((0,0,255))#rgb이용해서 배경색 채우기
    pygame.display.update()#게임화면 다시그리기_이걸로 계속 업데이트됨   
#pygame 종료
pygame.quit()
