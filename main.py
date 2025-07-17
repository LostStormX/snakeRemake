import time
from asyncio import wait_for

import pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Snake Remake - V 1.0.0")
pygame.display.set_icon(pygame.image.load("Logo.png"))

clock = pygame.time.Clock()
running = True
deltaTime = 0
speed = 0.1
score = 0

player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("#009b34")

    # Text
    font = pygame.font.SysFont("Arial", 30, True,False)
    textSurface = font.render("Score:", False, ("black"))


    # Draw the player obj
    player = pygame.Rect(player_pos.x, player_pos.y,30,30)
    player.centerx = player_pos.x
    player.centery = player_pos.y

    # Draw the boundaries
    boundary = pygame.Rect(0,0,700,500)\

    # Collission
    collide = boundary.colliderect(player)
    if collide:
        score += 1
        print(score)


    keys = pygame.key.get_pressed()

    forward = False
    backward = False
    left = False
    right = False

    # Implementing Arrow Keys
    if keys[pygame.K_UP]:
        forward = True
        backward = False
        left = False
        right = False

    if keys[pygame.K_DOWN]:
        forward = False
        backward = True
        left = False
        right = False

    if keys[pygame.K_LEFT]:
        forward = False
        backward = False
        left = True
        right = False

    if keys[pygame.K_RIGHT]:
        forward = False
        backward = False
        left = False
        right = True

    while forward:
        player_pos.y -= speed * deltaTime
        time.sleep(5)

    while backward:
        player_pos.y += speed * deltaTime
        time.sleep(5)

    while left:
        player_pos.x -= speed * deltaTime
        time.sleep(5)

    while right:
        player_pos.x += speed * deltaTime
        time.sleep(5)

    # Render Shapes
    pygame.draw.rect(screen, "#006c24", player)
    pygame.draw.rect(screen, "#006c24", boundary, 35)

    # Render text
    screen.blit(textSurface,(280, 0))


    pygame.display.flip()
    deltaTime = clock.tick(30)

pygame.quit()