#################################################################################################################################################
### [DAY 1] ###
#################################################################################################################################################



#################################################################################################################################################
### [CONCEPTS] ###
#################################################################################################################################################
# [Comment]
# ctrl + /  # commenting lines out at once 


# [print()]
print("Hello World!")
print("Hello" + " World!")


# [Line Changing]
# \n
# """a"""


# [input()]
print("Hello " + input("What is your name?") + "!")


# [Variables]
variable_name = "abc"
print(variable_name)   # printing abc only
variable_name = "aabbcc"
print(variable_name)   # printing abc & aabbcc in order


#################################################################################################################################################
### [EXERCISES] ###
#################################################################################################################################################
# [ex 1 - https://replit.com/@appbrewery/day-1-1-exercise]
# using """
print("""Day 1 - Python Print Function
The function is declared like this:
print('what to print')""")
# using \n
print("Day 1 - Python Print Function\nThe function is declared like this:\nprint('what to print')")


# [ex 2 - https://replit.com/@appbrewery/day-1-2-exercise]
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello" + " World")')
print("New lines can be created with a backslash and n.")


# [ex 3 - https://replit.com/@appbrewery/day-1-3-exercise]
name = input("What is your name? ")
print(len(name.lower()))


# [ex 4 - https://replit.com/@appbrewery/day-1-4-exercise]
a = input("a: ")
b = input("b: ")
c = a
a = b
b = c
print("a = " + a)
print("b = " + b)


# [Final - https://replit.com/@appbrewery/band-name-generator-start]
print("Welcome to the BAND NAME GENERATOR!")
city = input("What's the name of the city you grew up in?\n")
pet = input("What is the name of your pet?\n")
print("Your band name is " + city + " " + pet + "!")
