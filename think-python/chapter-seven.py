# Alexandra de Carvalho, 17 september 2021

# Exercise 7.1 - Rewrite the function print_n from Section 5.8 using iteration instead of recursion
def print_n(s, n):
    while n > 0:
        print(s)
        n=n-1

        
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
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()