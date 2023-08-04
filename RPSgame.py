import random

random.seed()

choices = ["Rock", "Paper", "Scissors"]

while(True):

    computer_choice = random.randint(0, 2)
    user_choice = int(input("Choose an option:\n1. Rock\n2. Paper\n3. Scissors\n4. Exit\n: "))
    if(user_choice == 4):
        break
    user_choice = user_choice - 1

    print("\nComputer choice: " + choices[computer_choice])

    if(computer_choice == user_choice):
        print("Draw.\n")
    elif(computer_choice == (user_choice + 1) % len(choices)):
        print("Computer wins.\n")    
    else:
        print("User wins.\n")
       
print("\nThanks for playing.\n")