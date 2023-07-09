# n1 = float(input("Enter first number :"))
# n2 = float(input("Enter second number :"))
# op = input("Enter operation :")
# if op=="+":
#     print(n1+n2)
# elif op=="-":
#     print(n1-n2)
# elif op=="*":
#     print(n1*n2)
# elif op=="/":
#     print(n1/n2)
# elif op=="//":
#     print(n1//n2)
# elif op=="**":
#     print(n1**n2)
# elif op=="%":
#     print(n1%n2)
    


def add(x,y):
    return(x + y)

def substract(x,y):
     return x - y

def multiply(x,y):
     return x * y

def devide(x,y):
     return x / y

def power(x,y):
     return x**y

def remainder(x,y):
     return x%y

def floor(x,y):
     return x //y

# take input from user 

num1 = int(input("Enter first number: "))
num2 = int(input("Enter first number: "))
opr=input("Enter the operator Whatever Want You")

if opr=="+":
    print(add(num1,num2))
elif opr=="-":
    print(substract(num1,num2))
elif opr=="*":
    print(multiply(num1,num2))
elif opr=="/":
    print(devide(num1,num2))
elif opr=="**":
    print(power(num1,num2))
elif opr=="%":
    print(remainder(num1,num2))
elif opr=="//":
    print(floor(num1,num2))
else:
    print("not a valid so please take serious on taking the  input")
