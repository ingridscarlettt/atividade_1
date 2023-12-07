texto_digitado= input("Digite uma frase: ").replace(" ","").lower();

cont_vogais = 0;

for i in texto_digitado:
    if i in 'aeiou':
        cont_vogais+=1;

print(cont_vogais);