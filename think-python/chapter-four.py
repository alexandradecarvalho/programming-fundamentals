# Alexandra de Carvalho, july 2021


import turtle
import math


# Exercise 4.1 - Write a function that takes a turtle as a parameter and uses it to draw a square
def square(bob):
    for times in range(4):
        bob.left(90)
        bob.forward(100)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error

# Exercise 4.2 - Add a length parameter to the square function, that indicates the square's sides' length
def square_with_length(bob, length):
    for times in range(4):
        bob.left(90)
        bob.forward(length)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error

# Exercise 4.3 - Write a function that draws a an n-sided regular polygon
def polygon(bob, n_sides, length=100):
    """
        Draws n_sides line segments with the given length to
        create a regular polygon. bob is a turtle.
    """
    angle = 360/n_sides
    for times in range(n_sides):
        bob.left(angle)
        bob.forward(length)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error

# Exercise 4.4 - Write a function that draws a circle of radius r by invoking the polygon function
def circle(bob, r=50):
    """
        Draws a regular polygon to create a circle effect with
        the given radius r. bob is a turtle.
    """
    circumference = 2 * math.pi * r
    bob.delay = 0.01
    n = int((circumference/3)+1)    # this way the sides of the polygon are small enough for it to look like a circle but big enough so that it isn't too much time consuming - tip from the book
    l = circumference/n   # l * n = 2 x pi() x r <=> l =2 x pi() x r / n
    polygon(bob, n, l)

# Exercise 4.5 - Write a function that takes an angle parameter to determine which fraction of the a circle to draw
def arc(bob, angle, r=50):
    """
        Draws lines to create fraction of a semi-circle effect
        with the given angle. bob is a turtle.
    """
    bob.delay = 0.01
    
    circumference = 2 * math.pi * r
    arc_len = circumference * angle/360 # rule of three
    n = int((arc_len/3)+1)    # this way the sides of the polygon are small enough for it to look like a circle but big enough so that it isn't too much time consuming - tip from the book
    
    l = arc_len / n   # l * n = 2 x pi() x r <=> l =2 x pi() x r / n
    angle = angle / n
    
    for times in range(n):
        bob.left(angle)
        bob.forward(l)

    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error


# Exercise 4.2 - Write an appropriately general set of functions that can draw flowers
def petal(t, r, angle):
    for i in range(2):
        arc(t, angle, r)
        t.left(180-angle)

def flower(t, n, r, angle):
    for i in range(n):
        petal(t, r, angle)
        t.left(360.0/n)

def move(t, length):
    t.up()
    t.forward(length)
    t.down()


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 4.1")
    print("2. Exercise 4.2")
    print("3. Exercise 4.3")
    print("4. Exercise 4.4")
    print("5. Exercise 4.5")
    print("6. Exercise 4.2")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [1-10] or 0 to quit: "))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            bob = turtle.Turtle()
            square(bob)
        elif choice==2:
            try:
                length = float(input("Square length? "))
            except ValueError:
                print("ERROR: Invalid values")
            else:
                bob = turtle.Turtle()
                square_with_length(bob,length)
        elif choice==3:
            try:
                n_sides = int(input("Number of sides of the polygon? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                polygon(bob, n_sides)
        elif choice==4:
            try:
                r = float(input("Circle radius? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                circle(bob, r)
        elif choice==5:
            try:
                fraction = float(input("Fraction of the arc? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                arc(bob, fraction)
        elif choice==6:
            bob = turtle.Turtle()
            move(bob, 100)
            flower(bob, 7, 60.0, 60.0)

            move(bob, 100)
            flower(bob, 10, 40.0, 80.0)

            move(bob, 100)
            flower(bob, 20, 140.0, 20.0)

            turtle.exitonclick()
            turtle.TurtleScreen._RUNNING = True # not to throw Terminator error           
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()