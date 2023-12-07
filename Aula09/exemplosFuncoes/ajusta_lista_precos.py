
'''-------------------------Exemplo de função lambda-----------------'''
precos = [100.0, 55.8, 250, 80.5, 200]


def ajusta_preco(preco):
    return preco * 0.10 + preco;

precos_reajustados = list(map(lambda preco:preco *0.1 +preco , precos));

print(precos_reajustados);


