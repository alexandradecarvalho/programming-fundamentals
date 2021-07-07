# Alexandra de Carvalho, 07 jul 2021


import sys


# Exercise 2 - Write a program that determines the frequency of the occurrence of all letters from a text file whose name should be passed as a command line argument, not distinguishing upper and lower cases, and showing the results in alphabetical order
def frequencyOfLetters(filename):
    frequency_results = {}
    try:
        f = open(filename, 'r')
    except IOError:
        print('ERROR: File not found')
    else:
        for line in f:
            for character in line:
                if character.isalpha():
                    frequency_results[character.lower()] = frequency_results.get(character.lower(),0) + 1
    return frequency_results 

def ex2():
    file = sys.argv[1]
    results = frequencyOfLetters(file)

    for letter in sorted(results.keys()):
        print(letter,results[letter]) 


# Exercise 3a) - Add the "add contact" operation that asks for a name and a number and adds it to the dictionary
def menu():
    """Shows the menu and gets user option."""
    print()
    print("(L)ist contacts")
    print("(A)dd contact")
    print("(R)emove contact")
    print("Search (N)umber")
    print("Search (P)art of name")
    print("(T)erminate\n")
    op = input("option? ").upper()   # converts to uppercase...
    return op

def listContacts(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {}".format("Numero", "Nome"))
    for num in dic:
        print("{:>12s} : {}".format(num, dic[num]))

def addContact(dic):
    name = input("Name: ")
    number = input("Number: ")
    dic[number] = name
    print("Contact added!")

# Exercise 3b) - Add the "remove contact" operation that asks for the number and deletes the correspondent item
def removeContact(dic):
    number = input("Number to delete: ")
    if number in dic:
        del dic[number]
    print("Contact removed!")

# Exercise 3c) - Add the "find number" operation  that asks for a number and shows the correspondent name, if it exists, or the number itself otherwise
def findNumber(dic):
    number = input("Number to find: ")
    if number in dic:
        return dic[number]
    else:
        return number

# Exercise 3d) - Complete the filterPartName function, which given a string, should return a dictionary with the contacts (name: number) whose names include that string, which should be used to implement the "search part of the name" operation, asking for a partial name and listing all contacts who contain it
def filterPartName(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    possible_contacts = {}
    for number,name in contacts.items():
        if partName.lower() in name.lower():
            possible_contacts[name] = number
    return possible_contacts

def ex3():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos = {"234370200": "Universidade de Aveiro",
        "727392822": "Cristiano Aveiro",
        "387719992": "Maria Matos",
        "887555987": "Marta Maia",
        "876111333": "Carlos Martins",
        "433162999": "Ana Bacalhau"
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contacts:")
            listContacts(contactos)
        elif op == "A":
            addContact(contactos)
            listContacts(contactos)
        elif op == "R":
            removeContact(contactos)
            listContacts(contactos)
        elif op == "N":
            print("Contact found: {}".format(findNumber(contactos)))
        elif op == "P":
            partName = input("Search: ")
            print("Matching Contacts: ")
            listContacts(filterPartName(contactos,partName))
        else:
            print("Not implemented!")


# Exercise 4 - Alter the previous program to save the final table in a text file, using the write method or the print function with the file= argument
def printOrSavePauta(lst, filename="InvalidFilename"):
    if filename == "InvalidFilename":
        print("{:<10}{:^60}{:<10}".format("Number", "Name", "Grade"))
        for student_record in lst:
            print("{:<10}{:^60}{:<10.2f}".format(student_record[0], student_record[1], notaFinal(student_record)))
    else:
        f = open(filename, 'w')
        f.write("{:<10}{:^60}{:<10}".format("Number", "Name", "Grade"))
        for student_record in lst:
            f.write("{:<10}{:^60}{:<10.2f}".format(student_record[0], student_record[1], notaFinal(student_record)))
        f.close()


def ex4():
    filename = 'school.csv'
    student_records = loadFile(filename)
    filename = input("Insert filename: ")
    if filename:
        printOrSavePauta(student_records, filename)
    else:
        printOrSavePauta(student_records)


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
def floatInputOptionallyInRange(prompt):
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
    if len(sys.argv) != 3:
        print("ERROR: Invalid Arguments during Program Call")
    else:
        print("Are {} and {} equal files? {}".format(sys.argv[1], sys.argv[2],compareFiles(sys.argv[1], sys.argv[2])))


# Exercise 7 - Create a function that goes through a directory (with os.listdir) and shows the size of each file
def directorysFileSizes(dir):
    pass

##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
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
        
        if choice==2:     
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
            if len(user_input) != 2:
                floatInputOptionallyInRange("val? ")
            else:
                min = float(user_input[0])
                max = float(user_input[1])
                floatInputOptionallyInRange("val? ", min, max)
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