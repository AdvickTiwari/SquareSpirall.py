import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["yellow", "blue", "red", "green"]
for x in range(100):
    t.pencolor( colors[ x % 4] )
    t.forward(x)
    t.left(92)
    
