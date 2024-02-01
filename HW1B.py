name = input("What is your name? ")
print("Hello " + name + "! " + "You have just delved into Python.")
print()

C = int(input("Enter a temperature in degrees Celsius: "))
F = 9 / 5 * C + 32
print(str(C) + " Celsius is " + str(F) + " Farenheit.")
print()

bill, gratuity_percent = eval(input("Enter the bill and gratuity rate: "))
gratuity = round(bill * gratuity_percent / 100, 2)
total_bill = round(bill + gratuity, 2)
print("The gratuity is $" + str(gratuity)
      + " and the total is $" + str(total_bill) + ".")
print()

random_number = input("Enter a number between 0 and 999: ")
x = 9
a, b, c = x, x, x
sum = a + b + c
print("The sum of the digits is " + str(sum) + ".")
print()

p = int(input("Enter your investment amount ($): "))
n = int(input("Enter your investment length (years): "))
r = 0.07
a = round(p * (1 + r) ** n, 2)
print("After " + str(n) + " years, you will have $" + str(a))
print()

age = int(input("Enter your age: "))
max_heart_rate = 220 - age
target_heart_rate1 = round(max_heart_rate * 0.50)
target_heart_rate2 = round(max_heart_rate * 0.85)
print("Your target heart rate is " + str(target_heart_rate1)
      + " - " + str(target_heart_rate2) + " bpm.")
