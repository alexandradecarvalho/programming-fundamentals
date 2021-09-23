# Alexandra de Carvalho, 23 September 2021


import random


# Exercise 12.1 - Write a function that takes any number of arguments and returns their sum
def sumall(*args):
    res = 0
    for arg in args:
        res += arg
    return res


# Exercise 12.2 - Modify the sort_by_length function so that words with the same length appear in random order
def sort_by_length(words):
    t = []
    for word in words:
        t.append((len(word), random.random(), word))
    t.sort(reverse=True)
    res = []
    for length, rand, word in t:
        res.append(word)
    return res


# Exercise 12.3 - Write a function that takes a string and prints the letters in decreasing order of frequency
def most_frequent(string):
    frequencies = {}
    for letter in string:
        frequencies[letter] = frequencies.get(letter,0) + 1
    
    t = list(frequencies.items())
    t2 = sorted(t, key=lambda tpl: tpl[1], reverse=True)
    
    for element in t2:
        print(element[0])


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 12.1")
    print("2. Exercise 12.2")
    print("3. Exercise 12.3")
    print("4. Exercise 12.4")
    print("5. Exercise 12.5")
    print("6. Exercise 12.6")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-6] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            lst = []
            while True:
                try:
                    val = int(input("val? "))
                except ValueError:
                    print("I'm sorry, the number you introduced seemed to be invalid. Please try again")
                else:
                    if val == 0:
                        break
                    else:
                        lst += [val]
            if lst:
                print(sumall(*(tuple(lst))))
        elif choice==2:
            words = input('print your sentence:\n').split(' ')
            print(sort_by_length(words))
        elif choice==3:
            string = input('string:\n')
            most_frequent(string)
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()