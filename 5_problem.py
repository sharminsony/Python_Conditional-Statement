## Temperature Converter: Write a Python program that takes a temperature input in 
##Celsius and converts it to Fahrenheit if the temperature is above 0°C, or to Kelvin 
##if the temperature is below 0°C.

temperature = float(input("Enter the temperature in Celsius: "))

if temperature > 0:
    fahrenheit = (temperature * 9/5) + 32
    print(f"The temperature in Fahrenheit is: {fahrenheit:.2f}")
elif temperature < 0:
    kelvin = temperature + 273.15
    print(f"The temperature in Kelvin is: {kelvin:.2f}")
else:
    print("The temperature is 0°C.")
    