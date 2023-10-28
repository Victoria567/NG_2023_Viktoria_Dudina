choice = input("1 - Celsius to Fahrenheit. 2 - if from Fahrenheit to Celsius")

if choice == "1":
    celsius = float(input("Temperature in Celsius"))
    fahrenheit = celsius * 9/5 + 32
    print(f"Temperature in degrees Fahrenheit: {fahrenheit: .2f}")

elif choice == "2":
    fahrenheit = float(input("Temperature in Fahrenheit"))
    celsius = (fahrenheit - 32) * 9/5
    print(f"Temperature in degrees Celsius: {celsius: 2f}")

else:
    print ("Error. Enter 1 or 2")
