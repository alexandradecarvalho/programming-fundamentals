# Alexandra de Carvalho, 25 September 2021


import os
import shelve
import urllib.request


# Exercise 14.1 - Use the walk function to print the names of the files in a given directory and its subdirectories
def walk(dir):
    for root, dirs, files in os.walk(dir):
        for filename in files:
            print(os.path.join(root, filename))


# Exercise 14.2 - Write a function that takes as arguments a pattern string, a replacement string, and two filenames; it should read the first file and write the contents into the second file, replacing the pattern string by the replacement string
def sed(pattern, replacement, f1, f2):
    try:
        source = open(f1,'r',encoding='utf8')
    except IOError:
        print('ERROR: Could not find the {} file\n'.format(f1))
    else:
        try:
            destiny = open(f2,'w',encoding='utf8')
        except IOError:
            print('ERROR: Could not find the {} file\n'.format(f2))
        else:
            for line in source:
                line = line.replace(pattern,replacement)
                destiny.write(line)


# Exercise 14.3 - Write three functions: one that finds anagram sets, another that stores the anagram dictionary in a "shelf" and the last one that looks up a word and returns a list of its anagrams
def anagram_sets():
    words = []
    try:
        f = open('words.txt', 'r',encoding='utf8')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            words += [line.strip()]
        f.close()
    
    anagram_pairs = {}
    for word in words:
        k = ''.join(sorted(word)) 
        anagram_pairs[k] = anagram_pairs.get(k,[]) + [word]
    
    return anagram_pairs

def store_anagrams(anagrams):
    with shelve.open('ex142db') as db:
        for k in anagrams.keys():
            db[k] = anagrams[k]

def read_anagrams(word):
    db = shelve.open('ex142db')
    res = db[''.join(sorted(word))]
    db.close()
    return res


# Exercise 14.6 - Run this code and follow the instructions you see there
def secret_message():
    with urllib.request.urlopen("http://thinkpython2.com/secret.html") as url:  # this link doesnt work anymore
        for line in url:
            print(line.strip())


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 14.1")
    print("2. Exercise 14.2")
    print("3. Exercise 14.3")
    print("6. Exercise 14.6")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-3,6] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            walk('.')
        elif choice==2:
            pattern=input('pattern: ')
            replacement=input('replacement: ')
            sed(pattern,replacement,'alicewonderland.txt','ex142.txt')
        elif choice==3:
            #store_anagrams(anagram_sets()) - this takes way too long for 100 000 + words
            word = input('word: ')
            print(read_anagrams(word))
        elif choice==6:
            secret_message()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()