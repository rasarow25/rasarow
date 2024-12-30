def factorial(n):
    """Calculate the factorial of a number."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    factorial_number = int(input("Enter a non-negative integer to calculate its factorial: "))
    print("Factorial of", factorial_number, ":", factorial(factorial_number))
