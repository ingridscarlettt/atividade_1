
texto_digitado = input("Digite uma frase:\n ").replace(" ","").lower()
texto_invertido = texto_digitado[::-1];

if texto_invertido == texto_digitado:
    print("É palindromo");
else:
    print("Não é palindromo");






