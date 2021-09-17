# Alexandra de Carvalho, 17 september 2021

# Exercise 9.1 - Write a program that reads words.txt and prints only the words with more than 20 characters (not counting whitespace)
def long_words():
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            word = line.strip()
            if len(word) > 20:
                print(word)
        f.close()


# Exercise 9.2 - Write a function that returns True if the given word doesn’t have the letter “e” in it
def has_no_e(word):
    if 'e' in word:
        return False
    else:
        return True

# Exercise 9.2 - Modify the last exercise to print only the words that have no “e” and compute the percentage of the words in the words.txt list that have no “e”
def words_without_e():
    total_words = 0
    words_without_e = 0
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            word = line.strip()
            total_words += 1

            if has_no_e(word):
                print(word)
                words_without_e += 1
        f.close()
    return words_without_e/total_words


# Exercise 9.3 - Write a function that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letters
def avoids(word, forbidden_letters):
    for letter in forbidden_letters:
        if letter in word:
            return False
    
    return True

# Exercise 9.3 - Modify your program to prompt the user to enter a string of forbidden letters and then print the number of words that don’t contain any of them
def forbid():
    count = 0
    forbidden_letters = input('Forbidden Letters: ')
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            word = line.strip()
            if avoids(word, forbidden_letters):
                count += 1
        f.close()
    return count


# Exercise 9.4 - Write a function that takes a word and a string of letters, and that returns True if the word contains only letters in the list
def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True


# Exercise 9.5 - Write a function that takes a word and a string of required letters, and that returns True if the word uses all the required letters at least once
def uses_all(word, required_letters):
    for letter in required_letters:
        if letter not in word:
            return False
    return True


# Exercise 9.6 - Write a function that returns True if the letters in a word appear in alphabetical order (double letters are ok)
def is_abecedarian(word):
    for index in range(len(word)-1):
        if word[index] > word[index+1]:
            return False
    return True


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 9.1")
    print("2. Exercise 9.2")
    print("3. Exercise 9.3")
    print("4. Exercise 9.4")
    print("5. Exercise 9.5")
    print("6. Exercise 9.6")
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
            long_words()
        elif choice==2:
            print('Percentage of words without e: {}%'.format(words_without_e()*100))
        elif choice==3:
            print('There are {} words without the mentioned forbidden letters.'.format(forbid()))
        elif choice==4:
            word = input("word: ")
            letters = input("letters: ")
            print(uses_only(word,letters))
        elif choice==5:
            word = input("word: ")
            letters = input("required letters: ")
            print(uses_all(word,letters))
        elif choice==6:
            word = input('word: ')
            print(is_abecedarian(word))

            words_abc = 0
            try:
                f = open('words.txt', 'r')
            except IOError:
                print('ERROR: Words File not found')
            else:
                for line in f:
                    word = line.strip()

                    if is_abecedarian(word):
                        words_abc += 1
                f.close()
            print(words_abc)
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()