"""Criando uma tabuada"""

def tabuada(numero, operador):
    operacao_escolhida = operador
    numero_escolhido = numero
    contador= 1;
    resultado = 0
    if operador ==  '+':
        while contador <=10:
            resultado = contador + numero;
            print(f"{contador} + {numero} = {resultado}")
            contador +=1
    if operador == '*':
        while contador <=10:
            resultado = contador * numero;
            print(f"{contador} * {numero} = {resultado}");
            contador +=1;



print("*"*50);
print("---------TABUADA VERSÃO 2023---------");
print("*"*50);
entrada_numero = int(input("Digite um numero de 1 a 10:\n"));
entrada_operacao = input("Escolha qual operação você quer: + , - , / , *\n").replace(" ","");

tabuada(entrada_numero,entrada_operacao);
