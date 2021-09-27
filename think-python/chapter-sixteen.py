# Alexandra de Carvalho, 27 September 2021


import math
import datetime


# Exercise 16.1 - Write a function that takes a Time object and prints it in the form hour:minute:second
class Time(object):
    """Represents the time of day.
    attributes: hour, minute, second
    """
    def __init__(self, hour, minute, second):
        self.hour=hour
        self.minute=minute
        self.second=second

def print_time(time):
    print(str(time.hour) + ':' + str(time.minute) + ':' + str(time.second))


# Exercise 16.2 - Write a boolean function that takes two Time objects, t1 and t2, and returns True if t1 follows t2 chronologically and False otherwise without using an if statement
def is_after(t1,t2):
    return t1.hour > t2.hour or (t1.hour == t2.hour and t1.minute > t2.minute) or (t1.hour == t2.hour and t1.minute == t2.minute and t1.second > t2.second)


# Exercise 16.3 - Write a correct version of increment that doesn’t contain any loops
def increment(time, seconds):
    time.second += seconds
    if time.second >= 60:
        r = time.second // 60
        time.second = time.second % 60
        time.minute += r
    if time.minute >= 60:
        r = time.minute // 60
        time.minute = time.minute % 60
        time.hour += r 


# Exercise 16.4 - Write a "pure" version of increment that creates and returns a new Time object rather than modifying the parameter
def pure_increment(time, seconds):
    s = time.second + seconds
    m = time.minute
    h = time.hour

    if s >= 60:
        r = s // 60
        s = s % 60
        m += r
    if m >= 60:
        r = m // 60
        m = m % 60
        h += r

    return Time(h,m,s) 


# Exercise 16.5 - Rewrite increment using time_to_int and int_to_time
def time_to_int(time):
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def int_to_time(seconds):
    m1, second = divmod(seconds, 60)
    hour, minute = divmod(m1, 60)
    return Time(hour,minute,second)

def new_increment(time, seconds):
    return int_to_time(time_to_int(time) + seconds)


# Exercise 16.6 - Write a function that takes a Time object and a number and returns a new Time object that contains the product of the original Time and the number
def mul_time(time, number):
    return int_to_time(time_to_int(time) * number)

# Exercise 16.6 - Then use that function to write a function that takes a Time object that represents the finishing time in a race, and a number that represents the distance, and returns a Time object that represents the average pace (time per mile)
def pace(finishing_time, distance):
    return mul_time(finishing_time, 1/distance)


# Exercise 16.7 - Use the datetime module to write a function that gets the current date and prints the day of the week
def day_of_week():
    today = datetime.date.today().weekday()
    if today == 0:
        print('Monday')
    elif today == 1:
        print('Tuesday')
    elif today == 2:
        print('Wednesday')
    elif today == 3:
        print('Thursday')
    elif today == 4:
        print('Friday')
    elif today == 5:
        print('Saturday')
    elif today == 6:
        print('Sunday')
    else:
        print('An error ocurred when trying to get day of the week\n')

# Exercise 16.7 - Write a function that takes a birthday as input and prints the user’s age and the number of days, hours, minutes and seconds until their next birthday
def isless(day1, day2):
    return (day1.month < day2.month) or (day1.month == day2.month and day1.day < day2.day)

def age(birthday):
    today = datetime.datetime.today()
    age = today.year - birthday.year
    
    next_birthday = datetime.datetime(today.year + 1, birthday.month, birthday.day)
    
    if isless(today, birthday):
        age -= 1
        next_birthday = datetime.datetime(today.year, birthday.month, birthday.day)
    
    print('You are ' + str(age) + ' years old.')
    print('Until your next birthday', next_birthday - today)


# Exercise 16.7 - Write a function that takes two birthdays and computes their Double Day
def age_at_date(data, birthday):
    age = data.year - birthday.year    
    if isless(data, birthday):
        age -= 1
    return age

def double_day(birthday1, birthday2):
    n = 0
    today = datetime.datetime.today()
    while True:
        single_date = today - datetime.timedelta(n)
        age1 = age_at_date(single_date, birthday1)
        age2 = age_at_date(single_date, birthday2)
        if age2 == age1 * 2 or age1 == age2 * 2:
            return single_date
        else:
            n+=1

# Exercise 16.7 - Write the more general version that computes the day when one person is n times older than the other
def n_day(times, birthday1, birthday2):
    n = 0
    today = datetime.datetime.today()
    while True:
        single_date = today - datetime.timedelta(n)
        age1 = age_at_date(single_date, birthday1)
        age2 = age_at_date(single_date, birthday2)
        if age2 == age1 * times or age1 == age2 * times:
            return single_date
        else:
            n+=1


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 16.1")
    print("2. Exercise 16.2")
    print("3. Exercise 16.3")
    print("4. Exercise 16.4")
    print("5. Exercise 16.5")
    print("6. Exercise 16.6")
    print("7. Exercise 16.7")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True
    t = Time(11,59,30)

    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-7] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            print_time(t)
        elif choice==2:
            while True:
                try:
                    h1 = int(input('hours of t1: '))
                    m1 = int(input('minutes of t1: '))
                    s1 = int(input('seconds of t1: '))

                    h2 = int(input('hours of t2: '))
                    m2 = int(input('minutes of t2: '))
                    s2 = int(input('seconds of t2: '))
                except ValueError:
                    print("We're sorry! At least one of the values you introduced seem to be invalid!")
                else:
                    t1 = Time(h1,m1,s1)
                    t2 = Time(h2,m2,s2)
                    print(is_after(t1,t2))
                    break
        elif choice==3:
            while True:
                try:
                    s = int(input('s: '))
                except ValueError:
                    print("We're sorry! The number of seconds must be a valid number! Please, try again.")
                else:
                    print_time(t)
                    increment(t,s)
                    print_time(t)
                    break
        elif choice==4:
            while True:
                try:
                    s = int(input('s: '))
                except ValueError:
                    print("We're sorry! The number of seconds must be a valid number! Please, try again.")
                else:
                    print_time(t)
                    print_time(pure_increment(t,s))
                    print_time(t)
                    break
        elif choice==5:
            while True:
                try:
                    s = int(input('s: '))
                except ValueError:
                    print("We're sorry! The number of seconds must be a valid number! Please, try again.")
                else:
                    print_time(t)
                    print_time(new_increment(t,s))
                    print_time(t)
                    break
        elif choice==6:
            finishing_time = Time(0,12,10)
            while True:
                try:
                    d = int(input('distance: '))
                except ValueError:
                    print("We're sorry! The distance must be a valid integer! Please, try again.")
                else:
                    print_time(pace(finishing_time,d))
                    break
        elif choice==7:
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