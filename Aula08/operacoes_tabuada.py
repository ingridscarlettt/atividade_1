def tabuada(numero, operador):
    operacao_escolhida = operador;
    numero_escolhido = numero;
    contador = 1;
    resultado = 0;
    if operacao_escolhida == '+':

        while contador <=10:
            resultado = contador + numero_escolhido;
            print(f"{contador} + {numero_escolhido} = {resultado}");
            contador +=1;

    if operacao_escolhida == '*':

        while contador<=10:
            resultado = contador * numero_escolhido;
            print(f"{contador} * {numero_escolhido} = {resultado}");
            contador +=1;

    if operacao_escolhida == '-':

        num_subtraido = numero_escolhido +1; #Ele ta fora apenas para receber o numero + 1;
        while contador <= 10: 
            resultado =  num_subtraido- numero_escolhido;
            print(f"{num_subtraido} - {numero_escolhido} = {resultado}");
            num_subtraido +=1;  # Aqui ele vai subindo o numero subtraido pelo escolhido até chegar no fim;
            contador +=1;

    if operacao_escolhida == '/':

        while contador <= 10:
            dividendo = contador * numero_escolhido; 
            resultado = dividendo / numero_escolhido;
            print(f"{dividendo:.0f} / {numero_escolhido} = {resultado:.0f}");
            contador +=1;