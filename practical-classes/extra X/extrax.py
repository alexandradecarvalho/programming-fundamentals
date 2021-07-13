# Alexandra de Carvalho, 13 jul 2021


# Exercise 1a) - The program must present a menu and process each chosen option
def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1) Register call")
    print("2) Read file")
    print("3) List clients")
    print("4) Bill")
    print("5) Exit")
    print("Option? ")

def ex1():
    loop = True
    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [5-9] or 0 to quit: "))
        except:
            choice = 222    # Invalid option

    if choice==1:
        print("Register Call: \n")
    elif choice==2:     
        print("Read File: \n")
    elif choice==3:     
        print("List Clients: \n")
    elif choice==4:     
        print("Bill: \n")
    elif choice==5:     
        print("Goodbye")
        loop=False # This will make the while loop to end as not value of loop is set to False
    else:
        # Any integer inputs other than values 1-5 we print an error message
        print("Wrong option selection. Enter any key to try again..")


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 1")
    print("2. Exercise 2")
    print("3. Exercise 3")
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
            print("Exercise 2: \n")
            ex1()
        elif choice==2:     
            print("Exercise 2: \n")
            ex2()
        elif choice==3:     
            print("Exercise 3: \n")
            print(ex3())
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()