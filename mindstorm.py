import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")

    #for i in range(1,5):
    #    brad.forward(200)
    #    brad.right(144)
    


    for i in range(1,11):
        brad.right(0)
        brad.forward(10)
        brad.right(-90)
        brad.forward(10)
        brad.right(90)


    #addition = 10
    #len = 20
    #for i in range(1,20):
    #    len = len + addition
    #    brad.forward(len)
    #    brad.right(90)

    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")

    for i in range(1,5):
        angie.circle(50)
        angie.right(90)
    

    
    window.exitonclick()

draw_square()
