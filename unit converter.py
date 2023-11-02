def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

while True:
    try:
        print("Welcome to the Temperature Converter!")
        print("Select conversion option:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        choice = int(input("Enter your choice (1 or 2): "))
        
        if choice not in [1, 2]:
            print("Invalid choice. Please enter 1 or 2.")
            continue
        
        value = float(input("Enter the temperature value: "))
        
        if choice == 1:
            result = celsius_to_fahrenheit(value)
            print(f"{value} Celsius is equal to {result:.2f} Fahrenheit.")
        else:
            result = fahrenheit_to_celsius(value)
            print(f"{value} Fahrenheit is equal to {result:.2f} Celsius.")
        
        break
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
    except Exception as e:
        print(f"An error occurred: {e}")
