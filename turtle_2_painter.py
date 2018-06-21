import turtle 

painter = turtle.Turtle()

painter.pencolor("blue") #we an also use color as "#ff00vb"
turtle.speed(5)
for i in range(50):
    painter.forward(50)
    painter.left(123) # Let's go counterclockwise this time 
    
painter.pencolor("red")
for i in range(50):
    painter.forward(100)
    painter.left(123)
    
turtle.done()
