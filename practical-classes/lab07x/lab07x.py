# Alexandra de Carvalho, 02 jul 2021


# Exercise 1 - Complete the genFibonacci(n) function to return a list with the first n Fibonacci numbers, working only for n>=2 
def genFibonacci(n):
    """Generate list of first n Fibonacci numbers: [F0 (n=1), F1 (n=2), ..., Fn-1]."""
    # your code here
    sequence = [0]
    
    n2 = 1
    n1 = 0
    
    index = 1
    
    
    while index < n:
        index += 1
        new_value = n2 + n1
        sequence.append(new_value)
        n2 = n1
        n1 = new_value

    return sequence

def ex1():
    # Do tests:
    lst = genFibonacci(10)
    print(lst)      #-> [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    # Check the results we expect.
    # (If a condition fails, the assert statement raises an AssertionError!)

    assert isinstance(lst, list), "lst should be a list"
    assert lst == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

    assert genFibonacci(2) == [0, 1]
    assert genFibonacci(6) == [0, 1, 1, 2, 3, 5]

    # If the program reaches this point...
    print("All tests passed!")

    # Let the user try it:
    n = int(input("N? "))
    print("genFibonacci({}) -> {}".format(n, genFibonacci(n)))


# Exercise 2 - Write a function that verifies whether a string contains consecutive equal characters, based on the checkDoubles.py program, and verify it passes the tests, also adding a few more adequate ones
def containsDoubles(word):
    # Define the function containsDoubles here,
    # so that it passes all the tests below.
    if len(word) <= 1:
        return False
    else:
        if word[0] == word[1]:
            return True
        else:
            return containsDoubles(word[1:])

def ex2():
    # Test function
    assert containsDoubles("pool") == True
    assert containsDoubles("polo") == False
    assert containsDoubles("erro") == True
    assert containsDoubles("connosco") == True
    assert containsDoubles("banana") == False

    # Add a few more tests below
    assert containsDoubles("eel") == True
    assert containsDoubles("ball") == True
    assert containsDoubles("bola") == False
    assert containsDoubles("!!") == True

    # If the program reaches this point...
    print("All tests passed!")


# Exercise 3 - In the checkDoubles.py program, complete the findLinesWithDoubles function to find out the words of a file which have duplicate letters
def findLinesWithDoubles(fname):
    words_with_duplicated_sequencial_characters = []
    try:
        f = open(fname, 'r')
    except IOError:
        print('ERROR: File not found')
    else:
        for word in f:
            if containsDoubles(word):
                words_with_duplicated_sequencial_characters += [word]
        f.close()
    return words_with_duplicated_sequencial_characters

def ex3():
    # This should show a list of all English words with double letters.
    lst = findLinesWithDoubles("/usr/share/dict/words")
    print(lst)

    # You may download files with Portuguese words from:
    # http://natura.di.uminho.pt/download/sources/Dictionaries/wordlists/LATEST/
    # But you may need to open them with the argument: encoding="latin1".


# Exercise 4 - Complete the findWords.py program to find out the missing word by reading a list of English words from the /usr/share/dict/words file, which usually exists in Linux/Unix systems, and by writing the filterPattern(lst,pattern) to extract, from a list of strings, the one with the given pattern
def load(fname):
    with open(fname) as f:
        lst = []
        for line in f:
            word = line.strip()
            lst.append(word)
    return lst

def matchesPattern(s, pattern):
    if len(s) != (word_len:=len(pattern)):
        return False
    else:
        index = 0
        while index < word_len:
            if pattern[index] != "?":
                if s[index].lower() != pattern[index].lower():
                    return False
            index += 1
    return True

def filterPattern(lst, pattern):
    matching_words = []
    for word in lst:
        if matchesPattern(word, pattern):
            matching_words += [word]
    return matching_words

def ex4():
    assert matchesPattern("secret", "s?c??t") == True
    assert matchesPattern("socket", "s?c??t") == True
    assert matchesPattern("soccer", "s?c??t") == False
    assert matchesPattern("SEcrEt", "?ecr?t") == True, "should be case-insensitive"
    
    print("All tests passed!")

    englishWords = load("/usr/share/dict/words")

    lst = filterPattern(englishWords, "s?c??t")
    print(lst)

    assert isinstance(lst, list),  "result lst should be a list"
    assert "secret" in lst,  "result should contain 'secret'"

    # Solution to "?YS???Y"
    lst = filterPattern(englishWords, "?ys???y")
    print(lst)


# Exercise 5a) - The printTable function must print a table with four columns: name, weight, height and body mass index (BMI) which is calculated by weight/height, with the numeric columns aligned to the right and with a fixed number of decimals
def printTable(list_of_people):
    print("\n{:<20}   {:>5}  {:>6}  {:>6}".format("Name","Weight","Height","BMI"))
    for person in list_of_people:
        print("{:<20}   {:>6.0f}  {:>6.2f}  {:>6.1f}".format(person[0],person[1],person[2],person[1]/(person[2]**2)))
    print("\n")

# Exercise 5b) - The inputBetween function must ask for and return a value introduced by the user, but only if is between the established limits, otherwise, it must warn the user and ask for the value again until it falls under the acceptable range
def inputBetween(prompt, min, max):
    while True:
        introduced_value = input(prompt)
        try:
            introduced_value = float(introduced_value)
        except ValueError:
            print("ERROR: Introduced value is not a valid number")
        else:
            if introduced_value > min and introduced_value < max:
                return introduced_value
            else:
                print("Value must be in [{},{}]!".format(min, max))

# Exercise 5c) - The selectTaller must return a list with the records of all people taller than the the given threshold
def selectTaller(list_of_people, limit):
    taller_people = []
    for person in list_of_people:
        if person[2] > limit:
            taller_people += [person]
    return taller_people

def ex5():
    # Lista de pessoas com nome, peso em kg, altura em metro.
    people = [("John", 64.5, 1.757),
        ("Berta", 64.0, 1.612),
        ("Maria", 45.1, 1.715),
        ("Andy", 98.3, 1.81),
        ("Lisa", 46.8, 1.622),
        ("Kelly", 83.2, 1.78)]

    # Imprime os dados numa tabela com 4 colunas: nome, peso, altura e IMC.
    printTable(people)
    
    # Pede e devolve um valor, mas só aceita se estiver no intervalo certo.
    limit = inputBetween("altura minima? ", 1.1, 2.5)
    
    # Extrai uma lista de pessoas com altura superior a limit.
    tallpeople = selectTaller(people, limit)
    
    # Mostra uma tabela só com as pessoas altas.
    printTable(tallpeople)


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 1")
    print("2. Exercise 2")
    print("3. Exercise 3")
    print("4. Exercise 4")
    print("5. Exercise 5")
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
        elif choice==2:     
            print("Exercise 2: \n")
            ex2()
        elif choice==3:     
            print("Exercise 3: \n")
            ex3()
        elif choice==4:
            print("Exercise 4: \n")
            ex4()
        elif choice==5:     
            print("Exercise 5: \n")
            ex5()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()