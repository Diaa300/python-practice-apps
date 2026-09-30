num1 = float(input("Please Inter Your Frist Number: "))
num2 = float(input("Please Inter Your Second_Number: "))
operation = input("Please Inter Your Operation (+, -, *, /): ")


if operation == "+" :
    
    print(num1 + num2)

elif operation == "-":

    print(num1 - num2)

elif operation == "*":

    print(num1 * num2)

elif operation == "/":
    if num2 == 0:
        print("Cannot divide by zero!")
    else:
        print(num1 / num2)
else:

    print("Invalid operation")