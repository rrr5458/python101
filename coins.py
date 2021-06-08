coins = 0
answer = "yes"
print(f"You have {str(coins)} coins.")
while answer == "yes":
    answer = input("Do you want another coin? yes or no: ")
    print(f"You have {str(coins)} coins.")
    coins += 1



    