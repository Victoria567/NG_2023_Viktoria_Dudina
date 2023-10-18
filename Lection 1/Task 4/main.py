import math

operation = input ("Введите + для слодения, - для вычитания, * для умножения, / для диления, ^ для возвидения в степень, k для извлечеления корня: ")

num1 = float(input("Число: 1"))
num2 = float(input("Число: 2"))

if operation == "+":
    result = num1 + num2
    print(f"Сума чисел: {result}")

elif operation == "-":
    result = num1 - num2
    print(f"Разница чисел: {result}")

elif operation == "*":
    result = num1 * num2
    print(f"Произведение чисел: {result}")

elif operation == "/":
    if num2 != 0:
        result = num1 / num2
        print(f"Частное чисел: {result}")
    else:
        print("Ошибка. На 0 делить запрещено.")

elif operation == "^":
    result = math.pow(num1, num2)
    print(f"{num1} в степени {num2}: {result}")

elif operation == "k":
    if num1 >= 0:
        result = math.pow(num1, 1/num2)
        print("Корень {num2}-й степени {num1}: {resultat}")


else:
    print("Неверный выбор. Выберете: +, -, *, /, ^, k")
