
import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
# print(operations["*"](4, 8))

print(art.logo)

response = "n"
while(True):
    if response == "n":
        num1 = float(input("What is your first number?: "))
    
    op = input("Pick an operation (+, -, *, /): ")
    num2 = float(input("What is your second number?: "))
    
    calculation_function = operations[op]
    answer = calculation_function(num1, num2)

    print(f"{num1} {op} {num2} = {answer}")
    
    response = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")
    num1 = answer