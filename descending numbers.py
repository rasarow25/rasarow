def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    user_input = input("Enter numbers separated by commas: ")
    numbers = [int(num.strip()) for num in user_input.split(',')]
    sorted_numbers = bubble_sort_descending(numbers)
    print("Sorted numbers in descending order are:", sorted_numbers)
