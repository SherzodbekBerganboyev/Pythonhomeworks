def invest(amount, rate, years):
    for i in range(1, years+1):
        amount = float(format(amount*(1+rate), '.2f'))
        print(f'year {i}: $', amount)

invest(100, .05, 4)