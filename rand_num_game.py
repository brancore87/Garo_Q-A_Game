
# Exercises

# 1. Change the range to be from 0 to 1,000,000.
# 2. Can you still guess the number?
# 3. Print the number of guesses made.
# 4. Limit the number of guesses to the minimum required.
from random import randint

print("Hai Anching dakode kalna abachengna mo")

def randy():
    start = 1
    end = 20
    value = randint(start, end)

    # print(value)
    print(f"Anga chanchienga number {start} aro {end} ni gisepo...")

    guess = None

    while guess != value:
        text = input("De Masieni number ko: ")
        guess = int(text)

        if guess < value:
            print("Chukale.")
        elif guess > value:
            print("Komikale.")

    print("Congratulations! Nangni chanchia onga:", value)
    print("Mitela! ia game ko kalanina ")

