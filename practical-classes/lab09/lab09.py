# Alexandra de Carvalho, 09 jul 2021


# Exercise 2 - Write a program that determines the frequency of the occurrence of all letters from a text file whose name should be passed as a command line argument, not distinguishing upper and lower cases, and showing the results in alphabetical order
def imc(w, h):
    return w/h**2

def ex2():
    # Lista de pessoas com nome, peso em kg, altura em metro.
    people = [("John", 64.5, 1.757),
        ("Berta", 64.0, 1.612),
        ("Maria", 45.1, 1.715),
        ("Andy", 98.3, 1.81),
        ("Lisa", 46.8, 1.622),
        ("Kelly", 83.2, 1.78)]

    print("People:", people)

    # Esta comprehension define uma lista dos nomes das pessoas em people
    names = [n for n,w,h in people]
        # = [p[0] for p in people]  # equivalente
    print("Names:", names)
    
    # Usando list comprehensions, obtenha: 
    # a) Uma lista com os valores de imc de todas as pessoas.
    imcs = [imc(person[1],person[2]) for person in people]
    print("IMCs:", imcs)

    # b) Uma lista dos tuplos de pessoas com altura superior a 1.7m.
    tallpeople = [person for person in people if person[2]>1.7]
    print("Tall people:", tallpeople)    

    # c) Uma lista de nomes das pessoas com IMC entre 18 e 25.
    midimc = [person for person in people if imc(person[1],person[2]) > 18 and imc(person[1],person[2]) < 25]
    print("Mid-IMC:", midimc)


# Exercise 3 - Write a program that shows, to each last name, the set of other names found on the list, without repetitions
def ex3():
    first_names = {}
    try:
        f = open('names.txt','r')
    except IOError:
        print("ERROR: Can\'t find file!")
    else:
        for line in f:
            if len(line.split(" ")) > 1:    # exclude header
                first_names[line.replace("\n","").split(" ")[-1]] = {name for name in line.split(" ")[:-1]}
        
        f.close()
        return first_names


# Exercise 4 - Create a primesUpTo(n) function that returns a set with all prime numbers until n, using the Sieve of Eratosthenes algorithm: start with the set {2,3,...,n}, then delete the multiples of 2, starting with 2², then the multiples of 3, starting with 3², and you can jump 4 because it has already been deleted (as with all its multiples), then continue eliminating the multiples of each number still in the set
def primesUpTo(n):
    starting_list = {number for number in range(2,n+1)}
    starting_list -= {number*power for number in range(2,n+1) for power in range(2, n+1)}
    return starting_list

def ex4():
    s = primesUpTo(1000)
    print(s)

    # Do some checks:
    assert primesUpTo(30) == {2,3,5,7,11,13,17,19,23,29}
    assert len(primesUpTo(1000)) == 168
    assert len(primesUpTo(7918)) == 999
    assert len(primesUpTo(7919)) == 1000
    print("All tests passed!")


def ex5():
    A = "reading"
    B = "eating"
    C = "traveling"
    D = "writing"
    E = "running"
    F = "music"
    G = "movies"
    H = "programming"

    interests = {
        "Marco": {A, D, E, F},
        "Anna": {E, A, G},
        "Maria": {G, D, E},
        "Paolo": {B, D, F},
        "Frank": {D, B, E, F, A},
        "Teresa": {F, H, C, D}
        }


    # Exercise 5a) - Create a dictionary with the common interests of each pair of people
    print("a) Table of common interests:")
    commoninterests = {(x,y): interests[x] & interests[y] for x in interests for y in interests if x>y}
    print(commoninterests)

    # Exercise 5b) - Find the biggest number of common interests
    print("b) Maximum number of common interests:")
    maxCI = max(len(common_interests) for common_interests in commoninterests.values())
    print(maxCI)

    # Exercise 5c) - Create a list of pairs of people which have the maximum number of common interests
    print("c) Pairs with maximum number of matching interests:")
    maxmatches = [pair for pair in commoninterests if len(commoninterests[pair])==maxCI]
    print(maxmatches)

    # Exercise 5d) - Create a list of pairs of people with less than 25% of interest similarity, measured by the Jaccard index between two sets: the division between the intersection size and the union size
    print("d) Pairs with low simmilarity:")
    lowJaccard = [(x,y) for x in interests for y in interests if len(interests[x] & interests[y])/len(interests[x] | interests[y]) < 0.25]
    print(lowJaccard)


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("2. Exercise 2")
    print("3. Exercise 3")
    print("4. Exercise 4")
    print("5. Exercise 5")
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
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()