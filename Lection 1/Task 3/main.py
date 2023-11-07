choice = input("1 - Celsius to Fahrenheit. 2 - if from Fahrenheit to Celsius\n")

match choice:
  case "1":
    celsius = float(input("Temperature in Celsius\n"))
    fahrenheit = celsius * 9/5 + 32
    print(f"Temperature in degrees Fahrenheit: {fahrenheit: .2f}")
  
  case "2":
    fahrenheit = float(input("Temperature in Fahrenheit\n"))
    celsius = (fahrenheit - 32) * 9/5
    print(f"Temperature in degrees Celsius: {celsius: 2f}")
  
  case _:
    print ("Error. Enter 1 or 2")
