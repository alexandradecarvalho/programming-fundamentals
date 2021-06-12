# coding: utf-8

# Execute the program and see what happens.
# Then modify the program so that X is replaced by the course input.
# Hint: see what we did with the name.

message = """
Dear {},

Welcome to Programming Fundamentals e to the degree of X.

We hope you learn a lot and have a lot of fun!

Best regards,

"""

name = input("What is your name? ")
course = input("What is your degree? ")

print(message.format(name))

