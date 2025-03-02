import pygame
import numpy as np
import math

def draw_arc(window, center, radius, start_angle, end_angle):
    p1 = center + (radius) * np.array([math.cos(start_angle), math.sin(start_angle)])
    p2 = center + (radius) * np.array([math.cos(end_angle), math.cos(end_angle)])
    pygame.draw.polygon(window, RED, [center, p1, p2], 0)


pygame.init
WIDTH = 800  #toa do x
HEIGHT = 800 #toa do y
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
CIRCLE_CENTER = np.array([WIDTH/2, HEIGHT/2], dtype = np.float64)
CIRCLE_RADIUS = 150
BALL_RADIUS = 5
ball_pos = np.array([WIDTH/2, HEIGHT/2 - 120], dtype = np.float64)

running = True
GRAVITY = 0.2
ball_vel = np.array([0, 0], dtype = np.float64)  #van toc cua ball 
arc_degrees = 60
start_angle = math.radians(-arc_degrees/2)
end_angle = math.radians(arc_degrees/2)

while running:
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            running = False
    ball_vel[1] += GRAVITY
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    dist = np.linalg.norm(ball_pos - CIRCLE_CENTER)
    if dist + BALL_RADIUS > CIRCLE_RADIUS:
        d = ball_pos - CIRCLE_CENTER
        d_unit = d/np.linalg.norm(d)
        ball_pos = CIRCLE_CENTER + (CIRCLE_RADIUS - BALL_RADIUS) * d_unit
        t = np.array([-d[1], d[0]], dtype = np.float64) #t la vecto vuong goc voi d
        proj_v_t = (np.dot(ball_vel, t)/np.dot(t, t)) * t #hinh chieu tu v xuong t
        ball_vel = 2 * proj_v_t - ball_vel #update van toc bong 

    window.fill(BLACK)
    pygame.draw.circle(window, ORANGE, CIRCLE_CENTER, CIRCLE_RADIUS, 3)
    pygame.draw.circle(window, RED, ball_pos, BALL_RADIUS)

    pygame.display.flip()
    clock.tick(60)

pygame.quit