# Alexandra de Carvalho, july 2021


import turtle
import math


# Exercise 2.1 - Now put the same statements into a script and run it. What is the output?
def ex21():
    5
    x = 5
    x + 1

# Exercise 2.1 - Modify the script by transforming each expression into a print statement and then run it again
def modified21():
    print(5)
    x=5
    print(x+1)


# Exercise 3.2 - Move the function call back to the bottom and move the definition of print_lyrics after the definition of repeat_lyrics . What happens when you run this program?
def repeat_lyrics(): # THIS WORKS!!!
    print_lyrics()
    print_lyrics()

def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")

repeat_lyrics()


# Exercise 3.3 - Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display
def right_justify(s):
    num_spaces = 70-len(s)
    spaces = " "*num_spaces
    return spaces+s

def ex33():
    s = input("string: ")
    print(right_justify(s))


# Exercise 3.4 - Modify do_twice so that it takes two arguments, a function object and a value, and calls the function twice, passing the value as an argument
def do_twice(f,val):
    f(val)
    f(val)

# Exercise 3.4 - Define a new function called do_four that takes a function object and a value and calls the function four times, passing the value as a parameter
def do_four(string):
    print_twice(string)
    print_twice(string)

# Exercise 3.4 - Write a more general version of print_spam , called print_twice , that takes a string as a parameter and prints it twice
def print_twice(string):
    print(string)
    print(string)

# Exercise 3.4 - Use the modified version of do_twice to call print_twice twice, passing 'spam' as an argument
def ex34():
    s = input("string: ")
    do_twice(print_twice,s)
    print("-"*20)
    do_four(s)


# Exercise 3.5 - Write a function that draws a grid
def draw_grid():
    n = 2
    while n > 0: 
        print('+','+','+',sep='----')
        print('|','|','|', sep=" "*4)
        print('|','|','|', sep=" "*4)
        print('|','|','|', sep=" "*4)
        print('|','|','|', sep=" "*4)
        n -=1 
    print('+','+','+',sep='----')

# Page 53
def turtleworld():
    bob = turtle.Turtle()    
    bob.forward(100)
    bob.left(90)
    bob.forward(100)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error


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
    angle = 360/n_sides
    for times in range(n_sides):
        bob.left(angle)
        bob.forward(length)
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error

# Exercise 4.4 - Write a function that draws a circle of radius r by invoking the polygon function
def circle(bob, r=50):
    circumference = 2 * math.pi * r
    bob.delay = 0.01
    n = int((circumference/3)+1)    # this way the sides of the polygon are small enough for it to look like a circle but big enough so that it isn't too much time consuming - tip from the book
    l = circumference/n   # l * n = 2 x pi() x r <=> l =2 x pi() x r / n
    polygon(bob, n, l)

# Exercise 4.5 - Write a function that takes an angle parameter to determine which fraction of the a circle to draw
def arc(bob, angle):
    bob.delay = 0.01
    r = 50 # rand
    
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

##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 2.1")
    print("2. Exercise 3.3")
    print("3. Exercise 3.4")
    print("4. Exercise 3.5")
    print("5. Exercises from page 53")
    print("6. Exercise 4.1")
    print("7. Exercise 4.2")
    print("8. Exercise 4.3")
    print("9. Exercise 4.4")
    print("10. Exercise 4.5")
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
            ex21()
            modified21()
        elif choice==2:
            ex33()
        elif choice==3:
            ex34()
        elif choice==4:
            draw_grid()
        elif choice==5:
            turtleworld()
        elif choice==6:
            bob = turtle.Turtle()
            square(bob)
        elif choice==7:
            try:
                length = float(input("Square length? "))
            except ValueError:
                print("ERROR: Invalid values")
            else:
                bob = turtle.Turtle()
                square_with_length(bob,length)
        elif choice==8:
            try:
                n_sides = int(input("Number of sides of the polygon? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                polygon(bob, n_sides)
        elif choice==9:
            try:
                r = float(input("Circle radius? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                circle(bob, r)
        elif choice==10:
            try:
                fraction = float(input("Fraction of the arc? "))
            except ValueError:
                print("ERROR: Invalid value")
            else:
                bob = turtle.Turtle()
                arc(bob, fraction)
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()