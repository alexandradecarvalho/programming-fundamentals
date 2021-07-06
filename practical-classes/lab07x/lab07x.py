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
    pass

def ex4():
    assert matchesPattern("secret", "s?c??t") == True
    assert matchesPattern("socket", "s?c??t") == True
    assert matchesPattern("soccer", "s?c??t") == False
    assert matchesPattern("SEcrEt", "?ecr?t") == True, "should be case-insensitive"
    
    print("All tests passed!")

    #englishWords = load("/usr/share/dict/words")

    #lst = filterPattern(englishWords, "s?c??t")
    #print(lst)

    #assert isinstance(lst, list),  "result lst should be a list"
    #assert "secret" in lst,  "result should contain 'secret'"

    # Solution to "?YS???Y"
    #lst = filterPattern(englishWords, "?ys???y")
    #print(lst)


# Exercise 5a) - To deal with the problem of a user inputting a text that generates a ValueError during conversion, create a floatInput(prompt) function that reads and validates user input: it asks for a value, tries to convert it and, if it fails, warns the user and repeats everything
def floatInput(prompt):
    repeat = True
    while repeat:  
        inputted_number = input(prompt)
        try:
            converted_float = float(inputted_number) 
        except ValueError:
            print("Not a float!")
        else:
            repeat = False
            print(converted_float)


# Exercise 5b) - Add two arguments min and max, validate if the inputted value is inside the interval [min,max] and warn the user and repeat everything if it isn't
def isFloatInputInRange(prompt, min, max):
    repeat = True
    while repeat:  
        inputted_number = input(prompt)
        try:
            converted_float = float(inputted_number) 
        except ValueError:
            print("Not a float!")
        else:
            repeat = False
            if converted_float >= min and converted_float <= max:
                print(converted_float)
            else:
                print("Value should be in [{},{}]".format(min,max))


# Exercise 5c) - Make the min and max arguments optional so that, when omitted, the function accepts any real value
#def floatInputOptionallyInRange(prompt, min=-math.inf, max=math.inf):
#    repeat = True
#    while repeat:  
#        inputted_number = input(prompt)
 #       try:
  #          converted_float = float(inputted_number) 
   #     except ValueError:
    #        print("Not a float!")
     #   else:
      #      repeat = False
       #     if converted_float >= min and converted_float <= max:
        #        print(converted_float)
         #   else:
          #      print("Value should be in [{},{}]".format(min,max))


# Exercise 6 - Write a function compareFiles that verifies whether two given binary mode files are the same, reading and comparing in blocks of 1KiB at a time, and terminating as soon as it finds a difference
def compareFiles(filename1, filename2):
    try:
        f1 = open(filename1, 'rb')
        f2 = open(filename2, 'rb')
    except IOError:
        print("ERROR: Invalid filename(s)!")
        return None
    else:
        while ((kib1 := f1.read(1024)) and (kib2 := f2.read(1024))):
            if kib1 != kib2:
                return False
        
        f1.close()
        f2.close()
        return True


# Test the function in a program that receives the names of the files as arguments
def ex6():
    pass
#    if len(sys.argv) != 3:
#        print("ERROR: Invalid Arguments during Program Call")
#    else:
#        print("Are {} and {} equal files? {}".format(sys.argv[1], sys.argv[2],compareFiles(sys.argv[1], sys.argv[2])))


# Exercise 7 - Create a function that goes through a directory (with os.listdir) and shows the size of each file
def directorysFileSizes(dir):
    pass
#    try:
#        directorys_content = os.listdir(dir)
#    except FileNotFoundError:
#        print("ERROR: Invalid directory name")
#    else:
#        for item in directorys_content:
#
#            if not os.path.isfile(item):
#                print(item + ": " + str(os.stat(dir+'/'+item).st_size))

##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 1")
    print("2. Exercise 2")
    print("3. Exercise 3")
    print("4. Exercise 4")
    print("5. Exercise 5")
    print("6. Exercise 6")
    print("7. Exercise 7")
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
            user_input = input("Min,Max? ").split(",")
            #if len(user_input) != 2:
            #    floatInputOptionallyInRange("val? ")
            #else:
             #   min = float(user_input[0])
              #  max = float(user_input[1])
               # floatInputOptionallyInRange("val? ", min, max)
        elif choice==6:
            print("Exercise 6: \n")
            ex6()
        elif choice==7:
            print("Exercise 7: \n")
            directory_name = input("dir name? ")
            directorysFileSizes(directory_name)
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()