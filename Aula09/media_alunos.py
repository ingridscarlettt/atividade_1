#Crire um script em python para manter a média de um grupo de alunos
#O script recebe o nome do aluno e quatro notas. Estes dados devem
# ser mantido numa lista e não há limite para o número de aluno.
# Ao final da execução deverá ser gerado um relatório com o nome de
# cada aluno, suas respectivas notas, a media de 4 notas e o status. O status
# deverá seguir a seguinte regra:
#  Provado: maior ou igual a 7
#  Reprovado: média menor de 4
#  Em Recuperação: média maior ou igual a 4 e menor que 7

import os as cmd;

from rich.console import Console
from rich.table import  Table
tabela = Table()

console = Console();
cmd.system('cls')


c = 1
lista_alunos = list()
notas = list()
dic_aluno = dict()
falso_verdade = True

'''Entrada de dados aqui'''
while falso_verdade == True:
    dic_aluno['nome'] = input("Informe o nome do aluno(a): ").strip().title();

    for i in range(1,5):
        nota = input(f"{i}ª nota: ");
        if nota.isdigit():
            nota = float(nota)
            notas.append(nota);

    dic_aluno['notas'] = notas
    lista_alunos.append(dic_aluno);
    
    dic_aluno = dict();
    notas = list();
    
    c+=1
    escolha = input('deseja continuar?\n ');
    if escolha == 'n':
        falso_verdade = False;
cmd.system('cls');

'''Saida de dados abaixo '''

soma_notas = 0;
for dic_aluno in lista_alunos:
    print(f'Nome do Aluno(a): {dic_aluno.get('nome')}');
    print('Notas: ',end='')

    for nota in dic_aluno.get('notas'):
        print(nota , end=' ');
        soma_notas +=nota

    print(f'\nMédia: {(soma_notas/4):.2f}');
    media_final = soma_notas/4
    if media_final >= 7:
        status = 'Aprovado(a)'

    elif media_final <7 and media_final >=4:
        status = 'Em Recuperação'

    else:
        status = 'Reprovado(a)'

    print('Condição:',status);
    soma_notas = 0
    print('')

print(f"Totais de alunos cadastrados foi de: {len(lista_alunos)}");