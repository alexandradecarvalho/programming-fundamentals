# Alexandra de Carvalho, 17 september 2021


# Exercise 10.1 - Write a function that takes a nested list of integers and add up the elements from all of the nested lists
def nested_sum(outter_list):
    result = []
    for lst in outter_list:
        result.append(sum(lst))
    return result

def is_numeric(lst):
    for element in lst:
        try:
            n = int(element)
        except ValueError:
            print("We're sorry! It seems that the element {} is not an integer!".format(element))
            return False

    return True


# Exercise 10.2 - Use the provided capitalize_all function to write a function that takes a nested list of strings and returns a new nested list with all strings capitalized
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(outter_list):
    resultant_list = []
    for lst in outter_list:
        resultant_list.append(capitalize_all(lst))
    return resultant_list


# Exercise 10.3 - Write a function that takes a list of numbers and returns the cumulative sum, that is, a new list where the ith element is the sum of the first i + 1 elements from the original list
def cumulative_sum(numbers):
    result = []
    for i in range(len(numbers)):
        result.append(sum(numbers[:i+1]))
    return result


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
                inpt = input("Please insert your list, with its elements separated by commas, or 'done' to terminate\n")
                if inpt == 'done':
                    break
                else:
                    inner_list = inpt.split(",")
                    if is_numeric(inner_list):
                        resultant_list = []
                        for i in range(len(inner_list)):
                            resultant_list.append(int(inner_list[i]))
                        outter_list.append(resultant_list)
            print(nested_sum(outter_list))
        elif choice==2:
            outter_list = []
            while True:
                inpt = input("Please insert your list, with its elements separated by commas, or 'done' to terminate\n")
                if inpt == 'done':
                    break
                else:
                    outter_list.append(inpt.split(","))
            print(capitalize_nested(outter_list))
        elif choice==3:
            while True:
                inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
                if is_numeric(inpt):
                    resultant_list = []
                    for i in range(len(inpt)):
                        resultant_list.append(int(inpt[i]))
                    print(cumulative_sum(resultant_list))
                    break
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()