import pygame
from rope import Rope
from time import time

win = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

rope = Rope((500, 200), (1000, 300), 50, 1)

prev_time = time()
while 1:
    now = time()
    dt = now - prev_time
    prev_time = now

    pygame.event.clear()

    rope.update(dt, 8, 1, 50)

    win.fill((255, 20 ,20))
    rope.draw(win)
    pygame.display.flip()
