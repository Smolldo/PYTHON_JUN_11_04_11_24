# import pygame
# # import random
# pygame.init()

# screen = pygame.display.set_mode((900,900))

# # def rand_color():
# #     return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

# # color = rand_color()

# x, y = 300, 400
# speed = 50

# square = pygame.Rect(350, 250, 100, 100)
# dragging = False

# running = True

# while running:
#     keys = pygame.key.get_pressed()
#     # pygame.draw.circle(screen, color, (450,450), 20)
#     # pygame.display.flip()


#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False

#         elif e.type == pygame.MOUSEBUTTONDOWN:
#             if square.collidepoint(e.pos):
#                 dragging = True
#                 mouse_x, mouse_y = e.pos
#                 offset_x = square.x - mouse_x
#                 offset_y = square.y - mouse_y

#         elif e.type == pygame.MOUSEBUTTONUP:
#             dragging = False

#         elif e.type == pygame.MOUSEMOTION:
#             if dragging:
#                 mouse_x, mouse_y = e.pos
#                 square.x = mouse_x + offset_x
#                 square.y = mouse_y + offset_y

#     screen.fill((255, 255, 255))
#     pygame.draw.rect(screen, (0, 128, 255), square)
#     pygame.display.flip()

#         # elif e.type == pygame.MOUSEBUTTONDOWN:
#         #     if e.button == 1:
#         #         print('натиснута ЛКМ')
#         #     elif e.button == 2:
#         #         print('натиснуто СКМ')
#         # elif e.type == pygame.MOUSEMOTION:
#         #     mouse_pos = e.pos
#         #     print(f'mouse pos: {mouse_pos}')

         
    
#         # if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
#         #     if keys[pygame.K_c]:
#         #         print('була комбінація Ctrl + C')

        
#         # elif e.type == pygame.KEYDOWN:
#         #     if e.key == pygame.K_UP:
#         #         # print('натиснуто стрілку вгору')
#         #         y -= speed
#         #     elif e.key == pygame.K_DOWN:
#         #         # print('натиснуто стрілку вниз')
#         #         y += speed
#         #     elif e.key == pygame.K_LEFT:
#         #         # print('натиснуто стрілку вліво')
#         #         x -= speed
#         #     elif e.key == pygame.K_RIGHT:
#         #         # print('натиснуто стрілку вправо')
#         #         x += speed

#     # screen.fill((0,0,0))
#     # pygame.draw.rect(screen, (255,0,0), (x, y, 50, 50))
#     # pygame.display.flip()

#         # elif e.type == pygame.KEYDOWN:
#         #     if e.key == pygame.K_SPACE:
#         #         color = rand_color()

        


# pygame.quit()

import pygame
import random

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Line')

running = True

def randcolor():
    return(random.randint(0,255), random.randint(0,255), random.randint(0,255))

color = randcolor()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                color = randcolor()

    # screen.fill((75,75,75))
    # pygame.draw.rect(screen, (0, 255, 0), (40, 40, 40, 40), 5)
    # pygame.draw.rect(screen, (0, 255, 0), (40, 100, 40, 40), 5)
    # pygame.draw.rect(screen, (0, 255, 0), (40, 150, 40, 40), 5)
    # pygame.draw.rect(screen, (0, 255, 0), (40, 200, 40, 40), 5)
    pygame.draw.circle(screen, color, (450 , 450), 12)
    pygame.display.flip()


    
            

        
pygame.quit()