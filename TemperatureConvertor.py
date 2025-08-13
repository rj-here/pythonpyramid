#This program will help you convert temperature from degrees Celsius to Fahrenheit and vice versa.
#Source: https://www.calculatorsoup.com/calculators/conversions/celsius-to-fahrenheit.php
print("Welcome to the Temperature Converter!\nHere, you'll convert temperature from ºC to ºF and vice versa")
print("Let's get started!")
yesOrNo = "yes"
while (yesOrNo.lower() == "yes"):
    choice = int(input("Enter your choice (1 for Celsius to Fahrenheit or 2 for Fahrenheit to Celsius): "))
    if choice == 1:
            celsius = float(input("Enter the temperature in degrees Celsius:\n"))
            fahrenheit = round((celsius * 9/5) + 32, 2) #rounding to 2 decimal places for ease
            print(f"{celsius}ºC = {fahrenheit}ºF")
    elif choice == 2:
            fahrenheit = float(input("Enter the temperature in degrees Fahrenheit:\n"))
            celsius = round((fahrenheit - 32) * 5/9, 2) #rounding to 2 decimal places for ease
            print(f"{fahrenheit}ºF = {celsius}ºC")
    yesOrNo = input("Would you like to do another conversion? (yes/no): ")
print("Thank you for using the Temperature Converter!")
#© 2025 Rishi
#Last updated: 13th August, 2025