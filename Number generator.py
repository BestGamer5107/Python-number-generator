import random

print("Whats the smallest number?")
num1 = int(input())
print("Whats the biggest number?")
num2 = int(input())

if num1 <= num2:
    result = random.randrange(num1, num2)
    print(f"Number: {result}")
elif num1 > num2:
    print("Error: The first number is bigger than the second number")