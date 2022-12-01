def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def product(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

while True:
    print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.End calculator")
    choice = int(input("Enter your choice:"))
    if choice==5:
        break
    num1 = int(input("Enter num1:"))
    num2 = int(input("Enter num2:"))
    if choice==1:
        print(add(num1,num2))
    elif choice==2:
        print(sub(num1,num2))
    elif choice==3:
        print(product(num1,num2))
    elif choice==4:
        print(div(num1,num2))
    else:
        print("Wrong input")
