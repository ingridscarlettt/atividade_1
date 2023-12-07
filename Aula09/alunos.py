'''teste do script de gerenciamento de alunos com dict'''


# alunos = {
#     'Maria Fernanda':[10,5.5,9,7.3],
#     'José Almeida': [10,5,3,5.5]

# }
# print(alunos['Maria Fernanda'][1]);
aluno1 ={
    'nome': 'Maria Fernanda',
    'idade': 24,
    'curso': 'Matemática',
    'notas': [10,5.5,9,7.3] 

}
aluno2 = {
    'nome': 'José Almeida',
    'idade': 30,
    'curso': 'Português',
    'notas': [10,10,10,10] 
}   

alunos = [aluno1,aluno2];


# print(aluno1.keys(), '\n', aluno1.values());


for i, j in aluno1.items():
    print(f"{i}: {j}")