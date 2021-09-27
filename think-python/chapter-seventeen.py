# Alexandra de Carvalho, 27 September 2021


# Exercise 17.1 - Rewrite time_to_int as a method
class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """
    def __init__(self, hour=0, minute=0, second=0):
        self.hour=hour
        self.minute=minute
        self.second=second

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds


# Exercise 17.2 - Write an init method for the Point class that takes x and y as optional parameters and assigns them to the corresponding attributes
class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    # Exercise 17.3 - Write a str method for the Point class
    def __str__(self):
        return '('+ str(self.x) + ',' + str(self.y) +')'

    # Exercise 17.4 - Write an add method for the Point class
    def __add__(self, point2):
        # Exercise 17.5 - Write an add method for Points that works with either a Point object or a tuple
        if isinstance(point2, Point):
            self.x += point2.x
            self.y += point2.y
            return self
        elif isinstance(point2, tuple):
            self.x += point2[0]
            self.y += point2[1]
            return self


# Exercise 17.6 - Change the attributes of Time to be a single integer representing seconds since midnight and modify the methods to work with the new implementation
class Time2(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """
    def __init__(self, seconds=0):
        self.seconds=seconds

    def time_to_int(self):
        return self.seconds


# Exercise 17.7 - Write a definition for a class named Kangaroo with the following methods
class Kangaroo(object):
    #1-An __init__ method that initializes an attribute named pouch_contents to an empty list
    def __init__(self):
        self.pouch_contents = []
    
    #2-A method named put_in_pouch that takes an object of any type and adds it to pouch_contents
    def put_in_pouch(self, obj):
        self.pouch_contents += [obj] 

    #3-A __str__ method that returns a string representation of the Kangaroo object and the contents of the pouch
    def __str__(self):
        contents = ""
        for elem in self.pouch_contents:
            contents += str(elem) + ","
        return 'KANGAROO -> pouch(' + contents[:-1] + ')'


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 17.1")
    print("3. Exercise 17.3")
    print("4. Exercise 17.4")
    print("5. Exercise 17.5")
    print("6. Exercise 17.6")
    print("7. Exercise 17.7")
    print("8. Exercise 17.8")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True
    t = Time(11,59,30)
    p1 = Point(1,2)
    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1,3-8] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            print(t.time_to_int())
        elif choice==3:
            while True:
                try:
                    x = int(input('x: '))
                    y = int(input('y: '))
                except ValueError:
                    print("We're sorry! The point coordinates you introduced seem to be invalid! Please try again.")
                else:
                    p = Point(x,y)
                    print(p)
                    break
        elif choice==4:
            p2 = Point(10,20)
            print(p1 + p2)
        elif choice==5:
            p3 = (5,8)
            print(p1 + p3)
        elif choice==6:
            t2 = Time2(11*3600+59*60+30)
            print(t2.time_to_int())
        elif choice==7:
            kanga = Kangaroo()
            roo = Kangaroo()
            kanga.put_in_pouch(roo)
            print(kanga)
            print(roo)
        elif choice==8:
            day_of_week()
            while True:
                day, month, year = input('DAY-MONTH-YEAR: ').split('-')
                try:
                    day = int(day)
                    month = int(month)
                    year = int(year)
                except ValueError:
                    print("We're sorry! Day, Month and Year must be valid integers! Please, try again.")
                else:
                    age(datetime.date(year, month, day))
                    break
            birthday1 = datetime.date(year, month, day) 
            
            while True:
                day2, month2, year2 = input('DAY-MONTH-YEAR: ').split('-')
                try:
                    day2 = int(day2)
                    month2 = int(month2)
                    year2 = int(year2)
                except ValueError:
                    print("We're sorry! Day, Month and Year must be valid integers! Please, try again.")
                else:
                    birthday2 = datetime.date(year2, month2,day2)
                    print(double_day(birthday1,birthday2))
                    while True:
                        try:
                            times = int(input('times: '))
                        except ValueError:
                            print("We're sorry! times must be valid integers! Please, try again.")
                        else:
                            print(n_day(times,birthday1,birthday2))
                            break
                    break
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()