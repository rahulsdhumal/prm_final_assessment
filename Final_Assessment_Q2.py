#Q2.Print the nth fibonacci number
def Fibonacci(n):
    if n<= 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
 
n=int(input("Enter input : "))
print(Fibonacci(n))