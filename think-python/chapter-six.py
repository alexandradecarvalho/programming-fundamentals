# Alexandra de Carvalho, 16 september 2021


import math


# Exercise 6.1 - Write a function that returns 1 if x > y, 0 if x == y, and -1 if x < y
def compare(x, y):
    if x > y:
        return 1
    if x < y:
        return -1
    else:
        return 0

# Exercise 6.2 - Use incremental development to write a function that returns the length of the hypotenuse of a right triangle given the lengths of the two legs as arguments
def hypotenuse(leg1, leg2):
    square1 = leg1**2
    square2 = leg2**2
    h2 = square1 + square2
    h = math.sqrt(h2)
    return h


# Exercise 6.3 - Write a function that returns True if x ≤ y ≤ z or False otherwise
def is_between(x, y, z):
    if compare(x,y) != 1 and compare(y,z) != 1:
        return True
    else:
        return False 


# Exercise 6.5 - Write a function that evaluates Ackermann’s function 
def ack(m,n):
    if m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1,1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m,n-1))


# Exercise 6.6
def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

# Exercise 6.6 - Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise
def is_palindrome(word):
    if len(word) > 2:
        if first(word) == last(word):
            return is_palindrome(word[1:-1])
        else:
            return False
    return True


# Exercise 6.7 - Write a function that takes parameters a and b and returns True if a is a power of b
def is_power(a,b):
    if a == b or  a == 1:
        return True
        
    return a%b == 0 and is_power(a/b, b)


# Exercise 6.8 - Write a function that takes parameters a and b and returns their greatest common divisor
def gcd(a,b):
    if b == 0:
        return a

    r = a%b
    return gcd(b,r)


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 6.1")
    print("2. Exercise 6.2")
    print("3. Exercise 6.3")
    print("5. Exercise 6.5")
    print("6. Exercise 6.6")
    print("7. Exercise 6.7")
    print("8. Exercise 6.8")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [1-3,5-8] or 0 to quit: "))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            while True:
                try:
                    x = int(input("x? "))
                    y = int(input("y? "))
                except ValueError:
                    print("I'm sorry, the values you introduced seemed to be invalid. Please try again")
                else:
                    break
            print(compare(x,y))
        elif choice==2:
            while True:
                try:
                    leg1 = int(input("leg 1? "))
                    leg2 = int(input("leg 2? "))
                except ValueError:
                    print("I'm sorry, the values you introduced seemed to be invalid. Please try again")
                else:
                    break
            print(hypotenuse(leg1,leg2))
        elif choice==3:
            while True:
                try:
                    x = int(input("x? "))
                    y = int(input("y? "))
                    z = int(input("z? "))
                except ValueError:
                    print("I'm sorry, the values you introduced seemed to be invalid. Please try again")
                else:
                    break
            print(is_between(x,y,z))
        elif choice==5:
            print(ack(3,4)) # should be 125
            #print(ack(130,140)) - max recursion depth exceeded error
        elif choice==6:
            print(middle('abc'))
            print(middle('ab'))
            print(middle('a'))
            print(middle(''))

            word = input("introduce word: ")
            print(is_palindrome(word))
        elif choice==7:
            while True:
                try:
                    a = int(input("a? "))
                    b = int(input("b? "))
                except ValueError:
                    print("I'm sorry, the values you introduced seemed to be invalid. Please try again")
                else:
                    break
            print(is_power(a,b))
        elif choice==8:
            while True:
                try:
                    a = int(input("a? "))
                    b = int(input("b? "))
                except ValueError:
                    print("I'm sorry, the values you introduced seemed to be invalid. Please try again")
                else:
                    break
            print(gcd(a,b))
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()