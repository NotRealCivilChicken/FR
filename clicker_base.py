import pygame

pygame.init()

window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Fruit Master")

FRUIT_SIZE = 500
fr1 = pygame.image.load("D:\Coding\Python_game_dev_mc\Clicker\Assets\Free\Items\Fruits\Orange.png")
fr1_scaled = pygame.transform.scale(fr1, (FRUIT_SIZE, FRUIT_SIZE ))
fr1_scaled = pygame.transform.rotate(fr1_scaled, 90)
fr1_scaled = pygame.transform.flip(fr1_scaled, True, False)

click_timer = 0
score = 0

text_font = pygame.font.SysFont("Arial", 48)
def draw_text(txt, font, text_col, x, y):
    img = font.render(txt, True, text_col)
    window.blit(img, (x, y))

run = True
while run:
    pygame.time.delay(60)

    window.fill((181, 101, 29))

    draw_text(f"Score: {score}", text_font, (123, 63, 0), 20, 20)

    mouse_pos = pygame.mouse.get_pos()

    window.blit(fr1_scaled, (960 - FRUIT_SIZE//2, 540 - FRUIT_SIZE//2))
    
    #show the hit area
    #pygame.draw.circle(window, (255, 0, 0), (960, 540), FRUIT_SIZE//4, 2) 

    current_size = FRUIT_SIZE + (click_timer * 7)
    if click_timer > 0:
        click_timer -= 1
        fr1_animation = pygame.transform.scale(fr1, (current_size, current_size))
        fr1_animation = pygame.transform.rotate(fr1_animation, 90)
        fr1_animation = pygame.transform.flip(fr1_animation, True, False)
        window.fill((181, 101, 29))
        draw_text(f"Score: {score}", text_font, (123, 63, 0), 20, 20)
        window.blit(fr1_animation, (960 - FRUIT_SIZE//2, 540 - FRUIT_SIZE//2))
    else:
        window.blit(fr1_scaled, (960 - FRUIT_SIZE//2, 540 - FRUIT_SIZE//2))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
   
        if event.type == pygame.MOUSEBUTTONDOWN:
            dist = pygame.Vector2(mouse_pos).distance_to(pygame.Vector2(960, 540))
            if dist < FRUIT_SIZE//4:
                score += 1
                print("+1 point")
                print(mouse_pos)
            click_timer = 10

    pygame.display.update()    

pygame.quit()
