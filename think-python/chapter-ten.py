# Alexandra de Carvalho, 17 september 2021

# Exercise 10.1 - Write a function that takes a nested list of integers and add up the elements from all of the nested lists
def nested_sum(outter_list):
    for lst in outter_list:
        print(lst)


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 10.1")
    print("2. Exercise 10.2")
    print("3. Exercise 10.3")
    print("4. Exercise 10.4")
    print("5. Exercise 10.5")
    print("6. Exercise 10.6")
    print("7. Exercise 10.7")
    print("8. Exercise 10.8")
    print("9. Exercise 10.9")
    print("10. Exercise 10.10")
    print("11. Exercise 10.11")
    print("12. Exercise 10.12")
    print("13. Exercise 10.13")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-13] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            outter_list = []
            while True:
                inpt = input("Please insert your list, with its elements separated by commas, or 'done' to terminate")
                if inpt == 'done':
                    break
                else:
                    inner_list = inpt.split(",")
                    list_numbers = []
                    for element in inner_list:
                        try:
                            list_numbers.append() = int(element)
                        except ValueError:
                            print("We're sorry! It seems thasat the element {} is not an integer!".format(element))
                            break
                        else:
                            outter_list.append(list_numbers)
            nested_sum(outter_list)
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()