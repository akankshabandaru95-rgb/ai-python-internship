"""Module 01 – Python practice: variables, loops, functions, lists."""

name = "Intern"
age = 20
print(f"Hello, {name}! Age: {age}")

print("Numbers 1-5:")
for i in range(1, 6):
    print(i, end=" ")
print()

count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1


def add(a, b):
    return a + b


def is_even(n):
    return n % 2 == 0


print("2 + 3 =", add(2, 3))
print("Is 4 even?", is_even(4))

fruits = ["apple", "banana", "mango"]
fruits.append("orange")
for f in fruits:
    print(f.upper())
print("Total fruits:", len(fruits))

marks = [78, 85, 92, 66]
print("Total:", sum(marks), "Average:", sum(marks) / len(marks))
