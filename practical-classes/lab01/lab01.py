# Alexandra de Carvalho, 12 jun 2021

# Exercise 5 - Copy the Python instructions used in the previous exercise to a file, to create a script
def final_grade_calculator():
    biology12_grade = 18 
    informatics12_grade = 20
    portuguese_grade = 17
    philosophy_grade = 16
    english_grade = 20
    mathematics_grade = 15
    mathematics_exam = 12
    biology_grade = 13
    physics_grade = 14
    final_grade = portuguese_grade + philosophy_grade + english_grade + (mathematics_grade * 0.7 + mathematics_exam * 0.3) + biology_grade + physics_grade + biology12_grade + informatics12_grade
    final_grade = final_grade / 8
    print(final_grade)

# Exercise 6 - Change the previous function to ask the user for the high school grades and appliance test scores (using the input function)
def final_grade_calculator_from_user_input():
    biology12_grade = int(input("Please insert your 12th grade biology score: "))
    while biology12_grade < 0 or biology12_grade > 20:
        biology12_grade = int(input("Incorrect value. Please insert your 12th grade biology score: "))

    informatics12_grade = int(input("Please insert your 12th grade informatics score: "))
    while informatics12_grade < 0 or informatics12_grade > 20:
        informatics12_grade = int(input("Incorrect value. Please insert your 12th grade informatics score: "))
    
    portuguese_grade = int(input("Please insert your portuguese score: "))
    while portuguese_grade < 0 or portuguese_grade > 20:
        portuguese_grade = int(input("Incorrect value. Please insert your portuguese score: "))
    
    philosophy_grade = int(input("Please insert your philosophy score: "))
    while philosophy_grade < 0 or philosophy_grade > 20:
       philosophy_grade = int(input("Incorrect value. Please insert your philosophy score: "))
    
    english_grade = int(input("Please insert your english score: "))
    while philosophy_grade < 0 or philosophy_grade > 20:
        english_grade = int(input("Incorrect value. Please insert your english score: "))
    
    mathematics_grade = int(input("Please insert your mathematics high school score: "))
    while mathematics_grade < 0 or mathematics_grade > 20:    
        mathematics_grade = int(input("Incorrect value. Please insert your mathematics high school score: "))
    
    mathematics_exam = int(input("Please insert your mathematics exam score: "))
    while mathematics_exam < 0 or mathematics_exam > 20:
        mathematics_exam = int(input("Incorrect value. Please insert your mathematics exam score: "))
    
    biology_grade = int(input("Please insert your biology score: "))
    while biology_grade < 0 or biology_grade > 20:
        biology_grade = int(input("Incorrect value. Please insert your biology score: "))
    
    physics_grade = int(input("Please insert your physics score: "))
    while physics_grade < 0 or physics_grade > 20:
        physics_grade = int(input("Incorrect value. Please insert your physics score: "))

    final_grade = portuguese_grade + philosophy_grade + english_grade + (mathematics_grade * 0.7 + mathematics_exam * 0.3) + biology_grade + physics_grade + biology12_grade + informatics12_grade
    final_grade = final_grade / 8
    print(final_grade)

# Exercise 7 - Change the welcome.py program so that the X is replaced by the value asked of the user
def welcoming_message():
    message = """
    Dear {},

    Welcome to Programming Fundamentals e to the degree of {}.

    We hope you learn a lot and have a lot of fun!

    Best regards!

    """

    name = input("What is your name? ")
    course = input("What is your degree? ")

    print(message.format(name, course))

# Exercise 8 - Edit the plot.py program to understand it. You can print variable values or change some parameters to see what happens
def plot():
    import numpy as np
    import matplotlib.pyplot as plt

    plt.figure(1)

    t = np.arange(0.0, 5.0, 0.1)  # try printing t
    print(t)

    plt.subplot(2, 1, 1)
    y1 = np.exp(-t)
    plt.plot(t, y1, 'b') 

    plt.subplot(2, 1, 2)
    y2 = np.cos(2*np.pi*t)
    plt.plot(t, y2, 'ro-')

    plt.show()

# Exercise 9 - Change the previous function to generate a third graphic with the result of the multiplication of functions y1 and y2. Make the graph with lines and green balls.
def plot_w_three_graphics():
    import numpy as np
    import matplotlib.pyplot as plt

    plt.figure(1)

    t = np.arange(0.0, 5.0, 0.1)  # try printing t

    plt.subplot(3, 1, 1)
    y1 = np.exp(-t)
    plt.plot(t, y1, 'b') 

    plt.subplot(3, 1, 2)
    y2 = np.cos(2*np.pi*t)
    plt.plot(t, y2, 'ro-')

    plt.subplot(3, 1, 3)
    y2 = np.cos(y1*y2)
    plt.plot(t, y2, 'go-')

    plt.show()


##################MAIN#####################

def print_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("5. Exercise 5")
    print("6. Exercise 6")
    print("7. Exercise 7")
    print("8. Exercise 8")
    print("9. Exercise 9")
    print("0. Exit")
    print(67 * "-")

def main():
    loop = True

    while loop:
        print_menu()
        choice = int(input("Enter your choice [5-9] or 0 to quit: "))
        
        if choice==5:     
            print("Exercise 5: \n")
            final_grade_calculator()
        elif choice==6:
            print("Exercise 6: \n")
            final_grade_calculator_from_user_input()
        elif choice==7:
            print("Exercise 7: \n")
            welcoming_message()
        elif choice==8:
            print("Exercise 8: \n")
            plot()
        elif choice==9:
            print("Exercise 9: \n")
            plot_w_three_graphics()
        elif choice==0:
            print("Goodbye")
            loop=False # This will make the while loop to end as not value of loop is set to False
        else:
            # Any integer inputs other than values 1-5 we print an error message
            print("Wrong option selection. Enter any key to try again..")

main()


