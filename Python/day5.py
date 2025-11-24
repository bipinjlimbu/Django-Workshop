def inputNum():
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    return n1, n2

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def modulus(a, b):
    return a % b

while True:
    print("Select operation:")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Exit")
    choice = input("Enter your choice: ")

    match choice:
        case '1':
            num1, num2 = inputNum()
            print("Result:", add(num1, num2))

        case '2':
            num1, num2 = inputNum()
            print("Result:", subtract(num1, num2))

        case '3':
            num1, num2 = inputNum()
            print("Result:", multiply(num1, num2))

        case '4':
            num1, num2 = inputNum()
            print("Result:", divide(num1, num2))

        case '5':
            num1, num2 = inputNum()
            print("Result:", modulus(num1, num2))

        case '6':
            print("Exiting the calculator. Goodbye!")
            break

        case "_":
            print("Invalid input")