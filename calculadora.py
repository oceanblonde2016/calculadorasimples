
print("select an opeartion to peform: ")
print("1. ADD")
print("2. SUBTRACT")
print("3. MULTIPLY")
print("4. DIVIDE")

operation = input()
if operation == "1":
    num1 = input("enter first numbr: ")
    num2 = input("enter second number: ")
    print("the sum is " + str(int(num1) + int(num2)))

elif operation == "2":
    num1 = input("enter first numbr: ")
    num2 = input("enter second number: ")
    print("the difference is " + str(int(num1) - int(num2)))

elif operation == "3":
    num1 = input("enter first numbr: ")
    num2 = input("enter second number: ")
    print("the product is " + str(int(num1) * int(num2)))

elif operation == "4":
    num1 = input("enter first numbr: ")
    num2 = input("enter second number: ")
    print("the result is " + str(int(num1) / int(num2)))

else:
    print("invalid Entry")