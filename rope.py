import pygame
from stick import Stick
from point import Point


class Rope:
    def __init__(self, start_pos, end_pos, num_segments, lock1=0):
        dx, dy = (end_pos[0] - start_pos[0]) / num_segments, (end_pos[1] - start_pos[1]) / num_segments
        self.points = []
        for i in range(num_segments):
            self.points.append(Point((start_pos[0] + dx * i, start_pos[1] + dy * i)))

        self.points[0].locked = lock1

        self.sticks = []
        for i in range(num_segments - 1):
            self.sticks.append(Stick(self.points[i], self.points[i + 1]))

    def update(self, dt, gravity, friction, iterations=5):
        for point in self.points:
            point.update(dt, gravity, friction)
        # self.points[-1].update(dt, gravity, friction, 1)

        for _ in range(iterations):
            for stick in self.sticks:
                stick.update()

    def draw(self, win: pygame.Surface):
        # for point in self.points:
        #     point.draw(win)

        for stick in self.sticks:
            stick.draw(win)



