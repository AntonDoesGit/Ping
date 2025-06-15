# Module for the score display sprite

import json


class ScoreDisplay:
    def __init__(self, canvas, ball):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.ball = ball
        self.id = canvas.create_rectangle(0, 0, self.canvas_width, 30, fill="#101010", width=0)
        self.display_id = canvas.create_text(300, 15, text="Score: 0", fill="white", width=0,
                                             font=("Roboto Mono", 20))

    def draw(self, score):
        if not self.ball.hit_bottom:
            self.canvas.itemconfig(self.display_id, text="Score: %s" % score)
        else:
            with open("data.json", "r+") as file:
                data = json.load(file)
                if score > data["high_score"]:
                    self.canvas.itemconfig(self.display_id, text=f"NEW BEST! Your score is {score}")
                    data["high_score"] = score
                    file.seek(0)
                    json.dump(data, file, indent=2)
                else:
                    self.canvas.itemconfig(self.display_id, text=f"Game over! Your score is {score}")
