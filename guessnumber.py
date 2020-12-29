import random as rd

def playGame():
    rdm = rd.randint(1, 100)
    print("Guess the number between 1 and 100..")
    while True:
        guess = int(input())
        if guess > rdm:
            print("Too High")
        elif guess < rdm:
            print("Too Low")
        else:
            print("Congrats!, You guessed the number...")
            playAgain()



def playAgain():
    print("Do you want to play again? Y/N")
    opt = input()
    if opt == 'Y':
        playGame()
    else:
        print("Thank You! for playing this game..")
