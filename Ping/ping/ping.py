# The game root file

# Installing necessary modules

from PIL import Image as PILImage
from PIL import ImageTk as PILImageTk
from tkinter import *
import time

import modules.ping_main as core
import modules.ping_ball as ping_ball
import modules.ping_paddle as ping_paddle
import modules.ping_display as ping_display

print("""
████ █            ██ 
█░░█░ ░          ██░░
████░█ ███   ███ █░░ 
█░░░░█░█░░█ █ ░█░ ░  
█░   █░█░ █░████░█   
 ░    ░ ░  ░ ░░█░ ░  
            ████░    
             ░░░░    """)

# Creating window

tk = Tk()
tk.title("Ping!")
tk.resizable(False, False)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=600, height=450, bd=0, highlightthickness=0, background="#101010")
canvas.pack()
tk.update()

# Creating sprites

raw_ball_img = PILImage.open("./assets/ball_textures/ball_default.png")
ball_img = PILImageTk.PhotoImage(raw_ball_img)

raw_paddle_img = PILImage.open("./assets/paddle_textures/paddle_default.png")
paddle_img = PILImageTk.PhotoImage(raw_paddle_img)

paddle = ping_paddle.Paddle(canvas, paddle_img)
ball = ping_ball.Ball(canvas, paddle, ball_img)
score_display = ping_display.ScoreDisplay(canvas, ball)

# Display loop

try:
    while True:
        if not ball.hit_bottom:
            ball.draw()
            paddle.draw()
            score_display.draw(core.score)
        tk.update()
        tk.update_idletasks()
        time.sleep(1 / 30)
except TclError:
    pass
