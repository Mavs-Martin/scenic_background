import turtle

# Set up the screen
screen = turtle.Screen()
screen.title("Scenic Background")
screen.bgcolor("skyblue")
screen.setup(width=800, height=600)

# Create a turtle for drawing
artist = turtle.Turtle()
artist.speed(0)  # Fastest drawing speed

# Draw the ground
artist.penup()
artist.goto(-400, -100)
artist.pendown()
artist.color("green")
artist.begin_fill()
artist.forward(800)
artist.right(90)
artist.forward(200)
artist.right(90)
artist.forward(800)
artist.right(90)
artist.forward(200)
artist.end_fill()

# Draw the sun
artist.penup()
artist.goto(-100, 200)
artist.pendown()
artist.color("yellow")
artist.begin_fill()
artist.circle(100)
artist.end_fill()

# Draw some clouds
def draw_cloud(x, y):
    artist.penup()
    artist.goto(x, y)
    artist.pendown()
    artist.color("white")
    artist.begin_fill()
    artist.circle(30)
    artist.end_fill()
    artist.penup()
    artist.goto(x + 40, y + 20)
    artist.pendown()
    artist.begin_fill()
    artist.circle(30)
    artist.end_fill()
    artist.penup()
    artist.goto(x + 20, y)
    artist.pendown()
    artist.begin_fill()
    artist.circle(30)
    artist.end_fill()

draw_cloud(100, 150)
draw_cloud(200, 200)
draw_cloud(-200, 150)

# Hide the turtle and finish
artist.hideturtle()
turtle.done()
