#---------------------------UTILIZANDO MÉTODO REDUCE---------------------------

from functools import reduce

notas = [10,5.5,9,7.3,8.5,5.4,4.3,2.5,1.6];

soma_notas = reduce(lambda n1,n2: n1 + n2,  notas);

print(f'{soma_notas:.2f}') # -----ISSO FUNCIONA PORQUE O REDUCE RETORNAR APENAS UM VALOR NO FIM

