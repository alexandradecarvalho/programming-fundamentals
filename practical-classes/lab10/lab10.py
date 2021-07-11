# Alexandra de Carvalho, 10 jul 2021


import sys
import bisect


# Exercise 2 - Make a new version of the program that lists the result decreasingly by occurrence, using the sorted method with the key= and reverse= arguments to sort the key-value (items) pairs sequence
def countLetters2(filename):
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
        f.close()
    return dict(sorted(frequency_results.items(),key=lambda item : item[1],reverse=True)) 

def ex2():
    file = sys.argv[1]
    results = countLetters2(file)

    for letter in results.keys():
        print(letter,results[letter]) 


# Exercise 3 - Write a program that shows, to each last name, the set of other names found on the list, without repetitions
def printTabela(tabela,numJogos,pontos):
    print()
    print("{:19s} {:>3} {:>3} {:>3} {:>3} {:>3}:{:<3} {:>3}".format(
            "Equipa", "J", "V", "E", "D", "GM", "GS", "P"))
    for reg in tabela:
        nome,v,e,d,gm,gs = reg
        print("{:19s} {:3d} {:3d} {:3d} {:3d} {:3d}:{:<3d} {:3d}".format(
                nome, numJogos(reg), v, e, d, gm, gs, pontos(reg)))

def ex3():
    tabela = [
        ("Rio Ave", 5, 3, 2, 17, 13),
        ("Tondela", 2, 3, 5, 12, 14),
        ("Moreirense", 5, 1, 4, 11, 14),
        ("Feirense", 2, 3, 5, 7, 11),
        ("Maritimo", 3, 1, 6, 6, 13),
        ("Benfica", 6, 2, 2, 19, 11),
        ("Setubal", 4, 2, 4, 13, 11),
        ("Portimonense", 3, 2, 5, 12, 18),
        ("Guimaraes", 4, 3, 3, 15, 12),
        ("Boavista", 2, 3, 5, 8, 14),
        ("Nacional", 2, 3, 5, 10, 19),
        ("Belenenses", 2, 6, 2, 7, 8),
        ("Santa Clara", 4, 2, 4, 17, 16),
        ("FC Porto", 8, 0, 2, 21, 6),
        ("Braga", 6, 3, 1, 19, 10),
        ("Sporting", 7, 1, 2, 18, 10),
        ("Aves", 3, 1, 6, 11, 15),
        ("Chaves", 2, 1, 7, 9, 17) ]

    N,V,E,D,GM,GS = 0,1,2,3,4,5 #   Name, Victories, Ti(E)s, Defeats, Scored Goals(GM) and Suffered Goals(GS)
    numJogos = lambda reg: reg[V]+reg[E]+reg[D]     # given a team record, returns the number of games played by the team
    print(tabela[3][N], numJogos(tabela[3]))  # Test: Feirense 10?

    # Exercise 3a) - Complete the lambda expression to define the pontos function that, given a team record, returns the number of points of that team
    pontos = lambda reg: (reg[V]*3) + reg[E]

    print(tabela[-1][N], pontos(tabela[-1]))  # Chaves 7?
    printTabela(tabela, numJogos,pontos) # Shows the unordered classifications table

    # Exercise 3b) - Add the adequate arguments to the sorted function to get an ordered table by decreasing points
    print("\n3b)")
    tab = sorted(tabela,key=pontos,reverse=True)
    printTabela(tab,numJogos,pontos)

    # Exercise 3c) - Add the adequate arguments to the sorted function to get an ordered table by decreasing difference between scored and suffered goals
    print("\n3c)")
    tab = sorted(tabela,key=lambda reg: reg[GM]-reg[GS],reverse=True)
    printTabela(tab,numJogos,pontos)

    # Exercise 3d) - Add the adequate arguments to the sorted function to get an ordered table by decreasing points, and, if there are teams with equal points, by the difference of goals
    print("\n3d)")
    tab = sorted(tabela,key=lambda record: (pontos(record),record[GM]-record[GS]),reverse=True)
    printTabela(tab,numJogos,pontos)


# Exercise 4 - Write a function that calculates the median of a list of values
def median(lst):
    mid = len(lst)//2
    if len(lst)%2==0:
        return (lst[mid] + lst[mid-1])/2
    else:
        return float(lst[mid])

def ex4():
    lst = []
    insert = input("Insert elements to the list: ")
    while insert != "":
        try:
            new_value = int(insert)
        except ValueError:
            print("ERROR: Invalid number")
        else:
            lst += [new_value]
        
        insert = input("Insert elements to the list: ")

    if len(lst) > 0:
        print(median(lst))
    else:
        print(0.0)


# Exercise 5 - Read words into a list and, using a binary search function (from the bisect module), find out how many words start with "ea" without going through all of them
def biSearch(lst,val):
    return bisect.bisect_left(lst,val)

def ex5():
    try:
        f = open('/usr/share/dict/words','r')
    except IOError:
        print("ERROR: File not found")
    else:
        lst = [word.replace("\n","") for word in f]
        print(biSearch(lst,"eb")-biSearch(lst,"ea"))
        print(biSearch(lst,"tc")-biSearch(lst,"tb"))    # Should be 0
        print(lst[bisect.bisect_right(lst,"tb") ])      # first word higher than 'b' to appear after a 't' in English words: 'e' -> 'tea'


# Exercise 6 - Write a function that shows all letters that can come after a given prefix
def autoComplete(prefix):
    return "cenas: " + prefix

def ex6():
    prefix = ""
    while True:
        if p:=input(">> " + prefix):
            prefix += p
            print(autoComplete(prefix))
        else:
            break



##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("2. Exercise 2")
    print("3. Exercise 3")
    print("4. Exercise 4")
    print("5. Exercise 5")
    print("6. Exercise 6")
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
            print(ex3())
        elif choice==4:
            print("Exercise 4: \n")
            ex4()
        elif choice==5:    
            print("Exercise 5: \n") 
            ex5()
        elif choice==6:    
            print("Exercise 6: \n") 
            ex6()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()