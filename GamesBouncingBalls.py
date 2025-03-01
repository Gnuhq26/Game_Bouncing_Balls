import pygame

pygame.init
WIDTH = 800  #toa do x
HEIGHT = 800 #toa do y
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
CIRCLE_CENTER = [WIDTH/2, HEIGHT/2]
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
ball_pos_start = [WIDTH/2, HEIGHT/2 - 120]

running = True
GRAVITY = 0.2
ball_vel = [0, 0]  #van toc cua ball 

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    ball_vel[1] += GRAVITY
    ball_pos_start[0] += ball_vel[0]
    ball_pos_start[1] += ball_vel[1]
    window.fill(BLACK)
    pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
    pygame.draw.circle(window, RED, ball_pos_start, BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit