# Module for the ball sprite

import tkinter
from random import choice
from . import ping_main as core


class Ball:
    def __init__(self, canvas, paddle, image):

        # __init__ function for the ball sprite, assigns data

        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_image(0, 0, image=image, anchor="center")
        self.canvas.move(self.id, 300, 210)
        starts = [-3, -2, 1, 1, 2, 3]
        self.start_x = choice(starts)
        self.x = self.start_x
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.hit_bottom = False

    def hit_paddle(self, pos):

        # Checks if the ball has hit the paddle

        paddle_pos = self.canvas.coords(self.paddle.id)
        if (pos[0] >= paddle_pos[0] - 48) and (pos[0] <= paddle_pos[0] + 48):
            if (pos[1] >= paddle_pos[1] - 16) and (pos[1] <= paddle_pos[1] + 16):
                return True
        return False

    def draw(self):

        # Draws the ball in the new position

        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 38:
            self.y = 3 + core.speed_factor
        if pos[1] >= self.canvas_height + 8:
            self.hit_bottom = True
        if self.hit_paddle(pos):
            core.score += 1
            self.y = -3 - core.speed_factor
            core.change_speed_factor()
        if pos[0] <= 8:
            self.x = abs(self.x) + core.speed_factor
        if pos[0] >= self.canvas_width - 8:
            self.x = (abs(self.x) * -1) + core.speed_factor
