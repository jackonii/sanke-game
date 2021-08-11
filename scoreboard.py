from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.draw_score()

    def read_high_score(self):
        with open("data.txt", mode="r") as file:
            content = file.read()
            return int(content) if content else 0

    def write_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(str(self.high_score))

    def draw_score(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.draw_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.draw_score()

