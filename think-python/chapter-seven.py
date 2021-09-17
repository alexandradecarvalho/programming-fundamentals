# Alexandra de Carvalho, 17 september 2021


import math


# Exercise 7.1 - Rewrite the function print_n from Section 5.8 using iteration instead of recursion
def print_n(s, n):
    while n > 0:
        print(s)
        n=n-1


# Exercise 7.2 - Encapsulate the Newton's square root method loop in a function that takes a as a parameter, chooses a reasonable value of x, and returns an estimate of the square root of a
def square_root(a):
    x = a/2
    while True:
        print(x)
        y = (x + a/x) / 2
        if y == x:
            break
        x = y


# Exercise 7.3 - Write a function that prints a table comparing the square root algorithm above and the math.sqrt results
def square_root_alg(a):
    x = a/2
    while True:
        y = (x + a/x) / 2
        if y == x:
            return x
        x = y

def test_square_root():
    for a in range(1,10):
        alg_result = square_root_alg(a)
        library_result = math.sqrt(a)
        print("{:2.1f} {:<12f} {:<12f} {:<12e}".format(float(a), alg_result, library_result, abs(alg_result-library_result)))


# Exercise 7.4 - Write a function that iteratively prompts the user, takes the resulting input and evaluates it using eval, and prints the result
def eval_loop():
    last_result = ''
    while True:
        exp = input('Write something:\n')
        if exp == 'done':
            return last_result
        else:
            last_result = eval(exp)
            print(last_result)


# Exercise 7.5 - Write a function that uses Srinivasa Ramanujan's infinite series that generate a numerical approximation of 1/π to compute and return an estimate of π
def estimate_pi():
    total = 0
    k = 0
    constant = (2*math.sqrt(2))/9801
    while True:
        inverted_pi = constant * ( (math.factorial(4*k)*(1103+26390*k)) / ((math.factorial(k))**4 * (396**(4*k))) )
        total += inverted_pi
        
        if abs(inverted_pi) < 1e-15:
            break

        k += 1

    return 1/total
         

##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 7.1")
    print("2. Exercise 7.2")
    print("3. Exercise 7.3")
    print("4. Exercise 7.4")
    print("5. Exercise 7.5")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [1-5] or 0 to quit: "))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            s = input("sentence?\n")
            while True:
                try:
                    n = int(input("number of times it will be repeated? "))
                except ValueError:
                    print("I'm sorry, that value seems to be invalid. Please try again")
                else:
                    break
            print_n(s,n)
        elif choice==2:
            while True:
                try:
                    a = int(input("a? "))
                except ValueError:
                    print("I'm sorry, that value seems to be invalid. Please try again")
                else:
                    break
            square_root(a)
        elif choice==3:
            test_square_root()
        elif choice==4:
            last_result = eval_loop()
            print('Last result was', last_result)
        elif choice==5:
            pi = estimate_pi()
            print('The difference is', abs(pi-math.pi))
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()