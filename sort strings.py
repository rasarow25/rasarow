def bubble_sort_by_length(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place, no need to check them
        for j in range(0, n-i-1):
            # Swap if the length of the current string is greater than the next string
            if len(arr[j]) > len(arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

if __name__ == "__main__":
    # Prompt the user to enter strings
    user_input = input("Enter strings separated by commas: ")
    
    # Convert the input string into a list of strings
    strings = [s.strip() for s in user_input.split(',')]
    
    # Sort the strings by their lengths using bubble sort
    sorted_strings = bubble_sort_by_length(strings)
    
    # Print the sorted array
    print("Sorted strings by length are:", sorted_strings)
