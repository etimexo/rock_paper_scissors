import random as ran
options = ["rock", "paper", "scissors"]
r = options[0]
p = options[1]
s = options[2]

while True:
    # print(system)
    print("NOTE: r represents rock, p represents paper and s represents scissors.")
    system = ran.choice(options)
    user = input("Rock Paper Scissors: ").lower()
    print("system chose: " + system)
    if user == system:
        print("It's a tie, go again!")
    elif (user == "r" and system == "scissors") or (user == "p" and system == "rock") or (user == "s" and system == "paper"):
        print("You win!")
    else: 
        print("You lose!")
        
    play_again = input("Do you want to play again? (y/n) ").lower()
    if play_again != "y":
        print('Goodbye!')
        break
