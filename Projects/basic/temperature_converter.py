def temperature_converter(unit_input):
    if unit_input == 1:
        celsius_input = float(input('enter the temperature in celsius: '))
        convert_to_fahrenheit = (celsius_input*9/5)+32
        print(f"Celsius to Fahrenheit: {convert_to_fahrenheit:.2f}")

    elif unit_input == 2:
        fahrenheit_input = float(
            input('enter the temperature in fahrenheit: '))
        convert_to_celsius = (fahrenheit_input-32)*5/9
        print(f"Fahrenheit to Celsius: {convert_to_celsius:.2f}")

    else:
        print("Please enter a valid number from above!")



unit_input = int(input('''
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
> '''))

temperature_converter(unit_input)

'''
def temperature_converter(unit_input: int, temp: float) -> float:
    if unit_input == 1:
        return (temp * 9/5) + 32
    elif unit_input == 2:
        return (temp - 32) * 5/9
    else:
        raise ValueError("Invalid unit input! Please enter 1 or 2.")

try:
    unit_input = int(input(""""""
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
> """))
    
    if unit_input not in [1, 2]:
        raise ValueError

    temp = float(input("Enter the temperature: "))
    result = temperature_converter(unit_input, temp)

    if unit_input == 1:
        print(f"{temp:.2f}°C is {result:.2f}°F")
    else:
        print(f"{temp:.2f}°F is {result:.2f}°C")

except ValueError:
    print("Invalid input! Please enter a valid number.")
'''