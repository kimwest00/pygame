import pygame
pygame.init()

screen_width = 480  #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//gunchim_background.png")
character = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//gunchim_character.png")
character = pygame.transform.scale(character, (70, 70))
character_size =  character.get_rect().size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = screen_width/2  - character_width/2
character_y_pos = screen_height-character_height
pygame.display.set_caption("군침이 폭발해요")

to_x = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창을 닫을때(x표시)
            running = False
        if event.type == pygame.KEYDOWN:
            if event.type == pygame.K_LEFT:
                to_x -= 15
            elif event.type == pygame.K_RIGHT:
                to_x += 15

        if event.type == pygame.KEYUP:
            to_x = 0
    character_x_pos += to_x

    screen.blit(background,(0,0))
    screen.blit(character,(character_x_pos,character_y_pos))
    pygame.display.update()

pygame.quit()
