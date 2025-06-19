from turtle import Turtle, Screen

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.width = 800
        self.height = 600
        self.screen.setup(width=self.width, height=self.height)
        self.screen.bgcolor("black")
        self.screen.title("pong")
        self.screen.tracer(0)
        self.force_open_on_top()

    def force_open_on_top(self):
        root = self.screen.getcanvas().winfo_toplevel()
        root.lift()
        root.attributes('-topmost', 1)
        root.focus_force()
        root.attributes('-topmost', 0)

    def update(self):
        self.screen.update()

    def mainloop(self):
        self.screen.mainloop()

    def listen(self):
        self.screen.listen()

    def onkey(self, func, key):
        self.screen.onkey(func, key)