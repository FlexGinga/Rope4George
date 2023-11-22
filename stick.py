import pygame
from math import sqrt


def distance(p0, p1):
    return sqrt((p1.x - p0.x) ** 2 + (p1.y - p0.y) ** 2)


class Stick:
    def __init__(self, p0, p1):
        self.p0, self.p1 = p0, p1
        self.length = distance(p0, p1)

    def update(self):
        dx = self.p1.x - self.p0.x
        dy = self.p1.y - self.p0.y
        _distance = sqrt(dx ** 2 + dy ** 2)
        difference = self.length - _distance
        percent = difference / _distance / 2
        offset_x = dx * percent
        offset_y = dy * percent

        if not self.p0.locked:
            self.p0.x -= offset_x
            self.p0.y -= offset_y
        if not self.p1.locked:
            self.p1.x += offset_x
            self.p1.y += offset_y

    def draw(self, win: pygame.Surface):
        pygame.draw.line(win, (10, 10, 10), (self.p0.x, self.p0.y), (self.p1.x, self.p1.y), 4)
