# Module for the paddle sprite

from . import ping_main as core


class Paddle:
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.id = canvas.create_image(0, 0, image=image, anchor="center")
        self.canvas.move(self.id, 300, 400)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all("<KeyPress-a>", self.go_left)
        self.canvas.bind_all("<KeyPress-Left>", self.go_left)
        self.canvas.bind_all("<KeyPress-d>", self.go_right)
        self.canvas.bind_all("<KeyPress-Right>", self.go_right)
        self.canvas.bind_all("<KeyRelease-a>", self.stop)
        self.canvas.bind_all("<KeyRelease-Left>", self.stop)
        self.canvas.bind_all("<KeyRelease-d>", self.stop)
        self.canvas.bind_all("<KeyRelease-Right>", self.stop)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)

    def go_left(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[0] <= 48:
            self.x = 0
        else:
            self.x = -6 - core.speed_factor

    def go_right(self, evt):
        pos = self.canvas.coords(self.id)
        if pos[0] >= self.canvas_width - 48:
            self.x = 0
        else:
            self.x = 6 + core.speed_factor

    def stop(self, evt):
        self.x = 0
