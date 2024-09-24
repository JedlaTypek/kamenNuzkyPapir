import random

volby = ['kamen', 'nuzky', 'papir']

try_again = 'y'

while try_again == 'y' or try_again == '':
    pc = random.choice([1,2,3])

    user_input = int(input("Tvá volba [Kamen - 1, Nuzky - 2, Papir - 3]:").strip())

    if user_input > 3 or user_input < 1:
        print("Spatny input")
    else:
        print(f"Pocitac: {volby[pc-1]}")
        print(f"Hrac: {volby[user_input-1]}")

        if user_input == pc == user_input:
            print("Remiza")
        elif user_input == 1 and pc == 2:
            print("Vyhral jsi")
        elif user_input == 2 and pc == 3:
            print("Vyhral jsi")
        elif user_input == 3 and pc == 1:
            print("Vyhral jsi")
        elif user_input == 2 and pc == 1:
            print("Prohraj jsi")
        elif user_input == 3 and pc == 2:
            print("Prohral jsi")
        elif user_input == 1 and pc == 3:
            print("Prohra jsi")
    try_again = input("Chces pokracovat? [Y/n]")