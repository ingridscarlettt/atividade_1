'''Possibilitando a interação do usuário via terminal de comandos'''

print("    DESCOBRINDO SE O NÚMERO É PAR OU IMPAR   ");
print("-"*50);
par_Impar = int(input("Digite um numero:"));

while par_Impar<0:
    print("Por favor digite um número positivo");
    par_Impar = int(input("Digite um numero:"));
    continue;
if par_Impar == 0:
    print("Numero digitado foi 0");

elif par_Impar%2==0:
    print(f"Numero digitado {par_Impar} é um número par");

else:
    print(f"Numero digitado {par_Impar} é  um número impar");

