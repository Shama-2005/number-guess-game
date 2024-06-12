import random
def guess_game():
    secret_number=random.randint(1,100)
    print("welcome to the number guessing game")
    attempts=0
    while True:

        guess=int(input("enter your guess"))
        attempts +=1
        if guess<secret_number:
            print("too low")
        elif guess>secret_number:
            print("too high")
        else:
            print(f"congratulations you have guesses the secret number { secret_number}in {attempts} attempts ")
            break
guess_game()
