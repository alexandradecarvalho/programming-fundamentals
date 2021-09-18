# Exercise 11.1 - Write a function that reads the words in words.txt and stores them as keys in a dictionary
def words_in_dict():
    result = dict()
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            result[line.strip()] = 1
        f.close()
    return result

def exists(s):
    return s in words_in_dict()


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 11.1")
    print("2. Exercise 11.2")
    print("3. Exercise 11.3")
    print("4. Exercise 11.4")
    print("5. Exercise 11.5")
    print("6. Exercise 11.6")
    print("7. Exercise 11.7")
    print("8. Exercise 11.8")
    print("9. Exercise 11.9")
    print("10. Exercise 11.10")
    print("11. Exercise 11.11")
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
            word = input('word: ')
            print(exists(word))
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()