# Alexandra de Carvalho, 16 jun 2021


# Exercise 1 - Execute and notice the effect of watch of the following code excerpts
def excerpt1():
    n = 4
    while n > 0:
        print(n)
        n -= 1

def excerpt2():
    n = 1
    while n < 1000:
        print(n)
        n *= 2

def excerpt3():
    for c in range(10):
        print(c)

def ex1():
    print(15*'-' + "EXCERPT 1" + 15*'-')
    excerpt1()
    print(15*'-' + "EXCERPT 2" + 15*'-')
    excerpt2()
    print(15*'-' + "EXCERPT 3" + 15*'-')
    excerpt3()
    

# Exercise 2 - Try and modify the table.py function to show the table to numbers between 1 and 20 using the range function and add a column to show 2^n, fixing the width of the columns and the alignment of the header
def table():
    print("{:^8s} {:^8s} {:^8s}".format("n", "n²", "2^n"))
    for n in range(20):
        print("{:8d} {:8d} {:8d}".format((n+1), (n+1)**2, 2**n))

def ex2():
    table()


# Exercise 3 - Complete the spiral function to draw a spiral with sides which increase/decrease with an arithmetic progression
def square(t, side):
    for n in range(4):
        t.forward(side)
        t.left(90)

def spiral(t, start, end, incr):
    # Complete the function...
    for n in range(start, end, incr):
        t.forward(n)
        t.left(90)

def ex3():
    print("This program opens a window with a graphical user interface.")
    wn = turtle.Screen()        # creates a graphics window
    alex = turtle.Turtle()      # create a turtle named alex

    alex.forward(150)           # tell alex to move forward by 150 units
    alex.left(90)               # turn by 90 degrees
    alex.forward(75)            # complete the second side

    beth = turtle.Turtle()      # another turtle
    beth.shape("turtle")        # with another shape
    beth.color("blue")          # and color
    beth.up()                   # pen up
    beth.goto(-200, 0)          # move to given point
    beth.down()                 # pen down
    square(beth, 100)           # draw a square

    # Move alex to another place
    alex.up()
    alex.goto(-200, -200)
    alex.setheading(0)
    alex.down()
    # This should draw a spiral
    spiral(alex, 10, 200, 10)

    turtle.exitonclick()        # wait for a button click, then close window
    print("The window was closed. Bye!")


# Exercise 4 - Change the sequenceUn.py to show all positive terms of the sequence Um = 1.01*(Un-1) - 1.01, using a while instruction, and that in the end says how many terms were shown
def sequenceUn():
    Un = 100                    # Un = each term of the sequence. Initially = U0
    counter = 0
    while Un > 0:
        print(Un)
        Un = 1.01*Un - 1.01     # Set Un to the next term of the sequence
        counter += 1
    print("{} terms were shown".format(counter))

def ex4():
    sequenceUn()


# Exercise 5 - Write a factorial(n) function that calculates the factorial of n, defined by n! = 1*2 *3 *... *n
def factorial(n):
    res = 1
    for x in range(n, 0, -1):
        res = res*x
    return res

def ex5():
    r = int(input("insert n: "))
    print("{}! = {}".format(r, factorial(r)))


# Exercise 6 - Complete the program hilo.py to do the rest of the game.
def hilo():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101);
    
    # put your code here
    guess = 2 if secret == 1 else 1 # starting with a guess != secret
    tries = 0
    while guess != secret:
        guess = int(input("Can you guess my secret?"))
        if guess < secret:
            print("Too Low!")
            tries += 1
        elif guess > secret:
            print("Too High!")
            tries += 1
        else:
            break
    print("Perfect! You found the secret in {} tries!".format(tries))
        
def ex6():
    hilo()

# Exercise 7 - Write a leibnizPi4(n) function which returns the sum of the first n terms of the Leibniz's series and test it asking the user for the value of n
def leibnizPi4(n):
    res = 0
    for term in range(n+1):
        res = res + ((-1)**term) / (2*term + 1)
    return res

def ex7():
    n = int(input("n? "))
    print("res: {}".format(leibnizPi4(n)))


# Exercise 8 - Write a program which asks the user a sequence of real numbers and shows the maximum value, the minimum value and the average of the inputed numbers
def max_min_avg():
    inpt = "#notempty"
    lst = []
    while inpt != "":
        inpt = input(">> ")
        try:
            n = int(inpt)
            lst += [n]
        except:
            break
    print("max: ", max(lst))
    print("min: ", min(lst))
    print("average: ", sum(lst)/len(lst))

def ex8():
    max_min_avg()

# Exercise 9 - Write a Fibonacci(n) function to calculate the n-ieth number of Fibonacci, updating and storing, in each iteration, the last two values
def fibonacci(n):
    last1 = 1
    last2 = 0
    if n < 2:
        return n
    else: 
        for term in range(2, n+1):
            res = last1 + last2
            last2 = last1
            last1 = res
        return res

def ex9():
    n = int(input("n? "))
    print(fibonacci(n))


# Exercise 10 - Write a isPrime(n) function which returns True if n is a prime number and False otherwise, by dividing n by 2, by 3, etc to see if any of the numbers exactly divide N and test the function in a program which goes through all the numbers between 1 and 100 and indicates whether or not each of them are prime numbers
def isPrime(n):
    for divisor in range(2, n):
        if n%divisor == 0:
            return False
    return True

def ex10():
    n = 1
    while n <= 100:
        if isPrime(n):
            print("{} is a prime number!".format(n))
        else:
            print("{} is not a prime number :/".format(n))
        n += 1


# Exercise 11 - Write a program which reads a positive integer from the keyboard, N, and prints the list of all its divisors (all numbers who divide N, except N) and also indicates if N is a deficient, perfect or abundant number
def divisors(N):
    res = []
    for divisor in range(1, N):
        if N%divisor == 0:
            res += [divisor]

    print(res)
    if sum(res) > N:
        print("{} is a abundant number".format(N))
    elif sum(res) < N:
        print("{} is a deficient number".format(N))
    else:
        print("{} is a perfect number".format(N))

def ex11():
    n = int(input("n? "))
    divisors(n)


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("2. Exercise 2")
    print("3. Exercise 3")
    print("4. Exercise 4")
    print("5. Exercise 5")
    print("6. Exercise 6")
    print("7. Exercise 7")
    print("8. Exercise 8")
    print("9. Exercise 9")
    print("10. Exercise 10")
    print("11. Exercise 11")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [5-9] or 0 to quit: "))
        except:
            choice = 222
        
        if choice==2:     
            print("Exercise 2: \n")
            ex2()
        elif choice==3:     
            print("Exercise 3: \n")
            ex3()
        elif choice==4:
            print("Exercise 4: \n")
            ex4()
        elif choice==5:     
            print("Exercise 5: \n")
            ex5()
        elif choice==6:
            print("Exercise 6: \n")
            ex6()
        elif choice==7:
            print("Exercise 7: \n")
            ex7()
        elif choice==8:
            print("Exercise 8: \n")
            ex8()
        elif choice==9:
            print("Exercise 9: \n")
            ex9()
        elif choice==10:
            print("Exercise 10: \n")
            ex10()
        elif choice==11:
            print("Exercise 11: \n")
            ex11()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()