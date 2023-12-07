'''CRIANDO UMA TABUADA'''
import os as cmd
cmd.system('cls');

from rich.console import Console
console = Console()

import entrada_tabuada as enter



print("*"*50);
print("---------TABUADA VERSÃO 2023----------");
print("*"*50);

primeira_entrada = input("Digite qualquer tecla para começar ");
enter.entrada_tabuada(primeira_entrada);
verdade_falso = True;

while verdade_falso == True:
    continua_entrada = console.input("Deseja continuar, [bold green]S[/bold green]/[bold red]N[/bold red]? ").replace(" ","").upper();

    if continua_entrada == 'N':
        verdade_falso = False;
        cmd.system('cls');
        console.print("[bold green]Obrigado por usar a Tabuada![/bold green]");

    elif continua_entrada != 'S':
        console.print("[bold red]Entrada incorreta, por favor apenas [bold green]S[/bold green] ou N[/bold red]");
    else:
        enter.entrada_tabuada(continua_entrada)
