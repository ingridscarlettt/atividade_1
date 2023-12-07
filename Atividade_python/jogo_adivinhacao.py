import random;

num_aleatorio = random.randint(1,10)
print("-------JOGO DE ADVINHAÇÃO------");
print("Um numero de 1 até 10 foi sorteado, tente descobrir qual é");
tentativa_num = int(input("Digite um numero de 0 a 10: "));

while tentativa_num != num_aleatorio:
    if tentativa_num > num_aleatorio:
        print("Numero sorteado é menor ");
        tentativa_num = int(input("Digite um numero de 0 a 10: "));
        continue;
    elif tentativa_num < num_aleatorio:
        print("Numero sorteado é maior ");
        tentativa_num = int(input("Digite um numero de 0 a 10: "));
        continue;

if num_aleatorio == tentativa_num:
    print("Parabéns, você acertou o número sorteado:",num_aleatorio);