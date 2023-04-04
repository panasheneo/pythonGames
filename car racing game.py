import turtle
import random

# Set up the screen
wn = turtle.Screen()
wn.title("Car Racing Game")
wn.bgcolor("white")
wn.setup(width=600, height=600)

# Create the player car
player_car = turtle.Turtle()
player_car.speed(0)
player_car.penup()
player_car.shape("square")
player_car.color("blue")
player_car.shapesize(stretch_wid=2, stretch_len=4)
player_car.goto(0, -250)

# Create the enemy cars
enemy_cars = []
for i in range(3):
    enemy_car = turtle.Turtle()
    enemy_car.speed(0)
    enemy_car.penup()
    enemy_car.shape("square")
    enemy_car.color("red")
    enemy_car.shapesize(stretch_wid=2, stretch_len=4)
    enemy_car.goto(random.randint(-280, 280), random.randint(200, 400))
    enemy_cars.append(enemy_car)


# Set up the keyboard bindings
def move_left():
    x = player_car.xcor()
    x -= 20
    if x < -280:
        x = -280
    player_car.setx(x)


def move_right():
    x = player_car.xcor()
    x += 20
    if x > 280:
        x = 280
    player_car.setx(x)


wn.listen()
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

# Main game loop
while True:
    # Move the enemy cars
    for enemy_car in enemy_cars:
        enemy_car.sety(enemy_car.ycor() - 5)

        # Check for collision with player car
        if enemy_car.distance(player_car) < 40:
            player_car.color("red")
            player_car.write("GAME OVER", align="center", font=("Arial", 24, "bold"))
            wn.update()
            wn.mainloop()

        # Check if enemy car is off the screen
        if enemy_car.ycor() < -300:
            enemy_car.goto(random.randint(-280, 280), random.randint(200, 400))

    wn.update()
