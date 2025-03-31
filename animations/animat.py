import pygame
import sys

pygame.init()

screen = pygame.display.set_mode((800,600))

# WHITE = (255,255,255)
# GREEN = (0, 255, 0)
# RED = (255, 0, 0)
# BLUE = (0, 0, 255)
# YELLOW = (255, 255, 0)

# player = pygame.Rect(100,100, 50, 50)
# obstacle = pygame.Rect(300, 300, 50, 50)
# goal = pygame.Rect(600, 400, 50, 50)

# speed = 1
# score = 0

# running = True

# while running:
#     for e in pygame.event.get():
#         if e.type == pygame.QUIT:
#             running = False
    
#     keys = pygame.key.get_pressed()
#     if keys[pygame.K_LEFT]:
#         player.x -= speed
#     if keys[pygame.K_RIGHT]:
#         player.x += speed
#     if keys[pygame.K_UP]:
#         player.y -= speed
#     if keys[pygame.K_DOWN]:
#         player.y += speed

#     if player.colliderect(obstacle):
#         player.x, player.y = 100, 100
#         score = 0
#     elif player.colliderect(goal):
#         goal.x, goal.y = 700, 500
#         score += 1

#     screen.fill(WHITE)
#     pygame.draw.rect(screen, GREEN, player)
#     pygame.draw.rect(screen, RED, obstacle)
#     pygame.draw.rect(screen, YELLOW, goal)

#     font = pygame.font.Font(None, 36)
#     text = font.render(f'SCORE: {score}', True, BLUE)
#     screen.blit(text, (10,10))

#     pygame.display.flip()


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]
color_index = 0

# x = 0
# y = 300
# speed = 5


clock = pygame.time.Clock()
fps = 60

ANIMATION_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ANIMATION_EVENT, 1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == ANIMATION_EVENT:
            color_index = (color_index + 1) % len(colors)




    screen.fill(WHITE)

    pygame.draw.rect(screen, colors[color_index], (300, 200, 200, 200))
    # x += speed
    # if x > 800:
    #     x = -50

    pygame.display.flip()
    clock.tick(fps)

# pygame.time.set_timer(MOVE_EVENT, 500)


pygame.quit()


    