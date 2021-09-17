# Alexandra de Carvalho, 17 september 2021


# Exercise 8.1 - Write a function that takes a string as an argument and displays the letters backward, one per line
def backwards(string):
    n = -1
    while n >= - len(string):
        print(string[n])
        n-=1


# Exercise 8.2 - Modify the program in page 73 to fix the error
def ducklings():
    prefixes = 'JKLMNOPQ'

    for letter in prefixes:
        if (letter=='O') or (letter=='Q'):
            suffix = 'uack'
        else:
            suffix = 'ack'
        print(letter + suffix)


# Exercise 8.4 - Modify the function of page 74 so that it has a third parameter, the index in word where it should start looking
def find(word, letter, start):
    index = start
    while index < len(word):
        if word[index] == letter:
            return index
        index = index + 1
    return -1


# Exercise 8.5 - Encapsulate the code of page 75 in a function, and generalize it so that it accepts the string and the letter as arguments
def count(word, wanted_letter):
    count = 0
    for letter in word:
        if letter == wanted_letter:
            count = count + 1
    print(count)


# Exercise 8.6 - Rewrite the function above so that instead of traversing the string, it uses the three-parameter version of find
def count_with_find(word, wanted_letter):
    count = 0
    start_index = 0
    while True:
        result_index = find(word, wanted_letter, start_index)
        if result_index != -1:
            count = count + 1
            start_index = result_index + 1
        else:
            break
    print(count)



##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 8.1")
    print("2. Exercise 8.2")
    print("4. Exercise 8.4")
    print("5. Exercise 8.5")
    print("6. Exercise 8.6")
    print("7. Exercise 8.7")
    print("9. Exercise 8.9")
    print("10. Exercise 8.10")
    print("11. Exercise 8.11")
    print("12. Exercise 8.12")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-2,4-7,9-12] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            s = input('word or sentence?\n')
            backwards(s)
        elif choice==2:
            ducklings()
        elif choice==4:
            word = input('word: ')
            letter = input('searched letter: ')
            while True:
                try:
                    start_index = int(input("start index? "))
                except ValueError:
                    print("I'm sorry, the introduced index seems to be invalid. Please try again")
                else:
                    break
            print(find(word,letter,start_index))
        elif choice==5:
            word = input('word: ')
            letter = input('searched letter: ')
            count(word,letter)
        elif choice==6:
            word = input('word: ')
            letter = input('searched letter: ')
            count_with_find(word,letter)   
        elif choice==7:
            # Exercise 8.7 - Write an invocation of the method count that counts the number of a's in 'banana'
            word = 'banana'
            print(word.count('a'))
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()