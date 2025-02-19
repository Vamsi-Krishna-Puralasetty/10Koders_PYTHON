operation = input("enter the operation :").lower()
num1 = int(input("enter first number :"))
num2 = int(input("enter second number :"))

if operation in ['add' , '+']:
    print(num1 + num2)
elif operation in ["sub" , "-"]:
    print(num1 - num2)
elif operation in ["mul" , "*" , "x"]:
    print(num1 * num2)
elif  operation in ["div" , "/"]:
    if num2 == 0:
        print("division not possible")
    else:
        print(num1 / num2)
else:
    print("invalid")


