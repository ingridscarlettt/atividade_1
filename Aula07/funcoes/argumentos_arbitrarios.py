'''Criando uma função que recebe um número variável de argumentos a cada chamada'''

def soma(*numeros):

    soma_total= 0
    for numero in numeros:
        soma_total+= numero;
           

    return soma_total


print(soma(10,20,30,40,50,60,70,80,90,100));
print(soma(1,2,3,4,5,6));
print(soma(2,2,2,2));
print(soma(90,34,57,23));
