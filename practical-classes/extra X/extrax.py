# Alexandra de Carvalho, 13 jul 2021


# Exercise 1a) - The program must present a menu and process each chosen option
def print_menu_ex1():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1) Register call")
    print("2) Read file")
    print("3) List clients")
    print("4) Bill")
    print("5) Exit")

# Exercise 1b) - Write a function to validate a phone number - a string with at least 3 digits (0-9), optionally with a '+' symbol in the beginning
def isValidPhone(phone_number):
    if phone_number[0] == '+':
        phone_number = phone_number[1:]
    
    if len(phone_number) < 3:
        return False
    
    try:
        phone_number = int(phone_number)
    except ValueError:
        return False
    else:
        return True

# Exercise 1c) - Add the option to register a new call (from the keyboard) using the previous function in order to validate the origin and destiny phone numbers
def registerCall():
    origin_phone_number = ""
    while not origin_phone_number or not isValidPhone(origin_phone_number):
        origin_phone_number = input("Origin Phone Number? ")
    
    destiny_phone_number = ""
    while not destiny_phone_number or not isValidPhone(destiny_phone_number):
        destiny_phone_number = input("Destiny Phone Number? ")
    
    while True:
        duration = input("Duration (s)? ")
        try:
            duration = int(duration)
        except ValueError:
            print("ERROR: Invalid duration, please insert a number")
        else:
            break

# Exercise 1d) - Develop an option to read a file of calls that, in each call, is registered 3 "words" separated by white spaces: the origin number, the destiny number and the duration in seconds
def read_file(fname):
    calls = []
    try:
        f = open(fname,'r')
    except IOError:
        print("ERROR while opening file "+fname)
    else:
        for line in f:
            call = tuple(line.replace("\n","").split("\t"))
            calls += [call]
        f.close()
    return calls

def ex1():
    register_loop = True
    while register_loop:
        print_menu_ex1()
        try:
            option = int(input("Option? "))
        except:
            option = 222    # Invalid option

        if option==1:
            registerCall()
        elif option==2:     
            print(read_file('chamadas1.txt'))
            print(read_file('chamadas2.txt'))
        elif option==3:     
            print("List Clients: \n")
        elif option==4:     
            print("Bill: \n")
        elif option==5:     
            print("Goodbye")
            register_loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 1")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [5-9] or 0 to quit: "))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            print("Exercise 1: \n")
            ex1()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()