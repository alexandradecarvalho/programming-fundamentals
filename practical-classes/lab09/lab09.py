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


# Exercise 4 - Adapt the previous program to allow associating an address to a contact
def listContactsWithAddress(dic):
    """Print the contents of the dictionary as a table, one item per row."""
    print("{:>12s} : {:^27s} : {:<20s}".format("Numero", "Nome","Morada"))
    for num, contact in dic.items():
        print("{:>12s} : {:^27s} : {:<20s} ".format(num, contact[0], contact[1]))

def addContactWithAddress(dic):
    name = input("Name: ")
    number = input("Number: ")
    address = input("Address: ")
    dic[number] = (name,address)
    print("Contact added!")

def filterPartNameWithAddress(contacts, partName):
    """Returns a new dict with the contacts whose names contain partName."""
    possible_contacts = {}
    for number,name_address in contacts.items():
        if partName.lower() in name_address[0].lower():
            possible_contacts[number] = name_address
    return possible_contacts

def ex4():
    """This is the main function containing the main loop."""

    # The list of contacts (it's actually a dictionary!):
    contactos_w_address = {"234370200": ("Universidade de Aveiro","Santiago, Aveiro"),
        "727392822": ("Cristiano Aveiro","Funchal"),
        "387719992": ("Maria Matos","Aveiro"),
        "887555987": ("Marta Maia","Coimbra"),
        "876111333": ("Carlos Martins","Porto"),
        "433162999": ("Ana Bacalhau","Lisboa")
        }

    op = ""
    while op != "T":
        op = menu()
        if op == "T":
            print("Fim")
        elif op == "L":
            print("Contacts:")
            listContactsWithAddress(contactos_w_address)
        elif op == "A":
            addContactWithAddress(contactos_w_address)
            listContactsWithAddress(contactos_w_address)
        elif op == "R":
            removeContact(contactos_w_address)
            listContactsWithAddress(contactos_w_address)
        elif op == "N":
            print("Contact found: {}".format(findNumber(contactos_w_address)))
        elif op == "P":
            partName = input("Search: ")
            print("Matching Contacts: ")
            listContactsWithAddress(filterPartNameWithAddress(contactos_w_address,partName))
        else:
            print("Not implemented!")


# Exercise 5a) - The program should ask the user the names of the teams and store them in a list
def getTeamNames():
    teams = []
    repeat = True
    while repeat:  
        team = input("Team Name (empty to quit): ")
        if team:
            teams += [team]
        else:
            repeat = False
    return teams

# Exercise 5b) - Use the function created in lab06 for exercise 4 to generate a list of all games - pairs (team1,team2)
def footbal_matches(lst):
    matches = []
    for team1 in lst:
        for team2 in lst[-1::-1]:
            if team1 != team2:
                matches.append(tuple([team1, team2]))
    return matches

# Exercise 5c) - The program should ask the user the result of each game (goals per team) and register that information in a dictionary indexed by game
def getGamesResults(matches):
    result = {}
    for match in matches:
        scores = input("In the game {} vs {}, how many goals did they score? (please use the notation: goals0,goals1)".format(match[0], match[1])).split(",")
        while len(scores) != 2:
            print("ERROR: Please ensure you enter the results with the right format")
            scores = input("In the game {} vs {}, how many goals did they score? (please use the notation: goals0,goals1)".format(match[0], match[1])).split(",")

        try:
            score0 = int(scores[0])
            score1 = int(scores[1])
        except ValueError:
            print("ERROR: Inserted values are not valid")
        else:
            result[match] = (score0,score1)
    
    return result

# Exercise 5d) - The program should keep a table with the record of number of wins, ties and losses, total of scored and suffered goals, and the points of each team, uptadet with the result of each game
def updateTable():
    table = {}
    matches = footbal_matches(getTeamNames())
    game_results = getGamesResults(matches)

    for match,score in game_results.items():
        table[match[0]] = list( map(add, table.get(match[0], [0,0,0,0,0,0]), [1 if score[0] > score[1] else 0, 1 if score[0] == score[1] else 0, 1 if score[0] < score[1] else 0, score[0], score[1], (2 if score[0] > score[1] else 0) if not score[0] == score[1] else 1]))
        table[match[1]] = list( map(add, table.get(match[1], [0,0,0,0,0,0]), [1 if score[1] > score[0] else 0, 1 if score[0] == score[1] else 0, 1 if score[1] < score[0] else 0, score[1], score[0], (2 if score[1] > score[0] else 0) if not score[0] == score[1] else 1]))

    return table

