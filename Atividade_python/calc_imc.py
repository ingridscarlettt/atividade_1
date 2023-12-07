
altura = float(input("Digite sua altura, por favor: "));
peso = float(input("Digite seu peso, por favor: "));

resul_imc = peso/(altura * altura);
if resul_imc <= 17:
    print(f"Você esta muito abaixo do peso com {resul_imc:.2f} de IMC");

elif resul_imc >=40:
    print(f"Você esta com Obesidade grau III(Morbida) com {resul_imc:.2f}");

elif resul_imc>= 17 and resul_imc <=18.49:
    print(f"Abaixo do peso com {resul_imc:.2f} de IMC");

elif resul_imc>=18.5 and resul_imc<=24.99:
    print(f"Você esta com o peso normal com {resul_imc:.2f} de IMC");

elif resul_imc>=25 and resul_imc<=29.99:
    print(f"Você esta acima do peso com {resul_imc:.2f} de IMC");

elif resul_imc>=30 and resul_imc <=34.99:
    print(f"Você esta com Obesidade grau I com {resul_imc:.2f} de IMC");

elif resul_imc>=35 and resul_imc <=39.99:
    print(f"Você esta com Obesidade grau II(Severa) com {resul_imc:.2f} de IMC")

