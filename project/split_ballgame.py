import os
import pygame
pygame.init()

screen_width = 480  #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))




pygame.display.set_caption("군침이 폭발해요")
clock = pygame.time.Clock()

current_path = os.path.dirname(__file__)#현재 파일의 위치
image_path= os.path.join(current_path, 'images')#image위치 반환

background = pygame.image.load(pygame.image.load(os.path.join(image_path,"gunchim_background.png")))
character = pygame.image.load(pygame.image.load(os.path.join(image_path,"gunchim_character")))
character = pygame.transform.scale(character, (70, 70))
character_size =  character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2  - character_width/2
character_y_pos = screen_height-character_height

enemy = pygame.image.load(pygame.image.load(os.path.join(image_path,"hunbal_enemy")))
enemy = pygame.transform.scale(enemy, (50, 50))
enemy_size =  enemy.get_rect().size#이미지 크기를 가져옴
enemy_width = enemy_size[0]#캐릭터 가로크기
enemy_height = enemy_size[1]#캐릭터 가로크기
enemy_x_pos = (screen_width / 2) - (enemy_width/2) #화면 가로의 절반크기에 해당하는 곳에 위치하도록(가로)
enemy_y_pos = (screen_height/2) - (enemy_height/2)  #화면 하단부에 위치하도록(세로)
to_x = 0

running = True
while running:
    dt = clock.tick(60)#게임화면 초당 프레임수 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창을 닫을때(x표시)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= dt
            elif event.key == pygame.K_RIGHT:
                to_x += dt

        if event.type == pygame.KEYUP:
            to_x = 0
        
    character_x_pos += to_x
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width-character_width :
        character_x_pos = screen_width-character_width

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    screen.blit(enemy,(enemy_x_pos,enemy_y_pos))
    pygame.display.update()

pygame.quit()
