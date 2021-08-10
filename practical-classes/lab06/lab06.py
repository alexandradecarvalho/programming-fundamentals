# Alexandra de Carvalho, 16 jun 2021


# Exercise 2a) - Create the inputFloatList() function which reads a sequence of numbers inputed by the user and returns them in a list
def inputFloatList():
    result = []
    user_input = input("number? ")
    while user_input != "":
        result += [float(user_input)]
        user_input = input("number? ")
    return result

# Exercise 2b) - Create the countLower(lst, v) function which calculates and returns the number of lst's elements that are lower than v
def countLower(lst, v):
    count = 0
    for element in lst:
        if element < v:
            count += 1
    return count

# Exercise 2c) - Create the minmax(lst) function which returns the maximum and the minimum values of a list, without using the min and the max functions
def minmax(lst):
    minimum = lst[0]
    maximum = lst[0]

    for element in lst:
        if element < minimum:
            minimum = element
        elif element > maximum:
            maximum = element
    
    return minimum, maximum

# Exercise 2d) - Use the functions above to create a program which reads a list of numbers, determines the average between the maximum and the minimum values and that counts how many numbers are inferior to that value
def ex2():
    user_list = inputFloatList()
    minimum, maximum = minmax(user_list)
    average = (minimum + maximum) / 2
    print("The average between the min and max numbers introduced is {}".format(average))
    print("{} numbers introduced are lower than the average".format(countLower(user_list, average)))


# Exercise 3a) - Complete the telToName function so that, given a phone number (and both lists), it can return the right name (or the number if it's not on the list)
def telToName(tel, telList, nameList):
    # your code here
    index = 0
    for number in telList:
        if number == tel:
            return nameList[index]
        index += 1
    return tel

# Exercise 3b) - Complete the nameToTels function so that, given part of a name, it can return the list of the matching numbers for names that include the searched part
def nameToTels(partName, telList, nameList):
    # your code here
    tels = []
    index = 0
    for name in nameList:
        if partName in name:
            tels += [telList[index]]
        index +=1
    if tels:
        return tels
    return partName 

# Exercise 3c) - Run the program to test these functions
def ex3():
    telList = ['975318642', '234000111', '777888333', '911911911']
    nameList = ['Angelina', 'Brad',      'Claudia',   'Bruna']

    # Test telToName:
    tel = input("Tel number? ")
    print( telToName(tel, telList, nameList) )
    print( telToName('234000111', telList, nameList) == "Brad" )
    print( telToName('222333444', telList, nameList) == "222333444" )

    # Test nameToTels:
    name = input("Name? ")
    print( nameToTels(name, telList, nameList) )
    print( nameToTels('Clau', telList, nameList) == ['777888333'] )
    print( nameToTels('Br', telList, nameList) == ['234000111', '911911911'] )


# Exercise 4 - Write a function that, given a list of football teams, generates a list of all matches that can be done
def footbal_matches(lst):
    matches = []
    for team1 in lst:
        for team2 in lst[-1::-1]:
            if team1 != team2:
                matches.append(tuple([team1, team2]))
    return matches

def ex4():
    teams_list = ['FCP', 'Belenenses', 'SLB', 'Boavista', 'Olhanense', 'SCP']
    print(footbal_matches(teams_list))


# Exercise 5 - Write a function that counts how many digits appear in a given string: countDigits("23 mil 456") should return 5
def countDigits(text):
    count = 0
    for letter in text:
        if letter.isdigit():
            count += 1
    return count

def ex5():
    text = input("Insert sentence: ")
    print("\"{}\" has {} digits".format(text, countDigits(text)))


# Exercise 6 - Write a function that, given a name, creates a short version, formed only by the capital letters: shorten("Universidade de Aveiro") = "UA"
def shorten(text):
    result = ""
    for letter in text:
        if letter.isupper():
            result += letter
    return result
        
def ex6():
    text = input("Insert sentence: ")
    print(shorten(text))


# Exercise 7 - Write a ispalindrome(s) function that returns a boolean value indicating whether or not the string is a palindrome
def isPalindrome(s):
    while s:
        if s[0] != s[-1]:
            return False
        else:
            return isPalindrome(s[1:-1])
    return True

def ex7():
    s = (input("Insert sentence: "))
    if isPalindrome(s):
        print("\"{}\" is palindrome!".format(s))
    else:
        print("\"{}\" is not a palindrome :/".format(s))


# Exercise 8a) - Write a function that, given a string, returns another one, made up by all characters of even positions followed by all characters of odd positions of the first string 
def evenThenOdd(s):
    return s[::2] + s[1::2]
    
# Exercise 8b) - Write a function that, given a string s, returns a similar string but without duplicate adjacent characters
def noAdjacent(s):
    result = s[0]
    index = 1
    while index < len(s):
        if s[index] != s[index-1]:
            result += s[index]
        index += 1
    return result

#Exercise 8c) - Write a function that, given a non-negative integer n, returns a list with 1,2,2,3,3,3,4,4,4,... until n repeated n times
def repeatNTimes(n):
    result = []
    current_int = 1
    while current_int <= n:
        count = 0
        while count < current_int:
            result.append(current_int)
            count += 1
        current_int += 1
    return result

# Exercise 8d) - Write a function that, given a not-empty list of values, returns the index of the first occurrence of the highest value, without using the functions max, find or index
def firstHighestValue(input_list):
    highest = input_list[0]
    index = 0
    result = 0
    for elem in input_list:
        if elem > highest:
            highest = elem
            result = index
        index += 1
    return result

def ex8():
    user_string = input("string? ")
    print("String with even positions then odd positions: \"{}\" \n".format(evenThenOdd(user_string)))
    print("String with no adjacent equal characters: \"{}\" \n".format(noAdjacent(user_string)))
    
    user_input = int(input("number? "))
    print("List of repeatNTimes: {} \n".format(repeatNTimes(user_input)))
    
    user_list = []
    elem = input("list element? ")
    while elem != "":
        user_list += [int(elem)]
        elem = input("list element? ")
    print("Highest value is at position {} \n".format(firstHighestValue(user_list)))

##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("2. Exercise 2")
    print("3. Exercise 3")
    print("4. Exercise 4")
    print("5. Exercise 5")
    print("6. Exercise 6")
    print("7. Exercise 7")
    print("8. Exercise 8")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input("Enter your choice [1-8] or 0 to quit: "))
        except:
            choice = 222
        
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
            ex5()
        elif choice==6:
            print("Exercise 6: \n")
            ex6()
        elif choice==7:
            print("Exercise 7: \n")
            ex7()
        elif choice==8:
            print("Exercise 8: \n")
            ex8()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()