# Exercise 5e) - Show the scores table with the following columns: team, victories, ties, losses, scored goals, suffered goals, and points
def ex5():
    ordered_podium = []

    table = updateTable()
    for team,scores in table.items():
        ordered_podium += [str(scores[5]) + team]

    if table:
        print("{:^15s} : {:^10s} : {:^10s} : {:^10s} : {:^15s} : {:^15s} : {:^10s}".format("Team", "Victories","Ties","Losses","Scored Goals","Suffered Goals","Points"))
        for team in sorted(ordered_podium,reverse=True):
            score = table[team[1:]]
            print("{:^15s} : {:^10d} : {:^10d} : {:^10d} : {:^15d} : {:^15d} : {:^10d}".format(team[1:], score[0], score[1], score[2], score[3],score[4],score[5]))
        
        # Exercise 5f) - presenting the winner team!
        winner = sorted(ordered_podium,reverse=True)[0][1:]
        winner_score = table[winner]
        best_rate = winner_score[3] - winner_score[4]

        for team in ordered_podium:
            team_score = table[team[1:]]
            if team_score[5] == winner_score[5]:
                if team_score[3] - team_score[4] > best_rate:
                    best_rate = team_score[3] - team_score[4]
                    winner = team
            else:
                break

        return winner
    return ""


# Exercise 6a) - Determine the most transacted company (with highest total volume) 
def mostTransactedCompany(filename):
    transactions = {}

    filename.seek(0)
    for line in filename:
        record = line.split(",")
        transactions[record[0]] = transactions.get(record[0],0) + int(record[-1])
    
    highest_transaction = 0
    most_transacted_company = ""
    for company,value in transactions.items():
        if value > highest_transaction:
            most_transacted_company = company

    return most_transacted_company

# Exercise 6b) - Determine the day and value of each stock to attain the highest value
def dayAndValueOfHighestStock(filename):
    transactions = {}

    filename.seek(0)
    for line in filename:
        record = line.split(",")
        company_record = transactions.get(record[0])
        if not company_record or float(record[3]) > company_record[1]:
            transactions[record[0]] = (record[1],float(record[3])) 

    return transactions

# Exercise 6c) - Determine the company with biggest daily valuation
def biggestDailyValuation(filename):
    transactions = {}
    number_of_counted_days = {}

    filename.seek(0)
    for line in filename:
        record = line.split(",")
        transactions[record[0]] = transactions.get(record[0],0) + (float(record[-2]) - float(record[2]))
        number_of_counted_days[record[0]] =number_of_counted_days.get(record[0],0) + 1
    
    for company in transactions.keys():
        transactions[company] = transactions[company] / number_of_counted_days[company]

    highest_valuation = 0
    most_valued_company = ""
    for company,valuation in transactions.items():
        if valuation > highest_valuation:
            most_valued_company = company

    return most_valued_company

# Exercise 6d) - Determine the company with the biggest valuation during the period in the file
def biggestValuation(filename):
    transactions = {}

    filename.seek(0)
    for line in filename:
        record = line.split(",")
        if not transactions.get(record[0]): # new company - lets store the opening value
            transactions[record[0]] = [record[2]]
        else:                           # let's replace closing value 
            transactions[record[0]].insert(1,record[-2])


    for company in transactions.keys():
        transactions[company] = float(transactions[company][1]) - float(transactions[company][0])

    highest_valuation = 0
    most_valued_company = ""
    for company,valuation in transactions.items():
        if valuation > highest_valuation:
            most_valued_company = company

    return most_valued_company

# Exercise 6e) - Create a function that calculates the valuation of a certain portfolio - a dictionary with the number of actions of each title - in between two given dates 
def portfolioValuation(filename, portfolio, date1, date2):
    transactions = {}
    portfolio_valuation = 0

    filename.seek(0)
    for line in filename:
        record = line.split(",")
        if record[0] in portfolio:  # if i have stocks for this company
            if not transactions.get(record[0]) and record[1] <= date2:
                transactions[record[0]] = [record[-2]]
            elif transactions.get(record[0]) and record[1] >= date1:
                if len(transactions[record[0]]) > 1:
                    del transactions[record[0]][1]
                transactions[record[0]].insert(1,record[2])
    
    for company in transactions.keys():
        portfolio_valuation += ((float(transactions[company][0]) - float(transactions[company][1])) * portfolio[company])

    return portfolio_valuation

def ex6():
    try:
        f = open("stocks.csv", 'r')
    except IOError:
        print("ERROR: Can\'t open file")
    else:
        print("Most transacted company: ",mostTransactedCompany(f))
        
        print("Day and value of each highest stock: ")
        for company,record in dayAndValueOfHighestStock(f).items():
            print(company,record,sep=": ")
        
        print("Most valued daily company: ", biggestDailyValuation(f))
        print("Most valued company in the recorded period: ", biggestValuation(f))
        
        print("Porfolio Valuation between 2015-11-20 and 2015-11-10: ", portfolioValuation(f, {'NFLX': 100, 'CSCO': 80}, '2015-11-10', '2015-11-20'))

        f.close()

