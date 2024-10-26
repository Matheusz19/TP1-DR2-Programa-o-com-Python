import random

numero_secreto = random.randint(1, 50)

print("Tente adivinhar o número secreto (entre 1 e 50)")

while True:
    palpite = int(input("Digite seu palpite:"))
    if palpite == numero_secreto:
        print("ACERTOU")
        break
    elif palpite < numero_secreto:
        print("Mais alto.")
    else:
        print("Mais baixo.")