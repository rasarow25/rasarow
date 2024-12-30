def reverse_string(s):
    return s[::-1]

if __name__ == "__main__":
    string_to_reverse = input("Enter a string to reverse: ")
    print("Reversed string of", string_to_reverse, ":", reverse_string(string_to_reverse))
