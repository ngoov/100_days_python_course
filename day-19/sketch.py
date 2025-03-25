from turtle import Turtle, Screen

class SketchApp:
    def __init__(self):
        self.tim = Turtle()
        self.screen = Screen()
        self.setup_controls()
        
    def move_forwards(self):
        self.tim.forward(10)
        
    def move_backwards(self):
        self.tim.backward(10)
        
    def turn_left(self):
        new_heading = self.tim.heading() + 10
        self.tim.setheading(new_heading)
        
    def turn_right(self):
        new_heading = self.tim.heading() - 10
        self.tim.setheading(new_heading)

    def clear(self):
        self.tim.clear()
        self.tim.penup()
        self.tim.home()
        self.tim.pendown()
        
    def setup_controls(self):
        self.screen.listen()
        self.screen.onkey(self.move_forwards, "w")
        self.screen.onkey(self.move_backwards, "s")
        self.screen.onkey(self.turn_left, "a")
        self.screen.onkey(self.turn_right, "d")
        self.screen.onkey(self.clear, "c")
    
    def start(self):
        self.screen.exitonclick()

app = SketchApp()
app.start()
