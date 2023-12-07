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
soma_notas = 0;
'''--------------------------------DEFININDO A TABELA--------------------------------------------'''
tabela = Table(show_header = True, header_style= 'bold magenta' );
tabela.add_column('NOME', style='white', justify="center", width=14);
tabela.add_column('NOTAS', style='white',justify="center", width=28);
tabela.add_column('MÉDIA', style='white',justify="center", width=6);
tabela.add_column('CONDIÇÃO', style='white',justify="center", width=16);

'''--------------------------------Entrada de dados aqui-----------------------------------------------'''
while falso_verdade == True:
    dic_aluno['nome'] = input("Informe o nome do aluno(a): ").strip().title();

    for i in range(1,5):
        nota = float(input(f"{i}ª nota: "));
        soma_notas +=nota;
        notas.append(nota);
    
    media_final = soma_notas/4;
    dic_aluno['notas'] = notas
    lista_alunos.append(dic_aluno);

    if media_final >= 7:
        status = '[bold green]Aprovado(a)[/bold green]'

    elif media_final <7 and media_final >=4:
        status =  '[bold yellow]Em Recuperação[/bold yellow]'

    else:
        status = '[bold red]Reprovado(a)[/bold red]'

    formata_notas = ' | '.join(map(str,dic_aluno['notas']))

# '''----------------------------------Saida de dados abaixo----------------------------------- '''

    tabela.add_row(dic_aluno['nome'], formata_notas, str(media_final), status);

    dic_aluno = dict();
    notas = list();
    soma_notas = 0.0
    
    c+=1
    decisao_user = console.input("[bold red]Deseja continuar cadastrando alunos ([bold green]S[/bold green]/N[/bold red])?: ").upper().replace(' ','');
    if decisao_user == 'N':
        falso_verdade = False
cmd.system('cls');

console.print(tabela)


