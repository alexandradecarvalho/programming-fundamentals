# Alexandra de Carvalho, 13 jun 2021

from numpy import arcsin
import math

# Exercise 1 - Write a program that reads a value1 of temperature in Celsius degrees, converts it into Fahrenheit degrees and prints the result
def temperature_converter():
    c = float(input("Write a temperature in Celsius degrees: "))
    f = 1.8*c + 32
    print("{} oC = {} oF".format(c, f))

# Exercise 2 - Write a program that asks both values, v1 and v2, and calculates and prints the average speed of the whole trip
def average_speed():
    v1 = float(input("Write the average speed of the first trip, v1: "))
    v2 = float(input("Write the average speed of the second trip, v2: "))
    average = (2 * v1 * v2) / (v1+v2)
    print(average)

# Exercise 3 - Ask the user their name and the year they were born to print them a message about what age they will have in 2030
def idade():
    name = input("What is your name? ")
    year = int(input("In what year were you born? "))
    age = 2030 - year
    print("{}, in 2030 you will be {} years old.".format(name, age))

# Exercise 4 - Write a program in which, given a time in seconds, shows in the console the time with the format hh:mm:ss
def time_format():
    seconds = int(input("Please, write a time duration, in seconds: "))
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = (seconds % 3600) % 60
    print("{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds))

# Exercise 5 - In a building with 4 floors (including the ground-level floor) and a tenant by floor, the elevator goes up and down 2 times a day per tenant. If every floor has a height of 3m, how many km the elevator does in a year? Considering that the elevator travels at a constant speed of 1m/s, how many hours does this elevator work in a year?
def elevator():
    ground_level_tenant = 3*0*2*365 / 1000  # 3m * 0 floors * 2 times a day * 365 days a year / conversion to km
    tenant_1floor = 3*1*2*365 / 1000  # 3m * 1 floor * 2 times a day * 365 days a year / conversion to km
    tenant_2floor = 3*2*2*365 / 1000  # 3m * 2 floors * 2 times a day * 365 days a year / conversion to km
    tenant_3floor = 3*3*2*365 / 1000  # 3m * 3 floors * 2 times a day * 365 days a year / conversion to km
    kms = ground_level_tenant + tenant_1floor + tenant_2floor + tenant_3floor
    print("The elevator des {} km in a year".format(kms))

    meters = kms * 1000
    seconds = meters
    hours = seconds / 3600
    print("The elevator works {} hours a year".format(hours))


# Exercise 6 - Write a program that reads the length of the legs and determines the hypotenuse, as well as the angle (in degrees) between leg A and the hypotenuse
def hypotenuse_and_angle():
    a = float(input("Please, insert the length of leg A: "))
    b = float(input("Please, insert the length of leg B: "))
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    angle = arcsin(b * math.sin(90) / hypotenuse)

    print("Hypotenuse: {}".format(hypotenuse))
    print("Angle between hypotenuse and leg A: {}".format(angle))

# Exercise 7 - Complete the program points.py to calculate and print the distance between the points.
def points():
    x1 = float(input("x1? "))
    y1 = float(input("y1? "))
    x2 = float(input("x2? "))
    y2 = float(input("y2? "))
    distance = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))
    print(distance)

# Exercise 8 - How much would be the book store profit? How much has been collected in taxes? 
def bookstore():
    pf = 20
    pc = 24.95
    imp = 0.23 * pc
    spa = 0.2

    profit = ((pc - spa) / (1 + imp)) - pf 
    print("Bookstore profit: {}".format(profit))
    print("Taxes: {}".format(imp))

# Exercise 9 - If one leaves the house at 6:52 and goes 1 km walking (at the pace of 10 min per km), and then do a quick training of 3 km (at 6 min per km) and goes back home walking, at what time do they arrive home for breakfast?
def training_time():
    walking_minutes = (1*10) / 1    # 1 km - 10 mins as well as 1 km - x mins  ---> times 2 (going and coming back)
    training_minutes = (3*60) / 6    # 6 km - 60 mins as well as 3 km - x mins

    total_minutes = walking_minutes + training_minutes - 8

    print("One arrives for breakfast at {}:{}".format(int(total_minutes)//60 + 7, int(total_minutes) % 60))

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
            temperature_converter()
        elif choice==2:     
            print("Exercise 2: \n")
            average_speed()
        elif choice==3:     
            print("Exercise 3: \n")
            idade()
        elif choice==4:
            print("Exercise 4: \n")
            time_format()
        elif choice==5:     
            print("Exercise 5: \n")
            elevator()
        elif choice==6:
            print("Exercise 6: \n")
            hypotenuse_and_angle()
        elif choice==7:
            print("Exercise 7: \n")
            points()
        elif choice==8:
            print("Exercise 8: \n")
            bookstore()
        elif choice==9:
            print("Exercise 9: \n")
            training_time()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()


