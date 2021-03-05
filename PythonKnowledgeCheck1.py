letter = ""
number = -1

wallet = float(input("How much money do you have to spend? "))

PRICES = {"A0": 1.99, "A1": 3.21,"A2": 0.50, "A3": 0.29,"A4": 1.49, "B0": 2.99,"B1": 3.50, "B2": 0.80,"B3": 1.30, "B4": 1.30}

while letter.upper() not in ['A','B'] or number > 4 or number < 0:
  letter = input("Enter a letter between A-B: ")
  number = int(input("Enter a number between 0-4: "))

selection = letter.upper() + str(number)
print("Your selection is {:>4}".format(selection))

price_of_selection = PRICES[selection]
is_affordable = price_of_selection <= wallet

if is_affordable:
  wallet = wallet - price_of_selection
  print("You have bought your item for {}, you have approximately £{:1.0f} remaining".format(price_of_selection, wallet))
else:
  print("I'm sorry, that is unaffordable")


#Content in here:
#Primitive data types: int, float, string, character, boolean
#Declaration, initialisation, assignment
#Variables and constants
#List and dictionary
#Basic Arithmetic
#Basic relational operators
#Boolean operators
#Sequence, selection, repetition
#Input/output
#Basic String manipulation and formatting

#Not covered:
#count-controlled repetition
#2D data structures
#subprograms
#Files
#Some built-ins
#List methods
#Random
#Math, time, turtle modules





