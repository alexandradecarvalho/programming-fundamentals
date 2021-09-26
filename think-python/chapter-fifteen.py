# Alexandra de Carvalho, 27 September 2021


import math


# Exercise 15.1 - Write a function that takes two Points as arguments and returns the distance between them
class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __str__(self):
        return '('+ str(self.x) + ',' + str(self.y) +')'

def distance_between_points(p1,p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)


# Exercise 15.2 - Write a function that takes a Rectangle and two numbers named dx and dy and changes the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner
class Rectangle(object):
    """Represents a rectangle.
    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner
    
    def __str__(self):
        return '('+ str(self.corner.x) + ',' + str(self.corner.y) +') with width ' + str(self.width) + ' and height ' + str(self.height) 

def move_rectangle(rec,dx,dy):
    rec.corner.x += dx
    rec.corner.y += dy
    

# Exercise 15.3 - Write a version of move_rectangle that creates and returns a new Rectangle instead of modifying the old one
def new_rectangle(rec,dx,dy):
    return Rectangle(rec.width, rec.height,Point(rec.corner.x + dx, rec.corner.y + dy))


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("1. Exercise 14.1")
    print("2. Exercise 14.2")
    print("3. Exercise 14.3")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        try:
            choice = int(input('Enter your choice [1-3] or 0 to quit: '))
        except:
            choice = 222    # Invalid option
        
        if choice==1:
            while True:
                try:
                    x1 = int(input('x1: '))
                    y1 = int(input('y1: '))

                    x2 = int(input('x2: '))
                    y2 = int(input('y2: '))
                except ValueError:
                    print("We're sorry! One or more of the values you introduced seem to be invalid!")
                else:
                    p1 = Point(x1,y1)
                    p2 = Point(x2,y2)
                    print('d = ', str(distance_between_points(p1,p2)))
                    break
        elif choice==2:
            rec = Rectangle(50,10,Point(5,5))
            while True:
                try:
                    x = int(input('x: '))
                    y = int(input('y: '))
                except ValueError:
                    print("We're sorry! At least one of the values you introduced seem to be invalid!")
                else:
                    move_rectangle(rec,x,y)
                    print(rec)
                    break
        elif choice==3:
            rec = Rectangle(50,10,Point(5,5))
            while True:
                try:
                    x = int(input('x: '))
                    y = int(input('y: '))
                except ValueError:
                    print("We're sorry! At least one of the values you introduced seem to be invalid!")
                else:
                    new = new_rectangle(rec,x,y)
                    print(rec)
                    print(new)
                    break
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()