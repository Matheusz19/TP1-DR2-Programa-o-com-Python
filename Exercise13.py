def e_palindromo(texto):
    texto_limpo = ''.join(texto.split()).lower()
    return texto_limpo == texto_limpo[::-1]

entrada = input("Digite uma palavra ou frase:")

if e_palindromo(entrada):
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")