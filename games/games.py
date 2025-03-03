# import pygame as p
# import time

# p.init()

# p.display.set_caption('Моя перша гра')
# screen = p.display.set_mode([800, 800])

# image = p.image.load('image.png')
# p.display.set_icon(image)

# screen.fill((0,0,255))
# p.display.flip()

# font = p.font.Font(None, 36)
# text = font.render('Дякую, що запустився', True, (255,255,255))
# screen.blit(text, (50,50))
# p.display.flip()

# time.sleep(5)

# p.quit()


import pygame
pygame.init()

screen = pygame.display.set_mode((800, 600))

running = True
x_position = 0 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), (x_position, 300, 50, 50))
    pygame.display.flip() 
    
    x_position += 5
    if x_position > 800:
        x_position = 0

    pygame.time.delay(50)

pygame.quit()