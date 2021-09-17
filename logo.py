# Connecting library
import turtle

# Screen settings
# Launch the window in which we will draw the logo
screen = turtle.Screen()
# The colors I will use to create my logo
bg_color = "#4B4E6D"
trl_color = "#ffffff"
trl_color_lucky = "#ffd700"
# Window sizes
screen.setup(width=700, height=550)
# Name of my window
screen.title("Logo_VB")
# Color settings
screen.bgcolor(bg_color)
# Start drawing
draw = turtle.Turtle()
draw.speed(1)  # Speed settings of logo drawing
draw.pensize(13)  # or can use .width()

#
draw.penup()  # Put the turtle up, after I can move turtle anywhere and nothing will be displayed
draw.goto(-120, 30)  # Go to a concrete place when I want to start drawing
draw.pendown()  # Put the turtle down, after that I can start drawing

# drawing V
draw.pencolor(trl_color)  # Set the color to the turtle
draw.forward(20)  # move forward ==> drawing forward on 20 px
draw.right(80)  # rotate settings
draw.forward(150)
draw.left(150)
draw.forward(250)
draw.right(70)

# drawing B
draw.forward(100)
draw.circle(-40, 180)  # Drawing circle
draw.forward(10)
draw.pencolor(trl_color_lucky)
draw.circle(80, - 300)
draw.pencolor(trl_color)
draw.forward(70)
draw.left(120)
draw.forward(20)
draw.right(140)
draw.forward(120)
draw.right(40)
draw.pencolor(trl_color)
draw.forward(50)

# Moving to letter B, when I will drawing small circle clockwise
draw.penup()
draw.goto(100, -2)
draw.right(180)
draw.pendown()

# Small ring inside letter B
draw.pencolor(trl_color_lucky)
draw.circle(-40, 290)

# Moving to special position, when I will drawing big circle counterclockwise
draw.penup()
draw.goto(16, 180)
draw.right(-110)
draw.pendown()

# Big circle
draw.pencolor(trl_color)
draw.circle(200)

turtle.done()
