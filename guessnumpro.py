import random

secret_number = random.randint(1, 50)
print("\nI have chosen a number between 1 and 50. You have 5 tries to guess it!")

while True:
    attempts = 5

    while attempts > 0:
        user_input = input("Enter your guess: ")

        if not user_input.isdigit():
          print("Invalid input! Please enter a number.")
          continue

        user_input = int(user_input)
    
        if user_input == secret_number:
            print("✅Awesome! It's correct. :3")
        
            # Ask the user if they want to continue
            choice = input("Do you want to continue? (yes/no): ").lower()
            if choice == "yes":
               print("Great! Let's play again.")
               secret_number = random.randint(1, 50)
               attempts = 5
            elif choice == "no":
               print("Game over, !")
               exit()
        
        elif user_input > secret_number:
           print("Too high! Try again.")

        else:
           print("Too low! try again.")

        attempts -= 1
        print(f"You have {attempts} attempts left.")

# Step 11: If out of attempts, reveal the correct number
    
    if attempts == 0:
        print(f"The correct number was {secret_number}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
    
        if play_again == "yes":
         print("Restarting game... 🎮")
         secret_number = random.randint(1, 50)  # ✅ Picks a new random number
         attempts = 5  # ✅ Reset attempts to 5
    
        else:
         print("Thanks for playing! 👋")   
         break
    
