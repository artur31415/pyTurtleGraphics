from math import pi

import pygame
from utils import vec_add, vec_from_angle, vec_mult, vec_sub


class TurtleGraphics:

    def __init__(self, position, theta_ratio, ds) -> None:
        self.init_position = position
        self.positions = [position]
        self.theta_ratio = theta_ratio
        self.theta = 0
        self.ds = ds
        self.num_of_steps = 0

    def forward(self):
        pos_increment = vec_from_angle(self.theta)
        self.positions.append(vec_add(self.positions[-1], pos_increment))
        self.num_of_steps += 1

    def turn(self, n):
        self.theta -= n * (2 * pi / self.theta_ratio)

    def get_scaled_pos(self, index):
        return vec_add(self.init_position, vec_mult(vec_sub(self.positions[index], self.init_position), self.ds))

    def draw(self, DISPLAY):
        last_pos = None
        for pos in self.positions:
            scaled_pos = pos
            if pos != self.init_position:
                scaled_pos = vec_add(self.init_position, vec_mult(vec_sub(pos, self.init_position), self.ds))
            if last_pos != None:
                pygame.draw.line(DISPLAY, (0, 0, 0), last_pos, scaled_pos)
            last_pos = scaled_pos

        pygame.draw.circle(DISPLAY, (0, 0, 255), self.positions[0], 2)
        pygame.draw.circle(DISPLAY, (255, 0, 0), self.get_scaled_pos(-1), 2)

    