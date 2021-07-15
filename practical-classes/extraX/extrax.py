# Alexandra de Carvalho, 13 jul 2021


# Exercise 1a) - The program must present a menu and process each chosen option
from typing import IO


def print_menu_ex1():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1) Register call")
    print("2) Read file")
    print("3) List clients")
    print("4) Bill")
    print("0) Exit")

# Exercise 1b) - Write a function to validate a phone number - a string with at least 3 digits (0-9), optionally with a '+' symbol in the beginning
def isValidPhone(phone_number):
    if phone_number[0] == '+':
        phone_number = phone_number[1:]
    
    if len(phone_number) < 3:
        return False
    
    try:
        phone_number = int(phone_number)
    except ValueError:
        return False
    else:
        return True

# Exercise 1c) - Add the option to register a new call (from the keyboard) using the previous function in order to validate the origin and destiny phone numbers
def registerCall():
    origin_phone_number = ""
    while not origin_phone_number or not isValidPhone(origin_phone_number):
        origin_phone_number = input("Origin Phone Number? ")
    
    destiny_phone_number = ""
    while not destiny_phone_number or not isValidPhone(destiny_phone_number):
        destiny_phone_number = input("Destiny Phone Number? ")
    
    while True:
        duration = input("Duration (s)? ")
        try:
            duration = int(duration)
        except ValueError:
            print("ERROR: Invalid duration, please insert a number")
        else:
            break

# Exercise 1d) - Develop an option to read a file of calls that, in each call, is registered 3 "words" separated by white spaces: the origin number, the destiny number and the duration in seconds
def read_file(fname):
    calls = []
    try:
        f = open(fname,'r')
    except IOError:
        print("ERROR while opening file "+fname)
    else:
        for line in f:
            call = tuple(line.replace("\n","").split("\t"))
            calls += [call]
        f.close()
    return calls

# Exercise 1e) - The "List Clients" option should show an ordered list of the clients who made calls, without repetitions
def list_clients(reg):
    origin_numbers = set([call[0] for call in reg])
    print(sorted(list(origin_numbers)))
    
# Exercise 1f) - Develop an option to produce a detailed invoice, asking the client number and listing all the calls made, their duration and cost, as well as the total cost
def billing():
    client = input("Please insert your number: ")
    while not isValidPhone(client):
        print("ERROR: Invalid phone number")
        client = input("Please insert your number: ")
    
    reg = read_file('chamadas1.txt')
    total_price = 0
    print("Invoice for client ",client)
    print("{:<15s}   {:>8s}  {:>8s}".format("Destiny","Duration","Cost"))
    
    for call in reg:
        if call[0] == client:
            if call[1][0] == "2":
                tarif = 0.02
            elif call[1][0] == "+":
                tarif = 0.8
            elif call[1][:2] == client[:2]:
                tarif = 0.04
            else:
                tarif = 0.1
            
            duration = call[2]
            cost = tarif / 60 * int(duration)
            total_price += cost
            print("{:<15s}   {:>8s}  {:>8.2f}".format(call[1],duration,cost))
    
    print("{:<15s}   {:>8s}  {:>8.2f}".format("","Total:",total_price))
            
def ex1():
    register_loop = True
    while register_loop:
        print_menu_ex1()
        try:
            option = int(input("Option? "))
        except:
            option = 222    # Invalid option

        if option==1:
            registerCall()
        elif option==2:     
            print(read_file('chamadas1.txt'))
            print(read_file('chamadas2.txt'))
        elif option==3:     
            list_clients(read_file('chamadas1.txt'))
        elif option==4:     
            billing()
        elif option==0:     
            print("Goodbye")
            register_loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")


# Exercise 2a) - Create an interface with the player that registers the bets to each tournament game: the user introduces the tournament number and then the bet to each game, which is asked by the program, that then validates the tournament's number (it has to be in the Jornadas.txt file) and each bet (only 1,X,2 allowed) and stores a file with the name of the tournament with all bets made, one per line
def register_bet():
    looping = True
    while looping:
        tournament = input("Tournament? ")
        try:
            tournament = int(tournament)
        except ValueError:
            print("ERROR: Invalid tournament number!")
        else:
            try:
                f = open('Jornadas.csv','r')
            except IOError:
                print("ERROR: Missing file Jornadas.txt")
            else:
                tournament_matches = []
                f.seek(0)
                for line in f:
                    game = line.replace("\n","").split(",")
                    if int(game[0]) == tournament:
                        looping = False
                        tournament_matches += [tuple([game[1],game[2]])]
                
                if looping:
                    print("ERROR: Invalid tournament number!")
                else:
                    f.close()

    counter = 1
    j = open('jornadas'+str(tournament)+'.csv','w')

    bets = []
    for game in tournament_matches:
        prompt = str(counter)+" "+game[0]+" vs "+game[1]+": "
        bet = input(prompt)

        while bet.lower() not in ["1","2","x"]:
            print("Invalid Bet!")
            bet = input(prompt)
        
        bets.append(bet)
        print(str(counter)+","+bet, file=j)
        counter += 1
    
    show_bulletin_results(tournament, tournament_matches, bets)
    j.close()

# Exercise 2b) - Alter the program so that, immediately after a player has filled its bulletin, presents a table with games from that tournament, its results, bets, and indicate which were right/wrong  
def show_bulletin_results(tournament, matches, bets):
    try:
        results_file = open('Jogos.csv','r')
    except IOError:
        print("ERROR: Couldn\'t find Jogos.csv file")
    else:
        print("Tournament ",str(tournament))
        count = 1
        for line in results_file:
            game = line.split(",")
            players = tuple([game[1],game[2]])
            if players in matches:
                idx = matches.index(players)
                bet = bets[idx]
                if int(game[3]) < int(game[4]) and bet == "2":
                    result = "RIGHT"
                elif int(game[3]) > int(game[4]) and bet == "1":
                    result = "RIGHT"
                elif int(game[3]) == int(game[4]) and bet.lower() == "x":
                    result = "RIGHT"
                else:
                    result = "WRONG"
            
                print("{:<2d} {:>15s} {:>2s}-{:<2s} {:<15s} : {:1s} ({:<5s})".format(count, game[1],game[3],game[4].replace("\n",""),game[2],bet,result))
                count +=1

                


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 1")
    print("2. Exercise 2")
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
            ex1()
        elif choice==2:
            register_bet()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()