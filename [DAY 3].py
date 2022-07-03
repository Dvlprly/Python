#################################################################################################################################################
### [DAY 3] ###
#################################################################################################################################################
# Conditional Statement (if, else, elif)
# Comparison Operators (>, <, >=, <=, ==, !=)
# Logical Operators (and, or, not)
# Code Blocks
# Scope
# Global and Local Name Spacing


#################################################################################################################################################
### [CONCEPTS] ###
#################################################################################################################################################
# [if, elif, else]
if condition:
  if another condition 1:
    do A
  elif condition 2:
    do B  
  else: 
    do C
else:
  do D


# [Comparison Operators]
a > b  # greater than
a < b  # less than
a >= b  # greater than or equal to
a <= b  # less than or equal to
a == b  # equal to
a != b  # not equal to


#################################################################################################################################################
### [EXERCISES] ###
#################################################################################################################################################
# [ex 1 - https://replit.com/@appbrewery/day-3-1-exercise]
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
  print(f"{number} is an even number.")
else:
  print(f"{number} is an odd number.")
