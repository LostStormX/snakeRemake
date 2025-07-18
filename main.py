import time
from asyncio import wait_for

import pygame

pygame.init()
screen = pygame.display.set_mode((700, 500))

pygame.display.set_caption("Snake Remake - V 1.0.0")
pygame.display.set_icon(pygame.image.load("Logo.png"))

clock = pygame.time.Clock()
run = True

deltaTime = 0
speed = 5
score = 0
length = 1
gameOver = False

direction = pygame.Vector2(0,0)

player_pos = pygame.Vector2(screen.get_width() / 2 , screen.get_height() / 2)

while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            print(pygame.key.name(event.key))
            if event.key == pygame.K_UP:
                print(pygame.key.name(event.key))
            if event.key == pygame.K_ESCAPE:
                run = False

    screen.fill("#009b34")

    # Text
    font = pygame.font.SysFont("Arial", 25, True,False)
    gFont = pygame.font.SysFont("Arial", 40, True,False)

    scoreText = font.render("Score: " + str(score), False, "black")
    endgameText = gFont.render("GAME OVER", False, "black")


    # Draw the player obj
    player = pygame.Rect(player_pos.x, player_pos.y,30,30)
    player.centerx = player_pos.x
    player.centery = player_pos.y

    boundaryR = pygame.Rect(670,0,30, screen.get_height())
    boundaryL = pygame.Rect(0,0,30, screen.get_height())
    boundaryU = pygame.Rect(30,0, screen.get_width() - 60,30)
    boundaryD = pygame.Rect(30, 470, screen.get_width() - 60,30)

    # Collisions
    collideU = boundaryU.colliderect(player)
    collideD = boundaryD.colliderect(player)
    collideR = boundaryR.colliderect(player)
    collideL = boundaryL.colliderect(player)

    if collideU or collideD or collideR or collideL:
        gameOver = True

    if gameOver:
        direction = pygame.Vector2(0, 0)
        speed = 0

        screen.blit(scoreText, (screen.get_width() / 2 - 40, screen.get_height() / 2 - 10))
        screen.blit(endgameText, (screen.get_width() / 2 - 110, screen.get_height() / 2 - 50))

    # Implementing Arrow Keys
    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and direction.y == 0:
        direction = pygame.Vector2(0, -1)
    if keys[pygame.K_DOWN] and direction.y == 0:
        direction = pygame.Vector2(0, 1)
    if keys[pygame.K_LEFT] and direction.x == 0:
        direction = pygame.Vector2(-1, 0)
    if keys[pygame.K_RIGHT] and direction.x == 0:
        direction = pygame.Vector2(1, 0)


    player_pos += direction * speed

    # Render Shapes
    pygame.draw.rect(screen, "#006c24", player)

    pygame.draw.rect(screen, "#006c24", boundaryL)
    pygame.draw.rect(screen, "#006c24", boundaryR)
    pygame.draw.rect(screen, "#006c24", boundaryU)
    pygame.draw.rect(screen, "#006c24", boundaryD)

    # Render text
    screen.blit(scoreText, (30, 0))

    pygame.display.flip()
    deltaTime = clock.tick(30)

pygame.quit()