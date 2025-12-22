#using recursion
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num-1)
a = int(input("Enter a number: "))
print(f"Factorial of {a} is: {factorial(a)}")