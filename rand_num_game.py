
from random import randint

print("\n\t(Computer)>> Hai Anching dakode kalna abachengna mo")

def randy():
    start = 1
    end = 20
    value = randint(start, end)

    # print(value)
    print(f"\n\t(Computer)>> Anga chanchienga number {start} aro {end} ni gisepo...")

    guess = None

    while guess != value:
        text = input("\n\t(Computer)>> De Na'a Masieni number ko: ")
        guess = int(text)

        if guess < value:
            print("Chukale.")
        elif guess > value:
            print("Komikale.")

    print("\n\t(Computer)>> Congratulations! Nangni chanchia onga:", value)
    print("\n\t(Computer)> >Mitela! ia game ko kalanina ")