# Exercise 7a) - Complete the value(b) function to return the total amount in the bag b
# Face values of coins (in cents):
COINS = [200, 100, 50, 20, 10, 5, 2, 1]

def value(bag):
    """Return total amount in a bag."""
    result = 0
    for type,number in bag.items():
        result += (type*number)
    return result

# Exercise 7b) - Complete the transfer1coin(b1,c,b2) function to try to transfer a coin of type c from bag b1 to bag b2, returning True and changing the coins of the bags if the operation succedes and returning False and letting the bags unchanged otherwise
def transfer1coin(bag1, c, bag2):
    """Try to transfer one coin of value c from bag1 to bag2.
    If possible, transfer coin and return True, otherwise return False."""
    if bag1[c] > 0:
        bag1[c] -= 1
        bag2[c] = bag2.get(c,0) + 1
        return True
    else:
        return False


# Exercise 7c) - Complete the transfer(b1, a, b2) function to try to transfer an amount a from b1 to b2 by transferring one coin at a time, if it is possible (returning True and updating the bags) - if it is not possible, the function should return False and keep the bags unchanged
def transfer(bag1, amount, bag2):
    """Try to transfer an amount from bag1 to bag2.
    If possible, transfer coins and return True,
    otherwise, return False and leave bags with same values."""
    if amount == 0:
        return True
    if value(bag1) < amount:
        return False

    while True:
        can_transfer = False
        for coin in sorted(bag1.keys(),reverse=True):
            if coin <= amount and bag1[coin]:
                can_transfer = True
                transfer1coin(bag1,coin,bag2)
                amount -= coin
                break
        if not can_transfer:
            return False
        return transfer(bag1,amount,bag2)

# Exercise 7d) - Change the strbag(bag) function to return a string with a friendlier representation, with the quantities of coins, decreasingly, of each type of coin, for example
def strbag(bag):
    """Return a string representing the contents of a bag.""" 
    # You may want to change this to produce a more user-friendly
    # representation such as "4x200+3x50+1x5+3x1=958".
    returned_string = ""
    for coin in sorted(bag.keys(),reverse=True):
        if bag[coin] != 0:
            returned_string += str(bag[coin])+"x"+str(coin)+"+"
    return returned_string[:-1]+"="+str(value(bag))

def ex7():
    # A bag of coins is represented by a dict of {coin: number} items
    bag1 = {1: 4, 2: 0, 5:1, 10: 0, 20: 5, 50: 4, 100: 2, 200: 1}
    bag2 = {}

    # Test the value function.
    assert value({}) == 0
    assert value({1:7, 5:2, 20:4, 100:1}) == 197

    print("All tests for the value function passed!")

    # Test the strbag function.
    print( strbag({1:7, 5:2, 20:4, 100:1}) )        # 1x100+4x20+2x5+7x1=197
    print( strbag({1:7, 5:2, 10:0, 20:4, 100:1}) )  # 1x100+4x20+2x5+7x1=197

    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0
    
    print(transfer1coin(bag1, 10, bag2))    # False!
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+5x20+1x5+4x1=709
    print("bag2:", strbag(bag2))    # bag2: =0

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+4x20+1x5+4x1=689
    print("bag2:", strbag(bag2))    # bag2: 1x20=20

    print(transfer1coin(bag1, 20, bag2))    # True
    print("bag1:", strbag(bag1))    # bag1: 1x200+2x100+4x50+3x20+1x5+4x1=669
    print("bag2:", strbag(bag2))    # bag2: 2x20=40

    print("Now let's test the transfer function: ")
    
    print("Transfering 157 euros from",value(bag1))
    print(transfer(bag1, 157, bag2))        # True (should be easy)
    print("bag1:", strbag(bag1))    # bag1: 1x200+1x100+3x50+3x20+2x1=512
    print("bag2:", strbag(bag2))    # bag2: 1x100+1x50+2x20+1x5+2x1=197

    print("Transfering 60 euros from",value(bag1))
    print(transfer(bag1, 60, bag2)) # not easy, but possible...
    print("bag1:", strbag(bag1))
    print("bag2:", strbag(bag2))

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
            print("!"*20 + ex5() + "!"*20)
        elif choice==6:
            print("Exercise 6: \n")
            ex6()
        elif choice==7:
            print("Exercise 7: \n")
            ex7()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()