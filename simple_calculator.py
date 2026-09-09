try:
        a = float(input("enter first number: "))
        b = float(input("enter second number: "))

        operation = input("enter operation (+,-,*,/)")

        if operation == "+":
            print("result = ",a + b)
        elif operation == "-":
            print("result = ",a - b)
        elif operation == "*":
            print("result = ",a * b)
        elif operation == "/":
            print("result = ",a / b)
        else:
            print("invalid operation")

except ValueError:
    print("Error: please enter valid number")
        
except ZeroDivisionError:
    print("Error: cannot divide by zero")
    