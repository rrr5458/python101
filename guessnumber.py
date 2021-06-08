import random


again = "yes"
while again == "yes":
    my_random_number = random.randint(1, 10)
    guess = int(input("Guess what number I'm thinking."))
    guesses = 0
    while guesses < 3:
        if guess > my_random_number:
            print(f"Too high. Guess again! You have {3- guesses} more guesses")
            guess = int(input("Guess what number I'm thinking."))
            guesses += 1
        elif guess < my_random_number:
            print(f"Too low. Guess again!. You have {3- guesses} more guesses")
            guess = int(input("Guess what number I'm thinking."))
            guesses += 1
        else:
            print("You win!")
            break
        print("Too many guesses. You lose.")
    again = input("Want to play again? yes or no")


print("Bye!")






    
    