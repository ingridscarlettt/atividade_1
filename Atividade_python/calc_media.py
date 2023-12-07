notas_alunos=[
    [10,10,10,10],
    [9,9,9,9],
    [8,8,8,8],
    [7,7,7,7],
    [8,8,8,8]
]
i= 0
media_notas= []

for nota in notas_alunos:
    for n in nota:
        print(n,end=" ");
    media_notas = sum(notas_alunos[i])/len(notas_alunos[i]);
    print(f"- a media foi de {media_notas:.1f}");
    i+=1;
    print()
