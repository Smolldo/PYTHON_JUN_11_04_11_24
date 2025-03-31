import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
running = True

image = pygame.image.load(r'D:\programming\PYTHON_JUN_11_04_11_24\MGS2_Solid_Snake.png')

x, y = 100, 100
speed = 1

obstacle = pygame.Rect(300, 300, 50, 50)


alpha = 0
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
       y -= speed
    if keys[pygame.K_s]:
        y += speed
    if keys[pygame.K_a]:
        x -= speed
    if keys[pygame.K_d]:
        x += speed 

    if pygame.Rect(x, y, 50, 50).colliderect(obstacle):
        if keys[pygame.K_w]:
            y += speed
        if keys[pygame.K_s]:
            y -= speed
        if keys[pygame.K_a]:
            x += speed
        if keys[pygame.K_d]:
            x -= speed 

    screen.fill((255,255,255))
    pygame.draw.rect(screen, (0, 128, 255), (x, y, 50, 50))
    pygame.draw.rect(screen, (255, 0, 0), obstacle)
    pygame.display.flip()

    # alpha += 5
    # if alpha > 255:
    #     alpha = 0
    # image_copy = image.copy()
    # image_copy.fill((255,0,0, 180), special_flags= pygame.BLEND_RGBA_MULT)

    # screen.fill((0,0,0))
    # scaled_image = pygame.transform.scale(image, (500, 900))
    # rotated_image = pygame.transform.rotate(scaled_image, 90)

    # rotated_image.set_alpha(alpha)

    # screen.blit(image_copy, (100,100))
    # pygame.display.flip()



pygame.quit()