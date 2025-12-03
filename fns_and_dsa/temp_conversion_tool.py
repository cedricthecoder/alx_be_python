# Global Conversion Factors
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 /5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 /9

#CELSIUS_TO_FAHRENHEIT_FACTOR\s*=\s*9\/5
FAHRENHEIT_FREEZING_POINT = 32

def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius using the global conversion factor."""
    # Using the global conversion factor
    celsius = (fahrenheit - FAHRENHEIT_FREEZING_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit using the global conversion factor."""
    # Using the global conversion factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FAHRENHEIT_FREEZING_POINT
    return fahrenheit

def get_temperature_input():
    """Handles user input for temperature and its unit."""
    while True:
        try:
            # Prompt the user for temperature
            temp = input("Enter the temperature to convert: ")
            temp = float(temp)  # Convert input to float

            # Prompt the user for the unit (Celsius or Fahrenheit)
            unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

            if unit not in ['C', 'F']:
                raise ValueError("Invalid unit. Please enter either 'C' for Celsius or 'F' for Fahrenheit.")

            return temp, unit
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid numeric value for temperature.")

def main():
    """Main function to perform temperature conversion."""
    temp, unit = get_temperature_input()

    if unit == 'F':
        # Convert Fahrenheit to Celsius
        converted_temp = convert_to_celsius(temp)
        print(f"{temp}°F is {converted_temp}°C")
    elif unit == 'C':
        # Convert Celsius to Fahrenheit
        converted_temp = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {converted_temp}°F")

if __name__ == "__main__":
    main()
