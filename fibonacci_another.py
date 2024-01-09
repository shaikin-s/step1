def fibonacci(n):
    if n <= 1:
        return n

    # Initialize the first two numbers in the sequence
    a, b = 0, 1

    # Calculate the Fibonacci sequence up to n
    for i in range(n - 1):
        a, b = b, a + b

    return b


# Test cases
print(fibonacci(0))  # Output: 0
print(fibonacci(1))  # Output: 1
print(fibonacci(2))  # Output: 1
print(fibonacci(3))  # Output: 2
print(fibonacci(4))  # Output: 3
print(fibonacci(5))  # Output: 5
print(fibonacci(6))  # Output: 8
