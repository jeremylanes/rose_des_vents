import turtle
colors = ['silver', 'red', 'black']
colorss = ['red', 'black', 'silver']
draw = turtle.Pen()
draw.speed(100)
for a in range(360):
    draw.pencolor(colors[a%3])
    draw.width(a/100+2)
    draw.forward(a)
    draw.left(-180)
    draw.right(30)
draw.hideturtle()