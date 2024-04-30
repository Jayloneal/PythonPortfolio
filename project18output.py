import turtle
import time
import random

win = turtle.Screen()
win.title("Pinball Game")
win.bgcolor("black")
win.setup(width=800, height=600)

# Create paddle
paddle = turtle.Turtle()
paddle.speed(0)
paddle.shape("square")
paddle.color("gray")
paddle.shapesize(stretch_wid=6, stretch_len=1)
paddle.penup()
paddle.goto(0, -250)

# Create ball
ball = turtle.Turtle()
ball.speed(10)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 250)
ball.dx = random.choice([-2, 2])
ball.dy = -2

# Create scoreboard
score = 0
score_board = turtle.Turtle()
score_board.speed(0)
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 260)
score_board.color("white")

# Function to move paddle
def move_paddle(x):
    paddle.setx(x)

# Keyboard binding
win.listen()
win.onkeypress(lambda: move_paddle(paddle.xcor() + 20), "Right")
win.onkeypress(lambda: move_paddle(paddle.xcor() - 20), "Left")

# Main game loop
while True:
    win.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 250)
        ball.dx *= -1
        score += 1
        score_board.clear()
        score_board.write(f"Score: {score}", align="center", font=("Bebas", 20, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 250)
        ball.dx *= -1
        score += 1
        score_board.clear()
        score_board.write(f"Score: {score}", align="center", font=("Bebas", 20, "bold"))

    # Paddle collision
    if (ball.dx > 0) and (ball.xcor() > paddle.xcor() - 50) and (ball.xcor() < paddle.xcor() + 50) and (ball.ycor() < -240):
        ball.sety(-240)
        ball.dy *= -1

    # Time delay
    time.sleep(0.01)
