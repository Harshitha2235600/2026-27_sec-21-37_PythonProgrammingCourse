#Implement a python program to that defines a function to convert Celsius to Fahrenheit and returns the result.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
celsius = 25
fahrenheit = celsius_to_fahrenheit(celsius)
print("Fahrenheit:",fahrenheit)