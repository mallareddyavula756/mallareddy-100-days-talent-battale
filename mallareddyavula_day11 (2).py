def fibonacci_series(n):
    a, b = 0, 1
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter the value of n: "))
fibonacci_series(n)
