import turtle 

t = turtle.Turle()
turtle.title("for my girl friend")

screen=turtle.Screen()
screen.bgcolor("black")

t.color("pink")
t.fillcolor("pink")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(100)

t.end_fill()

t.up()
t.setpos(-80, 150)
t.down()
t.color("white")
t.write("I LOVE YOU", font=("RockwellNova", 20))

t.ht()

turtle.mainloop()