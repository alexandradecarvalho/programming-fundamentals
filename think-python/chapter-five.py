# Alexandra de Carvalho, 16 september 2021


import turtle


# Exercise 5.2 - Write a function that takes a function object and a number, n, as arguments, and that calls the given function n times
def print_hi():
    print("Hi!")

def do_n(function, n):
    if n > 0:
        function()
        do_n(function, n-1)


# Exercise 5.3 - Write a function that takes four parameters — a, b, c and n — and that checks to see if Fermat’s theorem holds
def check_fermat(a,b,c,n):
    if n > 2:
        if (a**n) + (b**n) == c**n :
            print("Holy smokes, Fermat was wrong!")
        else:
            print("No, that doesn’t work")
    else:
        print("Please, n must be greater than 2")

# Exercise 5.3 - Write a function that prompts the user to input values for a, b, c and n, converts them to integers, and uses check_fermat to check whether they violate Fermat’s theorem
def get_values():
    while True:
        try:
            a = int(input("a? "))
            b = int(input("b? "))
            c = int(input("c? "))
            n = int(input("n? "))
        except ValueError:
            print("I'm sorry, the values you introduced seemed invalid. Please try again")
        else:
            break
    check_fermat(a,b,c,n)


# Exercise 5.4 - Write a function that takes three integers as arguments, and that prints either “Yes” or “No,” depending on whether you can or cannot form a triangle from sticks with the given lengths
def is_triangle(l1, l2, l3):
    if l1 > (l2 + l3) or l2 > (l1 + l3) or l3 > (l1 + l2):
        print("No")
    else:
        print("Yes")

# Exercise 5.4 - Write a function that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to check whether sticks with the given lengths can form a triangle
def get_stick_lengths():
    while True:
        try:
            l1 = int(input("l1? "))
            l2 = int(input("l2? "))
            l3 = int(input("l3? "))
        except ValueError:
            print("I'm sorry, the values you introduced seemed to be invalid. Please try again")
        else:
            break
    is_triangle(l1,l2,l3)    


# Exercise 5.5 - Read the following function, see if you can figure out what it does, and then run it
def draw(bob, length, n):
    if n == 0:
        return
    
    angle = 50
    bob.forward(length*n)
    bob.left(angle)
    draw(bob, length, n-1)
    bob.right(2*angle)
    draw(bob, length, n-1)
    bob.left(angle)
    bob.back(length*n)


# Exercise 5.6 - Write a function that takes a turtle and a length as parameters, and that uses the turtle to draw a Koch curve with the given length
def koch(bob, length):
    if length < 3:
        bob.forward(length)
    else:
        koch(bob,length/3)
        bob.left(60)
        koch(bob,length/3)
        bob.right(120)
        koch(bob,length/3)
        bob.left(60)
        koch(bob,length/3)

# Exercise 5.6 - Write a function called snowflake that draws three Koch curves to make the outline of a snowflake
def snowflake(bob, length):
    for side in range(4):
        koch(bob, length)
        bob.right(90)

        
def exit():
    turtle.exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error  

##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("2. Exercise 5.2")
    print("3. Exercise 5.3")
    print("4. Exercise 5.4")
    print("5. Exercise 5.5")
    print("6. Exercise 5.6")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [2-5] or 0 to quit: "))
        except:
            choice = 222    # Invalid option
        
        if choice==2:
            while True:
                try:
                    n = int(input("How many times do you want to be greeted? "))
                except ValueError:
                    print("I'm sorry, the value you introduced seems not to be a number. Please try again")
                else:
                    break
            do_n(print_hi,n)
        elif choice==3:
            get_values()
        elif choice==4:
            get_stick_lengths()
        elif choice==5:
            while True:
                try:
                    length = int(input("length? "))
                    n = int(input("n? "))
                except ValueError:
                    print("I'm sorry, the values you introduced seemed to be invalid. Please try again")
                else:
                    break
            
            bob = turtle.Turtle()
            draw(bob, length, n)
            exit() 
        elif choice==6:
            while True:
                try:
                    length = int(input("length? "))
                except ValueError:
                    print("I'm sorry, the length you introduced seemed to be invalid. Please try again")
                else:
                    break
            bob = turtle.Turtle()
            snowflake(bob, length)
            exit()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()