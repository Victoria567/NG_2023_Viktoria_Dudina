choice = input("1 - Цельсия в Фарингейти. 2 - если из Фарингейта в Цельсий")

if choice == "1":
    celsius = float(input("Температура в Цельсиях "))
    fahrenheit = celsius * 9/5 + 32
    print(f"Температура в градусах Фарингейта: {fahrenheit: .2f}" )

elif choice == "2":
    fahrenheit = float(input("Температура в Фарингейтах"))
    celsius = (fahrenheit - 32) * 9/5
    print(f"Температура в градусах Цельсия: {celsius: 2f}")

else:
    print ("Ошибка. Введите 1 или 2")
