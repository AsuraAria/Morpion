import pygame

def play (case):
    print(case)
    if case[1]<=260:
        if case[0]<=260:
            return 1
        elif 270<=case[0]<=530:
            return 2
        elif 540<=case[0]:
            return 3
        else:
            return 0
    elif 270<=case[1]<=530:
        if case[0]<=260:
            return 4
        elif 270<=case[0]<=530:
            return 5
        elif 540<=case[0]:
            return 6
        else:
            return 0
    elif 540<=case[1]:
        if case[0]<=260:
            return 7
        elif 270<=case[0]<=530:
            return 8
        elif 540<=case[0]:
            return 9
        else:
            return 0
    else:
        return 0

pygame.init()
pygame.display.set_caption('Fluffy Morpion')

grille = pygame.display.set_mode((800,800))
run = True
clock=pygame.time.Clock()
pygame.draw.line(grille,(255,255,255),(0,265),(800,265),10)
pygame.draw.line(grille,(255,255,255),(0,535),(800,535),10)
pygame.draw.line(grille,(255,255,255),(265,0),(265,800),10)
pygame.draw.line(grille,(255,255,255),(535,0),(535,800),10)
pygame.display.flip()
while run :
    clock.tick(60)
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if pygame.mouse.get_pressed() == (1,0,0) :
               print(play(pygame.mouse.get_pos()))
            
pygame.quit()