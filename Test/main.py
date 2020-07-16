import pygame

"""
    FUNCTIONS
"""

def pos_to_case(pos):

    case = [0, 0]

    if pos[1] <= 260:
        case[0] = 0
    elif 270 <= pos[1] <= 530:
        case[0] = 1
    elif 540 <= pos[1]:
        case[0] = 2
    else:
        return [0, 0]

    if pos[0] <= 260:
        case[1] = 0
    elif 270 <= pos[0] <= 530:
        case[1] = 1
    elif pos[0] >= 540:
        case[1] = 2
    else:
        return [0, 0]

    return case


def fillcase(player, case):

    player = icon00
    grille.blit(player, (case[1]*270+30, case[0]*270+30))
    pygame.display.flip()
    tabs[case[0]][case[1]]="a"
    print(tabs[0])
    print(tabs[1])
    print(tabs[2])

def initPlay():
    tabs = [["", "", ""],
            ["", "", ""],
            ["", "", ""]]
    grille.fill((225, 225, 225))
    pygame.draw.line(grille, (0, 0, 0), (0, 265), (800, 265), 10)
    pygame.draw.line(grille, (0, 0, 0), (0, 535), (800, 535), 10)
    pygame.draw.line(grille, (0, 0, 0), (265, 0), (265, 800), 10)
    pygame.draw.line(grille, (0, 0, 0), (535, 0), (535, 800), 10)
    pygame.display.flip()
    player = ""


def est_gagnant(grille):
    """
        détection de gain de la partie @grille
    """

    for i in range(3):
        if (grille[i][0] == grille[i][1]) and (grille[i][1] == grille[i][2]) and (grille[i][0] != ""):
            return 1
        if (grille[0][i] == grille[1][i]) and (grille[1][i] == grille[2][i]) and (grille[0][i] != ""):
            return 1
    if (grille[0][0] == grille[1][1]) and (grille[1][1] == grille[2][2]) and (grille[1][1] != ""):
        return 1
    if (grille[0][2] == grille[1][1]) and (grille[1][1] == grille[2][0]) and (grille[1][1] != ""):
        return 1
    return 0


def est_match_nul(grille):
    """
        détection de match nul de la partie @grille
    """

    for i in range(3):
        for j in range(3):
            if (tabs[i][j] == ""):
                return 0
    return 1


"""
    INIT
"""

pygame.init()
pygame.display.set_caption('Fluffy Morpion')
grille = pygame.display.set_mode((800, 800))
tabs = [["", "", ""],
        ["", "", ""],
        ["", "", ""]]
player = ""

icon00 = pygame.image.load("Ressources\icon00.png")
icon01 = pygame.image.load("Ressources\icon01.png")
icon02 = pygame.image.load("Ressources\icon02.png")
icon03 = pygame.image.load("Ressources\icon03.png")
icon04 = pygame.image.load("Ressources\icon04.png")

icon00 = pygame.transform.scale(icon00, (200, 200))
icon01 = pygame.transform.scale(icon01, (200, 200))
icon02 = pygame.transform.scale(icon02, (200, 200))
icon03 = pygame.transform.scale(icon03, (200, 200))
icon04 = pygame.transform.scale(icon04, (200, 200))

initPlay()

"""
    RUN
"""

run = True
clock = pygame.time.Clock()

while run:
    clock.tick(60)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed() == (1, 0, 0):
                case = pos_to_case(pygame.mouse.get_pos())
                if (tabs[case[0]][case[1]] == ""):
                    fillcase(player, [case[0], case[1]])

            if(est_gagnant(tabs)):
                print("Victoire")
            elif (est_match_nul(tabs)):
                print("Match null")

        if pygame.mouse.get_pressed() == (0, 0, 1):
            initPlay()
pygame.quit()
