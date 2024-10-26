def calcular(operacao, num1, num2):
    if operacao == '1':
        return num1 + num2
    elif operacao == '2':
        return num1 - num2
    elif operacao == '3':
        return num1 * num2
    elif operacao == '4':
        return num1 / num2 if num2 != 0 else "Erro:Divisão por zero"
    else:
        return "Operação inválida."

print("Escolha uma operação:")
print("1.Adição")
print("2.Subtração")
print("3.Multiplicação")
print("4.Divisão")

operacao = input("Digite o número da operação desejada.")
num1 = float(input("Digite o primeiro número."))
num2 = float(input("Digite o segundo número."))

resultado = calcular(operacao, num1, num2)
print("Resultado:", resultado)
