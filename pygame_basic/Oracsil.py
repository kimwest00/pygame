import pygame
pygame.init() #초기화

#화면크기 설정
screen_width = 480  #가로(너비)
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("민서 최애게임")#게임이름 설정
#FPS(화면속도 설정_Frame Per Seconds)
clock = pygame.time.Clock()#대문자로 안써주면 atrribte error 남
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
#이동할 좌표
to_x = 0
to_y = 0
#이동속도
character_speed = 10

running = True #게임 진행중?
while running:
    dt = clock.tick(60)#게임화면 초당 프레임수 설정

    #캐릭터가 100만큼 이동해야한다 치자
    #10프레임: 1초동안 10번 동작 -> 10만큼 이동하면됨
    #20 프레임: 1초동안 20번 동작 -> 5만큼 이동해야함



    print("fps: "+str(clock.get_fps()))
    for event in pygame.event.get():# 어떠한 이벤트가 발생하였는가?
        if event.type == pygame.QUIT: #창을 닫을때(x표시)
            running = False #그때 창을 종료하자
        if event.type == pygame.KEYDOWN:#키가 눌러졌냐?
            if event.key == pygame.K_LEFT:#캐릭터 왼쪽으로
                to_x -= character_speed
            elif event.key ==pygame.K_RIGHT:#캐릭터 오른쪽으로
                to_x +=character_speed
            elif event.key == pygame.K_UP:#캐릭터 위쪽으로
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:#캐릭터 아래쪽으로
                to_y += character_speed
        #방향키를 땠을때(누르지않을때는 멈추도록(=이동변수가 없도록))
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0
    character_x_pos += to_x
    character_y_pos += to_y
    #가로경계값(캐릭터가 화면밖에 나가지 못하도록)
    if character_x_pos <0:
        character_x_pos =screen_width - character_width
        character_x_pos =screen_width - character_width
    #세로경계값

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos>screen_height-character_height:
        character_y_pos = screen_height

    screen.blit(background,(0,0))#배경그리기_(0,0)은 background 나타나는 위치  
    screen.blit(character,(character_x_pos, character_y_pos))#캐릭터 그리기
    pygame.display.update()#게임화면 다시그리기_이걸로 계속 업데이트됨   
#pygame 종료
pygame.quit()
