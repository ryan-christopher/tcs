# Temperature Converter
# By Ashley :D  *a bit ehh, will add improvements later lol

# for more science-y kids! 
# simple code, but good practice for adding variables and learning about int and str

from time import sleep
import os


print("""

 Temperature Convertor

 ______________________
 |   ^F     _    ^C   |
 |  100  - | | -  40  |
 |   90  - |*| -  30  |
 |   80  - |-| -  25  |
 |   70  - | | -  20  |
 |   60  - | | -  15  |
 |   50  - | | -  10  |
 |   40  - | | -   5  |
 |   30  - | | -   0  |
 |   20  - | | -  -5  |
 |   10  - | | - -10  |
 |    0  - | | - -20  |
 |  -10  - | | - -25  |
 |  -20  - | | - -30  |
 |  -30  - | | - -35  |
 |        '***`       |
 |                    |
 |____________________|


""")

sleep(2)
os.system('cls')
print("""

  Hello fellow human!
""")

while True:

  print("""
  What would you like to convert today?

  1) Celsius to Fahrenheit
  2) Fahrenheit to Celsius
  3) Celsius to Kelvin
  4) Fahrenheit to Kelvin
  5) Kelvin to Celsius
  6) Kelvin to Fahrenheit

  """)
  answer = input()
  os.system('cls')

  if answer == "1":
      print("Celsius to Fahrenheit")
      celsius_value = int(input("Input your celsius value: "))
      fahrenheit = (celsius_value * 1.8) + 32
      print("Converting...")
      sleep(2)
      print(str(celsius_value) + "C° is " + str(round(fahrenheit, 2)) + "F°")

  if answer == "2":
      print("Fahrenheit to Celsius")
      fahrenheit_value = int(input("Input your fahrenheit value: "))
      celsius = (fahrenheit_value - 32) / 1.8
      print("Converting...")
      sleep(2)
      print(str(fahrenheit_value) + "F° is " + str(round(celsius, 2)) + "C°")

  if answer == "3":
      print("Celsius to Kelvin")
      celsius_value = int(input("Input your celsius value: "))
      kelvin = celsius_value + 273.15
      print("Converting...")
      sleep(2)
      print(str(celsius_value) + "C° is " + str(round(kelvin, 2)) + "K°")

  if answer == "4":
      print("Fahrenheit to Kelvin")
      fahrenheit_value = int(input("Input your fahrenheit value: "))
      kelvin = (fahrenheit_value - 32) * .55555 + 273.15
      print("Converting...")
      sleep(2)
      print(str(fahrenheit_value) + "F° is " + str(round(kelvin, 2)) + "K°")

  if answer == "5":
      print("Kelvin to Celsius")
      kelvin_value = int(input("Input your kelvin value: "))
      celsius = kelvin_value - 273.15
      print("Converting...")
      sleep(2)
      print(str(kelvin_value) + "K° is " + str(round(celsius, 2)) + "C°")

  if answer == "6":
      print("Kelvin to Fahrenheit")
      kelvin_value = int(input("Input your kelvin value: "))
      fahrenheit = (kelvin_value - 273.15) * 1.8 + 32
      print("Converting...")
      sleep(2)
      print(str(kelvin_value) + "K° is " + str(round(fahrenheit, 2)) + "F°")
  
  sleep(3)
  os.system('cls')
  again = input("Would you like to convert other temperatures? (y/n) ")
  if again == "y":
    continue
  else:
    print("Okay, see you around!")
    break