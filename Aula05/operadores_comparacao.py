# """Operador de igualdade(==)"""
# print("Operador de igualdade(==)");
# print("10 é igual a 11?:",10== 11);
# print("10 é igual a 10?:",10== 10);

# print("\n","-"*30);
# '''Operador de diferente (!=)'''
# print('Operador de diferente (!=)');
# print("10 é diferente de 11?:", 10 != 11);
# print("10 é diferente de 10?:", 10 != 10);

# print("\n","-"*30);

# '''Operador de maior que (>)'''
# print("Operador maior que(>):");
# print("10 é maior que 11?:", 10>11);
# print("10 é maior que 9?:", 10>9);

# print("\n","-"*30);

# '''Operador de menor que (<)'''
# print("Operador de menor que(<)");
# print("10 é menor que 11?:", 10<11);
# print("10 é menor que 9?:", 10<9);

# print("\n","-"*30);

# '''Operador de maior ou igual a que (>=)'''
# print("Operador de maior ou igual a que (>=)");
# print("10 é maior ou igual a que 11?:", 10>=11);
# print("10 é maior ou igual a que 9?:", 10>=9);

# print("\n","-"*30);


# '''Operador de menor ou igual a que (<=)'''
# print("Operador de menor ou igual a que (<=)");
# print("10 é menor ou igual a que 11?:", 10<=11);
# print("10 é menor ou igual a que 9?:", 10<=9);

# print("\n","-"*30);

# idade = int(input("Informe sua idade:"));

# if idade >= 18:
#     print("Maior de idade");

# else:
#     print("Menor de idade");


'''Critérios para participar do campeonato
    1) Ter idade maior que quinze anos
    2) Ter altura maior ou igual a 1.70'''


idade = int(input("Digite sua idade:"));
altura = float(input("Digite sua altura:"));
aluno_colegio = input("É aluno do colégio? (SIM | NÃO)\n");

if idade<0 or idade> 100:
    print("Idade digitada é inválida");

if altura < 1 or altura > 2.5:
    print("Altura digitada é inválida");

elif (idade >=15 and altura>= 1.70) and aluno_colegio.lower() == 'sim':
    print("Parabéns, pode participar do campeonato");

else:
    print("Você não pode participar do campeonato"); 
