
print("----------CONVERTENDO TEMPERATURA---------");
print("1 - Celsius para Fahrenheit");
print("2 - Faherenheit para Celsius");
converte_escolha =int(input("Digite qual conversão quer fazer:(1) ou (2)\n"));

if converte_escolha == 1:
    temp_celsius = float(input("Digite a temperatura em Celsius: "));
    temp_fahren = (temp_celsius * 1.8)+32;
    print(f"A temperatura de {temp_celsius:.1f} graus em Fahrenheit é de {temp_fahren:.1f}");

if converte_escolha == 2:
    temp_fahren = float(input("Digite a temperatura em Fahrenheit: "));
    temp_celsius = (temp_fahren-32)/1.8
    print(f"A temperatura de {temp_fahren:.1f} Fahrenheit em Celsius é de {temp_celsius:.1f} graus");