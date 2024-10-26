def calcular_desconto(valor_compra):
    if valor_compra > 500:
        desconto = 0.25
    elif valor_compra > 200:
        desconto = 0.15
    elif valor_compra > 100:
        desconto = 0.10
    else:
        desconto = 0.0

    return valor_compra * desconto

valor_compra = float(input("Digite o valor da compra:R$ "))

desconto = calcular_desconto(valor_compra)

valor_final = valor_compra - desconto

print(f"Valor da compra:R$ {valor_compra:.2f}")
print(f"Desconto aplicado:R$ {desconto:.2f}")
print(f"Valor final a pagar:R$ {valor_final:.2f}")