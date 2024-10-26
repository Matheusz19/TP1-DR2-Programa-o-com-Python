import random

def lancar_dados(num_dados):
    resultados = []
    for _ in range(num_dados):
        resultado = random.randint(1, 6)
        resultados.append(resultado)
    return resultados

num_dados = int(input("Quantos dados você deseja lançar? "))

resultados = lancar_dados(num_dados)

print("Resultados dos lançamentos dos dados:")
for i, resultado in enumerate(resultados, start=1):
    print(f"Dado {i}: {resultado}")