# Alexandra de Carvalho, 25 September 2021


import string
import random


# Exercise 13.1 - Write a program that reads a file, breaks each line into words, strips whitespace and punctuation from the words, and converts them to lowercase
def simplify_words(filename):
    treated_words = []
    try:
        f = open(filename, 'r', encoding='utf8')
    except IOError:
        print('ERROR: {} file not found'.format(filename))
    else:
        for line in f:
            words = line.split(' ')
            for idx in range(len(words)):
                word = words[idx].strip()
                new_word = ""

                for letter in range(len(word)):
                    if word[letter] not in string.punctuation:
                        new_word += word[letter].lower()

                treated_words += [new_word]
                
        f.close()

    return treated_words


# Exercise 13.2 - Modify the previous function to read a downloaded book, skip over the header information at the beginning of the file, and process the rest of the words as before, and then count the total number of words in the book, and the number of times each word is used
def number_of_words_in_book():
    words = simplify_words('alicewonderland.txt')
    total_words = {}
    for word in words:
        total_words[word] = total_words.get(word,0) + 1
            
    return total_words


# Exercise 13.3 - Modify the function from the previous exercise to print the 20 most frequently-used words in the book
def most_frequent_words_in_book():
    total_words = number_of_words_in_book()

    counter = 0
    for k in sorted(total_words.items(), key = lambda t: t[1], reverse=True):
        if counter < 20:
            print(k[0])
            counter +=1
        else:
            break


# Exercise 13.4 - Modify the previous function to read a word list and then print all the words in the book that are not in the word list
def non_words():
    known_words = []
    try:
        f = open('words.txt','r',encoding='utf8')
    except IOError:
        print("ERROR: Could not find the words.txt file\n")
    else:
        for line in f:
            known_words += [line.strip()]
    
        f.close()

    filewords = number_of_words_in_book().keys()
    for word in filewords:
        if word not in known_words:
            print(word)


# Exercise 13.5 - Write a function that takes a histogram and returns a random value from the histogram, chosen with probability in proportion to frequency
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def choose_from_hist(hist):
    options = []
    for k in hist.keys():
        options += [k] * hist[k]
    return random.choice(options)


# Exercise 13.6 - Write a program that uses set subtraction to find words in the book that are not in the word list
def set_subtraction():
    non_words()


# Exercise 13.7 - Write a program that uses this algorithm to choose a random word from the book
def random_bookword(hist):
    #1-Use keys to get a list of the words in the book
    words = list(hist.keys())
    numbers = list(hist.values())

    #2-Build a list that contains the cumulative sum of the word frequencies
    cumulative_sum = []
    for i in range(len(numbers)):
        cumulative_sum.append(sum(numbers[:i+1]))

    #3-Choose a random number from 1 to n
    rand = random.randint(1,cumulative_sum[-1])

    #4-Use the index to find the corresponding word in the word list
    return words[rand]    


# Exercise 13.8 - Write a program to read a text from a file and perform Markov analysis
def markov_analysis(prefix_length):
    res = dict()
    all_words = []
    try:
        f = open('alicewonderland.txt','r',encoding='utf8')
    except IOError:
        print("ERROR: Could not find alicewonderland.txt\n")
    else:
        for line in f:
            all_words += line.strip().split(' ')
        f.close()
            
    last_idx = len(all_words) - prefix_length - 1
    for idx in range(last_idx):
        prefix = ' '.join(all_words[idx:idx+prefix_length])
        suffix = all_words[idx+prefix_length]
        if prefix not in res:
            res[prefix] = dict()
        res[prefix][suffix] = res[prefix].get(suffix,0) + 1

    return res

# Exercise 13.8 - Add a function to generate random text based on the Markov analysis
def randomText(prefix_length):
    markov = markov_analysis(prefix_length)
    text = random.choice(list(markov.keys()))   # seed

    iterations = 0
    while iterations < 40:
        last_choice = ' '.join(text.split(' ')[-prefix_length:])
        text+=' '+sorted(markov[last_choice].items(), key= lambda t: t[1], reverse=True)[0][0]
        iterations+=1
    
    return text


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 13.1")
    print("2. Exercise 13.2")
    print("3. Exercise 13.3")
    print("4. Exercise 13.4")
    print("5. Exercise 13.5")
    print("6. Exercise 13.6")
    print("7. Exercise 13.7")
    print("8. Exercise 13.8")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-8] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            filename = input('Enter filename: ')
            print(simplify_words(filename))
        elif choice==2:
            d = number_of_words_in_book()
            print(d)
            print('There are ' + str(len(d.keys())) + ' different words in the book')
        elif choice==3:
            most_frequent_words_in_book()
        elif choice==4:
            non_words()
        elif choice==5:
            t = ['a', 'a', 'b']
            hist = histogram(t)
            print(choose_from_hist(hist))
        elif choice==6:
            set_subtraction()
        elif choice==7:
            print(random_bookword(number_of_words_in_book()))
        elif choice==8:
            l = 2
            print(markov_analysis(l))
            print(randomText(l))
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()