def fibonacci(n):
    if n <= 0:
        print(type(n))
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


print(type(fibonacci))
print(fibonacci(3))
