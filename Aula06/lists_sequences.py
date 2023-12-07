# lista_frutas = ["Morango", "Uva","Laranja", "Maracujá","Banana"];

# lista_frutas.append("Abacaxi");
# lista_frutas.insert(2,"Macã");

# for fruta in lista_frutas:
#     print(fruta,end=" ");

# print("\n");
# print("*"*100);
# print(lista_frutas[2]); #Imprimindo na tela apenas um indice da lista

# lista_arbritararia = ["Maria",45,[12.10 ,8,True],True];

# for lista in lista_arbritararia:
#     print(lista, end= ' ');

# print("");
# print(lista_arbritararia[2][0]);
# print("*"*100);

# for lista_dentro in lista_arbritararia[2]:
#     print(lista_dentro, end= ' ');


alunos = [
    'Fernanda Silva',
    'Bruno Souza',
    'Renata Campos',
    'Marta Guedes',
    'Carlos Vinhote'
]
# for aluno in alunos:
#     print(aluno);

# print(" ");

notas =[
    [10,10,10,9.5],
    [8.5,9,9.3,8.7],
    [10,5,3,7],
    [3,7,8,10],
    [10,3,6,3]
]
i = 0

for aluno in alunos:
    nota_aluno = notas[i];
    print(aluno, end=' ');

    for n in nota_aluno:
        print ((n), end=' ');
    
    i +=1;
    print()
'''Explicando o exercicio acima: foi criada a auxiliar (i) para receber 0, nela é salvo as posições da lista de notas, ai fica somando, pra ele pegar cada conjunto de notas
 basicamente faz isso
 aluno 1 recebe as 4 primeiras nota
 aluno 2 recebe as 4 segundas notas
 aluno 3 recebe as 4 terceiras notas
 e assim vai até acabar

'''