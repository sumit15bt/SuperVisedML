import turtle

seurat=turtle.Turtle()


dot_distance=20
width=10
height=8

seurat.penup()

for  i in range(height):
	for j in  range(width):
		seurat.dot()
		seurat.forward(dot_distance)
	seurat.backward(dot_distance*width)
	seurat.right(90)
	seurat.forward(dot_distance)
	seurat.left(90)

seurat.done()
