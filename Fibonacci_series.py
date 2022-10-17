# Function for nth Fibonacci number
def Fibonacci(n):
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return Fibonacci(n - 1) + Fibonacci(n - 2)
# print(Fibonacci(9))


# Write a program to print fibonacci series upto n terms in python

def Fib(n):
    n1, n2 = 0, 1
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")

# print(Fib(10))