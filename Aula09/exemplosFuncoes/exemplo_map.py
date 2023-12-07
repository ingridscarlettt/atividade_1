notas = [10,10,10,9.5] #Lista de números
print(notas);



#A função map(), junto com a função str(), transforma todos
# os itens da lista em strings

notas_strings = map(str,notas);

print(notas_strings,type(notas_strings),'----1');


#Transforma um objeto map em uma lista(list)
notas_strings = list(notas_strings);
print(notas_strings,type(notas_strings), '----2')

#Pega todos os elementos da lista de strings e transforma em
# Uma string, somando com um espaço em branco.


notas_strings = ' '.join(notas_strings);
print(notas_strings,type(notas_strings), '----3')

