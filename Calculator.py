def Calulate():
    operation = input("Enter an operation (+,-,*, /, // or %): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    #Add operation:
    if(operation == "+"):
        result = num1+num2
        print(f"Result is {round(result,3)}")
    # Subtraction operation:
    elif (operation == "-"):
        result = num1 - num2
        print(f"Result is {round(result,3)}")
    # Multiplication operation:
    elif (operation == "*"):
        result = num1 * num2
        print(f"Result is {round(result,3)}")
    # Division operation:
    elif (operation == "/"):
        result = num1 / num2
        print(f"Result is {round(result,3)}")
    # Integer Division
    elif (operation == "//"):
        result = num1 // num2
        print(f"Result is {round(result,3)}")
    # Remainder (Modulus)
    elif (operation == "%"):
        result = num1 % num2
        print(f"Result is {round(result,3)}")
    # Invalid operation:
    else:
        print(f"{operation} is not a valid operation")

Calulate()