# Alexandra de Carvalho, 14 jun 2021

# Exercise 1 - Alter the program max2.py to use a conditional instruction instead of the pre-defined max function
def max2():
    x1 = float(input("number? "))
    x2 = float(input("number? "))

    # Use conditional statements instead of max function!
    if x1 > x2:
        mx = x1
    else:
        mx = x2


    print("Maximum:", mx)



# Exercise 2 - Copy the previous function and modify this it to find the biggest out of three numbers with only two comparisons
def max3():
    x1 = float(input("number? "))
    x2 = float(input("number? "))
    x3 = float(input("number? "))

    # Use conditional statements instead of max function!
    if x1 > x2 and x1 > x3:
        mx = x1
    elif x2 > x1 and x2 > x3:
        mx = x2
    else:
        mx = x3


    print("Maximum:", mx)

# Exercise 3 - Write a program that reads an integer and shows a message indicating whether the number is even or odd
def even_or_odd():
    number = int(input("number? "))
    if number % 2 == 0: 
        result = "even"
    else:
        result = "odd" 
    
    print("The inputed number is {}.".format(result))

# Exercise 4 - Create a program that asks the number of fuel litres of a supply and determines the price to pay
def fuel_price():
    litres = float(input("How many litres? "))
    cost = 1.4 * litres
    if litres > 40:
        cost = 0.9 * cost
    
    print("The amount is {}€".format(cost))

# Exercise 5 - Execute the age.py program. Detect and fix the semantic error. Re-write the code with an if-elif-else instruction
# Semantic error : the age 13 is classified as adult
def age():
    age = int(input("Age? "))

    print("Age:", age)

    if age < 13 :
        cat = "child"
    elif age < 20:
        cat = "teenager"
    else:
        cat = "adult"

    print("Category:", cat)

# Exercise 6 - The imc.py program determines the BMI of the user and classifies it into just two categories. Modify it to return one out of 4 categories
def imc():
    print("Body Mass Index")

    height = float(input("Height (m)? "))
    weight = float(input("Weight (kg)? "))

    imc = weight / height**2

    print("IMC:", imc, "kg/m2")

    # Determine BMI category:
    if imc < 18.5:
        categoria = "Skinny"
    elif imc < 25:
        categoria = "Healthy"
    elif imc < 30:
        categoria = "Strong"
    else:
        categoria = "Obese"

    print("Categoria:", categoria)

# Exercise 7 - Detect the syntactic error reported in the kryptonite.py file and fix it. Why is there a TypeError now? Fix it. Now, modify the conditional instructions to fix the semantic errors
def kryptonite():
    print("Kryptonite phase classifier")

    # Input.  (You can fix the runtime error by changing something here!)
    T = int(input("Temperature (K)? "))
    P = int(input("Pressure (kPa)? "))

    # Determine the phase. (This is wrong! Fix to match phase diagram.)
    if P > 50.0 and T > 400.0:
        phase = "LIQUID"
    elif 50*T > -400*P and T < 400.0:
        phase = "SOLID"
    else:
        phase = "GAS"

    # Output.  (There's a subtle syntax error here!)
    print("At {} K and {} kPa, Kryptonite is in the {} phase.".format(T, P, phase))

# Exercise 8 - Write a program that asks for the grades of two evaluation components, CTP and CP, and calculates the final grade (integer) of a Programming Fundamentals student. If any of the components is lower than the minimum threshold, the final grade should be code 66. If the final grade is negative, the program should ask the appeal grades, ATPR and APR, and calculate the new final grade
def pf_grade():
    ctp = float(input("What was your Theorectical Component grade? "))
    cp = float(input("What was your Practical Component grade? "))
    
    if ctp < 7.0 or cp < 7.0:
        final_grade = 66
    else: 
        final_grade = 0.70 * cp + 0.30 * ctp
    
    if final_grade < 9.5:
        atpr = float(input("What was your Appeal Theoretical grade? "))
        apr = float(input("What was your Appeal Practical grade? "))
        final_grade = int(0.5 * atpr + 0.5 * apr)
    
    
    print("Final Grade: {}".format(final_grade))

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
        
        if choice==1:     
            print("Exercise 1: \n")
            max2()
        elif choice==2:     
            print("Exercise 2: \n")
            max3()
        elif choice==3:     
            print("Exercise 3: \n")
            even_or_odd()
        elif choice==4:
            print("Exercise 4: \n")
            fuel_price()
        elif choice==5:     
            print("Exercise 5: \n")
            age()
        elif choice==6:
            print("Exercise 6: \n")
            imc()
        elif choice==7:
            print("Exercise 7: \n")
            kryptonite()
        elif choice==8:
            print("Exercise 8: \n")
            pf_grade()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()


