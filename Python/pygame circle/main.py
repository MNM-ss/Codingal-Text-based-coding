import pygame

pygame.init()

window = pygame.display.set_mode((400, 400))
window.fill((255, 255, 255))

GREEN = (0, 255, 0)
pygame.draw.circle(window, GREEN, (300, 300), 50)
#hollow
pygame.draw.circle(window, GREEN, (100, 100), 50, 3)
pygame.display.update()
# game loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
#quit
pygame.quit()
