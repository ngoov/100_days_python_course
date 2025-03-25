from turtle import Screen, Turtle

screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")


def force_open_on_top():
    root = screen.getcanvas().winfo_toplevel()
    root.lift()
    root.attributes('-topmost', 1)
    root.focus_force()
    root.attributes('-topmost', 0)


force_open_on_top()

t = Turtle()

t.forward(100)

screen.mainloop()
