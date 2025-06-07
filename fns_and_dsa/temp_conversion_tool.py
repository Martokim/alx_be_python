# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9 
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Convert Fahrenheit to Celsius.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Convert Celsius to Fahrenheit.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def run_temperature_conversion():
    """
    Function to prompt user for input and perform temperature conversion.
    This allows safe import from main.py without executing input() on import.
    """
    try:
        temp = float(input("Enter temperature: "))
        unit = input("Is this temperature in Fahrenheit (F) or Celsius (C)? ").strip().upper()

        if unit == 'F':
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is equal to {celsius:.2f}°C")
        elif unit == 'C':
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is equal to {fahrenheit:.2f}°F")
        else:
            raise ValueError("Invalid unit. Please enter 'C' or 'F'.")
    except ValueError:
        print("Invalid temperature. Please enter a numeric value.")
