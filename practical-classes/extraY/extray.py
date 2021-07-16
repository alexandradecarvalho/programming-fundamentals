# Alexandra de Carvalho, 16 jul 2021


import random


# Exercise 1a) - Alter the printStocks function to show the table with aligned and formatted columns, with an extra column with the valuation of the stock, in percentage
def printStocks(stocks):
    for stock in stocks:
        print("{:<7s} {:<15s} {:>7.2f} {:>8.2f} {:>10d} {:>7.1f}%".format(stock[0],stock[1],stock[2],stock[3],stock[4], (stock[3]-stock[2])*100/stock[2]))

# Exercise 1d) - Create a load function to read the stocks.txt file and return a list of tuples similar to the stocks variable
def load(fname):
    stocks = []
    try:
        f = open(fname, 'r')
    except:
        print("ERROR while opening " + fname + " file")
    else:
        for line in f:
            stock = line.replace("\n","").split("\t")
            stocks += [tuple([stock[0], stock[1], float(stock[2]), float(stock[3]), int(stock[4])])]
        
        f.close()
    return stocks

def ex1():
    stocks = [
    ('INTC', 'London', 34.249, 34.451, 1792860),
    ('TSLA', 'London', 221.33, 229.63, 398520),
    ('EA', 'Paris', 72.63, 68.98, 1189510),
    ('INTC', 'Tokyo', 33.22001, 34.28999, 4509110),
    ('TSLA', 'Paris', 217.35, 217.75, 252500),
    ('ATML', 'Frankfurt', 8.23, 8.36, 810440),
    ]

    print("\na)")
    printStocks(stocks)

# Exercise 1b) - Add the right arguments to the sorted function in order to get an ordered table by the company name and, for the same company, by decreasing transacted volume
    print("\nb)")
    stocks2 = sorted(stocks, key=lambda stock : (stock[0],-stock[4]))
    printStocks(stocks2)

# Exercise 1c) - Alter the program to add to stocks3 a list only with the stocks from the Paris market
    print("\nc)")
    stocks3 = [stock for stock in stocks if stock[1] == "Paris"]
    
    printStocks(stocks3)

    print("\nd)")
    stocks4 = load("stocks.txt")
    printStocks(stocks4)
    
    # The following conditions must be true
    assert type(stocks4)==list
    assert type(stocks4[0])==tuple
    assert len(stocks4[0])==5
    assert type(stocks4[0][2])==float
    assert type(stocks4[0][4])==int
    print("FIM")


# Exercise 2 - Implement the combinations function provided and test it, calling it with some n and k values, such as A(2,1) = 2; A(5,2) = 20; A(5,3) = 60; A(10,3) = 720
def arranjos(n,k):
    if k == 0:
        return 1
    elif k > 0 and k <= n:
        return n*arranjos(n-1,k-1)
    else:
        return None

def ex2():
    assert arranjos(2,1) == 2
    assert arranjos(5,2) == 20
    assert arranjos(5,3) == 60
    assert arranjos(10,3) == 720
    print("ALL TESTS PASSED")


# Creates a random train
def randomTrain(a, b=0):
    Qmax = 60
    types = ["coal", "iron", "sand", "salt", "sugar", "rice"]
    n = a if a>b else random.randint(a, b)
    train = []
    for i in range(n):
        wagon = [random.choice(types), random.randint(1, Qmax)]
        train.append(wagon)
    return train

# Exercise 3a) - This function should return the total quantity of products of type m in a given t train
def quantityOf(t, m):
    """Quantidade total de mercadoria de tipo m no comboio t."""
    total = 0
    for wagon in t:
        if wagon[0] == m:
            total += wagon[1]
    return total

# Exercise 3b)
def unload(t, m, q):
    """Descarrega quantidade q de mercadoria de tipo m."""
    pass

# Exercise 3c)
def merchandise(t):
    """Devolve tabela com a quantidade de cada mercadoria no comboio t."""
    pass

# Exercise 3d)
def trainsPerMerchandise(trains):
    pass

def ex3():
    random.seed("abc") # Altering the argument results in different trains

    t = [['coal', 30], ['rice', 50], ['iron', 5], ['rice', 42], ['coal', 45]]
    #t = randomTrain(5)  # uncomment to get a random train
    print("t:", t)
    
    print("\na)")
    print(quantityOf(t, 'rice'),    # 92
          quantityOf(t, 'iron'),    # 5
          quantityOf(t, 'coal'),    # 75
          quantityOf(t, 'salt'))    # 0

    print("\nb)")
    q = unload(t, 'rice', 40)
    print("unload(t, 'rice', 40) ->", q)
    print("t:", t)
    q =unload(t, 'coal', 50)
    print("unload(t, 'coal', 50) ->", q)
    print("t:", t)
    q =unload(t, 'iron', 20)
    print("unload(t, 'iron', 20) ->", q)
    print("t:", t)

    print("\nc)")
    print(merchandise(t))
    print("t:", t)

    print("\nd)")
    trains = { tid: randomTrain(1,5) for tid in ['T1', 'T2', 'T3', 'T4'] }
    print("trains:", trains)
    trainsPerM = trainsPerMerchandise(trains)
    print(trainsPerM)

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