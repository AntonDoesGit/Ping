# Module for the game core

score = 0
speed_factor = 0


def change_speed_factor():
    global score, speed_factor
    speed_factor = score / 4
