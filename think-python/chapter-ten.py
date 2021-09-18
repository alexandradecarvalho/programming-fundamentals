# Alexandra de Carvalho, 17 september 2021


# Exercise 10.1 - Write a function that takes a nested list of integers and add up the elements from all of the nested lists
def nested_sum(outter_list):
    result = []
    for lst in outter_list:
        result.append(sum(lst))
    return result

def is_numeric(lst):
    for element in lst:
        try:
            n = int(element)
        except ValueError:
            print("We're sorry! It seems that the element {} is not an integer!".format(element))
            return False

    return True


# Exercise 10.2 - Use the provided capitalize_all function to write a function that takes a nested list of strings and returns a new nested list with all strings capitalized
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

def capitalize_nested(outter_list):
    resultant_list = []
    for lst in outter_list:
        resultant_list.append(capitalize_all(lst))
    return resultant_list


# Exercise 10.3 - Write a function that takes a list of numbers and returns the cumulative sum, that is, a new list where the ith element is the sum of the first i + 1 elements from the original list
def cumulative_sum(numbers):
    result = []
    for i in range(len(numbers)):
        result.append(sum(numbers[:i+1]))
    return result

    
# Exercise 10.4 - Write a function that takes a list and returns a new list that contains all but the first and last elements
def middle(lst):
    return lst[1:-1]


# Exercise 10.5 - Write a function that takes a list, modifies it by removing the first and last elements, and returns None
def chop(lst):
    del lst[0]
    del lst[-1]
    return None


# Exercise 10.6 - Write a function that takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise
def is_sorted(lst):
    for idx in range(len(lst)-1):
        if lst[idx] > lst[idx+1]:
            return False
    return True


# Exercise 10.7 - Write a function that takes two strings and returns True if they are anagrams
def is_anagram(s1, s2):
    for letter in s1:
        if letter not in s2:
            return False

    for letter in s2:
        if letter not in s1:
            return False
    
    return True


# Exercise 10.8 - Write a function that takes a list and returns True if there is any element that appears more than once
def has_duplicates(lst):
    for idx in range(len(lst)):
        new_list = lst[:]
        element = new_list.pop(idx)
        if element in new_list:
            return True
    return False


# Exercise 10.9 - Write a function that takes a list and returns a new list with only the unique elements from the original
def remove_duplicates(lst):
    full_lst_without_repetitions = []
    result = []

    for i in range(len(lst)):
        element = lst[i]
        if element in full_lst_without_repetitions:
            if element in result:
                result.remove(element)
        else:
            full_lst_without_repetitions.append(element)
            result.append(element)

    return result


# Exercise 10.10 - Write a function that reads the file words.txt and builds a list with one element per word
def append_word_list():
    result = []
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            result.append(line.strip())
        f.close()
    return result 

# Exercise 10.10 - Write another version of this function, one using not the append method as before but the idiom t = t + [x]
def add_word_list():
    result = []
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            result += [line.strip()]
        f.close()
    return result 


# Exercise 10.11 - Write a function that takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or None if it’s not
def bisect(sorted_list, target_value):
    l = len(sorted_list)
    if l == 0:
        return None
      
    i = l // 2
    if sorted_list[i] == target_value:
        return i
    elif sorted_list[i] > target_value:
        return bisect(sorted_list[:i], target_value)
    else:
       return bisect(sorted_list[i+1:], target_value)


# Exercise 10.12 - Write a program that finds all the reverse pairs in the word list
def exists(sorted_list, target_value):
    l = len(sorted_list)
    if l == 0:
        return False
      
    i = l // 2
    if sorted_list[i] == target_value:
        return True
    elif sorted_list[i] > target_value:
        return bisect(sorted_list[:i], target_value)
    else:
       return bisect(sorted_list[i+1:], target_value)

def get_words():
    # treating the words file
    word_list = []
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            word_list += [line.strip()]
        f.close()
    return word_list

def reverse_pairs():
    word_list = get_words()
    
    # finding reverse pairs
    for word in word_list:
        if exists(word_list,word[::-1]):
            print(word,word[::-1])


# Exercise 10.13 - Write a program that finds all pairs of words that interlock
def interlock():
    word_list = get_words()
    
    for word in word_list:
        even = word[::2]
        odd = word[1::2]
        if exists(word_list,even) and exists(word_list, odd):
            print(even,odd)
            word_list.remove(even)
            word_list.remove(odd)

# Exercise 10.13 - Can you find any words that are three-way interlocked
def three_way():
    word_list = get_words()
    
    for word in word_list:
        first_word = word[::3]
        second_word = word[1::3]
        third_word = word[2::3]
        if exists(word_list,first_word) and exists(word_list, second_word) and exists(word_list, third_word):
            print(first_word,second_word, third_word)
            word_list.remove(first_word)
            word_list.remove(second_word)
            word_list.remove(third_word)


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 10.1")
    print("2. Exercise 10.2")
    print("3. Exercise 10.3")
    print("4. Exercise 10.4")
    print("5. Exercise 10.5")
    print("6. Exercise 10.6")
    print("7. Exercise 10.7")
    print("8. Exercise 10.8")
    print("9. Exercise 10.9")
    print("10. Exercise 10.10")
    print("11. Exercise 10.11")
    print("12. Exercise 10.12")
    print("13. Exercise 10.13")
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
            outter_list = []
            while True:
                inpt = input("Please insert your list, with its elements separated by commas, or 'done' to terminate\n")
                if inpt == 'done':
                    break
                else:
                    inner_list = inpt.split(",")
                    if is_numeric(inner_list):
                        resultant_list = []
                        for i in range(len(inner_list)):
                            resultant_list.append(int(inner_list[i]))
                        outter_list.append(resultant_list)
            print(nested_sum(outter_list))
        elif choice==2:
            outter_list = []
            while True:
                inpt = input("Please insert your list, with its elements separated by commas, or 'done' to terminate\n")
                if inpt == 'done':
                    break
                else:
                    outter_list.append(inpt.split(","))
            print(capitalize_nested(outter_list))
        elif choice==3:
            while True:
                inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
                if is_numeric(inpt):
                    resultant_list = []
                    for i in range(len(inpt)):
                        resultant_list.append(int(inpt[i]))
                    print(cumulative_sum(resultant_list))
                    break
        elif choice==4:
            inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
            print(middle(inpt))
        elif choice==5:
            inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
            res = chop(inpt)
            print(inpt)
            print(res)
        elif choice==6:
            inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
            print(is_sorted(inpt))
        elif choice==7:
            w1 = input('word 1: ')
            w2 = input('word 2: ')
            print(is_anagram(w1,w2))
        elif choice==8:
            inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
            print(has_duplicates(inpt))
            print(inpt)
        elif choice==9:
            inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
            print(remove_duplicates(inpt))
        elif choice==10:
            print("Append method: ")
            print(append_word_list())
            print("Add method: ")
            print(add_word_list())
        elif choice==11:
            inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
            w1 = input('word 1: ')
            inpt.sort()
            print("sorted:",inpt)
            print(bisect(inpt,w1))
        elif choice==12:
            reverse_pairs()
        elif choice==13:
            interlock()
            three_way()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()