from rich.console import Console
import os as cmd

console = Console()

cmd.system('cls');
menu_principal = ''' 
[1] [bold red]->[/bold red] [bold blue]Criar Arquivo[/bold blue]
[2] [bold red]->[/bold red] [bold blue]Ler Arquivo[/bold blue]
[3] [bold red]->[/bold red] [bold blue]Editar Arquivo[/bold blue]
[4] [bold red]->[/bold red] [bold blue]Deletar Arquivo[/bold blue]
[5] [bold red]->[/bold red] [bold blue]Limpar Tela[/bold blue]
[6] [bold red]->[/bold red] [bold blue]Listar Diretório[/bold blue]
[7] [bold red]->[/bold red] [bold blue]Mudar Diretório[/bold blue]
[8] [bold red]->[/bold red] [bold blue]Localização Atual[/bold blue]
[0] [bold red]->[/bold red] [bold blue]Encerrar[/bold blue]
'''

menu_opcoes = ('1','2','3','4','5','6','7','8','0');
opcao_escolhida = ' ';


while opcao_escolhida != '0':
    try:
        console.input('[bold blue]-----------------DIGITE QUALQUER TECLA PARA CONTINUAR---------------[/bold blue]\n');
        console.print(menu_principal)
        opcao_escolhida = console.input("[bold blue]Informe a opção desejada:[/bold blue] ");

        if opcao_escolhida in menu_opcoes: #--------------------------CRIANDO ARQUIVO------------------------------------
            if opcao_escolhida == '1':
                cmd.system('cls');
                console.print(f'[bold green]{'#'*30} CRIANDO ARQUIVOS {'#'*30}[/bold green]');
                nome_arquivo = console.input('Informe o nome do arquivo: ');
                nome_arquivo = f'{nome_arquivo}.txt'
                
                with open(nome_arquivo,'x', encoding='utf-8') as f:
                    console.print(f'[bold green]Arquivo {nome_arquivo.upper()} criado com sucesso [/bold green]');


            elif opcao_escolhida == '2': # --------------------------LENDO ARQUIVO---------------------
                cmd.system('cls');
                console.print(f'[bold green]{'#'*30} LENDO ARQUIVOS {'#'*30}[/bold green]');
                nome_arquivo = input('Informe o nome do arquivo: ');
                nome_arquivo = f'{nome_arquivo}.txt'
                try:
                    with open(nome_arquivo,'r', encoding='utf-8') as f:
                        console.print(f'[bold green]{f.read()}[/bold green]');
                
                except FileNotFoundError:
                    console.print("[bold red]ARQUIVO NÃO ENCONTRADO [/bold red]");
            
            elif opcao_escolhida ==  '3':
                cmd.system('cls');
                console.print(f'[bold green]{'#'*30} EDITANDO ARQUIVOS {'#'*30}[/bold green]');
                nome_arquivo = input('Informe o nome do arquivo: ');
                nome_arquivo = f'{nome_arquivo}.txt'
                
                texto = input('Digite abaixo: \n');
                try:
                    with open(nome_arquivo, 'a', encoding='utf-8') as f: # o 'a' = append no arquivo, ele atualiza
                        f.write(texto)

                except FileNotFoundError:
                    console.print("[bold red]ARQUIVO NÃO ENCONTRADO [/bold red]");

            elif opcao_escolhida == '4':
                cmd.system('cls');
                console.print(f'[bold green]{'#'*30} DELETANDO O ARQUIVO {'#'*30}[/bold green]');
                nome_arquivo = input('Informe o nome do arquivo: ');
                nome_arquivo = f'{nome_arquivo}.txt'

                if cmd.path.exists(nome_arquivo):
                    cmd.remove(nome_arquivo);
                    console.print("ARQUIVO DELETADO COM SUCESSO!");
                else:
                    console.print("ARQUIVO INFORMADO NÃO EXISTE!");

            elif opcao_escolhida =='5':
                cmd.system('cls');

            elif opcao_escolhida == '6':
                cmd.system('cls')
                console.print(f'[bold green]{'#'*30} LISTANDO ARQUIVOS {'#'*30}[/bold green]');
                dir_atual = cmd.getcwd()
                console.print(f'[blue]PASTA ATUAL: [/blue][underline]{dir_atual}[/underline]');
                lista_dir_atual = cmd.listdir();
                for i in lista_dir_atual:
                    console.print(i);
                
            elif opcao_escolhida == '7':
                cmd.system('cls')
                console.print(f'[bold green]{'#'*30} ALTERANDO A PASTA ATUAL {'#'*30}[/bold green]');
                pasta_dest = cmd.chdir(console.input('[bold blue]Mudar para: [/bold blue] '));
                console.print('PASTA ATUAL:', cmd.getcwd());

        
            elif opcao_escolhida == '8':
                cmd.system('cls')
                console.print(f'[bold green]{'#'*30} LOCALIZAÇÃO ATUAL {'#'*30}[/bold green]');
                dir_atual = cmd.getcwd();
                console.print(f'[blue]DIRETÓRIO CONCORRENTE: [/blue][underline]{dir_atual}[/underline]');

        else:
            console.print('[bold red]OPÇÃO INVÁLIDA, SELECIONE UMA DAS OPÇÕES DO MENU ACIMA.[/bold red]');
    except FileExistsError:
        console.print('[bold]ERROR[/bold]: [bold red]ARQUIVO JÁ EXISTE (FileExistsError)[/bold red]');
    except FileNotFoundError:
        console.print('[bold]ERROR[/bold]: [bold red]ARQUIVO NÃO ENCONTRADO (FileNotFoundError) [/bold red]');
