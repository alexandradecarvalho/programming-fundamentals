# Alexandra de Carvalho, 12 jul 2021


import os


# Exercise 1 - Try to detect the cause of the errors in recErrors.py and fix the mistakes
def fact(n):                # n! = n*(n-1)!
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

def gcd(b, a):              # Euclidean Algorithm
    if b == 0:
        return a
    return gcd(a%b, b)

def ex1():
    print( fact(4) )        # 24
    print( fact(5) )        # 120

    x = 2*27*53*61
    y = 2*2*17*23*53
    print(x, y, gcd(x, y))
    assert gcd(x, y) == 2*53
    print("Asserted gdc! Well done!")


# Exercise 2 - Write a general function, genWords, that generates all words of length n, getting a list of words of size n-1 and, to each of them, adding each symbol of the alphabet. What will the base case be? And what is its result?
def genWords3(symbols): # Generates all length-3 words with symbols taken from the given alphabet
    return [ x+y+z for x in symbols for y in symbols for z in symbols ]

def genWords(symbols, n):   # Generates all length-n words with symbols taken from the given alphabet
    if n > 1:
        return [word+suffix for word in genWords(symbols,n-1) for suffix in symbols]
    return symbols

def ex2():
    lstA = genWords3("abc")
    print(lstA)

    lstB = genWords("abc", 3)  # should return the same words, maybe in other order
    print(lstB)
    assert sorted(lstA) == sorted(lstB)

    lstC = genWords("01", 4)  # should return all length-4 binary words
    print(lstC)


# Exercise 3 - In the findFiles.py, create a findFiles function that returns a list with the names of all files with a given extension in a given directory, recursively going through all subdirectories
def printDirFiles(d):
    lst = os.listdir(d)
    for fname in lst:
        path = os.path.join(d, fname)
        if os.path.isfile(path):
            ftype = "FILE"
        elif os.path.isdir(path):
            ftype = "DIR"
        else:
            ftype = "?"
        print(ftype, path)

def findFiles(path, ext):
    lst = os.listdir(path)
    return [element for element in [fname for fname in os.listdir(path) if os.path.isfile(os.path.join(path, fname)) and fname.split(".")[1] == ext[1:]] + [findFiles(os.path.join(path, subpath), ext) for subpath in os.listdir(path) if os.path.isdir(os.path.join(path, subpath))] if element]

def ex3():
    printDirFiles("..")

    # Test findFiles:
    lst = findFiles(".", ".py")
    print(lst)
    assert isinstance(lst, list)

    lst = findFiles("..", ".csv")
    print(lst)



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
            choice = int(input("Enter your choice [1-3] or 0 to quit: "))
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