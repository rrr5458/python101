bill = float(input("How much is your bill? "))
service = input("How good was the service? Good, fair, or bad? ")
friends = int(input("How many people are splitting the bill? "))
service_lower = service.lower()

if service_lower == "good":
    tip = bill * .20
    total = bill + tip
    print(f"Each friends owes {float(total / 5)}")
elif service_lower == "fair":
    tip = bill * .15
    total = bill + tip
    print(f"Each friends owes {float(total / 5)}")
else: 
    tip = bill * .10
    total = bill + tip
    print(f"Each friends owes {float(total / 5)}")

