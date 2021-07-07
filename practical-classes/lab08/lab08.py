# Alexandra de Carvalho, 07 jul 2021


import os
import turtle
import math
import sys


# Exercise 1 - Create a program that calculates the sum of a list of values, stored in a inputted file with only one value per line
def sumOfValuesOfAFile():
    inputted_filename = input("Please, introduce a file.")
    sum_of_values = 0
    try:
        f = open(inputted_filename, 'r')
    except IOError:
        print('ERROR: File not found')
    else:
        for line in f:
            try:
                number = float(line)
            except ValueError:
                print('ERROR: file has invalid elements')
            else:
                sum_of_values += number
        f.close()
        
        print("Sum of values: {}".format(sum_of_values))


# Exercise 2 - Complete the program turtledraw.py to read the instructions off of a file and use the turtle to draw
def turtledraw():
    # Exercise 5 on "How to think...", ch. 11.

    t = turtle.Turtle()
    filename = 'mystery.txt'

    try:
        f = open(filename, 'r')
    except IOError:
        print('ERROR: File not found')
    else:
        for line in f:
            if line == 'UP\n':
                t.up()
            elif line == 'DOWN\n':
                t.down()
            else:
                coordinates = line.split(" ")
                if len(coordinates) != 2:
                    print('ERROR: File has invalid instructions')
                else:
                    try:
                        x_value = float(coordinates[0])
                        y_value = float(coordinates[1])
                    except ValueError:
                        print('ERROR: file has invalid instructions')
                    else:
                        t.goto(x_value,y_value)
        f.close()

    # wait 
    turtle.Screen().exitonclick()
    turtle.TurtleScreen._RUNNING = True # not to throw Terminator error


# Exercise 3a) - Complete the loadFile(fname) function so that, given a file name with the right format, reads its content and returns a list of a tuple (number, name, grade1, grade2, grade3) by student
def loadFile(fname):
    lst = []

    try:
        f = open(fname, 'r')
    except IOError:
        print('ERROR: File not found')
    else:
        for line in f:
            if line != "Numero\tNome\tCurso\tRegime\tDataInscricao\tnota1\tnota2\tnota3\n": # ignoring header line
                line_content_list = line.strip("\n").split("\t")
                try:
                    student_number = int(line_content_list[0])
                    student_grade1 = float(line_content_list[5])
                    student_grade2 = float(line_content_list[6])
                    student_grade3 = float(line_content_list[7])
                except ValueError:
                    print("ERROR: Invalid values")
                else:
                    lst.append(tuple([student_number, line_content_list[1], student_grade1, student_grade2, student_grade3]))
        f.close()
    return lst


# Exercise 3b) - Create a notaFinal(reg) that, given a tuple with the record of a student, calculates and returns their final grade, the average of the three scores in the record
def notaFinal(reg):
    return (reg[2] + reg[3] + reg[4])/3
    

# Exercise 3c) - Create a printPauta(lst) function that, given a list of student records, shows a table with their names, numbers and final grades, formatted and with the name appearing centered and the number and grade appearing aligned to the right
def printPauta(lst):
    print("{:<10}{:^60}{:<10}".format("Number", "Name", "Grade"))
    for student_record in lst:
        print("{:<10}{:^60}{:<10.2f}".format(student_record[0], student_record[1], notaFinal(student_record)))


# Exercise 3d) - Using the functions above, complete the main function to read the file, sort the list with the .sort() method and show the final table
def ex3():
    filename = 'school.csv'
    student_records = loadFile(filename)
    printPauta(student_records)


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
def floatInputOptionallyInRange(prompt, min=-math.inf, max=math.inf):
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
    try:
        directorys_content = os.listdir(dir)
    except FileNotFoundError:
        print("ERROR: Invalid directory name")
    else:
        for item in directorys_content:

            if not os.path.isfile(item):
                print(item + ": " + str(os.stat(dir+'/'+item).st_size))

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
            sumOfValuesOfAFile()
        elif choice==2:     
            print("Exercise 2: \n")
            turtledraw()
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