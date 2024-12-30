def convert_temperature(celsius):
    return (celsius * 9/5) + 32

if __name__ == "__main__":
    celsius_temp = float(input("Enter temperature in Celsius: "))
    print(celsius_temp, "Celsius to Fahrenheit:", convert_temperature(celsius_temp))
