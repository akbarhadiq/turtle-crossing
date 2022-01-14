import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(height=600, width=600)
screen.title("Turtle Crossing Game")
# Turn off animation, make the screen update itself manually via a while loop
screen.tracer(0)

# Create Player from the Player Class
timmy = Player()

# Create car manager list,
car_manager = CarManager()

# Write the scoreboard onto the screen
scoreboard = Scoreboard()

# Make the screen listen to key presses
screen.listen()
# when the up arrow get pressed, move the player object
screen.onkeypress(timmy.move, "Up")

game_is_on = True
while game_is_on:
    # update screen object
    screen.update()
    # delay when updating screen object
    time_sleep = 0.1
    time.sleep(time_sleep)

    # Create a car using car_manager inside the loop
    car_manager.create_cars()
    car_manager.move_cars()

    # Detect Collision with cars
    for car in car_manager.all_cars:
        if timmy.distance(car) < 10:
            game_is_on = False
            scoreboard.game_over()

    # Detect when timmy the turtle crossed the road successfully
    if timmy.ycor() > 290:
        # Reset timmy location
        timmy.reset()
        # Update Scoreboard
        scoreboard.level = scoreboard.level + 1
        # Increase game speed by multiplying the time.sleep value
        time_sleep = time_sleep * 0.9
        # Write updated scoreboard onto screen
        scoreboard.update_scoreboard()

screen.exitonclick()
