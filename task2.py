temp = float(input("Enter the temperature value: "))
unit = (input("Type 'C' to convert C to F, or 'F' to convert F to C: ").upper())

if unit == "C":

    result = (temp * 9/5) + 32

    print(f'{temp}°C is equal to {result:.2f}°F')

elif unit == "F":

    result = (temp - 32) * 5/9

    print(f"{temp}°F is equal to {result:.2f}°C")

else :

    print("Invalid unit! Please enter C or F.")