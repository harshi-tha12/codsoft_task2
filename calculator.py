def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
def calculator():
 
 print('Calculator')
 print('choose the operation you want to perform')
 print('1.Addition')
 print('2.Subtraction')
 print('3.Multiplication')
 print('4.Division')
 operation=input("Enter your choice[1,2,3,4]: ")
 if operation in ['1','2','3','4']:
    first=float(input("Enter first number: "))
    second=float(input("Enter second number: "))
    
    if operation=='1':
        print("Addition of two numbers")
        print(f"{first}+{second} = {add(first,second)}")
    elif operation=='2':
        print("Difference between two numbers")
        print(f"{first}-{second} = {subtract(first,second)}")
    elif operation=='3':
        print("Multiplication of two numbers")
        print(f"{first}*{second} = {multiply(first,second)}")
    elif operation=='4':
        if second==0:
            print("Error!!Divided by zero")
        else:
            print("Division of two numbers")
            print(f"{first}/{second} = {divide(first,second)}")
 else:
  print("Invalid input!!")  
calculator()                  
              
