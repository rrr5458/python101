number = int(input("Pick an number: "))
factors = ""
for i in range(1, number):
    if number % i == 0:
        print(str(i), str(int(number / i)))

