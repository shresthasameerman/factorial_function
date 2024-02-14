'''Write a program that can compute the factorial of a given number. The number whose factorial is to be computed is input from the keyboard.'''




def factorial(s):
    if s==0:
        return 1
    else: 
        return s*factorial(s-1)
number = int(input("enter a positive integer:"))
if number<0:
    print("invalid input please enter positive number")
else:
    result=factorial(number)
    print(f"the factorial of {number} is {result}")
    