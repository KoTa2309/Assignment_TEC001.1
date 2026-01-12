# Task 1
from ftplib import print_line

print(f"Task 1: Write a program that asks your name and then greets you by your name!")
a = input('Enter your name: ')
print(f"Hello, {a}!")

# Task 2

import math
print(f"Task 2: Write a program that asks the user for the radius of a circle and the prints out the circumference of the circle.")
radius = float(input("Enter your radius: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {circumference:.2f}")

# Task 3

print(f"Task 3: Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of each four sides.")
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
perimeter = length * width * 2
area = (length * width) / 2
print(f"The perimeter of the rectangle is {perimeter:.2f}")
print(f"The area of the rectangle is {area:.2f}")

# Task 4

print(f"Task 4: Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.")
number1 = float(input("Enter a number: "))
number2 = float(input("Enter another number: "))
number3 = float(input("Enter another number: "))
sum = number1 + number2 + number3
product = number1 * number2 * number3
average = sum / 3
print(f"Sum of all the numbers is: {sum:.2f}")
print(f"Product of all the numbers is: {product:.2f}")
print(f"Average of all the numbers is: {average:.2f}")

# Task 5

print(f"Task 5: Write a program that asks the user to enter a mass in medieval units: talents, pounds, and lots. The program converts the input to full kilograms and grams and outputs the result to the user")
talents = float(input("Enter the talents: "))
pounds = float(input("Enter the pounds: "))
lots = float(input("Enter the lots: "))
pounds_to_lots = pounds * 32
talents_to_lots = talents * 20 * 32
total_lots = talents_to_lots + pounds_to_lots + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams - (kilograms * 1000)
print(f"The weight in modern units are: {kilograms:.2f} kilograms and {grams:.2f} grams. ")

# Task 6

print(f"Write a program that draws two random combinations of numbers for a combination lock")
a1 = random.randint(0, 9)
a2 = random.randint(0, 9)
a3 = random.randint(0, 9)
print(f"Combination lock from 3 random numbers is: {a1}{a2}{a3}")
b1 = random.randint(1, 6)
b2 = random.randint(1, 6)
b3 = random.randint(1, 6)
b4 = random.randint(1, 6)
print(f"Combination lock from 4 random numbers is: {b1}{b2}{b3}{b4}")
