
# texto = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec pulvinar pellentesque tellus. Nunc malesuada tincidunt metus id elementum. Vestibulum porttitor luctus ante non 
# aliquam. Integer finibus efficitur tellus, sit amet venenatis odio vehicula vitae. Fusce ultrices tempus risus, id pulvinar ante ornare non. Maecenas eget tempus libero, molestie 
# congue metus. Morbi urna ante, dictum quis massa et, elementum volutpat felis. Praesent eu consequat arcu. Integer posuere orci vel libero pulvinar, non consectetur nisl efficitur. 
# Quisque tempor, arcu eget mattis efficitur, sem orci gravida metus, eu imperdiet lectus eros sed eros. Ut ut turpis vestibulum, congue orci et, lacinia libero."""

# texto2 = '''Vivamus sapien erat, euismod ac sapien in, egestas efficitur urna. Nulla massa orci, rhoncus id maximus id, pellentesque non odio. Donec porttitor nisl ipsum, eu venenatis 
# tellus condimentum a. Mauris ac ante erat. Suspendisse tempor nec lectus sit amet mollis. Mauris luctus eget nisl et aliquet. Donec viverra elementum ex quis sodales. Donec magna 
# tellus, tempus eget ornare non, euismod quis velit. Phasellus vitae suscipit lorem. Nullam molestie maximus dolor a faucibus. Nulla metus nisi, varius eu elit sed, vestibulum 
# tincidunt sapien. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. In venenatis neque id nulla finibus mattis. Donec odio ipsum, dictum a 
# mattis convallis, mollis et nulla. Vestibulum viverra risus vel orci porta, sit amet sollicitudin diam congue. Morbi imperdiet tellus a libero scelerisque consequat.'''

# texto3 = "'Vivamus sapien erat, euismod ac sapien in, egestas efficitur urna. Nulla massa orci, rhoncus id maximus \
# id, pellentesque non odio. Donec porttitor nisl ipsum, eu venenatis" 
# -------------------------------------------------------------------Exemplo de como utilizar -------------------------------------------------------------------------




# mensagem = '           Python é "fácil" de aprender                 ';
# print(f"Tamanho com os espaços - {len(mensagem)}");
# mensagem = mensagem.strip();
# print(mensagem[10:15]);
# print(f"Tamanho sem os espaços - {len(mensagem)}");
# print(mensagem);

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------
# senac = "Serviço Nacional de Aprendizagem Comercial"
# print(senac); """Aqui sai de acordo com o que digitei"""
# senac = senac.lower();
# print(senac); """ Aqui vai sair tudo minusculo"""
# senac = senac.upper();
# print(senac); """aqui vai sair tudo maiusculo"""

# print("teste desse aqui ----------",senac.capitalize());
# print("Esse aqui faz cada palavra da frase ficar com a primeira letra maiuscula---", senac.title());

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

# msg = "Ceja Bem vindo ao Cenac!"

# msg = msg.title()
# msg = msg.replace("C", "S");
# print(msg);

senac = "Serviço Nacional de Aprendizagem Comercial"

senac = senac.split();

print(senac)
print(type(senac));

for item_Lista in senac:
    print(item_Lista, end = ' '); # com o End ai, imprime tudo na mesma linha.