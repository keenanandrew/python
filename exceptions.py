import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("No, this is maths")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Careful now")
    sys.exit(1)

print(result)
