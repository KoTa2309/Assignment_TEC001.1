# Task 1

print("Task 1")
print("")

numbers = []

while True:
    user_input = input("Enter a number (Enter nothing to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))

numbers.sort(reverse=True)

print("Five greatest numbers:")
for i in range(min(5, len(numbers))):
    print(numbers[i])
print("")

# Task 2

print("Task 2")
print("")

seasons = ("winter", "spring", "summer", "autumn")

while True:
    month = int(input("Enter month number (1-12): "))
    if month == 12 or month == 1 or month == 2:
        print(seasons[0])
        break
    elif month >= 3 and month <= 5:
        print(seasons[1])
        break
    elif month >= 6 and month <= 8:
        print(seasons[2])
        break
    elif month >= 9 and month <= 11:
        print(seasons[3])
        break
    else:
        print("Invalid month number. Please enter a valid month number (1-12).")
print("")

# Task 3

print("Task 3")
print("")

names = set()

while True:
    name = input("Enter a name (Enter nothing to quit): ")

    if name == "":
        break

    if name in names:
        print("Existing name")
    else:
        print("New name")
        names.add(name)

print("\nNames entered:")
for n in names:
    print(n)
print("")

# Task 4

print("Task 4")
# Solve by using Dictionary
print("")

def word_frequency(text):
    words = text.split()
    freq = {}

    for word in words:
        word = word.lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq


text = input("Enter a text: ")

result = word_frequency(text)

for word, count in result.items():
    print(word, ":", count)
print("")

#Solve without using Dictionary"                    Give the same output as above
#print("")

#text = input("Enter text: ")

#words = text.split()

#unique_words = []
#counts = []

#for word in words:
#    word = word.lower()

#    if word in unique_words:
#        index = unique_words.index(word)
#        counts[index] += 1
#    else:
#        unique_words.append(word)
#        counts.append(1)
#
#for i in range(len(unique_words)):
#    print(unique_words[i], ":", counts[i])

# Task 5
print("Task 5")
print("")

def remove_odds(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


original = [1, 2, 3, 24, 56, 67, 90, 85, 99, 100]

result = remove_odds(original)

print("Original list:", original)
print("Cut-out odds number list: ", result)
print("")

# Task 6
print("Task 6")
print("")

import random

points = int(input("How many random points to generate: "))

inside_circle = 0
total_points = 0

for i in range(points):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    total_points += 1

    if x**2 + y**2 < 1:
        inside_circle += 1

pi = 4 * inside_circle / total_points

print("Approximation of pi:", pi)