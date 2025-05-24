from random import choice

print("Rock(r), Paper(p), Scissors(s)")
c_user = c_cpu = 0
wins = {
    'r' : 's',
    's' : 'p',
    'p' : 'r'
}
characters = {
    'r' : 'rock',
    'p' : 'paper',
    's' : 'scissors'
}
while True:
    cpu = choice(['r', 'p', 's'])
    user = input("choice r/p/s : ")
    print("---------------")
    print("You: {}  ||  Cpu : {}".format(characters[user], characters[cpu]))
    if user != cpu:
        if wins[user] == cpu:
            print("You win")
            c_user += 1
        else:
            print("You lose")
            c_cpu += 1
    else:
        print("Draw")
    print(f"Scores: you: {c_user} || cpu : {c_cpu}")
    if max(c_cpu, c_user) >= 5:
        if c_cpu >= 5:
            print("Cpu is winner")
        else:
            print("Ypu winner")
        break