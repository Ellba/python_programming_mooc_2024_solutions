# Write your solution here
temp = float(input("Please type in a temperature (F): "))
#  °C = (°F - 32) × 5/9
celc = (temp - 32) * 5/9

print(f"{temp} degrees Fahrenheit equals {celc} degrees Celsius")
if celc < 0:
    print("Brr! It's cold in here!")