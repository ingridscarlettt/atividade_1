#------------------------------------------------FILTRA NOTAS--------------------------------------------------------

notas = [10,5.5,9,7.3,8.5,5.4,4.3,2.5,1.6];


aprovados = list(filter(lambda nota: nota >= 7, notas)); #filtra apenas aquilo que esta descrito, no caso ali ele filtrou apenas para notas maior que 7
print(aprovados)

reprovados = list(filter(lambda notas: notas <7, notas));

print(reprovados)