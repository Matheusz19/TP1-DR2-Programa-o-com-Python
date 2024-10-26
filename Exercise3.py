def combinar_nomes(nome1, nome2):
    meio1 = len(nome1) // 2
    meio2 = len(nome2) // 2
    
    nome_combinado = nome1[:meio1] + nome2[meio2:]
    
    return nome_combinado

nome1 = input("Digite o primeiro nome de usuário: ")
nome2 = input("Digite o segundo nome de usuário: ")

novo_nome = combinar_nomes(nome1, nome2)

print(novo_nome)
