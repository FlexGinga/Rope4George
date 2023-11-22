import pygame


class Point:
    def __init__(self, x_y, prev_x_y=None, locked=0):
        self.x, self.y = x_y
        if prev_x_y is None:
            self.prev_x, self.prev_y = float(self.x), float(self.y)
        else:
            self.prev_x, self.prev_y = prev_x_y
        self.locked = locked

    def update(self, dt, gravity, friction, end=0):
        if not self.locked:
            dx = (self.x - self.prev_x) * friction
            dy = (self.y - self.prev_y) * friction
            if end:
                dy += gravity * dt / 1.5
            else:
                dy += gravity * dt / 5

            self.prev_x, self.prev_y = float(self.x), float(self.y)
            self.x += dx
            self.y += dy

    def draw(self, win: pygame.Surface):
        pygame.draw.circle(win, (255, 255, 255), (self.x, self.y), 2)
