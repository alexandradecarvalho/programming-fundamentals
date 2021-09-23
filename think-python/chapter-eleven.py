# Alexandra de Carvalho, september 2021


# Exercise 11.1 - Write a function that reads the words in words.txt and stores them as keys in a dictionary
def words_in_dict():
    result = dict()
    try:
        f = open('words.txt', 'r')
    except IOError:
        print('ERROR: Words File not found')
    else:
        for line in f:
            result[line.strip()] = 1
        f.close()
    return result

def exists(s):
    return s in words_in_dict()


# Exercise 11.2 - Using get, write a consice histogram wihtout any if statements 
def histogram(s):
    counter = dict()
    for character in s:
        counter[character] = counter.get(character,0) + 1
    return counter


# Exercise 11.3 - Modify print_hist to print the keys and their values in alphabetical order
def print_hist(h):
    for c in sorted(h.keys()):
        print(c, h[c])


# Exercise 11.4 - Modify reverse_lookup so that it builds and returns a list of all keys that map to v, or an empty list if there are none
def reverse_lookup(d, v):
    ks = []
    for k in d:
        if d[k] == v:
            ks += [k]
    return ks


# Exercise 11.5 - Use the method setdefault to write a more concise version of invert_dict
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        complete_list = inverse.setdefault(val,[key])
        if key not in complete_list:
            inverse[val].append(key)
    return inverse


# Exercise 11.7 - Memoize the Ackermann function and see if memoization makes it possible to evaluate the function with bigger arguments
known = dict()
def ack(m,n):
    if (m,n) in known:
        return known[(m,n)]

    if m == 0:
        res = n+1
    elif m > 0 and n == 0:
        res = ack(m-1,1)
    elif m > 0 and n > 0:
        res = ack(m-1, ack(m,n-1))
    known[(m,n)] = res
    return res


# Exercise 11.9 - Use a dictionary to write a faster, simpler version of has_duplicates
def has_duplicates(lst):
    v = dict()
    for element in lst:
        new_val = v.get(element,0) + 1
        if new_val > 1:
            return True
        v[element] = new_val

    return False


# Exercise 11.10 - Write a program that reads a wordlist and finds all the rotate pairs 
def rotate_word(wordlist):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    rotations = dict()
    text = wordlist.split(" ")
    for word in text:
        for rotation in range(1,26):
            new_word = ''
            for character in word:
                new = alphabet.find(character.lower()) + rotation
                if new > len(alphabet)-1:
                    new = new - len(alphabet)
                
                appending_letter = alphabet[new]
                if character.isupper():
                    appending_letter = appending_letter.upper()
                
                new_word += appending_letter
            rotations[word] = rotations.get(word,[]) + [new_word]
    
    for word,new_words in rotations.items():
        for new_word in new_words:
            if new_word in rotations.keys():
                print(word,new_word)


# Exercise 11.11 - Write a program that lists all the words that without the first or the second letter sound the same as the whole word
def pronouncing():
    pronouncing = {}
    try:
        f = open('mcudict.txt', 'r')
    except IOError:
        print('ERROR: MCU Dict File not found')
    else:
        for line in f:
            entry = line.split(" ")
            pronouncing[entry[0]] = entry[1:]
        f.close()

    revert = {}
    for word, pronounciation in pronouncing.items():
        k = tuple(pronounciation)
        revert[k] = revert.get(k,[]) + [word]

    for wordlist in revert.values():
        if len(wordlist) > 1:
            for word in wordlist:
                if len(word) == 5 and word[1:] in wordlist and word[0] + word[2:] in wordlist:
                    print(word,word[1:], word[0] + word[2:]) 


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 11.1")
    print("2. Exercise 11.2")
    print("3. Exercise 11.3")
    print("4. Exercise 11.4")
    print("5. Exercise 11.5")
    print("7. Exercise 11.7")
    print("9. Exercise 11.9")
    print("10. Exercise 11.10")
    print("11. Exercise 11.11")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True
    d = {'um':'1', 'dois':'2', 'tres':'3', 'quatro':'4', 'cinco':'5', 'seis':'6', 'sete':'7', 'oito':'8', 'nove':'9', 'dez':'10', 'onze':'10'}

    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-5,7,9-11] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            word = input('word: ')
            print(exists(word))
        elif choice==2:
            word = input('word: ')
            print(histogram(word))
        elif choice==3:
            print_hist(d)
        elif choice==4:
            v = input('value: ')
            print(reverse_lookup(d,v))
        elif choice==5:
            print(invert_dict(d))
        elif choice==7:
            print(ack(3,4)) # should be 125
            #print(ack(4,5)) - max recursion depth exceeded error
        elif choice==9:
            inpt = input("Please insert your list, with its elements separated by commas\n").split(",")
            print(has_duplicates(inpt))
        elif choice==10:
            text = input("Insert your text here:\n")
            rotate_word(text)
        elif choice==11:
            pronouncing()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()