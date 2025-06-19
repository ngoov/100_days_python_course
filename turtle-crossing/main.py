import time
from gamescreen import GameScreen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = GameScreen()
screen.mainloop()
screen.force_open_on_top()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
