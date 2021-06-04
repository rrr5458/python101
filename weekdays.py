day_inp = int(input("Choose a number 0 to 6: "))

if day_inp == 0:
    print("Sunday")
elif day_inp == 1:
    print("Monday")
elif day_inp == 2:
    print("Tuesday")
elif day_inp == 3:
    print("Wednesday")
elif day_inp == 4:
    print("Thursday")
elif day_inp == 5:
    print("Friday")
else:
    print("Saturday")

if day_inp == 6 or day_inp == 0:
    print("Sleep in.")
else: 
    print("Wake up.")