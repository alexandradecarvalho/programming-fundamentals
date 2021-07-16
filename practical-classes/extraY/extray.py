# Alexandra de Carvalho, 16 jul 2021


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
    pass

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