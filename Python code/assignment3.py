#task 1

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = int(input("Enter a number to calculate its factorial: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial of", num, "is", factorial(num))


#task 2

import math
num = float(input("Enter a positive number: "))

if num <= 0:
    print("Square root and natural log require a positive number.")
else:
    sqrt_result = math.sqrt(num)
    log_result = math.log(num)
    sine_result = math.sin(num)

    print(f"\nResults for number: {num}")
    print(f"Square root: {sqrt_result}")
    print(f"Natural logarithm (ln): {log_result}")
    print(f"Sine (in radians): {sine_result}")
