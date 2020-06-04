# Now it's your turn. Here are some ideas to practice.

# Exercise 1
# 1Run the Python REPL and verify you have Python 3.6 or higher.
import sys
ma = sys.version_info.major
mi = sys.version_info.minor
print(f"Welcome to Python {ma}.{mi}!")

# Exercise 2
# Create a variable which is a whole number, compute the square and cube of it (i.e. x^2 and x^3,
# although that is not the Python code needed).
# ** is raising operator in Python
x = 4
y = x**2
z = x**3
print(f"Given the value of x is {x}, its square value is {y} and its cubed value is {z}")

# Exercise 3
# Ask a user for their name and age. Write code to tell them how many years you are older than them
# (negative numbers for younger is fine at this point).
num = input("What is your age? ")
age = int(num)
my_age = 33
diff = my_age - age
print(f"You are {age} years old and I am {my_age} years old, I am {diff} years older than you!")

# Exercise 4
# Use the built-in library datetime and the function datetime.datetime.now() to determine the current year and
# print that to REPL using an f-string.

import datetime
date = datetime.datetime.now()
print(f"Today's date is {date}!")

# Exercise 5
# Take one of these sets of code and visualize them with pythontutor.com\

# Testing line here to validate git branch second creates a secondary branch, this line should appear in ONLY the secondary branch
