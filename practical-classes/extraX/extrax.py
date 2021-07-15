# Alexandra de Carvalho, 13 jul 2021


import time


# Exercise 1a) - The program must present a menu and process each chosen option
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
            if tournament == 0:
                return "EXIT",{}
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

        # Exercise 3e) - Add the possibility of multiple bets, letting the user introduce a double (1X,X2,12) or triple (1X2) bet in each game and, in the end, calculating the equivalent number of bets and its cost
        while bet.lower() not in ["1","2","x","12","21","1x","x1","2x","x2","12x","1x2","21x","2x1","x12","x21"]:
            print("Invalid Bet!")
            bet = input(prompt)
        
        bets.append(bet)
        print(str(counter)+","+bet, file=j)
        counter += 1
    
    j.close()
    return show_bulletin_results(tournament, tournament_matches, bets)

# Exercise 2b) - Alter the program so that, immediately after a player has filled its bulletin, presents a table with games from that tournament, its results, bets, and indicate which were right/wrong  
def show_bulletin_results(tournament, matches, bets):
    try:
        results_file = open('Jogos.csv','r')
    except IOError:
        print("ERROR: Couldn\'t find Jogos.csv file")
    else:
        print("Tournament ",str(tournament))
        count = 1
        rights = 0
        total = {"simple":0,"double":0,"triple":0}
        
        for line in results_file:
            game = line.split(",")
            players = tuple([game[1],game[2]])
            
            if players in matches:
                idx = matches.index(players)
                bet = bets[idx]
                if len(bet) == 1:
                    total["simple"] += 1
                elif len(bet) == 2:
                    total["double"] += 1
                elif len(bet) == 3:
                    total["triple"] += 1

                for element in bet:
                    if int(game[3]) < int(game[4]) and element == "2":
                        rights += 1
                        result = "RIGHT"
                    elif int(game[3]) > int(game[4]) and element == "1":
                        rights += 1
                        result = "RIGHT"
                    elif int(game[3]) == int(game[4]) and element.lower() == "x":
                        rights += 1
                        result = "RIGHT"
                    else:
                        result = "WRONG"
            
                    print("{:<2d} {:>15s} {:>2s}-{:<2s} {:<15s} : {:^3s} ({:<5s})".format(count, game[1],game[3],game[4].replace("\n",""),game[2],element,result))
                    count +=1
        results_file.close()
    return prize(rights, total)

# Exercise 2c) - Indicate the number of right bets and if the player got the first prize (all bets right), the second prize (8 bets right), the third prize (7 bets right), or if they don't get a prize                
def prize(rights, total):
    string = "You got {} answers right.".format(rights)
    t = total["simple"] + total["double"] + total["triple"]
    if rights == t:
        string +=" FIRST PRIZE."
    elif rights == (t-1):
        string +=" SECOND PRIZE."
    elif rights == (t-2):
        string +=" THIRD PRIZE."
    else:
        string +=" NO PRIZE."
    
    print(string)
    return string, total

# Exercise 2d) - Repeat the game until the user answers zero to the "Tournament? " question and, since each bulletin costs 0.40 euros, the first prize is 5000€, the second prize 1000€ and the third prize 100€, calculate the balance of the player at the end of each bulletin. The initial balance is 0, so if a player fills in a bulletin they're automatically at a negative balance of -0.40€
def ex2():
    while True:
        result,total = register_bet()
        if result == "EXIT":
            break
        
        balance = 1**total["simple"] * 2**total["double"] * 3**total["triple"]

        place = result.split(".")[1]
        if place == "  FIRST PRIZE":
            balance += 5000
        elif place == "  SECOND PRIZE":
            balance += 1000
        elif place == "  THIRD PRIZE":
            balance += 100
        
        print("balance: "+str(balance)+" euro") 


# Exercise 3a) - In the "insert items" option, the program should ask for the product code and calculate the final price, printing something in the screen
def codeToProduct():
    sales = []
    try:
        f = open('hipermercado.txt','r')
    except IOError: 
        print("ERROR: DataBase File Not Found!")
    else:
        while True:
            try:
                code = int(input("code: "))
            except ValueError:
                print("ERROR: Invalid code")
            else:
                if code == 0:
                    break
                else:
                    f.seek(0)
                    for line in f:
                        product = line.split(";")
                        if int(product[0]) == code:
                            sales += [code]
                            price = float(product[3])+ (float(product[3])*(int(product[4].replace("%",""))/100))
                            print("{}: {:.2f}€".format(product[1],price))
        f.close()
    return sales

# Exercise 3b) - When the user choses to leave, the program should record, in a file, all the products sold
def register(sales):
    try:
        codes = open("hipermercado.txt",'r')
    except IOError:
        print("ERROR while opening file hipermercado.txt")
    else:
        price = 0
        for line in codes:
            product = line.split(";")
            if int(product[0]) in sales:
                price += float(product[3])+ (float(product[3])*(int(product[4].replace("%",""))/100))
        codes.close()

        f = open("sales.txt","a")
        print("{}: {:.2f}".format(time.strftime('%d/%m/%Y %H:%M'),price), file=f)
        f.close()   

# Exercise 3c) - When the user choses to leave, the program should record, in another file, the sold stock - one product code and total number of sold items per line
def stockOut(sales):
    stock = {}
    for code in sales:
        stock[code] = stock.get(code,0) + 1

    f = open("StockOut.txt","a")
    for code, stockout in stock.items():
        print("{:d}; {:d}".format(code,stockout), file=f)
    f.close()  

# Exercise 3d) - When the user asks for the invoice, the program should print one with all products organized by section and sorted by name
def billing2(sales):
    store = {}
    try:
        products = open("hipermercado.txt",'r')
    except IOError:
        print("ERROR while opening file hipermercado.txt")
    else:
        stock = {}
        for line in products:
            product = line.split(";")
            stock[int(product[0])] = [product[1],product[2],product[3],product[4]]  # code : [name,category,price,tax]
            
        for code in sales:
            product = stock[int(code)]   # [name,category,price,tax]
            if product[1] not in store.keys():
                store[product[1]] = {}

            if product[0] not in store[product[1]]:
                store[product[1]][product[0]] = [0,"",""]
            
            store[product[1]][product[0]] = [store[product[1]][product[0]][0] + 1, product[-1], product[2]] # category : {name : [quantity,tax,price]}

        for category in store.keys():
            print(category+":")
            for name, infos in store[category].items():
                print("{:>3d} {:<18s} (IVA {:<s})  {:<.2f}€".format(infos[0], name, infos[1].replace("\n",""), float(infos[2])+(float(infos[2]))*float(infos[1].replace("\n","").replace("%",""))/100))

def print_menu_ex3():
    print(30 * "-" , "MENU" , 30 * "-")
    print("(I)nsert Items")
    print("(B)illing")
    print("(L)eave")

def ex3():
    loop3 = True
    sales = []
    while loop3:
        print_menu_ex3()
        option = input("Option? ")
        
        if option=="I":
            sales += codeToProduct()
        elif option=="B":     
            billing2(sales)
        elif option=="L":
            register(sales)
            stockOut(sales)     
            print("Goodbye")
            loop3=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter a valid key to try again..")


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 1")
    print("2. Exercise 2")
    print("3. Exercise 3")
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
            ex2()
        elif choice==3:
            ex3()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()