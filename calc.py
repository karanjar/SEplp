num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
operator = input("Enter an operator: ")

if operator == "+":
    print(float(num1) + float(num2))
elif operator == "-":
    print(float(num1) - float(num2))
elif operator == "*":
    print(float(num1) * float(num2))
elif operator == "/":
    print(float(num1) / float(num2))
else:
    print("Invalid operator")