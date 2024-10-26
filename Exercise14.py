votos = {
    "Opção 1": 0,
    "Opção 2": 0,
    "Opção 3": 0
}

def exibir_opcoes():
    print("Por favor, vote em uma das seguintes opções:")
    for opcao in votos.keys():
        print(opcao)

def coletar_votos(num_votantes):
    for i in range(num_votantes):
        exibir_opcoes()
        voto = input(f"Votante {i + 1}, digite sua opção (1, 2 ou 3): ")

        if voto == '1':
            votos["Opção 1"] += 1
        elif voto == '2':
            votos["Opção 2"] += 1
        elif voto == '3':
            votos["Opção 3"] += 1
        else:
            print("Voto inválido. Tente novamente.")

num_votantes = int(input("Digite o número de votantes:"))

coletar_votos(num_votantes)

print("\nResultados da votação:")
for opcao, contagem in votos.items():
    print(f"{opcao}: {contagem} votos")