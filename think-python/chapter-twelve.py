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


# Exercise 12.4 - Write a program that reads a word list from a file and prints all the sets of words that are anagrams
def anagrams(wordlist):
    anagram_pairs = {}
    for word in wordlist:
        letters = set(word)
        found = False
        for k in anagram_pairs.keys():
            if set(k) == letters: 
                found = True
                anagram_pairs[k] += [word]
        
        if not found:
            anagram_pairs[tuple(letters)] = [word]

    for anagram_values in anagram_pairs.values():
        if len(anagram_values) > 1:
            print(anagram_values)

# Exercise 12.4 - Modify the previous program so that it prints the largest set of anagrams first, followed by the second largest set, and so on
def largest_anagrams(wordlist):
    anagram_pairs = {}
    for word in wordlist:
        letters = set(word)
        found = False
        for k in anagram_pairs.keys():
            if set(k) == letters: 
                found = True
                anagram_pairs[k] += [word]
        
        if not found:
            anagram_pairs[tuple(letters)] = [word]

    t = sorted(anagram_pairs.values(),key = lambda lst : len(lst), reverse=True)
    for lst in t:
        if len(lst) > 1:
            print(lst)

# Exercise 12.4 - What set of 8 letters forms the most possible bingos?
def most_bingos():
    words = []
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            word = line.strip()
            if len(word) == 8:
                words += [word]
        f.close()
    
    anagram_pairs = {}
    for word in words:
        k = tuple(sorted(word)) 
        anagram_pairs[k] = anagram_pairs.get(k,[]) + [word]
    
    t = sorted(anagram_pairs.values(),key = lambda lst : len(lst), reverse=True)
    max_len = len(t[0]) # 7
    for lst in t:
        if len(lst) == max_len:
            print(lst)
    

# Exercise 12.5 - Write a program that finds all of the metathesis pairs in the dictionary
def word_distance(w1,w2):
    differences = 0
    for l1, l2 in zip(w1,w2):
        if l1 != l2:
            differences += 1
    return differences

def metathesis_pairs():
    words = []
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            word = line.strip()
            words += [word]
        f.close()
    
    anagram_pairs = {}
    for word in words:
        k = tuple(sorted(word)) 
        anagram_pairs[k] = anagram_pairs.get(k,[]) + [word]

    for lst in anagram_pairs.values():
        if len(lst) > 1:
            for word1 in lst:
                for word2 in lst:
                    if word1 < word2 and word_distance(word1, word2) == 2:
                        print(word1, word2)


# Exrcise 12.6 - What is the longest English word, that remains a valid English word, as you remove its letters one at a time?
reducible = []
def children(wordlist, word):
    global reducible

    if word in reducible:
        return True

    if len(word) == 0:
        return True

    childrens_list = []
    for dropping_index in range(len(word)):
        child = word[:dropping_index] + word[dropping_index+1:]
        if child not in wordlist:
            return False
        else:
            reducible += [child]
            childrens_list += [child]
    
    for element in childrens_list:
        if not children(wordlist,element):
            return False
    
    return True

def always_valid_word():
    words = []
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            word = line.strip()
            words += [word]
        f.close()
    
    for word in words:
        if children(words,word):
            print(word)


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
        elif choice==4:
            wordlist = input('print your sentence:\n').split(' ')
            anagrams(wordlist)
            print('----------')
            largest_anagrams(wordlist)
            print('----------')
            most_bingos()
        elif choice==5:
            metathesis_pairs()
        elif choice==6:
            always_valid_word()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()