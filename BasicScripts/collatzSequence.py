# Collatz Sequence
def collatz(number):
    # Find an even number
    if number % 2 == 0:
        number = number // 2
        print(str(number))
        return number
    elif number % 2 == 1:
        number = 3 * number + 1
        print(str(number))
        return number

try:
    print('Enter number:')
    number = int(input())
    while number != 1:
        number = collatz(number)
except ValueError:
    print('Must enter integer value!')
