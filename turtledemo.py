import turtle
"""
new_turtle=turtle.Turtle() #create object of turtle
for  i in range(4):
	new_turtle.forward(100)
	new_turtle.right(90)


#for drawing star 
star = turtle.Turtle()

for i in range(5):
    star.forward(50)
    star.right(144)
 
"""
   
#for  spiral star drawing...
spiral = turtle.Turtle()

for i in range(10):
    spiral.forward(i * 10)
    spiral.right(144)   #think why 144
    
turtle.done()  #for  waiting the window tobe closed by user...
