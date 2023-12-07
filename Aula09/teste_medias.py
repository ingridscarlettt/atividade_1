import os as cmd;

from rich.console import Console
console = Console();

cmd.system('cls');

notinhas = []
alunos_notas = {}

nome_aluno = input("Digite o nome do aluno: ")
for i in range(1,5):
    notas_digitadas = float(input(f"digite a {i}ª nota: "));
    notinhas.append(notas_digitadas);

alunos_notas.update({nome_aluno:notinhas});

# print(alunos_notas)

# for aluno, notas in alunos_notas.items():
#     notas_formatadas = ", ".join(map(str, notas));

# print(f"{aluno}: {notas_formatadas}")

queroaqui = []
for media in alunos_notas.values():
    for n in media:
        queroaqui.append(n)
    

resultado = sum(queroaqui)/len(queroaqui);
print(resultado)