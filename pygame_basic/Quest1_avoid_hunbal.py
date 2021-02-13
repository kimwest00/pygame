import pygame
import random
pygame.init()


#화면크기 설정
screen_width = 480  #가로(너비)
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))
#화면 타이틀 설정
pygame.display.set_caption("군침이 터졌어요!")

background = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//gunchim_background.png")
#캐릭터(스프라이트) 불러오기
character = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//gunchim_character.png")
character = pygame.transform.scale(character, (70, 70))
character_size =  character.get_rect().size#이미지 크기를 가져옴
character_width = character_size[0]#캐릭터 가로크기
character_height = character_size[1]#캐릭터 가로크기
#캐릭터는 기본위치
character_x_pos = (screen_width / 2) - (character_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치하도록(가로)
character_y_pos = screen_height - character_height #화면 하단부에 위치하도록(세로)
#이동할 좌표
to_x = 0
to_y = 0

enemy = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//hunbal_enemy.png")
enemy = pygame.transform.scale(enemy, (70, 70))
enemy_size =  enemy.get_rect().size#이미지 크기를 가져옴
enemy_width = enemy_size[0]#캐릭터 가로크기
enemy_height = enemy_size[1]#캐릭터 가로크기

#캐릭터는 기본위치
enemy_x_pos = random.randint(0, screen_width) #화면 가로의 절반크기에 해당하는 곳에 위치하도록(가로)
enemy_y_pos = enemy_height/2 #화면 하단부에 위치하도록(세로)

#FPS(화면속도 설정_Frame Per Seconds)
clock = pygame.time.Clock()
character_speed = 0.6#속도 설정
enemy_speed = 0.4#적 투하속도 조정

start_ticks = pygame.time.get_ticks()#시작 시간 정보(tick)을 받아옴

running = True #게임 진행중?
while running:
##########################################################
    dt = clock.tick(60)#fps 설정
    
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x=0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y=0        

    #가로경계값(캐릭터가 화면밖에 나가지 못하도록)
    if character_x_pos <0:
        character_x_pos =screen_width - character_width
        character_x_pos =screen_width - character_width
    #세로경계값

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos>screen_height-character_height:
        character_y_pos = screen_height

    #enemy와 충돌처리

    character_rect =character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos#enemy가 고정은 되어있지만rect에 저장해준적이없어서
    enemy_rect.top = enemy_y_pos#해당 코드를 적어준다

    #충돌체크
    if(character_rect.colliderect(enemy_rect)):
        running = False

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    enemy_y_pos += dt * enemy_speed
    if enemy_y_pos >= screen_height - enemy_height:
        enemy_x_pos = random.randint(0, screen_width) #화면 가로의 절반크기에 해당하는 곳에 위치하도록(가로)
        enemy_y_pos = enemy_height #화면 하단부에 위치하도록(세로)
    screen.blit(background, (0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    
    pygame.display.update()#게임화면 다시그리기_이걸로 계속 업데이트됨  


pygame.quit()