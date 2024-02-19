import turtle

myScreen = turtle.getscreen()
turtle.title("My Python Journey")
turtle.bgcolor("pink")
mc = turtle.Turtle("turtle")
mc.speed("fastest")


def hexagon(mc, length):
    for ii in range(6):
        mc.forward(length)
        mc.left(60)


def radialHexagon(mc, n, length):
    for ii in range(n):
        hexagon(mc, length)
        mc.left(360 / n)


userInput = input("Would you like to draw a circle (Yes or No)? ").lower()
if userInput == "yes":
    size = int(input("How big should your circle be? "))
    mc.circle(size)
else:
    print("Let me draw something for you!")
    radialHexagon(mc, 10, 50)

turtle.mainloop()




