min = 0
max = 1000
while True:
    guess = min + (max - min) // 2
    print(guess, flush=True)
    answer = input()
    if answer == "lower":
        max = guess
    elif answer == "higher":
        min = guess
    elif answer == "correct":
        break
    else:
        break