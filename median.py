"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(numbers)

sum = len(numbers)
median = 0
if(sum%2) == 0:
    num1 = numbers[int((sum/2)-1)]
    num2 = numbers[int((sum/2))]
    count = (num1 + num2)/2
    print(count)
else:
    print(numbers[int(sum/2)])
