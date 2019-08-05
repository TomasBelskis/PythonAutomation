# Python Basics

# String concatenaton
added_strings =  str(32) + "_342"

# Getting input
input_from_user = input()

# Basic print function
print(input_from_user)

# Mixing boolean and comparison operations
if (4 < 5) and (5 < 6):
    print("True")

# Basic if  & if else flow
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print("You are not Alice, kiddo.")
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')

# Loops in Python 3
spam = 0
while spam < 5:
    print('Spam, spam!')
    spam = spam + 1

# Access loop
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe':
        continue
    print('Hello, Joe. What is the password? (It is a fish.)')
    password = input()
    if password = 'swordfish':
        break
print('Access granted.')

# For loops using range function
print("My name is")
for i in range(5):
    print('Jimmy Five Times (' + str(i) + ')')

# Using starting range
for i in range(12, 16):
    print(i)

# Importing modules
import random
for i in range(5):
    print(random.randint(1, 10))

# Exiting a python program
import sys

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
