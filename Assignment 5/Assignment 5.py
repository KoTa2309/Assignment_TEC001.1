# Task 1
print("Task 1")
print("")

numbers = []

while True:
    a = input("Enter a number (or press Enter to quit): ")

    if a == "":
        break

    numbers.append(float(a))

numbers.sort(reverse=True)

top_five = numbers[:5]

print("Top 5 largest numbers:", top_five)
print("")

#Task 2
print("Task 2")
print("")

Prime_check = int(input("Enter a number: "))

if Prime_check <= 1:
    print(f"{Prime_check} is not a prime number")
else:
    for i in range(2, Prime_check):
        if Prime_check % i == 0:
            print(f"{Prime_check} is not a prime number")
            break
    else:
        print(f"{Prime_check} is a prime number")

#Task 3
print("")
print("Task 3")
print("")

cities = []

for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)

print("\nCities you entered:")

for city in cities:
    print(city)

print("")

#Task 4

print("Task 4")
print("")

def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [4, 7, 13, 67, 69]

result = sum_list(my_list)
print("My list is: ",my_list)
print("The sum of the list is:", result)
print("")

#Task 5

print("Task 5")
print("")

def remove_odd(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers

List_All = [2, 5, 8, 11, 14, 17, 20, 23]

List_Even = remove_odd(List_All)

print("Original list:", List_All)
print("List without odd numbers:", List_Even)


















