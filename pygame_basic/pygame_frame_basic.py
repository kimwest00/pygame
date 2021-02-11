import pygame
#########################################
#기본 초기화 반드시 써줘야하는것들
pygame.init() #초기화

#화면크기 설정
screen_width = 480  #가로(너비)
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀 설정
pygame.display.set_caption("게임이름")
#FPS(화면속도 설정_Frame Per Seconds)
clock = pygame.time.Clock()

##############################################################

'''
1. 사용자 게임 초기화(배경화면, 게임이미지, 위치, 속도, 폰트,...)
#배경 이미지 불러오기 image.load
#transform.scale(),get_rect().size
#폰트 = font.Font(글씨체,크기)
2. while 반복문으로 이벤트
'''
running = True #게임 진행중?
while running:
##########################################################
    dt = clock.tick(60)#fps 설정

    #3.이벤트 처리(키보드, 마우스에 따른)
    '''pygame.event.get()#발생한 이벤트
        pygame.QUIT , KEYDOWN ,K_LEFT'''
    #4. 게임 캐릭터 위치 정의
    #5. 충돌 처리 rect.colliderect()
    
    #6. 화면에 그리기 blit(출력대상,좌표)

    pygame.display.update()#게임화면 다시그리기_이걸로 계속 업데이트됨  


#pygame 종료
pygame.quit()
