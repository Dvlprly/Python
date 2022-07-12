#################################################################################################################################################
### [DAY 2] ###
#################################################################################################################################################



#################################################################################################################################################
### [CONCEPTS] ###
#################################################################################################################################################
# [Data Types]
# String
"Hello"
print("Hello"[0])  # subscripting: pulling out a particular element
# Integer
123
123_456_789  # for large integer = 123,456,789
# Float
3.14
#Boolean
True
False


# [len()]
len("string")


# [type()]
type(abc)


# [Type Conversion]
str(abc)
int(abc)
float(abc)


# [Operations]
1 + 2
1 - 2
1 * 2
1 / 2
1 ** 2
1 // 2  # 몫 구하기
value = 0
value += 1  # manipulating a value based on its previous value
value -= 1
value *= 1
value /= 1 
"str" + "str" 


# [f-String]
value = 0
print(f"str {value}")  # mixing different data types


# [round()]
value = round(value, 2)  # round to 2 decimals
value = "{:.2f}.format(value)"  # 끝자리가 0으로 끝날 때


#################################################################################################################################################
### [EXERCISES] ###
#################################################################################################################################################
# [ex 1 - https://replit.com/@appbrewery/day-2-1-exercise]
two_digit_number = input("Type a two digit number: ")
first_number = int(two_digit_number[0])
second_number = int(two_digit_number[1])
print(first_number + second_number)
# or
two_digit_number = input("Type a two digit number: ")
first_number = two_digit_number[0]
second_number = two_digit_number[1]
result = int(first_number) + int(second_number)
print(result)


# [ex 2 - https://replit.com/@appbrewery/day-2-2-exercise]
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
h = float(height)
w = float(weight)
bmi = round(w / (h ** 2))
print(bmi)
# or
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = int(weight) / float(height) ** 2
bmi_int = int(bmi)
print(bmi_int)


# [ex 3 - https://replit.com/@appbrewery/day-2-3-exercise]
age = input("What is your current age? ")
age_left = int(90 - int(age))
days_left = 365 * age_left
weeks_left = 52 * age_left
months_left = 12 * age_left
print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")


# [Final - https://replit.com/@appbrewery/tip-calculator-start]
print("Welcome to the tip calculator!")
bill = input("What was the TOTAL bill? $")
tip = input("How much TIP would you like to give? 10, 12, 15? ")
people = input("How many PEOPLE to split the bill? ")
total_round = float(bill)
tip_float = float(1 + int(tip) / 100)
people_int = int(people)
final_amount = round(total_round * tip_float / people_int, 2)
print(f"Each person should pay: ${final_amount}")
# or
print("Welcome to the tip calculator!")
bill = float(input("What was the TOTAL bill? $"))
tip = int(input("How much TIP would you like to give? 10, 12, 15? "))
people = int(input("How many PEOPLE to split the bill? "))
each_bill = (tip / 100 * bill + bill) / people
final_amount = round(each_bill, 2)  # or final_amount = "{:.2f}.format(each_bill)"
print(f"Each person should pay: ${final_amount}")
