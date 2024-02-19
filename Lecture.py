# Hello World program
print("Hello World!")
# Printing
print()                                 # Basic print function
# Printing variables
num = 1                                 # Variable declaration
fruit = "peach"
print(f"{num} and {fruit}")             # Print format

# Inputs
age = input("Please enter your age: ")  # Ask user for age
print(age)

# Type Casting
print(type(age))                        # Print type of age variable
age_in_ten_years = age + 10             # Trying to do operation to find type comment out to avoid error
print(age_in_ten_years)                 # Print age operation variable

int_age = int(age)                      # Typecast age from str to int
print(type(int_age))

# Strings
name = "alex ov"
# String Methods
print(name.capitalize())
print(name.isdigit())
print(name.replace("alex", "AlEx"))

# Operators
sum = 0
print(sum)
sum = sum + 1
print(sum)
sum += 1
print(sum)
sum += 3
print(sum)
sum *= 2
print(sum)
sum -= 2
print(sum)
sum /= 2
print(sum)
# String manipulations
print("Hello " + "Hyperloop")
print("Hello! "*10)

# Comments
'''
Multiline 
Comments
'''
"""
Multiline 
comments
"""

# If Else
num = 11

# If Statements
if(num > 10):
    print("Greater than 10")
if(num > 7):
    print("Greater than 7")
if(num > 3):
    print("Greater than 3")

# If Else Statements
if(num > 42):
    print("Greater than 42")
else:
    print("Less than 42")

# If Elif Else Statements
# If Statements
if(num > 10):
    print("Greater than 10")
elif(num > 7):
    print("Greater than 7")
elif(num > 3):
    print("Greater than 3")
else:
    print("Less than 3")

# While Loop
num = 10
while num > 0:
    print(num)
    num -=1

# Lists
animals = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon",
           "Snake", "Horse", "Goat", "Monkey", "Rooster",
           "Dog", "Pig"]
print(animals[4])
print(animals[3:9])
print(animals[:4])
print(animals[-5:-1])
print(animals[-5:])

animals[11] = "Cat"
print(animals)
# For loop
for i in range(10):
    print(i)
for animal in animals:
    new_string = "The Year of the " + animal
    print(new_string)
# Functions
def function_name(parameter):
    parameter += 10
    return parameter

def song(num, artist, song):
    print(f"{num} : {song} by {artist}")

song(1, "Sour Grapes", "LE SSERAFIM")
song(artist="LE SSERAFIM", song="Sour Grapes", num=1)
