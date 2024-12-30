def calculate_sum(numbers):2
    return sum(numbers)

if __name__ == "__main__":
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers_for_sum = list(map(int, numbers_input.split()))
    print("Sum of", numbers_for_sum, ":", calculate_sum(numbers_for_sum))
