def minutos_para_horas(minutos):
    horas = minutos // 60
    minutos_restantes = minutos % 60
    return horas, minutos_restantes

def horas_para_minutos(horas, minutos):
    total_minutos = (horas * 60) + minutos
    return total_minutos

print("Escolha.")
print("1. Converter minutos para horas e minutos")
print("2. Converter horas e minutos para minutos")

opcao = input("Digite 1 ou 2: ")

if opcao == '1':
    minutos = int(input("Digite os minutos."))
    horas, minutos_restantes = minutos_para_horas(minutos)
    print(f"{minutos} minutos é igual a {horas} horas e {minutos_restantes} minutos.")
    
elif opcao == '2':
    horas = int(input("Digite o número de horas. (os minutos será na próxima pergunta.)"))
    minutos = int(input("Digite o número de minutos."))
    total_minutos = horas_para_minutos(horas, minutos)
    print(f"{horas} horas e {minutos} minutos é igual a {total_minutos} minutos.")
    
else:
    print("Opção inválida. Por favor, digite 1 ou 2.")