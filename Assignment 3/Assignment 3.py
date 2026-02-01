#Task 1
print('Task 1')
print(f'All numbers divisible by three in the range of 1-1000: ')
number = 1
while number <=1000:
    if number % 3 == 0:
        print(number)
    number = number + 1
print()

#Task 2
import math
print('Task 2')
while True:
    inches = float(input('Please enter a number: '))
    cm = 2.54 * inches
    if inches < 0:
        print('Program end due to negative numbers')
        break
    print(f'The cm of {inches} inches is {cm:.2f} cm')
print()

#Task 3
print('Task 3')
Numbers= []
while True:
    b = input('Please enter a number (Press Enter to quit) : ')
    if b == "":
        break
    b = float(b)

    Numbers.append(float(b))

print(f'{Numbers=}')

largest = Numbers[0]
for x in Numbers:
    if x > largest:
        largest = x
print('The largest number is', largest )

smallest = Numbers[0]
for y in Numbers:
    if y < smallest :
        smallest = y
print('The smallest number is', smallest )
print()

#Task 4
print('Task 4')
import random
z = random.randint(1,10)
while True:
    guess = int(input('Please enter a number from 1 to 10: '))
    if guess < 1 or guess > 10:
        print('Error, please enter a number from 1 to 10')
    elif guess < z:
        print('Too low')
    elif guess > z:
        print('Too high')
    else:
        print('Correct')
        break
print()

#Task 5
print('Task 5')
for i in range(5):
    username = input('Please enter a username: ')
    password = input('Please enter a password: ')
    if username == "python" and password == "rules":
        print('Welcome')
        break
    else:
        print('Wrong username or password!\nPlease try again')
else:
    print('Access denied')
print()

#Task 6
print('Task 6')
text = input('Please enter a text: ')
def middle_character(text):
    length = len(text)
    mid = length//2

    if length%2 == 0:
        return text[mid-1:mid+1]
    else:
        return text[mid]
print('The middle character(s) of your text: ',middle_character(text))
print()

#Task 7:
print('Task 7')
def acronym():
    words = input('Please enter a phrase: ')
    split = words.split()
    result = ''
    for word in split:
        result =  result + word[0].upper()
    return result
print('The acronym(s) of your phrase: ',acronym())
