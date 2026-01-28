# A linha abaixo cria um objeto que representa o arquivo.
# Ele está sendo aberto no modo de leitura, usando a codificação UTF-8
with open("testando.txt", "r", encoding="utf-8") as arquivo:
    # A instrução .read() lê o conteúdo em formato de string.
    conteudo = arquivo.read()
# A linha abaixo exibe o conteúdo que foi lido.
print(conteudo)
