import pygame
import random


pygame.init()


screen_width = 660
screen_height = 290
screen = pygame.display.set_mode((screen_width, screen_height))


clock = pygame.time.Clock()


pygame.display.set_caption("몬티홀의 역설 ㄷ")


#문 정의
DoorClose = pygame.image.load("pygame/source/MTH/DoorClose.png")
DoorOpen = pygame.image.load("pygame/source/MTH/DoorOpen.png")
DoorOpenInGoat = pygame.image.load("pygame/source/MTH/DoorOpenInGoat.png")
ChoiceDoor = pygame.image.load("pygame/source/MTH/ChoiceDoor.png")

Door_1 = DoorClose
Door_2 = DoorClose
Door_3 = DoorClose

Door_size = DoorOpen.get_rect().size
Door_width = Door_size[0]
Door_height = Door_size[1]

Door1_xPos = 0
Door2_xPos = (screen_width / 2) - (Door_width / 2)
Door3_xPos = screen_width - Door_width

Door_yPos = screen_height - Door_height

Door1_rect = pygame.Rect(Door1_xPos, Door_yPos, Door_width , Door_height)
Door2_rect = pygame.Rect(Door2_xPos, Door_yPos, Door_width , Door_height)
Door3_rect = pygame.Rect(Door3_xPos, Door_yPos, Door_width , Door_height)


#마우스 원 정의
circle_size = 5

circle_xPos = 0
circle_yPos = 0

circle_rect = pygame.Rect(circle_xPos, circle_yPos, circle_size * 2, circle_size * 2)
circle_rect.center = (circle_xPos, circle_yPos)


#변수
Choice_Num = 0
Choice_State = 0
Pop_State = 0
Goat_Pos = random.randint(0, 2)
Non_Goat = [1, 2, 3]
Non_Goat.pop(Goat_Pos)


# print(Non_Goat)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEMOTION:
            # Mouse_Pos = pygame.mouse.get_pos()
            circle_xPos, circle_yPos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if circle_rect.colliderect(Door1_rect):
                if Choice_State == 0:
                    Choice_Num = 1
                    Door_1 = ChoiceDoor
            elif circle_rect.colliderect(Door2_rect):
                if Choice_State == 0:
                    Choice_Num = 2
                    Door_2 = ChoiceDoor
            elif circle_rect.colliderect(Door3_rect):
                if Choice_State == 0:
                    Choice_Num = 3
                    Door_3 = ChoiceDoor
            if Choice_Num in Non_Goat:
                Non_Goat.remove(Choice_Num)
            # print(Non_Goat)
            
        
        if event.type == pygame.MOUSEBUTTONUP:
            # print(Choice_Num)
            Choice_State = 1
            if Pop_State == 0:
                OpenDoor = Non_Goat[0]
            # print(OpenDoor)
                if OpenDoor == 1:
                    Door_1 = DoorOpen
                elif OpenDoor == 2:
                    Door_2 = DoorOpen
                elif OpenDoor == 3:
                    Door_3 = DoorOpen
                Last_Door = [1, 2, 3]
                Last_Door.remove(OpenDoor)
                # print(Last_Door)
                Change_Door = [Last_Door[0], Last_Door[1]]
                Change_Door.remove(Choice_Num)
                # print(Last_Door)
            Pop_State =  1
        if event.type == pygame.KEYDOWN:
            if Pop_State == 1:
                if event.key == pygame.K_c:
                    if Choice_Num == 1:
                        Door_1 = DoorClose
                    elif Choice_Num == 2:
                        Door_2 = DoorClose
                    elif Choice_Num == 3:
                        Door_3 = DoorClose

                    if Change_Door == [1]:
                        Door_1 = ChoiceDoor
                    elif Change_Door == [2]:
                        Door_2 = ChoiceDoor
                    elif Change_Door == [3]:
                        Door_3 = ChoiceDoor
                        

                if event.key == pygame.K_SPACE:
                    # print(Last_Door)
                    if Last_Door == [1, 2]:
                        Door_1 = DoorOpen
                        Door_2 = DoorOpen
                    elif Last_Door == [1, 3]:
                        Door_1 = DoorOpen
                        Door_3 = DoorOpen
                    elif Last_Door == [2, 3]:
                        Door_2 = DoorOpen
                        Door_3 = DoorOpen

                    if Goat_Pos == 0:
                        Door_1 = DoorOpenInGoat
                    elif Goat_Pos == 1:
                        Door_2 = DoorOpenInGoat
                    elif Goat_Pos == 2:
                        Door_3 = DoorOpenInGoat
        

    circle_rect = pygame.Rect(circle_xPos, circle_yPos, circle_size * 2, circle_size * 2)
    circle_rect.center = (circle_xPos, circle_yPos)



    screen.fill((255, 255, 255))
    screen.blit(Door_1, (Door1_xPos, Door_yPos))
    screen.blit(Door_2, (Door2_xPos, Door_yPos))
    screen.blit(Door_3, (Door3_xPos, Door_yPos))

    pygame.draw.circle(screen, (255, 174, 201), (circle_xPos, circle_yPos), circle_size)

    pygame.display.update()

pygame.quit()