import pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))
clock = pygame.time.Clock()
running = True
deltaTime = 0

player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    # Draw the player obj
    pygame.draw.circle(screen, "green", player_pos, 20)

    # Key Strokes
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
       player_pos.y -= 1 * deltaTime
    if keys[pygame.K_DOWN]:
        player_pos.y += 1 * deltaTime
    if keys[pygame.K_LEFT]:
        player_pos.x -= 1 * deltaTime
    if keys[pygame.K_RIGHT]:
        player_pos.x += 1 * deltaTime

    pygame.display.flip()

    deltaTime = clock.tick(30)

pygame.quit()