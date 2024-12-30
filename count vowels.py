def count_vowels(s):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in s if char in vowels)

if __name__ == "__main__":
    string_to_check = input("Enter a string to count vowels: ")
    print("Number of vowels in", string_to_check, ":", count_vowels(string_to_check))
