count = 1
while count < 11:
    print(count)
    count += 1
try: 
    start = int(input("Pick a starting number: "))
    finish = int(input("Pick an ending number: "))

    count = start
    while count < finish + 1:
        print(count)
        count += 1
except:
    print("That's not a number")
