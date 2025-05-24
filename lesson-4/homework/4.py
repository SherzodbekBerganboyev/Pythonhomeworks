import random as r
num = r.randint(1, 100)
attemps = 0
again = True
while again:
    if attemps >= 10:
        print("Too many attempts")
        break
    guess = int(input("guess: "))
    if guess > num:
        print('Too high!')
    elif guess < num:
        print('Too low!')
    else:
        print("You guessed it right!")
        again = input("You lost. Want to play again?")
        again = (again in ["Y", "YES", "yes", "y", "ok"])
        attemps = 0
        num = r.randint(1, 100)
        continue
    attemps += 1
print("Good bye")
