# Author: Shelley Tennison
# Tech Academy - Python - Item 36


# Assign an integer to a variable.

var_int = 13
print var_int

# Assign a string to a variable.

var_string = "Here is an example of a string."

# Assign a float to a variable.

var_float = 2.14
print var_float

# Use print function and .format() notation to
# print out the variable you assigned.

print"{}".format(var_string)

# Use each of these operators +, -, *, /, +=, -=, %

x = 2
y = 4

print(x + y)
print(y - x)
print(x * y)
print(y / x)
print(y % x)
while x < 4:
    print x
    x += 1
while y > 0:
    print y
    y -= 1


# use logical operators: and, or, not

x = True
y = False

print('x and y is',x and y)

print('x or y is',x or y)

print('not x is',not x)

# Use conditional statements: if, elif, else

def wakeup(alarm):
    alarm = raw_input("Do you wakeup before 9:00am? \nYes/No").capitalize
    if alarm == "Yes":
        print("Oh, you're a Morning person!")
    elif alarm == "No":
        print("Looks like you're more of a night owl.")
    else:
        print("Please answer 'Yes' or 'No'.")

    wakeup(alarm)

        
# Use of a while loop.

a = 0		
while a < 10:	
    print a
    a += 1	


# Use for a loop.

for x in range(0, 4):
    print "Rock, paper, sicissors, go on three! %d" % (x)

# Create a list and iterate through that list using a loop to
# print each item out on a new line.

counter = 0

for counter in range (0, 13):
    print counter

    
# Create a tuple and iterate through it using a loop to
# print each item out on a new line.

tuple = (1,2,3,4,5,6,7)

for tuple in range(0,8):
    print tuple
    
# Define a function that returns a sting value,
#using the example from the nice or mean tutorial.

name = ""


def niceormean_game(name):
    if name != "": 
        print("\nThank you for playing again, {}!".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = raw_input("\nWhat is your name? ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted by several different people.")
                    print("You can be nice or mean when interacting with them.")
                    print("At the end of the game your fate will be decided from your actions.")
                    stop = False
    return name        



# Call the function you defined above and print the result to the shell.

niceormean_game(name)
print(name)
