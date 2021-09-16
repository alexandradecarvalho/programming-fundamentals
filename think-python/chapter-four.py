# Alexandra de Carvalho, july 2021


import turtle
import math


# Exercise 4.1 - Write a function that takes a turtle as a parameter and uses it to draw a square
def square(bob):
    for times in range(4):
        bob.left(90)
        bob.forward(100)


# Exercise 4.2 - Add a length parameter to the square function, that indicates the square's sides' length
def square_with_length(bob, length):
    for times in range(4):
        bob.left(90)
        bob.forward(length)


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


# Exercise 4.2 - Write an appropriately general set of functions that can draw flowers
def petal(bob, r, angle):
    a = 180 - angle
    for i in range(2):
        arc(bob, angle, r)
        bob.left(a)

def flower(bob, n, r, angle):
    for i in range(n):
        petal(bob, r, angle)
        t.left(360.0/n)

def move(bob, length):
    bob.up()
    bob.forward(length)
    bob.down()

def ex42(bob, n_petals, arc_r, angle):
    flower(bob, n_petals, arc_r, angle)
    move(bob, 100)


# Exercise 4.3 - Write an appropriately general set of functions that can draw shapes
def triangle(bob, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    bob.right(angle)
    bob.forward(r)
    bob.left(90+angle)
    bob.forward(2*y)
    bob.left(90+angle)
    bob.forward(r)
    bob.left(180-angle)

def ex43(bob, n_triangles, r):
    angle = 360.0 / n_triangles
    for i in range(n_triangles):
        triangle(bob, r, angle/2)
        bob.left(angle)
    move(bob, 100)


def exit():
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error    


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 4.1")
    print("2. Exercise 4.2")
    print("3. Exercise 4.3")
    print("4. Exercise 4.4")
    print("5. Exercise 4.5")
    print("6. Exercise 4.2")
    print("7. Exercise 4.3")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [1-7] or 0 to quit: "))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            bob = turtle.Turtle()
            square(bob)
            exit()
        elif choice==2:
            try:
                length = float(input("Square length? "))
            except ValueError:
                print("ERROR: Invalid values")
            else:
                bob = turtle.Turtle()
                square_with_length(bob,length)
                exit()
        elif choice==3:
            try:
                n_sides = int(input("Number of sides of the polygon? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                polygon(bob, n_sides)
                exit()
        elif choice==4:
            try:
                r = float(input("Circle radius? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                circle(bob, r)
                exit()
        elif choice==5:
            try:
                fraction = float(input("Fraction of the arc? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                arc(bob, fraction)
                exit()
        elif choice==6:
            bob = turtle.Turtle()
            ex42(bob, 7, 60.0, 60.0)
            ex42(bob, 10, 40.0, 80.0)
            ex42(bob, 20, 140.0, 20.0)
            exit()   
        elif choice==7:
            bob = turtle.Turtle()
            ex43(bob, 5, 40)
            ex43(bob, 6, 40)
            ex43(bob, 7, 40)
            ex43(bob, 8, 40)
            exit()          
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()