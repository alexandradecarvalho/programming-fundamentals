# Alexandra de Carvalho, 15 jun 2021


# Exercise 1 - Analyse and complete the bodyMassIndex function definition to calculate the index with bmi = weight / (height²). Complete the arguments in the function invocation. Complete the bmiCategory function to return a string with the correspondent body mass category and add a call to this function
def bodyMassIndex(height, weight):
    # Complete the function definition...
    bmi = weight / (height ** 2)
    return bmi

def bmiCategory(bmi):
    # Complete the function definition...
    if bmi < 18.5:
        categoria = "Skinny"
    elif bmi < 25:
        categoria = "Healthy"
    elif bmi < 30:
        categoria = "Strong"
    else:
        categoria = "Obese"
    return categoria

def ex1():
    print("Body Mass Index")
    altura = float(input("Height (m)? "))
    peso = float(input("Weight (kg)? "))

    # Complete the function calls...
    imc = bodyMassIndex(altura, peso)
    cat = bmiCategory(imc)

    print("BMI:", imc, "kg/m2")
    print("BMI category:", cat)


# Exercise 2 - Write a function to calculate the polynomial p(x) = x² + 2x +3 and use it to calculate and show the values of p(0), p(1), p(2) and p(p(1))
def polynomial(x):
    px = (x**2) + 2*x + 3

    return px

def ex2():
    print("p(0) = ", polynomial(0))
    print("p(1) = ", polynomial(1))
    print("p(2) = ", polynomial(2))
    print("p(p(1)) = ", polynomial(polynomial(1)))


# Exercise 3 - Define a function that returns the biggest out of its two arguments without using the pre-defined max function but Using an if instruction instead
def max2(number1, number2):
    if number1 > number2: 
        result = number1
    else:
        result = number2
    
    return result

def ex3():
    number1 = int(input("number? "))
    number2 = int(input("number? "))

    print("The biggest out of these two numbers is {}".format(max2(number1,number2)))


# Exercise 4 - Develop a function that returns the biggest out of its 3 arguments using only the function you defined before
def max3(number1, number2, number3):
    if max2(number1,number2) == number1 and max2(number1,number3) == number1:
        return number1
    elif max2(number1,number2) == number2 and max2(number2,number3) == number2:
        return number2
    else:
        return number3

def ex4():
    number1 = int(input("number? "))
    number2 = int(input("number? "))
    number3 = int(input("number? "))

    print("The biggest out of these three numbers is {}".format(max3(number1,number2, number3)))


# Exercise 5 - Write a function, tax(r), which implements the piecewise function using an if-elif-else instruction. Which values must you test?
# I must test a value below 1000 (like 800), 1000, a value between 1000 and 2000 (like 1500), 2000 and a value above 2000 (like 3000)
def tax(r):
    if r <= 1000:
        return 0.1*r
    elif r <= 2000:
        return 0.2*r-100
    else:
        return 0.3*r-300

def ex5():
    r = int(input("insert r: "))
    print("tax({}) = {}".format(r, tax(r)))


# Exercise 6 - Write a intersects(a1,b1,a2,b2) function that returns True if the [a1,b1[ and [a2,b2[ intervals intersect and False otherwise 
def intersects(a1,b1,a2,b2):
    if a2 < a1 and b2 < a1:
        return False
    elif a2 > b1 and b2 > b1:
        return False
    else:
        return True

def ex6():
    a1 = int(input("a1? "))
    b1 = int(input("b1? "))
    a2 = int(input("a2? "))    
    b2 = int(input("b2? "))    

    doesIntersect = intersects(a1,b1,a2,b2)
    if doesIntersect:
        print("[{},{}[ and [{},{}[ intersect".format(a1,b1,a2,b2))
    else:
        print("[{},{}[ and [{},{}[ do not intersect".format(a1,b1,a2,b2))


# Exercise 7 - Fix the error in the isLeapYear function
def isLeapYear(year):
    if year % 100 == 0:
        return year % 400 == 0
    else:
        return year % 4 == 0

def ex7():
    year = int(input("Insert year: "))
    if isLeapYear(year):
        print("{} is a leap year!".format(year))
    else:
        print("{} is not a leap year!".format(year))


# Exercise 8 - The function that determines the number of days in a month is also wrong. When the month is February, invoke the previous function to determine if the year is a leap year, in which case it should return 29 days
def monthDays(year, month):
    MONTHDAYS = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
    
    if month == 2 and isLeapYear(year):
        days = 29
    else:
        days = MONTHDAYS[month]

    return days

def ex8():
    month = int(input("Insert month: "))
    year = int(input("Insert year: "))

    print("{}/{} has {} days".format(month, year, monthDays(year, month)))


# Exercise 9 - Fix the nextDay function to correctly return the next day
def nextDay(year, month, day):
    if day != monthDays(year, month):
        day += 1
    else:
        day = 1
        if month == 12:
            month = 1
            year += 1
        else:
            month += 1
    return year, month, day

def ex9():
    print("Was", 2017, "a leap year?", isLeapYear(2017))    # False?
    print("Was", 2016, "a leap year?", isLeapYear(2016))    # True?
    print("Was", 2000, "a leap year?", isLeapYear(2000))    # True?
    print("Was", 1900, "a leap year?", isLeapYear(1900))    # False?
    
    print("January 2017 had", monthDays(2017, 1), "days")   # 31?
    print("February 2017 had", monthDays(2017, 2), "days")  # 28?
    print("February 2016 had", monthDays(2016, 2), "days")  # 29?
    print("February 2000 had", monthDays(2000, 2), "days")  # 29?
    print("February 1900 had", monthDays(1900, 2), "days")  # 28?
    
    y, m, d = nextDay(2017, 1, 30)
    print(y, m, d)    # 2017 1 31 ?
    y, m, d = nextDay(2017, 1, 31)
    print(y, m, d)    # 2017 2 1 ?
    y, m, d = nextDay(2017, 2, 28)
    print(y, m, d)    # 2017 3 1 ?
    y, m, d = nextDay(2016, 2, 29)
    print(y, m, d)    # 2016 3 1 ?
    y, m, d = nextDay(2017, 12, 31)
    print(y, m, d)    # 2018 1 1 ?


# Exercise 10 - Write a countdown(N) function which prints a countdown from a positive number N. Notice that you can `print(N)` and then do countdown(N-1)
def countdown(N):
    if N:
        print(N)
        countdown(N-1)

def ex10():
    N = int(input("number? "))
    countdown(N)


# Exercise 11 - Write a function to calculate the maximum common denominator and test it with several pairs of values
def mdc(a,b):
    r=a%b
    if r==0:
        return b
    elif r>0:
        return mdc(b,r)

def ex11():
    a = int(input("a: "))
    b = int(input("b: "))
    print(mdc(a,b))


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 1")
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
            choice = int(input("Enter your choice [1-11] or 0 to quit: "))
        except:
            choice = 222
        
        if choice==1:     
            print("Exercise 1: \n")
            ex1()
        elif choice==2:     
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


