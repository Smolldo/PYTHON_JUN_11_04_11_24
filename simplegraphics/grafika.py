import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('Line')

running = True

# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     screen.fill((75,75,75))
#     # pygame.draw.line(screen, (0,0,0), (100,100), (500,500), 8)
#     # pygame.draw.circle(screen, (0,0,255), (640, 360), 200, 99)
#     pygame.draw.rect(screen, (0, 255, 0), (150, 200, 500, 400), 5, 40)
#     pygame.display.flip()

sprite_image = pygame.image.load("MGS2_Solid_Snake.png")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = sprite_image
        self.rect = self.image.get_rect()
        self.rect.center = (400, 300)
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT]:
            self.rect.x += 5
        if keys[pygame.K_UP]:
            self.rect.y -= 5
        if keys[pygame.K_DOWN]:
            self.rect.y += 5

# Створення групи спрайтів та додавання нашого спрайта
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Оновлення спрайтів
    all_sprites.update()
    
    # Очищення екрану
    screen.fill((255, 255, 255))
    
    # Малювання спрайтів
    all_sprites.draw(screen)
    
    # Оновлення екрану
    pygame.display.flip()

# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         running = False
#     elif event == pygame.K_DOWN:
#         print('була натиснена клавіша dybp')

#     if event.type == pygame.KEYDOWN:
#         if event.mod & pygame.KMOD_CTRL and event.key == pygame.K_c:
#             print("Натиснуто Ctrl+C")
#         if event.mod & pygame.KMOD_SHIFT and event.key == pygame.K_SPACE:
#             print("Натиснуто Shift+Space")
#     elif event.type == pygame.MOUSEMOTION:
#         mouse_position = pygame.mouse.get_pos()
#         print("Позиція миші:", mouse_position)


pygame.quit()