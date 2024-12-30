def find_maximum(numbers):
    if not numbers:
        raise ValueError("List is empty.")
    return max(numbers)

if __name__ == "__main__":
    numbers_input = input("Enter numbers separated by spaces: ")
    numbers_for_max = list(map(int, numbers_input.split()))
    print("Maximum in", numbers_for_max, ":", find_maximum(numbers_for_max))
