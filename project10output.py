import turtle
import  random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Racing Game")

# Define race track parameters
track_width = 500
track_height = 400
num_lanes = 5 
lane_height = track_height // num_lanes 

# Create a list to hold the turtle racers 
racers = []

# Create the rack track
for i in range(num_lanes):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.penup()
    racer.setpos(-track_width//2, (i - num_lanes//2) * lane_height)
    racers.append(racer)

# Define a function to move the turtles
def race(): 
    while True:
        for racer in racers:
            distance = random.randint(1, 20)
            racer.forward(distance)

            # Check for a winner
            if racer.xcor() >=  track_width//2:
                winner_color = racer.fillcolor()
                print(f"The winner is the turtle with the color {winner_color}!")
                return
            
# Start the race
race()

# Celebrate the winner
celebration = turtle.Turtle()
celebration.hideturtle()
celebration.penup()
celebration.setpos(-100, track_height//4)
celebration.write(f"Congratulations to whoever won this thang!", font=("Bebas", 20, "bold"))

# Wait for the user to close the window
screen.mainloop()
