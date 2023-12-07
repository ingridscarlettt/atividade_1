import os as cmd
cmd.system('cls');

from rich.console import Console
console = Console()

import operacoes_tabuada as op

def entrada_tabuada(escolha):
    while True:
        entrada_numero= input("Digite um número de 1 a 10: ")
        if entrada_numero.isdigit(): # além da função isdigit(), tem também a função isaplha() para verificar se foi letra o que foi digitado.
            recebe_inteiro = int(entrada_numero)
            if recebe_inteiro >=1 and recebe_inteiro <=10:
                break
            else:
                console.print("[bold red] Por favor digite um número apenas dentro do intervalo de [bold yellow]1[/bold yellow] até [bold yellow]10[/bold yellow]:[/bold red] ");
        else:
            console.print("[bold red]Isso não é um número, digite novamente, por favor números de [bold yellow]1 a 10[/bold yellow]:[/bold red] ");


    entrada_numero = recebe_inteiro; # Aqui recebe inteiro após o usuário digitar corretamente

    entrada_operacao = input("Escolha qual operação você quer (+, -, *, /): ").replace(" ","");

    while entrada_operacao != '+' and entrada_operacao != '-' and entrada_operacao != '/' and entrada_operacao != '*': # Aqui ele verifica se o que foi digitado é diferente de tudo isso ai, se for, então executa  a linha, senão ele executa o codigo normalmente
        entrada_operacao = console.input("[bold red]Você digitou incorretamente, por favor digite a operação correta ao lado que você quer: (+, -, *, /)[/bold red]: ").replace(" ","");
        continue
    
    op.tabuada(entrada_numero,entrada_operacao); #No fim chama a função