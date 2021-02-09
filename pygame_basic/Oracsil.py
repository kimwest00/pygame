import pygame
pygame.init() #초기화

#화면크기 설정
screen_width = 480  #가로(너비)
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("민서 최애게임")#게임이름 설정
#배경 이미지 불러오기
background = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//gunchim_background.png")
#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//gunchim_character.png")
character = pygame.transform.scale(character, (70, 70))
character_size =  character.get_rect().size#이미지 크기를 가져옴
character_width = character_size[0]#캐릭터 가로크기
character_height = character_size[1]#캐릭터 가로크기

#캐릭터는 기본위치
character_x_pos = (screen_width / 2) - (character_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치하도록(가로)
character_y_pos = screen_height - character_height  #화면 하단부에 위치하도록(세로)
#git 정신차리자

running = True #게임 진행중?
while running:
    for event in pygame.event.get():# 어떠한 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창을 닫을때(x표시)
            running = False #그때 창을 종료하자
        if event.type == pygame.KEYDOWN:#키가 눌러졌냐?
            if event.key == pygame.K_LEFT:#캐릭터 왼쪽으로
                pass
            elif event.key ==pygame.K_RIGHT:#캐릭터 오른쪽으로
                pass
            elif event.key == pygame.K_UP:#캐릭터 위쪽으로
                pass
            elif event.key == pygame.K_DOWN:#캐릭터 아래쪽으로
                pass
    screen.blit(background,(0,0))#배경그리기_(0,0)은 background 나타나는 위치  
    screen.blit(character,(character_x_pos, character_y_pos))#캐릭터 그리기
    pygame.display.update()#게임화면 다시그리기_이걸로 계속 업데이트됨   
#pygame 종료
pygame.quit()
