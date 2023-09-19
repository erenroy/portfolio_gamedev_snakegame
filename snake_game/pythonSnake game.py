from turtle import Screen, Turtle
from snake import Snake
from food import Food
from score import Scoreboard
import time


screen = Screen()
screen.setup(width=1500,height=1000)
screen.bgcolor("black")
screen.title("MY SNAKE GAME ")
screen.tracer(0)


snake = Snake()
food  = Food()
Score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()
    
    if  snake.head.distance(food) <  15:
        food.refresh()
        
        
        
screen.exitonclick()