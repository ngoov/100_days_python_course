from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
canvas_width = 500
screen.setup(canvas_width, 400)

user_bet = screen.textinput("Make your bet",
                            "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []
turtle_size = 40
canvas_x_border = (canvas_width / 2) - (turtle_size / 2)

for i, color in enumerate(colors):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x=-canvas_x_border, y=-100 + i * 40)
    new_turtle.pendown()
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > canvas_x_border:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
            else:
                print("You've lost!")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
