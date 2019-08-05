# Functions in Python
def hello():
    print('Howdy!')
    print('Hello there.')

# Calling a function
hello()

# Function with arguments
def hello2(name):
    print('Hello ' + name)

hello2('Alice')

# Return values in functions
import random

def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'

r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# Print function sep & end
print('Hello', end='')
print('World')

print('cats', 'dogs', 'mice', sep=',')

# Global variables
# Variables in global scope

eggs = 'global variable'

def spam():
    global eggs
    eggs = 'spam modifed global variable'

spam()
print(eggs)