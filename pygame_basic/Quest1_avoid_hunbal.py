import pygame

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
character_y_pos = screen_height - character_height  #화면 하단부에 위치하도록(세로)
#이동할 좌표
to_x = 0
to_y = 0

enemy = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//hunbal_enemy.png")
enemy = pygame.transform.scale(enemy, (70, 70))
enemy_size =  enemy.get_rect().size#이미지 크기를 가져옴
enemy_width = enemy_size[0]#캐릭터 가로크기
enemy_height = enemy_size[1]#캐릭터 가로크기

#캐릭터는 기본위치
enemy_x_pos = (screen_width / 2) - (enemy_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치하도록(가로)
enemy_y_pos = (screen_height/2) - (enemy_height/2)  #화면 하단부에 위치하도록(세로)

#FPS(화면속도 설정_Frame Per Seconds)
clock = pygame.time.Clock()
character_speed = 0.6#속도 설정


start_ticks = pygame.time.get_ticks()#시작 시간 정보(tick)을 받아옴

running = True #게임 진행중?
while running:
##########################################################
    dt = clock.tick(60)#fps 설정
    
    character_x_pos += to_x * dt
    character_y_pos += to_y * dt

    #3.이벤트 처리(키보드, 마우스에 따른)
    '''pygame.event.get()#발생한 이벤트
        pygame.QUIT , KEYDOWN ,K_LEFT'''
    #4. 게임 캐릭터 위치 정의
    #5. 충돌 처리 rect.colliderect()
    
    #6. 화면에 그리기 blit(출력대상,좌표)

    pygame.display.update()#게임화면 다시그리기_이걸로 계속 업데이트됨  

pygame.init()
pygame.quit()