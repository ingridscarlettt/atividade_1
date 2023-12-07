import os

x, y, z, a = "Goiaba", "Melão", "Abacate", 100;

print(f"{x}\n{y}\n{z}\n{a}\n");

x = y = z = "melão";

print(x,y,z);

os.system('cls');

print("-"*50);
print("Digite o número  da opção desejada:");
print("1 - Inserir dados na lista.");
print("2 - Ler a lista completa.");
print("3 - Sair do programa.");
print("-"*50);
opcao_decidida = int(input());

if opcao_decidida <1 or opcao_decidida >3: 
    print("Por favor digite uma opção válida")

elif opcao_decidida == 3:
    os.system('cls');
    print("Programa encerrado, obrigado!");







