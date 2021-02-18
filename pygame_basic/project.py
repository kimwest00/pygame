import pygame
pygame.init()

screen_width = 480  #가로
screen_height = 640 #세로
screen = pygame.display.set_mode((screen_width,screen_height))
background = pygame.image.load("C://Users//김민서//OneDrive - 한국외국어대학교//바탕 화면//게임//Pygame//gunchim_background.png")

pygame.display.set_caption("군침이 폭발해요")



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #창을 닫을때(x표시)
            running = False
    screen.blit(background,(0,0))
    pygame.display.update()

pygame.quit()
