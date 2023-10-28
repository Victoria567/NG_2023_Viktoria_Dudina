import math

operation = input ("Enter + for addition, - for subtraction, * for multiplication, / for division, ^ for exponentiation, k for root extraction: ")

num1 = float(input("Number: 1"))
num2 = float(input("Number: 2"))

if operation == "+":
    result = num1 + num2
    print(f"The sum of numbers: {result}")

elif operation == "-":
    result = num1 - num2
    print(f"The difference of numbers: {result}")

elif operation == "*":
    result = num1 * num2
    print(f"The product of numbers: {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"The quotient of numbers: {result}")
    else:
        print("Error. Division by 0 is forbidden.")

elif operation == "^":
    result = math.pow(num1, num2)
    print(f"{num1} to the power {num2}: {result}")

elif operation == "k":
    if num1 >= 0:
        result = math.pow(num1, 1/num2)
        print("The root of a number {num2} to the power {num1}: {resultat}")


else:
    print("Wrong choice. Choose: +, -, *, /, ^, k")
